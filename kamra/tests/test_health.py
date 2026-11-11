"""System health checks (kamra.health) and the twice-daily GitHub poll.

GitHub is never contacted: urlopen is patched. The release cache lives in
redis, outside the test transaction, so it is saved in setUp and put back
in tearDown.
"""

from __future__ import annotations

import json
from collections import namedtuple
from unittest.mock import MagicMock, patch
from urllib.error import URLError

import frappe

from kamra import health
from kamra.tests.audit_fixtures import AuditTestCase, ensure_user

STATUSES = {"passed", "attention", "failed", "info"}
CHECK_IDS = {"version", "frappe", "apps", "database", "scheduler", "disk",
             "timezone"}
Usage = namedtuple("Usage", "total used free")
GB = 1024 ** 3


def _bump(version: str, minor: int = 0, patch_: int = 0) -> str:
	a, b, c = (int(x) for x in version.split(".")[:3])
	return f"v{a}.{b + minor}.{c + patch_}"


def github(tag: str):
	"""A urlopen stand-in that answers like the releases/latest API."""
	resp = MagicMock()
	resp.read.return_value = json.dumps({
		"tag_name": tag, "name": tag, "html_url": f"https://example.test/{tag}",
		"published_at": "2031-01-01T00:00:00Z", "body": "notes"}).encode()
	opener = MagicMock()
	opener.return_value.__enter__.return_value = resp
	return patch("kamra.health.urlopen", opener)


class HealthTestCase(AuditTestCase):
	properties = ()

	def setUp(self):
		super().setUp()
		self._cached = frappe.cache.get_value(health.CACHE_KEY)
		frappe.cache.delete_value(health.CACHE_KEY)

	def tearDown(self):
		frappe.cache.delete_value(health.CACHE_KEY)
		if self._cached is not None:
			frappe.cache.set_value(health.CACHE_KEY, self._cached,
			                       expires_in_sec=health.FAIL_TTL)
		super().tearDown()

	def by_id(self, out):
		return {c["id"]: c for c in out["checks"]}

	# structure -------------------------------------------------------------

	def test_returns_a_structured_result_for_every_check(self):
		with github(f"v{health.KAMRA_VERSION}"):
			out = health.system_health()
		self.assertEqual({c["id"] for c in out["checks"]}, CHECK_IDS)
		for c in out["checks"]:
			self.assertEqual(set(c), {"id", "title", "status", "detail", "link"})
			self.assertIn(c["status"], STATUSES, c["id"])
			self.assertTrue(c["title"] and c["detail"], c["id"])
		self.assertEqual(sum(out["summary"].values()), len(out["checks"]))
		for s in STATUSES:
			self.assertEqual(out["summary"][s],
			                 sum(1 for c in out["checks"] if c["status"] == s))
		self.assertIn(out["overall"], {"passed", "attention", "failed"})
		self.assertEqual(out["installed"]["kamra"], health.KAMRA_VERSION)
		self.assertEqual(out["installed"]["site"], frappe.local.site)
		self.assertIn("bench", out["upgrade"])

	def test_happy_path_core_checks_pass(self):
		with github(f"v{health.KAMRA_VERSION}"):
			checks = self.by_id(health.system_health())
		self.assertEqual(checks["version"]["status"], "passed")
		self.assertEqual(checks["database"]["status"], "passed")
		self.assertEqual(checks["apps"]["status"], "passed")
		self.assertEqual(checks["frappe"]["status"], "passed")

	def test_overall_is_the_worst_check(self):
		low_disk = Usage(100 * GB, 99 * GB, 1 * GB)
		with github(f"v{health.KAMRA_VERSION}"), \
		     patch("kamra.health.shutil.disk_usage", return_value=low_disk):
			out = health.system_health()
		self.assertEqual(self.by_id(out)["disk"]["status"], "failed")
		self.assertEqual(out["overall"], "failed")
		self.assertGreaterEqual(out["summary"]["failed"], 1)

	def test_attention_when_behind_latest_release(self):
		plenty = Usage(100 * GB, 10 * GB, 90 * GB)
		with github(_bump(health.KAMRA_VERSION, minor=1)), \
		     patch("kamra.health.shutil.disk_usage", return_value=plenty), \
		     patch("kamra.health._scheduler_check",
		           return_value=health._check("scheduler", "Scheduler",
		                                      "passed", "on")), \
		     patch("kamra.health._timezone_check",
		           return_value=health._check("timezone", "Time zone",
		                                      "passed", "ok")):
			out = health.system_health()
		self.assertEqual(self.by_id(out)["version"]["status"], "attention")
		self.assertEqual(out["overall"], "attention")

	# individual checks ------------------------------------------------------

	def test_database_check_reports_a_failing_database(self):
		with patch.object(frappe.local.db, "sql",
		                  side_effect=Exception("gone away")):
			c = health._database_check()
		self.assertEqual(c["status"], "failed")
		self.assertIn("gone away", c["detail"])

	def test_disk_check_thresholds(self):
		# 50 GB disk: under 2 GB free fails, under 5 GB needs attention
		for free, expect in ((1, "failed"), (4, "attention"), (40, "passed")):
			with patch("kamra.health.shutil.disk_usage",
			           return_value=Usage(50 * GB, (50 - free) * GB, free * GB)):
				self.assertEqual(health._disk_check()["status"], expect, free)

	def test_disk_check_unmeasurable_is_info(self):
		with patch("kamra.health.shutil.disk_usage", side_effect=OSError("nope")):
			c = health._disk_check()
		self.assertEqual(c["status"], "info")

	def test_scheduler_check_follows_system_settings(self):
		with patch.object(frappe.local.db, "get_single_value", return_value=0):
			off = health._scheduler_check()
		with patch.object(frappe.local.db, "get_single_value", return_value=1):
			on = health._scheduler_check()
		self.assertEqual(off["status"], "attention")
		self.assertEqual(off["link"], "/app/system-settings")
		self.assertEqual(on["status"], "passed")

	def test_apps_check_flags_a_missing_required_app(self):
		with patch.object(frappe, "get_installed_apps", return_value=["frappe"]):
			c = health._apps_check()
		self.assertEqual(c["status"], "failed")
		self.assertIn("kamra", c["detail"])

	def test_frappe_check_flags_an_old_major(self):
		with patch.object(frappe, "__version__", "15.2.0"):
			self.assertEqual(health._frappe_check()["status"], "attention")

	def test_timezone_check_is_structured(self):
		c = health._timezone_check()
		self.assertEqual(c["id"], "timezone")
		self.assertIn(c["status"], STATUSES)

	def test_version_check_states(self):
		v = health.KAMRA_VERSION
		ok = {"ok": True, "url": "u"}
		self.assertEqual(health._version_check({**ok, "tag": f"v{v}"})["status"],
		                 "passed")
		self.assertEqual(health._version_check(
			{**ok, "tag": _bump(v, patch_=1)})["status"], "attention")
		self.assertEqual(health._version_check(
			{**ok, "tag": "v0.0.1"})["status"], "info")  # ahead of GitHub
		self.assertEqual(health._version_check(
			{**ok, "tag": "nightly"})["status"], "info")  # unparsable
		self.assertEqual(health._version_check(
			{"ok": False, "tag": None, "error": "x"})["status"], "info")

	# GitHub cache -----------------------------------------------------------

	def test_github_unreachable_is_info_and_cached(self):
		opener = MagicMock(side_effect=URLError("offline"))
		with patch("kamra.health.urlopen", opener):
			first = health.system_health()
			second = health.system_health()
		self.assertEqual(self.by_id(first)["version"]["status"], "info")
		self.assertFalse(first["latest"]["ok"])
		self.assertEqual(self.by_id(second)["version"]["status"], "info")
		# the failure is cached: an offline site is asked once, not per load
		self.assertEqual(opener.call_count, 1)

	def test_refresh_bypasses_the_cache(self):
		with github(f"v{health.KAMRA_VERSION}") as opener:
			health.system_health()
			health.system_health()
			self.assertEqual(opener.call_count, 1)
			health.system_health(refresh=1)
			self.assertEqual(opener.call_count, 2)

	def test_poll_github_releases_refreshes_the_cache(self):
		frappe.cache.set_value(health.CACHE_KEY, {"ok": True, "tag": "v0.0.0"})
		with github("v9.9.9") as opener:
			health.poll_github_releases()
		opener.assert_called_once()
		self.assertEqual(frappe.cache.get_value(health.CACHE_KEY)["tag"], "v9.9.9")

	def test_poll_github_releases_survives_github_being_down(self):
		with patch("kamra.health.urlopen", side_effect=URLError("offline")):
			health.poll_github_releases()  # must not raise in the scheduler
		self.assertFalse(frappe.cache.get_value(health.CACHE_KEY)["ok"])

	# update nag -------------------------------------------------------------

	def test_update_nag_lifecycle(self):
		newer = _bump(health.KAMRA_VERSION, minor=1)
		# a developer site may run in demo mode, which hides the nag
		self._stack.enter_context(
			patch.object(frappe.local.db, "get_default", return_value=None))
		with github(newer):
			self.assertTrue(health.update_nag()["available"])
			health.dismiss_update_nag(newer)
			out = health.update_nag()
		self.assertFalse(out["available"])
		self.assertEqual(out["reason"], "dismissed")
		# a still newer release brings it back
		frappe.cache.delete_value(health.CACHE_KEY)
		with github(_bump(health.KAMRA_VERSION, minor=2)):
			self.assertTrue(health.update_nag()["available"])

	def test_update_nag_is_off_on_the_demo(self):
		with patch.object(frappe.local.db, "get_default", return_value="1"):
			self.assertEqual(health.update_nag(),
			                 {"available": False, "reason": "demo"})

	# access -----------------------------------------------------------------

	def test_only_admins_see_system_health(self):
		ensure_user("ut.health.desk@test.local", ["Front Desk"])
		ensure_user("ut.health.admin@test.local", ["Hotel Admin"])
		with github(f"v{health.KAMRA_VERSION}"):
			frappe.set_user("ut.health.desk@test.local")  # nosemgrep: frappe-setuser -- persona
			with self.assertRaises(frappe.PermissionError):
				health.system_health()
			frappe.set_user("ut.health.admin@test.local")  # nosemgrep: frappe-setuser -- persona
			self.assertIn("checks", health.system_health())
