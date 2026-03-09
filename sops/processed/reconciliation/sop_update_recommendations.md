# SOP Update Recommendations

**Purpose:** Specific text changes recommended for each raw SOP
**Generated:** 2025-11-19
**Priority:** Ordered by impact and urgency

---

## Summary

| SOP | Priority | Updates Needed | Key Issues |
|-----|----------|----------------|------------|
| Public Invoice | HIGH | 4 | Contradictions in Steps 3-4 |
| Deal Pipeline | HIGH | 5 | Stage names, naming convention |
| Registration | MEDIUM | 3 | Naming convention, clarifications |
| Quoting Process | MEDIUM | 4 | Undocumented automations |
| Private Attendee | LOW | 3 | Clarifications only |

---

## SOP 1: Public Invoice

**File:** `SOPs/raw_sops/public_invoice_sop.md`
**Priority:** HIGH
**Reason:** 2 critical contradictions causing duplicate records

### Update 1.1: Step 1 - Add Quote Location Note

**Current:**
```markdown
- Refresh the screen to allow the system to generate the quote.
```

**Replace with:**
```markdown
- Save the record. A Quote will be automatically created.
- Navigate to Quotes module to find the new Quote linked to this Deal.
- Or use the Deal's Related Quotes list to open it directly.
```

---

### Update 1.2: Step 2 - Add Automation Notes

**Current:**
```markdown
### Step 2: Open & Mark Quote as "Unused"
- Open the newly created Quote.
- (Optional) Type "Public" in the quote title for clarity.
- Scroll down to review student details for accuracy.
```

**Replace with:**
```markdown
### Step 2: Review Quote Details

- Open the newly created Quote from Quotes module
- **Note:** The following fields are auto-populated:
  - Quote Subject (auto-named, adding "Public" is optional but may be overwritten)
  - Course details from linked Deal
  - Pricing and tax (auto-calculated - do not manually enter)
- Review and verify:
  - Contact_Name is correct
  - Account_Name is correct
  - Quoted_Items show correct course and pricing
```

---

### Update 1.3: Step 3 - Fix Invoice Creation Method (CRITICAL)

**Current:**
```markdown
### Step 3: Convert Quote to Invoice
- At the top of the quote page, click "Convert" > "Convert to Invoice".
- Review invoice information:
  - Ensure all student and course details are accurate.
  - Add the Invoice Date (today's date).
  - The Due Date will auto-fill as one week from today unless the student is on a payment plan.
- Do not mark the invoice as "Paid" yet—leave as Draft until payment is received.
```

**Replace with:**
```markdown
### Step 3: Accept Quote to Create Invoice

- **Change Quote_Stage to "Closed Won"** and save
- **Do NOT use the "Convert" button** - this bypasses workflow tracking
- The system will automatically:
  - Create an Invoice record
  - Update the Deal stage to Closed Won
  - Set the Quote_Won_Date
- Navigate to Invoices module to find the new Invoice
- Review invoice information:
  - Invoice Date defaults to today (adjust if needed)
  - Due Date auto-calculates from Payment_term_in_days
  - If payment plan, manually adjust Due Date
  - Tax is auto-calculated - do not edit
- Leave Status as "Draft" until ready to send
```

---

### Update 1.4: Step 4 - Fix Invoice Send Method (CRITICAL)

**Current:**
```markdown
### Step 4: Send Invoice Email Using Template
- Click on "Send Email" from within the invoice page.
- Choose the "Public Invoice Template" (usually at the bottom of the template list).
- Click "Next" and "Send".
```

**Replace with:**
```markdown
### Step 4: Send Invoice

- **Change Status to "Sent"** and save
- **Do NOT use the "Send Email" button** - this bypasses workflow tracking
- The system will automatically:
  - Send the invoice email using the configured template
  - Set Invoice_Sent_Date
  - Trigger Xero sync (if applicable)
- **Note:** Email template is set in workflow configuration. To use different templates for different invoice types, contact your CRM administrator.
```

---

## SOP 2: Deal Pipeline Management

**File:** `SOPs/raw_sops/deal_pipeline_management.md`
**Priority:** HIGH
**Reason:** Stage names don't match CRM, naming convention contradicts

### Update 2.1: Step 1 - Clarify Deal Structure

**Current:**
```markdown
### Step 1: Understanding Deal Types
- Deals are split into Main Deals and Sub Deals.
  - **Main Deals** represent the overall client engagement.
  - **Sub Deals** represent individual courses, services, or projects.
```

**Replace with:**
```markdown
### Step 1: Understanding Deals

- Each Deal is an independent record (no parent-child hierarchy)
- Create one Deal per student per course
- Deals track the sales process from initial inquiry to payment
- Related records (Quotes, Invoices, Registrations) link via lookups

**Note:** The "Main/Sub Deal" concept is not currently implemented in CRM. Each Deal stands alone.
```

---

### Update 2.2: Step 2 - Fix Naming Convention

**Current:**
```markdown
### Step 2: Creating Sub Deals
- When a client books multiple courses or services, create Sub Deals under the Main Deal.
- Mandatory fields to populate:
  - Deal Name
  - Course or Service Type
  - Location
  - Start Date
```

**Replace with:**
```markdown
### Step 2: Creating Deals

When a client books a course, create a Deal:

**Required Fields:**
- Contact_Name (student)
- Account_Name (company/payer)
- Courseaa (course lookup - auto-fills details)
- Course_Start_Date

**Auto-Generated Fields (do not enter manually):**
- Deal_Name → Format: P - [Company] - [Location] - [Course]
- Deal_ID → Unique identifier
- Amount → Calculated from Course pricing × Number_of_Attendees

**Note:** The Deal Name will be auto-generated. Any manual entry will be overwritten.
```

---

### Update 2.3: Step 3 - Fix Stage Names (CRITICAL)

**Current:**
```markdown
### Step 3: Updating Deal Stages
- Move Sub Deals through the pipeline stages as they progress:
  - New
  - Ready to Quote
  - Quoted
  - Won
  - Lost
```

**Replace with:**
```markdown
### Step 3: Updating Deal Stages

Move Deals through the actual CRM pipeline stages:

| Stage | Description | Automation |
|-------|-------------|------------|
| **Qualification** | Initial stage - verify details | Auto-assigned on create |
| **Negotiation/Review** | Chase requirements | Manual |
| **Ready to Quote** | Quote needed | Quote auto-creates |
| **Awaiting ZipPay Confirmation** | (if applicable) | Manual |
| **Awaiting Purchase Order** | Quote sent, awaiting PO | PO reminders fire |
| **Awaiting Invoice Payment** | Invoice sent | Manual |
| **Closed Won** | Deal complete | Via Quote acceptance or PO entry |
| **Closed Lost** | Deal lost | Requires Loss_Reason |

**Important:**
- "New" and "Quoted" stages do not exist in CRM
- To close as Won: Set Quote_Stage = "Closed Won" OR enter Purchase_Order_Number
- Do NOT manually change Deal stage to Closed Won
```

---

### Update 2.4: Step 4 - Add Automation Notes

**Current:**
```markdown
### Step 4: Maintaining Pipeline Hygiene
- Regularly review open Deals to ensure:
  - Stages reflect current status.
  - No duplicate Deals exist for the same client and course.
  - Closed Deals (Won/Lost) are updated promptly.
```

**Replace with:**
```markdown
### Step 4: Maintaining Pipeline Hygiene

**Weekly Review:**
- Filter Deals by stage and Last_Modified_Date
- Update stages to reflect actual status
- Check for stale Deals (no update in 14+ days)

**Automated Reminders:**
PO chase reminders fire automatically:
- 28 days before Course_Start_Date
- 14 days before
- 5 days before
- 1 day before

**Duplicate Prevention:**
- Before creating Deal, check existing Deals for same Account + Course
- No automated duplicate detection exists - manual check required

**Closing Deals:**
- Won: Enter PO number or accept Quote
- Lost: Change stage and enter Loss_Reason (required)
```

---

### Update 2.5: Add Undocumented Automation Section

**Add new section at end:**
```markdown
### Automations You Should Know

The following workflows fire automatically:

| When | What Happens | Workflow ID |
|------|--------------|-------------|
| Deal created | Deal_ID assigned | 52330000002444572 |
| Deal created | Deal_Name generated | 52330000002967279 |
| Deal created | Amount calculated | 52330000003995130 |
| Stage = Ready to Quote | Quote created | 52330000002460308 |
| PO Number entered | Deal updated, Registrations confirmed | 52330000002460283, 52330000006993545 |
```

---

## SOP 3: Registration Process

**File:** `SOPs/raw_sops/registration_process.md`
**Priority:** MEDIUM
**Reason:** Naming convention issue, needs clarification

### Update 3.1: Step 2 - Fix Naming Convention

**Current:**
```markdown
- Fill in the deal name in the format: CourseCode + Location + Date + Student/Company Name.
  - Example: TAE22B Mackay July Smith
```

**Replace with:**
```markdown
- Set the required fields:
  - Contact_Name (student)
  - Account_Name (company - if applicable)
  - Courseaa (should auto-fill if creating from Course)
- **Do NOT enter Deal Name** - it will be auto-generated
- Format used: P - [Company] - [Location] - [Course]
```

---

### Update 3.2: Step 3 - Clarify Contact Updates

**Current:**
```markdown
### Step 3: Complete Student Details
- Ensure the Contact record for the student is linked to the Deal.
- Add or confirm:
  - Email
  - Mobile number
  - Any special notes relevant to the course.
```

**Replace with:**
```markdown
### Step 3: Complete Student Details

- Ensure Contact_Name is set on the Deal
- **Open the Contact record** to verify/add:
  - Email (required for invoices and notifications)
  - Mobile (required for SMS reminders)
- Add special notes to Deal Description field (dietary requirements, accessibility needs, etc.)

**Note:** Email and Mobile are on the Contact record, not the Deal.
```

---

### Update 3.3: Step 4 - Add Automation Notes

**Current:**
```markdown
### Step 4: Save and Confirm Registration
- Save the Deal.
- Confirm the student appears in the course's related Deals list.

The student is now registered in the CRM for the selected public course.
```

**Replace with:**
```markdown
### Step 4: Save and Confirm

- Save the Deal
- The system will automatically:
  - Assign a unique Deal_ID
  - Generate the Deal_Name
  - Calculate the Amount from Course pricing
- Verify the auto-generated Deal Name is correct
- Return to Course record and confirm Deal appears in related list

**Important:** This creates a Deal for quoting/invoicing. To track attendance and certification, also create a Registration Record in the Course's Registration Records section.
```

---

## SOP 4: Quoting Process

**File:** `SOPs/raw_sops/quoting_process_private_student.md`
**Priority:** MEDIUM
**Reason:** Multiple undocumented automations

### Update 4.1: Step 2 - Add Automation Notes

**After Step 2 instruction, add:**
```markdown
**Automations on Registration Creation:**
- Team Task created for follow-up
- Workdrive folder created for documents
- Private attendee status flagged
```

---

### Update 4.2: Step 3 - Add Automation Notes

**Replace last bullet:**
```markdown
- Refresh the page—this generates a Quote for the private student.
```

**With:**
```markdown
- Save the Deal. The following happens automatically:
  - Deal_ID assigned
  - Deal_Name generated (do not enter manually)
  - Amount calculated from Course pricing
  - Quote created in Quotes module
- Navigate to Quotes module to find the new Quote
```

---

### Update 4.3: Step 4 - Clarify Send Method

**Current:**
```markdown
- Send the Quote to the private payer using the appropriate email template.
```

**Replace with:**
```markdown
- To send the Quote:
  - Set **Send_Quote_as_EMAIL = TRUE** and save
  - The system will send the email and set Quote_Sent_Date
- **Note:** Email template is configured in workflow, not selected per quote
- Tax is auto-calculated - do not manually edit
```

---

### Update 4.4: Add Automation Summary

**Add new section at end:**
```markdown
### Automations Summary

| Step | Automation | Workflow ID |
|------|------------|-------------|
| Register student | Task, folder created | 52330000002518044, 52330000005138075 |
| Create Deal | ID, name, amount set | 52330000002444572, 52330000002967279, 52330000003995130 |
| Stage = Ready to Quote | Quote created | 52330000002460308 |
| Send_Quote_as_EMAIL = TRUE | Quote sent | 52330000006984913 |
```

---

## SOP 5: Private Attendee Invoicing

**File:** `SOPs/raw_sops/private_attendee_invoicing_sop.md`
**Priority:** LOW
**Reason:** Mostly clarifications, no major contradictions

### Update 5.1: Step 3 - Add Tax Note

**After "Review items, pricing, and tax information" add:**
```markdown
- **Note:** Tax (GST) is auto-calculated. Do not manually enter tax amounts.
```

---

### Update 5.2: Step 4 - Clarify Send Method

**Replace:**
```markdown
- Send the invoice and note any special payment terms.
```

**With:**
```markdown
- Change **Status to "Sent"** and save
- The system will send the email and set Invoice_Sent_Date
- Add special payment terms to Description field
- Adjust Due_Date if terms differ from default
```

---

### Update 5.3: Add Cross-Reference Note

**Add at end:**
```markdown
**Related Automations:**
- Tax auto-calculated (WF: 52330000004975124)
- Invoice syncs to Deal and Registration (WF: 52330000004251591)
- Amount syncs to Deal when paid (WF: 52330000009085784)
```

---

## Implementation Checklist

### Week 1: Critical Updates

- [ ] Public Invoice: Update Steps 3 and 4 (CON-001, CON-002)
- [ ] Deal Pipeline: Update Stage names in Step 3 (CON-004, CON-005)
- [ ] Deal Pipeline: Update Step 2 naming convention (CON-003)
- [ ] Registration: Update Step 2 naming convention (CON-006)

### Week 2: High Priority Updates

- [ ] Public Invoice: Update Steps 1 and 2
- [ ] Deal Pipeline: Update Steps 1 and 4
- [ ] Deal Pipeline: Add automation summary

### Week 3: Medium Priority Updates

- [ ] Registration: Update Steps 3 and 4
- [ ] Quoting Process: All 4 updates
- [ ] Private Attendee: All 3 updates

### Verification

After updates, have users test:
- [ ] Can create Quote without duplicate invoices
- [ ] Invoice sends with proper tracking
- [ ] Deal Name auto-generates correctly
- [ ] Users can find correct CRM stages

---

## Related Documents

- [Contradictions](contradictions.md)
- [Missing Automations](missing_automations.md)
- [Annotated SOPs](../annotated_sops/)
