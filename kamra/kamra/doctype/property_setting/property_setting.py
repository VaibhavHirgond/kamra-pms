# Copyright (c) 2026, HeyKoala and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class PropertySetting(Document):
	"""One module setting for one property. Written only through
	kamra.settings.save_settings, which validates against the registry."""

	def on_update(self):
		from kamra.settings import clear_cache

		clear_cache(self.property)

	def on_trash(self):
		from kamra.settings import clear_cache

		clear_cache(self.property)
