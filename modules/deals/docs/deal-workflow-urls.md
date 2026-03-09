# Deal Workflow URLs Reference

Quick access to all Deal-related workflows in Zoho CRM

## By Stage


### Qualification

**Stage Order:** 1  
**Description:** Initial deal assessment and data gathering  

**Workflows (fire automatically on entry):**

- **Update Deal ID**
  - ID: `52330000002444572`
  - Trigger: automatic
  - Action: Assigns Deal_CRM_ID field
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002444572)

- **Deal Naming Convention**
  - ID: `52330000002967279`
  - Trigger: automatic
  - Action: Formats Deal_Name field: [Course Type] - [Course] - [Date]
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967279)

- **Update Amount on create**
  - ID: `52330000003995130`
  - Trigger: create_or_edit (fires on both create AND edit)
  - Action: Calculates Amount from course fee × number of attendees
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995130)

- **Workflow - Update Deal ID**
  - ID: `52330000004452015`
  - Trigger: create_or_edit (fires on both create AND edit)
  - Action: Maintains Deal ID consistency
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004452015)

- **If Website Account Name**
  - ID: `52330000005157945`
  - Trigger: automatic
  - Action: Populates account name for web-originated deals
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005157945)

**Field Update Workflows:**

- **Copy of Deal Naming Convention**
  - ID: `52330000004013962`
  - Triggers when: Courseaa, Course_Type changes
  - Action: Updates Deal_Name to include course details
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004013962)

- **When Account name is not blank**
  - ID: `52330000005069264`
  - Triggers when: Account_Name changes
  - Action: Updates parent account and contact fields
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005069264)

**Human Actions Required:**

- Verify deal details
  - Fields: Deal_Name, Account_Name, Contact_Name
  - Confirm all contact information is correct

- Select course
  - Fields: Courseaa, Course_Type
  - ⚡ Triggers: Copy of Deal Naming Convention
  - Link to Course record or select course type

- Set number of attendees
  - Fields: Number_of_Attendees
  - ⚡ Triggers: Update Amount on create
  - Enter expected participant count

- Verify amount
  - Fields: Amount
  - Check auto-calculated amount is correct

---

### Negotiation Review

**Stage Order:** 2  
**Description:** Quote sent, awaiting client decision and purchase order

**Automatic Field-Update Workflows (trigger by setting checkbox fields):**

- **Email to training Coordinator from DEALS**
  - ID: `52330000002967852`
  - Trigger: field_update on Request_Attendees (automatic when checkbox changes)
  - Action: Sends email to Training Coordinator requesting attendee details
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967852)
  - Note: Fires automatically when Request_Attendees field changes. Works in any stage. Repeatable.

- **Create Team Task from Deals**
  - ID: `52330000002460147`
  - Trigger: field_update on Create_Follow_up_Task (automatic when checkbox changes)
  - Action: Creates Team Task for follow-up
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460147)
  - Note: Fires automatically when Create_Follow_up_Task field changes. Works in any stage. Repeatable.  

**Time-Based Workflows:**

- **Follow up on Purchase Order 28 days before**
  - ID: `52330000002638311`
  - Timing: 28 days before course
  - Action: Creates Team Task to chase PO if not received
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311)

- **Follow up on Purchase Order 14 days before course**
  - ID: `52330000002638269`
  - Timing: 14 days before course
  - Action: Creates Team Task to chase PO
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269)

- **Follow up on Purchase Order 1 days before**
  - ID: `52330000002638411`
  - Timing: 1 day before course
  - Action: Creates urgent Team Task - PO still missing
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638411)

**Stage Update Workflows:**

- **Follow up on Purchase Order 5 days before course**
  - ID: `52330000009085891`
  - Trigger: field_update on Stage (NOT time-based)
  - Action: Creates Team Task if still in negotiation
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085891)
  - Note: Despite the name, this fires on Stage field changes, not on a schedule. Has internal condition logic.

- **Follow up future deals**
  - ID: `52330000001178038`
  - Timing: On follow-up date
  - Action: Creates follow-up task for future dated deals
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000001178038)

**Human Actions Required:**

- Chase purchase order
  - Fields: Purchase_Order_Number, Po_Expected_Date
  - Contact client to obtain PO number

- Negotiate terms
  - Fields: Quote_Amount, Po_Expected_Date
  - Discuss pricing, dates, terms with client

- Update PO details in Quote
  - Fields: Expected_PO_Date, PO_Number
  - ⚡ Triggers: Update Deal with PO Number and Date
  - Enter PO details when received

- Set Quote status
  - Fields: Quote_Stage
  - Update to Accepted when client confirms

---

### Ready To Quote

**Stage Order:** 3  
**Description:** Quote automatically generated when stage entered  

**Workflows (fire automatically on entry):**

- **Create Quote - Stage Update Ready to quote**
  - ID: `52330000002460308`
  - Trigger: field_update on Stage (fires on ANY stage change)
  - Action: AUTO-CREATES Quote record linked to this Deal
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308)
  - Note: Fires on any Stage field change with internal condition checking Stage = "Ready to Quote"

**Human Actions Required:**

- Review auto-generated quote
  - Check Quote module for new quote linked to this deal

- Adjust pricing if needed
  - Fields: Quoted_Items (subform), Discount
  - Modify line items or add discounts

- Set valid until date
  - Fields: Valid_Till
  - Quote expiry date

- Send quote to client
  - Fields: Send_Quote_as_EMAIL
  - ⚡ Triggers: Send Quote (in Quotes module)
  - Set to TRUE to email quote

---

### Awaiting ZipPay Confirmation

**Stage Order:** 4  
**Description:** Awaiting ZipPay payment confirmation  

**Workflows:** None

**Human Actions Required:**

- Monitor ZipPay payment status
  - Fields: Payment_source, Payment_Status

- Set course start date
  - Fields: Course_Start_Date

---

### Awaiting Purchase Order

**Stage Order:** 5  
**Description:** Quote accepted, awaiting purchase order from client  

**Workflows:** None

**Human Actions Required:**

- Chase purchase order
  - Fields: Purchase_Order_Number, Po_Expected_Date

- Update PO details when received
  - Fields: Purchase_Order_Number
  - ⚡ Triggers: Purchase Order Received + Update Registration records

---

### Awaiting Invoice Payment

**Stage Order:** 6  
**Description:** Invoice sent, awaiting payment from client  

**Workflows:** None

**Human Actions Required:**

- Monitor invoice payment status
  - Module: Invoices
  - Fields: Status

- Follow up on payment
  - Fields: Payment_Status

---

### Unused

**Stage Order:** 7  
**Description:** Deal temporarily set aside or on hold  

**Workflows:** None (except Follow up future deals if Follow_up_date set)

**Human Actions Required:**

- Document reason for hold
  - Fields: Follow_Up_Notes

- Set follow-up date
  - Fields: Follow_up_date
  - ⚡ Triggers: Follow up future deals

---

### Closed Won

**Stage Order:** 8  
**Description:** Quote accepted, PO received, deal won  

**Field-Update Workflows (fire when PO# entered or Stage changes):**

- **Purchase Order Received**
  - ID: `52330000002460283`
  - Trigger: field_update on Purchase_Order_Number (fires in ANY stage when PO# entered)
  - Action: Updates deal status, notifies team, timestamps PO receipt
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460283)
  - Note: Not stage-specific - fires whenever Purchase_Order_Number field is updated

- **Update Registration records when PO Is received**
  - ID: `52330000006993545`
  - Trigger: field_update on Purchase_Order_Number (fires in ANY stage when PO# entered)
  - Action: Updates all Registration_Records linked to this Deal → Status = Confirmed
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006993545)
  - Note: Not stage-specific - fires whenever Purchase_Order_Number field is updated

- **On stage Update related Attendees**
  - ID: `52330000004335567`
  - Trigger: field_update on Stage (fires on ANY stage change, not just Closed Won)
  - Action: Updates Registration_Records → Status = Confirmed (if payment confirmed)
  - 🔗 [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004335567)
  - Note: Fires on any Stage field change with internal condition logic

**Human Actions Required:**

- Enter Purchase Order Number
  - Fields: Purchase_Order_Number
  - ⚡ Triggers: Purchase Order Received + Update Registration records
  - Enter PO number from client

- Verify invoice created
  - Check if invoice was auto-created by Quote acceptance

- Verify registrations confirmed
  - Check all Registration_Records for this course have Status = Confirmed

- Monitor payment
  - Fields: Status
  - Track invoice payment status

---

### Closed Lost

**Stage Order:** 9  
**Description:** Quote declined or deal abandoned  

**Human Actions Required:**

- Enter loss reason
  - Fields: Loss_Reason
  - Document why deal was lost (MANDATORY)

- Update Quote status
  - Fields: Quote_Stage
  - Set Quote_Stage to 'Declined' or 'Closed Lost'

- Cancel registrations if created
  - Fields: Status
  - Set Status to 'Cancelled' for any registrations

---

## Quick Reference - All Workflow URLs

| Workflow Name | ID | Stage | Type | URL |
|--------------|----|----|------|-----|
| Update Deal ID | `52330000002444572` | Qualification | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002444572) |
| Deal Naming Convention | `52330000002967279` | Qualification | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967279) |
| Update Amount on create | `52330000003995130` | Qualification | create_or_edit | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995130) |
| Workflow - Update Deal ID | `52330000004452015` | Qualification | create_or_edit | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004452015) |
| If Website Account Name | `52330000005157945` | Qualification | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005157945) |
| Copy of Deal Naming Convention | `52330000004013962` | Qualification | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004013962) |
| When Account name is not blank | `52330000005069264` | Qualification | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005069264) |
| Email to training Coordinator from DEALS | `52330000002967852` | Negotiation_Review | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967852) |
| Create Team Task from Deals | `52330000002460147` | Negotiation_Review | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460147) |
| Create Quote - Stage Update Ready to quote | `52330000002460308` | Ready_to_Quote | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308) |
| Follow up on Purchase Order 28 days before | `52330000002638311` | Negotiation_Review | date_or_datetime | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311) |
| Follow up on Purchase Order 14 days before course | `52330000002638269` | Negotiation_Review | date_or_datetime | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269) |
| Follow up on Purchase Order 1 days before | `52330000002638411` | Negotiation_Review | date_or_datetime | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638411) |
| Follow up on Purchase Order 5 days before course | `52330000009085891` | Any | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085891) |
| Follow up future deals | `52330000001178038` | Any | date_or_datetime | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000001178038) |
| Purchase Order Received | `52330000002460283` | Any | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460283) |
| Update Registration records when PO Is received | `52330000006993545` | Any | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006993545) |
| On stage Update related Attendees | `52330000004335567` | Any | field_update | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004335567) |
| Update Deal stage when 1 attendee, qualification and public | `52330000004434048` | Qualification | automatic | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004434048) |

---

## Additional Workflow Details

### Update Deal stage when 1 attendee, qualification and public

**Workflow ID:** `52330000004434048`
**URL:** [Open in Zoho](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004434048)
**Trigger:** On create (fires when Deal record is created)
**Status:** INACTIVE

**Conditions:**
- Number_of_Attendees = 1
- Course_Type = "Public"
- Checks Account's Po_Required field

**Actions:**
1. Skips execution if attendeeNum != 1 or courseType != "Public"
2. If Account.Po_Required = true, skips quote creation
3. Updates Deal Stage to "Awaiting Invoice Payment"
4. Creates and sends invoice

**Notes:** This workflow is currently INACTIVE (status: false). It was designed to fast-track single-attendee public course deals by skipping the quote stage when no PO is required, automatically moving to invoice generation. Last executed: 2025-07-01. Created by Nathan.
