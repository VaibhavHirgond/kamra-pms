"""Company payments recorded with city_ledger_settle before the ledger
completeness fix reduced the City Ledger Account but never credited the
AR ledger, so a paid receivable stayed on the trial balance forever.

Apply each such payment, oldest first, to the company's oldest open
city-ledger folios - the same order city_ledger_aging already showed them
in - with each AR credit dated to the later of the payment and the bill.
What a payment can't cover stays as unapplied credit on the account.

Idempotent: a payment's applied part is read back from its AR credits, so
a re-run applies nothing."""

import frappe


def execute():
	if not frappe.db.table_exists("City Ledger Entry"):
		return
	from kamra.ledger import apply_unapplied_credit

	for account in frappe.get_all("City Ledger Account", pluck="name"):
		apply_unapplied_credit(account, backdate=True)
