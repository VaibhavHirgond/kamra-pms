<p align="center">
  <img src="../frontend/public/quantumberg-logo.png" alt="Quantumberg Technologies" />
</p>

<h1 align="center">Quantumberg PMS Operations Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Front Desk, Hotel Administrators, Operations and Engineering staff

---

## Table of Contents

1. Introduction
2. Access, Navigation and Roles
3. Guest Requests (Service Tickets)
4. Ticket Priorities, Deadlines and Assignment
5. Ticket Status and Resolution Workflow
6. WhatsApp Inbox
7. Channels
8. Reports
9. Operations Settings
10. End-to-End Operations Workflows
11. Troubleshooting
12. Source Verification and Runtime Variations

---

## 1. Introduction

The Operations app brings guest service requests, guest messaging, communication-channel connections, operational reporting and request deadlines together. This guide describes the controls implemented in the current application; available pages and records vary by role, property access and enabled modules.

> **Property scope:** The property selected in the top bar determines which operational records are displayed or configured. Check it before creating a ticket, reviewing messages or editing a channel.

## 2. Access, Navigation and Roles

### 2.1 Open Operations

Sign in to Quantumberg, open the app switcher in the top bar, and select **Operations**. The app launcher’s **View all apps** page is another way to open the app. Use the Operations sidebar to open:

| Sidebar page | Purpose | Route |
|---|---|---|
| Guest Requests (Tickets) | View, create, assign and resolve guest/service requests | `/tickets` |
| WhatsApp | Read guest conversations and send eligible replies | `/whatsapp` |
| Channels | Configure phone and messaging connections | `/channels` |
| Reports | Open reports visible to the current role and enabled modules | `/reports` |
| Settings | Set ticket overdue deadlines | `/settings/operations` |

Routes are relative to the app base. For example, the standalone site uses `/kamra/tickets`; the Desk-mounted app uses `/desk/kamra/tickets`.

### 2.2 Role and permission notes

- The Operations app is listed for **Front Desk, Hotel Admin, System Manager and Administrator** roles. Individual sidebar entries have additional role gates.
- **Channels** and **Operations Settings** are listed for **Hotel Admin, System Manager and Administrator**.
- The ticket service endpoints permit **Front Desk, Housekeeping, Housekeeping Supervisor, Hotel Admin and Kamra Agent**; the actual navigation entry is still subject to the app and user’s role grants.
- WhatsApp inbox and reply endpoints permit **Front Desk, Hotel Admin and Kamra Agent**.
- Ticket, message and channel records are scoped to properties the user can access. Backend authorization is enforced in addition to menu visibility.
- The Operations Settings module’s editable role is **Hotel Admin**. Other users may have view-only access or may not see the page.

If a page is absent, ask an administrator to confirm the user’s role, property access and whether the Operations module is enabled. Do not use another person’s login to work around access controls.

## 3. Guest Requests (Service Tickets)

Open **Operations → Guest Requests (Tickets)**. The page displays the **Service Tickets** list. New guest requests may also arrive from connected guest channels; the ticket’s source badge identifies non-manual origins when present.

### 3.1 Views and filters

The view tabs show counts and filter the list:

| View | What it shows |
|---|---|
| Open | Tickets in Open or In Progress status |
| Mine | Open tickets assigned to the signed-in user |
| Unassigned | Open tickets without an assignee |
| Overdue | Open tickets whose deadline has passed |
| Resolved | Resolved and Closed tickets |
| All | Tickets for the selected property |

Use the controls below the tabs to narrow the results:

- **Search subject, room, guest, id:** searches request text and ticket identifiers (and associated room/guest text).
- **Category:** All categories, Housekeeping, Room Service, Maintenance, Front Desk, Concierge, Complaint or Other.
- **Priority:** Any priority, Low, Medium, High or Urgent.
- **Age:** Any age or open tickets older than 1, 3, 7 or 30 days.

Each row displays the subject, priority, category, source when applicable, remaining time or overdue duration, ticket identifier, room/guest where available, age, assignee or resolver, and action buttons. Select the subject or **Open** to open its detail sheet. **Take it** is available for an unassigned open request.

### 3.2 Create a ticket

1. Select **New ticket**.
2. Enter a required **Subject** describing what the guest needs.
3. Choose a **Category** and **Priority**.
4. Optionally select a **Room** or choose **No room**.
5. Add optional **Details** for staff.
6. Select **Create ticket**. Select **Cancel** to leave without creating it.

The deadline is calculated from the priority’s Operations Settings value at creation. Avoid putting unnecessary sensitive guest information into the free-text subject or details.

### 3.3 Ticket details

The detail sheet shows:

- Ticket identifier, category, subject, source, room and guest when available.
- Priority and current status badges.
- Age, time remaining or time overdue, first-response time, resolution time and SLA state.
- Request description and assignment information.
- The chronological event timeline: creation, assignment, status changes, notes and reopening events.

Ticket details are accessed from the list; URL query state may preserve the selected ticket when the list is shared within the application.

## 4. Ticket Priorities, Deadlines and Assignment

### 4.1 Priority levels

Priority is selected when a manual ticket is created. The list uses distinct badges for **Urgent**, **High**, **Medium** and **Low**. Priority determines the deadline interval; it is not a status.

| Priority | Default deadline after creation |
|---|---:|
| Urgent | 15 minutes |
| High | 30 minutes |
| Medium | 60 minutes |
| Low | 240 minutes (4 hours) |

These are defaults. A Hotel Admin can change the intervals under **Settings → Operations → Guest request deadlines**. See [Operations Settings](#9-operations-settings).

### 4.2 Assignment

In the ticket detail sheet, **Who has it** displays the assignee:

- Choose an eligible staff member from the assignee dropdown to assign or reassign an open ticket.
- Choose **Unassigned** to clear the assignment.
- Select **Assign to me** to claim the ticket for yourself.
- **Take it** in the list is a shortcut for claiming an unassigned open ticket.
- When work starts on an unassigned ticket, **Start work** assigns it to the current user automatically.

The selectable staff list includes active system users with an eligible Front Desk, Housekeeping, Housekeeping Supervisor or Hotel Admin role and access to the selected property. Resolved/closed/cancelled tickets cannot be assigned until reopened.

## 5. Ticket Status and Resolution Workflow

The detail sheet uses actions rather than a free-form status dropdown:

| Current state | Action | Result |
|---|---|---|
| Open | Start work | Moves to In Progress; assigns to the current user if unassigned |
| Open or In Progress | Mark solved | Moves to Resolved and records the optional resolution note |
| Resolved, Closed or Cancelled | Reopen | Moves back to Open, clears the resolution note and records the reason |

The UI’s standard **Mark solved** action creates a Resolved ticket. The server model also recognizes Closed and Cancelled as completed states, but this detail sheet does not expose a separate close or cancel button.

### 5.1 Complete ticket handling

1. Review the Open and Overdue counts and filter by priority or category.
2. Open the request and verify its room, description, source and deadline.
3. Assign it to the responsible eligible staff member, or claim it.
4. Select **Start work** when work begins. Record progress in the timeline using **Add a note** (for example, whom staff contacted or what was attempted).
5. Enter what was done in the resolution field and select **Mark solved**.
6. If the guest reports that the issue returned, enter a reopening reason of at least three characters and select **Reopen**. The request returns to Open and the reason is retained in the timeline.

The resolution text and timeline notes are retained with the ticket. The interface does not provide a separate priority-edit control after creation.

## 6. WhatsApp Inbox

Open **Operations → WhatsApp** to view guest conversations for the selected property. The left column lists conversations by guest/phone number, last message and time. Select a thread to load its messages in the conversation pane. A stay link may appear when the thread is associated with a reservation.

### 6.1 Reply to a guest

1. Select the guest thread.
2. Review the conversation and the session-window notice above the reply field.
3. Type a reply in **Reply to the guest…**.
4. Select **Send** or press **Enter** (Shift+Enter does not send).

Threads refresh periodically, and the conversation refreshes periodically while open. The inbox displays inbound/outbound direction, message/template labels, timestamps, delivery status and any provider error returned for an outbound message.

### 6.2 WhatsApp session window

A guest’s inbound message opens the WhatsApp 24-hour service window. The inbox permits free-form text replies, but the provider only delivers those within the open session. Outside the window, the guest must send another message to reopen it; WhatsApp-approved templates are required for outbound messages outside the window. The inbox reply field does not convert an ordinary reply into a template.

Use **Connect a number** to open Channels and configure the property’s WhatsApp Business connection. Booking confirmations and configured self-check-in/payment/room-charge templates are separate automated message workflows; their availability depends on the active provider connection, approved template names and relevant property settings.

## 7. Channels

Open **Operations → Channels**. The list shows the selected property’s **Channel**, **Provider**, **Number** and **Active** status. Use **Search** to find a phone number or provider; use the Channel and Active filters to narrow the list. **Export** downloads the visible channel records as CSV. **Columns** configures the displayed table columns.

### 7.1 Create or edit a connection

Select **New** to open the connection form, or select a row to inspect/edit an existing record. Required fields are **Channel** and **Provider**:

| Field | Purpose |
|---|---|
| Channel | WhatsApp, Voice or SMS |
| Provider | Meta Business, HeyKoala, Twilio, Retell, Vapi or Custom |
| Phone number (display) | Human-readable number associated with this connection |
| Meta phone number ID | For Meta WhatsApp Cloud API; obtain from Meta Business Manager → WhatsApp → API setup |
| Access token | Provider credential; permanent Cloud API token is stored encrypted |
| Webhook verify token | Configure the same value in the provider’s webhook setup |
| Meta App Secret | Meta App Settings → Basic; used to verify inbound webhook signatures and stored encrypted |
| Template language code | Language code for approved Meta templates |
| Template: booking confirmation | Approved template name; arguments are guest, property, check-in and check-out |
| Template: self check-in link | Approved template name; arguments are guest and link |
| Template: payment request | Approved template name; arguments are guest, amount and note |
| Template: room charge alert | Approved template name; arguments are guest, amount, description/location and balance; requires Front Desk room-charge alerts to be enabled |
| Active | Enables or disables this connection |

Use the form’s **Save** or **Cancel** button to complete or abandon an edit. This generic connection form does not show a provider test/send action. Confirm credentials, webhook configuration, approved templates and provider-side subscriptions with the provider before activating production traffic. Treat tokens and secrets as credentials; do not put them in tickets or reports.

> **Channels vs. Channel Manager:** Operations → Channels configures phone/messaging connections. OTA/channel-manager connections and room mappings are separate Revenue features, not this Channels screen.

## 8. Reports

### 8.1 Reports hub

Select **Reports** in the Operations sidebar. The hub groups report destinations by **Your reports**, **Daily**, **Revenue**, **Finance** and **Operations**. It may show:

- Department packs and Custom reports.
- Owner view, Manager flash, Night audit history and Shift report.
- Revenue dashboard/reports, F&B dashboard and Banquet registers.
- Ledgers, Folio history, Voids and allowances, and Accounting export.
- **SLA report** for guest requests and **Housekeeping tasks**.

The hub filters destinations according to role and enabled applications; the target page also checks authorization. A user may therefore see a shorter list than another user.

### 8.2 SLA report

Use **Operations → Reports → SLA report** (or `/ops-sla`) to review guest requests against their response deadlines. Select the intended property and report period, then compare overdue/breached requests with the ticket queue. The report is read-only; correct a ticket’s assignment/status from Guest Requests rather than trying to edit it in the report.

### 8.3 Custom reports and packs

The report page provides **My reports**, **New report**, **Department packs**, and (for eligible roles) **Manager flash**:

- **New report:** choose a permitted dataset, reporting dates, columns, filters, optional grouping and title. Select **Preview** to inspect rows, **CSV** to download, **Print** for a printable view, **Email** to send the result, and **Save** to store the definition.
- **Filters:** each filter has a dataset field, comparison operator and value; incomplete filters are not run. Grouped summaries can be drilled into by selecting a summary row.
- **Sharing and schedules:** eligible roles can share a report with the property and configure an Off, Daily or Weekly email schedule, delivery time, weekday for weekly schedules and comma-separated recipients.
- **My reports:** open a saved report to edit/run it; delete only reports for which the current user has permission. Report ownership and sharing are enforced server-side.
- **Department packs:** available packs include Front Office, Housekeeping, F&B, Engineering, Laundry and Hotel Manager. A pack includes only sections allowed by the user’s roles and the property’s enabled modules. Packs can be opened as a printable report, emailed, or scheduled weekly.
- **Manager flash:** where authorized, review daily or month-to-date occupancy, ADR, RevPAR, revenue and collections.

Custom report datasets are whitelisted by the server, not arbitrary SQL. Available dataset examples include arrivals, departures, in-house guests, no-shows/cancellations, occupancy/revenue by day, folio charges, payments, voids/allowances, contribution by source, housekeeping tasks, room status, lost and found, POS orders/items, kitchen times, service tickets, laundry orders, shift handover, early departures, overdue company balances and DSO. Dataset availability is role- and module-dependent. The custom report date range is limited by the server (currently up to 92 days); large results may be capped.

## 9. Operations Settings

Open **Operations → Settings**, or navigate to **Settings → Operations** in the Admin app. The Operations settings page has a **Guest request deadlines** section. Hotel Admin can configure:

| Field | Default | Accepted range | Meaning |
|---|---:|---:|---|
| Urgent | 15 min | 1–1,440 min | Time allowed before an Urgent request is overdue |
| High | 30 min | 1–1,440 min | Time allowed before a High request is overdue |
| Medium | 60 min | 1–1,440 min | Time allowed before a Medium request is overdue |
| Low | 240 min | 1–2,880 min | Time allowed before a Low request is overdue |

Edit the values and use the contextual **Save changes** action. The values govern request deadlines; they do not themselves assign a staff member, change a ticket’s priority or resolve the request. Confirm the new interval on a newly created request after saving. Existing requests keep their recorded due date.

The Settings page may also provide related links to **Channels** and **SLA report**. These open the corresponding screens; they are not additional Operations settings fields.

## 10. End-to-End Operations Workflows

### 10.1 Handle a guest service request

1. Confirm the selected property.
2. Open Guest Requests and check Open, Unassigned and Overdue views.
3. Filter to the relevant category/priority and open the ticket.
4. Claim or assign it; start work and add notes as the work progresses.
5. Record the resolution and mark it solved.
6. Review overdue/breached trends in SLA report and adjust deadlines only with Hotel Admin approval.

### 10.2 Connect WhatsApp for guest messaging

1. Obtain the correct provider connection credentials and approved template names from the authorized Meta/provider administrator.
2. In Channels, create a WhatsApp connection using the appropriate provider, phone number ID, encrypted access token and webhook verify token. For Meta, also enter the App Secret and template names/language.
3. Configure the provider webhook to use the same verify token and subscribe it to the required message events.
4. Validate the provider’s webhook and number configuration, then activate the connection.
5. Return to WhatsApp and confirm inbound conversations appear. Use free-form replies only while the guest’s 24-hour session window is open.

### 10.3 Review the service operation

1. Open Reports → SLA report and choose the property/date scope.
2. Compare late tickets with the Open/Overdue queue.
3. Use a Service Tickets custom report or Engineering pack (if available) to summarize by category/priority and inspect breaches/resolution time.
4. Share or schedule only the minimum report data needed by authorized recipients.

## 11. Troubleshooting

| Symptom | Checks |
|---|---|
| Operations or a sidebar item is missing | Confirm user role, property access and Operations module state. Channels and Settings have stricter role gates than the app. |
| Cannot create or assign a ticket | Confirm the ticket is not in a completed status, required subject is entered, and the assignee is active, eligible and scoped to the property. |
| No staff appear in the assignee list | Ensure active System Users have Front Desk, Housekeeping, Housekeeping Supervisor or Hotel Admin role and access to the selected property. |
| A ticket appears overdue immediately | Compare its creation time and priority deadline with current server time; verify Operations settings for requests created after a change. |
| WhatsApp thread is empty | Confirm the selected property, active connection, provider webhook URL/token/signature settings and inbound event subscription. |
| WhatsApp reply fails outside the 24-hour window | A guest must message again to reopen the session, or an approved template must be sent through the template-enabled workflow. The inbox reply box only sends free-form text. |
| Channel does not send messages | Verify Active status, correct credentials and provider-side setup. Recheck Meta phone number ID, App Secret, verify token and approved template names. |
| Report destination or dataset is missing | Report links/datasets are filtered by role and module. Ask an administrator to verify grants and module enablement. |
| Report export or email fails | Verify date range, recipients, mail/provider configuration and authorization; read the displayed error and retry only after correcting it. |

Do not paste access tokens or App Secrets into support requests. Share the error text and connection identifier instead.

## 12. Source Verification and Runtime Variations

This guide was checked against the Operations navigation in `frontend/src/lib/apps.ts`; ticket controls in `frontend/src/screens/Tickets.tsx`; WhatsApp UI and endpoints in `frontend/src/screens/WhatsAppChat.tsx` and `kamra/whatsapp.py`; channel fields in `frontend/src/screens/configs.ts`; report links and builder in `frontend/src/screens/ReportsHub.tsx`, `frontend/src/screens/Reports.tsx` and `kamra/custom_reports.py`; and ticket authorization/deadline logic in `kamra/tickets.py` and `kamra/settings.py`.

The actual property list, user grants, open tickets, channel providers, WhatsApp templates, report datasets and report results are runtime-dependent. Sample browser records are not a guarantee of production data or configuration.

---

*End of Quantumberg Operations Guide.*
