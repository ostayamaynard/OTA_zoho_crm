<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Calls Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 29

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| CTI_Entry | CTI Entry | boolean | No |
| Call_Agenda | Call Agenda | text | No |
| Call_Duration | Call Duration | text | Yes |
| Call_Duration_in_seconds | Call Duration (in seconds) | integer | No |
| Call_Purpose | Call Purpose | picklist | No |
| Call_Result | Call Result | picklist | No |
| Call_Start_Time | Call Start Time | datetime | Yes |
| Call_Type | Call Type | picklist | Yes |
| Caller_ID | Caller ID | text | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Description | Description | textarea | No |
| Dialled_Number | Dialled Number | text | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Outgoing_Call_Status | Outgoing Call Status | picklist | No |
| Owner | Call Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Reminder | Reminder | picklist | No |
| Scheduled_In_CRM | Scheduled in CRM | picklist | No |
| Subject | Subject | text | No |
| Tag | Tag | text | No |
| Voice_Recording__s | Voice Recording | website | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Call_Stage_Transcript | Call Stage (Transcript) | picklist | No |
| cf_transcription | Transcription | textarea | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| What_Id | Related To | lookup | No |
| Who_Id | Contact Name | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
