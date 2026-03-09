# SOP Extraction & Classification

**Purpose:** Internal working document for Phase 3 mapping
**Generated:** 2025-11-19
**Status:** Phase 2 Complete

---

## Classification Legend

| Symbol | Type | Description |
|--------|------|-------------|
| 👤 | Manual Action | User must perform this action |
| 🔀 | Decision Point | Conditional/branching logic |
| ✏️ | Manual Input | Data entry required |
| ⚠️ | Assumption | Implicit prerequisite |
| 📦 | Module | CRM module touched |

---

## SOP 1: Public Invoice

**Source:** `SOPs/raw_sops/public_invoice_sop.md`

### Step 1: Move Deal Stage to "Ready to Quote"

| Type | Extracted Item | Details |
|------|----------------|---------|
| ⚠️ Assumption | "already created from previous SOP" | Depends on Registration SOP |
| 👤 Manual Action | Navigate to the relevant Deal | User finds Deal record |
| 👤 Manual Action | Set the stage to "Ready to Quote" | Field update |
| 👤 Manual Action | Refresh the screen | Wait for system |
| ⚠️ Assumption | "system to generate the quote" | Expects auto-creation |
| 📦 Module | Deals | Primary |
| 📦 Module | Quotes | Auto-created |

### Step 2: Open & Mark Quote as "Unused"

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Open the newly created Quote | Navigate to Quotes module |
| 🔀 Decision Point | "(Optional) Type 'Public' in the quote title" | User choice |
| ✏️ Manual Input | Type "Public" in title | If optional chosen |
| 👤 Manual Action | Scroll down to review | Verification step |
| 👤 Manual Action | Review student details for accuracy | Human validation |
| 📦 Module | Quotes | Primary |

### Step 3: Convert Quote to Invoice

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Click "Convert" > "Convert to Invoice" | UI action |
| 👤 Manual Action | Review invoice information | Verification |
| 👤 Manual Action | Ensure all student and course details are accurate | Validation |
| ✏️ Manual Input | Add the Invoice Date (today's date) | Date entry |
| ⚠️ Assumption | "Due Date will auto-fill as one week" | System default |
| 🔀 Decision Point | "unless the student is on a payment plan" | Conditional behavior |
| 👤 Manual Action | Do not mark as "Paid" yet | Constraint |
| 📦 Module | Quotes | Source |
| 📦 Module | Invoices | Target |

### Step 4: Send Invoice Email Using Template

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Click on "Send Email" | UI action |
| 👤 Manual Action | Choose the "Public Invoice Template" | Template selection |
| ⚠️ Assumption | "usually at the bottom of the template list" | UI location hint |
| 👤 Manual Action | Click "Next" and "Send" | Complete action |
| 📦 Module | Invoices | Primary |

### Summary - Public Invoice SOP

| Category | Count |
|----------|-------|
| Manual Actions | 12 |
| Decision Points | 2 |
| Manual Inputs | 2 |
| Assumptions | 4 |
| Modules Touched | Deals, Quotes, Invoices |

---

## SOP 2: Private Attendee in Public Course Invoicing

**Source:** `SOPs/raw_sops/private_attendee_invoicing_sop.md`

### Step 1: Confirm Deal & Registration Status

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Navigate to the relevant course in CRM | Find course |
| 👤 Manual Action | Check if the private student has been registered | Verification |
| 👤 Manual Action | Check if Deal created | Verification |
| 🔀 Decision Point | "If not, follow the Registration SOP first" | Conditional branch |
| 📦 Module | Courses | Primary |
| 📦 Module | Deals | Check |
| 📦 Module | Registration Records | Check |

### Step 2: Open the Private Student Deal

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Find the Deal associated with the private student | Search/filter |
| 👤 Manual Action | Ensure the Deal is correctly linked to the course and student | Validation |
| 👤 Manual Action | Verify billing details reflect the private payer | Validation |
| ⚠️ Assumption | "e.g., individual, employer paying separately" | Business context |
| 📦 Module | Deals | Primary |

### Step 3: Edit & Finalise Invoice Details

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Open the invoice associated with the Deal | Navigate |
| 👤 Manual Action | Review items, pricing, and tax information | Verification |
| ✏️ Manual Input | Adjust any course fees | Price modification |
| ⚠️ Assumption | "based on private attendee pricing arrangements" | Business rules |
| 📦 Module | Invoices | Primary |

### Step 4: Send Invoice to Private Payer

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Use the appropriate email template | Select template |
| 👤 Manual Action | Confirm the recipient email is correct | Validation |
| 👤 Manual Action | Send the invoice | Action |
| 👤 Manual Action | Note any special payment terms | Documentation |
| 📦 Module | Invoices | Primary |

### Summary - Private Attendee Invoicing SOP

| Category | Count |
|----------|-------|
| Manual Actions | 12 |
| Decision Points | 1 |
| Manual Inputs | 1 |
| Assumptions | 2 |
| Modules Touched | Courses, Deals, Registration Records, Invoices |

---

## SOP 3: Deal Pipeline Management

**Source:** `SOPs/raw_sops/deal_pipeline_management.md`

### Step 1: Understanding Deal Types

| Type | Extracted Item | Details |
|------|----------------|---------|
| ⚠️ Assumption | "Deals are split into Main Deals and Sub Deals" | System structure |
| ⚠️ Assumption | "Main Deals represent overall client engagement" | Concept |
| ⚠️ Assumption | "Sub Deals represent individual courses/services" | Concept |
| 📦 Module | Deals | Primary |

### Step 2: Creating Sub Deals

| Type | Extracted Item | Details |
|------|----------------|---------|
| 🔀 Decision Point | "When a client books multiple courses" | Trigger condition |
| 👤 Manual Action | Create Sub Deals under the Main Deal | Record creation |
| ✏️ Manual Input | Deal Name | Required field |
| ✏️ Manual Input | Course or Service Type | Required field |
| ✏️ Manual Input | Location | Required field |
| ✏️ Manual Input | Start Date | Required field |
| 📦 Module | Deals | Primary |

### Step 3: Updating Deal Stages

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Move Sub Deals through the pipeline stages | Stage update |
| ⚠️ Assumption | Stages: New, Ready to Quote, Quoted, Won, Lost | Stage names |
| 📦 Module | Deals | Primary |

### Step 4: Maintaining Pipeline Hygiene

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Regularly review open Deals | Periodic check |
| 👤 Manual Action | Ensure stages reflect current status | Validation |
| 👤 Manual Action | Ensure no duplicate Deals exist | Deduplication |
| 👤 Manual Action | Update Closed Deals (Won/Lost) promptly | Timely updates |
| 📦 Module | Deals | Primary |

### Summary - Deal Pipeline Management SOP

| Category | Count |
|----------|-------|
| Manual Actions | 6 |
| Decision Points | 1 |
| Manual Inputs | 4 |
| Assumptions | 4 |
| Modules Touched | Deals |

---

## SOP 4: Quoting Process - Private Student in Public Course

**Source:** `SOPs/raw_sops/quoting_process_private_student.md`

### Step 1: Create or Locate the Course

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Navigate to the course in CRM | Find course |
| 👤 Manual Action | Confirm the course details | Validation |
| ✏️ Manual Input | Verify location, date, and type | Confirmation |
| 📦 Module | Courses | Primary |

### Step 2: Register the Private Student

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Add the student to the course as private attendee | Record creation |
| 👤 Manual Action | Ensure contact details are correct | Validation |
| 👤 Manual Action | Ensure billing details are correct | Validation |
| 📦 Module | Courses | Primary |
| 📦 Module | Contacts | Related |
| 📦 Module | Registration Records | Created |

### Step 3: Create a Deal for the Private Student

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Create a new Deal from course record | Record creation |
| ✏️ Manual Input | Use student's name and course details | Deal naming |
| 👤 Manual Action | Set the stage to "Ready to Quote" | Stage update |
| 👤 Manual Action | Refresh the page | Wait for system |
| ⚠️ Assumption | "this generates a Quote for the private student" | Auto-creation |
| 📦 Module | Courses | Source |
| 📦 Module | Deals | Created |
| 📦 Module | Quotes | Auto-created |

### Step 4: Review & Send Quote

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Open the Quote | Navigate |
| 👤 Manual Action | Check pricing, course details, student information | Validation |
| 👤 Manual Action | Send the Quote to the private payer | Action |
| 👤 Manual Action | Use appropriate email template | Template selection |
| 📦 Module | Quotes | Primary |

### Summary - Quoting Process SOP

| Category | Count |
|----------|-------|
| Manual Actions | 12 |
| Decision Points | 0 |
| Manual Inputs | 2 |
| Assumptions | 1 |
| Modules Touched | Courses, Contacts, Registration Records, Deals, Quotes |

---

## SOP 5: Registration Process

**Source:** `SOPs/raw_sops/registration_process.md`

### Step 1: Locate the Course in CRM

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Go to the Courses module in Zoho CRM | Navigation |
| 🔀 Decision Point | "If the tab is not visible, click the three dots" | Conditional UI |
| 👤 Manual Action | Find it in the dropdown | UI navigation |
| 👤 Manual Action | Use filters to locate the course | Search/filter |
| 🔀 Decision Point | "Filter by location OR filter by month" | Multiple options |
| ✏️ Manual Input | Filter by location (e.g., "Mackay") | Search criteria |
| ✏️ Manual Input | Filter by month (e.g., "July") | Search criteria |
| 👤 Manual Action | Select the correct course | Selection |
| ⚠️ Assumption | "e.g., Part B course" | Business context |
| 📦 Module | Courses | Primary |

### Step 2: Create a New Deal for the Student

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Scroll to the Deals section in course record | Navigation |
| 👤 Manual Action | Click the three dots > New Deal | UI action |
| ✏️ Manual Input | Fill in deal name format | Required format |
| ⚠️ Assumption | "CourseCode + Location + Date + Student/Company Name" | Naming convention |
| ⚠️ Assumption | "Example: TAE22B Mackay July Smith" | Format example |
| 🔀 Decision Point | "If applicable, select or create the associated Account" | Conditional action |
| 👤 Manual Action | Select or create Account | Record link/creation |
| 📦 Module | Courses | Source |
| 📦 Module | Deals | Created |
| 📦 Module | Accounts | Link/Create |

### Step 3: Complete Student Details

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Ensure the Contact record is linked to the Deal | Validation |
| ✏️ Manual Input | Add or confirm Email | Contact field |
| ✏️ Manual Input | Add or confirm Mobile number | Contact field |
| ✏️ Manual Input | Add any special notes | Notes field |
| 📦 Module | Deals | Primary |
| 📦 Module | Contacts | Link |

### Step 4: Save and Confirm Registration

| Type | Extracted Item | Details |
|------|----------------|---------|
| 👤 Manual Action | Save the Deal | Action |
| 👤 Manual Action | Confirm student appears in course's related Deals list | Verification |
| 📦 Module | Deals | Primary |
| 📦 Module | Courses | Verify |

### Summary - Registration Process SOP

| Category | Count |
|----------|-------|
| Manual Actions | 12 |
| Decision Points | 3 |
| Manual Inputs | 6 |
| Assumptions | 3 |
| Modules Touched | Courses, Deals, Accounts, Contacts |

---

## Combined Summary

### All SOPs - Extraction Totals

| SOP | Manual Actions | Decision Points | Manual Inputs | Assumptions | Modules |
|-----|----------------|-----------------|---------------|-------------|---------|
| Public Invoice | 12 | 2 | 2 | 4 | 3 |
| Private Attendee Invoicing | 12 | 1 | 1 | 2 | 4 |
| Deal Pipeline Management | 6 | 1 | 4 | 4 | 1 |
| Quoting Process | 12 | 0 | 2 | 1 | 5 |
| Registration Process | 12 | 3 | 6 | 3 | 4 |
| **TOTAL** | **54** | **7** | **15** | **14** | - |

### Module Touchpoint Matrix

| Module | Public Invoice | Private Attendee | Deal Pipeline | Quoting Process | Registration |
|--------|----------------|------------------|---------------|-----------------|--------------|
| Courses | - | ✓ | - | ✓ | ✓ |
| Contacts | - | - | - | ✓ | ✓ |
| Accounts | - | - | - | - | ✓ |
| Deals | ✓ | ✓ | ✓ | ✓ | ✓ |
| Quotes | ✓ | - | - | ✓ | - |
| Invoices | ✓ | ✓ | - | - | - |
| Registration Records | - | ✓ | - | ✓ | - |

### Key Assumptions Requiring Validation

1. **Auto-quote creation** - Public Invoice & Quoting Process assume Quote auto-creates on "Ready to Quote"
2. **Due Date auto-fill** - Public Invoice assumes 1-week default
3. **Stage names** - Deal Pipeline uses different names than CRM (New vs Qualification)
4. **Deal naming convention** - Registration Process assumes specific format
5. **Main/Sub Deal structure** - Deal Pipeline assumes hierarchy exists

### Decision Points Requiring Diagram Nodes

1. **Public Invoice Step 2:** Optional "Public" title
2. **Public Invoice Step 3:** Payment plan exception
3. **Private Attendee Step 1:** If not registered, follow Registration SOP
4. **Deal Pipeline Step 2:** When client books multiple courses
5. **Registration Step 1:** Tab visibility check
6. **Registration Step 1:** Filter by location OR month
7. **Registration Step 2:** If applicable, create Account

---

## Phase 3 Input Summary

This extraction provides the foundation for Phase 3 workflow mapping:

- **54 manual actions** to check against CRM automations
- **7 decision points** to add as diamond nodes in diagrams
- **15 manual inputs** to verify field requirements
- **14 assumptions** to validate against actual system behavior
- **Cross-module touchpoints** mapped for workflow tracking

---

**Next Phase:** Phase 3 - Workflow Mapping
