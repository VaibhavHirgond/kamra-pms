# Copyright (c) 2026, HeyKoala and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PaymentGatewaySettings(Document):
	def validate(self):
		from kamra import localization as loc

		offered = loc.payment_gateways(loc.pack_for(self.property))
		if self.enabled and self.gateway not in offered:
			frappe.throw(
				frappe._("{0} is not offered for this property's country. Available: {1}.")
				.format(self.gateway, ", ".join(offered) or frappe._("none")))
		# Razorpay confirmations are signature-checked with this secret;
		# without it every webhook is refused and folios never get marked
		# paid. Cashfree signs with the secret key instead.
		if self.enabled and self.gateway == "Razorpay" and not self.webhook_secret:
			frappe.msgprint(
				"Set the webhook secret (the same one entered on the gateway's "
				"webhook): payment confirmations are rejected until it is.",
				indicator="orange", alert=True)
