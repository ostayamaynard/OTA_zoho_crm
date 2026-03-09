<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Team_Tasks Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 35

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Name | Team Task Name | text | Yes |
| Owner | Team Task Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Alert_Timings | Due in number of days (+/-) | integer | No |
| Comments | Comments | text | No |
| Course_Type | Course Type | picklist | No |
| Date_Completed | Date Completed | date | No |
| Due_Date | Due Date | date | No |
| Frequency | Frequency | picklist | No |
| Priority | Priority | picklist | No |
| Recurring_Task_Category | Recurring Task Category | text | No |
| Related_To_ID | Related To ID | text | No |
| Related_To_Module | Related To Module | text | No |
| Related_To_Name | Related To Name | text | No |
| Required_For | Required For | picklist | No |
| Status | Status | picklist | No |
| Task_Details | Task Details | text | No |
| Warn_Date | Warn Date | date | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Contact | Contact | lookup | No |
| Course | Course | lookup | No |
| Course_Attendee | Course Attendee | lookup | No |
| Deal | Deal | lookup | No |
| Invoice | Invoice | lookup | No |
| Lead | Lead | lookup | No |
| Project | Project | lookup | No |
| Quote | Quote | lookup | No |
| Recurring_Task | Recurring Task | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
