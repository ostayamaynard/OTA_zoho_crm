# Zoho CRM System Overview

**Generated:** 2026-01-08 16:20:23
**Source Export:** 2026-01-08
**Data Model:** `models/CRM_DATA_MODEL.json`

---

## Executive Summary {#executive-summary}

| Metric | Count |
|--------|-------|
| Total Modules | 66 |
| Total Fields | 1798 |
| Total Workflows | 183 |
| Active Workflows | 0 |
| Lookup Relationships | 118 |
| Tier 1 Modules (Core) | 11 |
| Tier 2 Modules | 50 |
| Excluded Modules | 5 |

---

## Tier 1 Modules (Core Business) {#tier1-modules}

These are the primary business modules with significant configuration.

| Module | Fields | Workflows | Active WF | Lookups | Referenced By |
|--------|--------|-----------|-----------|---------|---------------|
| Accounts | 62 | 4 | 0 | 6 | 12 |
| Call_Analytics | 65 | 0 | 0 | 4 | 0 |
| Contacts | 124 | 12 | 0 | 1 | 21 |
| Courses | 137 | 37 | 0 | 6 | 8 |
| Deals | 96 | 25 | 0 | 7 | 12 |
| Invoices | 58 | 17 | 0 | 6 | 4 |
| Leads | 161 | 24 | 0 | 5 | 9 |
| Quotes | 40 | 9 | 0 | 7 | 5 |
| Registration_Records | 79 | 37 | 0 | 9 | 4 |
| Sales_Orders | 47 | 1 | 0 | 4 | 1 |
| twiliosmsextension0__Sent_SMS | 59 | 8 | 0 | 4 | 0 |

---

## Tier 2 Modules (Supporting) {#tier2-modules}

Supporting modules with lighter configuration.

| Module | Fields | Workflows | Lookups |
|--------|--------|-----------|---------|
| Actions_Performed | 7 | 0 | 1 |
| Approvals | 0 | 0 | 0 |
| Associated_Attendees | 12 | 0 | 4 |
| Associated_Attendess | 7 | 0 | 2 |
| Associated_Contacts | 6 | 0 | 2 |
| Associated_Deals | 10 | 0 | 2 |
| Attachments | 10 | 0 | 0 |
| Attendees | 8 | 0 | 1 |
| Calls | 29 | 1 | 2 |
| Campaigns | 36 | 0 | 3 |
| Cases | 0 | 0 | 0 |
| Cold_Outreach | 4 | 0 | 1 |
| Course_Days | 6 | 0 | 1 |
| Course_Performance | 40 | 0 | 1 |
| Course_Tasks | 9 | 0 | 1 |
| Course_Type_History | 13 | 0 | 1 |
| DealHistory | 12 | 0 | 1 |
| Email_Analytics | 24 | 0 | 0 |
| Email_Sentiment | 8 | 0 | 0 |
| Email_Template_Analytics | 14 | 0 | 1 |
| Events | 40 | 1 | 2 |
| Facebook | 5 | 0 | 0 |
| Feedbacks | 45 | 0 | 2 |
| Functions__s | 27 | 0 | 0 |
| Invoiced_Items | 14 | 0 | 2 |
| Locking_Information__s | 9 | 0 | 0 |
| Notes | 11 | 0 | 0 |
| Ordered_Items | 14 | 0 | 2 |
| Price_Books | 0 | 0 | 0 |
| Products | 26 | 0 | 0 |
| Projects_Inhouse | 25 | 2 | 0 |
| Projects_Tasks | 20 | 0 | 1 |
| Purchase_Orders | 0 | 0 | 0 |
| Quoted_Items | 14 | 0 | 2 |
| Recurring_Tasks | 9 | 0 | 1 |
| Referral_Form | 7 | 0 | 2 |
| Sales_Scripts | 25 | 0 | 0 |
| Solutions | 0 | 0 | 0 |
| Tasks | 23 | 0 | 2 |
| Team_Task_Templates | 15 | 0 | 0 |
| Team_Tasks | 35 | 3 | 9 |
| Twitter | 5 | 0 | 0 |
| Vendors | 0 | 0 | 0 |
| Venues | 23 | 0 | 1 |
| Visits | 0 | 0 | 0 |
| twiliosmsextension0__Inbound_SMS | 18 | 0 | 0 |
| twiliosmsextension0__SMS_Templates | 19 | 0 | 0 |
| twiliosmsextension0__Twilio_Autoresponders | 29 | 0 | 0 |
| twiliosmsextension0__Twilio_Error_Logs | 18 | 0 | 0 |
| twiliosmsextension0__Twilio_From_Numbers | 26 | 1 | 0 |

---

## Business Domain Groupings {#domain-groupings}

### Sales Pipeline

Leads, Contacts, Accounts, Deals, Campaigns

### Quoting & Billing

Quotes, Sales_Orders, Invoices, Purchase_Orders, Products, Price_Books

### Education & Training

Courses, Registration_Records, Attendees, Venues, Course_Days, Course_Tasks, Course_Performance, Course_Type_History

### Task Management

Tasks, Team_Tasks, Recurring_Tasks, Projects_Tasks, Events

### Customer Service

Cases, Solutions, Feedbacks

### Marketing

Campaigns, Cold_Outreach, Referral_Form

### Analytics

Email_Analytics, Email_Sentiment

---

## Most Referenced Modules {#most-referenced}

Modules that are frequently referenced by other modules (high integration points).

| Module | Referenced By (Count) | Referencing Modules |
|--------|----------------------|---------------------|
| Contacts | 21 | Leads, Accounts, Deals, Tasks, Events, +16 more |
| Accounts | 12 | Leads, Contacts, Accounts, Deals, Courses, +7 more |
| Deals | 12 | Leads, Registration_Records, Team_Tasks, Quotes, Sales_Orders, +7 more |
| Leads | 9 | Team_Tasks, zohosign__ZohoSign_Documents, clicksendext__Clicksend_SMS, Attendees, Cold_Outreach, +4 more |
| Courses | 8 | Leads, Accounts, Deals, Registration_Records, Team_Tasks, +3 more |
| Products | 5 | Deals, Courses, Quoted_Items, Ordered_Items, Invoiced_Items |
| Quotes | 5 | Registration_Records, Team_Tasks, Sales_Orders, zohosign__ZohoSign_Documents, Quoted_Items |
| Registration_Records | 4 | Team_Tasks, Associated_Attendees, Feedbacks, Course_Days |
| Invoices | 4 | Registration_Records, Team_Tasks, Associated_Attendees, Invoiced_Items |
| Team_Task_Templates | 3 | Team_Tasks, Recurring_Tasks, Course_Tasks |
| Campaigns | 2 | Campaigns, twiliosmsextension0__Sent_SMS |
| Venues | 2 | Courses, Registration_Records |
| Projects_Inhouse | 2 | Team_Tasks, Projects_Tasks |
| Course_Performance | 2 | Associated_Deals, Associated_Attendees |
| Sales_Orders | 1 | Ordered_Items |

---

## Related Documentation {#related-docs}

- **LATEST_CHANGES.md** - Recent configuration changes between exports
- **WORKFLOW_DEPENDENCY_MAP.md** - Impact analysis for workflow modifications
- **FIELD_REFERENCE.md** - Detailed field specifications and picklist values
- **CHANGE_PLANNING_GUIDE.md** - Best practices for making CRM changes

---

*Generated by `tools/generate_ai_kb.py` on 2026-01-08*
