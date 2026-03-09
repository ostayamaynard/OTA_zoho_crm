<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# zohosign__ZohoSign_Recipients Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 27

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
| Name | Zoho Sign Recipient Name | text | Yes |
| Owner | Zoho Sign Recipient Owner | ownerlookup | No |
| Record_Image | Zoho Sign Recipient Image | profileimage | No |
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
| zohosign__Date_Delivered | Date Delivered | date | No |
| zohosign__Declined_Reason | Declined Reason | text | No |
| zohosign__Recipient_Order | Recipient Order | integer | No |
| zohosign__Recipient_Status | Recipient Status | picklist | No |
| zohosign__Recipient_Type | Recipient Type | picklist | No |
| zohosign__ZohoSign_Document_ID | ZohoSign Document ID | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| zohosign__ZohoSign_Document | ZohoSign Document | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
