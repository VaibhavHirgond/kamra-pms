"""Supervisor reason codes remain role-gated when cashier PIN is optional."""

import frappe
from frappe.tests import IntegrationTestCase

from kamra import ledger


class SupervisorReasonTestCase(IntegrationTestCase):
	def setUp(self):
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- test fixture
		suffix = frappe.generate_hash(length=8)
		self.property = frappe.get_doc({"doctype": "Property",
			"property_name": "TEST Reason " + suffix, "require_cashier_pin": 0}).insert(
			ignore_permissions=True).name
		self.reason = frappe.get_doc({"doctype": "Reason Code", "code": "TEST-SUP-" + suffix,
			"description": "Test supervisor adjustment", "category": "Adjust",
			"requires_supervisor": 1}).insert(ignore_permissions=True).name
		self.finance = "test-finance-" + suffix + "@example.test"
		self.frontdesk = "test-frontdesk-" + suffix + "@example.test"
		self.hotel_admin = "test-admin-" + suffix + "@example.test"
		for email, role in ((self.finance, "Finance"), (self.frontdesk, "Front Desk"),
		                    (self.hotel_admin, "Hotel Admin")):
			frappe.get_doc({"doctype": "User", "email": email, "first_name": role,
				"user_type": "System User", "send_welcome_email": 0,
				"roles": [{"role": role}]}).insert(ignore_permissions=True)

	def reason_for(self, user, pin=None):
		frappe.set_user(user)  # nosemgrep: frappe-setuser -- test persona
		return ledger.require_reason("Adjust", self.reason, supervisor_pin=pin,
		                             property=self.property)

	def tearDown(self):
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- test fixture cleanup

	def test_finance_can_use_supervisor_reason_without_pin_when_property_pin_is_off(self):
		self.assertEqual(self.reason_for(self.finance), self.reason)

	def test_front_desk_still_needs_supervisor_role_when_property_pin_is_off(self):
		with self.assertRaises(frappe.PermissionError):
			self.reason_for(self.frontdesk)

	def test_hotel_admin_can_use_supervisor_reason_without_pin_when_property_pin_is_off(self):
		self.assertEqual(self.reason_for(self.hotel_admin), self.reason)

	def test_finance_still_needs_pin_when_property_pin_is_on(self):
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- fixture setup
		frappe.db.set_value("Property", self.property, "require_cashier_pin", 1)
		with self.assertRaises(frappe.ValidationError):
			self.reason_for(self.finance)

	def test_pin_enabled_supervisor_reason_checks_the_cashier_pin(self):
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- fixture setup
		frappe.db.set_value("Property", self.property, "require_cashier_pin", 1)
		frappe.get_doc({"doctype": "Cashier PIN", "user": self.finance,
			"pin": "1234", "must_reset": 0}).insert(ignore_permissions=True)
		with self.assertRaises(frappe.ValidationError):
			self.reason_for(self.finance, pin="9999")
		self.assertEqual(self.reason_for(self.finance, pin="1234"), self.reason)
