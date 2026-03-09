# Course Integration Flows

**Last Updated:** 10 December 2025 (aligned to 2025-12-10 export)
**Modules:** Courses, Registration_Records, Invoices
**External Systems:** WordPress, Workdrive, Xero, Stripe, ClickSend
**Status:** Outline - To be expanded

---

## Overview

This document details how the Courses module and related modules integrate with external systems:
- **WordPress** - Public course calendar and listings
- **Workdrive** - Document and material storage
- **Xero** - Accounting and invoicing
- **Stripe** - Payment processing
- **ClickSend** - SMS notifications

---

## WordPress Integration

### Course Publication Flow

**Trigger:** Course.Course_Status = 'Sync to Wordpress'

**WF: 52330000006315389 - Sync Course to Wordpress**
- Syncs course data to WordPress
- Creates WP_Course_ID
- Populates Event_URL with public course page

**Fields Synced:**
- Course Name
- Course_Description
- Course_Summary
- Course_Start_Time
- Course_End_Time
- Select_Venue
- Fees
- Course_Qualification

**WordPress Output:**
- Public course listing page
- Event calendar entry
- Registration form link

---

### Course Confirmation → Website Calendar

**WF: 52330000011998036 - Course Confirmed - Website Calendar**
- **Trigger:** Course.Course_Confirmed = true
- **Action:** Updates WordPress calendar with confirmed course
- **URL:** [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000011998036)

---

### Course Completion → WordPress Update

**WF: 52330000004065214 - Completed course for WP**
- **Trigger:** Time-based, after Course_Start_Time
- **Action:** Marks course as completed on WordPress
- **Purpose:** Removes from upcoming courses list

---

## Workdrive Integration

### Folder Creation on Course Create

**WF: 52330000002462001 - Courses_ZohoFlow_CRM Course to Workdrive Folder**
- **Trigger:** Course record created
- **Action:** Creates Workdrive folder structure
- **URL:** [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002462001)

**Folder Structure:**
```
/Courses/
  └── {Course_Name}/
      ├── Course Materials/
      ├── Attendees/
      │   └── {Attendee_Name}/
      │       ├── Compliance Documents/
      │       └── Certificates/
      └── Trainer Resources/
```

---

### Attendee Folder Management

**WF: 52330000005375288 - Move Course Attendee Folder on Course Change**
- **Trigger:** Registration.Course field changes
- **Action:** Moves attendee folder to new course folder
- **Use Case:** Student rescheduled to different course

---

### Workdrive URL Field

**Field:** Course.Workdrive_URL
- Stores link to course folder
- Populated by workflow on folder creation
- Used in trainer emails and notifications

---

## ClickSend SMS Integration

### Trainer SMS Notifications

**Automatic SMS Workflows:**

**1. 10 Days Before Course**
- **WF:** 52330000002656676 - 10 days before course SMS to Trainer
- **Timing:** 10 days before Course_Start_Time
- **Recipient:** Course_Trainer (via Trainer_Mobile field)
- **Content:** Course reminder, logistics details

**2. 1 Day Before Course**
- **WF:** 52330000002656692 - 1 day before course SMS to Trainer
- **Timing:** 1 day before Course_Start_Time
- **Recipient:** Course_Trainer
- **Content:** Final reminder, attendance sheet link

---

### Student SMS Notifications

**From Registration_Records Module:**

**Public Courses:**
- WF: 52330000002597951 - 7 Days before Public course SMS Reminder
- Timing: 7 days before course
- Recipients: All confirmed registrations

**Private Courses:**
- WF: 52330000005163433 - 7 Days before Private Confirmed course SMS Reminder
- Timing: 7 days before private confirmed course

**SMS Opt-Out:**
- Field: Course.SMS_Opt_Out
- If true, SMS workflows do not fire for this course

---

## Xero Integration

### Invoice Sync on Payment

**WF: 52330000002460231 - Push Invoice to Xero**
- **Trigger:** Invoice.Status = 'Paid'
- **Action:** Syncs invoice to Xero accounting
- **URL:** [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460231)

**Data Synced:**
- Invoice number
- Invoice date
- Due date
- Line items (course fees)
- GST amounts
- Customer (Account)
- Payment status

**Fields Updated:**
- Invoice.Xero_Invoice_URL
- Invoice.Xero_Invoice_Number

---

### Course Revenue Coding

**Fields:**
- Course.Xero_Account_Code - Revenue account code
- Course.Xero_Product_Code - Product/service code

**Purpose:**
- Ensures correct revenue categorization in Xero
- Maps to chart of accounts

---

## Stripe Integration

### Payment Processing

**Webhook Integration:**
- Stripe payment webhook updates Invoice.Status
- Invoice.Stripe_ID stores transaction ID
- Invoice.Merchant_Fee records processing fee

**Payment Fields:**
- Invoice.Payment_Source = 'Stripe'
- Invoice.Payment_Type
- Invoice.Last_Payment_Amount
- Invoice.Last_Payment_Date

**Flow:**
```
Student clicks payment link
    ↓
Stripe processes payment
    ↓
Webhook fires → Updates Invoice.Status = 'Paid'
    ↓
Triggers downstream workflows:
  - Update Deal Amount
  - Sync to Xero
  - Update Registration
```

---

### Payment Security

**PCI Compliance:**
- Full card details NEVER stored in CRM
- Only Stripe_ID (transaction reference) stored
- Stripe handles all sensitive data

---

## Integration Summary

### System-to-Module Mapping

| External System | Modules Affected | Primary Use Case |
|----------------|------------------|------------------|
| WordPress | Courses | Public course marketing |
| Workdrive | Courses, Registration_Records | Document storage |
| ClickSend | Courses, Registration_Records | SMS notifications |
| Xero | Invoices, Deals | Accounting sync |
| Stripe | Invoices | Payment processing |

---

### Workflow Count by Integration

| Integration | Workflow Count | Automatic | Manual |
|------------|---------------|-----------|--------|
| WordPress | 3 | 3 | 0 |
| Workdrive | 2 | 2 | 0 |
| ClickSend | 4+ | 4+ | 0 |
| Xero | 1 | 1 | 0 |
| Stripe | Webhook | 1 | 0 |

---

## Security & Compliance

### API Keys Storage

**Best Practices:**
- API keys stored in Zoho Connections (NOT in CRM fields)
- OAuth tokens for Xero
- Stripe webhook signing secret

### Data Privacy

**PII Considerations:**
- Student data in ClickSend (phone numbers)
- Financial data in Xero (payment amounts)
- Documents in Workdrive (compliance records)

**Retention:**
- Workdrive: 7 years (RTO compliance)
- Xero: 7 years (tax requirements)
- Stripe: Transaction history retained

---

## Troubleshooting

### WordPress Sync Fails

**Symptoms:**
- Course.WP_Course_ID not populated
- Event_URL empty

**Solutions:**
1. Verify WF: 52330000006315389 is active
2. Check WordPress API credentials
3. Verify Course_Description and Course_Summary are populated

---

### Workdrive Folder Not Created

**Symptoms:**
- Course.Workdrive_URL empty

**Solutions:**
1. Verify WF: 52330000002462001 is active
2. Check Zoho Flow connection to Workdrive
3. Verify course name doesn't contain invalid characters

---

### SMS Not Sending

**Symptoms:**
- Trainer doesn't receive SMS reminder

**Solutions:**
1. Verify Course.Trainer_Mobile is populated
2. Verify Course.SMS_Opt_Out = false
3. Check ClickSend credit balance
4. Verify workflow execution log

---

### Xero Sync Fails

**Symptoms:**
- Invoice.Xero_Invoice_URL empty after marking paid

**Solutions:**
1. Verify Invoice.Status = 'Paid' (exact value)
2. Check Xero API connection
3. Verify Invoice has all required fields (Account_Name, Due_Date, line items)
4. Check workflow execution log for errors

---

## Related Documentation

- [Courses Module - Workflows](../../modules/courses/docs/courses-workflows.md)
- [Invoices Module - Workflows](../../modules/invoices/docs/invoices-workflows.md)
- [Course → Registration Flow](course-registration-flow.md)
- [Registration → Invoice Flow](registration-invoice-flow.md)

---

**Note:** This document provides an outline of external system integrations. For complete API specifications and configuration details, consult with the system administrator.

**To be expanded with:**
- Complete API endpoint documentation
- Webhook payload specifications
- Error code reference
- Security audit procedures
- Compliance documentation
