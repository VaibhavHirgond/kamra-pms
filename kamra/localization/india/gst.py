"""GST returns. Each GSTIN files its own return, so rows are per property."""

import frappe


def gstr1_rows(properties: str | list[str], from_date: str, to_date: str):
	"""Invoice-level rows for a GSTR-1 style export (v0: B2C summary)."""
	if isinstance(properties, str):
		properties = [properties]
	if not properties:
		return []
	return frappe.get_all(
		"Folio",
		filters={
			"status": "Closed",
			"closed_on": ("between", [from_date, to_date]),
			"property": ("in", properties),
		},
		fields=["name", "invoice_number", "guest_name", "closed_on",
		        "charges_total", "tax_total", "grand_total"],
		order_by="closed_on asc",
	)
