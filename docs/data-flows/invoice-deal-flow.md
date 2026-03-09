# Invoice → Deal Data Flow

**Last Updated:** 10 December 2025 (aligned to 2025-12-10 export)
**Modules:** Invoices, Deals
**Flow Type:** Bi-directional
**Status:** Outline - To be expanded

---

## Overview

This document details the bi-directional data flow between Invoices and Deals modules, focusing on:
- Deal-to-Invoice creation flow
- Payment amount updates
- Status synchronization

---

## Relationship Structure

### Lookup Field

| Property | Value |
|----------|-------|
| **Field** | `Invoices.Deal_Name__s` |
| **Type** | lookup → Deals |
| **Cardinality** | Many-to-One (Multiple invoices can link to one deal) |

---

## Key Workflows

### WF: 52330000009085784 - Update Amount in Deal when Inv is paid

| Property | Value |
|----------|-------|
| **Trigger** | Invoice.Status field update |
| **Condition** | Status = 'Paid' |
| **Action** | Updates Deal.Amount with invoice total |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085784) |

**Flow:**
```
Invoice.Status changed to 'Paid'
    ↓
WF: 52330000009085784 fires
    ↓
Deal.Amount updated with Invoice.sbhtc__Total_inc_GST0
    ↓
Deal stage may progress based on amount
```

---

### WF: 52330000004251591 - New - Update deal and Reg record

| Property | Value |
|----------|-------|
| **Trigger** | Invoice created or edited |
| **Action** | Updates linked Deal and Registration_Record |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004251591) |

---

## Field Mappings

### Deal → Invoice (On Invoice Creation)

| Deal Field | Invoice Field | Data Type |
|------------|--------------|-----------|
| Deal_Name | Invoice.Subject | text |
| Account_Name | Invoice.Account_Name | lookup (Accounts) |
| Contact_Name | Invoice.Contact_Name | lookup (Contacts) |
| Course (if applicable) | Invoice.Course_Name | lookup (Courses) |
| Amount | Invoice line items | currency |

### Invoice → Deal (On Payment)

| Invoice Field | Deal Field | Trigger |
|--------------|-----------|---------|
| sbhtc__Total_inc_GST0 | Deal.Amount | When Status = 'Paid' |

---

## Common Scenarios

### Scenario 1: Quote to Invoice Creation

**Flow:**
1. Deal created
2. Quote created from Deal
3. Invoice created from Quote
4. Invoice inherits Deal details

**Workflows:**
- WF: 52330000008512961 "Update All Fields" on invoice creation

---

### Scenario 2: Invoice Paid - Deal Updated

**User Action:**
- Set Invoice.Status = 'Paid'

**System Response:**
1. WF: 52330000009085784 fires
2. Deal.Amount = Invoice.sbhtc__Total_inc_GST0
3. Deal may progress to "Closed Won" stage
4. Xero sync triggered (separate workflow)

---

## Integration Points

### Invoices → Xero

When invoice is paid:
- WF: 52330000002460231 "Push Invoice to Xero"
- Syncs paid invoice data to Xero accounting

### Invoices → Registration_Records

When invoice status changes:
- WF: 52330000004251591 updates linked Registration_Record
- May update registration payment status

---

## Related Documentation

- [Registration → Invoice Flow](registration-invoice-flow.md)
- [Course → Registration Flow](course-registration-flow.md)
- [Invoices Module - Workflows](../../modules/invoices/docs/invoices-workflows.md)
- [Deals Module - Kanban Usage](../../modules/deals/docs/deal-kanban-usage.md)

---

**Note:** This document provides an outline of the Invoice → Deal data flow. For complete details, refer to the module-specific workflow documentation.

**To be expanded with:**
- Complete field propagation tables
- Detailed workflow conditions
- Deal stage progression logic
- Error handling and troubleshooting
