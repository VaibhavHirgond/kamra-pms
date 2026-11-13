<p align="center">
  <img src="../images/quantumberg-logo.png" alt="Quantumberg Technologies" style="width: 200px; max-width: 100%; height: auto;" />
</p>

<h1 align="center">Quantumberg PMS Revenue Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Revenue Managers, Hotel Administrators, System Managers

---

## Table of Contents

1. Introduction
2. Access, Property Scope and Roles
3. Revenue Sidebar Navigation
4. Revenue Dashboard
5. Owner View
6. Reports
7. Channel Manager and OTA Room Mappings
8. Rate Calendar
9. Rate Plans
10. Seasons
11. Guardrails
12. Vouchers and Long-stay Discounts
13. Meal Plans
14. Experiences
15. Room Types
16. Travel Agents
17. Accounts Receivable
18. Revenue Settings
19. End-to-End Workflows
20. Permissions and Security
21. Troubleshooting and FAQs
22. Glossary
23. Source Verification and Runtime Variations

---

## 1. Introduction

Revenue brings together property performance, pricing controls, channels, offers, room types and sales-source records. It complements (but does not replace) the booking, folio, finance and channel provider systems of record.

## 2. Access, Property Scope and Roles

Open **Revenue** from the app switcher. The app requires **Revenue Manager**, **Hotel Admin**, **System Manager** or **Administrator**, and the module must be enabled for the property. Data is property-scoped except where an explicitly available portfolio view summarizes multiple accessible properties. The active property in the header affects record screens and reports.

The shared Reports hub may also show revenue links to users with other report roles. That does not grant write access to revenue configuration. API and document permissions remain authoritative.

## 3. Revenue Sidebar Navigation

| Page | Purpose |
|---|---|
| Revenue Dashboard | Review daily/month-to-date performance and property/portfolio summaries. |
| Owner view | Compact mobile-oriented performance, money, guest movement and audit summary. |
| Reports | Shared report hub, revenue report builder/packs and revenue-specific reports. |
| Channel Manager | Configure OTA connectivity. |
| OTA Room Mappings | Match local room types/rate plans to provider identifiers. |
| Rate Calendar | Review and maintain date-based room pricing. |
| Rate Plans | Configure sellable pricing plans and modifiers. |
| Seasons | Set date-specific adjustments and restrictions. |
| Guardrails | Set room-rate floors and ceilings. |
| Vouchers | Maintain booking discount codes. |
| Long-stay Discounts | Configure length-of-stay rate reductions. |
| Meal Plans | Configure board basis and per-person pricing. |
| Experiences | Configure booking add-ons such as tours or dining. |
| Room Types | Maintain capacity and base pricing used by quotes. |
| Travel Agents | Maintain source/commission records. |
| Accounts Receivable | Maintain corporate accounts and credit terms. |
| Settings | Revenue settings, including the overbooking allowance. |

## 4. Revenue Dashboard

The dashboard presents daily and month-to-date operating figures, departmental revenue and portfolio summaries where the user can access multiple properties. Use the property/scope selectors to choose a property or portfolio view. The displayed metric set is role-gated; users without the required financial/revenue role do not receive all figures.

Use the dashboard as a summary. For a discrepancy, open the relevant Revenue Report, reservation, folio, till or source record. A dashboard is not an edit screen and may refresh according to live data availability.

## 5. Owner View

Owner View is a compact summary designed for mobile use. It can switch between accessible properties and periods such as today, yesterday and month to date. Sections cover revenue, guest movement, money/outstanding balances, the next seven days, night audits and links to further reports. Figures are visible only to the backend-authorized roles.

Use the date/period and property controls to contextualize the summary. Follow report links to inspect detail; do not treat an omitted figure as zero until the selected property/date and permission scope have been checked.

## 6. Reports

The shared **Reports** page filters the available report links using the user's roles and enabled modules. Revenue users may access:

- Revenue Dashboard and Revenue Reports (pickup, pace, source and segment mix).
- Department packs and custom reports where the report builder role permits.
- Manager Flash, which summarizes occupancy, ADR, RevPAR, revenue and collections.
- Other report cards exposed by the user's access.

In the report builder, choose a server-whitelisted dataset, date range, columns and available filters, then preview. Saved reports can be titled, shared where authorized and scheduled with frequency/time/recipients. The backend applies dataset permissions and range limits; if a dataset or field is absent, do not attempt to bypass the whitelist.

## 7. Channel Manager and OTA Room Mappings

### 7.1 Channel Manager

Create a property connection using provider (**Channex**, **STAAH**, **AioSell** or **Custom**), API key/token, provider property ID, optional endpoint override, webhook secret, days to push and Active state. Credentials are stored encrypted by the application. Provider support and onboarding credentials are required; selecting a provider alone does not establish a live connection.

The connection list includes provider, provider property ID, last push, result and Active state. Availability/rate sync and incoming reservation handling depend on provider integration, valid mappings, connectivity and the active configuration.

### 7.2 OTA Room Mappings

For each provider room/rate mapping, select the **Channel Manager Connection**, local **Room Type**, provider room ID and optional provider rate-plan ID. Mappings determine which local inventory is synchronized and how incoming bookings resolve to a room type. Verify IDs against the provider account; incorrect mappings can misroute availability or reservations.

## 8. Rate Calendar

The calendar displays room-type pricing across a date range. Navigate earlier/later and choose the number of days shown. Select a room/date cell to inspect the rate and available edit actions. Rate values interact with room-type base price, rate-plan modifiers, seasonal rules and guardrails. Confirm the effective price and availability after saving a change.

Use the calendar for date-specific review, not as a replacement for configuring reusable plans or season rules. A seasonal/high-priority adjustment or floor/ceiling can constrain the final sellable rate.

## 9. Rate Plans

Rate Plans define a sellable plan (for example BAR, non-refundable or corporate). The record includes:

- Required plan **Name** and **Code**.
- **Modifier type**: Percent, Amount or Absolute.
- **Modifier value** (a negative percentage can represent a discount).
- Cancellation policy text.
- **Default plan** and **Disabled** status.

An enabled (not disabled) plan is available for booking; disabling unpublishes it. Validate the plan against current room types, rates and booking policies before activation.

## 10. Seasons

A Season applies a date-range rate adjustment and related booking restrictions. Configure:

- Name; optional room type (blank applies across types); inclusive start/end dates.
- Adjustment type (Percent, Amount or Absolute) and value.
- Days of week and priority; the highest applicable priority wins.
- Minimum nights, non-refundable, full-payment requirement and advance percentage.
- Holiday/long-weekend flag, small-group-rate restriction and Disabled status.

Season advance percentage of zero uses the property's usual deposit percentage. Where a stay crosses seasonal dates, the booking logic uses the highest applicable advance requirement. Review overlaps, priorities and stay-through restrictions before activating a season.

## 11. Guardrails

Guardrails protect an owner-defined nightly rate floor and ceiling. Set an optional room type, required floor and ceiling, optional days of week, and Disabled state. A blank room type applies to all types; blank days apply every day. Active guardrails constrain rate changes, including supported agent-driven changes. Set floors/ceilings deliberately and review them alongside season adjustments.

## 12. Vouchers and Long-stay Discounts

### Vouchers

Voucher fields include required code and value, discount type (**Percent** or **Amount**), validity dates, minimum nights, maximum uses and disabled state. **Times used** is read-only. Maximum uses of zero means unlimited. Disable a code to deactivate it; verify validity and intended distribution before sharing.

### Long-stay Discounts

Set the minimum stay nights, percentage discount, optional room type and Disabled status. For a stay that qualifies for more than one tier, the highest tier reached applies. Guardrail floors still protect the nightly rate.

## 13. Meal Plans

Meal Plans use code (**EP**, **CP**, **MAP** or **AP**), label, price per adult/night, price per child/night, default flag and Disabled flag. Confirm the board basis and rates before setting a default; meal-plan pricing is not the same as an F&B POS order.

## 14. Experiences

Experiences are optional add-ons for the public booking flow. Configure name, category (**Spa**, **Tour**, **Dining**, **Activity**, **Transport** or **Other**), price, tax, duration, guest-facing description, image, public booking visibility and Disabled status. Only active records with **Show on the public booking page** enabled are intended for display there.

## 15. Room Types

Room Types hold inventory categories, capacities and base pricing. Important fields include name/code, listing slug, category, base price, base occupancy, single/extra-adult/child pricing, adult/child capacity, tax, bed type and air-conditioning details. Optional small-group pricing includes threshold, per-adult price, applicable weekdays and whole-stay rule. Additional property/site listing fields include location name/address/slug, Google Maps URL and coordinates. Disabled room types should not be sold.

Review how occupancy-based rates and capacities affect quotations before changing a room type already linked to reservations.

## 16. Travel Agents

Maintain agent name, type (**Travel Agent**, **OTA**, **Tour Operator** or **Corporate Desk**), commission percentage and contact details. Commissions are computed for linked bookings according to the record; keep source attribution accurate. Disable an agent rather than using an obsolete source for new business.

## 17. Accounts Receivable

Accounts Receivable here is the **Corporate Account** master list, not the Finance ledger. Configure company name, tax ID, contact name/phone/email, negotiated rate plan, credit allowed and Disabled. The company detail panel contains additional account information where available. Grant city-ledger credit only after approval under property policy; actual invoices, aging and payments are handled in Finance.

## 18. Revenue Settings

The Revenue settings schema includes **Overbooking allowance** under **Overbooking**. Treat this as a deliberate inventory-risk setting and document the property's recovery plan before increasing it. Rate plans, seasons, guardrails, channel mappings and corporate accounts remain separate records.

## 19. End-to-End Workflows

### Publish a rate plan and seasonal offer

1. Confirm room types, base prices, capacity and tax.
2. Create or update the Rate Plan and set its modifier/cancellation terms.
3. Create the Season with inclusive dates, eligible room type, adjustment, priority and restrictions.
4. Check for overlapping seasons and active guardrails.
5. Review the Rate Calendar across affected dates and confirm effective rates.
6. Test the public booking path or controlled quote before promoting the offer.

### Connect an OTA

1. Obtain the provider credentials and property ID from the authorized provider account.
2. Create and activate the Channel Manager connection using the correct property and endpoint details.
3. Add OTA Room Mappings for each local room type/provider room and rate plan.
4. Check last push/result and provider-side mapping state.
5. Verify an inbound reservation and outbound availability/rate after the connection is live.

### Configure a voucher

1. Create a unique code and choose Percent or Amount.
2. Set value, validity dates, minimum nights and usage limit.
3. Leave the record enabled only when the code is approved for use.
4. Test eligibility in the booking flow and monitor use count; disable when expired.

## 20. Permissions and Security

- Revenue app access is restricted to Revenue Manager, Hotel Admin, System Manager and Administrator roles, subject to module enablement and property scope.
- Report builder and Owner View have separate backend role gates; a link can be hidden even when another revenue screen is visible.
- OTA credentials and webhook secrets are sensitive; do not paste them into documentation, notes or support screenshots.
- Ask an administrator to grant least-privilege access. Never share a privileged account to work around missing permissions.
- Rate/overbooking changes affect sellable inventory and revenue; follow the property's approval process.

## 21. Troubleshooting and FAQs

| Problem | Checks |
|---|---|
| No dashboard figures | Check selected property/date, role access, current business date and source data. |
| Provider push fails | Verify provider credentials, external property ID, endpoint/webhook secret and provider status. |
| OTA booking has no room type | Check that the connection is active and the inbound provider room ID maps to the correct local room type. |
| Calendar price differs from expected | Review room-type base price, active season priority, rate plan, weekday rule and guardrail. |
| Voucher is rejected | Check code spelling, disabled state, dates, min nights and usage cap. |
| Experience is not public | Confirm active state, public visibility checkbox, property booking engine state and image/content configuration. |
| Cannot edit a revenue record | Verify role, selected property, module enablement and record permissions. |

## 22. Glossary

- **ADR:** Average Daily Rate.
- **RevPAR:** Revenue per Available Room.
- **OTA:** Online Travel Agency.
- **Rate plan:** Sellable plan that modifies or defines room pricing.
- **Season:** Date range carrying an adjustment/restriction.
- **Guardrail:** Rate floor/ceiling constraint.
- **Pickup:** Reservations added for a future stay/event period.
- **Channel mapping:** Link between local inventory and provider identifiers.

## 23. Source Verification and Runtime Variations

This guide follows the Revenue app registry, dashboard and report screens, resource-form configuration, rate calendar, channel integration screens, backend APIs and the live application. Provider availability, external credentials, property rates, role grants, country settings and live booking-engine state vary by deployment. Do not treat sample property figures as expected values.
