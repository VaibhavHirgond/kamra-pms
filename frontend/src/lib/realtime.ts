import { useEffect } from "react"
/*  Live updates. Prefer Frappe's socket (nginx proxies /socket.io to the
    websocket service; the namespace is the SITE name, injected by
    kamra/www/kamra.py - not the hostname, which differs on a custom
    domain). A local bench has no nginx, so nothing proxies /socket.io on
    the webserver port - the page origin 404s and we retry the socketio
    service's own port (also injected by kamra.py) before falling back to
    polling while the tab is visible. Either way the caller just gets
    "something changed - re-fetch". */

export interface ChangeEvent {
  doctype?: string
  printer?: string
  property?: string | null
  outlet?: string | null
  name?: string
  /** the document was just created, not edited */
  is_new?: boolean
  /** hash of who made the change (see lib/notifications.ts `who`) */
  by?: string
}

export interface RealtimeOptions {
  /** Ignore pings this screen doesn't show (polling always re-fetches). */
  filter?: (e: ChangeEvent) => boolean
  /** Polling interval when the socket is down. Live screens (POS, kitchen)
   *  want seconds; dashboards are fine at the default. */
  fallbackMs?: number
  /** Socket event to listen for (default kamra_changed). */
  event?: string
}

// Bursts collapse to at most one re-fetch per window, and the LAST event of a
// burst always gets its re-fetch. A new order saves 2-4 times in a second;
// dropping the trailing ping meant the kitchen fetched before the KOT existed
// and missed it until the next safety-net poll.
const WINDOW_MS = 400

function siteName(): string {
  const w = window as unknown as { kamra_site?: string }
  return w.kamra_site || location.hostname
}

/** Where the socketio service can be reached. The page origin first (a
 *  production deploy proxies /socket.io there); then, when the boot page
 *  injected a socketio port and the origin isn't already on it, the
 *  service's own port - the local-bench case, same as the Desk client's
 *  dev_server path. */
function socketUrls(): string[] {
  const ns = `/${siteName()}`
  const urls = [`${location.origin}${ns}`]
  const w = window as unknown as { kamra_socketio_port?: number }
  const port = w.kamra_socketio_port
  if (port && location.port !== String(port)) {
    urls.push(`${location.protocol}//${location.hostname}:${port}${ns}`)
  }
  return urls
}

type Socket = ReturnType<(typeof import("socket.io-client"))["io"]>

/** Dial the first socket URL that answers. Resolves null when none do. */
function connectSocket(
  io: (url: string, opts?: Record<string, unknown>) => Socket,
  opts: Record<string, unknown>,
): Promise<Socket | null> {
  const urls = socketUrls()
  return new Promise((resolve) => {
    const attempt = (i: number) => {
      const s = io(urls[i], opts)
      s.once("connect", () => resolve(s))
      s.once("connect_error", () => {
        s.close()
        if (i + 1 < urls.length) attempt(i + 1)
        else resolve(null)
      })
    }
    attempt(0)
  })
}

export function subscribeRealtime(onChange: () => void, opts: RealtimeOptions = {}): () => void {
  let timer: ReturnType<typeof setInterval> | null = null
  let trailing: ReturnType<typeof setTimeout> | null = null
  let last = 0
  const fire = () => {
    const wait = WINDOW_MS - (Date.now() - last)
    if (wait <= 0) {
      last = Date.now()
      onChange()
    } else if (!trailing) {
      trailing = setTimeout(() => {
        trailing = null
        last = Date.now()
        onChange()
      }, wait)
    }
  }
  const onEvent = (e: ChangeEvent) => {
    if (opts.filter && e && !opts.filter(e)) return
    fire()
  }

  const startPolling = () => {
    if (timer) return
    timer = setInterval(() => {
      if (document.visibilityState === "visible") fire()
    }, opts.fallbackMs ?? 25000)
  }

  // socket.io-client is loaded on first subscribe, not in the entry chunk
  let socket: { close: () => void } | null = null
  let closed = false
  void import("socket.io-client")
    .then(({ io }) => {
      if (closed) return
      void connectSocket(io, {
        path: "/socket.io",
        withCredentials: true,
        reconnectionAttempts: 2,
        timeout: 4000,
      }).then((s) => {
        if (closed) {
          s?.close()
          return
        }
        if (!s) {
          startPolling()
          return
        }
        s.on(opts.event || "kamra_changed", onEvent)
        // after the first connect, socket.io reconnects on its own; a
        // dropped live channel just means "poll until it comes back"
        s.on("connect_error", startPolling)
        s.on("disconnect", startPolling)
        s.on("connect", () => {
          if (timer) {
            clearInterval(timer)
            timer = null
          }
        })
        socket = s
      })
    })
    .catch(startPolling)

  return () => {
    closed = true
    socket?.close()
    if (timer) clearInterval(timer)
    if (trailing) clearTimeout(trailing)
  }
}

/** Hook: re-run `onChange` whenever something changes on the property.
 * `onChange` should be stable (wrap in useCallback) so it doesn't
 * re-subscribe each render. Updates happen in place - no remount. */
export function useRealtime(onChange: () => void) {
  useEffect(() => subscribeRealtime(onChange), [onChange])
}

/** Is the live-update socket really delivering to this browser? Connects,
 *  runs `trigger` (which asks the server to ping this user) and resolves
 *  with how long the ping took to arrive, or null if it never did. */
export async function probeSocket(trigger: () => Promise<unknown>, timeoutMs = 5000): Promise<number | null> {
  const { io } = await import("socket.io-client")
  const s = await connectSocket(io, {
    path: "/socket.io", withCredentials: true, reconnectionAttempts: 1, timeout: 4000,
  })
  if (!s) return null
  try {
    const t0 = performance.now()
    const arrived = new Promise<number | null>((resolve) => {
      s.on("kamra_speed_ping", () => resolve(Math.round(performance.now() - t0)))
      setTimeout(() => resolve(null), timeoutMs)
    })
    await trigger()
    return await arrived
  } finally {
    s.close()
  }
}
