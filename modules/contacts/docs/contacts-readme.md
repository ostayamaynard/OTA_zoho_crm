# Contacts Module

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

The Contacts module stores individual person records including trainers, attendees, and other stakeholders. This is a central module referenced by many others.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Fields | 113 |
| Total Workflows | 7 |
| References From | 20 modules |

---

## Module Relationships

### Outbound Lookups
- Account_Name → Accounts

### Inbound References (Contacts is looked up by)
- Courses.Course_Trainer
- Courses.Venue_Contact
- Courses.Training_Coordinator
- Registration_Records.Attendee
- Registration_Records.Trainer
- Deals.Contact_Name
- Leads (conversion target)
- And many more...

---

## All Workflows (7 Total)

| Workflow | ID | Action |
|----------|-----|--------|
| Push Contact Updates to Xero | 52330000002460248 | Syncs contact to Xero |
| Create task in contacts | 52330000002758242 | Creates follow-up task |
| Contacts_ZohoFlow_CRM Contact to Workdrive Folder | 52330000002820175 | Creates document folder |
| Format Phone field | 52330000005817024 | Formats phone on create |
| On Edit - Format Phone field | 52330000005817052 | Formats phone on edit |
| updateContactAddressAndRemoveMapFileds | 52330000010756331 | Address formatting |
| setContactsGMapFiledsAsEmpty | 52330000010756379 | Clears map fields |

---

## Integration Points

### Xero
- **Workflow:** Push Contact Updates to Xero
- **Purpose:** Keeps Xero contacts in sync

### Zoho Workdrive
- **Workflow:** Contacts_ZohoFlow_CRM Contact to Workdrive Folder
- **Purpose:** Creates document storage folder

---

## Contact Types

Contacts can serve multiple roles:
- **Trainers** - Deliver courses
- **Attendees** - Enrolled in courses
- **Venue Contacts** - Site coordinators
- **Account Contacts** - Primary contacts for companies
- **Training Coordinators** - Manage training programs

---

## Key Fields

### Identity
- Full_Name
- First_Name
- Last_Name
- Email
- Phone
- Mobile

### Address
- Mailing_Street
- Mailing_City
- Mailing_State
- Mailing_Zip
- Mailing_Country

### Preferences
- SMS_Opt_Out
- Marketing_Opt_Out

---

## Workflow URLs

Base URL: `https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/`

| Workflow | URL |
|----------|-----|
| Push Contact Updates to Xero | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460248) |
| Create task in contacts | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002758242) |
| Contacts_ZohoFlow_CRM Contact to Workdrive Folder | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002820175) |
| Format Phone field | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005817024) |
| On Edit - Format Phone field | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005817052) |
| updateContactAddressAndRemoveMapFileds | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756331) |
| setContactsGMapFiledsAsEmpty | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756379) |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial documentation |
