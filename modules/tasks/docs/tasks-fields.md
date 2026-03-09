<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Tasks Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 23

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Closed_Time | Closed Time | datetime | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Description | Description | textarea | No |
| Due_Date | Due Date | date | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Owner | Task Owner | ownerlookup | No |
| Priority | Priority | picklist | No |
| Record_Status__s | Record Status | picklist | No |
| Recurring_Activity | Repeat | RRULE | No |
| Remind_At | Reminder | ALARM | No |
| Send_Notification_Email | Send Notification Email | boolean | No |
| Status | Status | picklist | No |
| Subject | Subject | text | Yes |
| Tag | Tag | text | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| twiliosmsextension0__Twilio_SMS | Sinch SMS | boolean | No |
| twiliosmsextension0__twilio_parent_record_id | Sinch_parent_record_id | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| What_Id | Related To | lookup | No |
| Who_Id | Contact Name | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
