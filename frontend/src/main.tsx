import { StrictMode } from "react"
import { createRoot, type Root } from "react-dom/client"
import { BrowserRouter } from "react-router-dom"
import "./index.css"
import App from "./App"
import { initTheme } from "./lib/theme"
import { initLang } from "./lib/dir"
import { asset } from "./lib/asset"
import { AuthProvider } from "./lib/auth"
import { CashierAuthProvider } from "./lib/cashierAuth"
import { ROUTER_BASENAME } from "./lib/routing"

declare global {
  interface Window {
    kamraDeskManaged?: boolean
    kamraMount?: (element: HTMLElement) => void
    kamraUnmount?: () => void
  }
}

let reactRoot: Root | null = null
let restoreDocumentState: (() => void) | null = null
let faviconLinks: HTMLLinkElement[] = []

function setIcon(rel: string, href: string, type?: string) {
  const link = document.createElement("link")
  link.rel = rel
  link.href = asset(href)
  if (type) link.type = type
  document.head.appendChild(link)
  return link
}

function mount(element: HTMLElement) {
  if (reactRoot) return

  const html = document.documentElement
  const previousTitle = document.title
  const previousLang = html.getAttribute("lang")
  const previousDir = html.getAttribute("dir")
  const hadDarkClass = html.classList.contains("dark")
  const stopTheme = initTheme(element)
  initLang()
  faviconLinks = [
    setIcon("icon", "logo-512.png", "image/png"),
    setIcon("apple-touch-icon", "logo-512.png", "image/png"),
  ]

  reactRoot = createRoot(element)
  reactRoot.render(
    <StrictMode>
      <BrowserRouter basename={ROUTER_BASENAME}>
        <AuthProvider>
          <CashierAuthProvider>
            <App />
          </CashierAuthProvider>
        </AuthProvider>
      </BrowserRouter>
    </StrictMode>,
  )

  restoreDocumentState = () => {
    stopTheme()
    html.classList.toggle("dark", hadDarkClass)
    if (previousLang === null) html.removeAttribute("lang")
    else html.setAttribute("lang", previousLang)
    if (previousDir === null) html.removeAttribute("dir")
    else html.setAttribute("dir", previousDir)
    document.title = previousTitle
    faviconLinks.forEach((link) => link.remove())
    faviconLinks = []
    restoreDocumentState = null
  }
}

function unmount() {
  if (!reactRoot) return
  reactRoot.unmount()
  reactRoot = null
  restoreDocumentState?.()
}

window.kamraMount = mount
window.kamraUnmount = unmount

if (!window.kamraDeskManaged) {
  const root = document.getElementById("root")
  if (!root) throw new Error("Hotel app root element was not found")
  mount(root)
}
