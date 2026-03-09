<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Campaigns Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 36

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Actual_Cost | Actual Cost | currency | No |
| Budgeted_Cost | Budgeted Cost | currency | No |
| Campaign_Name | Campaign Name | text | Yes |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Description | Description | textarea | No |
| End_Date | End Date | date | No |
| Expected_Response | Expected Response | bigint | No |
| Expected_Revenue | Expected Revenue | currency | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Layout | Layout | layout | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Num_sent | Numbers sent | bigint | No |
| Owner | Campaign Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Start_Date | Start Date | date | No |
| Status | Status | picklist | No |
| Tag | Tag | text | No |
| Type | Type | picklist | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Native__Campaigns__Extn__Campaign_Subject | Campaign Subject | text | No |
| Native__Campaigns__Extn__Reply_to_Address | Reply-to Address | picklist | No |
| Native__Campaigns__Extn__Sender_Address | Sender Address | picklist | No |
| Native__Campaigns__Extn__Sender_Name | Sender Name | text | No |
| Native__Survey__Extn__Department_ID | Department ID | text | No |
| Native__Survey__Extn__Survey | Survey | text | No |
| Native__Survey__Extn__Survey_Department | Survey Department | text | No |
| Native__Survey__Extn__Survey_Type | Survey Type | picklist | No |
| Native__Survey__Extn__Survey_URL | Survey URL | website | No |
| twiliosmsextension0__Number_of_replies_to_Twilio_campaign | Number of replies to Sinch campaign | integer | No |
| twiliosmsextension0__Successful_Twilio_Message_Deliveries | Successful Sinch Message Deliveries | integer | No |
| twiliosmsextension0__Time_to_send_Twilio_Campaign | Time to send Sinch Campaign | datetime | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Parent_Campaign | Parent Campaign | lookup | No |
| twiliosmsextension0__Twilio_From_Number_to_Use | Sinch From Number to Use | lookup | No |
| twiliosmsextension0__Twilio_Template | Sinch Template | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
