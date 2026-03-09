<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# clicksendext__Clicksend_SMS Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 29

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Currency | Currency | picklist | No |
| Exchange_Rate | Exchange Rate | double | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Name | Subject | text | Yes |
| Owner | Clicksend SMS Logs Owner | ownerlookup | No |
| Record_Image | Clicksend SMS Logs Image | profileimage | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| clicksendext__Business_Name | Business Name | text | No |
| clicksendext__Date | Date | datetime | No |
| clicksendext__Draft | Draft | boolean | No |
| clicksendext__From | From | text | No |
| clicksendext__Inbound | Inbound | boolean | No |
| clicksendext__Message_Id | Message_Id | text | No |
| clicksendext__Msg_Cost | Msg Cost | text | No |
| clicksendext__Recheck_at | Recheck at | datetime | No |
| clicksendext__Related_To | Related To | picklist | No |
| clicksendext__Text | Text | textarea | No |
| clicksendext__To | To | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| clicksendext__Contact | Contact | lookup | No |
| clicksendext__Lead | Lead | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
