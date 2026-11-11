"""The demo reset keeps the agent user that public /book writes as."""

from unittest.mock import patch

import frappe
from frappe.tests import IntegrationTestCase

from kamra.install import AGENT_EMAIL, AGENT_ROLE, ensure_agent_identity
from kamra.scripts import reset_demo


class ResetDemoAgentUserTestCase(IntegrationTestCase):
	def test_wipe_extra_users_spares_agent(self):
		# only these two users are offered to the wipe, so a test run never
		# deletes real users on the site
		extra = "test-reset-extra@example.test"
		with patch.object(reset_demo.frappe, "get_all", return_value=[AGENT_EMAIL, extra]), \
				patch.object(reset_demo.frappe, "delete_doc") as delete_doc:
			removed = reset_demo._wipe_extra_users()
		self.assertEqual(removed, 1)
		self.assertEqual([c.args[1] for c in delete_doc.call_args_list], [extra])

	def test_reset_recreates_a_missing_agent(self):
		# an older reset deleted the agent; the reset heals it with its role
		frappe.delete_doc("User", AGENT_EMAIL, force=1, ignore_permissions=True,
			delete_permanently=True)
		self.assertFalse(frappe.db.exists("User", AGENT_EMAIL))
		ensure_agent_identity()
		user = frappe.get_doc("User", AGENT_EMAIL)
		self.assertTrue(user.enabled)
		self.assertIn(AGENT_ROLE, {r.role for r in user.roles})

	def test_reset_leaves_an_enabled_agent(self):
		# the whole reset, with the destructive steps stubbed: even when the
		# wipe takes the agent out, reset() ends with it enabled and holding
		# its role, so the reseeded demo's /book still has a writer
		def wipe_users():
			frappe.delete_doc("User", AGENT_EMAIL, force=1, ignore_permissions=True,
				delete_permanently=True)
			return 1

		with patch.object(reset_demo, "is_playground", return_value=True), \
				patch.object(reset_demo, "_wipe_kamra_doctypes", return_value=0), \
				patch.object(reset_demo, "_wipe_core", return_value=0), \
				patch.object(reset_demo, "_wipe_extra_users", side_effect=wipe_users), \
				patch.object(reset_demo, "_reset_demo_passwords"), \
				patch("kamra.scripts.seed_demo.execute"), \
				patch.object(reset_demo.frappe.db, "commit"), \
				patch.object(reset_demo.frappe.db, "set_default"):
			out = reset_demo.reset()
		self.assertTrue(out["ok"])
		self.assertEqual(out["wiped"]["users"], 1)
		user = frappe.get_doc("User", AGENT_EMAIL)
		self.assertTrue(user.enabled)
		self.assertIn(AGENT_ROLE, {r.role for r in user.roles})
