"""OTA inventory must include bookings that do not yet have a room number."""

import frappe
from frappe.tests import IntegrationTestCase
from frappe.utils import add_days, nowdate

from kamra import channel_manager as cm


class ChannelManagerAvailabilityTestCase(IntegrationTestCase):
	def setUp(self):
		frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- test fixture
		self.property = frappe.get_doc({"doctype": "Property",
			"property_name": "TEST ARI " + frappe.generate_hash(length=8)}).insert(ignore_permissions=True).name
		self.room_type = frappe.get_doc({"doctype": "Room Type", "property": self.property,
			"room_type_code": "STD", "room_type_name": "Standard", "base_price": 1000,
			"adults_capacity": 2}).insert(ignore_permissions=True).name
		self.room = frappe.get_doc({"doctype": "Room", "property": self.property,
			"room_type": self.room_type, "room_number": "101"}).insert(ignore_permissions=True).name
		self.guest = frappe.get_doc({"doctype": "Guest", "first_name": "ARI Guest"}).insert(ignore_permissions=True).name
		self.conn = frappe.get_doc({"doctype": "Channel Manager Connection", "property": self.property,
			"provider": "AioSell", "active": 1, "external_property_id": "demo"}).insert(ignore_permissions=True)
		frappe.get_doc({"doctype": "Channel Room Mapping", "connection": self.conn.name,
			"room_type": self.room_type, "external_room_id": "std",
			"external_rate_id": "std-rate"}).insert(ignore_permissions=True)

	def reservation(self, status="Confirmed", room=None, check_in=None):
		ci = check_in or nowdate()
		return frappe.get_doc({"doctype": "Reservation", "property": self.property,
			"room_type": self.room_type, "guest": self.guest, "room": room,
			"status": status, "check_in_date": ci, "check_out_date": add_days(ci, 1),
			"adults": 2}).insert(ignore_permissions=True)

	def available(self):
		return cm.ari_snapshot(self.property, self.conn.name, days=1)[0]["days"][0]["available"]

	def test_unassigned_confirmed_stay_reduces_ota_inventory(self):
		stay = self.reservation()
		self.assertFalse(stay.room)
		self.assertEqual(self.available(), 0)

	def test_legacy_unassigned_stay_reduces_ota_inventory(self):
		frappe.db.set_value("Sellable Unit", {"property": self.property}, "is_active", 0)
		self.reservation()
		self.assertEqual(self.available(), 0)

	def test_assigned_stay_is_not_counted_twice(self):
		self.reservation(room=self.room)
		self.assertEqual(self.available(), 0)

	def test_requested_stay_holds_no_ota_inventory(self):
		self.reservation(status="Requested")
		self.assertEqual(self.available(), 1)

	def test_adjacent_stay_leaves_tonight_available(self):
		self.reservation(check_in=add_days(nowdate(), 1))
		self.assertEqual(self.available(), 1)

	def test_room_block_still_holds_ota_inventory(self):
		frappe.get_doc({"doctype": "Room Block", "property": self.property,
			"room": self.room, "from_date": nowdate(), "to_date": add_days(nowdate(), 1),
			"block_status": "Active", "reason": "Maintenance"}).insert(ignore_permissions=True)
		self.assertEqual(self.available(), 0)
