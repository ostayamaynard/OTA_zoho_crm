# Registration → Invoice → Deal Data Flow

**Last Updated:** 10 December 2025 (aligned to 2025-12-10 export)
**Modules:** Registration_Records, Invoices, Deals
**Flow Type:** Multi-directional
**Status:** Outline - To be expanded

---

## Overview

This document details the data flow from Registration_Records through to Invoices and Deals, covering:
- How invoices are created from registrations
- Payment tracking and status updates
- Deal amount updates when invoices are paid

---

## Key Workflows

### Registration → Invoice Creation

**Primary Flow:**
```
Registration_Record created
    ↓
Deal created (lookup from Registration)
    ↓
Quote created from Deal
    ↓
Invoice created from Quote
    ↓
Invoice inherits:
  - Course_Name (lookup)
  - Account_Name
  - Contact_Name (Attendee)
```

---

### Invoice Payment → Multi-Module Updates

**WF: 52330000004251591 - New - Update deal and Reg record**
- **Trigger:** Invoice created or edited
- **Action:** Updates linked Deal and Registration_Record
- **Direction:** Invoices → Deals + Registration_Records

**WF: 52330000009085784 - Update Amount in Deal when Inv is paid**
- **Trigger:** Invoice.Status = 'Paid'
- **Action:** Updates Deal.Amount with payment amount
- **Direction:** Invoices → Deals

**WF: 52330000002460231 - Push Invoice to Xero**
- **Trigger:** Invoice.Status = 'Paid'
- **Action:** Syncs paid invoice to Xero accounting
- **Direction:** Invoices → Xero (external)

---

## Field Mappings

### Registration → Deal → Invoice

| Source | Field | Destination | Notes |
|--------|-------|-------------|-------|
| Registration | Attendee (Contact) | Invoice.Contact_Name | Via Deal |
| Registration | Course (lookup) | Invoice.Course_Name | Via Deal |
| Course | Fees | Invoice line items | Amount |
| Deal | Account_Name | Invoice.Account_Name | Account billing |

---

## Status Synchronization

### Invoice Status Impact

| Invoice Status | Registration Impact | Deal Impact | Xero Impact |
|---------------|-------------------|-------------|-------------|
| Created (Draft) | None | None | None |
| Awaiting Payment | Auto-send email (WF: 52330000008694463) | None | None |
| Sent | Invoice_Sent_Date set | None | None |
| Paid | Registration status may update | Deal.Amount updated | Synced to Xero |

---

## Payment Tracking

### Payment Sources

**Fields:**
- `Invoice.Payment_Source` (picklist): Stripe, Bank Transfer, Cash, etc.
- `Invoice.Payment_Type` (picklist)
- `Invoice.Stripe_ID` (text): Stripe transaction ID
- `Invoice.Paid_In_CREZ` (boolean): Manual payment flag

**Workflow:** WF: 52330000002460196 - Paid in Crez
- Marks invoice as paid when `Paid_In_CREZ` checkbox set

---

## Common Scenarios

### Scenario 1: Registration to Invoice Creation

**User Actions:**
1. Create Registration_Record
2. Create Deal linked to Registration
3. Create Quote from Deal
4. Create Invoice from Quote

**System Automations:**
- Invoice inherits course and contact details
- WF: 52330000008512961 "Update All Fields" populates reference fields
- Payment URL generated

---

### Scenario 2: Invoice Paid

**User Actions:**
1. Mark Invoice.Status = 'Paid' (manual or Stripe webhook)

**System Automations:**
1. WF: 52330000009085784 updates Deal.Amount
2. WF: 52330000002460231 syncs to Xero
3. WF: 52330000004251591 updates Registration_Record
4. Confirmation emails sent

---

## Related Documentation

- [Course → Registration Flow](course-registration-flow.md)
- [Invoice → Deal Flow](invoice-deal-flow.md)
- [Invoices Module - Workflows](../../modules/invoices/docs/invoices-workflows.md)
- [Invoices Module - Fields](../../modules/invoices/docs/invoices-fields.md)

---

**Note:** This document provides an outline of the Registration → Invoice → Deal data flow. For complete details, refer to the module-specific workflow documentation listed above.

**To be expanded with:**
- Detailed field propagation tables
- Complete workflow specifications
- Error handling procedures
- Troubleshooting guides
