<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# zohosign__ZohoSign_Document_Events Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 21

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
| Name | Zoho Sign Document Events Name | text | Yes |
| Owner | Zoho Sign Document Events Owner | ownerlookup | No |
| Record_Image | Zoho Sign Document Events Image | profileimage | No |
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
| zohosign__Date | Date | date | No |
| zohosign__Description | Description | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| zohosign__ZohoSign_Document | ZohoSign Document | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
