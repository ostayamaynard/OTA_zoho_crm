# Private Attendee in Public Course Invoicing SOP - Annotated

> **Source:** `SOPs/raw_sops/private_attendee_invoicing_sop.md`
> **Coverage:** 29%
> **CRM Sources:** See [Source References](../analysis/source_references.md)

---

## Summary

This SOP has the second-lowest coverage at 29%. Primary issue: **10 steps (71%) have no automation support**, mostly navigation and validation steps.

| Status | Count |
|--------|-------|
| ✅ Aligned | 1 |
| ⚠️ Partial | 2 |
| ❌ Contradicts | 0 |
| 🔴 Missing | 10 |
| 🟡 Undocumented | 1 |

---

## Step 1: Confirm Deal & Registration Status

### Original SOP Instruction

> - Navigate to the relevant course in CRM.
> - Check if the private student has been registered and a Deal created.
> - If not, follow the Registration SOP first.

---

### Step 1.1: Navigate to the relevant course in CRM

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Go to Courses module
2. Filter by location, date, or course name
3. Open the course record

---

### Step 1.2: Check if private student has been registered

**Status:** 🔴 MISSING

**CRM Reality:**
- No validation workflow to check registration status
- User must manually review Registration Records related list

**👤 Human Actions Required:**
1. In Course record, scroll to Registration Records section
2. Look for the student's name
3. Verify Status is not "Cancelled"

---

### Step 1.3: Check if Deal created

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. In Course record, scroll to Deals section
2. Look for Deal with student/company name
3. Verify Deal exists and is linked correctly

---

### Step 1.4: If not, follow Registration SOP first

**Status:** 🔴 MISSING

**Decision Point:** 🔀

| Condition | Action |
|-----------|--------|
| Registration exists | Proceed to Step 2 |
| No registration | Follow Registration SOP first |

**CRM Reality:**
- No automated redirect or prompt
- User must recognize gap and switch to other SOP

---

## Step 2: Open the Private Student Deal

### Original SOP Instruction

> - Find the Deal associated with the private student in the course.
> - Ensure the Deal is correctly linked to the course and student.
> - Verify that the billing details reflect the private payer.

---

### Step 2.1: Find the Deal associated with the private student

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. From Course record, click on Deal in related list
2. Or go to Deals module and filter by Course + Contact/Account

---

### Step 2.2: Ensure Deal is correctly linked to course and student

**Status:** ⚠️ PARTIAL

**🤖 Partial Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| When Account name is not blank | [52330000005069264](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005069264) | field_update | Propagates Account to related records |

**Source:** `modules/deals/docs/deal-kanban-usage.md`

**👤 Human Actions Required:**
1. Verify Courseaa field = correct course
2. Verify Contact_Name = student
3. Verify Account_Name = billing entity (if different from student)

---

### Step 2.3: Verify billing details reflect private payer

**Status:** 🔴 MISSING

**CRM Reality:**
- No validation workflow for billing details
- User must manually verify Account represents the payer

**👤 Human Actions Required:**
1. Check Account_Name is the paying entity
2. Verify billing address and contact on Account
3. For employer-paid, Account = employer (not student)

---

## Step 3: Edit & Finalise Invoice Details

### Original SOP Instruction

> - Open the invoice associated with the Deal.
> - Review items, pricing, and tax information.
> - Adjust any course fees based on private attendee pricing arrangements.

---

### Step 3.1: Open the invoice associated with the Deal

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. In Deal record, scroll to Invoices section
2. Click on the Invoice record
3. Or go to Invoices module and filter by Deal_Name

---

### Step 3.2: Review items, pricing, and tax information

**Status:** 🟡 UNDOCUMENTED

**🤖 Undocumented Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Inhouse - Calculate Overall Tax | [52330000004975124](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004975124) | create_or_edit | Auto-calculates GST fields |

**Source:** `modules/invoices/docs/invoices-workflows.md:120-135`

**👤 Human Actions Required:**
1. Verify Invoiced_Items show correct course
2. Verify pricing matches agreement
3. **Do not manually enter tax** - it's auto-calculated

---

### Step 3.3: Adjust any course fees based on private attendee pricing

**Status:** 🔴 MISSING

**CRM Reality:**
- No workflow for price adjustments
- No audit trail for changes

**👤 Human Actions Required:**
1. Edit Invoiced_Items to adjust pricing
2. Document reason in notes or custom field
3. Tax will auto-recalculate on save

**Recommendation:** Add Adjustment_Reason field to track pricing changes

---

## Step 4: Send Invoice to Private Payer

### Original SOP Instruction

> - Use the appropriate email template for private attendee invoicing.
> - Confirm the recipient email is correct.
> - Send the invoice and note any special payment terms.

---

### Step 4.1: Use the appropriate email template

**Status:** ⚠️ PARTIAL

**🤖 Automation Available:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Send Invoice | [52330000004534311](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004534311) | Status = "Sent" | Sends configured template |

**⚠️ Gap Identified:**
- Template is set in workflow, not selectable per invoice
- Private vs Public template may not be differentiated

**Recommendation:** Create separate workflow for private invoices with different template

---

### Step 4.2: Confirm the recipient email is correct

**Status:** 🔴 MISSING

**👤 Human Actions Required:**
1. Check Contact's email address
2. For employer-paid, may need different recipient
3. Verify Email field on Invoice if overridden

---

### Step 4.3: Send the invoice

**Status:** ✅ ALIGNED

**🤖 Automation Triggered:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Send Invoice | [52330000004534311](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004534311) | Status = "Sent" | Sends email, sets Invoice_Sent_Date |

**👤 Human Actions Required:**
1. Change Status to "Sent"
2. Save record
3. Workflow sends automatically

---

### Step 4.4: Note any special payment terms

**Status:** 🔴 MISSING

**CRM Reality:**
- No field or workflow for payment term notes
- User must use generic notes field

**👤 Human Actions Required:**
1. Add notes to Description or custom field
2. Adjust Due_Date if terms differ from default

---

## Additional Undocumented Automations

| Workflow | ID | Action | User Should Know |
|----------|-----|--------|------------------|
| New - Update deal and Reg record | [52330000004251591](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004251591) | Updates Deal and Registration on invoice changes | Changes sync to related records |
| Update Amount in Deal when paid | [52330000009085784](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085784) | Updates Deal.Amount on payment | Amount syncs when Status = Paid |

---

## Corrected SOP Summary

### Recommended Updated Procedure

**Step 1: Confirm Deal & Registration Status**
1. Navigate to Courses module and find the course
2. Check Registration Records section for student
3. Check Deals section for linked Deal
4. If missing, complete Registration SOP first

**Step 2: Open and Verify Private Student Deal**
1. Open the Deal from the Course record
2. Verify: Courseaa, Contact_Name, Account_Name (payer)
3. Note: Account details auto-propagate to related records

**Step 3: Review and Adjust Invoice**
1. Open Invoice from Deal's related list
2. Review items and pricing
3. Adjust fees if needed (tax auto-recalculates)
4. Do not manually enter tax amounts

**Step 4: Send Invoice**
1. Verify recipient email is correct
2. Change Status to "Sent" and save
3. Add payment term notes to Description field
4. Adjust Due_Date for non-standard terms

---

## Related CRM Diagrams

- [Invoice Payment Flow](../../modules/invoices/diagrams/invoices-payment-flow.mmd)
- [Deal Workflow](../../modules/deals/diagrams/deals-workflow.mmd)
- [Registration Kanban](../../modules/registration_records/diagrams/registration-kanban-detailed.mmd)
