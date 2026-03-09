<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Team_Task_Templates Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 15

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Name | Team Task Template Name | text | Yes |
| Owner | Team Task Template Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Course_Tasks | Course Tasks | subform | No |
| Course_Type | Course Type | picklist | No |
| Recurring_Tasks | Recurring Tasks | subform | No |
| Task_Required_For | Task Required For | picklist | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
