<p align="center">
  <img src="../frontend/public/quantumberg-logo.png" alt="Quantumberg Technologies" />
</p>

<h1 align="center">Quantumberg PMS Finance Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Finance Teams, Front Desk Cashiers, Night Auditors, Hotel Administrators

---

## Table of Contents

1. Introduction
2. Access, Property Scope and Roles
3. Finance Sidebar Navigation
4. My Till
5. All Tills
6. Sessions and Shift Reports
7. Petty Cash
8. Shift Handover
9. Currency Desk
10. Billing and Folios
11. Folio History
12. Receivables and Accounts Receivable
13. Ledgers
14. Payables
15. Cash Outlook
16. Profit and Loss and Balance Sheet
17. Night Audit, Allowances and Other Finance Pages
18. Finance Settings
19. End-to-End Workflows
20. Permissions and Security
21. Troubleshooting and FAQs
22. Glossary
23. Source Verification and Runtime Variations

---

## 1. Introduction

Finance provides cashier sessions, guest folios, company receivables, supplier payables, subsidiary ledgers, cashier controls and management reports. Financial postings are auditable records; use the supported reversal, allowance, approval or correction workflow rather than deleting a posted transaction.

## 2. Access, Property Scope and Roles

The Finance app is available to **Finance**, **Front Desk**, **Night Auditor**, **Hotel Admin**, **System Manager** and **Administrator** roles when enabled for the selected property. Individual pages and money actions have additional server-side restrictions; Front Desk visibility does not grant every finance write permission.

The active property and its business date govern tills, folios, ledgers and reports. Confirm both before posting or reconciling.

## 3. Finance Sidebar Navigation

| Group | Sidebar page | Purpose |
|---|---|---|
| Cashier | My Till | Open/close the current user's till session and record cash movement. |
| Cashier | All Tills | Review terminals, open sessions, transfers, variances and cash office. |
| Cashier | Sessions | Search open/closed cashier sessions by business date. |
| Cashier | Petty Cash | Record petty-cash vouchers and property imprest. |
| Cashier | Shift Handover | Record shift cash count and follow-up handover. |
| Cashier | Currency Desk | Calculate/post foreign exchange and manage exchange rates. |
| Billing | Night Audit | Review business-date status, blockers and audit history. |
| Billing | Owner view | Finance-role summary of figures, guest movement and audit history. |
| Billing | Billing | Open folios, recent audit runs and My Till. |
| Billing | Folio History | Find closed folios and invoices. |
| Billing | Allowances to approve | Review and approve allowances requiring authorization. |
| Books | Receivables | Company/city-ledger invoices, account balances and collections. |
| Books | Ledgers | Review guest, deposit, AR and package subsidiary ledger balances. |
| Books | Payables | Maintain vendors, bills, approvals, payments and aging. |
| Books | Cash outlook | Forecast expected money in/out over 5, 15 or 30 days. |
| Books | Profit and loss | Management P&L over a selected period. |
| Books | Balance sheet | Management balance sheet as of a date. |
| Books | Transaction Codes | Configure posting codes and revenue groups. |
| Books | Reason Codes | Configure coded reasons for voids, adjustments, refunds and paid-outs. |
| Books | Reports | Shared report hub, finance reports and accounting export. |
| Books | Accounting Export | Export accounting data for supported external books. |
| Books | Settings | Tax, fees, corporate credit, till controls and exchange-rate settings. |

## 4. My Till

### 4.1 Open a session

If no till is open, choose the till/terminal (where configured), enter the **Opening float** and select **Open session**. One open session per cashier per business date is supported. A cashier PIN may be requested according to Finance settings.

### 4.2 Work in an open session

The summary distinguishes opening float, cash/card/instant or foreign-currency totals, paid-outs, drops, petty cash and expected cash. Guest payments and POS bills post to the open cashier session automatically; take those payments on the relevant Front Desk or Restaurant screen.

- **Paid out:** enter amount and reason for cash leaving the drawer.
- **Cash drop:** record cash removed to the safe/cash office; select destination where available.
- Other transfer actions shown for the configured till are PIN-protected where required.

Each money action is recorded in the session. Use the corresponding source screen for guest/restaurant payments.

### 4.3 Count and close

At shift end, enter the physical cash count and close the till. Compare counted against expected cash, review the variance and follow the configured manager-review process. Do not close a session using an estimated count. Open **Sessions** or the shift report to investigate after closure.

## 5. All Tills

All Tills shows the property business date, terminals, open sessions/cashiers, expected cash, cash-office balance/in-transit amounts, pending transfers and variances requiring review. Authorized users can add/edit a terminal with:

- Terminal name and kind (Front Desk, Restaurant, Bar, Spa, Cash Office or Other).
- Optional outlet, bill printer, default float and disabled flag.

Cash-office actions can receive pending transfers, record bank deposits and approve a variance where authorized. PIN may be required for cash receipt/deposit actions. Configure bill printer only from printers set to print bills. Do not delete/recreate terminals to hide a session variance.

## 6. Sessions and Shift Reports

Sessions lists open/closed cashier records for the selected business date. It shows cashier, status, opening float, system cash, expected and counted cash, variance, opened and closed times. Select the cashier link to open its shift report. Use **Open / close till** to return to My Till; a session begins when the cashier opens a till, not through a separate create-session form.

The shift report summarizes the session's collections by tender and recorded cash movement. Reconcile against source transactions and investigate variances before approving.

## 7. Petty Cash

Petty Cash is property-specific. Its summary shows imprest, spending today/month and voucher count. **Save imprest** changes the property's float. A new voucher contains **Payee**, **Amount**, **Category** (Supplies, Maintenance, Transport, Staff Welfare or Miscellaneous) and **Reason**. The voucher posts against the property's open till and may require a PIN. Open My Till first if the drawer is closed.

Review voucher history and totals after posting. Cash paid directly from a till is distinct from a supplier bill in Payables.

## 8. Shift Handover

Create a Shift Handover with shift (**Morning**, **Evening**, **Night**), date, opening cash, cash collected, payouts, closing cash, recipient, status (**Open** or **Closed**) and handover notes. The date field does not allow past dates in the configured form. Use notes to communicate exceptions/follow-ups; the record does not replace cashier session reconciliation.

## 9. Currency Desk

Currency Desk contains a calculator, exchange rate list and today's exchange history.

- Select offered currency and **Buy** or **Sell**, enter the foreign amount and choose **Calculate**.
- Review exchange rate, local amount, service tax and total before **Post exchange**.
- Posting is a cashier/financial operation and may request a PIN.
- Authorized Finance/Hotel Admin/System Manager/Administrator users can enter buy/sell rates and service tax and **Save**.
- **Fetch rates** is available to Finance/Hotel Admin/System Manager/Administrator where the rate provider is configured; manually entered rates are retained according to the server response.

Only currencies enabled for the property are offered. Check today's rate and direction carefully before posting.

## 10. Billing and Folios

Billing lists folios for the selected property with guest, status, invoice number, total, paid and balance. Select a folio to open its detail. The folio workflow supports reviewing/posting permitted charges, payments/settlement and printing the GST/tax invoice as configured. Charge and payment codes determine how postings appear in ledgers and reports.

Billing also links to:

- **Night Audit / End of Day** to review and close the property's business date.
- Recent audit runs and their audit packs.
- **My Till** to open/reconcile the cashier session.

Before settlement, verify guest, reservation, charges, taxes, payments, company/credit destination and remaining balance.

## 11. Folio History

Folio History helps locate closed bills/invoices. Search/filter for the required folio and open its detail for review or permitted print actions. Historical records are retained for audit; correction of a closed posting must use the authorized adjustment or allowance workflow.

## 12. Receivables and Accounts Receivable

Finance **Receivables** is the company/city-ledger collection workflow. Review company invoices and account balance/aging, open an account or invoice, record an authorized payment and review the resulting balance. Company statements can be printed or emailed to the configured billing contact/entered recipients.

Revenue's **Accounts Receivable** page is the Corporate Account master data (company contacts, negotiated rate plan and credit allowed); it is not the statement/collection ledger. Configure or correct company details there, then use Finance Receivables for money due and receipt activity. Only Finance, Hotel Admin, System Manager or Administrator can settle company balances in the UI; the server enforces permission.

## 13. Ledgers

Ledgers provides a business-date view of Guest, Deposit, AR and Package balances, total debits/credits, journal totals by transaction code, city-ledger aging and a folio reconciliation check. Select a date and refresh. The key reconciliation compares Guest + Deposit ledger net to folio balances; total debits exceeding credits can simply represent amounts guests owe, not necessarily an imbalance.

When a folio differs, open the linked folio and compare its postings with ledger entries. Company statement actions can print/save as PDF or email to approved recipients.

## 14. Payables

Payables tracks supplier vendors and bills. The Bills tab can filter **Still to pay**, **Awaiting approval**, **Paid**, **Cancelled** or **All bills**; the Vendors tab contains supplier details and current balance/aging. Summary cards show owed, overdue and bills awaiting approval.

- Finance/Hotel Admin/System Manager/Administrator can enter a vendor or supplier bill.
- Only Hotel Admin/System Manager/Administrator can approve a bill in the UI.
- Approved bills may be paid through the supported payment action; cancellation is a separate action with permission checks.
- Bill information includes vendor, bill number/date, due date, expense category, description, amount, tax rate/amount, total, paid, outstanding and status.

Supplier bills are not petty-cash vouchers. Cash paid from an open till belongs in Petty Cash.

## 15. Cash Outlook

Cash Outlook is a read-only forecast of expected receipts/payments for **5**, **15** or **30** days. Its calculation includes company bills, guest departures, deposits due and vendor bills; overdue items are counted today. The starting amount can use open-till cash or a user-entered cash/bank amount. Use **Update** after entering an opening position.

Select a day row to expand its underlying items. Draft supplier bills awaiting approval are flagged in the forecast. This is a planning view, not a bank reconciliation and not a posted transaction.

## 16. Profit and Loss and Balance Sheet

The management P&L offers **This month**, **Last month** or custom dates. It summarizes recorded room/F&B/banquet/other income, allowances, supplier bills, petty cash and paid-outs, tax collected/paid and the resulting management net.

The Balance Sheet tab shows management assets, liabilities and net as of a selected date, plus tax-month figures. The screen explicitly warns that these are **management views, not statutory accounts**. Payroll, depreciation, loans and payments outside Kamra may not be represented. Use the accountant's approved books and Accounting Export for statutory reporting.

## 17. Night Audit, Allowances and Other Finance Pages

### Night Audit

End of Day shows business date/property time, automatic run status, blockers, pending arrivals/departures, open cashiers and open POS bills. Review blockers before running the audit. Audit history can be searched by date/status and opened for a pack; authorized recovery/rebuild actions are for the specific failure cases shown on screen. An audit posts room/tax and rolls the business date—do not repeat a completed posting to correct a date issue.

### Allowances to approve

Review requested allowances and approve only when authorized. Allowance actions are audited with the applicable reason and may be limited by Finance settings/thresholds. See the related voucher/detail page for the record.

### Transaction Codes and Reason Codes

Transaction Codes classify revenue, payment, tax, package and adjustment postings, with code, description, revenue group, tax and property scope fields as configured. Reason Codes classify void, adjust, rate change, refund, paid-out and complimentary reasons; a code can require supervisor authorization. Disable used codes instead of deleting records referenced by transactions.

### Reports and Accounting Export

The shared Reports hub exposes links filtered by roles/module: manager flash, audit history, till shift report, ledgers, folio history, voids/allowances and accounting export among others. The Accounting Export page prepares supported accounting output for the external books; select the requested date/property scope, review warnings/totals and export. Reconcile the export with source ledgers before import to another accounting system.

## 18. Finance Settings

Finance Settings are edited by Hotel Admin, Finance and System Manager as permitted by the backend schema. Main groups are:

| Section | Important settings |
|---|---|
| Room tax | Tax mode, slab threshold, lower/upper rates, whether displayed rates include tax. |
| Fees & levies | Room levy/name, levy taxability, cleaning fee/taxability, pet allowance/charge and charge applicability. |
| Corporate billing | Behavior when a credit company has no billing rules. |
| Company credit | Default payment terms, credit control, overdue grace period, email reminders. |
| Cashier controls | Tills required for money, PIN requirements/lock duration, cash-refund limit for new cashiers, variance manager threshold, allowance approval and threshold. |
| Exchange rates | Offered currencies, market-rate margin and automatic daily fetch. |

These settings affect guest totals, invoice presentation, credit collection and authorization. Confirm local tax treatment with the property's finance adviser before changing tax fields.

## 19. End-to-End Workflows

### Reconcile and close a till

1. Confirm property and business date; open the correct terminal with a verified float.
2. Post guest/POS payments on their source screens and record cash paid-outs/drops in My Till.
3. At shift end, count physical cash and close the session.
4. Review any variance in Sessions/All Tills; follow manager approval where required.
5. Include the session report in the handover and Night Audit review.

### Receive a company payment

1. Verify the company account, invoice and outstanding balance.
2. Open Finance → Receivables and select the correct company.
3. Record the received amount/mode using the supported payment action.
4. Print or email the updated company statement if needed.
5. Confirm the ledger and folio/account balances agree.

### Process supplier invoice

1. Create/verify the vendor and its payment terms.
2. Enter supplier bill number/date, due date, category, amount and applicable tax.
3. Submit for approval; an authorized Hotel Admin/System Manager/Administrator approves.
4. Pay an approved bill using the supported action and reconcile Payables aging.
5. Review the bill in Cash Outlook/P&L as appropriate.

## 20. Permissions and Security

- Role availability is not blanket finance authorization. The backend separately gates cashier, folio, approval, adjustment, statement and report actions.
- PINs and payment credentials are private. Do not share them or record them in handover notes.
- Only authorized approvers may approve supplier bills/allowances or manager variances.
- Use a reason code and audit trail for voids, refunds and adjustments.
- Company statements and guest folios contain financial/personal information; share only with authorized recipients.

## 21. Troubleshooting and FAQs

| Problem | Checks |
|---|---|
| Cannot open a till | Check selected property, business date, terminal availability and whether this cashier already has an open session. |
| Expected cash differs from count | Review tenders, paid-outs, drops, transfers and source transactions; escalate according to variance policy. |
| Payment action requests a PIN | Use the signed-in cashier's configured PIN; ask an administrator for a reset if unavailable. |
| Folio and ledger do not reconcile | Open the listed discrepant folios and trace postings by transaction code/date; do not alter ledger records directly. |
| Supplier bill cannot be approved | Confirm status is Awaiting Approval and the user has an approver role. |
| Company balance is not reduced | Check payment posting/status, property and company invoice selected, then refresh Receivables and Ledgers. |
| Cash Outlook differs from bank | Enter the known cash/bank opening amount; open tills alone do not include external bank balances. |
| P&L differs from statutory accounts | The screen is a management view of records in Kamra, not a statutory ledger; reconcile using Accounting Export and the accountant's books. |

## 22. Glossary

- **Folio:** Guest or company bill with charges, payments and balance.
- **Till session:** Cashier shift opened against a till/terminal.
- **Imprest:** Property's petty-cash float.
- **City ledger:** Company receivable balance.
- **Allowance:** Authorized reduction/credit to a charge or balance.
- **Business date:** Hotel operating date used for cashier and audit periods.
- **Subsidiary ledger:** Guest/deposit/AR/package balance view that supports reconciliation.

## 23. Source Verification and Runtime Variations

This guide follows the Finance app registry, cashier, billing, ledger, receivable/payable, cash forecast, management-books and End of Day screens, backend APIs and the live application. Tax rules, payment tenders, terminals, PIN policy, roles, country pack and connected accounting providers vary by property. Management reports contain only data recorded in Kamra and are not a substitute for statutory accounting.
