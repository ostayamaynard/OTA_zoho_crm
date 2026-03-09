# Lead Workflow URLs Reference

Quick access to all Lead-related workflows in Zoho CRM

**Source:** zoho-dependencies-2025-11-13.json
**Total Workflows:** 18 (17 active, 1 inactive)

---

## By Status

### New Lead

**Status Order:** 1  
**Description:** New lead entry - initial status  

**Workflows (fire automatically on entry):**

- **New Lead Notification**
  - ID: `52330000000427010`
  - Trigger: automatic
  - Action: Sends email notification to team
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000427010)

- **CallWithIn24Hours and Team Task**
  - ID: `52330000000864146`
  - Trigger: automatic
  - Action: Creates call task and team task for follow-up
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000864146)

- **Format Number**
  - ID: `52330000005789994`
  - Trigger: automatic
  - Action: Formats phone numbers to standard format
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789994)

- **Lead Owner Assignment**
  - ID: `52330000007257288`
  - Trigger: automatic
  - Action: Assigns lead to appropriate owner based on rules
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007257288)

- **Tag G-Series Leadership Leads**
  - ID: `52330000007732209`
  - Trigger: automatic
  - Action: Tags specific course type leads
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007732209)

**Field Update Workflows:**

- **Format Number on Edit**
  - ID: `52330000005817040`
  - Triggers when: Phone, Mobile changes
  - Action: Formats phone numbers when edited
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005817040)

- **Course Details Udpated**
  - ID: `52330000005569771`
  - Triggers when: Course lookup field changes
  - Action: Updates lead with course details when course selected
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005569771)

- **Update Address**
  - ID: `52330000005569800`
  - Triggers when: State1 field changes
  - Action: Updates address fields when state changes
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005569800)

- **updateLeadAddressAndRemoveMapFileds**
  - ID: `52330000010756411`
  - Triggers when: Country, City, State changes
  - Action: Updates address and removes map fields
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756411)

**Human Actions Required:**

- Contact lead within 24 hours
  - Task created automatically by workflow
  - Fields: Phone, Mobile, Email

- Select course
  - Fields: Course
  - ⚡ Triggers: Course Details Udpated
  - Link to Course record if lead interested

- Update lead details
  - Fields: First_Name, Last_Name, Phone, Mobile, Email, Company
  - Complete lead information

---

### New Lead - Website

**Status Order:** 2  
**Description:** Lead from website form submission  

**Workflows:** Same as New Lead (fires on create)

**Human Actions Required:**

- Contact lead within 24 hours
  - Website leads typically more qualified - prioritize contact

- Review course selection
  - Fields: Course, Course_Type
  - Check if lead selected course on website

---

### New Lead - Google Ads

**Status Order:** 3  
**Description:** Lead from Google Ads campaign  

**Workflows:** Same as New Lead (fires on create)

**Human Actions Required:**

- Review campaign details
  - Fields: GCLID, ZCAMPAIGNID, Keyword
  - Check which ad campaign generated lead

- Contact lead
  - Follow up on Google Ads lead

---

### New Lead - Linkedin

**Status Order:** 4  
**Description:** Lead from LinkedIn campaign  

**Workflows:** Same as New Lead (fires on create)

**Human Actions Required:**

- Contact lead
  - Follow up on LinkedIn lead

---

### New Lead - Facebook

**Status Order:** 5  
**Description:** Lead from Facebook campaign  

**Workflows:** Same as New Lead (fires on create)

**Human Actions Required:**

- Contact lead
  - Follow up on Facebook lead

---

### Contacted

**Status Order:** 6  
**Description:** Lead successfully contacted  

**Manual Workflows (user triggers):**

- **Create Team task in leads**
  - ID: `52330000002758376`
  - How to trigger: Set Create_task checkbox to TRUE
  - Action: Creates Team Task for follow-up
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002758376)

- **Send Course email**
  - ID: `52330000006093561`
  - How to trigger: Set Course_Email checkbox to TRUE
  - Action: Sends course details email to lead
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006093561)

**Human Actions Required:**

- Assess lead interest and qualification
  - Fields: Course, Course_Type
  - Determine if lead is interested in courses

- Determine payment method
  - Fields: Payment_source
  - Discuss payment options (credit card, invoice, private)

- Set WF_Action if ready to convert
  - Fields: WF_Action
  - Set conversion action if lead qualified

---

### Attempted to Contact

**Status Order:** 7  
**Description:** Attempted to contact lead but no response  

**Workflows:** None

**Human Actions Required:**

- Schedule follow-up
  - Fields: Follow_up_date
  - Set follow-up date for next contact attempt

- Try alternative contact method
  - Try email if phone didn't work, or vice versa

---

### Re-Attempt 1

**Status Order:** 8  
**Description:** First re-attempt to contact lead  

**Workflows:** None

**Human Actions Required:**

- Try different contact method
  - Use alternative phone number or email

- Schedule next attempt
  - Fields: Follow_up_date

---

### Re-Attempt 2

**Status Order:** 9  
**Description:** Second re-attempt to contact lead  

**Workflows:** None

**Human Actions Required:**

- Final attempt
  - Last attempt before marking as lost

---

### Re-Attempt 3

**Status Order:** 10  
**Description:** Third and final re-attempt to contact lead  

**Workflows:** None

**Human Actions Required:**

- Final contact attempt
  - Last attempt - if no response, mark as lost

---

### Interested

**Status Order:** 11  
**Description:** Lead is interested and qualified  

**Manual Workflows (user triggers):**

- **Generate Payment URL**
  - ID: `52330000008228472`
  - How to trigger: Set WF_Action = "Generate Payment URL"
  - Action: Generates Zoho Form payment link
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008228472)

- **Update Location URL**
  - ID: `52330000008158816`
  - How to trigger: Set WF_Action field
  - Action: Generates location selection form
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008158816)

**Human Actions Required:**

- Determine conversion path
  - Fields: WF_Action
  - Options:
    - "Generate Payment URL" (credit card)
    - "Convert Pay Via Invoice" (invoice)
    - "Convert Non Paying Lead" (private)
    - "Convert to Only Create a contact" (contact only)

- Set WF_Action field
  - ⚡ Triggers: Various conversion workflows
  - Set appropriate conversion action

---

### Course Purchased - Convert

**Status Order:** 12  
**Description:** Lead purchased course - ready to convert  

**Workflows (fire automatically on payment):**

- **Convert on Payment Success**
  - ID: `52330000008292523`
  - Trigger: automatic (Stripe webhook)
  - Action: Auto-converts lead when payment received via Stripe
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523)

**Human Actions Required:**

- Verify payment received
  - Fields: Stripe_ID, Payment_CODE
  - Check if payment confirmed

- Monitor conversion
  - Check modules: Contacts, Accounts, Deals, Registration_Records, Invoices
  - Verify conversion workflow created records

---

### Convert - Create Records

**Status Order:** 13  
**Description:** Lead converted - records created  

**Conversion Workflows:**

- **Convert on Payment Success**
  - ID: `52330000008292523`
  - Trigger: automatic (Stripe webhook)
  - Creates: Contact, Account, Deal, Registration_Record, Invoice
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523)

- **Convert Pay Via Invoice**
  - ID: `52330000008920352`
  - Trigger: manual (WF_Action field)
  - Creates: Contact, Account, Deal, Registration_Record, Invoice
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008920352)

- **Convert Non Paying Lead**
  - ID: `52330000008250081`
  - Trigger: manual (WF_Action field)
  - Creates: Contact, Account, Deal
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008250081)

- **Convert to Only Create a contact**
  - ID: `52330000008405346`
  - Trigger: manual (WF_Action field)
  - Creates: Contact
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008405346)

**Human Actions Required:**

- Verify conversion records
  - Check created records in related modules
  - Fields: Converted_Contact, Converted_Account, Converted_Deal

- Verify Converted__s = TRUE
  - Fields: Converted__s
  - Ensure conversion flag is set

---

### Private Lead

**Status Order:** 14  
**Description:** Private course enquiry - requires quote/PO process  

**Workflows:** None (conversion via WF_Action)

**Human Actions Required:**

- Set WF_Action to Convert Non Paying Lead
  - Fields: WF_Action
  - ⚡ Triggers: Convert Non Paying Lead
  - Convert to Deal for private course quote process

- Gather requirements
  - Fields: Course, Course_Type, Number_of_Attendees
  - Document private course requirements

---

### Junk Lead

**Status Order:** 15  
**Description:** Invalid or spam lead  

**Human Actions Required:**

- Document reason
  - Fields: Description
  - Note why lead is junk

---

### Lost Lead

**Status Order:** 16  
**Description:** Lead lost - not interested or unresponsive  

**Human Actions Required:**

- Document loss reason
  - Fields: Description
  - Note why lead was lost

---

### Not Qualified

**Status Order:** 17  
**Description:** Lead not qualified for courses  

**Human Actions Required:**

- Document qualification reason
  - Fields: Description
  - Note why lead is not qualified

- Consider converting to contact only
  - Fields: WF_Action
  - Optional: May still convert to Contact for future reference

---

## Global Workflows (All Statuses)

These workflows apply across all lead statuses.

### Date/Time Triggered Workflows

- **setLeadGMapFiledsAsEmpty**
  - ID: `52330000010756363`
  - Trigger: date_or_datetime
  - Action: Clears Google Maps fields on schedule
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756363)

### Inactive Workflows

- **TEST SMS** (INACTIVE)
  - ID: `52330000008493195`
  - Trigger: field_update
  - Action: Testing workflow for SMS functionality
  - Status: Currently inactive
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008493195)

---

## Quick Reference - All Workflow URLs

| Workflow Name | ID | Status | Type | URL |
|--------------|----|----|------|-----|
| New Lead Notification | `52330000000427010` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000427010) |
| CallWithIn24Hours and Team Task | `52330000000864146` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000864146) |
| Format Number | `52330000005789994` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789994) |
| Lead Owner Assignment | `52330000007257288` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007257288) |
| Tag G-Series Leadership Leads | `52330000007732209` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007732209) |
| Format Number on Edit | `52330000005817040` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005817040) |
| Course Details Udpated | `52330000005569771` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005569771) |
| Update Address | `52330000005569800` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005569800) |
| updateLeadAddressAndRemoveMapFileds | `52330000010756411` | New_Lead | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756411) |
| Create Team task in leads | `52330000002758376` | Contacted | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002758376) |
| Send Course email | `52330000006093561` | Contacted | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006093561) |
| Generate Payment URL | `52330000008228472` | Interested | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008228472) |
| Update Location URL | `52330000008158816` | Interested | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008158816) |
| Convert on Payment Success | `52330000008292523` | Course_Purchased_Convert | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523) |
| Convert Pay Via Invoice | `52330000008920352` | Convert_Create_Records | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008920352) |
| Convert Non Paying Lead | `52330000008250081` | Convert_Create_Records | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008250081) |
| Convert to Only Create a contact | `52330000008405346` | Convert_Create_Records | manual | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008405346) |
| setLeadGMapFiledsAsEmpty | `52330000010756363` | Global | date_or_datetime | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756363) |
| TEST SMS | `52330000008493195` | Global | **inactive** | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008493195) |

---

**Last Updated:** 2025-11-18
**Source:** Zoho CRM Export 2025-11-13

