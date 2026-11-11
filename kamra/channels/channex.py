"""Channex.io adapter - https://docs.channex.io

API-first channel-manager infrastructure: self-serve signup, sandbox at
staging.channex.io, per-property pricing, certified with Booking.com,
Agoda, Expedia, Airbnb and more. The hotel brings its own Channex
account; api_key is a Channex user API key, external_property_id the
Channex property id, and mappings carry Channex room_type/rate_plan ids.

Webhook: register a Channex webhook (event: booking) pointing at
/api/method/kamra.channel_manager.webhook?connection=<name>; put the
same secret on both sides (Channex sends it back as X-Webhook-Secret).
The payload carries only revision ids - kamra.channel_manager
.process_channex_revision pulls the authoritative revision, applies it,
commits, and only then acknowledges it.
"""

from __future__ import annotations

DEFAULT_ENDPOINT = "https://app.channex.io/api/v1"


def _call(conn, method: str, path: str, payload=None):
	import requests

	key = conn.get_password("api_key", raise_exception=False)
	base = (conn.endpoint or DEFAULT_ENDPOINT).rstrip("/")
	res = requests.request(
		method, f"{base}/{path}",
		json=payload, headers={"user-api-key": key or ""}, timeout=20)
	ok = 200 <= res.status_code < 300
	try:
		body = res.json()
	except Exception:
		body = {"raw": res.text[:300]}
	return ok, body


def push_ari(conn, snapshot) -> tuple[bool, str]:
	"""Channex takes availability and rate values as bulk arrays."""
	availability, rates = [], []
	for rt in snapshot:
		for day in rt["days"]:
			availability.append({
				"property_id": conn.external_property_id,
				"room_type_id": rt["external_room_id"],
				"date": day["date"],
				"availability": day["available"],
			})
			if rt.get("external_rate_id"):
				rates.append({
					"property_id": conn.external_property_id,
					"rate_plan_id": rt["external_rate_id"],
					"date": day["date"],
					"rate": str(day["rate"]),
				})
	ok1, b1 = _call(conn, "POST", "availability",
	                {"values": availability})
	ok2, b2 = (True, {}) if not rates else _call(
		conn, "POST", "restrictions", {"values": rates})
	if ok1 and ok2:
		return True, f"{len(availability)} availability, {len(rates)} rate values"
	err = (b1 if not ok1 else b2)
	return False, str(err)[:280]


def parse_webhook(conn, payload) -> list[dict]:
	"""Channex booking revision -> normalized events.

	Takes a revision's attributes - the authoritative booking message
	({status, ota_reservation_code, ota_name, arrival_date, departure_date,
	customer{...}, rooms[...]}) - never the raw webhook, whose payload
	carries only ids (revision_id, booking_id, property_id).
	"""
	body = payload.get("payload") or payload
	status = (body.get("status") or "new").lower()
	event = {"new": "book", "modified": "modify",
	         "cancelled": "cancel"}.get(status, "book")
	customer = body.get("customer") or {}
	out = []
	for room in body.get("rooms") or [{}]:
		days = room.get("days") or {}
		total = sum(float(v or 0) for v in days.values()) or \
			float(body.get("amount") or 0)
		occ = room.get("occupancy") or {}
		out.append({
			"event": event,
			"ota_ref": body.get("ota_reservation_code")
			           or body.get("unique_id") or "",
			"channel": body.get("ota_name") or "OTA",
			"room_type_external_id": room.get("room_type_id") or "",
			"check_in": room.get("checkin_date") or body.get("arrival_date"),
			"check_out": room.get("checkout_date") or body.get("departure_date"),
			"adults": int(occ.get("adults") or 2),
			"children": int(occ.get("children") or 0),
			"guest_name": " ".join(filter(None, [customer.get("name"),  # nosemgrep: frappe-no-functional-code -- filter(None, ...) drops empty parts; equivalent to a comprehension
			                                     customer.get("surname")]))
			              or "OTA Guest",
			"phone": customer.get("phone") or "",
			"email": customer.get("mail") or customer.get("email") or "",
			"total": total,
			"nightly": [{"date": k, "amount": float(v or 0)} for k, v in sorted(days.items())],
			"currency": body.get("currency") or "",
			"notes": body.get("notes") or "",
		})
	return out


def _revision_attributes(item):
	"""Extract booking revision attributes from a JSON:API resource.

	Both the feed and the by-id endpoint wrap the message as
	{"type", "id", "attributes": {...}}; a bare attribute dict passes
	through with its id kept."""
	if not isinstance(item, dict):
		return {}

	revision = item.get("attributes") or item

	if isinstance(revision, dict) and item.get("id"):
		revision.setdefault("id", item["id"])

	return revision


def fetch_booking_revision(conn, revision_id: str):
	"""Fetch one complete booking revision from Channex."""
	ok, body = _call(
		conn,
		"GET",
		f"booking_revisions/{revision_id}"
	)

	if not ok:
		return False, body

	data = body.get("data") or {}
	revision = _revision_attributes(data)

	if not revision.get("id"):
		revision["id"] = revision_id

	return True, revision


def fetch_booking_revision_feed(conn):
	"""Fetch this connection's unacknowledged booking revisions, oldest first.

	The feed is account-wide, so it is filtered to this connection's
	property - another property's bookings must never land here."""
	filt = (f"filter[property_id]={conn.external_property_id}&"
	        if conn.external_property_id else "")
	ok, body = _call(
		conn,
		"GET",
		f"booking_revisions/feed?{filt}order[inserted_at]=asc"
	)

	if not ok:
		return False, body

	data = body.get("data") or []

	if not isinstance(data, list):
		return False, {"error": "Unexpected booking feed response"}

	return True, [_revision_attributes(item) for item in data]


def acknowledge_booking_revision(conn, revision_id: str):
	"""Acknowledge a revision after successful PMS processing."""
	return _call(
		conn,
		"POST",
		f"booking_revisions/{revision_id}/ack"
	)
