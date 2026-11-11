"""Razorpay Payment Links, on the property's own Razorpay account.

One REST call out, one webhook in (kamra.payments.razorpay_webhook). The
core decides what a link is for and posts the money; this module only
speaks Razorpay.
"""

import hashlib
import hmac
import json
import time

import frappe
from frappe.utils import get_url

GATEWAY = "Razorpay"
API = "https://api.razorpay.com/v1/payment_links"
# Kamra's partner referral link: costs the hotel nothing, helps fund the
# project. Site config kamra_razorpay_signup_url points it elsewhere.
SIGNUP_URL = "https://dashboard.razorpay.com/signup"


def create_link(settings, *, amount: float, currency: str, reference: str,
                description: str, customer: dict, notes: dict) -> tuple[str, str]:
	"""Returns (link id, short url)."""
	import requests

	secret = settings.get_password("key_secret", raise_exception=False)
	if not settings.key_id or not secret:
		frappe.throw("Razorpay key ID and secret are required for live payment links.")

	body = {
		"amount": int(round(float(amount) * 100)),
		"currency": currency,
		"accept_partial": False,
		# unique per merchant account; a folio can be re-linked, so stamp it
		"reference_id": f"{reference}-{int(time.time())}"[:40],
		"description": description[:2048],
		"customer": {k: v for k, v in customer.items() if v},
		"notify": {"sms": bool(customer.get("contact")),
		           "email": bool(customer.get("email"))},
		"reminder_enable": True,
		"notes": notes,
	}
	resp = requests.post(API, json=body, auth=(settings.key_id, secret), timeout=20)
	if resp.status_code >= 400:
		try:
			reason = resp.json().get("error", {}).get("description")
		except ValueError:
			reason = None
		frappe.throw(f"Razorpay refused the payment link: {reason or resp.status_code}")
	data = resp.json()
	return data["id"], data["short_url"]


def test_link(link_id: str) -> str:
	return f"https://rzp.io/test/{link_id}"


def info() -> dict:
	return {
		"gateway": GATEWAY,
		"webhook_url": get_url("/api/method/kamra.payments.razorpay_webhook"),
		"signup_url": frappe.conf.get("kamra_razorpay_signup_url") or SIGNUP_URL,
		"needs_webhook": True,
	}


def _paid_link(payload: bytes) -> dict | None:
	try:
		event = json.loads(payload or b"{}")
	except ValueError:
		return None
	if event.get("event") != "payment_link.paid":
		return None
	return event.get("payload", {}).get("payment_link", {}).get("entity") or None


def webhook_folio(payload: bytes) -> str | None:
	entity = _paid_link(payload)
	return ((entity or {}).get("notes") or {}).get("folio")


def verify_webhook(settings, payload: bytes, headers: dict) -> dict | None:
	"""Always verify - test mode too (Razorpay signs test webhooks). With no
	webhook secret there is nothing to verify against, so the call is
	refused rather than trusted."""
	secret = settings.get_password("webhook_secret", raise_exception=False)
	given = headers.get("x-razorpay-signature") or ""
	expected = hmac.new((secret or "").encode(), payload or b"",
	                    hashlib.sha256).hexdigest()
	if not secret or not hmac.compare_digest(given, expected):
		frappe.throw("Invalid webhook signature", frappe.PermissionError)
	entity = _paid_link(payload) or {}
	return {"link_id": entity.get("id") or "",
	        "amount": float(entity.get("amount_paid") or entity.get("amount") or 0) / 100}
