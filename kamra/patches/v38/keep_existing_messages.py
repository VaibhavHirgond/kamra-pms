"""Message retention is a default for new properties. A hotel already
running keeps its message history until it chooses a period."""

import frappe


def execute():
	frappe.db.sql("update `tabProperty` set message_retention_days = 0")
