import unittest

from kamra.assistant_privacy import mask_contact_value, scrub_for_llm


class TestAssistantPrivacy(unittest.TestCase):
	def test_masks_phone_last_four_when_not_strict(self):
		self.assertEqual(mask_contact_value("+91 98765 43210", strict=False), "***3210")

	def test_strict_redacts(self):
		self.assertEqual(mask_contact_value("+91 98765 43210", strict=True), "[redacted]")

	def test_scrubs_nested_guest(self):
		payload = {
			"guest": {"full_name": "Ada", "phone": "9876543210", "id_number": "ABCD1234"},
			"room": "101",
		}
		out = scrub_for_llm(payload, strict=False)
		self.assertEqual(out["room"], "101")
		self.assertEqual(out["guest"]["full_name"], "Ada")
		self.assertEqual(out["guest"]["phone"], "***3210")
		self.assertEqual(out["guest"]["id_number"], "***1234")

	def test_strict_scrubs_contact_fields(self):
		payload = {"mobile": "9999888777", "notes": "VIP"}
		out = scrub_for_llm(payload, strict=True)
		self.assertEqual(out["mobile"], "[redacted]")
		self.assertEqual(out["notes"], "VIP")

	def test_keeps_lookalike_keys(self):
		payload = {
			"occupancy_pct": 82.5,
			"company": "Acme 2024 Ltd",
			"max_occupants": 3,
			"paid_now": 1200,
			"quote_emailed_on": "2026-10-01",
		}
		self.assertEqual(scrub_for_llm(payload, strict=True), payload)

	def test_masks_lists_under_contact_keys(self):
		out = scrub_for_llm({"phones": ["9876543210"], "guest_email": "ada@x.in"}, strict=False)
		self.assertEqual(out["phones"], ["***3210"])
		self.assertEqual(out["guest_email"], "a***@x.in")


if __name__ == "__main__":
	unittest.main()
