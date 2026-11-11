export type Theme = "light" | "dark" | "system"

const KEY = "kamra-theme"
let themeRoot: HTMLElement | null = null

export const getTheme = (): Theme => {
  const t = localStorage.getItem(KEY)
  return t === "dark" || t === "system" ? t : "light"
}

const resolve = (t: Theme) =>
  t === "system"
    ? window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light"
    : t

export function applyTheme(t: Theme) {
  const dark = resolve(t) === "dark"
  document.documentElement.classList.toggle("dark", dark)
  themeRoot?.classList.toggle("dark", dark)
}

export function setTheme(t: Theme) {
  localStorage.setItem(KEY, t)
  applyTheme(t)
}

/** Apply the stored theme and return a disposer for the OS theme listener. */
export function initTheme(root?: HTMLElement) {
  themeRoot = root ?? null
  applyTheme(getTheme())
  const onChange = () => {
    if (getTheme() === "system") applyTheme("system")
  }
  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", onChange)
  return () => {
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .removeEventListener("change", onChange)
    if (themeRoot === root) themeRoot = null
  }
}
