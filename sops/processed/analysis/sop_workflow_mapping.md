# SOP to Workflow Mapping

**Purpose:** Master mapping of SOP steps to CRM workflow IDs
**Generated:** 2025-11-19
**Status:** Phase 3 Complete

---

## Mapping Legend

| Status | Symbol | Meaning |
|--------|--------|---------|
| ALIGNED | ✅ | SOP step matches CRM automation |
| PARTIAL | ⚠️ | Automation exists but SOP incomplete |
| CONTRADICTS | ❌ | SOP says X, CRM does Y |
| MISSING | 🔴 | Manual step needs automation |
| UNDOCUMENTED | 🟡 | CRM automation not in SOP |

---

## SOP 1: Public Invoice

**Source:** `SOPs/raw_sops/public_invoice_sop.md`
**Primary Modules:** Deals, Quotes, Invoices

### Step-by-Step Mapping

| Step | SOP Action | Module | Workflow ID | Workflow Name | Trigger | Status | Notes |
|------|------------|--------|-------------|---------------|---------|--------|-------|
| 1.1 | Navigate to Deal | Deals | - | - | - | 🔴 MISSING | No navigation aid |
| 1.2 | Set stage to "Ready to Quote" | Deals | 52330000002460308 | Create Quote - Stage Update | field_update (Stage) | ✅ ALIGNED | Quote auto-creates |
| 1.3 | Refresh screen | Deals | - | - | - | ⚠️ PARTIAL | Auto-creation not explained |
| 2.1 | Open newly created Quote | Quotes | - | - | - | 🔴 MISSING | No link to Quotes module |
| 2.2 | Type "Public" in title (optional) | Quotes | 52330000002856364 | Update Quote Naming convention | create_or_edit | 🟡 UNDOCUMENTED | System may override manual title |
| 2.3 | Review student details | Quotes | - | - | - | 🔴 MISSING | No validation workflow |
| 3.1 | Click Convert > Convert to Invoice | Quotes | 52330000002460325 | Update Deal and Invoice on Quote Closed Won | field_update (Quote_Stage) | ❌ CONTRADICTS | Invoice auto-creates on Quote_Stage=Closed Won, not via Convert button |
| 3.2 | Add Invoice Date | Invoices | - | - | - | ⚠️ PARTIAL | Date may auto-populate |
| 3.3 | Due Date auto-fills | Invoices | 52330000005069739 | Update Due Date | create | ✅ ALIGNED | Uses Payment_term_in_days |
| 3.4 | Leave as Draft | Invoices | - | - | - | 🔴 MISSING | No draft validation |
| 4.1 | Click Send Email | Invoices | 52330000004534311 | Send Invoice | field_update (Status) | ❌ CONTRADICTS | SOP says click button, CRM uses Status field change |
| 4.2 | Choose Public Invoice Template | Invoices | - | - | - | 🔴 MISSING | Template selection not automated |
| 4.3 | Click Next and Send | Invoices | - | - | - | ⚠️ PARTIAL | Workflow handles send on Status change |

### Undocumented Workflows Affecting This SOP

| Workflow ID | Name | Action | Impact |
|-------------|------|--------|--------|
| 52330000002597194 | Update Quote Details | Populates Quote_CRM_ID, Deal_ID, Course_ID | Quote fields auto-populated |
| 52330000004975235 | Inhouse - Calculate Overall Tax for Quote | Calculates GST fields | Tax auto-calculated |
| 52330000008512961 | Update All Fields (Invoice) | Populates Invoice_CRM_ID, URLs | Invoice fields auto-populated |
| 52330000004975124 | Inhouse - Calculate Overall Tax for Invoice | Calculates GST fields | Tax auto-calculated |

### Coverage Summary

| Category | Count |
|----------|-------|
| Total SOP Steps | 13 |
| ✅ ALIGNED | 2 |
| ⚠️ PARTIAL | 3 |
| ❌ CONTRADICTS | 2 |
| 🔴 MISSING | 5 |
| 🟡 UNDOCUMENTED | 1 |
| **Coverage** | **15%** |

---

## SOP 2: Private Attendee in Public Course Invoicing

**Source:** `SOPs/raw_sops/private_attendee_invoicing_sop.md`
**Primary Modules:** Courses, Deals, Registration Records, Invoices

### Step-by-Step Mapping

| Step | SOP Action | Module | Workflow ID | Workflow Name | Trigger | Status | Notes |
|------|------------|--------|-------------|---------------|---------|--------|-------|
| 1.1 | Navigate to course in CRM | Courses | - | - | - | 🔴 MISSING | No navigation aid |
| 1.2 | Check if student registered | Courses | - | - | - | 🔴 MISSING | No validation workflow |
| 1.3 | Check if Deal created | Deals | - | - | - | 🔴 MISSING | No validation workflow |
| 1.4 | If not, follow Registration SOP | - | - | - | - | 🔴 MISSING | No automated redirect |
| 2.1 | Find Deal for private student | Deals | - | - | - | 🔴 MISSING | No search aid |
| 2.2 | Ensure Deal linked to course/student | Deals | 52330000005069264 | When Account name is not blank | field_update | ⚠️ PARTIAL | Account propagation only |
| 2.3 | Verify billing details | Deals | - | - | - | 🔴 MISSING | No validation workflow |
| 3.1 | Open invoice for Deal | Invoices | - | - | - | 🔴 MISSING | No navigation aid |
| 3.2 | Review items, pricing, tax | Invoices | 52330000004975124 | Inhouse - Calculate Overall Tax | create_or_edit | 🟡 UNDOCUMENTED | Tax auto-calculated |
| 3.3 | Adjust course fees | Invoices | - | - | - | 🔴 MISSING | No pricing workflow |
| 4.1 | Use appropriate email template | Invoices | 52330000004534311 | Send Invoice | field_update (Status) | ⚠️ PARTIAL | Sends on Status change, not template selection |
| 4.2 | Confirm recipient email | Invoices | - | - | - | 🔴 MISSING | No validation |
| 4.3 | Send invoice | Invoices | 52330000004534311 | Send Invoice | field_update (Status) | ✅ ALIGNED | Sends when Status = Sent |
| 4.4 | Note special payment terms | Invoices | - | - | - | 🔴 MISSING | No notes workflow |

### Undocumented Workflows Affecting This SOP

| Workflow ID | Name | Action | Impact |
|-------------|------|--------|--------|
| 52330000004251591 | New - Update deal and Reg record | Updates Deal and Registration Records | Cross-module sync |
| 52330000009085784 | Update Amount in Deal when Inv is paid | Updates Deal.Amount | Amount sync on payment |

### Coverage Summary

| Category | Count |
|----------|-------|
| Total SOP Steps | 14 |
| ✅ ALIGNED | 1 |
| ⚠️ PARTIAL | 2 |
| ❌ CONTRADICTS | 0 |
| 🔴 MISSING | 10 |
| 🟡 UNDOCUMENTED | 1 |
| **Coverage** | **7%** |

---

## SOP 3: Deal Pipeline Management

**Source:** `SOPs/raw_sops/deal_pipeline_management.md`
**Primary Modules:** Deals

### Step-by-Step Mapping

| Step | SOP Action | Module | Workflow ID | Workflow Name | Trigger | Status | Notes |
|------|------------|--------|-------------|---------------|---------|--------|-------|
| 1.1 | Understand Main/Sub Deals | Deals | - | - | - | 🔴 MISSING | No Deal type field/workflow |
| 2.1 | Create Sub Deals under Main Deal | Deals | - | - | - | 🔴 MISSING | No hierarchy workflow |
| 2.2 | Populate Deal Name | Deals | 52330000002967279 | Deal Naming Convention | create | ❌ CONTRADICTS | SOP says manual, CRM auto-names |
| 2.3 | Populate Course/Service Type | Deals | - | - | - | 🔴 MISSING | No validation |
| 2.4 | Populate Location | Deals | - | - | - | 🔴 MISSING | No validation |
| 2.5 | Populate Start Date | Deals | - | - | - | 🔴 MISSING | No validation |
| 3.1 | Move to New stage | Deals | - | - | - | ❌ CONTRADICTS | CRM uses "Qualification" not "New" |
| 3.2 | Move to Ready to Quote | Deals | 52330000002460308 | Create Quote - Stage Update | field_update (Stage) | ✅ ALIGNED | Quote auto-creates |
| 3.3 | Move to Quoted | Deals | - | - | - | ❌ CONTRADICTS | CRM uses "Negotiation/Review" not "Quoted" |
| 3.4 | Move to Won | Deals | 52330000002460283 | Purchase Order Received | field_update (PO#) | ⚠️ PARTIAL | Won triggered by PO, not stage change |
| 3.5 | Move to Lost | Deals | - | - | - | 🔴 MISSING | No automation on Lost |
| 4.1 | Regularly review open Deals | Deals | - | - | - | 🔴 MISSING | No review reminder |
| 4.2 | Ensure stages current | Deals | - | - | - | 🔴 MISSING | No validation |
| 4.3 | Check for duplicates | Deals | - | - | - | 🔴 MISSING | No deduplication |
| 4.4 | Update Closed Deals promptly | Deals | - | - | - | 🔴 MISSING | No prompt workflow |

### Undocumented Workflows Affecting This SOP

| Workflow ID | Name | Action | Impact |
|-------------|------|--------|--------|
| 52330000002444572 | Update Deal ID | Assigns Deal_ID | Auto-ID on create |
| 52330000003995130 | Update Amount on create | Calculates amount | Auto-amount |
| 52330000004013962 | Copy of Deal Naming Convention | Updates name on Course change | Name may change |
| 52330000002638311 | 28 days before PO reminder | Creates task | PO chase automation |
| 52330000002638269 | 14 days before PO reminder | Creates task | PO chase automation |
| 52330000009085891 | 5 days before PO reminder | Creates task | PO chase automation |
| 52330000002638411 | 1 day before PO reminder | Creates task | PO chase automation |
| 52330000004335567 | On stage Update related Attendees | Updates Registration status | Cross-module sync |
| 52330000006993545 | Update Registration records when PO received | Updates registrations | Cross-module sync |
| 52330000002967852 | Email to training Coordinator | Sends attendee request | Coordinator workflow |
| 52330000002460147 | Create Team Task from Deals | Creates task | Manual task trigger |

### Critical Stage Name Mismatches

| SOP Stage | CRM Stage | Impact |
|-----------|-----------|--------|
| New | Qualification | Users will not find "New" stage |
| Qualified | Negotiation/Review | Users will not find "Qualified" stage |
| Quoted | (no equivalent) | No tracking of quote sent |
| Won/Lost | Closed Won/Closed Lost | Partial match |

### Coverage Summary

| Category | Count |
|----------|-------|
| Total SOP Steps | 15 |
| ✅ ALIGNED | 1 |
| ⚠️ PARTIAL | 1 |
| ❌ CONTRADICTS | 3 |
| 🔴 MISSING | 10 |
| 🟡 UNDOCUMENTED | 0 |
| **Coverage** | **7%** |

---

## SOP 4: Quoting Process - Private Student in Public Course

**Source:** `SOPs/raw_sops/quoting_process_private_student.md`
**Primary Modules:** Courses, Contacts, Registration Records, Deals, Quotes

### Step-by-Step Mapping

| Step | SOP Action | Module | Workflow ID | Workflow Name | Trigger | Status | Notes |
|------|------------|--------|-------------|---------------|---------|--------|-------|
| 1.1 | Navigate to course in CRM | Courses | - | - | - | 🔴 MISSING | No navigation aid |
| 1.2 | Confirm course details | Courses | - | - | - | 🔴 MISSING | No validation workflow |
| 2.1 | Add student as private attendee | Registration | 52330000002518044 | Calculate Registrations and create team task | create | 🟡 UNDOCUMENTED | Task auto-created on registration |
| 2.2 | Ensure contact details correct | Contacts | - | - | - | 🔴 MISSING | No validation |
| 2.3 | Ensure billing details correct | Contacts | - | - | - | 🔴 MISSING | No validation |
| 3.1 | Create Deal from course record | Deals | 52330000002444572 | Update Deal ID | create | 🟡 UNDOCUMENTED | ID auto-assigned |
| 3.2 | Use student name and course details | Deals | 52330000002967279 | Deal Naming Convention | create | 🟡 UNDOCUMENTED | Name auto-generated |
| 3.3 | Set stage to Ready to Quote | Deals | 52330000002460308 | Create Quote - Stage Update | field_update (Stage) | ✅ ALIGNED | Quote auto-creates |
| 3.4 | Refresh page | Deals | - | - | - | ⚠️ PARTIAL | Not explained why |
| 4.1 | Open Quote | Quotes | - | - | - | 🔴 MISSING | No navigation aid |
| 4.2 | Check pricing | Quotes | 52330000004975235 | Inhouse - Calculate Tax | create_or_edit | 🟡 UNDOCUMENTED | Tax auto-calculated |
| 4.3 | Check course details | Quotes | 52330000002597194 | Update Quote Details | create | 🟡 UNDOCUMENTED | Details auto-populated |
| 4.4 | Check student information | Quotes | - | - | - | 🔴 MISSING | No validation |
| 4.5 | Send Quote | Quotes | 52330000006984913 | Send Quote | field_update (Send_Quote_as_EMAIL) | ⚠️ PARTIAL | Uses field trigger not button |
| 4.6 | Use appropriate template | Quotes | - | - | - | 🔴 MISSING | Template not automated |

### Undocumented Workflows Affecting This SOP

| Workflow ID | Name | Action | Impact |
|-------------|------|--------|--------|
| 52330000002856364 | Update Quote Naming convention | Sets Subject field | Name auto-generated |
| 52330000003995201 | Update quote when sent or won | Sets Quote_Sent_Date | Date tracking |
| 52330000005138075 | Workdrive Folder Creation (Reg) | Creates document folder | Auto-folder on registration |
| 52330000005163090 | Private Attendee - Spot Tentative | Confirms private booking | Private handling |

### Coverage Summary

| Category | Count |
|----------|-------|
| Total SOP Steps | 15 |
| ✅ ALIGNED | 1 |
| ⚠️ PARTIAL | 2 |
| ❌ CONTRADICTS | 0 |
| 🔴 MISSING | 7 |
| 🟡 UNDOCUMENTED | 5 |
| **Coverage** | **7%** |

---

## SOP 5: Registration Process

**Source:** `SOPs/raw_sops/registration_process.md`
**Primary Modules:** Courses, Deals, Accounts, Contacts

### Step-by-Step Mapping

| Step | SOP Action | Module | Workflow ID | Workflow Name | Trigger | Status | Notes |
|------|------------|--------|-------------|---------------|---------|--------|-------|
| 1.1 | Go to Courses module | Courses | - | - | - | 🔴 MISSING | No navigation aid |
| 1.2 | If tab not visible, find in dropdown | Courses | - | - | - | 🔴 MISSING | UI guidance only |
| 1.3 | Filter by location | Courses | - | - | - | 🔴 MISSING | No filter workflow |
| 1.4 | Filter by month | Courses | - | - | - | 🔴 MISSING | No filter workflow |
| 1.5 | Select correct course | Courses | - | - | - | 🔴 MISSING | No validation |
| 2.1 | Scroll to Deals section | Courses | - | - | - | 🔴 MISSING | UI guidance only |
| 2.2 | Click three dots > New Deal | Deals | - | - | - | 🔴 MISSING | UI guidance only |
| 2.3 | Fill in deal name format | Deals | 52330000002967279 | Deal Naming Convention | create | ❌ CONTRADICTS | SOP says manual format, CRM auto-names |
| 2.4 | Select/create Account | Accounts | 52330000005069264 | When Account name is not blank | field_update | ⚠️ PARTIAL | Propagates but doesn't create |
| 3.1 | Link Contact to Deal | Deals | - | - | - | 🔴 MISSING | No validation |
| 3.2 | Add/confirm Email | Contacts | - | - | - | 🔴 MISSING | No validation |
| 3.3 | Add/confirm Mobile | Contacts | - | - | - | 🔴 MISSING | No validation |
| 3.4 | Add special notes | Deals | - | - | - | 🔴 MISSING | No workflow |
| 4.1 | Save the Deal | Deals | 52330000002444572 | Update Deal ID | create | 🟡 UNDOCUMENTED | ID auto-assigned on save |
| 4.2 | Confirm student in Deals list | Courses | - | - | - | 🔴 MISSING | No confirmation workflow |

### Undocumented Workflows Affecting This SOP

| Workflow ID | Name | Action | Impact |
|-------------|------|--------|--------|
| 52330000003995130 | Update Amount on create | Calculates Deal amount | Auto-amount |
| 52330000005157945 | Deal - From website | Assigns Account for web deals | Web integration |

### Coverage Summary

| Category | Count |
|----------|-------|
| Total SOP Steps | 15 |
| ✅ ALIGNED | 0 |
| ⚠️ PARTIAL | 1 |
| ❌ CONTRADICTS | 1 |
| 🔴 MISSING | 12 |
| 🟡 UNDOCUMENTED | 1 |
| **Coverage** | **0%** |

---

## Combined Coverage Matrix

### Overall Statistics

| SOP | Total Steps | ✅ | ⚠️ | ❌ | 🔴 | 🟡 | Aligned % |
|-----|-------------|-----|-----|-----|-----|-----|-----------|
| Public Invoice | 13 | 2 | 3 | 2 | 5 | 1 | 15% |
| Private Attendee | 14 | 1 | 2 | 0 | 10 | 1 | 7% |
| Deal Pipeline | 15 | 1 | 1 | 3 | 10 | 0 | 7% |
| Quoting Process | 15 | 1 | 2 | 0 | 7 | 5 | 7% |
| Registration | 15 | 0 | 1 | 1 | 12 | 1 | 0% |
| **TOTAL** | **72** | **5** | **9** | **6** | **44** | **8** | **7%** |

### Status Distribution

```
ALIGNED (✅):        5 steps  (7%)
PARTIAL (⚠️):        9 steps  (12%)
CONTRADICTS (❌):    6 steps  (8%)
MISSING (🔴):       44 steps  (61%)
UNDOCUMENTED (🟡):   8 steps  (11%)
```

### Key Findings

#### Critical Contradictions (❌)

1. **Public Invoice Step 3.1** - Convert Quote to Invoice
   - SOP: Click "Convert" > "Convert to Invoice"
   - CRM: Invoice auto-creates when Quote_Stage = "Closed Won"
   - Impact: Users may create duplicate invoices

2. **Public Invoice Step 4.1** - Send Invoice
   - SOP: Click "Send Email" button
   - CRM: Workflow triggers on Status field change
   - Impact: Button bypasses workflow tracking

3. **Deal Pipeline Step 2.2** - Deal Name
   - SOP: Manually fill format "CourseCode + Location + Date + Name"
   - CRM: Workflow 52330000002967279 auto-generates name
   - Impact: Manual entry overwritten by automation

4. **Deal Pipeline Steps 3.1, 3.3** - Stage Names
   - SOP: Uses "New", "Quoted"
   - CRM: Uses "Qualification", "Negotiation/Review"
   - Impact: Users cannot find expected stages

5. **Registration Step 2.3** - Deal Name Format
   - SOP: Manual format required
   - CRM: Auto-naming workflow
   - Impact: Manual entry overwritten

---

## Workflow Quick Reference

### Workflows by Module

#### Deals Module (13 workflows)

| ID | Name | Trigger | Used in SOP |
|----|------|---------|-------------|
| 52330000002444572 | Update Deal ID | create | Registration, Quoting |
| 52330000002967279 | Deal Naming Convention | create | Pipeline, Registration |
| 52330000003995130 | Update Amount on create | create | Pipeline, Registration |
| 52330000002460308 | Create Quote - Stage Update | field_update (Stage) | Public Invoice, Pipeline, Quoting |
| 52330000004013962 | Copy of Deal Naming Convention | field_update (Course) | Pipeline |
| 52330000002967852 | Email to training Coordinator | field_update (Request_Attendees) | Pipeline |
| 52330000002460147 | Create Team Task from Deals | field_update (Create_Follow_up_Task) | Pipeline |
| 52330000005069264 | When Account name is not blank | field_update | Private Attendee, Registration |
| 52330000002460283 | Purchase Order Received | field_update (PO#) | Pipeline |
| 52330000006993545 | Update Registration records when PO | field_update (PO#) | Pipeline |
| 52330000004335567 | On stage Update related Attendees | field_update (Stage) | Pipeline |
| 52330000002638311 | 28 days before PO reminder | date_or_datetime | Pipeline |
| 52330000002638269 | 14 days before PO reminder | date_or_datetime | Pipeline |
| 52330000009085891 | 5 days before PO reminder | field_update (Stage) | Pipeline |
| 52330000002638411 | 1 day before PO reminder | date_or_datetime | Pipeline |

#### Quotes Module (8 workflows)

| ID | Name | Trigger | Used in SOP |
|----|------|---------|-------------|
| 52330000002597194 | Update Quote Details | create | Quoting |
| 52330000002856364 | Update Quote Naming convention | create_or_edit | Public Invoice |
| 52330000004975235 | Inhouse - Calculate Tax | create_or_edit | Public Invoice, Quoting |
| 52330000002460325 | Update Deal and Invoice on Quote Closed Won | field_update (Quote_Stage) | Public Invoice |
| 52330000003995201 | Update quote when sent or won | field_update (Quote_Stage) | Quoting |
| 52330000006984913 | Send Quote | field_update (Send_Quote_as_EMAIL) | Quoting |
| 52330000006993468 | Update Deal with PO Number and Date | field_update (PO fields) | - |

#### Invoices Module (15 workflows)

| ID | Name | Trigger | Used in SOP |
|----|------|---------|-------------|
| 52330000005069739 | Update Due Date | create | Public Invoice |
| 52330000008512961 | Update All Fields | create | Public Invoice |
| 52330000008694463 | Send on create - Awaiting Payment | create | - |
| 52330000004251591 | New - Update deal and Reg record | create_or_edit | Private Attendee |
| 52330000004975124 | Inhouse - Calculate Tax | create_or_edit | Public Invoice, Private Attendee |
| 52330000002460196 | Paid in Crez | field_update (Paid_In_CREZ) | - |
| 52330000002460231 | Push Invoice to Xero | field_update (Status) | - |
| 52330000002610986 | Invoice Update | field_update (Status) | - |
| 52330000004534311 | Send Invoice | field_update (Status) | Public Invoice, Private Attendee |
| 52330000005069778 | When Po is received | field_update (PO#, Status) | - |
| 52330000008519048 | Update URL | field_update (Course, Amount, Deal) | - |
| 52330000008776519 | Refresh Payment URL | field_update (Refresh_PO_URL) | - |
| 52330000009085784 | Update Amount in Deal when paid | field_update (Status) | Private Attendee |

#### Registration Records Module (key workflows)

| ID | Name | Trigger | Used in SOP |
|----|------|---------|-------------|
| 52330000002518044 | Calculate Registrations and create team task | create | Quoting |
| 52330000005138075 | Workdrive Folder Creation | create | Quoting |
| 52330000005163090 | Private Attendee - Spot Tentative | create | Quoting |

---

## Phase 4 Input Summary

This mapping provides:

1. **6 critical contradictions** requiring SOP revision
2. **44 missing automation gaps** for potential new workflows
3. **8 undocumented automations** to add to SOPs
4. **Workflow ID reference** for all 5 SOPs

---

**Next Phase:** Phase 4 - Gap Analysis Report
