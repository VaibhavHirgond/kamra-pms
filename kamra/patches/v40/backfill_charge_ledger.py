"""Before the ledger completeness fix, automatic postings never reached the
ledger: room nights from the night audit and checkout, their meal-plan
and levy lines, no-show and cancellation fees, cleaning fees, add-ons, POS room-service orders and
allowances were appended to the folio without a Folio Ledger Entry, so the
trial balance left out room revenue.

Bring the per-line ledger in step with the folio lines:

1. Every Folio Charge with no Folio Ledger Entry gets its charge entry,
   dated to the charge's posting_date (an allowance a credit note already
   booked on the ledger is skipped).
2. A ledger entry whose folio line is gone (moved to another folio, or
   removed without a reversal) is reversed, on the date it was posted - the
   line's ledger now lives with the line.
3. A line whose ledger differs from the line (part of it was split to
   another folio) is trued up, on the date it was posted.
4. Every Folio Payment with no Folio Ledger Entry gets its payment entry,
   dated to its posting_date - otherwise backfilling only the charges
   would show guests owing money they had already paid.

Idempotent: a re-run finds every line already in step and does nothing.
All entries go through kamra.ledger.write_ledger_entry."""

import frappe


def _charges_without_ledger():
	return frappe.db.sql(
		"""
		SELECT fc.name, fc.parent, fc.posting_date
		FROM `tabFolio Charge` fc
		WHERE fc.parenttype = 'Folio'
		  AND NOT EXISTS (
			SELECT 1 FROM `tabFolio Ledger Entry` e
			WHERE e.source_doctype = 'Folio Charge' AND e.source_name = fc.name
			  AND e.folio = fc.parent)
		  -- an open-folio credit note posted its allowance line and booked
		  -- the Guest credit itself (source Credit Note)
		  AND NOT (fc.charge_type = 'Allowance' AND EXISTS (
			SELECT 1 FROM `tabFolio Ledger Entry` cn
			WHERE cn.folio = fc.parent AND cn.source_doctype = 'Credit Note'
			  AND fc.description LIKE CONCAT(cn.description, ':%%')))
		ORDER BY fc.parent, fc.idx
		""",
		as_dict=True,
	)


def _orphaned_entries():
	"""Charge ledger still carrying a balance for a line no longer on that
	folio."""
	return frappe.db.sql(
		"""
		SELECT e.folio, e.source_name, e.property,
		       SUM(e.debit - e.credit) AS net
		FROM `tabFolio Ledger Entry` e
		WHERE e.source_doctype = 'Folio Charge'
		  AND NOT EXISTS (
			SELECT 1 FROM `tabFolio Charge` fc
			WHERE fc.name = e.source_name AND fc.parent = e.folio)
		GROUP BY e.folio, e.source_name, e.property
		HAVING ABS(SUM(e.debit - e.credit)) >= 0.005
		""",
		as_dict=True,
	)


def _drifted_lines():
	"""Lines whose ledger no longer equals the line (split before splits
	were booked)."""
	return frappe.db.sql(
		"""
		SELECT fc.name, fc.parent AS folio,
		       -- what record_charge_ledger books for the line
		       COALESCE(NULLIF(fc.total, 0), fc.amount, 0) AS total,
		       SUM(e.debit - e.credit) AS net
		FROM `tabFolio Charge` fc
		JOIN `tabFolio Ledger Entry` e
		  ON e.source_doctype = 'Folio Charge' AND e.source_name = fc.name
		 AND e.folio = fc.parent
		WHERE fc.parenttype = 'Folio'
		GROUP BY fc.name, fc.parent, fc.total, fc.amount
		HAVING ABS(SUM(e.debit - e.credit)
		           - COALESCE(NULLIF(fc.total, 0), fc.amount, 0)) >= 0.005
		""",
		as_dict=True,
	)


def _original(folio, source_name):
	return frappe.db.get_value(
		"Folio Ledger Entry",
		{"source_doctype": "Folio Charge", "source_name": source_name,
		 "folio": folio, "reversal_of": ["in", ["", None]]},
		["name", "property", "ledger", "transaction_code", "description",
		 "business_date"],
		as_dict=True, order_by="posted_at asc")


def _true_up(folio, source_name, diff, label):
	"""Post `diff` (positive = credit) against the line's original entry,
	dated with it."""
	from kamra.ledger import write_ledger_entry
	orig = _original(folio, source_name)
	if not orig:
		return
	diff = round(float(diff), 2)
	write_ledger_entry(
		property=orig.property,
		folio=folio,
		ledger=orig.ledger or "Guest",
		debit=-diff if diff < 0 else 0,
		credit=diff if diff > 0 else 0,
		description=f"{label}: {orig.description or ''}"[:140],
		transaction_code=orig.transaction_code,
		reversal_of=orig.name,
		source_doctype="Folio Charge",
		source_name=source_name,
		business_date=str(orig.business_date),
	)


def execute():
	if not frappe.db.table_exists("Folio Ledger Entry"):
		return
	from kamra.ledger import record_charge_ledger, record_payment_ledger

	for row in _orphaned_entries():
		_true_up(row.folio, row.source_name, row.net, "BACKFILL line gone")

	for row in _drifted_lines():
		_true_up(row.folio, row.name, float(row.net) - float(row.total or 0),
		         "BACKFILL split")

	folio = None
	for row in _charges_without_ledger():
		if folio is None or folio.name != row.parent:
			folio = frappe.get_doc("Folio", row.parent)
		charge = next((c for c in folio.charges if c.name == row.name), None)
		if not charge:
			continue
		record_charge_ledger(folio, charge.as_dict(),
		                     business_date=str(row.posting_date)
		                     if row.posting_date else None)

	for row in frappe.db.sql(
		"""
		SELECT p.name, p.parent, p.posting_date
		FROM `tabFolio Payment` p
		WHERE p.parenttype = 'Folio'
		  AND NOT EXISTS (
			SELECT 1 FROM `tabFolio Ledger Entry` e
			WHERE e.source_doctype = 'Folio Payment' AND e.source_name = p.name)
		ORDER BY p.parent, p.idx
		""",
		as_dict=True,
	):
		if folio is None or folio.name != row.parent:
			folio = frappe.get_doc("Folio", row.parent)
		payment = next((p for p in folio.payments if p.name == row.name), None)
		if not payment:
			continue
		record_payment_ledger(folio, payment.as_dict())
		if row.posting_date:
			entry = frappe.db.get_value(
				"Folio Ledger Entry",
				{"source_doctype": "Folio Payment", "source_name": row.name})
			frappe.db.set_value("Folio Ledger Entry", entry, "business_date",
			                    row.posting_date, update_modified=False)
