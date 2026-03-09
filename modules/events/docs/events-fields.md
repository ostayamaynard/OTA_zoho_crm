<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Events Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 40

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| All_day | All day | boolean | No |
| Check_In_Address | Check-In Address | textarea | No |
| Check_In_By | Check-In By | ownerlookup | No |
| Check_In_City | Check-In City | text | No |
| Check_In_Comment | Check-In Comment | textarea | No |
| Check_In_Country | Check-In Country | text | No |
| Check_In_State | Check-In State | text | No |
| Check_In_Status | Checked In Status | text | No |
| Check_In_Sub_Locality | Check-In Sub-Locality | text | No |
| Check_In_Time | Check-In Time | datetime | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Description | Description | textarea | No |
| End_DateTime | To | datetime | Yes |
| Event_Title | Title | text | Yes |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Latitude | Latitude | double | No |
| Longitude | Longitude | double | No |
| Meeting_Provider__s | Provider | picklist | No |
| Meeting_Venue__s | Meeting Venue | picklist | Yes |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Owner | Host | ownerlookup | No |
| Participants | Participants | bigint | No |
| Record_Status__s | Record Status | picklist | No |
| Recurring_Activity | Repeat | RRULE | No |
| Remind_At | Reminder | multireminder | No |
| Remind_Participants | Participants Reminder | multireminder | No |
| Start_DateTime | From | datetime | Yes |
| Tag | Tag | text | No |
| Venue | Location | text | No |
| ZIP_Code | Zip Code | text | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Course_End_Date | Course End Date | date | No |
| Course_Location | Course Location | text | No |
| Course_Start_Date | Course Start Date | date | No |
| Course_Type | Course Type | picklist | No |
| Course_URL | Course URL | website | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| What_Id | Related To | lookup | No |
| Who_Id | Contact Name | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
