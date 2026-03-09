# Registration Records Module (Course Attendees)

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

The Registration_Records module manages individual student enrolments in courses. This is the operational module where attendee lifecycle, compliance, attendance, and certification are tracked.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Fields | 78 |
| Total Workflows | 36 |
| Lookup Fields | 9 |
| Boolean Triggers | 13 |

---

## Status Workflow

### Registration Status Picklist

| Order | Status | Description |
|-------|--------|-------------|
| 1 | Spot Tentative | Initial enquiry/booking |
| 2 | Spot Booked | Payment received/confirmed |
| 3 | To Be Rebooked | Needs to be moved to another course |
| 4 | Waiting List | Course full, on waitlist |
| 5 | Course Completed | Finished course |
| 6 | Cancelled | Withdrawn from course |
| 7 | Details Confirmed | All details verified |
| 8 | Fully Attended | Attended all days |
| 9 | Partially Attended | Missed some days |
| 10 | Resources Uploaded | Materials submitted |

---

## Lookup Relationships

| Field | Target Module | Description |
|-------|---------------|-------------|
| Course | Courses | Parent course record |
| Attendee | Contacts | The enrolled person |
| Account_Name | Accounts | Company (for corporate bookings) |
| Related_Deal | Deals | Associated sales deal |
| Venue | Venues | Training location |
| Trainer | Contacts | Course trainer |
| Invoice | Invoices | Payment invoice |
| Deal | Deals | Alternative deal link |
| Quote | Quotes | Associated quote |

---

## All Workflows (36 Total)

### Registration Creation (5)

| Workflow | ID | Action |
|----------|-----|--------|
| Populate Course Days | 52330000002460165 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460165) | Creates attendance subform entries |
| Calculate Registrations and create team task | 52330000002518044 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518044) | Updates course counts, creates task |
| Calculate Registrations | 52330000002518060 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518060) | Updates registration counts |
| Registration_Records_ZohoFlow_Copy of CRM Contact | 52330000005138075 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005138075) | Creates Workdrive folder |
| SMS Attendance Link | 52330000005789634 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789634) | Sends attendance app link |

### Payment Workflows (5)

| Workflow | ID | Action |
|----------|-----|--------|
| Email - Attendee paid via credit card | 52330000002582386 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002582386) | Confirmation for card payment |
| Email - Attendee Created - Public - Pay via Invoice | 52330000005157446 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005157446) | Invoice payment path |
| Email - Attendee Payment made for Invoice | 52330000005157463 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005157463) | Invoice payment confirmation |
| Send payment link | 52330000003024548 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003024548) | Sends payment URL |
| IF paid via credcard | 52330000004534986 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004534986) | Credit card processing |

### SMS Workflows (6)

| Workflow | ID | Timing |
|----------|-----|--------|
| Generate SMS Shorten Link | 52330000005789649 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789649) | Creates short URL |
| Generate SMS Link 15 days prior if Empty | 52330000005789664 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789664) | 15 days before |
| 14 days SMS Before Attendance Confirmation | 52330000005789721 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789721) | 14 days before |
| SMS - Attendance Acknowledgement | 52330000006676878 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006676878) | Attendance confirmed |
| Thank you SMS | 52330000002656733 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002656733) | Post-course |
| 7 Days before Public course SMS Reminder | 52330000002597951 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002597951) | 7 days before |

### Email Reminders - Public Courses (2)

| Workflow | ID | Timing |
|----------|-----|--------|
| 1 week prior to Public course | 52330000002582766 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002582766) | 7 days before |
| Feedback Email from attendee | 52330000002633996 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002633996) | Post-course |

### Email Reminders - Private Courses (4)

| Workflow | ID | Timing |
|----------|-----|--------|
| Private Attendee - Spot Tentative | 52330000005163090 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163090) | On creation |
| Private course Tentative - Attendee Spot Booked | 52330000005163175 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163175) | Booking confirmed |
| Private Course Confirmed - Attendee Spot Booked | 52330000005163264 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163264) | Course confirmed |
| 1 week prior to Private Confirmed course | 52330000005163385 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163385) | 7 days before |
| 7 Days before Private Confirmed course SMS Reminder | 52330000005163433 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163433) | 7 days SMS |

### Attendance & Certification (5)

| Workflow | ID | Action |
|----------|-----|--------|
| Update Course Attended 1 Day from course | 52330000003014499 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003014499) | 1 day after |
| Update Course Attended 1 week from course date | 52330000003014483 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003014483) | 1 week after |
| Certificate Held Back | 52330000002667069 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002667069) | Certificate on hold |
| Update course details | 52330000003014626 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003014626) | Syncs from course |
| status update | 52330000004045787 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004045787) | Status transitions |

### Deal & Payment Integration (2)

| Workflow | ID | Action |
|----------|-----|--------|
| Update Attendee for Payment Update with DEAL | 52330000004335393 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004335393) | Links deal payment |
| Trainer Edited | 52330000004112123 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004112123) | Updates trainer info |

### Administrative (7)

| Workflow | ID | Action |
|----------|-----|--------|
| Create Team Task | 52330000003121331 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003121331) | Creates follow-up task |
| Move Course Attendee Folder on Course Change | 52330000005375288 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005375288) | Moves Workdrive folder |
| Update Name on Course Change | 52330000009066119 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009066119) | Updates record name |
| Registration Cancelled | 52330000009966152 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009966152) | Cancellation handling |
| Waitlist Record | 52330000007034348 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007034348) | Waitlist management |
| Set Opt-Outs to False | 52330000007826269 | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007826269) | Reset opt-outs |

---

## Manual Trigger Fields

| Field | Workflow Triggered | Action |
|-------|-------------------|--------|
| Update | Update course details | Syncs course info |
| Send_payment_link | Send payment link | Emails payment URL |
| Create_Team_Task | Create Team Task | Creates task |
| send_cert_email | Certificate email | Sends certificate |

---

## Compliance Fields

| Field | Description |
|-------|-------------|
| Request_3rd_Party_Record | Pre-requisite evidence complete |
| CV_Submitted | Resume on file |
| Additional_Documents_Submitted | Supporting docs received |
| SOA_Sent | Statement of Attainment sent |
| USI_Number | Unique Student Identifier |
| English_second_language | ESL indicator |
| Reading_writing_difficulties | Learning support needed |
| Difficulty_with_IT | IT support needed |

---

## Integration Points

### Zoho Workdrive
- Creates attendee document folder
- Stores compliance documents
- Moves folder on course change

### ClickSend SMS
- Attendance reminders
- Payment confirmations
- Thank you messages

### Xero (via Deals/Invoices)
- Payment tracking
- Invoice synchronization

---

## Workflow URLs

Base URL: `https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/`

All workflow IDs listed above can be accessed by appending the ID to the base URL.

Example: [Populate Course Days](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460165)

---

## Related Modules

| Module | Relationship |
|--------|-------------|
| Courses | Parent record (Course lookup) |
| Contacts | Attendee person (Attendee lookup) |
| Accounts | Company for corporate bookings |
| Deals | Sales transaction |
| Invoices | Payment tracking |
| Team_Tasks | Follow-up tasks |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial documentation |
