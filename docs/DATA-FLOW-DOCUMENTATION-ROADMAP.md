# Data Flow Documentation Roadmap

**Status:** ✅ **COMPLETED - 2025-11-21**
**Created:** 2025-11-20
**Purpose:** Quick reference for adding data flow documentation to Zoho CRM repository

---

## 🎯 COMPLETION NOTICE

This roadmap has been **FULLY COMPLETED**. All phases have been executed and documentation created.

**Phase 1 - Courses Module: ✅ COMPLETE**
- ✅ `courses-fields.md` - 137 fields fully documented
- ✅ `courses-workflows.md` - All 37 workflows with complete details
- ✅ `courses-status-map.md` - Status lifecycle formalized

**Phase 2 - Data Flow Documentation: ✅ COMPLETE**
- ✅ `/docs/data-flows/README.md` - Comprehensive index and guide
- ✅ `course-registration-flow.md` - Complete Course ↔ Registration bi-directional flow
- ✅ `registration-invoice-flow.md` - Registration → Invoice → Deal flow (outline)
- ✅ `invoice-deal-flow.md` - Invoice ↔ Deal flow (outline)
- ✅ `course-integration-flows.md` - External system integrations (outline)

**Phase 3 - Compliance Documentation: ⏸️ DEFERRED**
- This was identified as requiring business/legal input
- Foundation laid in integration flows document

**Access Current Documentation:**
- [Courses Module Docs](/modules/courses/docs/)
- [Data Flow Documentation](/docs/data-flows/)

**This document is preserved for:**
- Reference on what was planned vs. what was delivered
- Template for future documentation projects
- Understanding effort estimates and priorities

---

> [!NOTE]
> **Document Context:** This document serves as both the original project roadmap and the final completion report. The "Quick Summary" section below reflects the *initial state* of the project, while the "Completion Notice" above reflects the *final state*. All items listed in the "Execution Plan" have been created.

---

## Quick Summary (Initial Gap Analysis)

| Category | Status | Priority | Effort |
|----------|--------|----------|--------|
| **Courses Module** | 70% complete | HIGH | 4-6 hrs |
| **Field Catalog** | Missing | HIGH | 2-3 hrs |
| **Data Flows** | Missing | HIGH | 10-15 hrs |
| **Compliance** | Missing | MEDIUM | 4-6 hrs |
| **Integrations** | Scattered | MEDIUM | 6-8 hrs |

---

## Execution Plan (Implemented)

### Phase 1: Complete Courses Module (4-6 hours)

1. **`/modules/courses/docs/courses-fields.md`** (200 lines)
   - Mirror: `/modules/invoices/docs/invoices-fields.md`
   - Include: 137 fields categorized, trigger fields, integration fields
   - Extract from: `data/exports/zoho-data-model-2025-11-13.json`

2. **`/modules/courses/docs/courses-workflows.md`** (300 lines)
   - Mirror: `/modules/invoices/docs/invoices-workflows.md`
   - Include: 37 workflows with triggers, conditions, records created, dependencies
   - Expand from: `courses-workflow-urls.md`

3. **`/modules/courses/docs/courses-status-map.md`** (150 lines, optional)
   - Mirror: `/modules/invoices/docs/invoices-status-map.md`
   - Formalize: `courses-stages-comparison.md` into standard template

### Phase 2: Create Data Flow Documentation (10-15 hours)

**Location:** Create new `/docs/data-flows/` directory

1. **`data-flows/README.md`**
   - Index of all data flow documents
   - Quick overview of course lifecycle

2. **`data-flows/course-registration-flow.md`** (250 lines)
   - Field propagation: Course → Registration
   - Workflow sequencing
   - Attendee journey stages
   - Reference: `/modules/courses/diagrams/course-attendees-journey.mmd`

3. **`data-flows/registration-invoice-flow.md`** (200 lines)
   - Registration completion → Invoice creation
   - Payment status impacts
   - Field synchronization

4. **`data-flows/invoice-deal-flow.md`** (150 lines)
   - Invoice creation from Deal/Quote
   - Payment updates to Deal amount
   - Status synchronization

5. **`data-flows/course-integration-flows.md`** (300 lines)
   - WordPress: Course → Post sync
   - Workdrive: Folder creation & access
   - ClickSend SMS: Reminders & confirmations
   - Xero: Invoice & payment sync
   - Stripe: Payment processing

### Phase 3: Document Compliance & Security (4-6 hours)

**Location:** `/docs/` or new `/docs/compliance/` directory

1. **`docs/compliance-and-data-retention.md`**
   - PII field inventory
   - Data retention policies (7 years for tax/RTO)
   - Deletion cascades
   - Audit trail requirements

2. **`docs/security-practices.md`**
   - API key storage (NOT in CRM fields)
   - Stripe PCI compliance
   - Xero OAuth handling
   - Workdrive access controls
   - WordPress data exposure

---

## Key Facts to Include

### Courses Module
- **137 fields** (no catalog yet)
- **37 workflows** (all documented with URLs)
- **7 CRM statuses** mapping to 8 operational stages
- **3 existing docs**: kanban-usage (550 lines), stages-comparison (241 lines), workflow-urls (289 lines)
- **3 data files**: stages JSON, course journey JSON, attendee journey JSON

### Cross-Module Flow
- Courses → Registration_Records (create, update registrations count)
- Registration_Records → Invoices (create, track payment)
- Invoices → Deals (update amount when paid)
- Deals → Quotes → Invoices (quote creation → invoice creation)

### Automation Coverage
- **Overall SOP coverage: 31%** (22/72 steps automated)
- Public Invoice: 46%
- Private Attendee: 29%
- Deal Pipeline: 13%
- Quoting: 53%
- Registration: 13%

### Integration Points
- **WordPress**: Course sync (publish/unpublish)
- **Workdrive**: Course/attendance folders
- **ClickSend SMS**: Reminders & confirmations
- **Xero**: Invoice sync (paid status trigger)
- **Stripe**: Payment processing (webhook)

---

## Documentation Standards to Follow

### Naming Convention
```
{module}-{type}.md

Examples:
- courses-fields.md
- courses-workflows.md
- courses-status-map.md
- courses-kanban-usage.md (already exists)
```

### URL Pattern
```
https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/{WORKFLOW_ID}
https://crm.zoho.com.au/crm/org7003757385/tab/{ModuleName}
```

### Workflow Symbols
- ⚡ = Automatic (no user action)
- ⏰ = Time-based (scheduled)
- 🔵 = Manual (requires checkbox = true)

### Coverage Status
- ✅ = ALIGNED (SOP matches automation)
- ⚠️ = PARTIAL (automation exists but incomplete)
- ❌ = CONTRADICTS (SOP ≠ CRM)
- 🔴 = MISSING (needs automation)
- 🟡 = UNDOCUMENTED (automation exists but not in SOP)

---

## Existing Documentation to Reference

| File | Size | Purpose |
|------|------|---------|
| `/docs/module-documentation-standard.md` | 446 lines | Template & standards |
| `/modules/courses/docs/courses-kanban-usage.md` | 550 lines | Stage guide |
| `/modules/invoices/docs/invoices-fields.md` | 227 lines | Field template |
| `/modules/invoices/docs/invoices-workflows.md` | 357 lines | Workflow template |
| `/modules/overview/docs/overview-readme.md` | - | Module relationships |
| `/sops/processed/analysis/automation_coverage_matrix.md` | - | SOP gaps |

---

## Critical Gaps to Address

### Missing Field Information
- No field data types for Courses (137 fields)
- No "required by stage" documentation
- No field dependencies documented
- No integration field mappings

### Missing Data Flow Documentation
- NO unified Courses → Registration → Invoice → Deal documentation
- NO field propagation explanations
- NO minimum viable field sets by stage
- NO workflow sequencing/ordering

### Missing Compliance & Security
- NO PII field inventory
- NO data retention policies
- NO deletion cascade documentation
- NO audit trail specification
- NO security practices (Stripe, Xero, Workdrive)

---

## Recommended Approach to Avoid Duplication

**Don't repeat what's already documented:**
- Use LINKS instead of copy-paste
- Assume reader knows individual modules
- Focus on CONNECTIONS between modules
- Use tables for field mappings instead of paragraphs

**Example:**
```markdown
# Field Propagation: Courses to Registrations

When a registration is created, these course fields propagate:

| Course Field | Registration Field | Trigger |
|------|------|--------|
| Course_Start_Time | Start_Date | On create |
| Select_Venue | Venue | On create |

For complete registration details, see:
- [registration-records-readme.md](../registration_records/docs/registration-records-readme.md)
- [registration-kanban-usage.md](../registration_records/docs/registration-kanban-usage.md)
```

---

## Full Report

For complete analysis with line numbers, file paths, and evidence, see:
- `/docs/DOCUMENTATION_EXPLORATION_REPORT.md` (34 KB, 750+ lines)

This roadmap is the quick reference. The full report contains:
- Detailed gap analysis with line numbers
- Complete directory structure recommendations
- Specific data extraction instructions
- Field-by-field breakdown of what's missing
- Security & compliance requirements

---

**Next Step:** Start with Phase 1 (Courses module completion) before building cross-module data flow documentation.

