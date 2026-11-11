// Resolve a static asset shipped in frontend/public against the build base.
// Dev: BASE_URL is "/", so an asset resolves from the Vite public directory.
// Prod: BASE_URL is "/assets/kamra/frontend/", so the same call resolves to
// the corresponding static file served by Frappe.
export const asset = (path: string) =>
  import.meta.env.BASE_URL + path.replace(/^\//, "")
