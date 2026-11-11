"""No-show policy: when an arrival that never came becomes a No Show, which
arrivals the night audit holds, which no-shows carry a fee, and the release
of non-guaranteed arrivals.

All of it is per property (Settings → Front Desk → Night audit & no-shows):

  no_show_timing              "At audit for arrival date" (default): the audit
                              that closes day D marks D's unarrived arrivals.
                              "One day later": they stay Due In until the
                              audit of D + 1.
  protect_late_arrivals       on (default): an arrival due on the closed date
                              is held, not no-showed, while it is flagged
                              late_arrival or its ETA is still ahead of the
                              moment the audit runs. The next audit decides.
  waive_no_show_fee_for_ota   on (default): an OTA / channel booking is still
                              marked No Show but carries no fee - the OTA
                              collects under its own policy.
  non_guaranteed_release_time blank = off. At that local time today's
                              arrivals that are not guaranteed are cancelled
                              with no fee (15-minute scheduler).

The night audit (kamra.folio.run_night_audit) and the End of Day "Mark
no-show" action (kamra.night_audit.eod_mark_no_show) are the only writers of
No Show, both through kamra.folio.apply_no_show; this module only answers the
policy questions.
"""

from __future__ import annotations

import re
from datetime import datetime, time, timedelta

import frappe
from frappe.utils import cint, get_datetime, getdate

AT_AUDIT = "At audit for arrival date"
ONE_DAY_LATER = "One day later"

# An ETA earlier than this is the small hours after the arrival date: a guest
# due on the 12th "arriving at 01:00" lands on the 13th at 01:00.
AFTER_MIDNIGHT_BEFORE = time(6, 0)

# channel values that are not an OTA, should an import or a desk flow set one
NOT_OTA_CHANNELS = {"", "direct", "walk-in", "walkin", "website", "phone",
                    "pms", "manual"}


def policy(property: str) -> frappe._dict:
	"""The property's no-show settings, with the defaults filled in."""
	row = frappe.db.get_value(
		"Property", property,
		["no_show_charge", "no_show_timing", "protect_late_arrivals",
		 "waive_no_show_fee_for_ota", "non_guaranteed_release_time"],
		as_dict=True) or frappe._dict()

	def flag(v, default=1):
		return default if v is None or v == "" else cint(v)

	return frappe._dict(
		charge=row.get("no_show_charge") or "None",
		timing=row.get("no_show_timing") or AT_AUDIT,
		protect_late=flag(row.get("protect_late_arrivals")),
		waive_ota=flag(row.get("waive_no_show_fee_for_ota")),
		release_time=_as_time(row.get("non_guaranteed_release_time")),
	)


# --- clocks ------------------------------------------------------------------

def property_now(property: str) -> datetime:
	"""Wall-clock time at the property (naive). The site clock is converted
	when the property sets a time zone different from the site's."""
	from frappe.utils import get_system_timezone, now_datetime
	now = now_datetime()
	tz = (frappe.db.get_value("Property", property, "timezone") or "").strip()
	site = get_system_timezone()
	if not tz or tz == site:
		return now
	try:
		from zoneinfo import ZoneInfo
		return (now.replace(tzinfo=ZoneInfo(site))
		        .astimezone(ZoneInfo(tz)).replace(tzinfo=None))
	except Exception:
		return now


def _as_time(v) -> time | None:
	"""A Time field value (timedelta from the db, or 'HH:MM[:SS]') as time."""
	if v in (None, ""):
		return None
	if isinstance(v, time):
		return v
	if isinstance(v, timedelta):
		secs = int(v.total_seconds()) % 86400
		return time(secs // 3600, (secs % 3600) // 60)
	m = re.match(r"^\s*(\d{1,2}):(\d{2})", str(v))
	if not m:
		return None
	h, mi = int(m.group(1)), int(m.group(2))
	return time(h, mi) if h < 24 and mi < 60 else None


_ETA_RE = re.compile(r"(\d{1,2})(?:\s*[:.h]\s*(\d{2}))?\s*(am|pm|a\.m\.|p\.m\.)?",
                     re.IGNORECASE)
_LATE_WORDS = ("late", "midnight", "after 12", "night")


def parse_eta(text) -> time | str | None:
	"""The guest's free-text ETA ("14:30", "1 am", "9.45pm", "late night") as a
	time, the string "late" when it only says the guest comes late, or None
	when it can't be read."""
	if text in (None, ""):
		return None
	if isinstance(text, (time, timedelta)):
		return _as_time(text)
	s = str(text).strip().lower()
	if "midnight" in s:
		return time(0, 0)
	if "noon" in s:
		return time(12, 0)
	m = _ETA_RE.search(s)
	if m:
		h = int(m.group(1))
		mi = int(m.group(2) or 0)
		ampm = (m.group(3) or "").replace(".", "")
		if ampm == "pm" and h < 12:
			h += 12
		elif ampm == "am" and h == 12:
			h = 0
		if h < 24 and mi < 60 and (m.group(2) or ampm):
			return time(h, mi)
	if any(w in s for w in _LATE_WORDS):
		return "late"
	return None


def expected_arrival(arrival_date, t: time) -> datetime:
	"""Arrival date + ETA; an ETA in the small hours means the next morning."""
	at = datetime.combine(getdate(arrival_date), t)
	if t < AFTER_MIDNIGHT_BEFORE:
		at += timedelta(days=1)
	return at


def late_arrival_reason(res, run_at: datetime) -> str | None:
	"""Why the audit running at `run_at` (property local time) should hold
	this arrival rather than mark it a No Show - or None.

	Held when the desk flagged it Late Arrival, the guest's ETA only says
	"late", or the ETA (the guest's `eta`, or the desk's planned arrival
	time, whichever is later) is still ahead of the run. A manual audit at
	23:00 holds a 01:00 ETA; the 03:00 scheduled run does not."""
	if cint(res.get("late_arrival")):
		return "flagged late arrival"
	times = []
	eta = parse_eta(res.get("eta"))
	if eta == "late":
		return f"ETA {res.get('eta')}"
	if isinstance(eta, time):
		times.append(eta)
	planned = _as_time(res.get("planned_check_in_time"))
	if planned:
		times.append(planned)
	if not times:
		return None
	latest = max(expected_arrival(res.check_in_date, t) for t in times)
	if latest > run_at:
		return f"ETA {latest:%H:%M} is after the audit ({run_at:%H:%M})"
	return None


def audit_outcome(res, pol, business_date, run_at: datetime) -> frappe._dict:
	"""What the audit closing `business_date` (running at `run_at`, property
	time) does with this unarrived Confirmed stay - the one decision both the
	audit and its pre-check checklist use, so the checklist never promises
	something the audit then does differently.

	outcome: "defer"   - "One day later" timing: stays Due In tonight
	         "hold"    - late arrival protected until the next audit
	         "no_show" - marked No Show tonight
	fee (no_show only): "none" (policy charges nothing), "waived" (OTA) or
	"charge" (the policy's basis is posted)."""
	bd = str(getdate(business_date))
	ci = str(getdate(res.check_in_date))
	if pol.timing == ONE_DAY_LATER and ci >= bd:
		return frappe._dict(outcome="defer", reason="no-show timing is one day later",
		                    fee=None)
	if pol.protect_late and ci == bd:
		why = late_arrival_reason(res, run_at)
		if why:
			return frappe._dict(outcome="hold", reason=why, fee=None)
	return fee_decision(res, pol)


def fee_decision(res, pol) -> frappe._dict:
	"""A stay that is being marked No Show: does the policy charge a fee,
	charge nothing, or waive it because an OTA collects?"""
	if pol.charge == "None":
		return frappe._dict(outcome="no_show", reason="", fee="none")
	if pol.waive_ota and is_ota_booking(res):
		return frappe._dict(outcome="no_show",
		                    reason=f"{res.get('channel') or res.get('source') or 'OTA'} booking",
		                    fee="waived")
	return frappe._dict(outcome="no_show", reason="", fee="charge")


# --- who pays ----------------------------------------------------------------

def is_ota_booking(res) -> bool:
	"""Came through an OTA / channel manager: the OTA collects under its own
	policy, so a no-show fee on our folio would bill the guest twice."""
	if (res.get("source") or "") == "OTA" or (res.get("ota_ref") or "").strip():
		return True
	return (res.get("channel") or "").strip().lower() not in NOT_OTA_CHANNELS


def is_guaranteed(res) -> bool:
	"""Is the room secured? Kamra has no card-on-file guarantee, so a stay
	counts as guaranteed when money or a third party stands behind it: an
	advance paid, a payment or deposit on any of its folios, an OTA /
	channel booking, or a company (corporate) booking."""
	if float(res.get("advance_paid") or 0) > 0:
		return True
	if is_ota_booking(res):
		return True
	if res.get("company") or (res.get("booking_type") or "") == "Corporate":
		return True
	return bool(frappe.db.sql(
		"""SELECT 1 FROM `tabFolio Payment` fp
		   JOIN `tabFolio` f ON fp.parent = f.name
		   WHERE f.reservation = %s AND fp.amount > 0 LIMIT 1""",
		res.name))


# --- release of non-guaranteed arrivals ----------------------------------------

def release_non_guaranteed_arrivals():
	"""Scheduler (every 15 min): for each property with a release time, cancel
	today's non-guaranteed arrivals once that time has passed - no fee."""
	props = frappe.get_all(
		"Property", filters={"disabled": 0,
		                     "non_guaranteed_release_time": ("is", "set")},
		pluck="name")
	for p in props:
		try:
			released = release_for_property(p)
			if released:
				frappe.db.commit()  # nosemgrep: frappe-manual-commit -- scheduler job persists each property's releases independently; reviewed as intentional
		except Exception:
			frappe.db.rollback()
			frappe.log_error(title=f"Non-guaranteed release failed: {p}")


def release_for_property(property: str, now: datetime | None = None) -> list[str]:
	"""Cancel (fee waived) today's Confirmed arrivals that are not guaranteed,
	once the property's release time has passed. Stays flagged Late Arrival
	and bookings made after the release time are left alone. Returns the
	released reservation names."""
	pol = policy(property)
	if not pol.release_time:
		return []
	now = now or property_now(property)
	if now.time() < pol.release_time:
		return []
	release_at = datetime.combine(now.date(), pol.release_time)
	# creation is on the site clock; shift it onto the property's
	from frappe.utils import now_datetime
	shift = property_now(property) - now_datetime()
	from kamra.api import _do_cancel
	from kamra.savings import log_action
	released = []
	for name in frappe.get_all(
			"Reservation",
			filters={"property": property, "status": "Confirmed",
			         "check_in_date": str(now.date())},
			pluck="name"):
		res = frappe.get_doc("Reservation", name)
		if cint(res.get("late_arrival")):
			continue
		created = get_datetime(res.creation) + shift
		if created >= release_at:
			continue
		if is_guaranteed(res):
			continue
		note = (f"Non-guaranteed arrival released at "
		        f"{pol.release_time:%H:%M} - no advance, deposit, OTA or "
		        f"company guarantee; no fee")
		_do_cancel(res, reason="Other", note=note, waive_fee=1)
		log_action("non_guaranteed_release", "Reservation", res.name, property,
		           rationale=f"{res.name} ({res.guest_name}) released at "
		                     f"{pol.release_time:%H:%M}: not guaranteed",
		           agent_name="Night Audit", autonomy="Full", channel="API")
		released.append(res.name)
	return released
