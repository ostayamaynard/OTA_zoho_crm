<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Deals Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 96

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| ADGROUPID | ADGROUPID | text | No |
| ADID | ADID | text | No |
| Ad | Ad | text | No |
| AdGroup_Name | AdGroup Name | text | No |
| Ad_Campaign_Name | Ad Campaign Name | text | No |
| Ad_Click_Date | Ad Click Date | date | No |
| Ad_Network | Ad Network | picklist | No |
| Amount | Amount | currency | No |
| Change_Log_Time__s | Change Log Time | datetime | No |
| Click_Type | Click Type | picklist | No |
| Closing_Date | Closing Date | date | No |
| Conversion_Export_Status | Conversion Export Status | picklist | No |
| Conversion_Exported_On | Conversion Exported On | datetime | No |
| Cost_per_Click | Cost per Click | currency | No |
| Cost_per_Conversion | Cost per Conversion | currency | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Deal_Name | Deal Name | text | Yes |
| Description | Description | textarea | No |
| Device_Type | Device Type | picklist | No |
| Expected_Revenue | Expected Revenue | currency | No |
| GADCONFIGID | GADCONFIGID | text | No |
| GCLID | GCLID | text | No |
| KEYWORDID | KEYWORDID | text | No |
| Keyword | Keyword | text | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Lead_Conversion_Time | Lead Conversion Time | integer | No |
| Lead_Source | Lead Source | picklist | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Overall_Sales_Duration | Overall Sales Duration | integer | No |
| Owner | Deal Owner | ownerlookup | No |
| Reason_For_Loss__s | Reason For Loss | picklist | No |
| Reason_for_Conversion_Failure | Reason for Conversion Failure | picklist | No |
| Record_Status__s | Record Status | picklist | No |
| Sales_Cycle_Duration | Sales Cycle Duration | integer | No |
| Search_Partner_Network | Search Partner Network | picklist | No |
| Stage | Stage | picklist | Yes |
| Tag | Tag | text | No |
| Type | Type | picklist | No |
| ZCAMPAIGNID | ZCAMPAIGNID | text | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Amount_Paid_Lead | Amount Paid (Lead) | currency | No |
| Associated_Course_Code | Associated Course Code | text | No |
| Attendee_Form_submitted | Attendee Form submitted | date | No |
| Attendee_Requested_on | Attendee Requested on | date | No |
| Course_ID | Course ID | text | No |
| Course_Start_Date | Course Start Date | date | No |
| Course_Type | Course Type | picklist | No |
| Create_Follow_up_Task | Create team task | boolean | No |
| Created_Date | Created Date | date | No |
| Creation_Source | Creation Source | picklist | No |
| Deal_CRM_ID | Deal CRM ID | text | No |
| Deal_Identifier | Deal Identifier | autonumber | No |
| Follow_Up_Notes | Task Details | textarea | No |
| Follow_up_date | Due Date | date | No |
| Is_Converted | Is_Converted | boolean | No |
| Lead_ID | Lead_ID | text | No |
| Loss_Reason | Loss Reason | textarea | No |
| Marketing_Opt_out | Marketing Opt out | boolean | No |
| Multi_Line_3 | Multi-Line 3 | textarea | No |
| Number_of_Attendees | Number of Attendees | integer | No |
| Po_Expected_Date | Po Expected Date | date | No |
| Po_Required | Po Required? | boolean | No |
| Preferred_Payment_Method | Preferred Payment Method | picklist | No |
| Priority | Priority | picklist | No |
| Purchase_Order_Number | Purchase Order Number | text | No |
| Quote_Amount | Quote incl. GST Amount | currency | No |
| Quote_ID | Quote ID | text | No |
| Request_Attendees | Request Attendees | boolean | No |
| Request_PO_URL | Request PO URL | website | No |
| Required_For | Required For | picklist | No |
| Task_Name | Task Name | text | No |
| Task_Owner | Task Owner | userlookup | No |
| Udpate | Update | boolean | No |
| Website_Account_Name | Website Account Name | text | No |
| Workflow_Trigger | Workflow Trigger | picklist | No |
| leadchain0__Social_Lead_ID | Social Lead ID | text | No |
| twiliosmsextension0__Address_For_Email_To_SMS | Address For Email To SMS | email | No |
| twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message | Last Time They Replied To Sinch Message | datetime | No |
| twiliosmsextension0__Last_Time_They_Sent_Us_a_Message | Last Time They Sent Us a Message | datetime | No |
| twiliosmsextension0__Num_Inbound_Twilio_Messages | Num Inbound Sinch Messages | integer | No |
| twiliosmsextension0__Num_Outbound_Twilio_Messages | Num Outbound Sinch Messages | integer | No |
| twiliosmsextension0__Smooth_Conversation_Team_Assigned | Sinch Conversation Team Assigned | text | No |
| twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied | They sent an SMS and we haven't replied | boolean | No |
| twiliosmsextension0__Twilio_Auto_Responders_Enabled | Sinch Auto Responders Enabled | boolean | No |
| twiliosmsextension0__Twilio_SMS_Message_Opt_Out | Sinch SMS Message Opt Out | boolean | No |
| twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied | We Sent Them An SMS and They Haven't Replied | boolean | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Contact | Account Contact | lookup | No |
| Account_Name | Account Name | lookup | No |
| Contact_Name | Contact Name | lookup | No |
| Course | Product | lookup | No |
| Courseaa | Course | lookup | No |
| Parent_Account | Parent Account | lookup | No |
| Training_Coordinator | Training Coordinator | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
