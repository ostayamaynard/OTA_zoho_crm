<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Projects_Tasks Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 20

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_Time | Created Time | datetime | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_Time | Modified Time | datetime | No |
| Name | Projects Tasks Name | text | Yes |
| Owner | Projects Tasks Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Date_Completed | Date Completed | date | No |
| Due_Date | Due Date | date | No |
| Priority | Priority | picklist | No |
| Status | Status | picklist | No |
| Task_Comments | Task Comments | text | No |
| Task_Details | Task Details | textarea | No |
| Task_Time | Task Time | text | No |
| Warn_Date | Warn Date | date | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Associated_Project | Associated Project | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
