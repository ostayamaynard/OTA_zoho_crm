# Accounts Module

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

The Accounts module stores company/organization records. Used for corporate training clients, private course bookings, and organizational billing.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Fields | 61 |
| Total Workflows | 4 |
| Lookup Fields | 6 |
| References From | 12 modules |

---

## Lookup Relationships

### Outbound Lookups

| Field | Target Module | Description |
|-------|---------------|-------------|
| Parent_Account | Accounts | Hierarchical parent |
| Primary_Contact | Contacts | Main contact person |
| Last_Course | Courses | Most recent course |
| Account_Contact | Contacts | Alternative contact |
| Account_Payable | Contacts | Billing contact |
| Secondary_Contact | Contacts | Secondary contact |

### Inbound References (Accounts is looked up by)
- Courses.Private_Course_Client
- Registration_Records.Account_Name
- Deals.Account_Name
- Contacts.Account_Name
- Leads.Existing_Company_Record

---

## All Workflows (4 Total)

| Workflow | ID | Action |
|----------|-----|--------|
| Push Account Updates to Xero | 52330000002460265 | Syncs account to Xero |
| Send Update Your Details | 52330000005584202 | Requests info update |
| updateAccountsAddressAndRemoveMapFileds | 52330000010756347 | Address formatting |
| setAccountsGMapFiledsAsEmpty | 52330000010756395 | Clears map fields |

---

## Integration Points

### Xero
- **Workflow:** Push Account Updates to Xero
- **Purpose:** Keeps Xero organizations in sync
- **Sync Direction:** CRM → Xero

---

## Account Types

Accounts represent:
- **Corporate Clients** - Companies booking private training
- **Billing Organizations** - Entities responsible for payment
- **Training Partners** - Organizations referring attendees
- **Parent Companies** - Hierarchical relationships

---

## Key Fields

### Company Information
- Account_Name (mandatory)
- Website
- Phone
- Industry
- Annual_Revenue
- Number_of_Employees

### Address
- Billing_Street
- Billing_City
- Billing_State
- Billing_Code
- Billing_Country

### Contacts
- Primary_Contact → Contacts
- Account_Contact → Contacts
- Account_Payable → Contacts
- Secondary_Contact → Contacts

### Training History
- Last_Course → Courses

---

## Workflow URLs

Base URL: `https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/`

| Workflow | URL |
|----------|-----|
| Push Account Updates to Xero | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460265) |
| Send Update Your Details | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005584202) |
| updateAccountsAddressAndRemoveMapFileds | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756347) |
| setAccountsGMapFiledsAsEmpty | [Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010756395) |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial documentation |
