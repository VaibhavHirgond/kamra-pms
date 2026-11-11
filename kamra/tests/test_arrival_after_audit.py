"""A stay that arrives after its night's business date has already closed.

Night audit posts a night when that night's business date rolls over, so a
night is written by the audit that closes its date or by check-out - never
by both. Once end-of-day has run for the current date the business date
sits ahead of the calendar, and a booking made for that date afterwards is
never seen by the audit that should have charged it, while no later audit
looks back at a date the stay has passed. The folios sat at zero until
check-out: GRP-2026-8180, two rooms at 2,600 + 5% that never reached the
group bill.

Reservation.handle_check_in now posts those nights - exactly once, at the
stay's own locked rate and GST, routed by target_folio to the folio the
payment arrangement (master_pays / pays_own_charges / company rules) picks.
"""

from __future__ import annotations

import frappe

from kamra import api
from kamra import folio as folio_mod
from kamra.tests.audit_fixtures import (
	PROP_A,
	TODAY,
	AuditTestCase,
	d,
	make_property,
	make_reservation,
	make_room,
	make_room_type,
)

GROUP = "UT Arrival Wedding"
RATE = 2600
TAX = 5
NIGHT = RATE * (1 + TAX / 100)  # 2,730 - the amount the booking confirmed


class ArrivalAfterAuditTestCase(AuditTestCase):
	properties = (PROP_A,)

	def setUp(self):
		super().setUp()
		self.at(TODAY, "kamra.folio", "kamra.business_date", "kamra.ledger")
		# end-of-day for TODAY has already run: tomorrow's date is the open one
		make_property(PROP_A, business_date=d(1))
		self.rt = make_room_type(PROP_A, "STD", base_price=RATE,
		                         tax_percent=TAX)
		self.rooms = [make_room(PROP_A, self.rt, n) for n in ("102", "106")]

	# helpers ------------------------------------------------------------

	def group(self, pays="Room only", check_out=None, opts_out=()):
		"""A two-room group with its main room already picked - the shape
		the desk checks in after the group quotation is confirmed.
		`opts_out` is the index of a room that pays its own charges."""
		gb = frappe.get_doc({
			"doctype": "Group Booking", "property": PROP_A,
			"group_name": GROUP, "check_in_date": TODAY,
			"check_out_date": check_out or d(1), "status": "Confirmed",
		}).insert(ignore_permissions=True)
		stays = [make_reservation(PROP_A, self.rt, TODAY,
		                          check_out or d(1), room=room,
		                          group_booking=gb.name)
		         for room in self.rooms]
		gb.db_set({"master_reservation": stays[0].name, "master_pays": pays})
		for i in opts_out:
			api.set_pays_own_charges(stays[i].name, 1)
		out = api.group_check_in(gb.name)
		self.assertEqual(out["skipped"], [], out)
		return gb, stays

	def room_lines(self, res):
		name = res if isinstance(res, str) else res.name
		return frappe.get_all(
			"Folio Charge",
			filters={"reservation": name, "charge_type": "Room"},
			fields=["parent", "posting_date", "amount", "gst_rate", "total",
			        "auto_posted"],
			order_by="posting_date asc")

	def guest_folio(self, res):
		return frappe.db.get_value(
			"Folio", {"reservation": res if isinstance(res, str) else res.name,
			          "folio_type": "Guest"})

	def group_folio(self, gb):
		return frappe.db.get_value(
			"Folio", {"group_booking": gb.name, "folio_type": "Group"})

	# the reported defect ------------------------------------------------

	def test_both_rooms_land_on_the_group_bill_at_check_in(self):
		gb, (r1, r2) = self.group()
		for res in (r1, r2):
			lines = self.room_lines(res)
			self.assertEqual(len(lines), 1, res.name)
			self.assertEqual(str(lines[0].posting_date), TODAY)
			self.assertEqual(float(lines[0].amount), RATE)
			self.assertEqual(float(lines[0].gst_rate), TAX)
			self.assertAlmostEqual(float(lines[0].total), NIGHT, places=2)
			self.assertTrue(lines[0].auto_posted)
		bill = frappe.get_doc("Folio", self.group_folio(gb))
		self.assertEqual(float(bill.charges_total), 2 * RATE)
		self.assertEqual(float(bill.tax_total), 2 * RATE * TAX / 100)
		self.assertAlmostEqual(float(bill.grand_total), 2 * NIGHT, places=2)
		# the main room pays the room for every room: the guest folios are empty
		for res in (r1, r2):
			self.assertAlmostEqual(
				float(frappe.db.get_value("Folio", self.guest_folio(res),
				                          "grand_total")), 0, places=2)

	def test_the_bill_balances_to_what_the_booking_confirmed(self):
		gb, stays = self.group()
		billed = float(frappe.db.get_value("Folio", self.group_folio(gb),
		                                   "grand_total"))
		confirmed = sum(float(s.amount_after_tax) for s in stays)
		self.assertAlmostEqual(billed, confirmed, places=2)

	# exactly once --------------------------------------------------------

	def test_a_second_pass_and_checkout_never_bill_the_night_twice(self):
		_gb, (r1, r2) = self.group()
		self.assertEqual(len(self.room_lines(r1)), 1)
		# the writer check-out uses has nothing left to add
		self.assertEqual(
			folio_mod.post_remaining_nights(
				frappe.get_doc("Reservation", r1.name)), 0)
		# and neither does the check-in side effect run again
		self.assertEqual(
			folio_mod.post_closed_nights(
				frappe.get_doc("Reservation", r1.name)), [])
		for res in (r1, r2):
			self.assertEqual(len(self.room_lines(res)), 1)

	def test_only_the_closed_nights_are_posted_at_check_in(self):
		_gb, (r1, _r2) = self.group(check_out=d(2))
		self.assertEqual([str(x.posting_date) for x in self.room_lines(r1)],
		                 [TODAY])
		# the nights ahead of the business date are still owed to their own audits
		folio_mod.post_remaining_nights(frappe.get_doc("Reservation", r1.name))
		self.assertEqual([str(x.posting_date) for x in self.room_lines(r1)],
		                 [TODAY, d(1)])

	# the payment arrangement picks the folio -----------------------------

	def test_a_room_that_pays_its_own_keeps_its_room_charge(self):
		gb, (r1, r2) = self.group(opts_out=(1,))
		self.assertEqual(self.room_lines(r1)[0]["parent"], self.group_folio(gb))
		self.assertEqual(self.room_lines(r2)[0]["parent"], self.guest_folio(r2))

	def test_master_pays_nothing_leaves_every_room_on_its_own_folio(self):
		_gb, (r1, r2) = self.group(
			pays="Nothing (guest pays unless rules say so)")
		for res in (r1, r2):
			self.assertEqual(self.room_lines(res)[0]["parent"],
			                 self.guest_folio(res))

	def test_a_single_booking_gets_its_own_folio(self):
		res = make_reservation(PROP_A, self.rt, TODAY, d(1),
		                       room=self.rooms[0])
		api.check_in(res.name)
		lines = self.room_lines(res)
		self.assertEqual(len(lines), 1)
		self.assertEqual(lines[0]["parent"], self.guest_folio(res))
		self.assertAlmostEqual(float(lines[0].total), NIGHT, places=2)
		self.assertAlmostEqual(
			float(frappe.db.get_value("Folio", self.guest_folio(res),
			                          "grand_total")), NIGHT, places=2)

	# the control: an open business date behaves exactly as before --------

	def test_nothing_is_posted_while_the_business_date_is_still_open(self):
		make_property(PROP_A, business_date=TODAY)
		res = make_reservation(PROP_A, self.rt, TODAY, d(1),
		                       room=self.rooms[0])
		api.check_in(res.name)
		self.assertFalse(self.room_lines(res))  # tonight is tonight's audit's

		out = folio_mod.run_night_audit(PROP_A)
		self.assertEqual(out["room_charges_posted"], 1)
		lines = self.room_lines(res)
		self.assertEqual(len(lines), 1)
		self.assertEqual(str(lines[0].posting_date), TODAY)
		self.assertTrue(lines[0].auto_posted)

		# the same date closing again adds nothing
		self.assertTrue(
			folio_mod.run_night_audit(PROP_A, TODAY).get("already_ran"))
		self.assertEqual(len(self.room_lines(res)), 1)
