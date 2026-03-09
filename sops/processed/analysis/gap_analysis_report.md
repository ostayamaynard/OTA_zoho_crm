# Gap Analysis Report

**Purpose:** Comprehensive analysis of gaps between SOPs and CRM workflows
**Generated:** 2025-11-19
**Status:** Phase 4 Complete

---

## Executive Summary

Analysis of 5 SOPs against 133+ CRM workflows reveals significant misalignment between documented procedures and actual system behavior. Only **7% of SOP steps** are fully aligned with CRM automations.

### Overall Gap Statistics

| Gap Type | Count | Percentage |
|----------|-------|------------|
| ✅ ALIGNED | 5 | 7% |
| ⚠️ PARTIAL | 9 | 12% |
| ❌ CONTRADICTS | 6 | 8% |
| 🔴 MISSING | 44 | 61% |
| 🟡 UNDOCUMENTED | 8 | 11% |
| **Total Steps** | **72** | **100%** |

### Risk Assessment

- **Critical Issues:** 6 contradictions that cause user errors
- **High Impact:** 44 missing automations reducing efficiency
- **Medium Impact:** 8 undocumented automations causing confusion
- **Low Impact:** 9 partial alignments needing clarification

---

## Section 1: Critical Contradictions (❌)

### Severity: CRITICAL
These contradictions will cause users to perform incorrect actions or create duplicate records.

---

### GAP-001: Invoice Creation Method

**Severity:** CRITICAL
**SOP:** Public Invoice, Step 3.1
**Source:** `SOPs/raw_sops/public_invoice_sop.md`

#### Contradiction

| What SOP Says | What CRM Does |
|---------------|---------------|
| "Click 'Convert' > 'Convert to Invoice'" | Invoice auto-creates when Quote_Stage = "Closed Won" |

#### CRM Workflow Reference

- **Workflow:** Update Deal and Invoice on Quote Closed Won
- **ID:** 52330000002460325
- **Source:** `modules/quotes/docs/quotes-workflows.md:104-122`
- **Trigger:** Quote_Stage field update to "Closed Won"

#### Impact

1. **Duplicate invoices** - Users create manual invoice, then automation creates another
2. **Missing fields** - Manual conversion bypasses workflow that sets Quote_Won_Date, updates Deal stage
3. **Reporting errors** - Invoice count inflated, revenue double-counted

#### Resolution

**Update SOP to read:**
```
Step 3: Mark Quote as Accepted
- In the Quote record, change Quote_Stage to "Closed Won"
- The system will automatically:
  - Create an Invoice record
  - Update the Deal stage to Closed Won
  - Set the Quote_Won_Date
- Go to Invoices module to find the new invoice
```

---

### GAP-002: Invoice Send Method

**Severity:** HIGH
**SOP:** Public Invoice, Step 4.1
**Source:** `SOPs/raw_sops/public_invoice_sop.md`

#### Contradiction

| What SOP Says | What CRM Does |
|---------------|---------------|
| "Click on 'Send Email' from within the invoice page" | Invoice sends when Status field changed to "Sent" |

#### CRM Workflow Reference

- **Workflow:** Send Invoice
- **ID:** 52330000004534311
- **Source:** `modules/invoices/docs/invoices-workflows.md:220-236`
- **Trigger:** Status field update

#### Impact

1. **Workflow bypass** - Clicking button may not trigger workflow
2. **Missing tracking** - Invoice_Sent_Date not populated
3. **Xero sync issues** - Status-based sync may not fire

#### Resolution

**Update SOP to read:**
```
Step 4: Send Invoice
- Change the Status field to "Sent"
- The system will automatically:
  - Send the invoice email using the configured template
  - Set Invoice_Sent_Date
  - Trigger Xero sync if applicable
```

---

### GAP-003: Deal Naming Convention

**Severity:** HIGH
**SOP:** Deal Pipeline Management, Step 2.2 & Registration Process, Step 2.3
**Source:** `SOPs/raw_sops/deal_pipeline_management.md`, `SOPs/raw_sops/registration_process.md`

#### Contradiction

| What SOP Says | What CRM Does |
|---------------|---------------|
| "Fill in deal name format: CourseCode + Location + Date + Student/Company Name" | Workflow auto-generates name using different format |

#### CRM Workflow Reference

- **Workflow:** Deal Naming Convention
- **ID:** 52330000002967279
- **Source:** `modules/deals/docs/sop-workflow-accuracy-report.md:50`
- **Trigger:** Record create
- **Format:** `P - [Company] - [Location] - [Course/Contact]`

#### Impact

1. **User frustration** - Manual entry immediately overwritten
2. **Inconsistent naming** - If workflow fails, manual name persists
3. **Search issues** - Users search for wrong format

#### Resolution

**Update SOPs to read:**
```
Step: Create Deal
- Create a new Deal from the course record
- The Deal Name will auto-populate using format: P - [Company] - [Location] - [Course]
- Verify the auto-generated name is correct
- Do NOT manually enter the Deal Name - it will be overwritten
```

---

### GAP-004: Stage Name "New"

**Severity:** HIGH
**SOP:** Deal Pipeline Management, Step 3.1
**Source:** `SOPs/raw_sops/deal_pipeline_management.md`

#### Contradiction

| What SOP Says | What CRM Does |
|---------------|---------------|
| "Move Sub Deals through stage: New" | CRM has stage "Qualification" (no "New" stage exists) |

#### CRM Stage Reference

- **Source:** `modules/deals/docs/sop-workflow-accuracy-report.md:18-20`
- **Actual stages:** Qualification, Negotiation/Review, Ready to Quote, etc.

#### Impact

1. **Stage not found** - Users cannot find "New" in dropdown
2. **Process confusion** - Users skip to wrong stage
3. **Reporting gaps** - "New" deals not tracked

#### Resolution

**Update SOP to use actual CRM stage names:**
```
Stage Progression:
- Qualification (initial stage, replaces "New")
- Negotiation/Review (replaces "Qualified")
- Ready to Quote
- Awaiting ZipPay Confirmation (if applicable)
- Awaiting Purchase Order
- Awaiting Invoice Payment
- Closed Won / Closed Lost
```

---

### GAP-005: Stage Name "Quoted"

**Severity:** MEDIUM
**SOP:** Deal Pipeline Management, Step 3.3
**Source:** `SOPs/raw_sops/deal_pipeline_management.md`

#### Contradiction

| What SOP Says | What CRM Does |
|---------------|---------------|
| "Move Sub Deals through stage: Quoted" | CRM has no "Quoted" stage; uses "Negotiation/Review" |

#### Impact

1. **Missing tracking** - No way to track "quote sent" status
2. **Process gap** - No stage between Ready to Quote and Won/Lost
3. **Reporting blind spot** - Cannot report on pending quotes

#### Resolution

**Option A - Update SOP:**
```
After sending quote, return Deal to "Negotiation/Review" stage.
Track quote status in Quotes module via Quote_Stage field.
```

**Option B - Add CRM Stage:**
Consider adding "Quote Sent" stage to CRM if business requires tracking.

---

### GAP-006: Quote Closed Won Trigger

**Severity:** MEDIUM
**SOP:** Deal Pipeline Management, Step 3.4
**Source:** `SOPs/raw_sops/deal_pipeline_management.md`

#### Contradiction

| What SOP Says | What CRM Does |
|---------------|---------------|
| "Move to Won" (implies stage change) | Deal moves to Won via Quote_Stage or PO Number, not direct stage change |

#### CRM Workflow Reference

- **Workflow:** Purchase Order Received
- **ID:** 52330000002460283
- **Source:** `modules/deals/docs/deal-kanban-usage.md:376`
- **Trigger:** Purchase_Order_Number field update

#### Impact

1. **Workflow bypass** - Direct stage change misses PO processing
2. **Registration update missed** - Attendees not confirmed
3. **Tracking gaps** - PO_Received_Date not set

#### Resolution

**Update SOP to read:**
```
To Close a Deal as Won:
- Option 1: In Quotes module, set Quote_Stage = "Closed Won"
  (Auto-updates Deal, creates Invoice)
- Option 2: Enter Purchase_Order_Number on Deal
  (Triggers PO workflows, updates registrations)
- Do NOT manually change Deal Stage to Closed Won
```

---

## Section 2: Missing Automations (🔴)

### Severity Ratings

| Severity | Count | Description |
|----------|-------|-------------|
| HIGH | 12 | Frequently used steps needing automation |
| MEDIUM | 18 | Useful automation opportunities |
| LOW | 14 | Nice-to-have or UI guidance |

---

### HIGH Priority Missing Automations

#### MISS-001: Navigation Aids

**Count:** 8 steps across all SOPs
**Steps:** 1.1 in all SOPs, 2.1 in Private Attendee, 3.1 in Private Attendee, 4.1 in Quoting

**Description:** Users must manually navigate to find records with no system assistance.

**Recommendation:**
- Add Quick Links or Recent Records widget
- Implement "Related Records" navigation buttons
- Create keyboard shortcuts for common modules

---

#### MISS-002: Validation Workflows

**Count:** 6 steps
**Steps:** Public Invoice 2.3, Private Attendee 1.2, 1.3, 2.3, 3.2

**Description:** Users must manually validate data accuracy with no system checks.

**Recommendation:**
- Add workflow to validate required fields on stage change
- Create alert for missing Contact/Account links
- Implement data completeness scoring

**Suggested Workflow:**
```
Name: Validate Deal Data Completeness
Trigger: Stage update to "Ready to Quote"
Conditions: Check Contact_Name, Account_Name, Courseaa not empty
Action: Alert user if fields missing, block stage change
```

---

#### MISS-003: Registration SOP Validation

**Count:** 2 steps
**Steps:** Private Attendee 1.2, 1.4

**Description:** No way to check if student is already registered or redirect to Registration SOP.

**Recommendation:**
- Add lookup validation before invoice creation
- Create workflow to check for existing Registration Record
- Implement redirect or alert if registration missing

---

#### MISS-004: Template Selection

**Count:** 2 steps
**Steps:** Public Invoice 4.2, Private Attendee 4.1

**Description:** Users must manually find correct email template.

**Recommendation:**
- Auto-select template based on Course_Type or Account_Type field
- Pre-populate template based on Deal type (Public/Private)

**Suggested Workflow:**
```
Name: Auto-Select Invoice Template
Trigger: Invoice Status = "Sent"
Conditions: Check Course_Type field
Action: Set Email_Template field accordingly
```

---

### MEDIUM Priority Missing Automations

#### MISS-005: Duplicate Detection

**SOP:** Deal Pipeline Management, Step 4.3
**Description:** No automation to detect duplicate Deals for same client/course.

**Recommendation:**
```
Name: Duplicate Deal Alert
Trigger: Deal create
Conditions: Same Account_Name + Courseaa combination exists
Action: Alert user, suggest linking to existing Deal
```

---

#### MISS-006: Pipeline Review Reminders

**SOP:** Deal Pipeline Management, Step 4.1
**Description:** No reminder to review open Deals periodically.

**Recommendation:**
```
Name: Weekly Pipeline Review Task
Trigger: Scheduled (every Monday)
Conditions: Deals in stages > 14 days
Action: Create Team Task for review
```

---

#### MISS-007: Payment Term Notes

**SOP:** Private Attendee, Step 4.4
**Description:** No workflow to capture special payment terms.

**Recommendation:**
- Add Payment_Terms field to Invoice
- Create workflow to alert when non-standard terms used

---

#### MISS-008: Price Adjustment Tracking

**SOP:** Private Attendee, Step 3.3
**Description:** No audit trail for fee adjustments.

**Recommendation:**
- Add Original_Amount and Adjustment_Reason fields
- Create workflow to log adjustments

---

### LOW Priority Missing Automations

| Step | SOP | Description | Recommendation |
|------|-----|-------------|----------------|
| 1.2 | Registration | Tab visibility check | UI training only |
| 2.1 | Registration | Scroll to Deals section | UI training only |
| 2.2 | Registration | Click three dots | UI training only |
| 1.3-1.4 | Registration | Filter options | Document filter usage |
| 3.4 | Registration | Add special notes | Optional enhancement |
| 4.2 | Registration | Confirm in Deals list | Document verification steps |
| 2.2 | Public Invoice | Type "Public" in title | Optional, auto-naming may override |
| 3.4 | Public Invoice | Leave as Draft | Document status behavior |

---

## Section 3: Undocumented Automations (🟡)

These workflows affect SOP processes but are not mentioned in the SOPs.

---

### UNDOC-001: Quote Details Auto-Population

**Workflow:** Update Quote Details
**ID:** 52330000002597194
**Source:** `modules/quotes/docs/quotes-workflows.md:24-38`

**Action:** Populates Quote_CRM_ID, Deal_ID, Course_ID, and other reference fields from linked Deal

**Affects:** Public Invoice Step 2, Quoting Process Step 4

**SOP Update Needed:**
```
Add note: "Quote fields (Course, Contact, Pricing) will auto-populate from the linked Deal"
```

---

### UNDOC-002: Tax Calculation

**Workflow:** Inhouse - Calculate Overall Tax for Quote/Invoice
**IDs:** 52330000004975235 (Quote), 52330000004975124 (Invoice)
**Source:** `modules/quotes/docs/quotes-workflows.md:66-78`, `modules/invoices/docs/invoices-workflows.md:120-135`

**Action:** Calculates GST fields automatically

**Affects:** Public Invoice Step 3, Private Attendee Step 3, Quoting Process Step 4

**SOP Update Needed:**
```
Add note: "Tax (GST) is calculated automatically - do not manually enter tax amounts"
```

---

### UNDOC-003: Deal ID Assignment

**Workflow:** Update Deal ID
**ID:** 52330000002444572
**Source:** `modules/deals/docs/sop-workflow-accuracy-report.md:51`

**Action:** Assigns unique Deal_ID on record creation

**Affects:** Registration Process Step 4, Quoting Process Step 3

**SOP Update Needed:**
```
Add note: "A unique Deal ID will be automatically assigned upon save"
```

---

### UNDOC-004: Deal Amount Calculation

**Workflow:** Update Amount on create
**ID:** 52330000003995130
**Source:** `modules/deals/docs/sop-workflow-accuracy-report.md:52`

**Action:** Calculates Deal amount based on Course and Number_of_Attendees

**Affects:** Registration Process, Quoting Process

**SOP Update Needed:**
```
Add note: "Deal Amount will auto-calculate based on Course pricing and Number_of_Attendees"
```

---

### UNDOC-005: Registration Record Creation

**Workflow:** Calculate Registrations and create team task
**ID:** 52330000002518044
**Source:** `modules/registration_records/docs/registration-kanban-usage.md:40-41`

**Action:** Updates course registration counts, creates follow-up task

**Affects:** Quoting Process Step 2

**SOP Update Needed:**
```
Add note: "When adding an attendee, a Team Task will be automatically created for follow-up"
```

---

### UNDOC-006: Workdrive Folder Creation

**Workflow:** Workdrive Folder Creation
**ID:** 52330000005138075
**Source:** `modules/registration_records/docs/registration-kanban-usage.md:42`

**Action:** Creates document folder for registration

**Affects:** Quoting Process Step 2

**SOP Update Needed:**
```
Add note: "A Workdrive folder will be automatically created for document storage"
```

---

### UNDOC-007: Private Attendee Confirmation

**Workflow:** Private Attendee - Spot Tentative
**ID:** 52330000005163090
**Source:** `modules/registration_records/docs/registration-kanban-usage.md:43`

**Action:** Confirms private booking status

**Affects:** Quoting Process Step 2

**SOP Update Needed:**
```
Add note: "Private attendees are automatically flagged for separate billing"
```

---

### UNDOC-008: Quote Naming Override

**Workflow:** Update Quote Naming convention
**ID:** 52330000002856364
**Source:** `modules/quotes/docs/quotes-workflows.md:44-59`

**Action:** Sets Subject field using naming convention

**Affects:** Public Invoice Step 2.2

**SOP Update Needed:**
```
Update note: "The Quote Subject will auto-populate. Adding 'Public' to the title is optional
but may be overwritten by the naming convention workflow on next edit."
```

---

## Section 4: Partial Alignments (⚠️)

These steps have automation support but SOP descriptions are incomplete.

| Step | SOP | Issue | Resolution |
|------|-----|-------|------------|
| 1.3 | Public Invoice | "Refresh screen" not explained | Add: "Quote appears in Quotes module after refresh" |
| 3.2 | Public Invoice | Invoice Date may auto-populate | Clarify: "Invoice Date defaults to today if left blank" |
| 4.3 | Public Invoice | Workflow handles send | Align with Status field trigger method |
| 2.2 | Private Attendee | Account propagation only | Add: "Account details will sync to related records" |
| 4.1 | Private Attendee | Uses Status field trigger | Update to describe field-based sending |
| 3.4 | Deal Pipeline | Won triggered by PO | Describe PO-based closure method |
| 2.4 | Registration | Account propagation only | Clarify: "Select existing Account or create new" |
| 3.4 | Quoting | "Refresh" not explained | Add: "Quote record will appear in Quotes module" |
| 4.5 | Quoting | Uses field trigger | Update: "Set Send_Quote_as_EMAIL = true to send" |

---

## Section 5: Priority Matrix

### Immediate Action Required (Week 1)

| ID | Type | Description | Impact |
|----|------|-------------|--------|
| GAP-001 | ❌ | Invoice creation method | Duplicate invoices |
| GAP-003 | ❌ | Deal naming convention | User frustration |
| GAP-004 | ❌ | Stage name "New" | Cannot find stage |

### Short-Term (Week 2-3)

| ID | Type | Description | Impact |
|----|------|-------------|--------|
| GAP-002 | ❌ | Invoice send method | Workflow bypass |
| GAP-005 | ❌ | Stage name "Quoted" | Missing tracking |
| GAP-006 | ❌ | Quote Closed Won trigger | Registration miss |
| UNDOC-001-008 | 🟡 | All undocumented | User confusion |

### Medium-Term (Month 1)

| ID | Type | Description | Impact |
|----|------|-------------|--------|
| MISS-002 | 🔴 | Validation workflows | Data quality |
| MISS-003 | 🔴 | Registration validation | Process errors |
| MISS-004 | 🔴 | Template selection | Efficiency |

### Long-Term (Quarter 1)

| ID | Type | Description | Impact |
|----|------|-------------|--------|
| MISS-005 | 🔴 | Duplicate detection | Data quality |
| MISS-006 | 🔴 | Pipeline review | Process discipline |
| MISS-001 | 🔴 | Navigation aids | User experience |

---

## Section 6: Metrics & KPIs

### Current State

| Metric | Value |
|--------|-------|
| SOP-CRM Alignment | 7% |
| Critical Contradictions | 6 |
| Missing Automations | 44 |
| Undocumented Features | 8 |

### Target State (After Remediation)

| Metric | Target |
|--------|--------|
| SOP-CRM Alignment | 80%+ |
| Critical Contradictions | 0 |
| Missing Automations | <10 (highest priority only) |
| Undocumented Features | 0 |

### Success Criteria

1. All 6 contradictions resolved in SOP updates
2. All 8 undocumented automations added to SOPs
3. Top 5 missing automations implemented or documented as manual
4. User error rate reduced by 50%

---

## Appendix: Source File References

### SOPs Analyzed

- `SOPs/raw_sops/public_invoice_sop.md`
- `SOPs/raw_sops/private_attendee_invoicing_sop.md`
- `SOPs/raw_sops/deal_pipeline_management.md`
- `SOPs/raw_sops/quoting_process_private_student.md`
- `SOPs/raw_sops/registration_process.md`

### CRM Source Documentation

- `modules/deals/docs/deal-kanban-usage.md`
- `modules/deals/docs/sop-workflow-accuracy-report.md`
- `modules/quotes/docs/quotes-workflows.md`
- `modules/invoices/docs/invoices-workflows.md`
- `modules/registration_records/docs/registration-kanban-usage.md`

### Workflow URL Pattern

All workflow URLs follow: `https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/{WORKFLOW_ID}`

---

**Next Phase:** Phase 5 - Automation Coverage Matrix
