# Zoho CRM Business Glossary

**Purpose:** Maps business terminology to technical system objects, fields, and processes.
**Audience:** Business users, trainers, new team members, and process documentation.
**Last Updated:** 2025-12-10 (aligned to 2025-12-10 export; see `reports/export_diff_2025-12-10_vs_2025-11-13.md` for changes)

---

## How to Use This Glossary

- **Business Term** → What you call it in daily operations
- **System Object/Field** → What it's called in Zoho CRM
- **Location** → Where to find it in the system
- **Related Processes** → Which SOPs or workflows use this term

---

## Table of Contents

1. [Core Business Objects](#core-business-objects)
2. [Course & Training Terminology](#course--training-terminology)
3. [Sales & Pipeline Terminology](#sales--pipeline-terminology)
4. [Financial Terminology](#financial-terminology)
5. [Customer & Contact Terminology](#customer--contact-terminology)
6. [Status & Stage Values](#status--stage-values)
7. [Process & Workflow Terminology](#process--workflow-terminology)
8. [Integration Systems](#integration-systems)
9. [Field Type Terminology](#field-type-terminology)
10. [Common Abbreviations](#common-abbreviations)

---

## Core Business Objects

### Modules (Record Types)

| Business Term | System Module | API Name | What It Stores |
|--------------|--------------|----------|----------------|
| **Lead** | Leads | `Leads` | Potential customers who haven't purchased yet |
| **Contact** | Contacts | `Contacts` | Individual people (customers or prospects) |
| **Company** / **Organization** | Accounts | `Accounts` | Business entities or organizations |
| **Opportunity** / **Sale** | Deals | `Deals` | Sales opportunities and course bookings |
| **Quote** / **Proposal** | Quotes | `Quotes` | Price quotes sent to customers |
| **Invoice** / **Bill** | Invoices | `Invoices` | Payment requests and receipts |
| **Course** / **Training Event** | Courses | `Courses` | Scheduled training courses |
| **Attendee** / **Registration** | Registration Records | `Registration_Records` | Individual course attendees |
| **Sales Order** | Sales Orders | `Sales_Orders` | Confirmed orders (used less frequently) |
| **Task** / **Follow-up** | Team Tasks | `Team_Tasks` | Action items for staff |
| **Project** | Projects Inhouse | `Projects_Inhouse` | Internal projects |
| **Call** / **Call Log** | Calls | `Calls` | Phone call records |
| **Meeting** / **Appointment** | Events | `Events` | Scheduled meetings |
| **Venue** / **Location** | Venues | `Venues` | Physical course locations |

---

## Course & Training Terminology

### Course Types

| Business Term | System Field | API Name | Values |
|--------------|-------------|----------|---------|
| **Public Course** | Course Type | `Courses.Course_Type` | "Public" |
| **Private Course** / **In-house Training** | Course Type | `Courses.Course_Type` | "Private" |
| **Online Course** / **Virtual Training** | Course Delivery | `Courses.Course_Delivery` | "Online" / "Virtual" |
| **Face-to-face** / **In-person** | Course Delivery | `Courses.Course_Delivery` | "Classroom" |

### Course Status

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Scheduled Course** | Stage | `Courses.Stage` | Course is planned and bookable |
| **Running Course** / **In Progress** | Stage | `Courses.Stage` | Course is currently happening |
| **Completed Course** | Stage | `Courses.Stage` | Course has finished |
| **Cancelled Course** | Stage | `Courses.Stage` | Course was cancelled |
| **Course Code** | Course Code | `Courses.Course_Code` | Unique identifier (e.g., "PRINCE2-SYD-2025") |

### Attendee/Registration Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Private Attendee** | Course Type | `Registration_Records.Course_Type` | Attendee from private/in-house course |
| **Public Attendee** | Course Type | `Registration_Records.Course_Type` | Attendee from public course |
| **Paying Attendee** | Payment Status | `Registration_Records.Payment_Status` | Attendee who has paid |
| **Non-paying Attendee** / **Sponsored** | Payment Status | `Registration_Records.Payment_Status` | Attendee whose company pays (not individual) |
| **No-show** | Attendance Status | `Registration_Records.Attendance_Status` | Attendee didn't attend |
| **Attended** | Attendance Status | `Registration_Records.Attendance_Status` | Attendee completed course |
| **Certificate Issued** | Certificate | `Registration_Records.Certificate` | Certificate has been sent |

### Course Fields

| Business Term | System Field | API Name | Purpose |
|--------------|-------------|----------|---------|
| **Trainer** / **Facilitator** | Trainer | `Courses.Trainer` | Person delivering the course |
| **Start Date** | Start Date | `Courses.Start_Date` | When course begins |
| **End Date** | End Date | `Courses.End_Date` | When course finishes |
| **Course Price** | Course Price Public/Private | `Courses.Course_Price_Public_Including_GST` | Cost per attendee |
| **Total Registrations** | Total Registrations | `Courses.Total_Registrations` | Number of attendees |
| **Venue** / **Location** | Location | `Courses.Location` | Where course takes place |

---

## Sales & Pipeline Terminology

### Deal (Opportunity) Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Deal** / **Opportunity** | Deal Name | `Deals.Deal_Name` | Sales opportunity |
| **Deal Value** / **Amount** | Amount | `Deals.Amount` | Total value of the deal |
| **Number of Attendees** | Number of Attendees | `Deals.Number_of_Attendees` | How many people in booking |
| **Course Booking** | Associated Course Code | `Deals.Associated_Course_Code` | Which course is being booked |

### Deal Stages

| Business Term | System Stage | API Name | Meaning |
|--------------|-------------|----------|---------|
| **New Deal** / **Qualification** | Qualification | `Deals.Stage` | Initial contact/qualification |
| **Needs Analysis** | Needs Analysis | `Deals.Stage` | Understanding requirements |
| **Proposal Sent** / **Quote Sent** | Negotiation/Review | `Deals.Stage` | Quote has been sent |
| **PO Requested** | PO Requested | `Deals.Stage` | Waiting for purchase order |
| **Closed Won** / **Won** | Closed Won | `Deals.Stage` | Deal is successful |
| **Closed Lost** / **Lost** | Closed Lost | `Deals.Stage` | Deal was unsuccessful |

### Purchase Order Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **PO** / **Purchase Order** | PO Number | `Deals.PO_Number` | Customer's purchase order reference |
| **PO Received** | PO Received | `Deals.PO_Received` | PO has been received |
| **PO Follow-up** | Workflow trigger | Various | Automated reminders for PO |

---

## Financial Terminology

### Invoice Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Invoice** / **Bill** | Invoice Number | `Invoices.Invoice_Number` | Unique invoice identifier |
| **Due Date** | Due Date | `Invoices.Due_Date` | Payment deadline |
| **Tax** / **GST** | Tax | `Invoices.Tax` | Goods & Services Tax amount |
| **Subtotal** | Sub Total | `Invoices.Sub_Total` | Amount before tax |
| **Grand Total** | Grand Total | `Invoices.Grand_Total` | Total including tax |
| **Discount** | Discount | `Invoices.Discount` | Discount amount or percentage |

### Invoice Status

| Business Term | System Status | API Name | Meaning |
|--------------|--------------|----------|---------|
| **Draft Invoice** | Draft | `Invoices.Status` | Invoice being prepared |
| **Sent Invoice** | Sent | `Invoices.Status` | Invoice sent to customer |
| **Paid Invoice** | Paid | `Invoices.Status` | Payment received |
| **Overdue Invoice** | Overdue | `Invoices.Status` | Past due date, unpaid |

### Payment Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Payment Link** | Payment URL | `Invoices.Payment_URL` | Stripe payment link |
| **Payment Status** | Payment Status | `Registration_Records.Payment_Status` | Whether payment received |
| **Stripe Payment** | Integration | Workflow action | Online payment processor |
| **Payment Confirmation** | Workflow name | Various | Automated confirmation email |

### Quote Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Quote** / **Quotation** | Quote Number | `Quotes.Quote_Number` | Price quote identifier |
| **Quote Expiry** | Valid Until | `Quotes.Valid_Until` | Quote expiration date |
| **Quote Stage** | Quote Stage | `Quotes.Quote_Stage` | Status of the quote |

---

## Customer & Contact Terminology

### Contact Types

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Primary Contact** | Primary Contact | `Accounts.Primary_Contact` | Main person at company |
| **Account Contact** | Account Contact | `Accounts.Account_Contact` | General company contact |
| **Accounts Payable** | Account Payable | `Accounts.Account_Payable` | Person who handles payments |
| **Secondary Contact** | Secondary Contact | `Accounts.Secondary_Contact` | Backup contact person |

### Account (Company) Types

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Account** / **Company** | Account Name | `Accounts.Account_Name` | Business organization |
| **Parent Account** | Parent Account | `Accounts.Parent_Account` | Head office of organization |
| **Customer** | Account Type | `Accounts.Account_Type` | Existing customer |
| **Prospect** | Account Type | `Accounts.Account_Type` | Potential customer |

### Lead Terms

| Business Term | System Field | API Name | Meaning |
|--------------|-------------|----------|---------|
| **Lead** / **Prospect** | Lead Name | `Leads.Full_Name` | Potential customer |
| **Lead Source** | Lead Source | `Leads.Lead_Source` | Where lead came from |
| **Converted Lead** | Is Converted | `Leads.Converted` | Lead became customer |
| **Lead Status** | Lead Status | `Leads.Lead_Status` | Current lead state |

---

## Status & Stage Values

### Lead Status

| Business Term | System Value | When Used |
|--------------|-------------|-----------|
| **New Lead** | New | Just created in system |
| **Contacted** | Contacted | First contact made |
| **Qualified** | Qualified | Meets criteria for purchase |
| **Unqualified** | Unqualified | Not a good fit |
| **Converted** | Converted | Became customer |
| **Junk Lead** | Junk Lead | Invalid/spam |

### Course Stage

| Business Term | System Value | When Used |
|--------------|-------------|-----------|
| **Scheduled** | Scheduled | Course planned, accepting bookings |
| **In Progress** | Running | Course currently happening |
| **Completed** | Completed | Course finished |
| **Cancelled** | Cancelled | Course was cancelled |
| **On Hold** | On Hold | Temporarily paused |

### Registration Status

| Business Term | System Value | When Used |
|--------------|-------------|-----------|
| **Confirmed** | Confirmed | Registration confirmed |
| **Pending** | Pending | Waiting for payment/confirmation |
| **Cancelled** | Cancelled | Registration cancelled |
| **No Show** | No Show | Didn't attend |
| **Attended** | Attended | Completed course |

---

## Process & Workflow Terminology

### Automation Triggers

| Business Term | System Trigger | When It Fires |
|--------------|---------------|---------------|
| **When created** | create | New record is created |
| **When field changes** | field_update | Specific field is modified |
| **On edit** | edit | Any field is changed |
| **Scheduled** / **Date-based** | date_or_datetime | Specific date/time reached |
| **On create or edit** | create_or_edit | Record created OR edited |

### Common Workflow Actions

| Business Term | System Action | What It Does |
|--------------|--------------|--------------|
| **Send Email** | Email notification | Sends automated email |
| **Send SMS** | ClickSend SMS | Sends text message |
| **Create Task** | Create task | Creates follow-up task |
| **Update Field** | Field update | Changes field value |
| **Sync to Xero** | Webhook/Function | Sends data to accounting system |
| **Create Quote** | Create record | Auto-generates quote |

### Process Names

| Business Term | Workflow/SOP Name | What It Does |
|--------------|------------------|--------------|
| **Lead Conversion** | Convert Lead workflows | Turns lead into contact/deal |
| **Payment Processing** | Payment confirmation workflows | Handles payment receipt |
| **Course Reminders** | Course reminder workflows | Sends pre-course notifications |
| **PO Follow-up** | PO reminder workflows | Chases purchase orders |
| **Certificate Issuance** | Issue certificate workflow | Sends course certificates |
| **Feedback Request** | Feedback workflows | Requests course feedback |

---

## Integration Systems

### External Systems

| Business Term | System Name | Integration Purpose |
|--------------|------------|---------------------|
| **Accounting System** | Xero | Financial record sync |
| **Website** | WordPress | Course publishing |
| **Payment Gateway** | Stripe | Online payments |
| **SMS System** | ClickSend | Text message notifications |
| **Document Storage** | Workdrive | File storage and sharing |

### Integration Fields

| Business Term | System Field | Purpose |
|--------------|-------------|---------|
| **Xero Contact ID** | Xero Contact ID | Links to Xero contact |
| **Xero Invoice ID** | Xero Invoice ID | Links to Xero invoice |
| **WordPress Course ID** | WordPress ID | Links to website course |
| **Stripe Payment Link** | Payment URL | Online payment URL |

---

## Field Type Terminology

### Common Field Types

| Business Term | System Type | Example |
|--------------|-----------|---------|
| **Dropdown** / **Picklist** | picklist | Course Type: Public, Private |
| **Multi-select** | multiselectpicklist | Course Categories: Leadership, IT |
| **Lookup** / **Link** | lookup | Course → Links to Courses module |
| **Checkbox** / **Yes/No** | boolean | Certificate Issued: Yes/No |
| **Auto-number** | autonumber | Course ID: COURSE-00001 |
| **Date** | date | Course Start Date |
| **Date/Time** | datetime | Created Time |
| **Currency** / **Money** | currency | Deal Amount: $1,500 |
| **Number** | integer / double | Number of Attendees: 12 |
| **Email Address** | email | attendee@example.com |
| **Phone Number** | phone | +61 2 1234 5678 |
| **Text** / **Single Line** | text | Course Code |
| **Multi-line Text** / **Notes** | textarea | Description |
| **Owner** / **User** | ownerlookup | Course Owner |

---

## Common Abbreviations

### System Abbreviations

| Abbreviation | Full Term | Context |
|-------------|-----------|---------|
| **CRM** | Customer Relationship Management | The Zoho CRM system |
| **API** | Application Programming Interface | Technical field names |
| **PO** | Purchase Order | Customer's order reference |
| **SO** | Sales Order | Confirmed order |
| **GST** | Goods & Services Tax | Australian tax |
| **ID** | Identifier | Unique record number |
| **SOP** | Standard Operating Procedure | Process documentation |

### Field Abbreviations

| Abbreviation | Full Term | Where Used |
|-------------|-----------|-----------|
| **Reg** | Registration | Registration Records |
| **Spec** | Special | Enrolled (Spec) field |
| **CV** | Curriculum Vitae | CV Submitted field |
| **SMS** | Short Message Service | Text messages |
| **URL** | Uniform Resource Locator | Web links |

### Course Abbreviations

| Abbreviation | Full Term | Example |
|-------------|-----------|---------|
| **PRINCE2** | Projects IN Controlled Environments | PRINCE2 Foundation course |
| **PMP** | Project Management Professional | PMP Certification |
| **ITIL** | Information Technology Infrastructure Library | ITIL Foundation |

---

## Cross-Reference: Business Process to System Objects

### Registration Process

**Business Flow:**
1. Customer inquires → **Lead** created
2. Send quote → **Quote** created from **Deal**
3. Customer pays → **Invoice** marked paid
4. Create booking → **Deal** created, **Registration Record** created
5. Course runs → **Course** status updated
6. Issue certificate → **Registration Record** certificate field updated

**System Objects Used:** Leads, Deals, Quotes, Invoices, Courses, Registration_Records

### Invoice Process

**Business Flow:**
1. Deal won → **Invoice** auto-created
2. Send to customer → Invoice status = "Sent"
3. Payment received → Invoice status = "Paid"
4. Sync to accounting → **Xero** integration triggered

**System Objects Used:** Invoices, Deals, Integration (Xero)

### Course Lifecycle

**Business Flow:**
1. Create course → **Course** record created
2. Publish online → **WordPress** sync triggered
3. Send reminders → **Workflows** send emails/SMS
4. Course runs → Stage = "Running"
5. Course ends → Stage = "Completed"
6. Issue certificates → **Registration Records** updated

**System Objects Used:** Courses, Registration_Records, Integrations (WordPress, ClickSend)

---

## Usage Examples

### Example 1: "Where do I find all private attendees?"
- **Module:** Registration_Records
- **Filter:** `Course_Type` = "Private"
- **Also check:** `Attendee_Type` field for additional classification

### Example 2: "How do I see which invoices are overdue?"
- **Module:** Invoices
- **Filter:** `Status` = "Sent" AND `Due_Date` < Today

### Example 3: "What's the difference between a Lead and a Contact?"
- **Lead:** Potential customer who hasn't purchased
- **Contact:** Person record (can be customer or prospect)
- **Note:** When a Lead converts, it creates a Contact (and optionally Account and Deal)

### Example 4: "Where is the course price stored?"
- **Public courses:** `Courses.Course_Price_Public_Including_GST`
- **Private courses:** `Courses.Course_Price_Private_Including_GST`
- **On registration:** `Registration_Records.Registration_Fee`

### Example 5: "What's a Deal Identifier?"
- **Field:** `Deals.Deal_Identifier`
- **Type:** Auto-number
- **Purpose:** Unique deal reference number (auto-generated)

---

## Special Terms by Department

### Sales Team Terms

| Business Term | System Reference |
|--------------|-----------------|
| **Pipeline** | Deals module with Stage field |
| **Qualified Lead** | Lead_Status = "Qualified" |
| **Opportunity** | Deal record |
| **Close Date** | Deals.Closing_Date |
| **Win Rate** | Report: Closed Won / Total Deals |

### Finance Team Terms

| Business Term | System Reference |
|--------------|-----------------|
| **Receivables** | Invoices with Status = "Sent" |
| **Paid Invoices** | Invoices with Status = "Paid" |
| **Revenue** | Sum of Paid Invoices |
| **Tax Report** | Invoice Tax field totals |
| **Xero Sync** | Integration workflows to Xero |

### Training Coordinator Terms

| Business Term | System Reference |
|--------------|-----------------|
| **Course Roster** | Registration_Records for a Course |
| **Attendance List** | Registration_Records with Attendance field |
| **Trainer Schedule** | Courses filtered by Trainer |
| **Pre-course Emails** | Automated workflows 7 days before |
| **Certificate Batch** | Registration_Records where Certificate = "Pending" |

### Marketing Team Terms

| Business Term | System Reference |
|--------------|-----------------|
| **Lead Source** | Leads.Lead_Source field |
| **Conversion Rate** | Converted Leads / Total Leads |
| **Course Catalogue** | Courses module, published to WordPress |
| **Public Courses** | Courses.Course_Type = "Public" |
| **Campaign** | Ad Campaign Name field (from Google Ads) |

---

## Related Documentation

- **Field Details:** See individual module documentation in `modules/[module-name]/docs/`
- **Workflow Details:** See [LOGIC_INDEX.md](LOGIC_INDEX.md) for automation details
- **Process Flows:** See `sops/processed/` for detailed process documentation
- **API Names:** See `[module]-fields.md` files for complete API name reference

---

## Maintenance Notes

### Adding New Terms
When adding new business terminology:
1. Identify the common business term
2. Find the corresponding system field/module
3. Document in the appropriate section above
4. Add cross-references if term relates to multiple areas
5. Update the "Usage Examples" section if helpful

### Updating Existing Terms
When field names or processes change:
1. Update the system reference
2. Add a note about when it changed
3. Update related cross-references
4. Notify team of terminology change

---

**Document Conventions:**
- **Bold** = Business terms (how people talk about it)
- `Code format` = System fields/API names (what it's called in CRM)
- *Italics* = Process names or workflow names

---

**Quick Navigation:**
- [Return to Top](#zoho-crm-business-glossary)
- [Logic Index](LOGIC_INDEX.md) - Workflow reference
- [Repository Inventory](REPOSITORY_INVENTORY.md) - File listing
- [Module Documentation](modules/) - Detailed field docs

*Last Updated: 2025-11-21*
*Maintained by: System Documentation Team*
*For questions or additions, contact your CRM administrator*
