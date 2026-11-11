<p align="center">
  <img src="../frontend/public/quantumberg-logo.png" alt="Quantumberg Technologies" />
</p>

<h1 align="center">Quantumberg PMS F&B and POS Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Front Desk, Finance, F&B Managers, Hotel Administrators

---

## Table of Contents

1. Introduction
2. Access, Property Scope and Roles
3. F&B Sidebar Navigation
4. Restaurant POS
5. F&B Dashboard
6. Kitchen Display
7. Menu, Bulk Upload and Recipes
8. Ingredients
9. Kitchen Inventory
10. Outlets and Waiters
11. Printers and KOT Routing
12. F&B Settings
13. End-to-End Workflows
14. Permissions and Security
15. Troubleshooting and FAQs
16. Glossary
17. Source Verification and Runtime Variations

---

## 1. Introduction

The F&B module covers restaurant and bar orders, room service, kitchen tickets, menu setup and outlet-level ingredient stock. The screens documented here are the features present in the current frontend and backend.

## 2. Access, Property Scope and Roles

Open **F&B** from the app switcher. The app is available to users with **Front Desk**, **Finance**, **F&B Manager**, **Hotel Admin**, **System Manager** or **Administrator** roles, provided F&B is enabled for the selected property.

Most F&B records are property-scoped. The property selected in the application header controls which outlets, menu items, orders and stock are shown. A screen being visible does not necessarily grant permission to edit its records; server-side role and document permissions still apply.

## 3. F&B Sidebar Navigation

| Page | Purpose |
|---|---|
| Restaurant POS | Open, update, send and settle restaurant, bar, room-service, takeaway and delivery orders. |
| F&B Dashboard | Review outlet sales, covers, open bills, exceptions, popular items and kitchen timing. |
| Kitchen Display | Accept and prepare kitchen tickets by outlet, station and course. |
| Menu | Maintain sellable dishes and drinks; includes bulk upload and the recipe editor. |
| Ingredients | Maintain ingredient names, units, categories and indicative costs. |
| Kitchen Inventory | Receive stock, count it, record wastage and review stock movements. |
| Outlets | Configure restaurants, bars and other points of sale, including tax and KOT mode. |
| Printers | Configure receipt/KOT printers and route output to outlet/station combinations. |
| Reports | Open reports permitted by the user's role and enabled modules. |
| Settings | F&B settings and menu master lists; restricted to authorized roles. |

## 4. Restaurant POS

The POS screen is an operational order workspace. Select an outlet before entering an order. The screen presents menu categories and item search alongside the current bill, table board, open orders and recent order history.

### 4.1 Start an order

1. Select the outlet.
2. Choose an order type: **Dine In**, **Room Service**, **Takeaway** or **Delivery**.
3. For dine-in, choose a table. Table tiles indicate states such as vacant, running, fired, ready, reserved or cleaning. Search/filter tools help narrow tables by area and occupancy.
4. For room service or a room charge, select an eligible in-house room. Only checked-in guests in rooms allowed to take room charges are offered.
5. Search or filter the menu and add items. Adjust quantities and enter item instructions where needed. Guest allergy notes travel with the order and are checked against menu allergen tags on the Kitchen Display.
6. Add customer/guest details, party size or waiter where the order requires them.

### 4.2 Send and manage items

- **Send / Fire KOT** sends the selected items to the kitchen. An existing order can be sent in multiple rounds; courses may be held until the table is ready.
- Kitchen ticket status and order history are available from the POS. Reopen an order to add items or continue service.
- Voiding items already visible to the kitchen follows the approval/reason flow shown by the POS; it is not equivalent to deleting an unsent cart line.
- The POS supports table reservations from the table board with table, guest, phone, party size and reservation time.
- **Open bills** and **Order history** provide access to unsettled and recent orders.

### 4.3 Settle or post a bill

Use the settlement panel to review the total and choose a supported tender. Configured country/payment modes determine the available choices. A room-service bill can be posted to an eligible guest folio when permitted; room charges are subject to property and reservation rules. Print the bill from the available print action. Settlement is recorded as a financial transaction, so use the authorized void/refund workflow to correct a completed posting rather than recreating or deleting it.

## 5. F&B Dashboard

Choose an outlet and a date or date range. The dashboard is read-only and refreshes current-day figures as new activity arrives. It summarizes:

- Gross sales, settled bills, average bill and covers.
- Sales by order type and tender.
- Open bills and their unsettled total.
- Complimentary orders, their count/value, voids and cancellations.
- Top-selling items.
- Average time from firing to ready.

Use the open-bill and exception lists to locate the source POS order before investigating or correcting it. Dashboard totals are property/outlet data, not a substitute for the folio or cashier record.

## 6. Kitchen Display

The Kitchen Display shows live kitchen orders and item-level tickets. Tickets include outlet, table/room or takeaway destination, order time, captain/waiter, courses, preparation station, instructions, allergy note and applicable dietary/allergen tags.

The available workflow is **Ordered → Fired → Started → Ready**. Depending on the outlet's KOT mode, an order is either auto-accepted/printed or awaits a kitchen user to press **Start**. Mark prepared items done; a ticket becomes ready when its live items are complete. Held courses can be released when service is ready. Cancellations/voids are shown with their reason and are not silently removed.

Use the station filter and course grouping to focus the work queue. The elapsed-time indicator is based on when items were fired; it highlights new, working and late tickets. On a device configured for a printer, use the screen's print-station option to receive routed tickets.

## 7. Menu, Bulk Upload and Recipes

### 7.1 Menu records

The Menu list can be searched and includes item name, outlet, category, price and availability. A menu item form contains:

| Field | Use |
|---|---|
| Outlet, Item name | Select the selling outlet and name the dish or drink. |
| Category, Price | Set a category suggestion and current selling price. |
| Photo, Description | Add the POS-card photo and item description. |
| Course, Prep station | Route the item to its service course and kitchen station. |
| Allergens & dietary tags | Tag declared allergens/dietary properties; these tags are matched against the guest allergy note on the Kitchen Display. |
| Vegetarian, Alcohol | Mark food type and alcohol. Alcohol is posted to the guest folio rather than a company folio. |
| Available | Control whether the item can be selected for sale. |

The item photo guidance in the form is a landscape JPG/WebP image around 800×600 and below 500 KB. Master values for categories, courses, stations and allergens are configured under **Settings → F&B → Menu master lists**.

### 7.2 Bulk upload

Authorized users can choose **Bulk upload** from Menu, download/use the offered template, populate item data, then submit the file through the import panel. Review validation feedback and correct rejected rows before retrying. Imported rows appear after the list refreshes. Do not treat a failed import as proof that no rows were created; check the resulting menu list before submitting the same data again.

### 7.3 Recipes

Choose **Recipes** on Menu, search for a dish and open it. Add ingredient lines with quantity per dish and optional notes, remove lines that no longer belong, then save. Inventory is reduced when the recipe-backed dish is fired through the kitchen workflow. A dish without a recipe does not deduct ingredient stock; this is a valid configuration. Recipe quantities use the ingredient's single configured unit.

## 8. Ingredients

Ingredients is the master list for kitchen stock and recipes. Search/filter active records and create or edit an ingredient with:

- **Ingredient** name and optional free-text **Category** (for example produce, dairy or dry goods).
- **Unit (UOM)**: kg, g, L, ml, pc, bottle or packet. Use one consistent unit for purchasing and recipes.
- **Cost / unit**: indicative last-known unit cost, used to value wastage; it is not FIFO accounting.
- **Input GST %** and **Active** status.

Turn an ingredient inactive rather than deleting it if recipes or stock history already refer to it.

## 9. Kitchen Inventory

Choose an outlet: stock is tracked **per outlet**, not as a combined property-wide quantity. The stock list shows ingredient, unit, category, cost, on-hand quantity, par level, last-counted date and status (**OK**, **LOW**, **OUT** or **NEGATIVE**). Negative stock is a warning that counts are stale or movements have exceeded the recorded balance; review the ledger rather than hiding it.

Authorized users have three stock actions:

1. **Receive** — record incoming stock and supplier/reference details requested by the form.
2. **Stock take** — enter a counted quantity; investigate a difference from the expected amount.
3. **Wastage** — record discarded stock and its reason.

Open an ingredient's movement history to see quantity change, resulting balance, reason, reference, note and supplier. Low-stock alerts may show menu dishes affected, but the system does not automatically mark dishes unavailable; a person decides whether to change menu availability.

## 10. Outlets and Waiters

An outlet represents a restaurant, room-service operation, bar, spa or other point of sale. Configure **Outlet name**, **Type**, **GST %**, **Disabled** and **KOT on send**:

- **Use F&B setting** inherits the property default.
- **Auto-accept and print** sends/prints the KOT and marks it started on the kitchen display.
- **Kitchen presses Start** leaves acceptance to the kitchen.

The outlet editor also provides waiter/staff assignment controls where configured. Keep staff associations and outlet assignments current so POS orders can be attributed correctly.

## 11. Printers and KOT Routing

Authorized users can add, edit, test or remove a printer. Important fields are:

| Field | Purpose |
|---|---|
| Printer name | Label shown to staff. |
| Connection | **Print station** (a kitchen screen claims the printer) or **Direct IP**. |
| Paper width, Copies | Receipt/ticket layout and number of copies. |
| IP address, Port | Network destination for a direct-IP printer (default port shown by the form). |
| Fallback printer | Backup destination when configured. |
| Prints KOTs / Prints bills | Select which documents this device handles. |
| Routes | Select outlet and prep station combinations served by the printer. A blank station route covers the outlet generally. |
| Disabled | Pause the printer without deleting its setup. |

Use **Test print** and review last-seen/last-printed, queue, error and failed-today information. For a print-station connection, the kitchen display must be opened on a device and set to print for that printer.

## 12. F&B Settings

Hotel Admin, Finance and F&B Manager can edit the F&B module settings. The Admin settings page groups controls as follows:

| Section | Fields and effect |
|---|---|
| Kitchen orders (KOT) | Auto-accept and print KOT; print void slips in the kitchen; flag a bill not sent to the kitchen after a configured interval. |
| Table reservations | How far ahead a reservation is shown and how long it remains visible. |
| External POS | Largest room charge accepted from an external POS; zero means no configured limit. |
| Menu master lists | Allergens/dietary tags, prep stations, courses and menu categories. Values are newline-separated suggestions/tags. |

Do not store secrets in free-text menu fields. Printer routes, outlet settings, menu records and stock are maintained on their own pages.

## 13. End-to-End Workflows

### Open, prepare and settle a dine-in order

1. Select the property and outlet; confirm the correct table is available.
2. Start a **Dine In** bill and add the guest count, waiter/customer details if needed, and menu items.
3. Check quantities, course, instructions and allergy notes.
4. Send the KOT. The kitchen accepts/starts it according to the outlet configuration, prepares each course and marks items ready.
5. Review the final bill, apply only permitted adjustments, settle using the selected tender, and print if required.
6. Confirm the order is no longer open and reconcile the related cashier session.

### Record a room-service order

1. Start **Room Service** and choose the in-house room.
2. Add items and any guest/allergy instructions; verify the room shown belongs to the intended current stay.
3. Send the KOT. The kitchen sees the room destination and tray setup tag.
4. Settle through an allowed tender or post to the guest folio, then confirm the posting in the folio.

### Receive and count ingredients

1. Create/activate each ingredient with a consistent unit.
2. Select the outlet in Kitchen Inventory and use **Receive** for a delivery.
3. Use **Stock take** to reconcile physical quantities; investigate negative or unexpected balances using movement history.
4. Record wastage with an accurate reason and update recipes when portions change.

## 14. Permissions and Security

- F&B app access is role- and module-gated. Front Desk may see F&B, but write actions are separately restricted by the UI and backend.
- F&B stock changes, menu imports/recipes and printer configuration are limited to **Finance**, **F&B Manager**, **Hotel Admin**, **System Manager** or **Administrator** as applicable.
- F&B Settings is limited to **Finance**, **F&B Manager**, **Hotel Admin**, **System Manager** and **Administrator** in the app navigation; backend setting permissions remain authoritative.
- Cashier PIN/security rules apply to money actions when configured. Do not share PINs or use another user's session.
- Access tokens and printer/network credentials must be stored only in their intended secured configuration fields.

## 15. Troubleshooting and FAQs

| Problem | Checks |
|---|---|
| No outlets or menu items | Confirm the selected property, that the outlet/menu item is active, and that the user has property access. |
| KOT does not appear | Check outlet KOT mode, whether items were fired/sent, selected outlet/station filters, and Kitchen Display connectivity. |
| Printer remains waiting/offline | Confirm a kitchen screen is set to **Print for this printer**, check IP/port for Direct IP, route outlet/station, disabled state and last error; send a test print. |
| A room cannot be charged | Confirm the guest is checked in, the room is eligible for charges and the folio/payment mode is allowed. |
| Ingredient stock is negative or low | Review the outlet-specific movement ledger and last count; correct with a receive/count action rather than changing the balance informally. |
| Menu item is missing from POS | Check outlet assignment, availability, category/search filter and selected property. |
| Bulk upload rejects rows | Review import validation details, required fields and allowed formats; correct the source file and inspect the menu list before retrying. |

## 16. Glossary

- **KOT:** Kitchen Order Ticket sent from POS to kitchen.
- **Outlet:** A restaurant, bar or other point of sale within a property.
- **Prep station:** Kitchen station responsible for preparing an item.
- **Course:** Service stage such as starter, main, dessert or drink.
- **Par level:** Target stock quantity used to identify low stock.
- **Stock take:** Physical count entered to reconcile recorded stock.
- **Print station:** A kitchen display device that claims and prints routed tickets.

## 17. Source Verification and Runtime Variations

This guide follows the current F&B app registry, React screens, shared resource forms, backend API permissions and the live F&B interface. The live property, outlets, menu, rates, printer availability and payment methods are site-specific and can change. Roles, enabled modules, country settings, network devices and third-party integrations can affect which actions appear. No sample records or credentials are universal configuration.
