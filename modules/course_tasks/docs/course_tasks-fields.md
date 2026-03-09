<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Course_Tasks Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 9

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_Time | Created Time | datetime | No |
| Modified_Time | Modified Time | datetime | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Due_in_number_of_days | Due in number of days (+/-) | integer | No |
| Interval_From | Interval From | picklist | No |
| Priority | Priority | picklist | No |
| Task_Details | Task Details | text | No |
| Task_Name | Task Name | text | No |
| Task_Owner | Task Owner | userlookup | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Parent_Id | Parent ID | lookup | Yes |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
