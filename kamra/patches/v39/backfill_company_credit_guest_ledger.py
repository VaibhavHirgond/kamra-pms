"""City ledger transfers before #190 wrote only the AR debit: the Company
Credit payment that zeroed the guest folio never credited the guest ledger,
so the debt sat in both ledgers. Post the missing guest-ledger credit for
every such payment, dated to the day the transfer happened.

Idempotent: a payment that already has its Folio Ledger Entry is skipped."""

import frappe


def execute():
	if not frappe.db.table_exists("Folio Ledger Entry"):
		return
	from kamra.ledger import record_payment_ledger

	rows = frappe.db.sql(
		"""
		SELECT p.name, p.parent, p.posting_date
		FROM `tabFolio Payment` p
		WHERE p.parenttype = 'Folio'
		  AND p.mode = 'Company Credit'
		  AND NOT EXISTS (
			SELECT 1 FROM `tabFolio Ledger Entry` e
			WHERE e.source_doctype = 'Folio Payment' AND e.source_name = p.name)
		""",
		as_dict=True,
	)
	for row in rows:
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
