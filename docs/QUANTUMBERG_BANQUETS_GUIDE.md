<p align="center">
  <img src="../frontend/public/quantumberg-logo.png" alt="Quantumberg Technologies" />
</p>

<h1 align="center">Quantumberg PMS Banquets and Groups Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Front Desk, Revenue Managers, Banquet Sales, Hotel Administrators

---

## Table of Contents

1. Introduction
2. Access, Property Scope and Roles
3. Banquets & Groups Sidebar
4. Banquets Sales Workspace
5. Month Availability
6. Function Diary
7. Registers
8. Menus & Services
9. All Functions and Function Detail
10. Groups & Blocks
11. Halls & Venues
12. Banquets & Groups Settings
13. End-to-End Workflows
14. Permissions and Security
15. Troubleshooting and FAQs
16. Glossary
17. Source Verification and Runtime Variations

---

## 1. Introduction

Banquets & Groups supports venue enquiries, availability review, quotations, function planning, service/menu catalogues, payments and group room blocks. The function workflow is centered on a **Venue Booking** record and its detail workspace.

## 2. Access, Property Scope and Roles

Open **Banquets & Groups** from the app switcher. Its app-level roles are **Front Desk**, **Revenue Manager**, **Hotel Admin**, **System Manager** and **Administrator**, and the module must be enabled for the selected property. Function and venue data are property-scoped. Keep the header's selected property correct before creating or editing records.

Role access can differ by action: the catalogue editor also permits **Finance** users when the endpoint grants access, while module settings are restricted to **Revenue Manager**, **Hotel Admin**, **System Manager** and **Administrator**. Backend permissions determine the final result.

## 3. Banquets & Groups Sidebar

| Page | Purpose |
|---|---|
| Banquets | Sales overview with reminders, pipeline and searchable function list; create new enquiries. |
| Month Availability | Month grid of venues by morning, afternoon and evening session. |
| Function Diary | Rolling 14-day hall calendar with search, status filter and date check. |
| Registers | Functions, quotations, enquiries, cash book/receipts and sales summaries for a selected period. |
| Menus & Services | Maintain banquet menus, dishes and event services used in quotations and event orders. |
| All Functions | Search, filter and open Venue Booking records. |
| Groups & Blocks | Manage group reservations, room block dates, cutoff and pickup control. |
| Halls & Venues | Configure event spaces, capacities, rental rates and setup information. |
| Settings | Quotation margins, default payment milestones and enquiry follow-up timing. |

## 4. Banquets Sales Workspace

The Banquets home page offers **Needs chasing**, **Month by month** and **All functions** views. The sales summary includes confirmed value, pipeline value (enquiries and tentative holds), confirmed outstanding balance and conversion rate. Date range fields can scope the pipeline; text search and status filter narrow the function list.

Use **New enquiry** to begin a prospect record. The **Diary** button opens the rolling function calendar. Clicking an open availability slot from the month grid or diary can start an enquiry with venue/date/session preselected.

Reminder rows identify follow-ups and high-urgency alerts. Record a follow-up date and sales owner on the function, then return to the reminder view to work the queue.

## 5. Month Availability

The month grid displays each venue across calendar dates, with one row per **Morning**, **Afternoon** and **Evening** session. The color key differentiates **Enquiry**, **Tentative**, **Confirmed** and **Completed**; tentative holds are visually provisional rather than confirmed inventory.

- Use previous/next month and **This month** to navigate.
- Weekend evening availability is highlighted as a quick prospecting cue.
- Select an open cell to create an enquiry for the selected venue, date and session.
- Existing function cells link to their function record.

This screen is an availability aid, not a substitute for checking the function detail and venue/session when changing an event. Verify multi-day dates and existing holds before confirming a quote.

## 6. Function Diary

The diary shows a rolling 14-day period with halls down the side and dates across the top. Multi-day functions display on each date they cover. Search by customer/company/reference and filter by function status.

- Use **Earlier**, **Today** and **Later** to shift the displayed period.
- Use **Check a date** for the date-specific availability inquiry.
- Click an event to open its function; click an open day slot to start an enquiry.
- Scroll horizontally where the full period does not fit the screen.

## 7. Registers

Select **From** and **To** dates, then choose a register tab:

| Register | Contents |
|---|---|
| Functions | Functions booked in the period. |
| Quotations | Quotes issued and whether they converted. |
| Enquiries | Incoming enquiries and their outcomes. |
| Cash book | Payments by payment mode. |
| Sales summary | Revenue grouped by hall, event type and session. |

Review the row totals and period before selecting **CSV** or **Print**. CSV exports the displayed register columns; the print action uses the browser print dialog. Empty periods display an empty state rather than a fabricated total.

## 8. Menus & Services

The catalogue has **Menus**, **Services** and **Dishes** tabs, search and an add action for the selected tab.

- **Menus:** menu name, meal period, cuisine, food type, service style, per-person rate, GST and course list.
- **Dishes:** dish name, course type, food type, kitchen, portion per person and recipe lines. Recipe ingredients are drawn from the F&B ingredient list where available.
- **Services:** service name/category, unit of measure, rate, GST, chargeable default, pack-list setting and alcohol flag.

Services include non-food event requirements (for example audio-visual equipment or decor). A service marked non-chargeable can still appear on the event order/pack list; the function can override the default where the detail workflow exposes the option.

Choose **New menu**, **New dish** or **New service** to open the corresponding editor. Search narrows the current list. Save through the form action and confirm that the refreshed catalogue contains the change. Catalogue edits are available to the roles authorized by the page/backend; a read-only user can still inspect allowed records.

## 9. All Functions and Function Detail

All Functions is a searchable Venue Booking list, filterable by event date, status and event type. Rows show reference, customer, hall, event type/date, guaranteed attendance, status, quote total and amount due. Open a row to enter its dedicated function workspace; financial and menu details belong there rather than the quick-edit form.

### 9.1 Function record fields

The record captures venue, event type/name, start and optional end date, customer name/phone/email, linked company, expected and guaranteed attendees, status, next follow-up, and requirements. Quote total, advance received and balance due are calculated/read-only summary values on the list form.

Function status values in the implementation include **Enquiry**, **Tentative**, **Confirmed**, **Completed**, **Cancelled** and **Lost**. The detail screen offers status-specific actions; permitted transitions and reopen controls are role-gated. Use the action presented by the screen instead of editing status to bypass a required confirmation.

### 9.2 Function detail workspace

The function sheet is the working record for sales follow-up, quotation, customer/company, dates, venue, attendance, menus/services, event requirements, payment milestones and balance. It also provides related-document links and print actions where configured. Keep the customer-facing quotation and operational event order consistent with the final venue, date/session, guaranteed pax, service quantities and taxes.

The **WhatsApp guest** action is available on the detail page when channel configuration and permissions support it. Messaging delivery depends on the property's connected provider and approved template/window rules.

## 10. Groups & Blocks

Choose **New group booking** to open the dedicated creation dialog; this page deliberately does not use generic create. Required information includes group name and arrival/departure dates, with optional company, cutoff date and notes. The list shows status (**Open**, **Confirmed** or **Cancelled**) and can be filtered by status/arrival or searched by group/company.

Open a group to view its Group Rooms Control detail, including associated block/pickup and rooming-list workflows. Use the cutoff date to manage when unpicked allocation should be reviewed/released. Verify linked reservations and the property's availability before changing allocation. Group blocks are not the same as a room-block record used for maintenance/house use.

## 11. Halls & Venues

Create a Venue record before selling a function in that space. The list can be searched by venue name/code and filtered by type. The form includes:

- Venue name and code (the code prints on the event order).
- Type: Banquet Hall, Lawn, Poolside, Rooftop, Board Room, Conference Hall, Restaurant or Other.
- Maximum and minimum worthwhile capacity, area, day rental, hourly rental, minimum hours and rental GST.
- Supported setup styles and amenities.
- Disabled flag.

Review capacity and pricing before publishing availability or preparing quotations. A disabled venue should not be used for a new function.

## 12. Banquets & Groups Settings

Hotel Admin and Revenue Manager can edit these settings:

| Section | Fields | Effect |
|---|---|---|
| Quotation margins | Target margin; floor margin | Establishes the expected and minimum quote margin; quotes below the floor are flagged for review. |
| Default payment milestones | Advance at confirmation; interim payment; interim due | Defaults for newly created functions; each function can be adjusted as permitted. |
| Sales follow-up | Follow up an enquiry after | Sets the default follow-up interval for new enquiries. |

Set defaults according to property policy, then review each function's actual quote, margin and payment schedule before sending the customer-facing quotation.

## 13. End-to-End Workflows

### Enquiry to completed function

1. Check Month Availability or the Function Diary for the venue/date/session.
2. Create a new enquiry and enter customer, contact, company, event type, expected pax, requirements and follow-up date.
3. Confirm availability and quote using the venue rental, menu and service catalogue. Check the target/floor margin.
4. Record the customer's decision through the function status action. Set the guaranteed pax and payment milestones when confirming.
5. Record advances/interim payments using the function's payment workflow; monitor outstanding balance.
6. Print/share the approved quotation or operational event order from the function detail.
7. On the event date, reconcile delivered menus/services and attendance; mark the function completed only after the event workflow is finished.
8. Use Registers to reconcile quotations, enquiries, receipts and sales for the period.

### Create a group and monitor pickup

1. Create the group with company and stay dates.
2. Set/confirm the cutoff and room block allocation in the group detail.
3. Add or associate the rooming list/reservations using the controls provided by the group record.
4. Review pickup and availability before cutoff; release unused rooms through the supported block action.
5. Confirm the resulting room inventory in the Front Desk Tape Chart.

## 14. Permissions and Security

- The module is shown only when the user's role and property's enabled modules allow it.
- Function screens are property-scoped. Do not change the selected property while editing a function or payment.
- Catalogue writing is restricted by role, and settings are limited to Revenue Manager, Hotel Admin, System Manager or Administrator.
- Financial approvals and payment operations may have stricter server checks than page visibility.
- Share quotations, customer details and company statements only with authorized recipients. Do not place payment credentials in event requirements or notes.

## 15. Troubleshooting and FAQs

| Problem | Checks |
|---|---|
| Venue does not appear in availability | Verify the property, venue record, disabled flag, date/session and that the venue has been configured. |
| Open diary cell does not start the expected enquiry | Confirm the venue/date query parameters and that the user can create a function; reload and check for a conflicting booking. |
| Function missing from a register | Check the selected From/To dates, property and whether the record falls in that register's data category. |
| Quote total or balance is unexpected | Recheck venue rental, menu/service quantities, GST, guaranteed pax, payment entries and function date. |
| Cannot edit catalogue/settings | Ask an administrator to verify role assignment, property scope and enabled module. |
| Group pickup is incomplete | Open Group Rooms Control and inspect cutoff, allocated block and linked reservations; verify availability before releasing inventory. |
| WhatsApp action fails | Confirm channel provider connection, active number, approved template/session requirements and recipient details. |

## 16. Glossary

- **Function:** A venue event represented by a Venue Booking record.
- **Session:** Morning, afternoon or evening venue availability slot.
- **Pax:** Attendee count; guaranteed pax is the agreed billing/operational count.
- **Pipeline:** Enquiries and tentative holds still being pursued.
- **Room block:** Group room allocation with pickup and cutoff.
- **Register:** Period-based list or summary for banquet activity.

## 17. Source Verification and Runtime Variations

This guide follows the app registry, Banquets/Diary/Month/Registers/Catalogue/Function screens, shared resource configuration, backend API and the live application. Venue records, property settings, tax, availability, payment status, integrations and permissions vary by site. The values shown in an installed instance are operational records, not sample defaults to copy blindly.
