# Quoting Process - Private Student in Public Course - Annotated

> **Source:** `SOPs/raw_sops/quoting_process_private_student.md`
> **Coverage:** 53%
> **CRM Sources:** See [Source References](../analysis/source_references.md)

---

## Summary

This SOP has the **highest coverage (53%)** due to multiple auto-population workflows. However, **5 steps have undocumented automations** that users should know about.

| Status | Count |
|--------|-------|
| ✅ Aligned | 1 |
| ⚠️ Partial | 2 |
| ❌ Contradicts | 0 |
| 🔴 Missing | 7 |
| 🟡 Undocumented | 5 |

---

## Step 1: Create or Locate the Course

### Original SOP Instruction

> - Navigate to the course in CRM.
> - Confirm the course details: location, date, and type.

---

### Step 1.1: Navigate to the course in CRM

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Go to Courses module
2. Filter by location, date, or course code
3. Open the course record

---

### Step 1.2: Confirm course details

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Verify Course_Name, Course_Start_Date
2. Verify Select_Venue is correct
3. Check Course_Status is appropriate (not Cancelled)

---

## Step 2: Register the Private Student

### Original SOP Instruction

> - Add the student to the course as a private attendee.
> - Ensure their contact details and billing details are correct.

---

### Step 2.1: Add student as private attendee

**Status:** 🟡 UNDOCUMENTED

**🤖 Undocumented Automations:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Calculate Registrations and create team task | [52330000002518044](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518044) | create | Updates course count, creates task |
| Workdrive Folder Creation | [52330000005138075](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005138075) | create | Creates document folder |
| Private Attendee - Spot Tentative | [52330000005163090](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163090) | create | Confirms private booking |

**Source:** `modules/registration_records/docs/registration-kanban-usage.md:36-44`

**👤 Human Actions Required:**
1. In Course record, go to Registration Records section
2. Create new Registration Record
3. Set Attendee = Contact, set as private attendee
4. System will: create task, create Workdrive folder, update counts

---

### Step 2.2-2.3: Ensure contact and billing details correct

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Verify Contact has email and mobile
2. For private billing, verify Account = payer (may be employer)
3. No validation workflow exists

---

## Step 3: Create a Deal for the Private Student

### Original SOP Instruction

> - From the course record, create a new Deal using the student's name and course details.
> - Set the stage to "Ready to Quote".
> - Refresh the page—this generates a Quote for the private student.

---

### Step 3.1: Create Deal from course record

**Status:** 🟡 UNDOCUMENTED

**🤖 Undocumented Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Update Deal ID | [52330000002444572](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002444572) | create | Assigns unique Deal_ID |

**👤 Human Actions Required:**
1. In Course record, go to Deals section
2. Click New Deal
3. Set Contact_Name, Account_Name, Courseaa
4. Deal_ID auto-assigns on save

---

### Step 3.2: Use student's name and course details

**Status:** 🟡 UNDOCUMENTED

**🤖 Undocumented Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Deal Naming Convention | [52330000002967279](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967279) | create | Auto-generates Deal_Name |
| Update Amount on create | [52330000003995130](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995130) | create | Calculates amount |

**Note:** Do not manually enter Deal Name - it will be auto-generated.

---

### Step 3.3: Set stage to "Ready to Quote"

**Status:** ✅ ALIGNED

**🤖 Automation Triggered:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Create Quote - Stage Update | [52330000002460308](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308) | Stage = "Ready to Quote" | Creates Quote record |

**👤 Human Actions Required:**
1. Change Stage to "Ready to Quote"
2. Save the Deal
3. Quote auto-creates in Quotes module

---

### Step 3.4: Refresh the page

**Status:** ⚠️ PARTIAL

**CRM Reality:**
- Quote is created automatically but in Quotes module
- Refresh only updates current page, doesn't show Quote

**⚠️ Gap Identified:**
- SOP doesn't explain Quote is in different module

**✅ Correct Procedure:**
```
After saving Deal with "Ready to Quote" stage:
1. Go to Quotes module
2. Find Quote linked to this Deal
3. Or use Deal's related Quotes list
```

---

## Step 4: Review & Send Quote

### Original SOP Instruction

> - Open the Quote.
> - Check that pricing, course details, and student information are correct.
> - Send the Quote to the private payer using the appropriate email template.

---

### Step 4.1: Open the Quote

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Navigate to Quotes module
2. Find by Deal_Name or recent records
3. Open the Quote record

---

### Step 4.2: Check pricing

**Status:** 🟡 UNDOCUMENTED

**🤖 Undocumented Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Inhouse - Calculate Tax | [52330000004975235](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004975235) | create_or_edit | Auto-calculates GST |

**Note:** Tax is auto-calculated - do not manually enter.

---

### Step 4.3: Check course details

**Status:** 🟡 UNDOCUMENTED

**🤖 Undocumented Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Update Quote Details | [52330000002597194](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002597194) | create | Auto-populates Course_ID, Deal_ID |

**Note:** Course details auto-populate from Deal.

---

### Step 4.4: Check student information

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Verify Contact_Name is the student
2. Verify email address is correct
3. No validation workflow exists

---

### Step 4.5: Send Quote to private payer

**Status:** ⚠️ PARTIAL

**🤖 Automation Available:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Send Quote | [52330000006984913](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006984913) | Send_Quote_as_EMAIL = true | Sends email, updates Quote_Stage |

**Source:** `modules/quotes/docs/quotes-workflows.md:149-167`

**👤 Human Actions Required:**
1. Set Send_Quote_as_EMAIL checkbox to TRUE
2. Save the record
3. Workflow sends email and sets Quote_Stage to "Sent"

**🟡 Also triggered:**

| Workflow | ID | Action |
|----------|-----|--------|
| Update quote when sent or won | [52330000003995201](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995201) | Sets Quote_Sent_Date |

---

### Step 4.6: Use appropriate email template

**Status:** 🔴 MISSING

**CRM Reality:**
- Template is configured in workflow, not selected by user
- No separate template for private attendees

**Recommendation:** Create workflow variant with private attendee template

---

## Corrected SOP Summary

### Recommended Updated Procedure

**Step 1: Locate Course**
1. Go to Courses module
2. Filter and find the course
3. Verify details (dates, venue, status)

**Step 2: Register Private Student**
1. Create Registration Record in Course
2. Set Attendee, mark as private
3. System auto-creates: task, Workdrive folder
4. Verify Contact has email/mobile

**Step 3: Create Deal**
1. Create Deal from Course record
2. Set Contact_Name, Account_Name (payer), Courseaa
3. Do NOT enter Deal Name - it auto-generates
4. Amount auto-calculates from Course
5. Change Stage to "Ready to Quote" and save
6. Quote auto-creates in Quotes module

**Step 4: Send Quote**
1. Go to Quotes module and open the Quote
2. Verify auto-populated details (pricing, course, contact)
3. Tax is auto-calculated - do not edit
4. Set Send_Quote_as_EMAIL = TRUE and save
5. System sends email and sets Quote_Sent_Date

---

## Related CRM Diagrams

- [Deal Workflow](../../modules/deals/diagrams/deals-workflow.mmd)
- [Quote Lifecycle](../../modules/quotes/diagrams/quotes-lifecycle.mmd)
- [Registration Timeline](../../modules/courses/diagrams/registration-timeline.mmd)
