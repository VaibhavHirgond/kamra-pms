window.kamraDeskSpa = (() => {
	const REGISTERED_PROPERTY_STYLE_ID = "kamra-desk-registered-properties";
	let activeWrapper = null;
	let appAssetsPromise = null;
	let stylesheet = null;
	let stylesheetPromise = null;
	let scriptPromise = null;
	let stylesheetUrl = null;
	let scriptUrl = null;
	let mountedWrapper = null;
	let appHost = null;
	let appShadow = null;

	// Tailwind declares its --tw-* defaults with @property. @property is
	// document-scoped: browsers ignore it inside a shadow tree, so the
	// stylesheet living in our shadow root registers nothing there and every
	// var(--tw-*) read (border-style, shadows, rings, transforms) collapses to
	// its invalid value -- which is what stripped borders and shadows from this
	// route. Re-declare the same registrations on the outer document, where
	// they reach the shadow tree too, so /desk/kamra matches /kamra.
	function registerCustomProperties(sheet) {
		if (!sheet) return;

		const rules = [];
		const walk = (list) => {
			for (const rule of list) {
				if (rule.cssRules) {
					walk(rule.cssRules);
					continue;
				}
				const cssText = rule.cssText || "";
				if (cssText.startsWith("@property")) rules.push(cssText);
			}
		};

		try {
			walk(sheet.cssRules);
		} catch (error) {
			return;
		}

		if (!rules.length) return;

		let style = document.getElementById(REGISTERED_PROPERTY_STYLE_ID);
		if (!style) {
			style = document.createElement("style");
			style.id = REGISTERED_PROPERTY_STYLE_ID;
			document.head.appendChild(style);
		}
		style.textContent = rules.join("\n");
	}

	function unregisterCustomProperties() {
		const style = document.getElementById(REGISTERED_PROPERTY_STYLE_ID);
		if (style) style.remove();
	}

	async function getAssetUrls() {
		if (!appAssetsPromise) {
			appAssetsPromise = (async () => {
				const response = await fetch("/kamra", { credentials: "same-origin" });
				if (!response.ok) {
					throw new Error(`Could not load Hotel app assets (${response.status})`);
				}

				const html = await response.text();
				const parsed = new DOMParser().parseFromString(html, "text/html");
				const css = parsed.querySelector('link[rel="stylesheet"][href]');
				const module = parsed.querySelector('script[type="module"][src]');
				if (!css || !module) {
					throw new Error("Hotel app stylesheet or module script was not found");
				}
				stylesheetUrl = css.href;
				scriptUrl = module.src;
			})();
		}

		try {
			await appAssetsPromise;
		} catch (error) {
			appAssetsPromise = null;
			throw error;
		}
	}

	async function loadAssets() {
		await getAssetUrls();
		window.kamraDeskManaged = true;

		if (!stylesheet) {
			stylesheet = document.createElement("link");
			stylesheet.rel = "stylesheet";
			stylesheet.href = stylesheetUrl;
			stylesheet.dataset.kamraDeskStylesheet = "true";
			const link = stylesheet;
			stylesheetPromise = new Promise((resolve, reject) => {
				link.onload = resolve;
				link.onerror = () => reject(new Error("Could not load Hotel app stylesheet"));
			});
			appShadow.appendChild(link);
			try {
				await stylesheetPromise;
			} catch (error) {
				link.remove();
				stylesheet = null;
				stylesheetPromise = null;
				throw error;
			}
		}
		await stylesheetPromise;
		registerCustomProperties(stylesheet && stylesheet.sheet);

		if (!scriptPromise) {
			scriptPromise = new Promise((resolve, reject) => {
				const script = document.createElement("script");
				script.type = "module";
				script.src = scriptUrl;
				script.onload = resolve;
				script.onerror = () => reject(new Error("Could not load Hotel app module"));
				document.head.appendChild(script);
			}).catch((error) => {
				scriptPromise = null;
				throw error;
			});
		}
		await scriptPromise;
	}

	async function mount(wrapper) {
		activeWrapper = wrapper;
		if (!appHost) {
			appHost = document.createElement("div");
			appHost.id = "kamra-desk-overlay";
			Object.assign(appHost.style, {
				position: "fixed",
				inset: "0",
				zIndex: "99999",
				overflow: "auto",
			});
			appShadow = appHost.attachShadow({ mode: "open" });
			const root = document.createElement("div");
			root.id = "root";
			root.className = "min-h-screen bg-zinc-50 text-zinc-900 antialiased";
			appShadow.appendChild(root);
			document.body.appendChild(appHost);
		}

		await loadAssets();
		if (activeWrapper !== wrapper || !wrapper.kamraActive) return;
		const root = appShadow.querySelector("#root");
		if (!(root instanceof HTMLElement)) throw new Error("Hotel app root was not created");
		window.kamraMount(root);
		mountedWrapper = wrapper;
	}

	function unmount(wrapper) {
		if (activeWrapper !== wrapper) return;
		activeWrapper = null;
		if (mountedWrapper === wrapper) {
			window.kamraUnmount();
			mountedWrapper = null;
		}
		appHost?.remove();
		appHost = null;
		appShadow = null;
		stylesheet?.remove();
		stylesheet = null;
		stylesheetPromise = null;
		unregisterCustomProperties();
	}

	return { mount, unmount };
})();
