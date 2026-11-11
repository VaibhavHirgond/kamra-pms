import { useEffect, useState } from "react"

import { login } from "../lib/api"
import { asset } from "../lib/asset"
import { Button } from "../components/ui/button"
import { getSiteInfo } from "../lib/siteInfo"
import { LANGS, getLang, setLang, type Lang } from "../lib/dir"
import { useT, t as translate } from "../lib/i18n"


const inputCls =
  "w-full rounded-lg border border-zinc-300 bg-white px-3 py-2 text-sm " +
  "text-zinc-900 placeholder:text-zinc-500 " +
  "focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-brand-600"

const DEMO_ACCOUNTS = [
  { label: "System Admin", usr: "admin@kamra.local", pwd: "KamraAdmin1!" },
  { label: "Hotel Admin (GM)", usr: "gm@kamra.local", pwd: "KamraGM1!" },
  { label: "Front Desk", usr: "frontdesk@kamra.local", pwd: "KamraDesk1!" },
  { label: "Revenue", usr: "revenue@kamra.local", pwd: "KamraRev1!" },
  { label: "Finance", usr: "finance@kamra.local", pwd: "KamraFin1!" },
  { label: "Housekeeping", usr: "hk@kamra.local", pwd: "KamraHK1!" },
]

export default function Login(props: { onSuccess: () => void }) {
  const { t, lang } = useT()
  const [usr, setUsr] = useState("")
  const [pwd, setPwd] = useState("")
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  // Demo accounts only exist on the seeded demo site; hide them elsewhere.
  const [demoMode, setDemoMode] = useState(false)
  const [langState, setLangState] = useState<Lang>(lang || getLang())

  useEffect(() => {
    setLangState(lang)
  }, [lang])

  useEffect(() => {
    getSiteInfo().then((info) => {
      setDemoMode(Boolean(info.demo_mode))
    })
  }, [])

  async function submit(u = usr, p = pwd) {
    setBusy(true)
    setError(null)
    try {
      await login(u, p)
      // Navigation + the production CSRF re-boot are handled by the /login
      // route (LoginPage.onSuccess).
      sessionStorage.removeItem("kamra_session_ended")
      props.onSuccess()
    } catch {
      setError(t("Wrong email, username, or password."))
    } finally {
      setBusy(false)
    }
  }

  const sessionEnded = sessionStorage.getItem("kamra_session_ended") === "1"

  return (
    <div className="flex min-h-[100dvh] flex-col items-center justify-center bg-zinc-50 px-4 text-zinc-900">
      <div
        className="fixed inset-x-0 top-0 h-[5px]"
        style={{ background: "linear-gradient(105deg, #453D89, #C8499A)" }}
        aria-hidden
      />
      <div className="w-full max-w-sm">
        {sessionEnded && (
          <p className="mb-4 rounded border border-amber-200 bg-amber-50 px-4 py-2.5 text-center text-sm text-amber-800">
            {t("Your session ended. Sign in to pick up where you left off.")}
          </p>
        )}
        <div className="mb-6 flex flex-col items-center gap-2">
          <img
            src={asset("Logo_print.png")}
            alt="Quantumberg"
            className="h-16 w-auto max-w-full object-contain"
          />
          <label className="mt-1 flex items-center gap-2 text-xs text-zinc-600">
            <span>{t("Language")}</span>
            <select
              className="rounded-lg border border-zinc-300 bg-white px-2 py-1 text-xs text-zinc-800"
              value={langState}
              onChange={(e) => {
                const next = e.target.value as Lang
                setLang(next)
                setLangState(next)
              }}
              aria-label={t("Language")}
            >
              {LANGS.map((l) => (
                <option key={l.code} value={l.code}>
                  {l.nativeLabel}
                </option>
              ))}
            </select>
          </label>
        </div>

        <form
          className="space-y-3 rounded-xl border border-zinc-200 bg-white p-6 shadow-sm"
          onSubmit={(e) => {
            e.preventDefault()
            submit()
          }}
        >
          <label className="block">
            <span className="mb-1 block text-xs font-medium text-zinc-700">
              {t("Email or username")}
            </span>
            <input
              className={inputCls}
              type="text"
              autoComplete="username"
              autoCapitalize="none"
              autoCorrect="off"
              spellCheck={false}
              value={usr}
              onChange={(e) => setUsr(e.target.value)}
              placeholder={t("Administrator or you@hotel.com")}
            />
          </label>
          <label className="block">
            <span className="mb-1 block text-xs font-medium text-zinc-700">
              {t("Password")}
            </span>
            <input
              className={inputCls}
              type="password"
              autoComplete="current-password"
              value={pwd}
              onChange={(e) => setPwd(e.target.value)}
            />
          </label>

          {error && (
            <div className="rounded-lg border border-rose-200 bg-rose-50 px-3 py-2 text-sm text-rose-800">
              {translate(error)}
            </div>
          )}

          <Button
            className="w-full justify-center rounded bg-[linear-gradient(105deg,#453D89,#C8499A)] py-2 text-white hover:opacity-90 focus-visible:outline-[#453D89]"
            disabled={busy || !usr || !pwd}
            type="submit"
          >
            {busy ? t("Signing in...") : t("Sign in")}
          </Button>
        </form>

        {demoMode && (
        <div className="mt-4 rounded-xl border border-dashed border-zinc-300 p-4">
          <p className="mb-3 rounded-lg border border-amber-200 bg-amber-50 px-3 py-2 text-center text-xs leading-relaxed text-amber-800">
            {t("Shared playground, not a live hotel. Play data is wiped every night and the sample hotel is seeded again. Don't put real guests, payments or API keys here.")}
          </p>
          <p className="mb-2 text-center text-xs text-zinc-600">
            {t("Demo accounts - one tap to try each role")}
          </p>
          <div className="grid grid-cols-2 gap-2">
            {DEMO_ACCOUNTS.map((a) => (
              <button
                key={a.usr}
                disabled={busy}
                onClick={() => submit(a.usr, a.pwd)}
                className="rounded-lg border border-zinc-300 bg-white px-2 py-1.5 text-xs font-medium text-zinc-700 hover:border-brand-600 hover:text-brand-700 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-600"
              >
                {t(a.label)}
              </button>
            ))}
          </div>
        </div>
        )}
        <p className="mt-6 text-center text-[11px] text-zinc-600">Quantumberg</p>
      </div>
    </div>
  )
}
