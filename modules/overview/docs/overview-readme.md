# Overview Module - System-Wide Documentation

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-12-10
**Last Updated:** 10 December 2025

---

## Purpose

The Overview module provides system-wide documentation including:
- Complete customer journey across all modules
- Module relationships and dependencies
- Integration architecture
- Cross-cutting workflows

---

## Module Inventory

### Primary Modules

| Module | Fields | Workflows | Purpose |
|--------|--------|-----------|---------|
| **Leads** | 151 | 19 | Prospective customer management |
| **Contacts** | 113 | 7 | Individual person records |
| **Accounts** | 61 | 4 | Company/organization records |
| **Deals** | 86 | 19 | Sales opportunities |
| **Courses** | 137 | 37 | Training course management |
| **Registration_Records** | 78 | 36 | Course attendee enrolments |
| **Invoices** | 57 | 15 | Billing and payments |
| **Quotes** | 40 | 8 | Quotation management |
| **Venues** | 23 | 0 | Training locations |

### Supporting Modules

| Module | Purpose |
|--------|---------|
| Team_Tasks | Operational task management |
| Course_Performance | Course analytics |
| Products | Course templates and pricing |
| Campaigns | Marketing campaigns |

---

## System Architecture

### Customer Journey Flow

```
Lead → Contact → Account → Deal → Registration → Course Delivery → Certification
```

### Module Relationships

```
                    ┌─────────────┐
                    │   Leads     │
                    └──────┬──────┘
                           │ converts to
                    ┌──────▼──────┐
                    │  Contacts   │
                    └──────┬──────┘
                           │ linked to
                    ┌──────▼──────┐
                    │  Accounts   │
                    └──────┬──────┘
                           │ creates
                    ┌──────▼──────┐
                    │   Deals     │
                    └──────┬──────┘
                           │ generates
              ┌────────────▼────────────┐
              │  Registration_Records   │
              └────────────┬────────────┘
                           │ linked to
                    ┌──────▼──────┐
                    │   Courses   │
                    └─────────────┘
```

---

## Integration Points

### External Systems

| System | Integration Type | Modules Affected |
|--------|------------------|------------------|
| **WordPress** | Webhook/API | Courses, Leads |
| **Xero** | Sync | Contacts, Invoices |
| **Zoho Workdrive** | Zoho Flow | Courses, Contacts, Registration_Records |
| **ClickSend SMS** | API | Courses, Registration_Records |
| **Stripe** | Webhook | Leads, Deals |

### Internal Zoho Integrations

- Zoho Calendar
- Zoho Books
- Zoho Flow
- Zoho Analytics

---

## Workflow Summary

### Total System Workflows (from 2025-12-10 export)

| Module | Workflow Count |
|--------|----------------|
| Courses | 37 |
| Registration_Records | 36 |
| Invoices | 15 |
| Leads | 19 |
| Deals | 19 |
| Quotes | 8 |
| Contacts | 7 |
| Accounts | 4 |
| Venues | 0 |
| **Total** | **158** |

---

## Key Lookup Relationships

### Courses Dependencies
- Course_Trainer → Contacts
- Course_Qualification → Products
- Select_Venue → Venues
- Private_Course_Client → Accounts

### Registration_Records Dependencies
- Course → Courses
- Attendee → Contacts
- Account_Name → Accounts
- Related_Deal → Deals
- Venue → Venues
- Invoice → Invoices

### Deals Dependencies
- Courseaa → Courses
- Account_Name → Accounts
- Contact_Name → Contacts

---

## Files in This Module

### Data Files
- `customer-journey-overview.json` - Complete customer journey across all modules
- `lucid-workflow.json` - Original Lucid Chart export
- `lucid-workflow-enhanced.json` - Enhanced workflow details

### Diagrams
- `overview-complete-journey.mmd` - All 11 customer journey stages
- `module-relationships.mmd` - Entity-relationship diagram
- `integration-architecture.mmd` - External system connections

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial documentation |
