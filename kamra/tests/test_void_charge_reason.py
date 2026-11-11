# Copyright (c) 2026, HeyKoala and contributors
# For license information, please see license.txt

"""Voiding a charge needs a reason. The bill screen now asks for one, so the
API must refuse a blank reason and pass a typed one through to the void."""

import unittest
from unittest.mock import patch

import frappe

from kamra import api


_real_get_value = frappe.db.get_value


def _get_value(doctype, *args, **kwargs):
	# only answer for the folio; everything else (Meta loading) stays real
	if doctype == "Folio":
		return "PROP-1"
	return _real_get_value(doctype, *args, **kwargs)


class TestVoidChargeReason(unittest.TestCase):
	def _void(self, **kwargs):
		with patch.object(api, "_pin_guard"), \
		     patch("frappe.db.get_value", side_effect=_get_value), \
		     patch("kamra.ledger.ensure_default_reason_codes"), \
		     patch("kamra.ledger.reverse_ledger_for_charge"), \
		     patch("kamra.folio.void_charge", return_value={"ok": 1}) as void:
			result = api.void_folio_charge("FOLIO-1", "row1", **kwargs)
		return result, void

	def test_blank_reason_is_refused(self):
		for reason in ("", "   "):
			with self.assertRaises(frappe.ValidationError):
				self._void(reason=reason)

	def test_typed_reason_is_passed_to_the_void(self):
		_, void = self._void(reason="Posted by mistake")
		void.assert_called_once_with("FOLIO-1", "row1", "Posted by mistake")
