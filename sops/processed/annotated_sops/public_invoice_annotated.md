# Public Invoice SOP - Annotated

> **Source:** `SOPs/raw_sops/public_invoice_sop.md`
> **Coverage:** 46%
> **CRM Sources:** See [Source References](../analysis/source_references.md)

---

## Summary

This annotated version cross-references the Public Invoice SOP against actual CRM workflows. Key finding: **2 critical contradictions** in invoice creation and sending methods.

| Status | Count |
|--------|-------|
| ✅ Aligned | 2 |
| ⚠️ Partial | 3 |
| ❌ Contradicts | 2 |
| 🔴 Missing | 5 |
| 🟡 Undocumented | 1 |

---

## Step 1: Move Deal Stage to "Ready to Quote"

### Original SOP Instruction

> - Navigate to the relevant Deal (already created from previous SOP).
> - Set the stage to "Ready to Quote".
> - Refresh the screen to allow the system to generate the quote.

---

### Step 1.1: Navigate to the relevant Deal

**Status:** 🔴 MISSING

**CRM Reality:**
- No navigation workflow exists
- User must manually search or filter Deals module

**👤 Human Actions Required:**
1. Go to Deals module
2. Use filters (Account, Course, Date) to find Deal
3. Or use Recent Records if recently accessed

**Recommendation:** Add Quick Links widget for common Deal searches

---

### Step 1.2: Set the stage to "Ready to Quote"

**Status:** ✅ ALIGNED

**🤖 Automation Triggered:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Create Quote - Stage Update | [52330000002460308](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308) | Stage = "Ready to Quote" | Creates Quote record |

**Source:** `modules/deals/docs/deal-kanban-usage.md:229-246`

**👤 Human Actions Required:**
1. Open Deal record
2. Change Stage field to "Ready to Quote"
3. Save the record

**Fields Affected:**

| Field | Module | Update Type | Value |
|-------|--------|-------------|-------|
| Stage | Deals | Manual | "Ready to Quote" |
| Quote record | Quotes | Automatic | New record created |

---

### Step 1.3: Refresh the screen to allow system to generate quote

**Status:** ⚠️ PARTIAL

**CRM Reality:**
- Quote is created automatically by workflow 52330000002460308
- SOP doesn't explain where to find the Quote

**⚠️ Gap Identified:**
- User may not know Quote appears in Quotes module
- No link provided from Deal to new Quote

**Recommendation:** Update SOP to say:
```
After changing stage, go to Quotes module to find the new Quote
linked to this Deal. The Quote will have auto-populated details.
```

---

## Step 2: Open & Mark Quote as "Unused"

### Original SOP Instruction

> - Open the newly created Quote.
> - (Optional) Type "Public" in the quote title for clarity.
> - Scroll down to review student details for accuracy.

---

### Step 2.1: Open the newly created Quote

**Status:** 🔴 MISSING

**CRM Reality:**
- No navigation aid exists
- User must go to Quotes module and find by Deal linkage

**👤 Human Actions Required:**
1. Navigate to Quotes module
2. Filter by Deal_Name or recent records
3. Open the Quote record

**Recommendation:** Add "View Related Quotes" button on Deal page

---

### Step 2.2: (Optional) Type "Public" in the quote title

**Status:** 🟡 UNDOCUMENTED

**🤖 Automation That May Interfere:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Update Quote Naming convention | [52330000002856364](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002856364) | create_or_edit | Auto-sets Subject field |

**Source:** `modules/quotes/docs/quotes-workflows.md:44-59`

**⚠️ Gap Identified:**
- Manual title entry may be overwritten on next edit
- Naming convention workflow uses format: [Account] - [Course Type] - [Date]

**Decision Point:** 🔀

| Choice | Outcome |
|--------|---------|
| Add "Public" | May be overwritten by workflow |
| Skip | Subject uses auto-generated name |

**Recommendation:** Update SOP to note:
```
The Quote Subject will auto-populate. Adding "Public" is optional but
may be overwritten by the naming convention workflow on next edit.
```

---

### Step 2.3: Review student details for accuracy

**Status:** 🔴 MISSING

**CRM Reality:**
- No validation workflow exists
- User must manually verify all fields

**👤 Human Actions Required:**
1. Verify Contact_Name is correct
2. Verify Account_Name is correct
3. Check Quoted_Items for correct course and pricing
4. Verify email address for sending

**🟡 Undocumented Automation:**

| Workflow | ID | Action |
|----------|-----|--------|
| Update Quote Details | [52330000002597194](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002597194) | Auto-populates Quote_CRM_ID, Deal_ID, Course_ID |
| Inhouse - Calculate Tax | [52330000004975235](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004975235) | Auto-calculates GST fields |

**Note:** These fields are auto-populated - do not manually enter tax amounts.

---

## Step 3: Convert Quote to Invoice

### Original SOP Instruction

> - At the top of the quote page, click "Convert" > "Convert to Invoice".
> - Review invoice information:
>   - Ensure all student and course details are accurate.
>   - Add the Invoice Date (today's date).
>   - The Due Date will auto-fill as one week from today unless the student is on a payment plan.
> - Do not mark the invoice as "Paid" yet—leave as Draft until payment is received.

---

### Step 3.1: Click "Convert" > "Convert to Invoice"

**Status:** ❌ CONTRADICTS

**What SOP Says:**
> Click "Convert" > "Convert to Invoice"

**What CRM Does:**
Invoice is automatically created when Quote_Stage is set to "Closed Won"

**🤖 Actual Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Update Deal and Invoice on Quote Closed Won | [52330000002460325](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460325) | Quote_Stage = "Closed Won" | Creates Invoice, updates Deal |

**Source:** `modules/quotes/docs/quotes-workflows.md:104-122`

**❌ Impact of Following SOP:**
1. **Duplicate invoices** - Manual conversion creates one, then automation creates another
2. **Missing field updates** - Quote_Won_Date not set, Deal stage not updated
3. **Reporting errors** - Invoice count inflated

**✅ Correct Procedure:**
```
Step 3: Mark Quote as Accepted
1. In the Quote record, change Quote_Stage to "Closed Won"
2. Save the record
3. The system will automatically:
   - Create an Invoice record
   - Update the Deal stage to Closed Won
   - Set the Quote_Won_Date
4. Go to Invoices module to find the new invoice
```

---

### Step 3.2: Add the Invoice Date (today's date)

**Status:** ⚠️ PARTIAL

**CRM Reality:**
- Invoice Date may auto-populate to today's date
- User can override if needed

**👤 Human Actions Required:**
1. Verify Invoice_Date is correct (defaults to today)
2. Adjust if backdating is required

---

### Step 3.3: Due Date will auto-fill

**Status:** ✅ ALIGNED

**🤖 Automation Triggered:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Update Due Date | [52330000005069739](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005069739) | create | Sets Due_Date based on Payment_term_in_days |

**Source:** `modules/invoices/docs/invoices-workflows.md:24-38`

**Decision Point:** 🔀

| Condition | Due Date Behavior |
|-----------|-------------------|
| Standard terms | Auto-fills to Invoice_Date + Payment_term_in_days |
| Payment plan | User must manually adjust Due_Date |

**👤 Human Actions Required:**
1. Verify Due_Date is correct
2. If payment plan, manually set appropriate Due_Date

---

### Step 3.4: Leave as Draft until payment received

**Status:** 🔴 MISSING

**CRM Reality:**
- No workflow validates Draft status
- User must remember not to mark as Paid

**👤 Human Actions Required:**
1. Ensure Status field is NOT set to "Paid"
2. Leave as "Draft" or "Sent" depending on next step

---

## Step 4: Send Invoice Email Using Template

### Original SOP Instruction

> - Click on "Send Email" from within the invoice page.
> - Choose the "Public Invoice Template" (usually at the bottom of the template list).
> - Click "Next" and "Send".

---

### Step 4.1: Click on "Send Email"

**Status:** ❌ CONTRADICTS

**What SOP Says:**
> Click on "Send Email" from within the invoice page

**What CRM Does:**
Invoice is sent via workflow when Status field changes

**🤖 Actual Automation:**

| Workflow | ID | Trigger | Action |
|----------|-----|---------|--------|
| Send Invoice | [52330000004534311](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004534311) | Status = "Sent" | Sends email, sets Invoice_Sent_Date |

**Source:** `modules/invoices/docs/invoices-workflows.md:220-236`

**❌ Impact of Following SOP:**
1. **Workflow bypass** - Clicking button may not trigger workflow
2. **Missing tracking** - Invoice_Sent_Date not set
3. **Xero sync issues** - Status-based integrations may not fire

**✅ Correct Procedure:**
```
Step 4: Send Invoice
1. Change the Status field to "Sent"
2. Save the record
3. The system will automatically:
   - Send the invoice email
   - Set Invoice_Sent_Date
   - Trigger any integrations (Xero, etc.)
```

---

### Step 4.2: Choose the "Public Invoice Template"

**Status:** 🔴 MISSING

**CRM Reality:**
- No template auto-selection workflow exists
- Workflow uses default template configured in workflow settings

**⚠️ Gap Identified:**
- User cannot select template when using Status field trigger
- Template is determined by workflow configuration

**Recommendation:**
- Verify workflow 52330000004534311 uses correct template
- Or create separate workflows for different invoice types

---

### Step 4.3: Click "Next" and "Send"

**Status:** ⚠️ PARTIAL

**CRM Reality:**
- When using Status field method, no additional clicks required
- Workflow handles the send automatically

**👤 Human Actions Required:**
1. Change Status to "Sent"
2. Save record
3. Workflow sends email automatically

---

## Additional Undocumented Automations

These workflows affect this SOP but are not mentioned:

| Workflow | ID | Action | User Should Know |
|----------|-----|--------|------------------|
| Update All Fields | [52330000008512961](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008512961) | Populates Invoice_CRM_ID, URLs | Reference fields auto-populated |
| Inhouse - Calculate Tax | [52330000004975124](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004975124) | Calculates GST | Do not manually enter tax |

---

## Corrected SOP Summary

### Recommended Updated Procedure

**Step 1: Move Deal Stage to "Ready to Quote"**
1. Navigate to Deals module and find the relevant Deal
2. Change Stage to "Ready to Quote" and save
3. A Quote will be automatically created in Quotes module

**Step 2: Review Quote**
1. Go to Quotes module and find the new Quote linked to the Deal
2. Verify Contact, Account, Course, and pricing details
3. Note: Quote Subject and tax are auto-calculated

**Step 3: Accept Quote to Create Invoice**
1. Change Quote_Stage to "Closed Won" and save
2. The system will automatically create an Invoice
3. Go to Invoices module to find the new Invoice
4. Verify Due_Date (auto-calculated) and adjust for payment plans

**Step 4: Send Invoice**
1. Change Invoice Status to "Sent" and save
2. The system will automatically send the email and track the date
3. Do not use the "Send Email" button - use Status field instead

---

## Related CRM Diagrams

- [Deal Workflow](../../modules/deals/diagrams/deals-workflow.mmd)
- [Quote Lifecycle](../../modules/quotes/diagrams/quotes-lifecycle.mmd)
- [Invoice Payment Flow](../../modules/invoices/diagrams/invoices-payment-flow.mmd)
