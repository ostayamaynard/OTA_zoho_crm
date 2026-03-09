<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# zohosign__ZohoSign_Documents Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 36

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Currency | Currency | picklist | No |
| Email | Email | email | No |
| Email_Opt_Out | Email Opt Out | boolean | No |
| Exchange_Rate | Exchange Rate | double | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Name | Zoho Sign Document Name | text | Yes |
| Owner | Zoho Sign Document Owner | ownerlookup | No |
| Record_Image | Zoho Sign Document Image | profileimage | No |
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
| zohosign__Date_Completed | Date Completed | date | No |
| zohosign__Date_Declined | Date Declined | date | No |
| zohosign__Date_Sent | Date Sent | date | No |
| zohosign__Declined_Reason | Declined Reason | textarea | No |
| zohosign__DeleteEdit_Preview_or_Position_Signature_Fields | Preview or Position Signature Fields | boolean | No |
| zohosign__Document_Deadline | Document Deadline | date | No |
| zohosign__Document_Message | Document Description | textarea | No |
| zohosign__Document_Note | Document Note | textarea | No |
| zohosign__Document_Status | Document Status | text | No |
| zohosign__Module_Name | Module Name | text | No |
| zohosign__Module_Record_ID | Module Record ID | text | No |
| zohosign__Time_to_complete | Time to complete | text | No |
| zohosign__ZohoSign_Document_ID | ZohoSign Document ID | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| zohosign__Account | Account | lookup | No |
| zohosign__Contact | Contact | lookup | No |
| zohosign__Deal | Deal | lookup | No |
| zohosign__Lead | Lead | lookup | No |
| zohosign__Quote | Quote | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
