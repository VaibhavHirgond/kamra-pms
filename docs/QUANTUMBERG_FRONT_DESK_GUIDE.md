<p align="center">
  <img src="../frontend/public/quantumberg-logo.png" alt="Quantumberg Technologies" />
</p>

<h1 align="center">Quantumberg PMS Front Desk Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Front Desk Teams, Night Auditors, Hotel Administrators

---

## Table of Contents

1. Introduction
2. Access, Property Scope and Roles
3. Front Desk Sidebar Navigation
4. Today Dashboard
5. Kamra Agent
6. In House: Arrivals, In-house and Departures
7. Reservations and Reservation Detail
8. Tape Chart
9. Rooms
10. Guest History
11. Billing
12. Night Audit
13. Calendar
14. Central Reservations
15. Room Blocks
16. Group Booking
17. Reports
18. Front Desk Settings
19. End-to-End Workflows
20. Permissions and Security
21. Troubleshooting and FAQs
22. Glossary
23. Source Verification and Runtime Variations

---

## 1. Introduction

Front Desk is the daily operating workspace for guest arrivals, in-house stays, departures, reservations, rooms, guest history, billing and night audit. This guide describes the existing application screens and supported workflows without replacing the property's business rules.

## 2. Access, Property Scope and Roles

The Front Desk app is available to users with **Front Desk**, **Night Auditor**, **Hotel Admin**, **System Manager** or **Administrator** roles when the module is enabled. Access to settings and financial actions is more restrictive than access to the daily desk. The selected property in the header controls the displayed reservations, rooms, guests and business date.

Individual actions such as check-in, checkout, charge posting, ID-document access, room status changes and overrides are checked separately by the backend. A visible record does not imply access to every action.

## 3. Front Desk Sidebar Navigation

| Page | Purpose |
|---|---|
| Today | Daily overview, arrivals/departures, occupancy, tasks and room board. |
| Kamra Agent | AI assistant/workspace subject to configured AI access and permitted tools. |
| In House | Arrival, in-house and departure lists with date controls and stay actions. |
| Reservations | Search and open booking records; use New booking for creation. |
| Tape Chart | Date/room-type inventory timeline and booking allocation workflow. |
| Rooms | Room board, status filters, room drawer and room insights. |
| Guest History | Search guests, view stay statistics and export/select table columns. |
| Billing | Folios, night audit shortcut and cashier till shortcut. |
| Night Audit | End of Day checklist, business-date close and audit history. |
| Calendar | Calendar of reservations/availability; booking action depends on permission. |
| Central Reservations | Search reservations and supported property inventory centrally. |
| Room Blocks | Hold/release physical rooms for maintenance, VIP, owner or house use. |
| Group Booking | Group records, room blocks, pickup and rooming list. |
| Reports | Report hub filtered by role/module. |
| Settings | Front Desk configuration; restricted to Hotel Admin/System Manager/Administrator. |

## 4. Today Dashboard

Today shows the property's business date and summary cards for arrivals, departures, in-house stays, occupancy, revenue and open tasks. Financial figures may be hidden for roles without finance access. Additional cards include collected/outstanding/open folios, month-to-date occupancy/revenue, occupancy-on-the-books forecast, arrivals and room board information.

- Use **Customize** to change the personal widget layout where the feature is available; an authorized Hotel Admin can save a property default layout.
- Use arrival/departure links to open the corresponding In House tab.
- Use the room board to inspect status and open a room drawer.
- Use task cards to open operational task records; update the underlying task rather than treating a dashboard count as the record.
- The next-90-day occupancy strip distinguishes booked rooms from group-held inventory and offers a weekly breakdown.

The dashboard is a summary and may refresh; open the underlying reservation, folio or room record for changes.

## 5. Kamra Agent

Kamra Agent opens the assistant workspace. Available actions depend on AI provider setup, property-level AI access and the user's role/tool grants. Ask questions relevant to the selected property and review proposed actions before confirming them. The assistant does not override normal reservation, payment, permission or approval rules. If the assistant or a tool is unavailable, use the normal page for that workflow.

## 6. In House: Arrivals, In-house and Departures

In House provides **Arrivals**, **In-house** and **Departures** tabs. Use previous/next day and **Today**; arrival view can extend the date range using **Until**. Lists show guest, room, stay dates, source and amount due. Click a row to open the registration/stay detail.

- For today's arrivals, use **Check in** after confirming identity, room readiness, booking and payment requirements.
- Use **Check out** on eligible in-house/departure rows to review and complete departure.
- Use **Open folio** to inspect billing from a stay.
- Arrival ranges and date tabs are useful for planning but do not change the reservation dates.

## 7. Reservations and Reservation Detail

Reservations is a property-scoped list, searchable by reference, guest or room, filterable by status and check-in date. Statuses include **Requested**, **Held**, **Pending Payment**, **Waitlist**, **Confirmed**, **Checked In**, **Checked Out**, **Cancelled** and **No Show**. Create a new booking using the shell's **New booking** action; the resource list itself does not provide generic create.

Opening a reservation displays its detail workspace. Depending on status and role, actions include:

- Confirm/accept or decline an online booking request; a decline may require a reason.
- Check-in, checkout, room assignment/change and stay amendment.
- Cancellation/reinstatement, waitlist promotion and late-arrival handling.
- Deposit/payment review and payment-link state.
- Guest identity document capture and verification (subject to access/retention policy).
- Open folio, linked records, guest instructions and registration documents.

Before a status action, verify guest, dates, party size, room type/assignment, rate/tax, deposit, source and cancellation terms. Server validation controls availability and allowed transitions.

## 8. Tape Chart

Tape Chart presents room types and dates as a planning grid. Use the date range and room filters to review availability. Selecting a slot opens the booking/allocation flow when the user's role allows booking. Existing reservations can be opened from their chart cells. Allocation suggestions and room assignment controls are available where the property and reservation support them.

Do not infer that a visually free cell overrides a room block, out-of-order state or backend availability validation. Confirm the actual reservation record after saving.

## 9. Rooms

Rooms has **Board** and **Insights** views. The board supports room/guest search, floor and room-type filters, and status chips for all rooms, ready to sell, dirty, occupied, arriving today, departing today, out of service and open task. It refreshes periodically and supports manual refresh.

Select a room to open its drawer, which provides the room's current stay, guest/history, status/task information and permitted actions such as check-in/out, room change or housekeeping status. Insights summarizes room sales, revenue, cleaning and performance data where authorized. Use the status workflow rather than editing a room record to bypass a required inspection/block rule.

## 10. Guest History

Guest History can search by name or phone, paginate results and display guest name, phone, email, bookings, stays, nights, lifetime value and last stay. The **Columns** menu controls visible columns and remembers the choice in the browser. **Export** downloads the currently shown columns as CSV. Select a guest row to open their journey/history.

Guest information is personal data. Search only for a legitimate service purpose and follow the property's privacy and retention policy.

## 11. Billing

Billing lists folios with guest, status, invoice, total, paid and balance. Open a folio to review permitted charges, payments and invoice actions. The page also links to My Till and recent Night Audit runs/audit packs.

Verify the correct guest/reservation, folio balance, tax, payment mode and cashier session before posting. To correct completed postings, use an authorized allowance/void/refund action with the required reason rather than deleting the record.

## 12. Night Audit

Night Audit is labelled **End of Day** in some screens. It shows each accessible property's business date, property-local time, scheduled-run state, audit history and blockers such as pending arrivals/departures, open tills or POS bills. Scheduled audit uses the same configured checklist.

1. Confirm the property and business date.
2. Review blockers, open balances and departures still in house.
3. Resolve outstanding items or use only an explicitly offered authorized override with reason.
4. Run End of Day once.
5. Review posted room/tax charges, no-show/late-arrival results, exceptions and audit pack.
6. Confirm the business date advanced before beginning next-day work.

If the audit closed but the date did not advance, use the specific recovery action shown for a stuck date; do not rerun posting blindly.

## 13. Calendar

The Calendar displays reservation occupancy across dates and room types. Navigate dates and select an available slot to start a booking when the user's booking permission allows. The calendar's display is planning information; the booking API validates availability and restrictions when saving.

## 14. Central Reservations

Central Reservations (CRS) provides the supported central search/booking workflow across the properties the user can access. Enter the stay dates and occupancy/search criteria exposed by the page, review available property/room-type results, and open the selected result to proceed with a booking. Property scope and module access affect results. Confirm final availability and pricing in the booking flow before promising inventory.

## 15. Room Blocks

Room Blocks are physical-room holds that remove rooms from sale. Create a block with room, reason (**House Use**, **VIP Hold**, **Owner**, **Maintenance** or **Other**), **From date**, **To date (exclusive)**, status (**Active** or **Released**) and note. Search by room/note and filter by reason/status.

Use a block for inventory that should not be sold, such as a maintenance hold. Review the exclusive end date carefully. Release the block through its supported status action when the room is sellable again.

## 16. Group Booking

Choose **New group booking** to create a group with required group name and stay dates, optional company, cutoff date and notes. The list filters by **Open**, **Confirmed** or **Cancelled**, arrival date and search fields. Opening a group provides Group Rooms Control, block/pickup and rooming-list-related workflows.

Confirm cutoff and pickup before releasing unallocated rooms. A group booking is not the same record as an individual reservation or a physical room maintenance block.

## 17. Reports

The Reports hub groups links into department packs, custom reports, daily reports, revenue, finance and operations. What is visible depends on role and enabled modules. The custom report builder uses server-approved datasets, columns and filters; select the date range, preview and save/share/schedule only if permitted.

Use reports for analysis and exports, then follow a source link to correct the underlying reservation, folio, task or cashier record. Do not treat an export as a write-back.

## 18. Front Desk Settings

Hotel Admin can edit the Front Desk settings module. The settings include:

| Section | Fields |
|---|---|
| Arrivals | Automatically send pre-check-in links, how far ahead, whether pre-check-in is required before access details, access instructions. |
| Door locks | Door lock system selection/configuration. |
| Guest info at check-in | Wi-Fi name/password, breakfast times, emergency number and additional guest instructions. |
| Guest alerts | WhatsApp guest when a room charge is posted. |
| Holds & selling | Hold duration for unconfirmed bookings and sell message. |
| Night audit & no-shows | No-show handling, late-arrival hold, OTA no-show fee rule and release time for non-guaranteed arrivals. |
| Automatic night audit | Enablement, run time and grace/wait interval. |
| Night audit checklist | Whether open tills/POS bills/departures block audit, high-balance threshold, rate variance tolerance and scheduled-audit behavior when blocked. |
| Hourly view | Day-start and day-end boundaries. |

Changes affect guest communication, inventory release and business-date close. Test the configured guest-facing instructions and audit schedule with the property before relying on them.

## 19. End-to-End Workflows

### Check in a confirmed arrival

1. Open In House → Arrivals and select the correct date.
2. Open the reservation and verify guest identity, dates, guest count, deposit/payment, source and room.
3. Confirm the room is clean/ready and assign it through the check-in flow.
4. Capture/verify guest ID if required by property process; complete registration and any outstanding payment.
5. Check in and confirm the stay appears in In-house and the room board.

### Complete checkout

1. Open In House → Departures or select the stay from the room board.
2. Review folio charges, taxes, payments, deposit and balance.
3. Resolve allowed adjustments through the authorized workflow; settle or follow approved company credit.
4. Complete checkout and verify folio closure and room turnover task/status.

### Handle a maintenance block

1. Open Room Blocks and create a block for the correct room and dates.
2. Select Maintenance, set the exclusive end date and add a useful note.
3. Verify that the room is excluded from sellable availability.
4. Release the block only after maintenance has confirmed the room is usable.

## 20. Permissions and Security

- Front Desk visibility does not confer Finance or Settings privileges.
- Reservation, guest ID, folio, check-in/out, room status and audit actions each have server-side checks.
- Guest identity documents are sensitive; access, verification and disposal follow property retention policy.
- Do not share guest lists, folios, access instructions or payment information outside authorized channels.
- Use the selected property deliberately before creating a reservation or financial record.

## 21. Troubleshooting and FAQs

| Problem | Checks |
|---|---|
| Reservation does not appear | Verify property, date range, status filter, search text and user property permissions. |
| Check-in is unavailable | Check reservation status/date, room assignment/readiness, required payment/registration and user role. |
| Room appears unavailable | Review current stay, active Room Block, out-of-order status and housekeeping status. |
| Folio cannot be settled | Check open till/PIN requirement, payment mode, folio status and Finance authorization. |
| Night Audit is blocked | Resolve open till/POS bills, due-out stays or configured balance/rate exceptions; consult audit checklist. |
| Guest ID is not visible | Verify the reservation, user permission and retention status; discarded documents cannot be retrieved from the UI. |
| Report link is missing | The role, module or report dataset may not be enabled for this user/property. |

## 22. Glossary

- **Business date:** Hotel operating date used for daily close and reporting.
- **Folio:** Guest bill with charges/payments.
- **Room block:** Inventory hold that removes a physical room from sale.
- **Tape Chart:** Date-based room/inventory planning grid.
- **No-show:** Reservation guest did not arrive under the property's configured rules.
- **Night Audit / End of Day:** Close process that posts room/tax and advances the business date.
- **CRS:** Central Reservations search and booking workspace.

## 23. Source Verification and Runtime Variations

This guide follows the Front Desk app registry, Today/In House/Reservation/Rooms/Tape Chart/Guest/Calendar/CRS/Billing/End of Day screens, resource forms, settings schema, backend endpoints and the live application. Actual fields, roles, taxes, guest-ID policy, room-lock integration, booking inventory and report availability depend on the property's configuration and enabled modules.
