"""Shared fixtures for the night-audit and scheduled-audit unit tests.

Several of the routines under test call ``frappe.db.commit()`` themselves
(the night audit, the retention purges). IntegrationTestCase only rolls back
once per class, so ``AuditTestCase`` gives every test its own savepoint,
turns commits into no-ops while the test runs and rolls back to the
savepoint afterwards. Nothing a test writes survives it.

Dates are pinned: ``TODAY`` is a fixed calendar day far from any seeded data,
and the tests patch ``nowdate`` where each module imports it rather than
depending on the wall clock.
"""

from __future__ import annotations

from contextlib import ExitStack
from unittest.mock import patch

import frappe
from frappe.tests import IntegrationTestCase
from frappe.utils import add_days

# a Wednesday, years away from anything a seeded site holds
TODAY = "2031-03-12"
YESTERDAY = add_days(TODAY, -1)

PROP_A = "UT Audit A"
PROP_B = "UT Audit B"

SAVEPOINT = "kamra_ut_audit"


def d(offset: int) -> str:
	"""TODAY shifted by `offset` days, as a string."""
	return str(add_days(TODAY, offset))


def ensure_role(role: str) -> None:
	if not frappe.db.exists("Role", role):
		frappe.get_doc({"doctype": "Role", "role_name": role,
		                "desk_access": 0}).insert(ignore_permissions=True)


def ensure_user(email: str, roles: list[str]) -> str:
	for r in roles:
		ensure_role(r)
	if not frappe.db.exists("User", email):
		frappe.get_doc({
			"doctype": "User", "email": email, "first_name": email.split("@")[0],
			"enabled": 1, "user_type": "System User", "send_welcome_email": 0,
			"roles": [{"role": r} for r in roles],
		}).insert(ignore_permissions=True)
	else:
		user = frappe.get_doc("User", email)
		have = {r.role for r in user.roles}
		extra = [r for r in have if r not in roles and r not in
		         ("All", "Guest", "Desk User")]
		if extra:
			user.remove_roles(*extra)
		missing = [r for r in roles if r not in have]
		if missing:
			user.add_roles(*missing)
	frappe.clear_cache(user=email)
	return email


def make_property(name: str, **fields) -> str:
	"""A bare property, put back to these exact values if it exists."""
	payload = {
		"property_name": name, "city": "Testville", "state": "Karnataka",
		"gst_mode": "Fixed", "no_show_charge": "None", "business_date": None,
		"disabled": 0, "rates_include_tax": 0, "room_levy_percent": 0,
		"require_cashier_pin": 0, "guest_retention_months": 0,
		"message_retention_days": 0, "security_deposit_amount": 0,
		# no-show policy at its defaults; the policy tests change it
		"no_show_timing": "At audit for arrival date",
		"protect_late_arrivals": 1, "waive_no_show_fee_for_ota": 1,
		"non_guaranteed_release_time": None, "timezone": None,
		"default_company_billing": "Room and F&B (liquor to guest)",
	}
	payload.update(fields)
	if frappe.db.exists("Property", name):
		doc = frappe.get_doc("Property", name)
		doc.update({k: v for k, v in payload.items() if doc.meta.has_field(k)
		            or k == "property_name"})
		doc.save(ignore_permissions=True)
	else:
		doc = frappe.get_doc({"doctype": "Property",
		                      **{k: v for k, v in payload.items()
		                         if k == "property_name"
		                         or frappe.get_meta("Property").has_field(k)}})
		doc.insert(ignore_permissions=True)
	frappe.clear_document_cache("Property", name)
	return doc.name


def make_room_type(prop: str, code: str = "STD", base_price: float = 1000,
                   **fields) -> str:
	existing = frappe.db.get_value("Room Type", {"property": prop,
	                                             "room_type_code": code})
	if existing:
		return existing
	return frappe.get_doc({
		"doctype": "Room Type", "property": prop, "room_type_code": code,
		"room_type_name": f"UT {code}", "base_price": base_price,
		"adults_capacity": 3, **fields,
	}).insert(ignore_permissions=True).name


def make_room(prop: str, room_type: str, number: str) -> str:
	existing = frappe.db.get_value("Room", {"property": prop,
	                                        "room_number": number})
	if existing:
		return existing
	return frappe.get_doc({
		"doctype": "Room", "property": prop, "room_type": room_type,
		"room_number": number,
	}).insert(ignore_permissions=True).name


def make_guest(first: str = "UT Guest", **fields) -> str:
	return frappe.get_doc({"doctype": "Guest", "first_name": first,
	                       **fields}).insert(ignore_permissions=True).name


def make_reservation(prop: str, room_type: str, check_in: str, check_out: str,
                     status: str = "Confirmed", room: str | None = None,
                     guest: str | None = None, **fields):
	"""A stay with any dates: past check-ins are what the audit works on,
	so the past-date guard is waived the way imports and walk-ins waive it."""
	doc = frappe.get_doc({
		"doctype": "Reservation", "property": prop, "room_type": room_type,
		"guest": guest or make_guest(), "status": status, "room": room,
		"check_in_date": check_in, "check_out_date": check_out,
		"adults": 2, "children": 0, **fields,
	})
	doc.flags.allow_past_check_in = True
	if status == "Checked In":
		# check in the way the desk does - Confirmed, then the status change
		# fires handle_check_in (room occupied, guest folio opened)
		doc.status = "Confirmed"
		doc.insert(ignore_permissions=True)
		doc.status = "Checked In"
		doc.save(ignore_permissions=True)
		return doc
	doc.insert(ignore_permissions=True)
	return doc


def guest_folio(reservation: str) -> str | None:
	return frappe.db.get_value("Folio", {"reservation": reservation,
	                                     "folio_type": "Guest"})


def charges(reservation: str, charge_type: str | None = None) -> list:
	filters = {"reservation": reservation}
	if charge_type:
		filters["charge_type"] = charge_type
	return frappe.get_all("Folio Charge", filters=filters,
	                      fields=["charge_type", "posting_date", "amount",
	                              "description", "parent"])


class AuditTestCase(IntegrationTestCase):
	"""Per-test isolation for code that commits.

	Subclasses list the properties they touch in ``properties`` so their
	cached documents are dropped after the rollback (the cache lives in
	redis, outside the transaction)."""

	properties: tuple = (PROP_A, PROP_B)

	def setUp(self):
		super().setUp()
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- test fixture
		self._stack = ExitStack()
		# commits inside the code under test would end the savepoint and
		# leak rows into the site; turn them into no-ops for the test
		self._stack.enter_context(patch.object(frappe.local.db, "commit"))
		self._lang = getattr(frappe.local, "lang", None)
		frappe.db.savepoint(SAVEPOINT)

	def tearDown(self):
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- test fixture teardown
		frappe.db.rollback(save_point=SAVEPOINT)
		self._stack.close()
		frappe.local.lang = self._lang
		for p in self.properties:
			frappe.clear_document_cache("Property", p)
		super().tearDown()

	def at(self, today: str = TODAY, *modules: str):
		"""Pin the calendar for `modules` (dotted paths importing nowdate)."""
		for m in modules or ("kamra.folio", "kamra.business_date"):
			self._stack.enter_context(patch(f"{m}.nowdate", return_value=today))
