# Data Flow Documentation

**Last Updated:** 8 January 2026
**Purpose:** Cross-module data flow and integration documentation for Zoho CRM

---

## Overview

This directory contains comprehensive documentation of how data flows between modules and external systems in the Zoho CRM implementation. Unlike module-specific documentation (which focuses on individual modules in isolation), these documents explain the **connections** and **dependencies** between modules.

**When exports change:** run `python tools/update_pipeline.py --apply` (or with `--date/--previous-date`) and check `reports/manual_review_<new>_vs_<old>.md` for curated files to update (journeys, kanban stages, SOPs).

---

## Available Documentation

### Course Lifecycle Data Flows

| Document | Description | Key Modules |
|----------|-------------|-------------|
| [course-registration-flow.md](course-registration-flow.md) | Course → Registration data flow and field propagation | Courses, Registration_Records |
| [registration-invoice-flow.md](registration-invoice-flow.md) | Registration → Invoice creation and payment tracking | Registration_Records, Invoices, Deals |
| [invoice-deal-flow.md](invoice-deal-flow.md) | Invoice → Deal amount updates and status sync | Invoices, Deals |

### External Integration Flows

| Document | Description | Systems |
|----------|-------------|---------|
| [course-integration-flows.md](course-integration-flows.md) | WordPress, Workdrive, Xero, Stripe, ClickSend integrations | Courses, Invoices, External APIs |

---

## Quick Reference: Complete Course Lifecycle

```
┌──────────────┐
│    Course    │ (1) Course created, published
│    Created   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Registration │ (2) Student registers for course
│   Created    │     Fields propagate from Course
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Deal Created │ (3) Deal created for revenue tracking
│              │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Quote Created │ (4) Quote generated from Deal
│              │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Invoice       │ (5) Invoice created from Quote
│Created       │     Linked to Course, Registration, Deal
└──────┬───────┘
       │
       ├──────────────────────┐
       │                      │
       ▼                      ▼
┌──────────────┐       ┌──────────────┐
│Payment       │       │Invoice Sent  │
│Received      │       │to Customer   │
└──────┬───────┘       └──────────────┘
       │
       ▼
┌──────────────┐
│Deal Amount   │ (6) Deal updated with payment amount
│Updated       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Registration  │ (7) Registration marked as paid
│Status        │
│Updated       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Course        │ (8) Course confirmed, registrations count updated
│Confirmed     │
└──────────────┘
```

For detailed step-by-step flows, see the individual documentation files.

---

## Key Concepts

### Field Propagation

**Definition:** When a record is created or updated, certain fields are automatically copied from related records.

**Example:** When a Registration_Record is created:

- `Course.Course_Start_Time` → `Registration.Start_Date`
- `Course.Select_Venue` → `Registration.Venue`
- `Course.Course_Trainer` → `Registration.Trainer`

**See:** [course-registration-flow.md](course-registration-flow.md)

### Workflow Sequencing

**Definition:** The order in which workflows must fire to ensure data consistency.

**Example:** Invoice payment workflow sequence:

1. Invoice.Status = 'Paid' (manual or webhook)
2. "Push Invoice to Xero" workflow fires
3. "Update Amount in Deal" workflow fires
4. "Update Registration Record" workflow fires

**See:** [registration-invoice-flow.md](registration-invoice-flow.md)

### Bi-directional Updates

**Definition:** When two modules update each other's fields to maintain synchronization.

**Example:** Courses ↔ Registration_Records:

- Course updates Registration when Course_Start_Time changes
- Registration updates Course.Registrations_Confirmed when status changes

**See:** [course-registration-flow.md](course-registration-flow.md)

### External Sync Points

**Definition:** Moments when CRM data is synchronized with external systems.

**Example:** WordPress sync triggers:

- Course.Course_Status = 'Sync to Wordpress'
- Course.Course_Status = 'Completed'
- Course.Course_Confirmed = true

**See:** [course-integration-flows.md](course-integration-flows.md)

---

## Data Flow Patterns

### Pattern 1: Lookup-Based Propagation

**When:** Parent record fields need to appear in child record
**How:** Lookup field + workflow with field update actions
**Example:** Course → Registration

### Pattern 2: Status Change Cascade

**When:** Status change in one module triggers updates in related modules
**How:** Field update workflow with related record update actions
**Example:** Invoice.Status = 'Paid' → Deal.Amount updated

### Pattern 3: Count Rollup

**When:** Parent needs to track count of related child records
**How:** Related list rollup formula OR workflow that increments/decrements
**Example:** Course.Registrations_Confirmed count

### Pattern 4: External System Sync

**When:** CRM data needs to match external system
**How:** Webhook workflow or Zoho Flow integration
**Example:** Invoice → Xero accounting

### Pattern 5: Manual Trigger Cascade

**When:** User action should trigger multiple downstream updates
**How:** Boolean checkbox field + workflow + related record updates
**Example:** Course.Update_Registration_Records = true → updates all linked registrations

---

## Common Workflow Triggers

### Automatic Triggers (No User Action)

| Trigger Event | Example | Typical Actions |
|---------------|---------|-----------------|
| **Record Create** | New course created | Set ID fields, create folders, create tasks |
| **Field Update** | Course_Status changed | Sync to WordPress, send notifications |
| **Time-Based** | 10 days before course | Send trainer SMS, generate PDFs |
| **Related Record Update** | Registration marked paid | Update course confirmation count |

### Manual Triggers (User Action Required)

| Trigger Field | Module | Action |
|---------------|--------|--------|
| Send_Trainer_email | Courses | Send logistics email to trainer |
| Update_Registration_Records | Courses | Push course changes to all registrations |
| Paid_In_CREZ | Invoices | Mark invoice as paid in CRM |

---

## Module Relationship Summary

### Core Revenue Flow

```
Leads → Contacts → Deals → Quotes → Invoices
         ↓
    Registration_Records ← Courses
```

### Course Management Flow

```
Products (Qualifications)
   ↓
Courses ← Venues
   ↓        ↓
   └─→ Registration_Records ← Contacts (Attendees)
           ↓
        Invoices → Deals
```

### External Integration Points

```
Courses → WordPress (public calendar)
Courses → Workdrive (materials)
Registration_Records → ClickSend (SMS notifications)
Invoices → Xero (accounting)
Invoices → Stripe (payments)
```

---

## Related Documentation

### Module-Specific Documentation

For detailed module information, see:

- [Courses Module Docs](/modules/courses/docs/)
- [Registration_Records Module Docs](/modules/registration_records/docs/)
- [Invoices Module Docs](/modules/invoices/docs/)
- [Deals Module Docs](/modules/deals/docs/)

### Workflow Documentation

For complete workflow references:

- [courses-workflows.md](/modules/courses/docs/courses-workflows.md)
- [invoices-workflows.md](/modules/invoices/docs/invoices-workflows.md)
- [Master Workflow URLs](/docs/master-workflow-urls.md)

### Field Documentation

For field catalogs:

- [courses-fields.md](/modules/courses/docs/courses-fields.md)
- [invoices-fields.md](/modules/invoices/docs/invoices-fields.md)

---

## How to Use This Documentation

### For New Team Members

1. Read this README to understand the overall architecture
2. Review [course-registration-flow.md](course-registration-flow.md) to understand the primary revenue flow
3. Explore module-specific docs for details on individual modules

### For Troubleshooting

1. Identify which modules are involved in the issue
2. Find the relevant data flow document (e.g., if invoice not updating deal, see [invoice-deal-flow.md](invoice-deal-flow.md))
3. Check workflow execution in Zoho CRM against documented sequence

### For New Feature Development

1. Review existing data flows to understand current patterns
2. Identify integration points with existing workflows
3. Plan new workflows to align with established patterns
4. Update this documentation when complete

---

## Maintenance Notes

### Updating These Documents

- When workflows are modified, update the corresponding data flow document
- When new modules are added, create new data flow documentation
- Keep diagrams synchronized with actual CRM configuration
- Update "Last Updated" dates when making changes

### Verification

- Cross-reference with `/modules/{module}/docs/{module}-workflows.md`
- Test workflows in Zoho CRM to verify documented behavior
- Validate field mappings against actual CRM exports

---

## Gaps & Future Documentation

### Current Gaps

- Deals → Quotes flow (not yet documented in detail)
- Accounts → Courses (Last_Course field) propagation
- Team_Tasks creation and assignment flows
- Course_Performance metrics calculation

### Planned Documentation

- Lead conversion to Contact/Deal flow
- Email template and ClickSend SMS integration details
- Workdrive folder structure and access controls
- Certificate generation and distribution flow

---

**Document Index Created:** 2025-11-21
**Documentation Coverage:** Courses, Registration_Records, Invoices, Deals
**External Systems:** WordPress, Workdrive, Xero, Stripe, ClickSend
