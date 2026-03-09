# Missing Automations

**Purpose:** Document manual SOP steps that could benefit from automation
**Generated:** 2025-11-19
**Total Missing:** 44 steps across 5 SOPs

---

## Summary by Priority

| Priority | Count | Description |
|----------|-------|-------------|
| HIGH | 12 | Frequently used steps causing significant manual burden |
| MEDIUM | 18 | Useful automation opportunities |
| LOW | 14 | Nice-to-have or UI guidance only |

---

## HIGH Priority Recommendations

### AUTO-001: Navigation Quick Links

**Affected SOPs:** All 5
**Steps:** 8 navigation steps
**Current State:** Users must manually navigate to modules and search for records

**Recommendation:**

```
Name: Quick Navigation Widget
Type: Custom Button / Zoho Creator Widget
Location: Home page dashboard

Features:
- Recent Deals (last 10)
- Recent Quotes (last 10)
- Recent Invoices (last 10)
- Quick filters by Account, Course, Date
- Direct links to create new records
```

**Business Case:**
- 8 steps across all SOPs require manual navigation
- Average 30 seconds per search = 4+ minutes per complete SOP execution
- High frequency: performed multiple times daily

**Estimated Impact:** Reduce navigation time by 75%

---

### AUTO-002: Deal Data Validation

**Affected SOPs:** Public Invoice, Quoting Process
**Steps:** 4 validation steps
**Current State:** Users manually verify required fields before quote generation

**Recommendation:**

```
Name: Validate Deal Before Quote
Workflow ID: (new)
Trigger: Stage update to "Ready to Quote"
Conditions: Check required fields populated

Validation Rules:
- Contact_Name is not empty
- Account_Name is not empty (if B2B)
- Courseaa is not empty
- Number_of_Attendees > 0
- Course_Start_Date is not empty

Actions:
- If valid: Allow stage change, proceed with quote creation
- If invalid: Alert user with list of missing fields, block stage change
```

**Business Case:**
- Quotes created with missing data cause downstream errors
- Manual review takes 2-3 minutes per Deal
- Errors discovered later require rework

**Estimated Impact:** Reduce quote errors by 80%

---

### AUTO-003: Registration Existence Check

**Affected SOPs:** Private Attendee Invoicing
**Steps:** 2 (1.2, 1.4)
**Current State:** Users manually check if registration exists before invoicing

**Recommendation:**

```
Name: Check Registration Before Invoice
Workflow ID: (new)
Trigger: Invoice creation from Deal
Conditions: Check for Registration Record

Validation:
- Query Registration_Records where Course = Deal.Courseaa AND Attendee = Deal.Contact_Name
- Check Status is not "Cancelled"

Actions:
- If exists: Proceed with invoice
- If not exists: Alert "No registration found for this student. Complete registration first."
```

**Business Case:**
- Invoicing without registration causes compliance issues
- Manual check requires navigating to Course, reviewing related lists
- Errors caught late require invoice cancellation

**Estimated Impact:** Eliminate registration-invoice mismatch errors

---

### AUTO-004: Template Auto-Selection

**Affected SOPs:** Public Invoice, Private Attendee, Quoting Process
**Steps:** 3 (template selection steps)
**Current State:** Workflow uses single template; users cannot select per invoice

**Recommendation:**

```
Name: Auto-Select Email Template
Workflow ID: (new or modify existing)
Trigger: Invoice/Quote Status = "Sent"
Conditions: Check Course_Type or Account_Type

Template Selection Logic:
- If Course_Type = "Public" → Use "Public Invoice Template"
- If Course_Type = "Private" → Use "Private Invoice Template"
- If Account_Type = "Government" → Use "Government Invoice Template"
- Default → Use "Standard Invoice Template"

Implementation:
- Add Email_Template lookup field to Invoice
- Modify Send Invoice workflow (52330000004534311) to use dynamic template
```

**Business Case:**
- Different customer types require different email content
- Currently one-size-fits-all template
- Users cannot customize without bypassing workflow

**Estimated Impact:** Improve customer communication quality

---

### AUTO-005: Quote-to-Registration Link

**Affected SOPs:** Quoting Process
**Steps:** 2 (verification steps)
**Current State:** No automatic link between Quote and Registration Record

**Recommendation:**

```
Name: Link Quote to Registration
Workflow ID: (new)
Trigger: Quote creation (existing WF 52330000002460308)
Additional Action: Update Registration Record

Process:
1. When Quote created from Deal
2. Find Registration where Course = Deal.Courseaa AND Attendee = Deal.Contact
3. Set Registration.Quote = new Quote ID
4. Set Registration.Deal = Deal ID

Benefits:
- Complete audit trail from registration to payment
- Easy navigation between related records
- Better reporting on registration-to-invoice conversion
```

**Business Case:**
- Currently no link between Registration and Quote
- Users must manually track relationships
- Reporting requires manual data matching

**Estimated Impact:** Improve data integrity and reporting

---

### AUTO-006: Duplicate Deal Detection

**Affected SOPs:** Deal Pipeline Management
**Step:** 4.3
**Current State:** Users manually check for duplicate Deals

**Recommendation:**

```
Name: Duplicate Deal Alert
Workflow ID: (new)
Trigger: Deal creation
Conditions: Check for existing Deal with same Account + Course + Contact

Detection Logic:
- Query Deals where:
  - Account_Name = new Deal.Account_Name
  - Courseaa = new Deal.Courseaa
  - Contact_Name = new Deal.Contact_Name
  - Stage not in (Closed Won, Closed Lost)

Actions:
- If duplicate found:
  - Alert user: "Possible duplicate. Existing Deal: [Deal_Name] in stage [Stage]"
  - Provide link to existing Deal
  - Allow user to proceed or cancel
```

**Business Case:**
- Duplicate Deals cause double-billing risk
- Manual deduplication is time-consuming
- Currently no systematic detection

**Estimated Impact:** Prevent duplicate billing errors

---

## MEDIUM Priority Recommendations

### AUTO-007: Pipeline Review Reminder

**Affected SOPs:** Deal Pipeline Management
**Step:** 4.1
**Current State:** No reminder to review open Deals

```
Name: Weekly Pipeline Review Task
Trigger: Scheduled (every Monday 9:00 AM)
Conditions: Deals in active stages > 14 days without update

Actions:
- Create Team Task for Sales Manager
- Subject: "Pipeline Review: X deals need attention"
- Include list of stale Deals
```

---

### AUTO-008: Invoice Price Adjustment Tracking

**Affected SOPs:** Private Attendee Invoicing
**Step:** 3.3
**Current State:** No audit trail for fee adjustments

```
Name: Track Price Adjustments
Fields to Add:
- Original_Amount (auto-set on create)
- Adjustment_Amount (calculated)
- Adjustment_Reason (picklist)

Workflow:
- On create: Set Original_Amount = Grand_Total
- On edit: If Grand_Total changed, require Adjustment_Reason
```

---

### AUTO-009: Payment Term Notes Field

**Affected SOPs:** Private Attendee Invoicing
**Step:** 4.4
**Current State:** No dedicated field for special payment terms

```
Fields to Add:
- Payment_Terms_Notes (text area)
- Non_Standard_Terms (checkbox)

Workflow:
- If Non_Standard_Terms = true, require Payment_Terms_Notes
- Include notes in invoice email
```

---

### AUTO-010: Contact Validation

**Affected SOPs:** Registration, Quoting Process
**Steps:** 4 (email/mobile verification)
**Current State:** Users manually check Contact has required fields

```
Name: Validate Contact for Registration
Trigger: Registration Record creation
Conditions: Check Contact fields

Validation:
- Email is not empty
- Mobile is not empty (for SMS notifications)

Actions:
- If invalid: Alert "Contact missing required fields: [list]"
```

---

### AUTO-011: Quote Expiry Reminder

**Affected SOPs:** Quoting Process
**Current State:** No reminder when quotes are about to expire

```
Name: Quote Expiry Reminder
Trigger: 3 days before Valid_Till date
Conditions: Quote_Stage = "Sent"

Actions:
- Create Task for Deal Owner
- Subject: "Quote expiring soon: [Quote_Name]"
- Send email reminder to client (optional)
```

---

### AUTO-012: Deal-to-Registration Auto-Create

**Affected SOPs:** Registration Process
**Current State:** Creating Deal doesn't create Registration Record

```
Name: Auto-Create Registration from Deal
Trigger: Deal creation from Course
Optional Action: Also create Registration Record

Process:
- When Deal created with Courseaa and Contact_Name
- Auto-create Registration Record with:
  - Course = Deal.Courseaa
  - Attendee = Deal.Contact_Name
  - Status = "Spot Tentative"
  - Related_Deal = Deal.ID
```

---

## LOW Priority Recommendations

### AUTO-013 to AUTO-019: UI Guidance Items

These steps are pure UI navigation that cannot be automated but could be improved with:

- In-app tooltips
- Walkthrough tours for new users
- Quick reference cards

| ID | Step | Description |
|----|------|-------------|
| AUTO-013 | Reg 1.2 | Find Courses in dropdown menu |
| AUTO-014 | Reg 2.1 | Scroll to Deals section |
| AUTO-015 | Reg 2.2 | Click three dots menu |
| AUTO-016 | Reg 1.3-1.4 | Filter by location/month |
| AUTO-017 | Public 2.1 | Navigate to Quotes module |
| AUTO-018 | Private 3.1 | Open Invoice from Deal |
| AUTO-019 | Quoting 4.1 | Open Quote |

### AUTO-020: Optional Title Enhancement

**Step:** Public Invoice 2.2
**Current State:** Optional "Public" in Quote title may be overwritten

```
Not recommended for automation - workflow naming convention is preferred.
Update SOP to explain this is optional and may be overwritten.
```

---

## Implementation Roadmap

### Phase 1: Quick Wins (Week 1-2)

| ID | Name | Effort | Impact |
|----|------|--------|--------|
| AUTO-002 | Deal Data Validation | Low | High |
| AUTO-003 | Registration Check | Low | High |
| AUTO-010 | Contact Validation | Low | Medium |

### Phase 2: Core Automations (Week 3-4)

| ID | Name | Effort | Impact |
|----|------|--------|--------|
| AUTO-004 | Template Auto-Selection | Medium | High |
| AUTO-006 | Duplicate Detection | Medium | High |
| AUTO-005 | Quote-Registration Link | Medium | Medium |

### Phase 3: Enhancements (Month 2)

| ID | Name | Effort | Impact |
|----|------|--------|--------|
| AUTO-001 | Navigation Widget | High | High |
| AUTO-007 | Pipeline Review | Low | Medium |
| AUTO-011 | Quote Expiry | Low | Medium |

### Phase 4: Advanced (Quarter 2)

| ID | Name | Effort | Impact |
|----|------|--------|--------|
| AUTO-008 | Price Adjustment Tracking | Medium | Medium |
| AUTO-009 | Payment Term Notes | Low | Low |
| AUTO-012 | Auto-Create Registration | Medium | Medium |

---

## Estimated Coverage Improvement

### Current State
- Total manual steps: 44
- Overall coverage: 31%

### After Phase 1
- Manual steps reduced to: 38
- Coverage increase: +8%

### After Phase 2
- Manual steps reduced to: 30
- Coverage increase: +14%

### After All Phases
- Manual steps reduced to: 18
- Target coverage: 67%

---

## Related Documents

- [Gap Analysis Report](../analysis/gap_analysis_report.md)
- [Automation Coverage Matrix](../analysis/automation_coverage_matrix.md)
- [SOP Update Recommendations](sop_update_recommendations.md)
