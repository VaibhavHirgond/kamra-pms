// Frappe Desk hosts the same SPA at /desk/kamra; the website route remains
// available at /kamra for existing links and integrations.
export const ROUTER_BASENAME = import.meta.env.PROD
  ? window.location.pathname.startsWith("/desk/kamra-front-desk")
    ? "/desk/kamra-front-desk"
    : window.location.pathname.startsWith("/desk/kamra")
      ? "/desk/kamra"
      : "/kamra"
  : "/"

// Prefix an in-app path with the basename for a full-page navigation
// (window.location), which the router's own navigate() would otherwise add.
export function toFullPath(path: string): string {
  const base = ROUTER_BASENAME === "/" ? "" : ROUTER_BASENAME
  return base + (path.startsWith("/") ? path : "/" + path)
}
