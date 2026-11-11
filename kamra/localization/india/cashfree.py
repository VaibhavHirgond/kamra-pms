"""Cashfree Payment Links, on the property's own Cashfree account.

Each link carries its own notify_url (kamra.payments.cashfree_webhook), so
the hotel sets up no webhook in Cashfree. Test App IDs (TEST...) go to
Cashfree's sandbox.
"""

import base64
import hashlib
import hmac
import json
import re
import time

import frappe
from frappe.utils import get_url

GATEWAY = "Cashfree"
API_VERSION = "2025-01-01"
# Kamra's partner referral link; site config kamra_cashfree_signup_url
# points it elsewhere.
SIGNUP_URL = "https://merchant.cashfree.com/merchants/signup"


def _webhook_url() -> str:
	return get_url("/api/method/kamra.payments.cashfree_webhook")


def create_link(settings, *, amount: float, currency: str, reference: str,
                description: str, customer: dict, notes: dict) -> tuple[str, str]:
	"""Returns (link id, link url)."""
	import requests

	secret = settings.get_password("key_secret", raise_exception=False)
	if not settings.key_id or not secret:
		frappe.throw("Cashfree App ID and secret key are required for live payment links.")
	phone = re.sub(r"\D", "", customer.get("contact") or "")
	if len(phone) < 10:
		frappe.throw("Cashfree needs the guest's mobile number to send a payment link. "
		             "Add it to the guest profile.")
	link_id = re.sub(r"[^A-Za-z0-9_-]", "-", f"{reference}-{int(time.time())}")[-50:]
	body = {
		"link_id": link_id,
		"link_amount": round(float(amount), 2),
		"link_currency": currency,
		"link_purpose": description[:500],
		"customer_details": {k: v for k, v in {
			"customer_name": customer.get("name"), "customer_email": customer.get("email"),
			"customer_phone": phone[-10:]}.items() if v},
		"link_notify": {"send_sms": True, "send_email": bool(customer.get("email"))},
		"link_auto_reminders": True,
		"link_notes": {k: str(v) for k, v in notes.items()},
		"link_meta": {"notify_url": _webhook_url()},
	}
	base = ("https://sandbox.cashfree.com/pg" if settings.key_id.upper().startswith("TEST")
	        else "https://api.cashfree.com/pg")
	resp = requests.post(f"{base}/links", json=body, timeout=20, headers={
		"x-client-id": settings.key_id, "x-client-secret": secret,
		"x-api-version": API_VERSION, "x-idempotency-key": link_id})
	if resp.status_code >= 400:
		try:
			reason = resp.json().get("message")
		except ValueError:
			reason = None
		frappe.throw(f"Cashfree refused the payment link: {reason or resp.status_code}")
	return link_id, resp.json()["link_url"]


def test_link(link_id: str) -> str:
	return f"https://payments.cashfree.com/links/test/{link_id}"


def info() -> dict:
	return {
		"gateway": GATEWAY,
		"webhook_url": _webhook_url(),
		"signup_url": frappe.conf.get("kamra_cashfree_signup_url") or SIGNUP_URL,
		"needs_webhook": False,
	}


def _paid_link(payload: bytes) -> dict | None:
	try:
		event = json.loads(payload or b"{}")
	except ValueError:
		return None
	data = event.get("data") or {}
	if event.get("type") != "PAYMENT_LINK_EVENT" or data.get("link_status") != "PAID":
		return None
	return data


def webhook_folio(payload: bytes) -> str | None:
	data = _paid_link(payload)
	return ((data or {}).get("link_notes") or {}).get("folio")


def signature(secret: str, timestamp: str, payload: bytes) -> str:
	"""base64(HMAC-SHA256(timestamp + raw body)), keyed by the secret key."""
	return base64.b64encode(hmac.new(
		secret.encode(), (timestamp or "").encode() + (payload or b""),
		hashlib.sha256).digest()).decode()


def verify_webhook(settings, payload: bytes, headers: dict) -> dict | None:
	"""Signed with the property's own secret key. Verified in test mode
	too, like Razorpay: an unsigned call is refused, never trusted."""
	secret = settings.get_password("key_secret", raise_exception=False)
	given = headers.get("x-webhook-signature") or ""
	if not secret or not hmac.compare_digest(
			given, signature(secret, headers.get("x-webhook-timestamp") or "", payload)):
		frappe.throw("Invalid webhook signature", frappe.PermissionError)
	data = _paid_link(payload) or {}
	return {"link_id": data.get("link_id") or "",
	        "amount": float(data.get("link_amount_paid") or data.get("link_amount") or 0)}
