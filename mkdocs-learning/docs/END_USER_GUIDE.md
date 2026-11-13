<p align="center">
  <img src="../images/quantumberg-logo.png" alt="Quantumberg Technologies" style="width: 200px; max-width: 100%; height: auto;" />
</p>

<h1 align="center">Quantumberg PMS – Complete End-User Operations Guide</h1>

**Product version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** All Hotel and Restaurant Operations Staff

---

## Table of Contents

1. [Introduction and Getting Started](#1-introduction-and-getting-started)
2. [Finding Your Way Around](#2-finding-your-way-around)
3. [Start-of-Day and Property Readiness](#3-start-of-day-and-property-readiness)
4. [Rates, Booking Engine and Channels](#4-rates-booking-engine-and-channels)
5. [Guests and Reservations](#5-guests-and-reservations)
6. [Groups and Room Blocks](#6-groups-and-room-blocks)
7. [Arrivals and Check-in](#7-arrivals-and-check-in)
8. [In-house Guests, Requests and Communication](#8-in-house-guests-requests-and-communication)
9. [Guest Charges, Payments and Checkout](#9-guest-charges-payments-and-checkout)
10. [Departures and Room Turnover](#10-departures-and-room-turnover)
11. [Housekeeping Operations](#11-housekeeping-operations)
12. [Laundry, Lost and Found, and the Phone App](#12-laundry-lost-and-found-and-the-phone-app)
13. [Restaurant and F&B Operations](#13-restaurant-and-fb-operations)
14. [Banquets and Events](#14-banquets-and-events)
15. [Finance and Cashier Operations](#15-finance-and-cashier-operations)
16. [Revenue and Booking Engine Operations](#16-revenue-and-booking-engine-operations)
17. [Night Audit and Business-Date Close](#17-night-audit-and-business-date-close)
18. [How Departments Work Together](#18-how-departments-work-together)
19. [Role-Based Daily Checklists](#19-role-based-daily-checklists)
20. [Troubleshooting and Common Mistakes](#20-troubleshooting-and-common-mistakes)
21. [Glossary](#21-glossary)
22. [Source Verification and Runtime Variations](#22-source-verification-and-runtime-variations)

---

## 1. Introduction and Getting Started

Quantumberg PMS brings hotel and restaurant work into one system. Front Desk staff manage reservations, guests, arrivals, stays and folios. Housekeeping manages room readiness and tasks. Operations handles guest requests and approved communication channels. Restaurant staff take orders in POS and send kitchen tickets. Banquet staff manage event enquiries and functions. Finance supports till sessions, accounts, reconciliation and reports. Revenue staff manage pricing, distribution and the public booking experience.

The application is organized as role- and property-scoped apps. The same guest stay may involve several departments, but each team updates the record or task it owns. A dashboard or report summarizes activity; it does not replace the underlying reservation, folio, ticket, order or room record.

### 1.1 Sign in and sign out

1. Open the Quantumberg site or the Hotel application in Frappe Desk.
2. Enter your assigned email/username and password on the login screen and select **Sign in**.
3. If sign-in succeeds, the application opens at the page allowed for your account.
4. To finish work, open the user menu in the top bar and select **Logout**.

If the session has expired, sign in again. Do not share passwords or remain signed in on a shared device when your shift is over.

### 1.2 Property and business date

If your account can access multiple properties, use the property selector in the top bar to choose the hotel you are working at. Check it before creating or changing any reservation, room task, ticket, POS order, till entry or financial record. A user who has access to only one property may not see a selector.

The **business date** is the hotel's operating date, which can differ from the calendar date around night audit. Cashier sessions, audit checks and daily reports use the property's business-date rules. Check the date shown by the page before closing a till or running Night Audit.

### 1.3 Login permissions

Pages and actions depend on your assigned role, property access and enabled modules. For example, an attendant may update a room to Clean but not mark it Ready; a finance action may require a cashier PIN or approver; and settings may be read-only. If a button or app is missing, ask your manager or administrator to check your access. Never use another employee's account or attempt to bypass a permission.

## 2. Finding Your Way Around

### 2.1 App switcher and sidebars

Use the app switcher in the top bar to move between **Front Desk**, **Housekeeping**, **Operations**, **F&B**, **Banquets & Groups**, **Revenue**, **Finance**, **Booking Engine** and **Admin**, as permitted. Each app has its own sidebar. Common entries include:

| App               | Daily work                                                                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Front Desk        | Today, In House, Reservations, Tape Chart, Rooms, Guest History, Billing, Night Audit, Calendar, Central Reservations, Room Blocks, Group Booking, Reports and Settings.                                                                         |
| Housekeeping      | Room Board, Rooms, Tasks, Laundry, Lost & Found, Reports, Phone App and Settings.                                                                                                                                                                |
| Operations        | Guest Requests (Tickets), WhatsApp, Channels, Reports and Settings.                                                                                                                                                                              |
| F&B               | Restaurant POS, F&B Dashboard, Kitchen Display, Menu, Ingredients, Kitchen Inventory, Outlets, Printers, Reports and Settings.                                                                                                                   |
| Banquets & Groups | Banquets, Month Availability, Function Diary, Registers, Menus & Services, All Functions, Groups & Blocks, Halls & Venues and Settings.                                                                                                          |
| Revenue           | Revenue Dashboard, Owner view, Reports, Channel Manager, OTA Room Mappings, Rate Calendar, Rate Plans, Seasons, Guardrails, Vouchers, Long-stay Discounts, Meal Plans, Experiences, Room Types, Travel Agents, Accounts Receivable and Settings. |
| Finance           | My Till, All Tills, Sessions, Petty Cash, Shift Handover, Currency Desk, Billing, Folio History, Receivables, Ledgers, Payables, Cash outlook, Profit and loss, reports and related finance tools.                                               |
| Booking Engine    | Hotel Profile, Amenities, Photos, Policies, Payments, FAQ, SEO and Settings.                                                                                                                                                                     |

The app and entry names shown depend on module enablement and role access.

### 2.2 Search, notifications and dashboards

- Use the global search button or **Ctrl/Cmd+K** to find supported pages and actions.
- The notification control shows notifications available to your account. Open an item to inspect the relevant record when a destination is provided.
- Use **Today** for a Front Desk overview. Use app-specific dashboards for F&B or Revenue detail.
- Use **Reports** for permitted department packs, custom reports and summaries.

Search results, notification counts and dashboards are not proof that an action is complete. Open the source record to verify status.

## 3. Start-of-Day and Property Readiness

Start with the selected property and its business date. The exact opening tasks depend on the department and property policy.

### 3.1 Front Desk opening review

1. Open **Front Desk → Today** and review arrivals, departures, in-house count, occupancy and open tasks.
2. Open **Front Desk → In House** and check today's arrivals and departures. Confirm unusual dates, room assignments or guest notes with the reservation.
3. Open **Front Desk → Rooms** or the shared room board and compare dirty, clean, inspected, blocked and occupied states.
4. Review open guest requests from **Operations → Guest Requests (Tickets)** and assign or follow up on urgent/unassigned work.
5. Check the cashier session under **Finance → My Till** if you are responsible for taking payments.

### 3.2 Room availability and rates

Front Desk may review room availability using the **Tape Chart**, **Calendar** or **Rooms**. Do not promise a room based only on a dashboard count. Active room blocks, out-of-order rooms, existing reservations, stay rules and room readiness all affect whether a room can be sold.

Revenue-authorized staff review rates in **Revenue → Rate Calendar** and reusable plans under **Rate Plans**, **Seasons** and **Guardrails**. Most Front Desk staff should not change these controls. If a displayed rate appears wrong, capture the dates, room type, rate plan and reservation, then ask Revenue to review.

### 3.3 Restaurant opening review

Restaurant managers should confirm the correct outlet is selected, active menu items are available, the Kitchen Display is open at required stations, and configured printers are available. Review outstanding orders and stock warnings in the F&B app. Do not mark an unavailable item as available merely to clear a shortage warning.

### 3.4 Banquet opening review

Banquet staff should open **Banquets** or **Function Diary**, review reminders and high-priority follow-ups, verify the venue/session for today's functions, and confirm guaranteed attendance, event requirements and balances on the function record.

## 4. Rates, Booking Engine and Channels

This section explains how a guest's online or channel booking becomes work for the hotel. Only Revenue/Booking Engine authorized roles edit rates, channel credentials and public property content.

### 4.1 How online availability is determined

The public booking flow searches dates, guest count and room types, then shows server-calculated availability and prices. Availability depends on configured room types/inventory, reservations and blocks, selected dates, occupancy rules, minimum nights, enabled booking engine and active rate/policy configuration. The public page does not guarantee a room until its booking request is accepted/confirmed according to the configured payment and booking workflow.

### 4.2 Online booking to Front Desk

1. Guest selects check-in/check-out, adults/children and an available room type on the public booking page.
2. Guest reviews the server-calculated quote, meal plan/add-ons if offered, policies and required payment.
3. Guest enters the required contact/guest details and submits the booking/payment step.
4. A booking request or reservation appears in the PMS with its source/channel and current status. Payment or deposit state is shown in reservation detail.
5. Authorized staff open **Front Desk → Reservations**, verify the request, inventory, guest and payment state, then use the available accept/confirm or follow-up action.
6. Front Desk handles the confirmed stay through arrivals, check-in, folio and checkout.

Do not treat a payment link or pending payment as settled until the reservation detail reflects the received payment. If the record remains Requested, Held or Pending Payment, follow the status and payment actions shown by the application.

### 4.3 OTA bookings

An OTA reservation reaches the PMS through a configured channel-manager connection and room mapping. Revenue or an administrator configures the connection and maps local room types to provider IDs. Front Desk handles the resulting reservation like other bookings but should retain the source/channel information and check its imported dates, guests and room type.

If the booking is missing or mapped incorrectly, contact Revenue/IT to check connection activity, provider room IDs and last-push/error details. Do not create a duplicate booking until the channel result has been checked.

## 5. Guests and Reservations

### 5.1 Search before creating a guest

Open **Front Desk → Guest History** and search by guest name or phone before creating a new profile. Select a result to inspect the guest journey, past stays and contact details. Reuse the correct existing profile; ask the guest or supervisor if records may refer to different people. Guest information is personal data—collect and share only what the stay requires.

### 5.2 Create a reservation

Start a reservation from **Front Desk → Reservations** using **New booking**, or from a supported date/room slot in Tape Chart, Calendar or Central Reservations.

1. Confirm the selected property and enter check-in/check-out dates, adults/children and room type/availability.
2. Select an existing guest or enter the guest information requested by the booking form. Avoid creating a duplicate guest.
3. Review the price, rate plan, taxes/fees, source, special requests, guarantee/deposit and cancellation terms shown.
4. Assign a room only when the workflow permits and an eligible room is available. If no specific room is assigned, preserve the room type and let the supported allocation workflow handle it.
5. Select the form's save/create action and wait for confirmation.
6. Reopen the reservation and verify the reference, status, dates, guest, room type/room, source and payment/deposit summary.

Required form fields and actions can differ by booking source, property configuration, stay and role. Server-side availability and transition checks remain final.

### 5.3 Reservation statuses

Common statuses include **Requested**, **Held**, **Pending Payment**, **Waitlist**, **Confirmed**, **Checked In**, **Checked Out**, **Cancelled** and **No Show**. Status is not the same as payment status. A reservation can require a deposit even when it is confirmed, and a pending request may have a separate payment link.

Open the reservation detail to use supported actions such as accepting/declining a booking request, taking a deposit, confirming, cancelling/reinstating, promoting a waitlist entry, recording late arrival, changing a room or amending dates. Some actions require a reason, permission, payment or eligible status. Use the action shown by the screen; do not directly edit status to skip a required step.

### 5.4 Deposit and payment review

In the reservation detail's **Billing** area, compare total, paid and balance due. Deposit and security-deposit panels appear when applicable. Use the supported payment/link action. Wait for the result to return to the reservation or folio before telling a guest that payment has cleared.

## 6. Groups and Room Blocks

### 6.1 Group booking

Choose **Front Desk → Group Booking → New group booking**. The multi-step form collects group name/type, dates, company/payer information, room-type blocks and rooming-list details. Where available, it also supports negotiated rate, rooms-per-night, deposit, attrition and quotation-only options.

1. Enter group name/type and arrival/departure dates.
2. Select company/payer and the billing arrangement shown by the form.
3. Add room types and block counts. Review the server-generated price preview.
4. Enter the rooming list by guest and phone; each guest can have their own dates within the group dates. The paste/upload option can accept a supported spreadsheet/CSV list.
5. Review the summary, price, block, cutoff and warnings before submitting.
6. Check the result for created reservations, skipped guests and warnings. Open the resulting group to manage pickup and rooming-list details.

Guests not named in the rooming list can remain held in the block until cutoff; verify the group's specific result. Do not assume every blocked room has a guest assigned.

### 6.2 Individual room blocks

Use **Front Desk → Room Blocks** for a physical room taken out of sale (for example maintenance, VIP, owner or house use). Select the room, reason, **From date**, **To date (exclusive)**, status and note. Review the end date carefully: it is exclusive. Release the block through the supported status action when the room can be sold again.

Group room blocks and physical room maintenance blocks serve different purposes. Use Group Booking for group allocations and Room Blocks for a physical room hold.

## 7. Arrivals and Check-in

1. Open **Front Desk → In House → Arrivals** and choose the correct day. For future planning, use the date range control; check-in actions are available only for eligible arrivals.
2. Open the reservation/registration detail. Confirm guest identity, reservation status, dates, party size, room type, room assignment, payment/deposit and special requests.
3. Confirm the room is ready in **Rooms** or with Housekeeping. A dirty or blocked room should not be assigned as ready.
4. Use **Check in** and complete the form/dialog fields shown, such as room assignment, registration details and payment decisions.
5. Capture/verify an ID document when required by the property's process. Use **Verify identity** only after comparing the document with the guest.
6. Confirm the result: the reservation should be Checked In, appear in the In-house list, and be reflected in the room board.
7. If the room is unavailable, the guest identity/details do not match or money remains due, stop and resolve the discrepancy with the appropriate supervisor/Finance staff.

Online pre-check-in information and access instructions may appear in reservation detail. A missing ID warning does not necessarily block arrival; follow the property's policy and the controls displayed.

## 8. In-house Guests, Requests and Communication

### 8.1 Manage an in-house stay

Open **Front Desk → In House → In-house**, select the correct date and guest, and use reservation detail for permitted date amendments, room changes, late-arrival notes, guest instructions and linked folio access. Changing dates may change availability and the amount due. Confirm the final dates and price with the guest and verify the saved result.

Use **Rooms** to check occupancy and **Room Board** to coordinate housekeeping. A room move should be completed through the room-change workflow so that the reservation and inventory remain aligned.

### 8.2 Guest Requests (Service Tickets)

Open **Operations → Guest Requests (Tickets)**. Create a manual request with subject, category, priority, optional room and details; select **Create ticket**. Categories include Housekeeping, Room Service, Maintenance, Front Desk, Concierge, Complaint and Other. Use neutral, factual descriptions and avoid unnecessary sensitive details.

The ticket views are:

| View       | Meaning                                   |
| ---------- | ----------------------------------------- |
| Open       | Open or In Progress work.                 |
| Mine       | Open work assigned to the signed-in user. |
| Unassigned | Open work without an owner.               |
| Overdue    | Open work past its due time.              |
| Resolved   | Resolved/Closed records.                  |
| All        | Tickets for the selected property.        |

Open a ticket to review the guest/room, priority, SLA time, description and timeline. Assign a staff member, select **Assign to me**, **Start work**, add a note, then use **Mark solved** with an optional resolution note when complete. Reopening a completed request may require a reason. The actual actions offered depend on ticket status and role. Ticket deadlines come from the priority and Operations settings.

### 8.3 WhatsApp and channels

Authorized staff use **Operations → WhatsApp** to open a guest conversation and review inbound/outbound messages. Select the thread, read its latest messages and reply in the composer. Free-form replies are allowed only while the guest's 24-hour messaging session is open; outside that window use the approved template workflow where configured. Do not promise delivery until the message status confirms it.

**Operations → Channels** is for authorized administrators to connect provider phone/messaging lines. Staff should report a failed connection rather than changing credentials. The reservation/detail link may open the associated stay for context.

## 9. Guest Charges, Payments and Checkout

### 9.1 Post or review guest charges

Open the guest's folio from reservation detail or **Finance → Billing**. Check the folio, guest, reservation and property before posting. Use the supported charge action and select the correct charge/code and amount. Restaurant room-service charges are posted from the POS settlement workflow when the room is eligible; do not manually add a duplicate charge.

### 9.2 Take payment

Collect money from the correct source screen: reservation/deposit workflow, folio settlement, Restaurant POS or company Receivables. If cashier tills are required, ensure the responsible cashier has an open till and use their authorized session. Verify the posted payment and remaining folio balance after the action completes.

### 9.3 Check out

1. Open **Front Desk → In House → Departures** or the guest's reservation detail.
2. Review every folio line, tax, payment, deposit, credit and balance.
3. Resolve discrepancies using the permitted adjustment/allowance/refund action and required reason/approval.
4. Settle the balance or follow the approved company-credit workflow.
5. Select **Check out** and complete any final confirmation shown.
6. Verify the reservation is Checked Out, the folio is closed/settled as expected, and the room is flagged for turnover.

Do not mark a folio paid because a guest shows a bank notification; verify the PMS payment record. Do not delete accounting entries to correct an error.

## 10. Departures and Room Turnover

Checkout updates the stay and leads to a room-cleaning task/status for Housekeeping. Front Desk should confirm checkout succeeded, then hand the room to Housekeeping. Housekeeping marks the physical work complete and, where required, a supervisor inspects the room. Only after the required steps should the room become Ready for sale.

The **Rooms** board distinguishes occupancy and housekeeping status. A Checked Out guest does not mean the room is already clean. Do not assign an arriving guest to a room until Front Desk and Housekeeping agree it is ready.

## 11. Housekeeping Operations

### 11.1 Room statuses

| Status       | Staff meaning                                                                          |
| ------------ | -------------------------------------------------------------------------------------- |
| Dirty        | Cleaning/turnover is still required.                                                   |
| Clean        | Housekeeping has cleaned the room. It may still need supervisor inspection if enabled. |
| Inspected    | A supervisor has completed the inspection step.                                        |
| Ready        | The room is released as sellable under the property's configured workflow.             |
| Out of Order | The room is not available for sale.                                                    |

The allowed transitions shown to you depend on your role. Attendants generally receive **Dirty** and **Clean** controls; supervisor/authorized roles receive broader inspection, Ready and Out of Order controls.

### 11.2 Assign and complete room tasks

1. Open **Housekeeping → Room Board** or **Tasks**.
2. Filter by floor, status, due-out or open task; review room, occupancy, priority, notes and assignee.
3. A supervisor assigns eligible work to a housekeeper. Use the task assignment control; do not assign work to a user who is not in the property staff list.
4. Open **Tasks** and select/create the correct room task: Checkout Clean, Stayover Clean, Deep Clean, Inspection or Maintenance.
5. Set priority (Low, Medium, High, Urgent), status and notes as needed.
6. Start the task, complete the work, record useful notes/media and mark it Done.
7. If inspection is required, the supervisor reviews the room and marks it Inspected/Ready using the authorized control.
8. Front Desk confirms the room is Ready in the shared room view before assignment.

Task deadlines are based on priority and property Housekeeping settings. If a task cannot be completed, leave a clear note and alert the supervisor instead of marking it complete.

### 11.3 Stayover cleaning

Review the occupied-room task list and guest instructions before entering. Complete only the requested service, update the task/status and record any maintenance issue or guest request as a separate task/ticket. Respect do-not-disturb and property entry procedures.

## 12. Laundry, Lost and Found, and the Phone App

### 12.1 Laundry

In **Housekeeping → Laundry**, locate the Requested order. Use the following sequence:

1. **Collect & count** the actual pieces/items, services and any express/house/complimentary details shown.
2. Record a shortage before sending the order onward.
3. Select **Send to laundry** when the items are handed over.
4. Select **Mark ready** when processing is complete.
5. Use **Return & deliver** to record returned quantities and shortage note, then complete delivery.
6. Use **Cancel** only for an order that is genuinely cancelled; a reason is required.
7. Use **Docket** to print an order ticket where needed.

Review rates and express pricing configured for the property. Check the resulting bill/folio according to the order type; do not assume every laundry order is chargeable.

### 12.2 Lost & Found

Open **Housekeeping → Lost & Found**. Search before creating a record. Enter item description, condition (Found/Missing/Damaged), room/location if known, logged date, logged-by person, guest if reliably known and notes. Update status to Returned with return date when handed back, or Disposed only under property policy. Do not record unnecessary identity or payment information in notes.

### 12.3 Phone App

Open **Housekeeping → Phone App** on the authorized mobile device. Sign in as yourself, check your assigned tasks and room details, then use the visible controls to start work and mark it Done. Supervisors may see additional assignment/status tools. Capture task/room media only where the screen offers it and property policy allows. Sign out after use on a shared device.

## 13. Restaurant and F&B Operations

### 13.1 Know your outlet and menu

An **outlet** is a restaurant, bar, room-service operation or other point of sale. Restaurant managers should verify the outlet is active and correct, table/staff assignments are current, printers route to the required stations, and menu items are available and priced correctly. Only authorized roles edit outlets, menu items, ingredients, recipes or printer setup.

Menu items can include category, price, photo, description, course, preparation station, allergens/dietary tags, vegetarian/alcohol flags and availability. Check allergens carefully. If an ingredient is out of stock, inform the manager and follow the site's process for changing menu availability.

### 13.2 Start a Restaurant POS order

1. Open **F&B → Restaurant POS** and select the correct outlet.
2. Select **Dine In**, **Room Service**, **Takeaway** or **Delivery**.
3. For Dine In, choose an available table. For Room Service, select an eligible in-house room; only current stays that allow room charges are offered. Takeaway/Delivery may need customer name, phone and delivery address.
4. Enter guest/customer details, party size and waiter/captain where requested.
5. Search/browse the menu and add items. Adjust quantity, course and item instructions. Include allergy information supplied by the guest.
6. Review the bill, outlet, table/room, order type and items before sending.

### 13.3 Send KOT, prepare and serve

1. Select the POS **Send/Fire KOT** action for items to be prepared.
2. The KOT appears on the Kitchen Display for the configured outlet/station. Depending on outlet KOT mode, it may auto-start or wait for kitchen staff to select **Start**.
3. Kitchen staff check destination, quantity, course, instructions and allergy warnings. Prepare the items and mark each live item done/ready.
4. For additional items or a later course, the waiter reopens the existing bill, adds the items and sends another round if supported.
5. The waiter checks the order state, collects ready items and serves the guest. The app records kitchen timing and ticket status; it does not confirm that physical service occurred.

### 13.4 Settle, charge to room and print

1. Open the correct running order and review items, quantities, discounts/adjustments and total.
2. Choose a supported tender in the settlement panel and complete any required cashier PIN/approval.
3. For eligible Room Service orders, select the guest's in-house room/folio charge option. Confirm the guest and room; the server rejects an ineligible room or disallowed charge.
4. Print the guest bill/receipt using the available print action. Kitchen tickets use the configured KOT route/printer.
5. Confirm the order is settled or posted and review the recent order/history list.

Restaurant payments post to the configured cashier session when applicable. Room charges appear on the guest folio and must be reconciled at hotel checkout. Do not take a second payment for a room-charged bill.

### 13.5 Kitchen Display and printers

Kitchen Display groups tickets by outlet, station and course and shows fired age, instructions and ticket status. Use station filters so the team sees its own work. If using a print station, open Kitchen Display on that device and choose the configured printer. Managers can inspect printer state, route KOTs by outlet/station, test output and review errors under **F&B → Printers**.

### 13.6 F&B Dashboard, reports and inventory

The **F&B Dashboard** is read-only. Choose an outlet and date/date range to review sales, bills, covers, average bill, open orders, tender, complimentary orders, voids, cancellations, top items and fire-to-ready time.

For stock:

1. Maintain the Ingredients list with one consistent unit of measure.
2. In **Menu → Recipes**, associate ingredient quantities with the dishes that consume stock.
3. Open **Kitchen Inventory**, select the outlet and review OK/LOW/OUT/NEGATIVE status.
4. Use **Receive** for supplier deliveries, **Stock take** for a physical count and **Wastage** for discarded stock.
5. Review movement history when a balance is unexpected.

Stock is per outlet, not a combined property total. A recipe-backed item reduces stock through the configured kitchen firing process; a dish without a recipe does not deduct ingredients. Stock warnings do not automatically disable menu items.

## 14. Banquets and Events

### 14.1 Enquiry and availability

1. Open **Banquets & Groups → Month Availability** or **Function Diary** and check the venue, date and session (Morning, Afternoon, Evening).
2. Select an open slot to start an enquiry with venue/date/session preselected, or select **Banquets → New enquiry**.
3. Enter customer/contact, company if applicable, event type/name, event dates, expected pax, requirements and follow-up date.
4. Save and verify the new function in **All Functions** or Banquets.

Availability colors distinguish Enquiry, Tentative, Confirmed and Completed. A tentative hold is not a confirmed event. Verify the function record before committing a venue.

### 14.2 Quote, confirm and deliver

1. Open the function detail and verify venue, date/session, customer, event type and requirements.
2. Select menus, dishes and services from **Menus & Services**. Enter quantities/guaranteed pax and applicable charges.
3. Review quote total, tax, cost/margin where shown, advance/payment milestones and balance due.
4. Use the function's available status action to move from Enquiry to Tentative or Confirmed. Follow any approval/reason prompt; status transitions are role- and state-dependent.
5. Share/print the quotation or event order using the available detail action.
6. Record advances/receipts on the function and confirm the balance updates.
7. Before the event, reconfirm guaranteed pax, schedule, venue setup, menu/service details, group block and outstanding payments.
8. After execution, close/complete the function through its supported action and review receipts and balance in **Registers**.

### 14.3 Registers and group stays

**Registers** provides Functions, Quotations, Enquiries, Cash book and Sales summary views for a selected period; use CSV or Print after checking dates. **Groups & Blocks** supports a hotel rooming list and room pickup associated with a function/group. Monitor the cutoff and release unpicked inventory using the supported group workflow.

## 15. Finance and Cashier Operations

### 15.1 Open a till

1. Open **Finance → My Till**.
2. Choose a terminal if offered, enter the actual **Opening float**, then select **Open session**.
3. Confirm the business date and open session details.

There is one open session per cashier per business date. If an open till already exists, select it; do not open a second shift to bypass reconciliation.

### 15.2 Payments and cash movement

Take guest payments from the reservation/folio screens, and restaurant payments in POS. These source records post to the open cashier session according to property settings. Use My Till for **Paid out** (amount and reason) and **Cash drop** (amount and destination if available). These actions record cash leaving the drawer; they are not guest refunds or supplier-bill payments.

**Petty Cash** records vouchers with payee, amount, category and reason against an open till; the form may request a PIN. Use **Currency Desk** only if the property accepts foreign currency: select currency and Buy/Sell direction, enter amount, calculate and review the local total/tax before posting.

### 15.3 Handover, count and close

1. Review My Till totals: float, tenders, paid-outs, drops, petty cash and expected cash.
2. Count the physical drawer and compare the counted amount with expected cash.
3. Close the session using the displayed count/close action.
4. Review **Finance → Sessions**, **All Tills** or **Shift report** for variance and collections by tender.
5. If there is a variance, recount and review source transactions, cash drops, paid-outs and transfers. Follow the manager approval process; never alter a count to make it match.
6. Record handover details under **Finance → Shift Handover**, including shift/date, cash figures, recipient, status and operational notes.

### 15.4 Folios, receivables and books

- **Billing/Folio History:** review open or closed guest/company bills and invoice details.
- **Receivables:** handle company/city-ledger invoices and collections; statements can be printed or emailed to the authorized billing contact.
- **Ledgers:** review Guest, Deposit, AR and Package balances and folio reconciliation.
- **Payables:** enter vendors and bills; Finance can enter/pay authorized bills, while only designated approvers approve them.
- **Cash outlook:** review expected money in/out over 5, 15 or 30 days; entered starting cash/bank amount improves the forecast.
- **Profit and loss / Balance sheet:** management views based on records in Quantumberg, not statutory accounts.
- **Accounting Export:** prepare approved data for external books and reconcile it before import.

Do not settle a supplier invoice from Petty Cash unless property policy explicitly directs a till-paid voucher; Payables and Petty Cash are separate workflows.

## 16. Revenue and Booking Engine Operations

These pages are normally maintained by Revenue Managers or authorized administrators; other staff use the resulting rates and booking content.

### 16.1 Rates and room types

- **Room Types** contain room category, capacity, base/occupancy pricing and tax details.
- **Rate Plans** are sellable plans with a code, modifier type/value, cancellation policy, default and disabled state.
- **Rate Calendar** shows date-based values for room types. Check effective prices after changes.
- **Seasons** apply date ranges, adjustment, priority, minimum nights and payment/cancellation restrictions.
- **Guardrails** define rate floors and ceilings.
- **Vouchers** are codes with discount type/value, validity, minimum nights and usage limits.
- **Long-stay Discounts** apply a percentage at a minimum stay length.
- **Meal Plans** define board basis and per-adult/child nightly prices.
- **Experiences** are add-ons that may appear on the public booking page.

Review overlapping seasons, priorities and guardrails before enabling a pricing change. Rates affect guest quotes and channel distribution.

### 16.2 Channel connection and OTA mapping

Authorized Revenue staff configure the **Channel Manager** connection using provider credentials and the external property ID. They then add **OTA Room Mappings** for each local room type/provider room and rate-plan identifier. Check the connection's last push/result and provider-side setup.

If a connected OTA booking does not appear, Front Desk should avoid making a duplicate. Revenue/IT checks the connection, provider webhook, mapping and channel log; after the booking arrives, Front Desk verifies its reservation record and handles it normally.

### 16.3 Booking Engine console and public page

The Booking Engine sidebar includes **Hotel Profile**, **Amenities**, **Photos**, **Policies**, **Payments**, **FAQ**, **SEO** and **Settings**. Authorized staff edit the selected property's public content and rules. Most text/setting edits remain pending until **Save Changes**; successful image uploads are persisted when the upload finishes. **Preview Page** opens the public booking page for review. **Engine Live** controls public booking availability when saved.

Before enabling/publishing:

1. Verify property name/contact/location, logo, hero/gallery images and amenities.
2. Check stay rules (minimum nights, cancellation, children/pets/extra beds, check-in/out, fees and deposits).
3. Confirm the payment mode/gateway is configured for the country/property.
4. Check room types, dates, rate plans, inventory and availability.
5. Review FAQ and SEO title/description/slug/social image.
6. Save, preview the public page and test a guest booking path safely before relying on it.

Do not create a live test booking or payment without the property's approval. A public page can be live while dates are unavailable because inventory, room types, restrictions or pricing do not match the search.

### 16.4 Revenue dashboard and Owner View

Use **Revenue → Revenue Dashboard** for property or portfolio summaries, and **Owner view** for compact revenue, occupancy, movement, money and audit information. Figures are role-gated. Follow links to source reports or records for investigation.

## 17. Night Audit and Business-Date Close

Night Audit is also called **End of Day**. It posts the configured room/tax activity and advances the property's business date. The scheduled job follows the same checks.

1. Open **Finance/Front Desk → Night Audit** and select the correct property.
2. Review business date, property-local time, scheduled audit status and pending blockers.
3. Use the wizard's steps to inspect arrivals/departures, due-outs, open cashiers, open restaurant bills, balances/rate exceptions and other configured checks.
4. Resolve the listed records from their proper pages. If the wizard offers **Acknowledge/Continue** for a warning or override, read it and provide the required reason. Blocking checks cannot be skipped without the permitted action.
5. Run the audit once when ready; wait for success before navigating away.
6. Review the run status and saved audit pack, including posted amounts and exceptions.
7. Verify the business date advanced before beginning next-day reconciliation.

If a run is in progress, reopen it to resume. If the audit closed but the date did not advance, use the specific recovery action shown by the page or contact an administrator. Do not rerun posting to fix a stuck date.

## 18. How Departments Work Together

### 18.1 Online booking → check-in

1. **Guest:** searches the public Booking Engine and submits a booking.
2. **Channel/Booking Engine:** creates a request/reservation with its source and payment state.
3. **Front Desk:** verifies and confirms the reservation, guest, dates, payment and room assignment.
4. **Housekeeping:** prepares/inspects the room and sets it Ready.
5. **Front Desk:** checks the guest in and confirms the stay appears in In-house and the room board.

### 18.2 Check-in → room service → folio → checkout

1. **Front Desk:** checks in the guest and verifies the room/folio.
2. **Waiter:** creates a Room Service POS order for the eligible room and sends the KOT.
3. **Kitchen:** prepares and marks the ticket ready; waiter serves the order.
4. **Waiter/Cashier:** posts the bill to the permitted guest folio (or takes another allowed tender).
5. **Front Desk/Finance:** reviews the charge during checkout, reconciles and settles the folio.

### 18.3 Guest request → resolution

1. **Front Desk/Guest Relations:** creates or reviews the guest's Service Ticket with room, category and priority.
2. **Supervisor:** assigns it to an eligible team member.
3. **Assigned department:** starts work, records progress notes and completes the request.
4. **Ticket owner:** marks it solved with a resolution note; reopen with a reason if the issue returns.
5. **Manager:** reviews overdue/SLA reports and escalates recurring problems.

### 18.4 Checkout → room-ready → next guest

1. **Front Desk:** completes checkout and confirms the folio/room status.
2. **Housekeeping:** accepts checkout-clean task, services the room and records completion.
3. **Supervisor:** inspects and marks Inspected/Ready if required by property settings.
4. **Front Desk:** assigns the room to the next eligible arrival only after verifying Ready.

### 18.5 Restaurant order → KOT → settlement

1. **Waiter:** selects outlet/order type/table or room, adds items and fires KOT.
2. **Kitchen:** sees the ticket by outlet/station, starts preparation and marks items ready.
3. **Waiter:** serves items and adds a supported follow-on course/order round if requested.
4. **Cashier:** settles the order or uses eligible room charge; the POS/cashier/folio records update.
5. **Manager:** reviews dashboard, open bills, voids and stock movement.

### 18.6 Banquet enquiry → event → payment

1. **Banquet Sales:** checks Month Availability/Function Diary and creates an enquiry.
2. **Sales:** builds the quote using configured venue, menu and service catalogue; records follow-up.
3. **Authorized approver/sales role:** places tentative hold or confirms using the available status action.
4. **Finance:** records advances/receipts and monitors balance.
5. **Event team:** confirms guaranteed pax and requirements, executes the function and updates completion.
6. **Manager:** reviews Registers and financial status.

### 18.7 Cashier shift → audit → new business date

1. **Cashier:** opens a till, handles payments on source screens and records cash movement.
2. **Cashier:** counts and closes the till; investigates variance with Finance/manager.
3. **Night Auditor:** checks that tills and POS bills are closed and resolves End of Day blockers.
4. **Night Auditor:** runs the audit and reviews the audit pack.
5. **Next shift:** confirms the new business date before starting daily work.

### 18.8 OTA booking → reservation → arrival

1. **Revenue/IT:** keeps the channel connection active and local/provider room mappings correct.
2. **Channel Manager:** receives the provider booking and maps it to a PMS room type/reservation.
3. **Front Desk:** verifies source, dates, guest, payment and imported details; avoids duplicate creation.
4. **Housekeeping/Front Desk:** prepare the assigned room and complete check-in.

## 19. Role-Based Daily Checklists

These checklists are practical operating guidance. Follow the property's approved shift procedures when they differ.

### Front Desk staff

- **Opening:** Confirm property/business date; review Today, arrivals/departures, room readiness, open tickets and till status.
- **During shift:** Verify guest/reservation before check-in; record accurate room assignment; route guest requests; use folio/POS charge workflows; update stay changes.
- **End of shift:** Reconcile assigned till; review pending arrivals, departures, guest requests and handover notes; sign out on shared devices.

### Reservation staff

- **Opening:** Review Requested/Held/Pending Payment/Waitlist records and channel exceptions.
- **During shift:** Search guest history first; verify dates, occupancy, rate, source, deposit and cancellation terms; confirm using allowed actions.
- **End of shift:** Recheck incomplete booking requests, deposits and guest communications; hand unresolved exceptions to the next shift.

### Housekeeping attendants

- **Opening:** Open Phone App or Tasks; review assigned rooms, priority and due-outs.
- **During shift:** Follow room-entry policy; complete assigned cleaning; record actual status/notes; report maintenance or guest issues.
- **End of shift:** Mark only completed work Done; hand blocked/unfinished rooms to supervisor; sign out of shared devices.

### Housekeeping supervisors

- **Opening:** Review Room Board, due-outs, task backlog and urgent/overdue work; assign eligible staff.
- **During shift:** Inspect completed checkout cleans when required; set Inspected/Ready only after inspection; block rooms requiring maintenance.
- **End of shift:** Confirm ready-room state with Front Desk; reassign unfinished work and review laundry/lost-property exceptions.

### Waiters and restaurant cashiers

- **Opening:** Confirm outlet, table map, menu availability and open cashier session; know which orders can be room charged.
- **During shift:** Enter correct order type/table/room and guest count; include instructions/allergy details; send KOT; verify kitchen status; settle once and print when needed.
- **End of shift:** Review open bills, recent orders and tender totals; close/reconcile till and pass unresolved orders to the next shift.

### Kitchen staff

- **Opening:** Open Kitchen Display for assigned outlet/stations and confirm print-station selection if used.
- **During shift:** Review destination, item, course, notes and allergens; start tickets; prepare and mark completed items ready; report unavailable ingredients.
- **End of shift:** Clear completed/held tickets according to service policy and notify the manager of printer, stock or unresolved order issues.

### Restaurant managers

- **Opening:** Verify active outlets, prices/availability, staff/printer routes and ingredient warnings.
- **During shift:** Monitor open bills, KOT timing, voids/complimentary orders, service problems and per-outlet stock.
- **End of shift:** Review F&B Dashboard and exceptions; check till/session reconciliation; record counts, receipts and wastage accurately.

### Banquet staff

- **Opening:** Review Banquets reminders, Function Diary, today's venue/session, guaranteed pax, requirements and balances.
- **During shift:** Record follow-ups; keep quotation, menu/services and function status current; inform Finance of receipts and the event team of changes.
- **End of shift:** Update outcome/follow-up date, outstanding actions and next owner; check cutoff/pickup for group blocks.

### Finance and cashier staff

- **Opening:** Confirm property/business date, terminal, float and expected open session.
- **During shift:** Take payments through the correct source screen; record paid-outs/drops/vouchers with reason; protect PIN and receipt data.
- **End of shift:** Count cash, close session, investigate variance, reconcile receivables/payables as assigned and record handover.

### Revenue managers

- **Opening:** Review Revenue Dashboard, pickup/pace reports, future availability and channel push status.
- **During shift:** Validate rate changes against season overlaps, plan rules and guardrails; maintain channel mappings and Booking Engine content.
- **End of shift:** Confirm saved rate/content changes, inspect preview where relevant and hand off channel/availability exceptions.

### Hotel managers

- **Opening:** Review Today/Owner View, occupancy, arrivals, departures, open tasks/tickets and financial exceptions.
- **During shift:** Coordinate Front Desk, Housekeeping, F&B, Events and Finance on blocked rooms, service escalation and payment issues.
- **End of day:** Verify till reconciliation and audit readiness; review Night Audit exceptions and confirm the business date rolls successfully.

## 20. Troubleshooting and Common Mistakes

| Problem                                     | Safe checks and next step                                                                                                                                                           |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cannot see an app, page or button           | Check selected property, role, enabled module and the status of the record. Ask an administrator to review access.                                                                  |
| Room is not available for assignment        | Check existing stay, room type/capacity, active room block, out-of-order state and housekeeping readiness. Ask Front Desk/Supervisor to reconcile the room board.                   |
| Room is still Dirty after checkout          | Checkout does not mean cleaning is complete. Check the checkout-clean task, assignment, completion and required inspection.                                                         |
| Reservation cannot be confirmed             | Review current status, dates/availability, required guest/contact fields, source, deposit/payment and any validation message. Escalate channel errors to Revenue/IT.                |
| Guest or room cannot be found               | Confirm property and search by the correct name/reference/phone; review filters and dates before creating a duplicate record.                                                       |
| Payment is not reflected in the folio       | Check the payment action result, reservation/folio, till session and payment status. Do not take a second payment until Finance verifies the first.                                 |
| POS order is not visible in Kitchen Display | Verify outlet, KOT was fired/sent, station filter, outlet KOT mode, network/realtime status and open order details.                                                                 |
| KOT is not printing                         | Check printer route (outlet/station), printer enabled/error state, direct IP settings or print-station device selection; send a test print and contact the manager.                 |
| Room-service charge is rejected             | Confirm guest is currently checked in, selected room is correct, room charges are permitted and folio/charge limit policy allows it.                                                |
| Till cannot be closed                       | Review open session, required count fields, pending tender/transfer actions and PIN prompts. Ask Finance/manager about a genuine discrepancy; do not change figures to force close. |
| Cash variance appears                       | Recount, compare expected cash, drops, paid-outs, petty-cash vouchers and tender receipts; document the variance and request approval.                                              |
| Booking page shows no rooms                 | Check Engine Live, room types, rates, selected date/guest count, minimum nights, room blocks and inventory. Revenue/administrator checks settings and public preview.               |
| OTA reservation is missing                  | Do not create a duplicate first. Ask Revenue/IT to check connection status, provider webhook, mapping IDs and last-push/error; then verify the reservation list/property.           |
| Ticket is overdue or unassigned             | Open Operations → Tickets, check Open/Unassigned/Overdue view, priority, assignee and due time; assign to eligible staff and notify the supervisor.                                 |
| WhatsApp reply is rejected                  | Check active property number, provider status and whether the 24-hour guest session is open. Outside the window, use an approved template if configured.                            |
| Night Audit is blocked                      | Resolve the source records listed by the wizard (open tills/POS bills, due-out stays or configured exceptions) and retry only when the checklist is ready.                          |

Never bypass permissions or manually alter database records. Capture the page, record reference, property, business date and exact error for the authorized supervisor/administrator or support contact.

## 21. Glossary

| Term                     | Plain-language meaning                                                                                    |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| Reservation              | A booking record for a guest's planned stay.                                                              |
| Guest profile            | Contact and stay-history record for a person.                                                             |
| Check-in                 | Starts the guest's in-house stay and assigns the room through the permitted workflow.                     |
| Check-out                | Ends the stay and leads to folio closure and room turnover.                                               |
| Folio                    | The guest/company bill containing charges, payments and balance.                                          |
| KOT                      | Kitchen Order Ticket sent from POS to kitchen staff.                                                      |
| Outlet                   | Restaurant, bar, room-service point or other POS operation.                                               |
| Room block               | Hold on inventory; a group allocation differs from a physical room maintenance block.                     |
| Rate plan                | A sellable pricing option and its modifier/cancellation terms.                                            |
| Season                   | Date range with pricing or booking restrictions.                                                          |
| ADR                      | Average Daily Rate, a room-revenue-per-sold-room measure.                                                 |
| RevPAR                   | Revenue per Available Room, a room-revenue/available-inventory measure.                                   |
| Night Audit / End of Day | Process that checks the operating day, posts configured room/tax activity and advances the business date. |
| Business date            | Hotel operating date used for cashiering and daily close.                                                 |
| Till session             | Cashier's open shift on a terminal for a business date.                                                   |
| Opening float            | Starting cash placed in a till at the beginning of a session.                                             |
| Cash drop                | Recorded cash removed from the drawer to a safe/cash office.                                              |
| Paid out                 | Recorded cash paid from a till with a reason.                                                             |
| Tentative hold           | Provisional event status; not a confirmed function.                                                       |
| Confirmed function       | Event record accepted for delivery, subject to its recorded details and payments.                         |
| Pickup                   | Reservations/rooms assigned against a group room block.                                                   |
| SLA                      | Target response/resolution timing used for guest-request tickets.                                         |

## 22. Source Verification and Runtime Variations

This guide is based on the Administrator Guide and the Front Desk, Housekeeping, Operations, Booking Engine, F&B/POS, Banquets, Revenue and Finance guides, plus the current frontend routes/screens and backend permission/workflow implementations. It describes user-facing actions and avoids database or developer procedures.

Live behavior varies by property, role, enabled module, country pack, payment/channel provider, printer hardware, configured settings and actual records. Follow the labels and validations shown in your installed application. If a feature mentioned here is hidden or unavailable, confirm access and property configuration with your supervisor/administrator rather than assuming it is enabled.
