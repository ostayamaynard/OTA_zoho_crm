<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Contacts Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 124

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
| Average_Time_Spent_Minutes | Average Time Spent (Minutes) | double | No |
| Change_Log_Time__s | Change Log Time | datetime | No |
| Click_Type | Click Type | picklist | No |
| Conversion_Export_Status | Conversion Export Status | picklist | No |
| Conversion_Exported_On | Conversion Exported On | datetime | No |
| Cost_per_Click | Cost per Click | currency | No |
| Cost_per_Conversion | Cost per Conversion | currency | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Date_of_Birth | Date of Birth | date | No |
| Days_Visited | Days Visited | integer | No |
| Department | Department | text | No |
| Description | Description | textarea | No |
| Device_Type | Device Type | picklist | No |
| Email | Email | email | No |
| Email_Opt_Out | Email Opt Out | boolean | No |
| Enrich_Status__s | Enrich Status | picklist | No |
| Fax | Fax | text | No |
| First_Name | First Name | text | No |
| First_Visited_Time | First Visit | datetime | No |
| First_Visited_URL | First Page Visited | website | No |
| Full_Name | Full Name | text | No |
| GADCONFIGID | GADCONFIGID | text | No |
| GCLID | GCLID | text | No |
| Home_Phone | Home Phone | phone | No |
| KEYWORDID | KEYWORDID | text | No |
| Keyword | Keyword | text | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Last_Enriched_Time__s | Last Enriched Time | datetime | No |
| Last_Name | Last Name | text | Yes |
| Last_Visited_Time | Most Recent Visit | datetime | No |
| Locked__s | Locked | boolean | No |
| Mobile | Mobile | phone | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Number_Of_Chats | Number Of Chats | integer | No |
| Other_Phone | Other Phone | phone | No |
| Owner | Contact Owner | ownerlookup | No |
| Phone | Phone | phone | No |
| Reason_for_Conversion_Failure | Reason for Conversion Failure | picklist | No |
| Record_Status__s | Record Status | picklist | No |
| Referrer | Referrer | website | No |
| Salutation | Salutation | picklist | No |
| Search_Partner_Network | Search Partner Network | picklist | No |
| Secondary_Email | Secondary Email | email | No |
| Tag | Tag | text | No |
| Title | Title | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| Visitor_Score | Visitor Score | bigint | No |
| ZCAMPAIGNID | ZCAMPAIGNID | text | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Address_Line_1 | Address Line 1 | text | No |
| Address_Line_2 | Address Line 2 | text | No |
| Alternate_Email | CC to | email | No |
| App_Password | App_Password | text | No |
| Color_Code | Color Code | text | No |
| Contact_Source | Contact Source | picklist | No |
| Contact_Type | Contact Type | picklist | No |
| Country | Country | picklist | No |
| Course_End_Date | Course End Date | date | No |
| Course_For | Course For | picklist | No |
| Course_Name | Course Name | text | No |
| Create_task | Create task | boolean | No |
| Created_Date | Created Date | date | No |
| Dashboard_PIN | Dashboard PIN | text | No |
| Dashboard_URL | Dashboard URL | website | No |
| Due_Date | Due Date | date | No |
| Interested_By | Interested By | picklist | No |
| Is_Converted | Is_Converted | boolean | No |
| Last_Course_Booked | Last Course Booked | text | No |
| Lead_Contact_Tier | Lead/Contact Tier | picklist | No |
| Lead_ID | Lead_ID | text | No |
| Lead_Notes | Lead_Notes | textarea | No |
| Marketing_Opt_Out | Marketing Opt Out | boolean | No |
| Multi_Line_3 | Objections | textarea | No |
| Position | Position | picklist | No |
| Postcode | Postcode | text | No |
| Preferred_Contact_Method | Preferred Contact Method | picklist | No |
| Priority | Priority | picklist | No |
| Referral_Form | Referral Form | subform | No |
| Required_For | Required For | picklist | No |
| SMS_Opt_out | SMS Opt out | boolean | No |
| State | State | picklist | No |
| Suburb | Suburb | text | No |
| Target_Course_per_Month | Target Course per Month | integer | No |
| Task_Details | Task Details | text | No |
| Task_Name | Task Name | text | No |
| Task_Owner | Task Owner | userlookup | No |
| Trainer_Status | Trainer Status | picklist | No |
| Units | Attendee Status | textarea | No |
| Usi_number | USI number | text | No |
| Venue_Location | Venue Location | text | No |
| WP_Organizer_ID | WP Organizer ID | text | No |
| Website_Account_Name | Website Account Name | text | No |
| Work_Drive_Link | Work Drive Link | website | No |
| Xero_ID | Xero ID | text | No |
| clicksendext__Date_Time | Date Time | datetime | No |
| googlemapreports__Date_of_last_visit | Date of last visit | date | No |
| googlemapreports__Event_Name | Event Name | text | No |
| googlemapreports__Google_response_expire_date | Google response Expiration | date | No |
| googlemapreports__Latitude | Latitude | text | No |
| googlemapreports__Longitude | Longitude | text | No |
| leadchain0__Social_Lead_ID | Social Lead ID | text | No |
| location | location | text | No |
| twiliosmsextension0__Address_For_Email_To_SMS | Address For Email To SMS | email | No |
| twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message | Last Time They Replied To Sinch Message | datetime | No |
| twiliosmsextension0__Last_Time_They_Sent_Us_a_Message | Last Time They Sent Us a Message | datetime | No |
| twiliosmsextension0__Num_Inbound_Twilio_Messages | Num Inbound Sinch Messages | integer | No |
| twiliosmsextension0__Num_Outbound_Twilio_Messages | Num Outbound Sinch Messages | integer | No |
| twiliosmsextension0__Smooth_Conversation_Team_Assigned | Sinch Conversation Team Assigned | text | No |
| twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied | They sent an SMS and we haven't replied | boolean | No |
| twiliosmsextension0__Twilio_Auto_Responders_Enabled | Sinch Auto Responders Enabled | boolean | No |
| twiliosmsextension0__Twilio_SMS_Message_Opt_Out | Sinch Message Opt Out | boolean | No |
| twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied | We Sent Them An SMS and They Haven't Replied | boolean | No |
| twiliosmsextension0__Whatsapp_Number | Whatsapp Number | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Name | Account Name | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
