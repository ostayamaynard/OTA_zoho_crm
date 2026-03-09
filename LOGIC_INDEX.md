# Logic Index - Zoho CRM Automation Map

**Purpose:** Root-level reference for all active workflows, triggers, and automations across the Zoho CRM system.
**Last Updated:** 2025-12-10 (content based on 2025-12-10 export)
**Source:** `data/exports/zoho-dependencies-2025-12-10.json` (use `tools/update_pipeline.py` for newer exports)

---

## Quick Reference

| Module | Active Workflows | Key Automation Areas |
|--------|-----------------|---------------------|
| [Courses](#courses-37-workflows) | 34 | Course lifecycle, trainer notifications, WordPress sync |
| [Registration Records](#registration-records-36-workflows) | 30 | Attendee management, payment processing, reminders |
| [Leads](#leads-19-workflows) | 18 | Lead capture, conversion, data quality |
| [Deals](#deals-19-workflows) | 18 | Pipeline automation, PO reminders, quote generation |
| [Invoices](#invoices-15-workflows) | 13 | Payment processing, Xero sync, Stripe integration |
| [Quotes](#quotes-8-workflows) | 7 | Quote generation, tax calculation, Xero sync |
| [Contacts](#contacts-7-workflows) | 7 | Data quality, Xero sync, folder creation |
| [Accounts](#accounts-4-workflows) | 4 | Data quality, Xero sync, folder creation |
| [Team Tasks](#team-tasks-3-workflows) | 3 | Task automation, status updates |
| [Projects Inhouse](#projects-inhouse-2-workflows) | 2 | Project tracking |
| [Calls](#calls-1-workflow) | 1 | Call logging |
| [Events](#events-1-workflow) | 1 | Event management |
| [Sales Orders](#sales-orders-1-workflow) | 1 | SO naming conventions |
| [ClickSend SMS](#clicksend-sms-1-workflow) | 1 | SMS integration |

**Total Active Workflows:** 144 across 14 modules

---

## Trigger Type Guide

Understanding when workflows execute:

| Trigger Type | When It Fires | Example Use Case |
|-------------|--------------|-----------------|
| **create** | New record is created | Send welcome email to new lead |
| **field_update** | Specific field(s) change | Update course details when status changes |
| **edit** | Any field is modified | Sync data to external system on any update |
| **create_or_edit** | Record created OR edited | Format phone number on create/edit |
| **date_or_datetime** | Scheduled date/time is reached | Send course reminder 7 days before start |
| **outgoing_call_createedit** | Call is logged | Create follow-up task after call |

---

## Courses (37 Workflows)

**Business Context:** Most complex module - manages entire course lifecycle from creation to completion.

### Course Creation & Setup
- **Create Course Registration** (create) → Creates initial registration records
- **Set Course Name** (create) → Enforces naming conventions
- **Duplicate Course Code** (create) → Prevents duplicate course codes
- **Create Workdrive Folder** (create) → Sets up document storage
- **Default for Trainers** (create) → Assigns default trainer values

### Pre-Course Automation
- **Create Trainer Meetings** (field_update: `Trainer`) → Schedules trainer sessions
- **Course SMS Reminder 11 days** (date_or_datetime: `Start_Date`) → SMS to trainer 11 days before
- **Course SMS Reminder 10 days** (date_or_datetime: `Start_Date`) → SMS to trainer 10 days before
- **Course SMS Reminder 7 days** (date_or_datetime: `Start_Date`) → SMS to trainer 7 days before
- **Course SMS Reminder 1 day** (date_or_datetime: `Start_Date`) → SMS to trainer 1 day before
- **Trainer Email 10 days before** (date_or_datetime: `Start_Date`) → Detailed pre-course email
- **Trainer Email 5 days before** (date_or_datetime: `Start_Date`) → Reminder email
- **Trainer Email 2 days before** (date_or_datetime: `Start_Date`) → Final preparation email

### During Course
- **Upload Materials** (field_update: `Upload_Materials`) → Processes course materials
- **Task Email Confirmations** (field_update: `Tasks_to_Email`) → Sends confirmations to attendees
- **Attendance PDF** (field_update: `Attendance_PDF`) → Generates attendance records

### Post-Course
- **Course Completed** (field_update: `Stage`) → Triggers completion workflows
- **Performance Check** (date_or_datetime: `End_Date`) → Evaluates course performance
- **Send Post Course Data to Trainer** (field_update: `Post_course_data_sent`) → Shares results with trainer
- **Task Completed** (field_update: `Stage`) → Updates task status

### Status & Visibility Management
- **Update Course Status - Private** (field_update: `Course_Type`) → Manages private courses
- **Update Course Status - Public** (field_update: `Course_Type`) → Manages public courses
- **Cancelled Course** (field_update: `Stage`) → Handles cancellations

### Integration & Sync
- **Course Sync To WordPress** (field_update: `Type`, `Stage`) → Publishes to website
- **WordPress Calendar** (field_update: `Course_Type`, `Start_Date`) → Updates website calendar
- **Update Contacts Details form** (field_update: `Update_Details`) → Syncs attendee data

### Data Quality
- **Update Address** (field_update: `Location`) → Formats address fields
- **Update State** (field_update: `State1`) → Standardizes state values
- **Calculate Total Reg** (field_update: `Total_Registrations`) → Recalculates totals

### Financial
- **Course Price Public inc GST** (field_update: `Course_Price_Public_Including_GST`) → Calculates pricing
- **Course Price Private inc GST** (field_update: `Course_Price_Private_Including_GST`) → Calculates pricing

---

## Registration Records (36 Workflows)

**Business Context:** Manages entire attendee lifecycle from registration to post-course follow-up. Critical for revenue tracking.

### Registration Creation
- **Set Registration Name** (create) → Enforces naming conventions
- **Create Registration** (create) → Initializes new registration
- **Calculate Registration Fee** (field_update: `Course`, `Type`) → Calculates fees based on course/type
- **Calculate Total After Discount** (field_update: `Discount`) → Applies discounts
- **Update Overall Tax** (field_update: `Tax`) → Calculates final tax

### Payment Processing
- **Create Payment Link** (field_update: `Create_Payment_Link`) → Generates Stripe payment URL
- **Refresh Payment Link** (field_update: `Refresh_Payment_Link`) → Regenerates payment URL
- **Reg Record Confirmation - Paid** (field_update: `Payment_Status`) → Sends confirmation when paid
- **Update Invoices** (field_update: `Payment_Status`) → Updates linked invoices
- **Update Deal with Payment** (field_update: `Payment_Status`) → Updates linked deals

### Pre-Course Communication
- **Pre Arrival Survey 1 Week** (date_or_datetime: `Course_Start_Date`) → Survey 1 week before
- **Pre_Arrival Survey 7 days** (date_or_datetime: `Course_Start_Date`) → Survey 7 days before
- **SMS Reminder 7 days before** (date_or_datetime: `Course_Start_Date`) → SMS reminder
- **Email Confirmation 7 days before** (date_or_datetime: `Course_Start_Date`) → Email reminder
- **SMS Reminder 1 day before** (date_or_datetime: `Course_Start_Date`) → Final SMS reminder

### Attendance Tracking
- **Mark No Show Same Day** (date_or_datetime: `Course_Start_Date`) → Tracks attendance on course day
- **Mark No Show 1 Day After** (date_or_datetime: `Course_Start_Date`) → Updates no-show status
- **Mark No Show 1 Week After** (date_or_datetime: `Course_Start_Date`) → Final attendance update

### Post-Course
- **Send Feedback Request** (date_or_datetime: `Course_End_Date`) → Requests course feedback
- **Thank You Email** (date_or_datetime: `Course_End_Date`) → Sends thank you message
- **Thank You SMS** (date_or_datetime: `Course_End_Date`) → Sends thank you SMS
- **Issue Certificate** (field_update: `Certificate_Issued`) → Generates and sends certificate

### Cross-Module Updates
- **Update Course Registrations** (field_update: `Payment_Status`) → Updates course record
- **Update Deal Registrations** (field_update: `Payment_Status`) → Updates deal record
- **Update Contact from Registration** (field_update: multiple) → Syncs contact data
- **Update Account from Registration** (field_update: multiple) → Syncs account data

### Data Quality
- **Format Phone Number** (create_or_edit: `Phone`, `Mobile`) → Standardizes phone format
- **Update Address** (field_update: `State`) → Formats address
- **Calculate Attendee Count** (field_update: `Attendee_Status`) → Updates counts

---

## Leads (19 Workflows)

**Business Context:** First point of contact - handles lead capture, qualification, and conversion to customers.

### Lead Capture & Notification
- **New Lead Notification** (create) → Notifies team of new leads
- **Lead Owner Assignment** (create) → Assigns leads to team members
- **CallWithIn24Hours and Team Task** (create) → Creates follow-up task for 24hr call

### Lead Conversion
- **Convert Non Paying Lead** (field_update: `Payment_Status`) → Converts free attendees
- **Convert Lead and update Attendees** (field_update: `Payment_Status`) → Full conversion with payment
- **Convert Lead to Contact** (field_update: `Payment_Status`) → Creates contact record
- **Update Deals and Attendees on Paid** (field_update: `Payment_Status`) → Updates related records

### Data Quality
- **Format Number** (create) → Formats phone on creation
- **Format Number on Edit** (field_update: `Phone`, `Mobile`) → Formats phone on edit
- **Update Address** (field_update: `State1`) → Standardizes address fields

### Course Management
- **Course Details Updated** (field_update: `Course`) → Syncs course information
- **Send Course Email** (field_update: `Send_Course_Email`) → Sends course details
- **Create Task in Leads** (field_update: `Create_task`) → Creates follow-up tasks

### Communication
- **Send Payment URL** (field_update: `Send_Payment_URL`) → Sends Stripe payment link
- **Refresh Payment Link** (field_update: `Refresh_Payment_Link`) → Regenerates payment URL

### Lead Tagging & Qualification
- **Tag G-Series Leadership Leads** (field_update: `Course`) → Tags leadership program leads
- **Lead Qualification Score** (field_update: multiple) → Calculates lead score

---

## Deals (19 Workflows)

**Business Context:** Sales pipeline automation - tracks opportunities from quote to close.

### Deal Creation
- **Set Deal ID** (create) → Generates unique deal identifier
- **Set Deal Name** (create) → Enforces naming conventions
- **Calculate Deal Amount** (field_update: `Quantity`, `Unit_Price`) → Calculates total value

### Quote Generation
- **Create Quote at Stage** (field_update: `Stage`) → Auto-generates quote at specific stage
- **Create Quote for Deal** (field_update: `Create_Quote`) → Manual quote generation trigger

### Purchase Order Management
- **PO Follow Up 28 days** (date_or_datetime: `Course_Start_Date`) → PO reminder 28 days before
- **PO Follow Up 14 days** (date_or_datetime: `Course_Start_Date`) → PO reminder 14 days before
- **PO Follow Up 5 days** (date_or_datetime: `Course_Start_Date`) → PO reminder 5 days before
- **PO Follow Up 1 day** (date_or_datetime: `Course_Start_Date`) → Final PO reminder

### Registration & Attendee Management
- **Create Registrations for Deal** (field_update: `Create_Registrations`) → Generates registration records
- **Update Attendee Count** (field_update: `Number_of_Attendees`) → Updates attendee numbers
- **Calculate Registrations Count** (field_update: `Registration_Status`) → Recalculates totals

### Stage Management
- **Update Deal Stage** (field_update: `Qualification_Status`) → Moves deal through pipeline
- **Deal Won** (field_update: `Stage`) → Triggers win workflows
- **Deal Lost** (field_update: `Stage`) → Handles lost opportunities

### Financial
- **Calculate Tax** (field_update: `Tax_Type`) → Calculates tax amounts
- **Apply Discount** (field_update: `Discount_Percentage`) → Applies discounts
- **Update Invoice Link** (field_update: `Invoice_Created`) → Links to invoices

---

## Invoices (15 Workflows)

**Business Context:** Financial processing - manages billing, payment tracking, and accounting sync.

### Invoice Creation
- **Set Invoice Number** (create) → Generates sequential invoice numbers
- **Auto-populate Invoice Details** (create) → Copies data from deal/registration
- **Calculate Due Date** (create) → Sets payment due date based on terms

### Tax & Pricing
- **Calculate Tax Amount** (field_update: `Tax_Type`) → Calculates GST/tax
- **Calculate Overall Tax** (field_update: `Tax`) → Recalculates total with tax
- **Apply Discount to Invoice** (field_update: `Discount`) → Applies discount amounts

### Payment Processing
- **Create Payment URL** (field_update: `Create_Payment_URL`) → Generates Stripe payment link
- **Refresh Payment Link** (field_update: `Refresh_Payment_Link`) → Regenerates Stripe link
- **Payment Received** (field_update: `Status`) → Triggers payment received workflows
- **Update Payment Status** (field_update: `Payment_Status`) → Syncs payment status

### Integration - Xero Accounting
- **Sync Invoice to Xero** (field_update: `Status`) → Sends invoice to Xero
- **Update Xero Invoice** (edit) → Syncs changes to Xero

### Communication
- **Send Invoice Email** (field_update: `Send_Invoice`) → Emails invoice to customer
- **PO Confirmation Email** (field_update: `PO_Received`) → Confirms PO receipt

---

## Quotes (8 Workflows)

**Business Context:** Quote generation and management - supports sales process.

### Quote Creation
- **Generate Quote ID** (create) → Creates unique quote identifier
- **Set Quote Name** (create) → Enforces naming conventions
- **Auto-populate Quote Details** (create) → Copies data from deal

### Pricing & Tax
- **Calculate Quote Tax** (field_update: `Tax_Type`) → Calculates tax amounts
- **Calculate Quote Total** (field_update: `Discount`) → Calculates final total
- **Set Due Date** (create) → Sets quote expiration date

### Integration
- **Sync Quote to Xero** (field_update: `Status`) → Sends quote to Xero
- **Create Payment URL** (field_update: `Generate_Payment_Link`) → Generates payment link

---

## Contacts (7 Workflows)

**Business Context:** Customer contact management - maintains individual contact records.

### Data Quality
- **Format Contact Phone** (create) → Formats phone on creation
- **Format Phone on Edit** (field_update: `Phone`, `Mobile`) → Formats phone on edit
- **Update Contact Address** (field_update: `State`) → Standardizes address fields

### Integration
- **Sync Contact to Xero** (field_update: multiple) → Syncs to Xero contacts
- **Create Workdrive Folder** (create) → Creates document storage folder

### Task Management
- **Create Team Task for Contact** (field_update: `Create_Task`) → Creates follow-up tasks
- **Update Contact Details Form** (field_update: `Update_Details`) → Updates related forms

---

## Accounts (4 Workflows)

**Business Context:** Company/organization management - maintains business account records.

### Data Quality
- **Update Account Address** (field_update: `State`) → Standardizes address fields
- **Clean Google Maps Data** (field_update: `Address`) → Removes map formatting

### Integration
- **Sync Account to Xero** (edit) → Syncs to Xero customers
- **Create Workdrive Folder** (create) → Creates document storage folder

---

## Team Tasks (3 Workflows)

**Business Context:** Task automation - manages follow-up tasks across all modules.

### Task Automation
- **Update Task Status** (field_update: `Status`) → Automatically updates status
- **Calculate Due Date** (create) → Sets due date based on priority
- **Task Completion Notification** (field_update: `Status`) → Notifies assignee on completion

---

## Projects Inhouse (2 Workflows)

**Business Context:** Internal project tracking.

### Project Management
- **Set Project Name** (create) → Enforces naming conventions
- **Update Project Status** (field_update: `Stage`) → Manages project lifecycle

---

## Calls (1 Workflow)

**Business Context:** Call logging and tracking.

### Call Management
- **Log Outgoing Call** (outgoing_call_createedit) → Creates call record and follow-up task

---

## Events (1 Workflow)

**Business Context:** Event management.

### Event Management
- **Set Event Name** (create) → Enforces naming conventions

---

## Sales Orders (1 Workflow)

**Business Context:** Sales order processing.

### SO Management
- **Set SO Name** (create) → Enforces naming conventions

---

## ClickSend SMS (1 Workflow)

**Business Context:** SMS integration module.

### SMS Integration
- **ClickSend SMS Sent** (field_update: `Status`) → Logs SMS delivery status

---

## External System Integrations

### Xero Accounting (5 workflows)
- **Contacts** → Sync Contact to Xero
- **Accounts** → Sync Account to Xero
- **Invoices** → Sync Invoice to Xero, Update Xero Invoice
- **Quotes** → Sync Quote to Xero

### WordPress Website (3 workflows)
- **Courses** → Course Sync To WordPress, WordPress Calendar

### Workdrive Document Storage (2 workflows)
- **Contacts** → Create Workdrive Folder
- **Accounts** → Create Workdrive Folder (Courses also creates folders)

### Stripe Payment Processing (4+ workflows)
- **Leads** → Send Payment URL, Refresh Payment Link
- **Registration Records** → Create Payment Link, Refresh Payment Link
- **Invoices** → Create Payment URL, Refresh Payment Link

### ClickSend SMS (3+ workflows)
- **Courses** → Multiple SMS reminder workflows
- **Registration Records** → SMS reminder workflows
- **ClickSend SMS Module** → Status tracking

---

## Cross-Module Automation Chains

### Lead → Contact → Deal → Registration → Invoice
1. **Lead created** → New Lead Notification, Owner Assignment
2. **Payment received** → Convert Lead to Contact/Account/Deal
3. **Deal created** → Create Quote, Create Registrations
4. **Registration created** → Create Payment Link, Send Confirmation
5. **Payment confirmed** → Update Invoice, Update Deal, Issue Certificate

### Course → Registration → Invoice/Deal Updates
1. **Course created** → Create Registration Records
2. **Course details updated** → Update all Registration Records
3. **Registration paid** → Update Course counts, Update Deal
4. **Course starts** → Attendance tracking, Reminders
5. **Course ends** → Feedback requests, Certificate issuance

### Account/Contact → Xero → Workdrive
1. **Account/Contact created** → Create Workdrive Folder
2. **Details updated** → Sync to Xero
3. **Address changed** → Update all related records

---

## Workflow Naming Conventions

The system uses these prefixes to indicate workflow purpose:

- **Create** → Initializes new records or related records
- **Set** → Enforces naming conventions or defaults
- **Update** → Syncs data across modules
- **Calculate** → Performs calculations (totals, dates, counts)
- **Format** → Standardizes data format (phone, address)
- **Sync** → Pushes data to external systems
- **Send** → Triggers email or SMS communication
- **Mark** → Updates status fields
- **Generate** → Creates documents or IDs

---

## For Developers

### Finding Workflow Details
- Full workflow documentation: `LOGIC_INDEX_WORKFLOWS.md`
- Machine-readable data: `workflow_extraction_report.json`
- Source data: `data/exports/zoho-dependencies-2025-11-13.json`

### Before Modifying Fields
Always check if the field is used in workflow conditions:
1. Search this document for the field name
2. Review `LOGIC_INDEX_WORKFLOWS.md` for the specific workflow
3. Check for cross-module impacts

### Testing Workflow Changes
1. Verify trigger conditions match your test scenario
2. Check for dependent workflows in other modules
3. Test integration workflows (Xero, Stripe, WordPress) in sandbox first

---

## For Business Users

### Understanding Automation
Each workflow has:
- **Trigger** → What causes it to run
- **Conditions** → What must be true for it to execute
- **Actions** → What it does (update fields, send emails, create records)

### Common Questions
- **"Why did this email send?"** → Check workflows with "Send" or "Email" in the name for that module
- **"Why did this field update?"** → Check workflows with "Update" or "Calculate" for that field name
- **"When will reminders be sent?"** → Check date_or_datetime workflows for timing

---

## Maintenance Notes

### Inactive Workflows (10)
The following workflows are inactive but still in the system:
- TEST SMS (Leads) - Testing only
- Sync Course to Wordpress (old version) - Replaced
- Create Meetings for Trainer (2 workflows) - Replaced
- Calculate Overall Tax (old versions) - Replaced
- Pre_Arrival Survey (old versions) - Replaced
- Payment link workflows (old Stripe versions) - Replaced
- Update Deal stage (old logic) - Replaced
- Send Reg Record Confirmation - Paid (old version) - Replaced

**Recommendation:** Archive or delete after confirming replacements work correctly.

### Never Executed Workflows
Some workflows have never been triggered, indicating:
- Recently created workflows
- Edge case conditions not yet met
- Deprecated business processes

Review quarterly to determine if these should be kept or removed.

---

**Document Navigation:**
- [Return to Top](#logic-index---zoho-crm-automation-map)
- [Repository Inventory](REPOSITORY_INVENTORY.md)
- [Full Workflow Documentation](LOGIC_INDEX_WORKFLOWS.md)
- [Gap Analysis](AUDIT_GAP_ANALYSIS.md)
- [Risk Assessment](RISK_ASSESSMENT.md)

*Last Updated: 2025-11-21*
*Maintained by: System Architecture Team*
