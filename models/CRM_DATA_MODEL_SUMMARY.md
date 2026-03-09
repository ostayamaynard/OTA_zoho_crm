<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->

# Zoho CRM Data Model Summary

Generated from: zoho-data-model-2026-01-08.json

## Statistics

- **Total Modules**: 66
- **Total Fields**: 1,798
- **Total Workflows**: 183
- **Active Workflows**: 0
- **Lookup Relationships**: 118

## Most Referenced Modules

| Module | Referenced By |
|--------|---------------|
| Contacts | 21 modules |
| Accounts | 12 modules |
| Deals | 12 modules |
| Leads | 9 modules |
| Courses | 8 modules |
| Products | 5 modules |
| Quotes | 5 modules |
| Invoices | 4 modules |
| Registration_Records | 4 modules |
| se_module | 3 modules |
| Team_Task_Templates | 3 modules |
| Campaigns | 2 modules |
| Venues | 2 modules |
| Projects_Inhouse | 2 modules |
| Course_Performance | 2 modules |

## Most Complex Modules

| Module | Fields | Active Workflows |
|--------|--------|------------------|
| Leads | 161 | 0 |
| Courses | 137 | 0 |
| Contacts | 124 | 0 |
| Deals | 96 | 0 |
| Registration_Records | 79 | 0 |
| Call_Analytics | 65 | 0 |
| Accounts | 62 | 0 |
| twiliosmsextension0__Sent_SMS | 59 | 0 |
| Invoices | 58 | 0 |
| Sales_Orders | 47 | 0 |
| Feedbacks | 45 | 0 |
| Events | 40 | 0 |
| Quotes | 40 | 0 |
| Course_Performance | 40 | 0 |
| Campaigns | 36 | 0 |

## All Modules

### Accounts

- **Singular**: Account
- **Plural**: Accounts
- **Fields**: 62 (38 custom)
- **Workflows**: 0 active / 4 total
- **Lookup Fields**: 6
- **Mandatory Fields**: 0
- **Referenced By**: 12 modules

**Lookup Relationships**:
- `Account_Contact` → Contacts
- `Account_Payable` → Contacts
- `Last_Course` → Courses
- `Parent_Account` → Accounts
- `Primary_Contact` → Contacts
- `Secondary_Contact` → Contacts

### Actions_Performed

- **Singular**: Actions Performed
- **Plural**: Actions Performed
- **Fields**: 7 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Chat_Attachment` → Attachments

### Approvals

- **Singular**: My Jobs
- **Plural**: My Jobs
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Associated_Attendees

- **Singular**: Associated Attendees
- **Plural**: Associated Attendees
- **Fields**: 12 (9 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 4
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Course_Attendee` → Registration_Records
- `Deal` → Deals
- `Invoice` → Invoices
- `Parent_Id` → Course_Performance

### Associated_Attendess

- **Singular**: Associated Attendess
- **Plural**: Associated Attendess
- **Fields**: 7 (4 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Attendees` → Contacts
- `Parent_Id` → Deals

### Associated_Contacts

- **Singular**: Associated Contacts
- **Plural**: Associated Contacts
- **Fields**: 6 (3 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Contact_Name` → Contacts
- `Parent_Id` → Accounts

### Associated_Deals

- **Singular**: Associated Deals
- **Plural**: Associated Deals
- **Fields**: 10 (7 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Deal_Name` → Deals
- `Parent_Id` → Course_Performance

### Attachments

- **Singular**: Attachment
- **Plural**: Attachments
- **Fields**: 10 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 1 modules

### Attendees

- **Singular**: Student more 1 attendee
- **Plural**: Student more 1 attendee
- **Fields**: 8 (5 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Leads

### Call_Analytics

- **Singular**: Call Analytics
- **Plural**: Call Analytics
- **Fields**: 65 (48 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 4
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Account` → Accounts
- `Contact` → Contacts
- `Lead` → Leads
- `Related_Call` → Leads

### Calls

- **Singular**: Call
- **Plural**: Calls
- **Fields**: 29 (2 custom)
- **Workflows**: 0 active / 1 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `What_Id` → se_module
- `Who_Id` → Contacts

### Campaigns

- **Singular**: Campaign
- **Plural**: Campaigns
- **Fields**: 36 (14 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 3
- **Mandatory Fields**: 0
- **Referenced By**: 2 modules

**Lookup Relationships**:
- `Parent_Campaign` → Campaigns
- `twiliosmsextension0__Twilio_From_Number_to_Use` → twiliosmsextension0__Twilio_From_Numbers
- `twiliosmsextension0__Twilio_Template` → twiliosmsextension0__SMS_Templates

### Cases

- **Singular**: Case
- **Plural**: Cases
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Cold_Outreach

- **Singular**: Cold Outreach
- **Plural**: Cold Outreach
- **Fields**: 4 (1 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Leads

### Contacts

- **Singular**: Contact
- **Plural**: Contacts
- **Fields**: 124 (64 custom)
- **Workflows**: 0 active / 12 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 21 modules

**Lookup Relationships**:
- `Account_Name` → Accounts

### Course_Days

- **Singular**: Course Days
- **Plural**: Course Days
- **Fields**: 6 (3 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Registration_Records

### Course_Performance

- **Singular**: Course Performance
- **Plural**: Course Performance
- **Fields**: 40 (28 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 2 modules

**Lookup Relationships**:
- `Course` → Courses

### Course_Tasks

- **Singular**: Course Tasks
- **Plural**: Course Tasks
- **Fields**: 9 (6 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Team_Task_Templates

### Course_Type_History

- **Singular**: Course Type History
- **Plural**: Course Type History
- **Fields**: 13 (3 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Full_Name` → Leads

### Courses

- **Singular**: Course
- **Plural**: Courses
- **Fields**: 137 (121 custom)
- **Workflows**: 0 active / 37 total
- **Lookup Fields**: 6
- **Mandatory Fields**: 0
- **Referenced By**: 8 modules

**Lookup Relationships**:
- `Course_Qualification` → Products
- `Course_Trainer` → Contacts
- `Private_Course_Client` → Accounts
- `Select_Venue` → Venues
- `Training_Coordinator` → Contacts
- `Venue_Contact` → Contacts

### DealHistory

- **Singular**: Stage History
- **Plural**: Stage History
- **Fields**: 12 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Potential_Name` → Deals

### Deals

- **Singular**: Deal
- **Plural**: Deals
- **Fields**: 96 (51 custom)
- **Workflows**: 0 active / 25 total
- **Lookup Fields**: 7
- **Mandatory Fields**: 0
- **Referenced By**: 12 modules

**Lookup Relationships**:
- `Account_Contact` → Contacts
- `Account_Name` → Accounts
- `Contact_Name` → Contacts
- `Course` → Products
- `Courseaa` → Courses
- `Parent_Account` → Accounts
- `Training_Coordinator` → Contacts

### Email_Analytics

- **Singular**: Email Analytics
- **Plural**: Email Analytics
- **Fields**: 24 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Email_Sentiment

- **Singular**: EmailSentiment
- **Plural**: EmailSentiment
- **Fields**: 8 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Email_Template_Analytics

- **Singular**: Email Template Analytics
- **Plural**: Email Template Analytics
- **Fields**: 14 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Template_Name` → Email_Template__s

### Events

- **Singular**: Meeting
- **Plural**: Meetings
- **Fields**: 40 (5 custom)
- **Workflows**: 0 active / 1 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `What_Id` → se_module
- `Who_Id` → Contacts

### Facebook

- **Singular**: Facebook
- **Plural**: Facebook
- **Fields**: 5 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Feedbacks

- **Singular**: Feedback
- **Plural**: Feedback
- **Fields**: 45 (34 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Attendee_Record` → Registration_Records
- `Trainer_Record` → Contacts

### Functions__s

- **Singular**: Function
- **Plural**: Functions
- **Fields**: 27 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Invoiced_Items

- **Singular**: Invoiced Items
- **Plural**: Invoiced Items
- **Fields**: 14 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Invoices
- `Product_Name` → Products

### Invoices

- **Singular**: Invoice
- **Plural**: Invoices
- **Fields**: 58 (40 custom)
- **Workflows**: 0 active / 17 total
- **Lookup Fields**: 6
- **Mandatory Fields**: 0
- **Referenced By**: 4 modules

**Lookup Relationships**:
- `Account_Contact` → Contacts
- `Account_Name` → Accounts
- `Contact_Name` → Contacts
- `Course_Name` → Courses
- `Deal_Name__s` → Deals
- `Parent_Account` → Accounts

### Leads

- **Singular**: Lead
- **Plural**: Leads
- **Fields**: 161 (89 custom)
- **Workflows**: 0 active / 24 total
- **Lookup Fields**: 5
- **Mandatory Fields**: 0
- **Referenced By**: 9 modules

**Lookup Relationships**:
- `Converted_Account` → Accounts
- `Converted_Contact` → Contacts
- `Converted_Deal` → Deals
- `Course` → Courses
- `Existing_Company_Record` → Accounts

### Locking_Information__s

- **Singular**: Locking Information
- **Plural**: Locking Information
- **Fields**: 9 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Notes

- **Singular**: Note
- **Plural**: Notes
- **Fields**: 11 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Ordered_Items

- **Singular**: Ordered Items
- **Plural**: Ordered Items
- **Fields**: 14 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Sales_Orders
- `Product_Name` → Products

### Price_Books

- **Singular**: Price Book
- **Plural**: Price Books
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Products

- **Singular**: Course Template
- **Plural**: Course Templates
- **Fields**: 26 (8 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 5 modules

### Projects_Inhouse

- **Singular**: Project
- **Plural**: Projects Inhouse
- **Fields**: 25 (15 custom)
- **Workflows**: 0 active / 2 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 2 modules

### Projects_Tasks

- **Singular**: Projects Tasks
- **Plural**: Projects Tasks
- **Fields**: 20 (9 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Associated_Project` → Projects_Inhouse

### Purchase_Orders

- **Singular**: Purchase Order
- **Plural**: Purchase Orders
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Quoted_Items

- **Singular**: Quoted Items
- **Plural**: Quoted Items
- **Fields**: 14 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Quotes
- `Product_Name` → Products

### Quotes

- **Singular**: Quote
- **Plural**: Quotes
- **Fields**: 40 (23 custom)
- **Workflows**: 0 active / 9 total
- **Lookup Fields**: 7
- **Mandatory Fields**: 0
- **Referenced By**: 5 modules

**Lookup Relationships**:
- `Account_Contact` → Contacts
- `Account_Name` → Accounts
- `Contact_Name` → Contacts
- `Course_Name` → Courses
- `Deal_Name` → Deals
- `Parent_Account` → Accounts
- `Public_Attendee` → Contacts

### Recurring_Tasks

- **Singular**: Recurring Tasks
- **Plural**: Recurring Tasks
- **Fields**: 9 (6 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Team_Task_Templates

### Referral_Form

- **Singular**: Referral Form
- **Plural**: Referral Form
- **Fields**: 7 (4 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Parent_Id` → Contacts
- `Referred_Lead` → Leads

### Registration_Records

- **Singular**: Course Attendee
- **Plural**: Course Attendees
- **Fields**: 79 (64 custom)
- **Workflows**: 0 active / 37 total
- **Lookup Fields**: 9
- **Mandatory Fields**: 0
- **Referenced By**: 4 modules

**Lookup Relationships**:
- `Account_Name` → Accounts
- `Attendee` → Contacts
- `Course` → Courses
- `Deal` → Deals
- `Invoice` → Invoices
- `Quote` → Quotes
- `Related_Deal` → Deals
- `Trainer` → Contacts
- `Venue` → Venues

### Sales_Orders

- **Singular**: Sales Order
- **Plural**: Sales Orders
- **Fields**: 47 (5 custom)
- **Workflows**: 0 active / 1 total
- **Lookup Fields**: 4
- **Mandatory Fields**: 0
- **Referenced By**: 1 modules

**Lookup Relationships**:
- `Account_Name` → Accounts
- `Contact_Name` → Contacts
- `Deal_Name` → Deals
- `Quote_Name` → Quotes

### Sales_Scripts

- **Singular**: Sales Scripts
- **Plural**: Sales Scripts
- **Fields**: 25 (8 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Solutions

- **Singular**: Solution
- **Plural**: Solutions
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Tasks

- **Singular**: Task
- **Plural**: Tasks
- **Fields**: 23 (2 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `What_Id` → se_module
- `Who_Id` → Contacts

### Team_Task_Templates

- **Singular**: Team Task Template
- **Plural**: Team Task Templates
- **Fields**: 15 (4 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 3 modules

### Team_Tasks

- **Singular**: Team Task
- **Plural**: Team Tasks
- **Fields**: 35 (24 custom)
- **Workflows**: 0 active / 3 total
- **Lookup Fields**: 9
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `Contact` → Contacts
- `Course` → Courses
- `Course_Attendee` → Registration_Records
- `Deal` → Deals
- `Invoice` → Invoices
- `Lead` → Leads
- `Project` → Projects_Inhouse
- `Quote` → Quotes
- `Recurring_Task` → Team_Task_Templates

### Twitter

- **Singular**: Twitter
- **Plural**: Twitter
- **Fields**: 5 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Vendors

- **Singular**: Vendor
- **Plural**: Vendors
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### Venues

- **Singular**: Venue
- **Plural**: Venues
- **Fields**: 23 (12 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 2 modules

**Lookup Relationships**:
- `Venue_Contact` → Contacts

### Visits

- **Singular**: Visit
- **Plural**: Visits
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### clicksendext__Clicksend_SMS

- **Singular**: Clicksend SMS Logs
- **Plural**: Clicksend SMS Logs
- **Fields**: 29 (13 custom)
- **Workflows**: 0 active / 1 total
- **Lookup Fields**: 2
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `clicksendext__Contact` → Contacts
- `clicksendext__Lead` → Leads

### clicksendext__test

- **Singular**: test
- **Plural**: test
- **Fields**: 0 (0 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### twiliosmsextension0__Inbound_SMS

- **Singular**: Sinch Inbound fetcher
- **Plural**: Sinch Inbound fetcher
- **Fields**: 18 (2 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### twiliosmsextension0__SMS_Templates

- **Singular**: Sinch SMS Template
- **Plural**: Sinch SMS Templates
- **Fields**: 19 (3 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 1 modules

### twiliosmsextension0__Sent_SMS

- **Singular**: Sinch Message
- **Plural**: Sinch Messages
- **Fields**: 59 (43 custom)
- **Workflows**: 0 active / 8 total
- **Lookup Fields**: 4
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `ContactName` → Contacts
- `LeadName` → Leads
- `twiliosmsextension0__Campaign` → Campaigns
- `twiliosmsextension0__DealName` → Deals

### twiliosmsextension0__Twilio_Autoresponders

- **Singular**: Sinch Autoresponder
- **Plural**: Sinch Autoresponders
- **Fields**: 29 (13 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### twiliosmsextension0__Twilio_Error_Logs

- **Singular**: Sinch Error Log
- **Plural**: Sinch Error Logs
- **Fields**: 18 (2 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

### twiliosmsextension0__Twilio_From_Numbers

- **Singular**: Sinch From Number
- **Plural**: Sinch From Numbers
- **Fields**: 26 (10 custom)
- **Workflows**: 0 active / 1 total
- **Lookup Fields**: 0
- **Mandatory Fields**: 0
- **Referenced By**: 1 modules

### zohosign__ZohoSign_Document_Events

- **Singular**: Zoho Sign Document Events
- **Plural**: Zoho Sign Document Events
- **Fields**: 21 (3 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `zohosign__ZohoSign_Document` → zohosign__ZohoSign_Documents

### zohosign__ZohoSign_Documents

- **Singular**: Zoho Sign Document
- **Plural**: Zoho Sign Documents
- **Fields**: 36 (18 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 5
- **Mandatory Fields**: 0
- **Referenced By**: 2 modules

**Lookup Relationships**:
- `zohosign__Account` → Accounts
- `zohosign__Contact` → Contacts
- `zohosign__Deal` → Deals
- `zohosign__Lead` → Leads
- `zohosign__Quote` → Quotes

### zohosign__ZohoSign_Recipients

- **Singular**: Zoho Sign Recipient
- **Plural**: Zoho Sign Recipients
- **Fields**: 27 (9 custom)
- **Workflows**: 0 active / 0 total
- **Lookup Fields**: 1
- **Mandatory Fields**: 0
- **Referenced By**: 0 modules

**Lookup Relationships**:
- `zohosign__ZohoSign_Document` → zohosign__ZohoSign_Documents

