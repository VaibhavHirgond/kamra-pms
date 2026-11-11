function mountHotelApp(wrapper) {
	wrapper.kamraActive = true;
	frappe.require("/assets/kamra/js/desk_spa_v2.js").then(() => {
		if (wrapper.kamraActive) return window.kamraDeskSpa.mount(wrapper);
	}).catch((error) => {
		console.error("Hotel Desk app failed to mount", error);
		frappe.msgprint(__("Hotel could not be loaded. See the browser console for details."));
	});
}

frappe.pages["kamra-front-desk"].on_page_load = function (wrapper) {
	wrapper.on_page_show = () => mountHotelApp(wrapper);
	$(wrapper).on("hide.kamra", () => {
		wrapper.kamraActive = false;
		window.kamraDeskSpa?.unmount(wrapper);
	});
};
