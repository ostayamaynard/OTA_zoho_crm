<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# twiliosmsextension0__Sent_SMS Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 59

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
| Name | Sinch Message Name | text | Yes |
| Owner | Sinch Message Owner | ownerlookup | No |
| Record_Image | Sinch Message Image | profileimage | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| From | From | text | No |
| Message | Message | textarea | No |
| Message_Date | Message Date | text | No |
| Message_Type | Message Type | text | No |
| Sid | Sid | text | No |
| To | To | text | No |
| twiliosmsextension0__API_Names_To_Update | API Names To Update | textarea | No |
| twiliosmsextension0__Activity_ID | Activity ID | text | No |
| twiliosmsextension0__Activity_Type | Activity Type | picklist | No |
| twiliosmsextension0__Autoresponder_Debug | Autoresponder Debug | textarea | No |
| twiliosmsextension0__Autoresponder_Message | Autoresponder Message | boolean | No |
| twiliosmsextension0__Drip_SMS_Cancel_on_prior_reply | Drip SMS Cancel on prior reply | boolean | No |
| twiliosmsextension0__Error | Error | text | No |
| twiliosmsextension0__Field_updates_for_parent_record_after_sending | Field updates for parent record after sending | textarea | No |
| twiliosmsextension0__Hour_Received | Hour Received | text | No |
| twiliosmsextension0__MMS_content | MMS content | textarea | No |
| twiliosmsextension0__Message_Recipient_Replied | Message Recipient Replied? | boolean | No |
| twiliosmsextension0__Message_Reporting_Tag | Message Reporting Tag | text | No |
| twiliosmsextension0__Message_Source | Message Source | text | No |
| twiliosmsextension0__Metadata_for_sending_SMS_later | Metadata for sending SMS later | textarea | No |
| twiliosmsextension0__Mobile_App_Sending_Metadata | Mobile App Sending Metadata | textarea | No |
| twiliosmsextension0__Only_use_specified_To_field | Only use specified To field | boolean | No |
| twiliosmsextension0__Out_of_hours_SMS | Out of hours SMS | boolean | No |
| twiliosmsextension0__Phone_Field_API_Name_To_Use | Phone Field API Name To Use | text | No |
| twiliosmsextension0__Previous_Outbound_Message_for_inbound_messages | Previous Outbound Message (for inbound messages) | textarea | No |
| twiliosmsextension0__Previously_linked_to_merged_record_id | Previously linked to merged record id | text | No |
| twiliosmsextension0__Replied_To_Message_ID | Replied To Message ID | text | No |
| twiliosmsextension0__Reply_Stats_Updated | Reply Stats Updated | boolean | No |
| twiliosmsextension0__Response_Time_Minutes | Response Time Minutes | integer | No |
| twiliosmsextension0__Retry_Count | Retry Count | integer | No |
| twiliosmsextension0__Scheduled_time_to_send | Scheduled time to send | datetime | No |
| twiliosmsextension0__Send_To_User_enter_User_ID | Send To User - enter User ID | text | No |
| twiliosmsextension0__Skip_Reschedule_Check | Skip Reschedule Check | boolean | No |
| twiliosmsextension0__Skip_duplicate_check | Skip duplicate check | boolean | No |
| twiliosmsextension0__Status | Status | text | No |
| twiliosmsextension0__Sync_Result | Sync Result | textarea | No |
| twiliosmsextension0__Synced | Synced | boolean | No |
| twiliosmsextension0__Trigger_Send_via_workflow | Trigger Send via workflow | boolean | No |
| twiliosmsextension0__Twilio_Webhook_Contents | Webhook Contents | textarea | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| ContactName | ContactName | lookup | No |
| LeadName | LeadName | lookup | No |
| twiliosmsextension0__Campaign | Campaign | lookup | No |
| twiliosmsextension0__DealName | DealName | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
