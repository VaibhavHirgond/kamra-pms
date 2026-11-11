# Kamra architecture (read when needed)

## Stack

Frappe v16 + `payments`. React 19 SPA at `/kamra`. MariaDB. Optional
ERPNext / Frappe HR on the same site — not a dependency.

```
Staff UI / REST token / Claude / copilot
        │
        ▼
kamra.<module>.<fn>   @whitelist + @require_roles
        │
        ▼
pricing · folio ledger · availability · policy
        │
        ▼
MariaDB  +  Agent Action Log
```

## MCP

- Hosted: `POST /mcp` Streamable HTTP, JSON-RPC 2.0, Bearer from OAuth 2.1
  (PKCE S256, scope `kamra.mcp`, grant = user + property).
- Versions: `2025-11-25`, `2025-03-26`, `2024-11-05`.
- Methods: `initialize`, `ping`, `tools/list`, `tools/call`.
- `call_tool` sets `frappe.flags.kamra_agent_call` (skips cashier PIN;
  identity is the OAuth user) and logs `mcp_<name>` when mutating.
- Stdio: `mcp/kamra_mcp.py` with `KAMRA_URL` + API key. Same `TOOLS` list.
- Connect UI: **Kamra Agent → Connect your AI**. Localhost/`http` disables
  Connect Claude (Anthropic cannot reach you).

Registry: `kamra/mcp_tools.py` (`TOOLS`, `GROUP_MODULE`, `TOOL_COUNT`).
Docs: `docs-site/gen_mcp_tools.py` → `mcp-tools.md`.

## REST

`POST /api/method/kamra.<module>.<fn>`
`Authorization: token <api_key>:<api_secret>`

Response `{ "message": <value> }`. Generate keys on Developers or
Connect your AI (role-scoped). Regenerators: `docs-site/gen_api.py`.

Webhooks: `kamra.payments.razorpay_webhook`,
`kamra.channel_manager.webhook`, `kamra.whatsapp.webhook`.

## Stay lifecycle

Quote → book (desk `create_booking` / public `public_api.book`) →
optional hold / host approve → pre-check-in token → check-in (folio
opens) → charges/payments/POS/HK → night audit → check-out → close
folio (invoice number assigned once).

Instant public book snapshots the payment policy. Request-to-book does
not hold inventory until confirmed.

## Hard money rules

- Rate guardrails: `set_room_rate` cannot leave the owner's floor/ceiling.
- Hurdle rates: demand premium + minimum sell rate by occupancy.
- Folios are append-only (Guest / Deposit / AR / Package). Voids are
  reversals. Close requires zero balance (or part-settle).
- Cashier: open session + optional PIN for humans; agents bypass PIN
  and stay on the activity log.
- Localization pack picks tax split and currency words. India GST slabs
  are per night from the tariff.

## Local bench (this workspace)

```
# containers
cd /Users/azzax/Workspace/agenticpms/frappe_docker
docker compose -f .devcontainer/docker-compose.yml -p kamra-dev up -d

# Frappe :8000
docker exec -d -w /workspace/development/frappe-bench kamra-dev-frappe-1 \
  bash -c "bench serve --port 8000 >> /tmp/bench-serve.log 2>&1"

# SPA :5173
cd /Users/azzax/Workspace/agenticpms/kamra/frontend && npm run dev
```

| Surface | URL |
| --- | --- |
| Vite SPA | http://localhost:5173 |
| Frappe | http://kamra.localhost:8000 |
| Public demo | https://demo.kamrapms.com/kamra |
| Nightly | https://nightly.kamrapms.com |

Demo users are seeded (`kamra.scripts.seed_users`) and printed on the
demo login screen. Do not use the playground as a live hotel.

```
bench --site kamra.localhost migrate
bench --site kamra.localhost execute kamra.scripts.seed_demo.execute
```

## Scheduler (hooks.py)

Hourly ARI push; 03:00 night audit; 09:00 pre-arrival links; every 15 min
HK escalation + hold expiry; 08:30 banquet reminders; 04:15 demo reset
(no-op unless `kamra_demo_mode`).

## Related docs in-repo

- `CONTRIBUTING.md` — branches, commits, PR gates
- `RELEASING.md` — patch-first trains
- `docs-dev.md` — local Docker notes (some version labels lag)
- `docs-site/` — what we publish to kamrapms.com/docs
