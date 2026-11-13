<p align="center">
  <img src="../images/quantumberg-logo.png" alt="Quantumberg Technologies" style="width: 200px; max-width: 100%; height: auto;" />
</p>

<h1 align="center">Quantumberg PMS Administrator Guide</h1>

**Version:** 2.7.1
**Product:** Quantumberg PMS (Property Management System)
**Platform:** Frappe v16
**Audience:** Hotel Administrators, System Managers, IT Administrators

---

## Table of Contents

1. Introduction
2. Application Overview
3. Administrator Login and Logout
4. Admin Portal Layout
5. Admin Sidebar Navigation
6. System Health
7. Property Management
8. Settings Overview
9. Property Settings - Field-by-Field Guide
10. Stay Policies
11. Privacy & Data
12. Front Desk Settings
13. Housekeeping Settings
14. Operations Settings
15. F&B Settings
16. Banquets & Groups Settings
17. Revenue Settings
18. Finance Settings
19. Booking Engine Settings
20. Staff & Access Management
21. Module Management
22. AI Access and AI Assistant
23. Payment Integrations
24. Webhooks
25. Appearance Settings
26. Developer Settings and API Keys
27. Rooms and Room Types
28. Activity Log
29. Go-live Import
30. New Property Setup
31. Finish Setup Checklist
32. Frappe Desk Access
33. Common Administrative Workflows
34. Permissions and Security
35. Troubleshooting and FAQs
36. Glossary
37. Front Desk Dashboard and Daily Views
38. Operational Workflows
39. Administrator Best Practices
40. Source Verification and Runtime Variations

---

## 1. Introduction

Quantumberg PMS is a property-management system for hotels and short-term rentals. It combines Front Desk, Housekeeping, Operations, Events, Revenue, Finance and Admin functions in one web application, served from a Frappe v16 backend.

This guide is written for **Administrators** - the people who configure the property, manage staff access, set up rooms and pricing, and keep the system healthy. It is based on the actual v2.7.1 implementation.

> **Important:** This is a documentation-only guide. It does not modify any application code or data.

## 2. Application Overview

- **Frontend:** React single-page application served at /Quantumberg (and /desk/Quantumberg inside Frappe Desk).
- **Backend:** Frappe v16 (Python) with MariaDB.
- **Multi-property:** One site can host several properties; each user is scoped to the properties they are granted.
- **Role-based access:** Menus and pages are shown according to the user roles.
- **Apps:** Front Desk, Housekeeping, Operations, Events (Banquets), Revenue, Finance, Admin.

## 3. Administrator Login and Logout

### 3.1 Accessing the Application

Open a browser and go to the site URL (for example http://localhost:8000). The login screen appears.

### 3.2 Login Fields

| Field            | Purpose                      | How to use                                                 | Example           | Notes                                           |
| ---------------- | ---------------------------- | ---------------------------------------------------------- | ----------------- | ----------------------------------------------- |
| Email / Username | Identifies your user account | Enter the email or username assigned by your administrator | admin@example.com | Case-insensitive in most setups                 |
| Password         | Authenticates you            | Enter your password                                        | (not shown)       | Never share. Reset via Frappe Desk if forgotten |

### 3.3 Sign-in Process

1. Enter your email/username.
2. Enter your password.
3. Click **Sign in**.
4. On success you are redirected to the application home (Front Desk by default).
5. If credentials are wrong, an error message is shown and you remain on the login page.

### 3.4 Session Behaviour

- Sessions use cookies. If you close the browser, you may need to log in again depending on session expiry.
- If your session expires mid-work, a session-ended notice appears on the login screen.
- The app checks your roles and property access on load; menus are filtered accordingly.

### 3.5 Logout

1. Open the user menu (top-right).
2. Click **Logout**.
3. You are returned to the Quantumberg login route under the current app base (`/Quantumberg/login` or `/desk/Quantumberg/login`).

### 3.6 Access Restrictions

- Only users with roles such as Hotel Admin, System Manager or Administrator can open the Admin app.
- Each settings page also checks editor roles; a user without the role sees the page read-only or is denied.
- Property scoping: a user with access to one property cannot see another property's data.

## 4. Admin Portal Layout

- **Top bar:** app switcher, global search (Ctrl/Cmd+K), property selector, notifications, user menu.
- **Sidebar (left):** navigation for the currently selected app. In the Admin app it lists Settings, System Health, Rooms, Room Types, Activity Log, Marketplace, Go-live Import, New Property, Staff & Access, Finish setup, Frappe Desk.
- **Main area:** the selected page.
- **Quantumberg branding:** the sidebar shows the Quantumberg logo and a purple-pink gradient background. The browser tab title is Quantumberg.

## 5. Admin Sidebar Navigation

| #   | Item           | Route             | Purpose                                            | Roles                                      |
| --- | -------------- | ----------------- | -------------------------------------------------- | ------------------------------------------ |
| 1   | Settings       | /settings/general | Property identity, policies, and all configuration | Hotel Admin, System Manager, Administrator |
| 2   | System Health  | /health           | Version check, diagnostics, upgrade guidance       | Hotel Admin, System Manager, Administrator |
| 3   | Rooms          | /rooms            | Manage individual rooms                            | Hotel Admin, System Manager, Administrator |
| 4   | Room Types     | /room-types       | Manage room categories and pricing                 | Hotel Admin, System Manager, Administrator |
| 5   | Activity Log   | /activity         | Audit trail of changes                             | Hotel Admin, System Manager, Administrator |
| 6   | Marketplace    | /marketplace      | Install/enable add-ons                             | Hotel Admin, System Manager, Administrator |
| 7   | Go-live Import | /go-live          | Import data when going live                        | Hotel Admin, System Manager, Administrator |
| 8   | New Property   | /setup            | Create a new property                              | System Manager, Administrator              |
| 9   | Staff & Access | /settings/staff   | Manage users, roles, property access               | Hotel Admin, System Manager, Administrator |
| 10  | Finish setup   | /finish-setup     | Onboarding checklist                               | Hotel Admin, System Manager, Administrator |
| 11  | Frappe Desk    | (external)        | Open Frappe's desk interface                       | Administrator, System Manager              |

### Front Desk application

The front-desk application entries are filtered by role and module:

| Item                 | Purpose                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| Today                | Open the daily dashboard for the selected property and business date.                                   |
| Quantumberg Agent    | Open the staff assistant; available actions depend on AI setup and the user's normal roles.             |
| In House             | Review current stays and due-outs.                                                                      |
| Reservations         | Find and manage bookings.                                                                               |
| Tape Chart           | Inspect room/date availability.                                                                         |
| Rooms                | Open the room board/status view.                                                                        |
| Guest History        | Search guest profiles and past stays.                                                                   |
| Billing              | Open folios, charges and payment workflows.                                                             |
| Night Audit          | Review and run business-date close tasks.                                                               |
| Calendar             | Calendar-based reservation/availability view.                                                           |
| Central Reservations | Reservation work across properties the user can access.                                                 |
| Room Blocks          | Manage inventory held from general sale.                                                                |
| Group Booking        | Manage group records and pickup.                                                                        |
| Reports              | Open reports with property/date filters.                                                                |
| Settings             | Front Desk settings; only Hotel Admin, System Manager and Administrator roles are listed for this link. |

### Other application sidebars

The app switcher exposes applications according to role and property module state. Their source-defined entries are:

| Application       | Entries                                                                                                                                                                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Housekeeping      | Room Board; Rooms; Tasks; Laundry; Lost & Found; Reports; Phone App; Settings                                                                                                                                                                                                         |
| Operations        | Guest Requests (Tickets); WhatsApp; Channels; Reports; Settings                                                                                                                                                                                                                       |
| F&B               | Restaurant POS; F&B Dashboard; Kitchen Display; Menu; Ingredients; Kitchen Inventory; Outlets; Printers; Reports; Settings                                                                                                                                                            |
| Banquets & Groups | Banquets; Month Availability; Function Diary; Registers; Menus & Services; All Functions; Groups & Blocks; Halls & Venues; Settings                                                                                                                                                   |
| Revenue           | Revenue Dashboard; Owner view; Reports; Channel Manager; OTA Room Mappings; Rate Calendar; Rate Plans; Seasons; Guardrails; Vouchers; Long-stay Discounts; Meal Plans; Experiences; Room Types; Travel Agents; Accounts Receivable; Settings                                          |
| Finance           | My Till; All Tills; Sessions; Petty Cash; Shift Handover; Currency Desk; Night Audit; Owner view; Billing; Folio History; Allowances to approve; Receivables; Ledgers; Payables; Cash outlook; Profit and loss; Transaction Codes; Reason Codes; Reports; Accounting Export; Settings |
| Booking Engine    | Hotel Profile; Amenities; Photos; Policies; Payments; FAQ; SEO; Settings                                                                                                                                                                                                              |

Some links have narrower roles than their parent application. Features also depend on module state, country pack and configured integrations. Absence of a link does not grant or deny an API permission; server-side authorization remains authoritative.

## 6. System Health

**Purpose:** Shows installed Quantumberg and Frappe versions, latest available release information, status checks returned by the health endpoint, and upgrade guidance. It does not upgrade the site automatically.

**What you can do:**
- See the current version and whether an update is available.
- Review checks and refresh the health result.
- Read upgrade guidance.

**Roles:** Hotel Admin, System Manager, Administrator.

**Steps:**
1. Open Admin -> System Health.
2. Review the version card and any update available notice.
3. Run diagnostics if prompted.
4. Follow the printed upgrade steps (manual).

**Notes:** This page reports status and manual upgrade guidance; it does not perform an upgrade.

## 7. Property Management

Property identity and configuration live under Settings -> Property (the general module). One site can host multiple properties; switch the active property from the top bar before editing.


## 8. Settings Overview

Settings are organised into groups:

- **Property (organisation):** Property, Stay policies, Privacy & data, Front Desk, Housekeeping, Operations, F&B, Banquets & Groups, Revenue, Finance, Booking Engine.
- **Modules:** enable/disable parts of the product.
- **Access:** Staff & access, Modules, AI access (MCP).
- **Integrations:** Payments, AI assistant, Webhooks, Quantumberg Verify, ZATCA e-invoicing.
- **You (personal):** Appearance.

Each module page has sections; each section has fields. Changes are saved per module via **Save**. The Settings hub requests the supported schema from the backend, validates changes and records them. The fields below are the schema-defined property settings; related records/cards are noted separately.

---

## 9. Property Settings - Field-by-Field Guide

### Identity section

| Field         | Purpose                                              | How to use                       | Example                         | Notes                                                                          |
| ------------- | ---------------------------------------------------- | -------------------------------- | ------------------------------- | ------------------------------------------------------------------------------ |
| Property name | Display name of the property                         | Enter the hotel name             | Quantumberg Demo Palace         | Printed on invoices and the GRC                                                |
| Legal name    | Registered legal entity name                         | Enter as registered              | Quantumberg Hospitality Pvt Ltd | Printed on invoices                                                            |
| Short code    | 2-6 letters/digits used in allowance voucher numbers | Enter initials                   | QDP                             | Changing it starts a new voucher series; invoice numbers keep their own series |
| Property kind | Hotel vs. short-term rental                          | Select                           | Hotel                           | Affects some workflows                                                         |
| Logo          | Property logo (square, 512px+)                       | Upload PNG/SVG with transparency | logo.png                        | Shown on the booking engine and reports                                        |

### Location & locale section

| Field          | Purpose                            | How to use       | Example      | Notes                                                                |
| -------------- | ---------------------------------- | ---------------- | ------------ | -------------------------------------------------------------------- |
| Country        | Selects the tax and invoicing pack | Select from list | India        | Tax labels, ID types, payment methods and guest phone code follow it |
| Currency       | ISO currency code                  | Enter code       | INR          | Used for all amounts                                                 |
| Time zone      | Hotel local clock                  | Select from list | Asia/Kolkata | Used for night audit and timestamps                                  |
| Address        | Street address                     | Enter            | 12 MG Road   | Printed on invoices                                                  |
| City           | City                               | Enter            | Bengaluru    |                                                                      |
| State / region | State or region                    | Enter            | Karnataka    |                                                                      |
| Postal code    | PIN/ZIP                            | Enter            | 560001       |                                                                      |

### Contact & registration section

| Field                   | Purpose           | How to use | Example                 | Notes               |
| ----------------------- | ----------------- | ---------- | ----------------------- | ------------------- |
| Phone                   | Property phone    | Enter      | +91 80 1234 5678        |                     |
| Email                   | Property email    | Enter      | info@quantumberg.com    |                     |
| Website                 | Property website  | Enter URL  | https://quantumberg.com |                     |
| Tax registration number | GSTIN / VAT / TRN | Enter      | 29ABCDE1234F1Z5         | Printed on invoices |

---

## 10. Stay Policies

### Check-in & check-out

| Field          | Purpose                    | How to use  | Example | Notes        |
| -------------- | -------------------------- | ----------- | ------- | ------------ |
| Check-in time  | Default check-in time      | Enter HH:MM | 14:00   | Used for ETA |
| Check-out time | Default check-out time     | Enter HH:MM | 11:00   | Used for ETD |
| Minimum stay   | Minimum nights per booking | Number      | 1       | 1-60 nights  |

### Cancellation & no-show

| Field                   | Purpose                             | How to use | Example     | Notes                                                                                         |
| ----------------------- | ----------------------------------- | ---------- | ----------- | --------------------------------------------------------------------------------------------- |
| Free cancellation until | Days before arrival for free cancel | Number     | 1           | 0-365 days                                                                                    |
| Late cancellation fee   | Fee if cancelled late               | Select     | First Night | Options: None, First Night, Full Stay                                                         |
| No-show charge          | Charge if guest does not arrive     | Select     | First Night | Posted automatically by the night audit                                                       |
| Early departure charge  | Charge for early checkout           | Select     | All Nights  | Options: None, One Night, All Nights. Finance/Hotel Admin can override per stay with a reason |

### Deposits

| Field                       | Purpose                            | How to use   | Example | Notes |
| --------------------------- | ---------------------------------- | ------------ | ------- | ----- |
| Deposit expected at booking | % deposit required                 | Number 0-100 | 0       | %     |
| Security deposit            | Refundable security deposit amount | Number       | 0       |       |

### Rate changes in house

| Field                                               | Purpose                              | How to use | Example             | Notes                                                                                                                       |
| --------------------------------------------------- | ------------------------------------ | ---------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| When a stay's rate changes after nights are charged | How to handle already-charged nights | Select     | Keep charged nights | Options: Keep charged nights, Credit the difference, Correct back-dated rates. Charged nights are never re-priced in place. |

---

## 11. Privacy & Data

The Privacy module is edited by Hotel Admin. Its exact source-defined settings are:

| Section           | Field                    | Effect                                                                                                     |
| ----------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Retention         | Guest ID retention       | `Store` or `Verify & Discard`; the latter masks ID numbers and removes ID photos at checkout.              |
| Retention         | Erase guest data after   | Months without a stay before guest data is erased; bills remain for accounting. `0` keeps guest data.      |
| Retention         | Clear message text after | Days before WhatsApp and AI chat text is cleared; delivery/audit metadata remains. `0` keeps message text. |
| Grievance contact | Privacy contact          | Email or phone shown on booking and check-in pages for privacy requests.                                   |

Review applicable privacy and accounting obligations before changing retention values.

---

## 12. Front Desk Settings

Hotel Admin can edit this module. The backend schema groups its property settings as follows:

| Section                | Fields                                                                                                                                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arrivals               | Send pre-check-in links automatically; Send links this far ahead; Require pre-check-in before access details; Access instructions                                                                              |
| Door locks             | Door lock system                                                                                                                                                                                               |
| Guest info at check-in | Wi-Fi name; Wi-Fi password; Breakfast times; Emergency number; Anything else for guests                                                                                                                        |
| Guest alerts           | WhatsApp the guest when a charge is posted to the room                                                                                                                                                         |
| Holds & selling        | Hold unconfirmed bookings for; Sell message                                                                                                                                                                    |
| Night audit & no-shows | Mark no-shows; Hold late arrivals until the next audit; No no-show fee on OTA bookings; Release non-guaranteed arrivals at                                                                                     |
| Automatic night audit  | Run the night audit automatically; Run at; Wait after that time                                                                                                                                                |
| Night audit checklist  | Open tills block the audit; Open restaurant bills block the audit; Departures still in house block the audit; Flag in-house folios owing more than; Rate variance tolerance; Scheduled audit when checks block |
| Hourly view            | Day starts; Day ends                                                                                                                                                                                           |

Other related cards (such as check-in steps, night-audit schedule, printer status, laundry rates and country-specific integrations) are separate UI screens or records, not additional fields in this module schema. Only configure integrations actually available on the site.

---

## 13. Housekeeping Settings

Hotel Admin and Housekeeping Supervisor can edit these settings:

| Section        | Fields                                               | Effect                                                                        |
| -------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------- |
| Task deadlines | Urgent; High; Medium; Low                            | Minutes before a housekeeping task becomes overdue/escalates.                 |
| Room turnover  | Inspect after every checkout clean; Inspection takes | Creates an inspection step after checkout cleaning and sets its due duration. |
| Laundry        | Express price                                        | Multiplier used when a laundry rate-card item has no express price.           |

Additional housekeeping functionality is configured through the Room Board, task, laundry and room records. Do not assume there are extra room-status settings in this section.

---

## 14. Operations Settings

Hotel Admin can configure the **Guest request deadlines** section. Its fields are **Urgent**, **High**, **Medium** and **Low** (minutes). These values set how long a guest request may remain open before it is considered overdue. The Operations app separately provides tickets, WhatsApp and channel screens subject to roles and enabled modules.

---

## 15. F&B Settings

Hotel Admin, Finance and F&B Manager roles can edit this module.

| Section              | Fields                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| Kitchen orders (KOT) | Auto-accept and print KOT; Print void slips in the kitchen; Flag a bill not sent to the kitchen after |
| Table reservations   | Show a reservation from; Keep showing it until                                                        |
| External POS         | Largest room charge from an external POS                                                              |
| Menu master lists    | Allergens & dietary tags; Prep stations; Courses; Menu categories                                     |

The external POS charge limit of zero means no configured limit. Master lists are newline-separated values used as tags or suggestions. Outlets, menu items, ingredients, inventory and printer routes are managed on their respective screens.

---

## 16. Banquets & Groups Settings

Hotel Admin and Revenue Manager can edit:

| Section                    | Fields                                                |
| -------------------------- | ----------------------------------------------------- |
| Quotation margins          | Target margin; Floor margin                           |
| Default payment milestones | Advance at confirmation; Interim payment; Interim due |
| Sales follow-up            | Follow up an enquiry after                            |

Payment milestones are defaults for new functions and can be changed on the function. Quotes below the floor margin are flagged for review.

---

## 17. Revenue Settings

Hotel Admin and Revenue Manager can edit the **Overbooking allowance** under **Overbooking**. Treat this as a deliberate inventory-risk setting and document the property's recovery plan before increasing it. Rate plans, seasons, guardrails, channel mappings and other revenue records are managed in their respective Revenue screens.

---

## 18. Finance Settings

Hotel Admin, Finance and System Manager roles may edit finance settings as allowed by the server schema.

| Section           | Fields                                                                                                                                                                                                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Room tax          | Tax mode; Slab threshold per night; Rate below threshold; Rate above threshold; Displayed rates include tax                                                                                                                                                 |
| Fees & levies     | Room levy name; Room levy; Tax applies to the levy; Cleaning fee per stay; Cleaning fee is taxable; Pets allowed; Pet charge; Pet charge applies                                                                                                            |
| Corporate billing | When a credit company has no billing rules                                                                                                                                                                                                                  |
| Company credit    | Default payment terms; Credit control; Overdue grace period; Email payment reminders                                                                                                                                                                        |
| Cashier controls  | Take money through cashier tills; Require cashier PIN on money actions; Lock a PIN after; Lock for / stay unlocked for; Cash refund limit for new cashiers; Till variance that needs a manager; Allowances need a manager's approval; Only allowances above |
| Exchange rates    | Foreign currencies taken; Margin on the market rate; Fetch rates automatically every day                                                                                                                                                                    |

Check country-specific tax rules with the property's finance adviser. Settings can change guest totals, invoice presentation, cashier authorization and credit follow-up.

---

## 19. Booking Engine Settings

The property settings schema includes:

| Section       | Fields                                    |
| ------------- | ----------------------------------------- |
| Booking page  | Public booking page is live; Booking mode |
| Guest payment | Guests pay; Advance; Registration fee     |

Separate Booking Engine screens cover Hotel Profile, Amenities, Photos, Policies, Payments, FAQ and SEO. Visibility is limited to Revenue Manager, Hotel Admin, System Manager and Administrator roles; actual payment options depend on the property's country pack and gateway setup. Verify the complete public booking journey before publishing.

---

## 20. Staff & Access Management

**Route:** /settings/staff

Manage who can sign in, their roles, and which properties they reach.

**Fields per staff row:**
- Email, full name, job title, enabled (active), roles, properties (all or specific), last login/active, cashier PIN status, self flag, editable flag.

**Actions:** Invite/add user, edit roles/properties, deactivate, reset cashier PIN, send welcome email.

**Roles:** Hotel Admin, System Manager, Administrator.

---

## 21. Module Management

**Route:** /settings/modules

Toggle modules (F&B, Banquets, Housekeeping, etc.) on/off for this property. Disabled modules hide their apps from the sidebar.

---

## 22. AI Access and AI Assistant

- **AI access (MCP)** is a separate access page, not the AI Assistant provider card. It controls per-property MCP enablement, read-only/write-tool policy, staff levels (None, Read, Manage), connected client sessions, blocked tools and additional OAuth redirect URIs. The site can disable MCP globally. An AI client acts as the connected user and cannot exceed that user's regular roles. Redirect URIs are site-wide, must be exact HTTPS addresses and cannot use wildcards; only IT can edit them.
- **AI Assistant** is the property-scoped provider configuration for Quantumberg Agent: enabled, provider preset, base URL, model, API key, extra instructions, contact-detail redaction and connection test. The API key is write-only. Provider/network processing is subject to that provider's terms and region.

---

## 23. Payment Integrations

**Route:** /settings/payments

Where the country pack offers a gateway, configure enabled state, test mode, gateway, key/app ID, secret and webhook secret. Secret fields are write-only. Configure the provider's expected callback and test safely before live collection. Some countries may not have a supported online gateway.

---

## 24. Webhooks

**Route:** /settings/webhooks

Configure a label, HTTPS endpoint, active state and selected event types. The signing secret appears once after creation; save it securely. Review the delivery log and response details before retrying. Make receiver handlers signature-aware and idempotent.

---

## 25. Appearance Settings

**Route:** /settings/appearance

Theme and language for this browser are personal preferences, not property-wide branding. Available language options are supplied by the UI; Arabic supports right-to-left layout.

---

## 26. Developer Settings and API Keys

**Route:** /developers (System Manager, Administrator only)

The Developers page generates or rotates the current user's API credentials and explains the REST surface and connection setup. The secret is shown once; rotation invalidates the old key. Requests run with the key owner's permissions and are auditable. Webhooks and MCP controls are separate settings pages.

---

## 27. Rooms and Room Types

- **Rooms** (/rooms): manage individual rooms - number, type, floor, status, out-of-order.
- **Room Types** (/room-types): categories, pricing, capacity, amenities.

---

## 28. Activity Log

**Route:** /activity

Audit trail of changes across the property. Filter by date, user, doctype.

---

## 29. Go-live Import

**Route:** /go-live

Import data (rooms, rates, guests) when going live. Used during initial setup.

---

## 30. New Property Setup

**Route:** /setup (System Manager, Administrator)

Create a new property: identity, location, contact, then configure rooms and rates.

---

## 31. Finish Setup Checklist

**Route:** /finish-setup

Onboarding checklist: getting started steps to complete before go-live.

---

## 32. Frappe Desk Access

**Route:** external link to Frappe Desk (/app/build).

Opens Frappe's desk interface in a new tab for low-level administration (DocTypes, reports, scripts). Roles: Administrator, System Manager.

---

## 33. Common Administrative Workflows

### Update property information
1. Admin -> Settings -> Property.
2. Edit fields in Identity / Location & locale / Contact & registration.
3. Click Save.
4. Verify on invoices/GRC.

### Change property logo
1. Settings -> Property -> Identity -> Logo.
2. Upload square PNG/SVG (512px+).
3. Save. Logo appears on the booking engine and reports.

### Manage staff access
1. Admin -> Staff & Access.
2. Add/edit user, assign roles and properties.
3. Save. User receives welcome email if enabled.

### Configure modules
1. Admin -> Modules.
2. Toggle modules on/off.
3. Save. Disabled modules hide from sidebar.

### Check system health
1. Admin -> System Health.
2. Review version, diagnostics, upgrade guidance.

### Configure booking engine
1. Admin -> Settings -> Booking Engine.
2. Set language, branding, FAQ, SEO.
3. Save.

### Manage rooms
1. Admin -> Rooms / Room Types.
2. Add/edit rooms and types.
3. Save.

### Review activity log
1. Admin -> Activity Log.
2. Filter and review.

---

## 34. Permissions and Security

- Role-based: Front Desk, Night Auditor, Hotel Admin, Revenue Manager, System Manager, Administrator, F&B Manager, etc.
- Property scoping: users see only granted properties.
- Ledger entries (Folio/City Ledger/Credit Note) are read-only outside Quantumberg's money code (System Manager keeps full access).
- Dashboard hides money and occupancy from Front Desk.
- MCP/AI access is role- and property-gated.

---

## 35. Troubleshooting and FAQs

- **Can't see Admin app?** Check roles (Hotel Admin / System Manager / Administrator).
- **Settings read-only?** Check editor role for that module.
- **Version mismatch?** Check System Health.
- **Room not available?** Check availability and existing bookings.
- **Favicon wrong?** Hard refresh (Ctrl+Shift+R).

---

## 36. Glossary

- **Property:** A hotel or short-term rental.
- **Folio:** A guest's bill.
- **Night audit:** End-of-day close process.
- **GRC:** Guest Registration Card.
- **Quantumberg Verify:** Tax/ID verification via Quantumberg Connect.
- **MCP:** Model Context Protocol - AI client access.
- **ZATCA:** Saudi e-invoicing (FATOORA).

---

## 37. Front Desk Dashboard and Daily Views

The **Today** page is the daily Front Desk view. It is property-scoped and its date/business-day context matters, especially around night audit. Dashboard widgets can be rearranged through **Customize**; this changes the user's dashboard layout, not hotel records.

The dashboard data model includes arrivals, departures, in-house count, no-shows, total rooms, occupancy, today's revenue and collections, month-to-date occupancy/revenue, ADR, RevPAR, rooms sold, room-status counts, open/overdue housekeeping tasks and finance outstanding/open-folio counts. Not every metric is shown to every role: revenue figures are hidden for users outside Finance, Revenue and manager roles. The Revenue Dashboard can switch between a property and portfolio view only when the user has access to multiple properties.

Use the dashboard as a summary:

1. Confirm the selected property and displayed business date.
2. Review arrivals and departures; open the reservation/stay to act.
3. Check in-house and occupancy figures against the room board when resolving a room discrepancy.
4. Review open/overdue tasks and assign or update the underlying task.
5. Open the source folio or financial screen for a revenue, collection or outstanding-balance discrepancy.

The Rooms board supports search and filters for floor, room type and status, including vacant-ready, dirty, occupied, arriving, departing, out-of-order/blocked and task-related views. It refreshes periodically. Use its room drawer and actions rather than changing status in an unrelated record.

---

## 38. Operational Workflows

The procedures below describe the safe sequence supported by the screens. Individual required fields vary by property, country pack, enabled modules and role.

### 38.1 Create a property

1. Open **Admin → New Property**. Choose the supported setup mode and property kind.
2. Enter verified property identity, country, currency, time zone and contact details.
3. Define at least one valid room type with code, name and rate; complete the room/inventory topology appropriate to the property.
4. If using guided setup, review selected modules and optional F&B outlets, stations and tills.
5. Review the submitted configuration and create the property once.
6. Select the property and use **Finish Setup** to review its checklist.

The setup screen can create the property and initial related setup records. Review submitted values before creating; do not make a duplicate property to fix a field.

### 38.2 Configure rooms and room types

1. Create room types first, ensuring codes, names, rates and occupancy details are correct.
2. Add individual rooms where the selected inventory topology uses physical rooms.
3. Assign rooms to the intended type and property.
4. Review the room board and correct records through their edit screens.
5. Use supported block/unavailable/housekeeping workflows to prevent sale; do not delete rooms linked to stays.

### 38.3 Create and maintain guests

1. Search Guest History before creating a profile.
2. Reuse an existing matching profile; resolve possible duplicates carefully.
3. Enter only verified information needed for the stay.
4. Apply the property's ID handling and privacy-retention policy.

### 38.4 Create a reservation

1. Start from Reservations, Tape Chart, Calendar or the booking dialog.
2. Confirm property, arrival/departure dates, room type, occupancy and availability.
3. Select or create the guest; enter source and other information requested by the form.
4. Check rate, taxes/fees, deposit, guarantee, payment and cancellation terms.
5. Save, then verify the reservation status, assigned inventory and any resulting folio/deposit.

Do not treat an unconfirmed/held reservation as guaranteed. The server validates availability and status transitions.

### 38.5 Check in and manage in-house stays

1. Open the arrival/reservation and verify guest identity, dates and booking status.
2. Confirm an eligible room is ready; assign or change the room through the check-in workflow.
3. Complete the required registration and payment/deposit steps.
4. Provide access instructions only after any configured pre-check-in/access requirements are met.
5. Confirm the stay is listed as In House.
6. During the stay, use the reservation/stay workflow for extensions or room changes and verify that inventory and future rates update correctly.
7. Record service requests as tickets/tasks and check that they reach the correct operational queue.

### 38.6 Check out

1. Open the current stay and review dates, room, guest and folio.
2. Confirm charges, taxes, payments, deposits and any credit balance.
3. Resolve adjustments through the authorized void/reversal/allowance workflow with a reason and approval as required.
4. Settle the balance or follow the approved company-credit process.
5. Complete checkout and verify the folio and resulting housekeeping status.

### 38.7 Billing and payment reconciliation

1. Confirm the selected property, folio, guest and currency.
2. Review every charge and its transaction code/source.
3. Take payment using the configured till or supported gateway flow.
4. Verify the payment entry and remaining folio balance.
5. Close and reconcile the cashier session at shift end; investigate variances before finalizing.
6. Use supported reversals, credits or allowances to correct mistakes; never delete accounting records to hide a discrepancy.

### 38.8 Room blocks

1. Create a room block for the correct property and dates.
2. Set room-type allocation, pickup/cutoff and associated group/event details as the form allows.
3. Monitor pickup and remaining allocation.
4. Review the block before its cutoff; expired blocks can release unpicked inventory through scheduled processing.
5. Confirm the resulting availability in the Tape Chart.

### 38.9 Group bookings and functions

1. Create the group record and organizer/contact details.
2. Create and link the room block when rooms are allocated to the group.
3. Track the rooming list and reservation pickup against that block.
4. For an event, create the function/venue and quotation; review margin and payment milestones.
5. Record received payments and follow-ups on the related records.
6. Reconcile pickup and release unused block inventory at the cutoff.

### 38.10 Housekeeping

1. Review the Room Board and task list for checkout cleans, priorities and overdue work.
2. Assign tasks using the available workflow.
3. Record completion after the room has actually been serviced.
4. If inspection is enabled, complete the supervisor inspection before marking the room ready.
5. Review escalations and update the underlying task/room status; do not mark a room ready before it is inspected where required.

### 38.11 Night audit

1. Confirm the property business date and time zone.
2. Open Night Audit and review the checklist: open tills/POS bills, due-out stays, high balances and rate variances.
3. Resolve blocking records. Use an override only where the screen offers it and record a meaningful reason.
4. Run the audit manually or verify the scheduled run according to property policy.
5. Review the Night Audit Run/audit pack, posted charges and all warnings/exceptions.
6. Confirm the business date rolled as expected before starting the next day's reconciliation.

### 38.12 Reports

1. Open Reports from the relevant application.
2. Choose the correct property, date range/business-date basis and filters.
3. Compare totals with source reservations, folios, cashier sessions or audit records.
4. Export or share only the required fields with authorized recipients.

---

## 39. Administrator Best Practices

- Use individual accounts and least-privilege roles; promptly disable access for departed staff.
- Protect API keys, payment credentials, MCP grants and webhook secrets in an approved secrets manager. Rotate credentials if exposed.
- Confirm backup schedules with the site operator and periodically test restoration through the approved recovery process.
- Review staff/property scope, activity history, webhook deliveries and connected AI clients regularly.
- Use payment test mode and controlled test flows before live collection. Do not test by creating fake production financial records.
- Confirm property country, time zone, currency, tax, inventory and business-date settings before opening for live operations.
- Reconcile cashier sessions, folios and night-audit exceptions every operating day.
- Minimize collection, display and export of guest personal/identity data; follow the configured retention policy and applicable law.
- Schedule configuration changes with affected departments, record the reason, then verify the resulting workflow.
- Do not use database edits, destructive imports, reruns of migrations or record deletion as a shortcut for correcting an operational error.

---

## 40. Source Verification and Runtime Variations

The administrator-visible labels, routes, role gates and setting fields in this guide were checked against this project's `frontend/src/lib/apps.ts`, `frontend/src/screens/settings/SettingsHub.tsx`, `frontend/src/screens/settings/api.ts`, `frontend/src/screens/settings/cards.tsx`, `frontend/src/screens/settings/McpAccessPage.tsx`, `frontend/src/screens/settings/WebhooksPage.tsx`, `frontend/src/screens/Dashboard.tsx`, `frontend/src/screens/Today.tsx` and `Quantumberg/settings.py`.

The site decides the actual property list, user's role grants, enabled modules, country-specific payment gateways, custom check-in steps and dashboard widgets at runtime. Those values cannot be asserted universally here. If a menu entry or field differs, use the live schema shown to an authorized user and consult the site administrator; do not infer a missing capability.

---

*End of Quantumberg Administrator Guide.*
