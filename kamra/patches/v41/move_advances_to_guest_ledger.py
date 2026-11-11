"""An advance credits the Deposit ledger when it is taken. Before this fix it
never left: at check-in it should have moved to the Guest ledger (it pays
the stay), so every in-house or departed stay with an advance left the
Deposit ledger holding money the guest had already spent, and the Guest
ledger owing it. Post the missing transfer, dated to the day the guest
checked in.

Idempotent: kamra.ledger.transfer_advances_to_guest only moves what is
still held for each advance payment."""

import frappe
from frappe.utils import getdate


def execute():
	if not frappe.db.table_exists("Folio Ledger Entry"):
		return
	from kamra.ledger import transfer_advances_to_guest

	stays = frappe.db.sql(
		"""
		SELECT DISTINCT r.name, r.actual_check_in, r.check_in_date
		FROM `tabReservation` r
		JOIN `tabFolio` f ON f.reservation = r.name
		JOIN `tabFolio Payment` p ON p.parent = f.name AND p.parenttype = 'Folio'
		WHERE r.status IN ('Checked In', 'Checked Out')
		  AND p.payment_kind = 'Advance'
		""",
		as_dict=True,
	)
	for stay in stays:
		when = stay.actual_check_in or stay.check_in_date
		transfer_advances_to_guest(
			stay.name, business_date=str(getdate(when)) if when else None)
