<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Call_Analytics Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 65

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Email | Email | email | No |
| Email_Opt_Out | Email Opt Out | boolean | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Name | Call Analytics Name | text | Yes |
| Owner | Call Analytics Owner | ownerlookup | No |
| Record_Image | Call Analytics Image | profileimage | No |
| Record_Status__s | Record Status | picklist | No |
| Secondary_Email | Secondary Email | email | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| AI_Processed | AI Processed | boolean | No |
| AI_Raw_JSON_Output | AI Raw JSON Output | textarea | No |
| AI_Summary | AI Coaching Summary | textarea | No |
| Agent | Agent | userlookup | No |
| Audio_File_URL | Audio File URL | website | No |
| CRM_Call_Record_ID | CRM Call Record ID | text | No |
| CX_Call_ID | 3CX Call ID | text | No |
| CX_Recording_ID | 3CX Recording ID | text | No |
| Call_Date | Call Date | date | No |
| Call_Duration_Minutes | Call Duration (Minutes) | double | No |
| Call_Duration_Seconds | Call Duration (Seconds) | integer | No |
| Call_Stage_Transcript | Call Stage (Transcript) | picklist | No |
| Call_Start_Datetime | Call Start Datetime | datetime | No |
| Call_Time | Call Time | datetime | No |
| Call_Type | Call Type | picklist | No |
| Closing | Closing | integer | No |
| Completed_Script_Steps | Completed Script Steps | integer | No |
| Discovery | Discovery | integer | No |
| Extension | Extension | text | No |
| Insights_Created | Insights Created | boolean | No |
| Missed_Steps | Missed Steps | textarea | No |
| Non_Standard_Call | Non Standard Call | boolean | No |
| Not_Enough_Data_flag | Not Enough Data flag | boolean | No |
| Objection_Category | Objection Category | picklist | No |
| Objection_Sentences_JSON | Objection Sentences JSON | textarea | No |
| Objection_Themes_JSON | Objection Themes JSON | textarea | No |
| Objections | Objections | integer | No |
| Opportunities | Opportunities | textarea | No |
| Overall_Call_Score | Overall Call Score | integer | No |
| Phone_Number | Phone Number | text | No |
| Primary_Objection | Primary Objection | text | No |
| Rapport | Rapport | integer | No |
| Recommended_Coaching | Recommended Coaching | textarea | No |
| Sales_Script_Key | Sales Script Key | text | No |
| Script_Compliance | Script Compliance % | percent | No |
| Script_Fallback_Used | Script Fallback Used | boolean | No |
| Script_Name | Script Name | text | No |
| Script_Writer_Doc_ID | Script Writer Doc ID | text | No |
| Secondary_Objection | Secondary Objection | text | No |
| Strengths | Strengths | textarea | No |
| Threats | Threats | textarea | No |
| Tier | Tier | picklist | No |
| Value | Value | integer | No |
| Weaknesses | Weaknesses | textarea | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account | Account | lookup | No |
| Contact | Contact | lookup | No |
| Lead | Lead | lookup | No |
| Related_Call | Related Call | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
