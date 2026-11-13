<p align="center">
  <img src="../images/quantumberg-logo.png" alt="Quantumberg Technologies" style="width: 200px; max-width: 100%; height: auto;" />
</p>

<h1 align="center">Quantumberg PMS Housekeeping Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Housekeeping Attendants, Supervisors, Front Desk, Hotel Administrators

---

## Table of Contents

1. Introduction
2. Access, Property Scope and Roles
3. Housekeeping Sidebar Navigation
4. Room Board
5. Rooms and Room Insights
6. Tasks
7. Laundry
8. Lost & Found
9. Reports
10. Phone App
11. Housekeeping Settings
12. End-to-End Workflows
13. Permissions and Security
14. Troubleshooting and FAQs
15. Glossary
16. Source Verification and Runtime Variations

---

## 1. Introduction

Housekeeping supports room turnover, task assignment, inspections, laundry orders, lost-property tracking and a mobile task workflow. Accurate room status is shared with Front Desk and reservation availability; update it only after the work has actually been completed.

## 2. Access, Property Scope and Roles

Housekeeping is available to **Housekeeping**, **Housekeeping Supervisor**, **Front Desk**, **Hotel Admin**, **System Manager** and **Administrator** roles when the module is enabled. Room Board, Rooms and Settings have narrower role checks than Tasks or the phone app. The selected property controls room/task data.

Attendants may mark a room **Dirty** or **Clean** on the supervisor board. Supervisors and authorized desk/admin users may set the broader states, assign tasks and carry out inspection/ready/out-of-order actions. The server validates property and role permissions.

## 3. Housekeeping Sidebar Navigation

| Page | Purpose |
|---|---|
| Room Board | Property room overview, floor/status filters, task assignment and permitted status changes. |
| Rooms | Shared room board and Insights view with stay history/status drawer. |
| Tasks | Search, create and manage housekeeping tasks and inspections. |
| Laundry | Track guest/house laundry from request and count through delivery. |
| Lost & Found | Log found/missing/damaged items and return/disposal status. |
| Reports | Shared reports, department packs and task/laundry summaries where allowed. |
| Phone App | Mobile-oriented task and room workflow at the `/hk` route. |
| Settings | Task deadlines, room turnover inspection and laundry express multiplier. |

## 4. Room Board

Room Board displays rooms with room number/type/floor, housekeeping status, occupancy, guest and current task/assignee. It refreshes periodically and includes manual **Refresh**.

- Filter by floor and by **All**, room status, **Due out** or **Has task**; count badges show matching rooms.
- Select a room to expose status and assignment actions.
- Attendants can select **Dirty** or **Clean**.
- Supervisors can set supported statuses **Dirty**, **Clean**, **Inspected**, **Ready** and **Out of Order**, and assign a task to a housekeeper.
- A ready status may be shown only when the property uses the inspection/turnover flow.

Rooms due out, same-day/hourly stays and open tasks are shown as operational context. Do not mark a due-out room ready before checkout and cleaning have been completed.

## 5. Rooms and Room Insights

Rooms is shared with Front Desk and has **Board** and **Insights** tabs. The board supports room/guest search, floor and room-type filters and status groups: ready to sell, dirty, occupied, arriving, departing, out of service and open task.

Opening a room drawer shows room information, current/previous stay, guest, room status, cleaning/task history and permitted actions. A supervisor/desk user may hand off to check-in/out, room change or housekeeping status dialogs according to their role. **Insights** summarizes room sales, revenue, cleaning and operational data; financial details can be role-gated.

## 6. Tasks

Tasks lists property Housekeeping Task records and can search by room and filter status (**Pending**, **In Progress**, **Done**, **Verified**). Task fields include:

- Required room (property-scoped), task type and priority.
- Task type: **Checkout Clean**, **Stayover Clean**, **Deep Clean**, **Inspection** or **Maintenance**.
- Priority: **Low**, **Medium**, **High** or **Urgent**.
- Status and notes.
- Associated room/task media panel where available.

Completing a task updates the room's live housekeeping status through the supported workflow. Use **Verified** only after the required inspection. Tasks may be created from operational actions as well as the list; avoid duplicate tasks by checking the room's open work first.

## 7. Laundry

Laundry is the guest-laundry board. It separates requested orders from orders already collected/in hand and shows recent delivered/cancelled history. Order cards include room/guest or house label, express/complimentary flags, pieces, amount, ready-by time, notes and shortage/overdue indicators.

Supported progression:

1. **Requested → Collect & count:** enter actual quantities for each laundry item and applicable service/express/guest-or-house details.
2. **Collected → Send to laundry:** hand off the counted order for processing.
3. **In Process → Mark ready.**
4. **Ready → Return & deliver:** record returned quantities and any shortage note, then complete delivery.
5. **Cancel:** requires a reason. Use only for an order that is genuinely cancelled.

**Docket** prints the laundry order ticket. Rates are configured through the housekeeping laundry rate/settings workflow; the order's total is shown where chargeable. A house order has no guest room, and complimentary guest orders are identified separately.

## 8. Lost & Found

Lost & Found is a property-scoped list searchable by item description or logged-by person. Filter by condition (**Found**, **Missing**, **Damaged**) and status (**In Storage**, **Returned**, **Disposed**). Record fields include item description, room found in, date logged, logged by, guest if known, status, return date and notes.

Record a factual description and location. Set **Returned** and the return date when the item is handed back; use **Disposed** only according to property policy. The record is not a guest-message or shipping workflow.

## 9. Reports

Reports are shown according to enabled modules and role. Housekeeping may access the department pack, custom report builder and task report links where backend grants permit. Report datasets are server-filtered. Choose the permitted date range and columns, preview and export/share only if authorized.

## 10. Phone App

The Phone App opens the mobile-focused `/hk` screen. Housekeepers can view their assigned tasks and room information and update supported task state (for example **In Progress** and **Done**). Supervisor roles may have additional assignment and room-status controls. Photo capture/room media is available where exposed by the device and the task flow.

The phone route uses the same property and user authorization rules as the desktop workflow. It does not create a separate housekeeping database or bypass task permissions. Keep the device logged in only for its assigned user and sign out at the end of use.

## 11. Housekeeping Settings

Hotel Admin and Housekeeping Supervisor can edit:

| Section | Fields | Effect |
|---|---|---|
| Task deadlines | Urgent, High, Medium and Low minutes | Defines when a housekeeping task is considered overdue/escalated. |
| Room turnover | Inspect after every checkout clean; inspection duration | Adds an inspection step and sets its due time. |
| Laundry | Express price multiplier | Used when a laundry item has no express-specific price. |

Room statuses, task records, laundry rate cards and room assignment are maintained in their respective screens, not as additional fields in these settings.

## 12. End-to-End Workflows

### Turn over a departing room

1. Review the Room Board for due-out rooms and confirm the guest has checked out in Front Desk.
2. Open or create the Checkout Clean task; assign it if you are a supervisor.
3. Start the task and service the room. Record notes/media if the task requires evidence.
4. Mark the task done and set room status to Clean.
5. If inspection is enabled, the supervisor inspects and marks **Inspected/Ready** through the supported action.
6. Confirm the room is shown as ready to sell in the shared Rooms/Tape Chart view.

### Complete laundry

1. Open Laundry and select the requested order.
2. Collect items and count actual quantities; note shortages before sending.
3. Send to laundry, update processing status, then mark ready.
4. Record return quantities and shortage note, complete delivery and print a docket if required.
5. Verify any billable total on the guest record/folio according to property policy.

### Log and return lost property

1. Search existing records to avoid a duplicate.
2. Create an entry with condition, item description, room/location, date and logged-by details.
3. Link a guest only when reasonably identified and record notes without unnecessary sensitive data.
4. Update the status and return date when handed back, or mark disposed according to policy.

## 13. Permissions and Security

- The Housekeeping app is role- and property-gated; the Room Board and room status actions are separately restricted.
- Supervisors should assign work only to eligible property staff. Attendants should update only assigned/authorized task records.
- Never mark a room ready if it has not passed the configured cleaning/inspection steps.
- Guest names, room numbers, laundry details and found-property data are sensitive; do not export or share them outside approved channels.
- Confirm identity before returning a found item, and follow the property's retention/disposal policy.

## 14. Troubleshooting and FAQs

| Problem | Checks |
|---|---|
| A room is missing from the board | Check selected property, room record, floor/type filters and user property permissions. |
| Status action is unavailable | Attendants only receive Clean/Dirty controls; ask a supervisor for inspection, Ready or Out of Order action. |
| Room remains not ready after task completion | Check task status, inspection requirement and supervisor verification; completion and readiness are separate steps when inspection is enabled. |
| Task is overdue | Review priority and configured deadline; update assignment/status and contact a supervisor if work is blocked. |
| Laundry count or bill is wrong | Reopen order details, check collected/returned quantities, service rates, express rate and shortage note. |
| Phone App shows no assigned work | Verify login, selected property, task assignment and network access; refresh the phone view. |
| Lost item cannot be found | Search description/date/status and verify property; check whether it has already been returned or disposed. |

## 15. Glossary

- **Checkout Clean:** Room turnover task after a guest departure.
- **Stayover Clean:** Room service during an active stay.
- **Inspection:** Supervisor check after cleaning where enabled.
- **Ready:** Room can be sold after required housekeeping/inspection rules.
- **Express laundry:** Laundry service with an express price or configured multiplier.
- **Room Board:** Shared view of room status, occupancy and housekeeping work.

## 16. Source Verification and Runtime Variations

This guide follows the Housekeeping app registry, Room Board, shared Rooms drawer/insights, task resource configuration, Laundry, Lost & Found and phone-app screens, settings schema, backend endpoints and the live application. Task deadlines, staff assignments, device capabilities, laundry rates, inspection policy and permissions vary by property. Actual rooms, guests and tasks are operational data and should not be copied as defaults.
