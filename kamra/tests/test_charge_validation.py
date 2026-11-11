# Copyright (c) 2026, HeyKoala and contributors
# For license information, please see license.txt

"""Posted charges: positive amount, tax rate from the country pack.

The check belongs on what the caller sends. Rates the hotel decides itself
(the agent's post_stay_charge, banquet billing) must not be refused."""

import unittest
from unittest.mock import patch

import frappe

from kamra import api
from kamra.api import _check_charge_amount_and_tax


class _IndiaPack:
	@staticmethod
	def tax_rate_options(property):
		return [0, 5, 12, 18, 28]


class _SaudiPack:
	@staticmethod
	def tax_rate_options(property):
		return [0, 15]


def _check(amount, gst, pack=_IndiaPack):
	with patch("kamra.localization.pack_for", return_value=pack):
		return _check_charge_amount_and_tax("P", amount, gst)


class TestChargeValidation(unittest.TestCase):
	def test_normal_charge_passes(self):
		_check(100, 5)
		_check("250.50", 0)
		_check(100, None)

	def test_zero_and_minus_amount_rejected(self):
		for amount in (0, -50, "-1"):
			with self.assertRaisesRegex(frappe.ValidationError, "more than zero"):
				_check(amount, 5)

	def test_not_a_number_rejected(self):
		for amount in (None, "abc", float("inf"), float("nan"), "inf"):
			with self.assertRaisesRegex(frappe.ValidationError, "must be a number"):
				_check(amount, 5)

	def test_unknown_tax_rate_rejected(self):
		with self.assertRaisesRegex(frappe.ValidationError, "99% is not allowed"):
			_check(100, 99)
		with self.assertRaisesRegex(frappe.ValidationError, "7% is not allowed"):
			_check(100, 7)


class TestPostingPaths(unittest.TestCase):
	"""Which entry points run the check, and on which rate."""

	def test_add_folio_charge_checks_what_the_caller_sent(self):
		real_get_value = frappe.db.get_value

		def get_value(doctype, *args, **kwargs):
			if doctype == "Folio":
				return "P"
			return real_get_value(doctype, *args, **kwargs)

		with patch("kamra.localization.pack_for", return_value=_IndiaPack), \
		     patch("kamra.api.frappe.db.get_value", side_effect=get_value), \
		     patch("kamra.api._post_folio_charge") as post:
			with self.assertRaisesRegex(frappe.ValidationError, "99% is not allowed"):
				api.add_folio_charge("F", "Misc", "x", 100, 99)
			with self.assertRaisesRegex(frappe.ValidationError, "more than zero"):
				api.add_folio_charge("F", "Misc", "x", -5, 5)
			post.assert_not_called()
			api.add_folio_charge("F", "Misc", "x", 100, 5)
			post.assert_called_once()

	def _stay_charge(self, pack, gst_rate, is_alcohol, resolved):
		res = frappe._dict(status="Checked In", property="P", name="R")
		with patch("kamra.localization.pack_for", return_value=pack), \
		     patch("kamra.api.frappe.get_doc", return_value=res), \
		     patch("kamra.folio.target_folio", return_value="F"), \
		     patch("kamra.api._resolve_charge_gst", return_value=resolved), \
		     patch("kamra.api._post_folio_charge",
		           return_value={"folio_type": "Guest", "balance": 0}) as post:
			out = api.post_stay_charge("R", "Minibar", "beer", 100,
			                           gst_rate, is_alcohol)
		return out, post

	def test_agent_alcohol_outside_india_is_not_refused(self):
		# no rate sent -> the hotel's alcohol default (18) is not in Saudi's list
		out, post = self._stay_charge(_SaudiPack, 0, 1, resolved=18.0)
		post.assert_called_once()
		self.assertEqual(post.call_args.args[4], 18.0)
		self.assertEqual(out["folio"], "F")

	def test_agent_rate_sent_by_caller_is_still_checked(self):
		with self.assertRaisesRegex(frappe.ValidationError, "18% is not allowed"):
			self._stay_charge(_SaudiPack, 18, 1, resolved=18.0)

	def test_agent_minus_amount_is_refused(self):
		res = frappe._dict(status="Checked In", property="P", name="R")
		with patch("kamra.localization.pack_for", return_value=_IndiaPack), \
		     patch("kamra.api.frappe.get_doc", return_value=res), \
		     patch("kamra.api._post_folio_charge") as post:
			with self.assertRaisesRegex(frappe.ValidationError, "more than zero"):
				api.post_stay_charge("R", "Misc", "x", -50, 5, 0)
			post.assert_not_called()

	def test_banquet_billing_does_not_use_the_checked_entry_point(self):
		import inspect

		from kamra import banquet
		src = inspect.getsource(banquet.post_to_folio)
		self.assertIn("_post_folio_charge", src)
		self.assertNotIn("add_folio_charge", src)

	def test_internal_poster_is_not_whitelisted(self):
		self.assertNotIn(api._post_folio_charge, frappe.whitelisted)
		self.assertIn(api.add_folio_charge, frappe.whitelisted)
