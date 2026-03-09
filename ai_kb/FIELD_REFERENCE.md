# Field Reference Guide

**Generated:** 2026-01-08 16:20:23
**Source Export:** 2026-01-08
**Purpose:** Quick field lookup and specification reference

---

## Overview {#overview}

| Metric | Count |
|--------|-------|
| Total Fields (All Modules) | 1798 |
| Tier 1 Module Fields | 928 |
| Tier 1 Modules (Full Detail) | 11 |
| Tier 2 Modules (Summary) | 50 |

**Documentation Levels:**
- **Tier 1**: Complete field listings with picklist values and lookup targets
- **Tier 2**: Summary statistics and lookup fields only

---

## Table of Contents {#toc}

### Tier 1 Modules (Full Detail)
- [Accounts (62 fields)](#module-accounts)
- [Call_Analytics (65 fields)](#module-call_analytics)
- [Contacts (124 fields)](#module-contacts)
- [Courses (137 fields)](#module-courses)
- [Deals (96 fields)](#module-deals)
- [Invoices (58 fields)](#module-invoices)
- [Leads (161 fields)](#module-leads)
- [Quotes (40 fields)](#module-quotes)
- [Registration_Records (79 fields)](#module-registration_records)
- [Sales_Orders (47 fields)](#module-sales_orders)
- [twiliosmsextension0__Sent_SMS (59 fields)](#module-twiliosmsextension0__sent_sms)

### Tier 2 Modules (Summary)
- [Actions_Performed (7 fields)](#module-actions_performed)
- [Approvals (0 fields)](#module-approvals)
- [Associated_Attendees (12 fields)](#module-associated_attendees)
- [Associated_Attendess (7 fields)](#module-associated_attendess)
- [Associated_Contacts (6 fields)](#module-associated_contacts)
- [Associated_Deals (10 fields)](#module-associated_deals)
- [Attachments (10 fields)](#module-attachments)
- [Attendees (8 fields)](#module-attendees)
- [Calls (29 fields)](#module-calls)
- [Campaigns (36 fields)](#module-campaigns)
- [Cases (0 fields)](#module-cases)
- [Cold_Outreach (4 fields)](#module-cold_outreach)
- [Course_Days (6 fields)](#module-course_days)
- [Course_Performance (40 fields)](#module-course_performance)
- [Course_Tasks (9 fields)](#module-course_tasks)
- *+35 more modules*

---

# Tier 1 Modules - Full Field Reference {#tier1}

## Accounts {#module-accounts}

**Total Fields:** 62
**Custom Fields:** 38
**Lookup Fields:** 6

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Account Name | Account_Name | text | ✓ |  |
| Billing City | Billing_City | text |  |  |
| Billing Code | Billing_Code | text |  |  |
| Billing Country | Billing_Country | text |  |  |
| Billing Street | Billing_Street | text |  |  |
| Change Log Time | Change_Log_Time__s | datetime |  |  |
| Created Time | Created_Time | datetime |  |  |
| Description | Description | textarea |  |  |
| Enrich Status | Enrich_Status__s | picklist |  | Available, Enriched, Data not found |
| Fax | Fax | text |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Last Enriched Time | Last_Enriched_Time__s | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Phone | Phone | phone |  |  |
| Rating | Rating | picklist |  | -None-, Tier 1, Tier 2, Project Cancelled, Shut Down, +1 more |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| Tag | Tag | text |  |  |
| Website | Website | website |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| ABN Number | ABN_Number | text |  |  |
| Account Status | Account_Status | picklist |  | -None-, Blacklisted, Need Advance Payment, No Restrictions |
| Street 2 | Billing_Street_2 | text |  |  |
| Created Date | Created_Date | date |  |  |
| Details Updated Date | Details_Updated_Date | date |  |  |
| Email | Email | email |  |  |
| Email for Invoice | Email_for_Invoice | email |  |  |
| Home Phone | Home_Phone | phone |  |  |
| Interest Rating (out of 5) | Interest_Rating | integer |  |  |
| Is_Converted | Is_Converted | boolean |  |  |
| Last Invoice Amount | Last_Invoice_Amount | currency |  |  |
| Marketing Opt out | Marketing_Opt_out | boolean |  |  |
| Multi-Line 3 | Multi_Line_3 | textarea |  |  |
| Next Follow Up (Tier 1) | Next_Follow_Up_Tier_1 | date |  |  |
| Number of Attendees | Number_of_Attendees | integer |  |  |
| Other Phone | Other_Phone | phone |  |  |
| Payment Period | Payment_Period | picklist |  | -None-, End of Current Month, After End of Month, In Days |
| Payment term in days | Payment_term_in_days | integer |  |  |
| Po Required | Po_Required | boolean |  |  |
| Relevant Industry | Relevant_Industry | picklist |  | -None-, Accounting, Airlines/Aviation, Alternative Dispute Resolution, Alternative Medicine, +143 more |
| Send Update your Details Form | Send_Update_your_Details_Form | boolean |  |  |
| State. | State | picklist |  | -None-, VIC, NSW, TAS, QLD, +4 more |
| Tier 1 Stage | Tier_1_Stage | picklist |  | -None-, To Contact, Blockout Date Email Sent, Called Client, Quote Sent - Private, +6 more |
| Update Your details sent | Update_Your_details_sent | date |  |  |
| Xero ID | Xero_ID | text |  |  |
| Date of last visit | googlemapreports__Date_of_last_visit | date |  |  |
| Event Name | googlemapreports__Event_Name | text |  |  |
| Google response Expiration | googlemapreports__Google_response_expire_date | date |  |  |
| Latitude | googlemapreports__Latitude | text |  |  |
| Longitude | googlemapreports__Longitude | text |  |  |
| INACTIVE | inactive | boolean |  |  |
| Sinch Auto Responders Enabled | twiliosmsextension0__Twilio_Auto_Responders_Enabled | boolean |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Contact | Account_Contact | → Contacts |  |
| Account Payable | Account_Payable | → Contacts |  |
| Created By | Created_By | → Unknown |  |
| Last Course | Last_Course | → Courses |  |
| Modified By | Modified_By | → Unknown |  |
| Account Owner | Owner | → Unknown |  |
| Parent Account | Parent_Account | → Accounts |  |
| Primary Contact | Primary_Contact | → Contacts |  |
| Secondary Contact | Secondary_Contact | → Contacts |  |
| Tier Account Manager | Tier_Account_Manager | → Unknown |  |

**Legend:** 🔄 = Used in workflows

---

## Call_Analytics {#module-call-analytics}

**Total Fields:** 65
**Custom Fields:** 48
**Lookup Fields:** 4

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Created Time | Created_Time | datetime |  |  |
| Email | Email | email |  |  |
| Email Opt Out | Email_Opt_Out | boolean |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| CustomModule Name | Name | text | ✓ |  |
| Record Image | Record_Image | profileimage |  |  |
| Record Status | Record_Status__s | picklist |  | Available, Draft, Trash |
| Secondary Email | Secondary_Email | email |  |  |
| Tag | Tag | text |  |  |
| Unsubscribed Mode | Unsubscribed_Mode | picklist |  | Consent form, Manual, Unsubscribe link, Zoho campaigns |
| Unsubscribed Time | Unsubscribed_Time | datetime |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| AI Processed | AI_Processed | boolean |  |  |
| AI Raw JSON Output | AI_Raw_JSON_Output | textarea |  |  |
| AI Coaching Summary | AI_Summary | textarea |  |  |
| Audio File URL | Audio_File_URL | website |  |  |
| CRM Call Record ID | CRM_Call_Record_ID | text |  |  |
| 3CX Call ID | CX_Call_ID | text |  |  |
| 3CX Recording ID | CX_Recording_ID | text |  |  |
| Call Date | Call_Date | date |  |  |
| Call Duration (Minutes) | Call_Duration_Minutes | double |  |  |
| Call Duration (Seconds) | Call_Duration_Seconds | integer |  |  |
| Call Stage (Transcript) | Call_Stage_Transcript | picklist |  | -None-, Answered, Qualified, Needs Follow-Up, Send Quote,, +5 more |
| Call Start Datetime | Call_Start_Datetime | datetime |  |  |
| Call Time | Call_Time | datetime |  |  |
| Call Type | Call_Type | picklist |  | -None-, Inbound, Outbound, Internal, Other |
| Closing | Closing | integer |  |  |
| Completed Script Steps | Completed_Script_Steps | integer |  |  |
| Discovery | Discovery | integer |  |  |
| Extension | Extension | text |  |  |
| Insights Created | Insights_Created | boolean |  |  |
| Missed Steps | Missed_Steps | textarea |  |  |
| Non Standard Call | Non_Standard_Call | boolean |  |  |
| Not Enough Data flag | Not_Enough_Data_flag | boolean |  |  |
| Objection Category | Objection_Category | picklist |  | -None-, Price, Timing, Authority, Need, +2 more |
| Objection Sentences JSON | Objection_Sentences_JSON | textarea |  |  |
| Objection Themes JSON | Objection_Themes_JSON | textarea |  |  |
| Objections | Objections | integer |  |  |
| Opportunities | Opportunities | textarea |  |  |
| Overall Call Score | Overall_Call_Score | integer |  |  |
| Phone Number | Phone_Number | text |  |  |
| Primary Objection | Primary_Objection | text |  |  |
| Rapport | Rapport | integer |  |  |
| Recommended Coaching | Recommended_Coaching | textarea |  |  |
| Sales Script Key | Sales_Script_Key | text |  |  |
| Script Compliance % | Script_Compliance | percent |  |  |
| Script Fallback Used | Script_Fallback_Used | boolean |  |  |
| Script Name | Script_Name | text |  |  |
| Script Writer Doc ID | Script_Writer_Doc_ID | text |  |  |
| Secondary Objection | Secondary_Objection | text |  |  |
| Strengths | Strengths | textarea |  |  |
| Threats | Threats | textarea |  |  |
| Tier | Tier | picklist |  | -None-, Tier 1 New, Tier 1 Existing, Tier 2, Public, +1 more |
| Value | Value | integer |  |  |
| Weaknesses | Weaknesses | textarea |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account | Account | → Accounts |  |
| Agent | Agent | → Unknown |  |
| Contact | Contact | → Contacts |  |
| Created By | Created_By | → Unknown |  |
| Lead | Lead | → Leads |  |
| Modified By | Modified_By | → Unknown |  |
| CustomModule Owner | Owner | → Unknown |  |
| Related Call | Related_Call | → Leads |  |

**Legend:** 🔄 = Used in workflows

---

## Contacts {#module-contacts}

**Total Fields:** 124
**Custom Fields:** 64
**Lookup Fields:** 1

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| ADGROUPID | ADGROUPID | text |  |  |
| ADID | ADID | text |  |  |
| Ad | Ad | text |  |  |
| AdGroup Name | AdGroup_Name | text |  |  |
| Ad Campaign Name | Ad_Campaign_Name | text |  |  |
| Ad Click Date | Ad_Click_Date | date |  |  |
| Ad Network | Ad_Network | picklist |  | Search Network, Display Network |
| Average Time Spent (Minutes) | Average_Time_Spent_Minutes | double |  |  |
| Change Log Time | Change_Log_Time__s | datetime |  |  |
| Click Type | Click_Type | picklist |  | Other, Phone calls, Headline, Product plusbox offer, Sitelink, +8 more |
| Conversion Export Status | Conversion_Export_Status | picklist |  | -None-, Success, Failure, NA - Invalid, Not started |
| Conversion Exported On | Conversion_Exported_On | datetime |  |  |
| Cost per Click | Cost_per_Click | currency |  |  |
| Cost per Conversion | Cost_per_Conversion | currency |  |  |
| Created Time | Created_Time | datetime |  |  |
| Date of Birth | Date_of_Birth | date |  |  |
| Days Visited | Days_Visited | integer |  |  |
| Department | Department | text |  |  |
| Description | Description | textarea |  |  |
| Device Type | Device_Type | picklist |  | Other, Computers, Mobile devices with full browsers, Tablets with full browsers |
| Email | Email | email |  |  |
| Email Opt Out | Email_Opt_Out | boolean |  |  |
| Enrich Status | Enrich_Status__s | picklist |  | Available, Enriched, Data not found |
| Fax | Fax | text |  |  |
| First Name | First_Name | text |  |  |
| First Visited Time | First_Visited_Time | datetime |  |  |
| First Visited URL | First_Visited_URL | website |  |  |
| Full Name | Full_Name | text |  |  |
| GADCONFIGID | GADCONFIGID | text |  |  |
| GCLID | GCLID | text |  |  |
| Home Phone | Home_Phone | phone |  |  |
| KEYWORDID | KEYWORDID | text |  |  |
| Keyword | Keyword | text |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Last Enriched Time | Last_Enriched_Time__s | datetime |  |  |
| Last Name | Last_Name | text | ✓ |  |
| Last Visited Time | Last_Visited_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Mobile | Mobile | phone |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Number Of Chats | Number_Of_Chats | integer |  |  |
| Other Phone | Other_Phone | phone |  |  |
| Phone | Phone | phone |  |  |
| Reason for Conversion Failure | Reason_for_Conversion_Failure | picklist |  | -None-, INVALID_CONVERSION_TYPE, UNPARSEABLE_GCLID, CONVERSION_PRECEDES_CLICK, FUTURE_CONVERSION_TIME, +4 more |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| Referrer | Referrer | website |  |  |
| Salutation | Salutation | picklist |  | -None-, Mr., Mrs., Ms., Dr., +1 more |
| Search Partner Network | Search_Partner_Network | picklist |  | Google search, Search partners, Display Network |
| Secondary Email | Secondary_Email | email |  |  |
| Tag | Tag | text |  |  |
| Title | Title | text |  |  |
| Unsubscribed Mode | Unsubscribed_Mode | picklist |  | Consent form, Manual, Unsubscribe link, Zoho campaigns |
| Unsubscribed Time | Unsubscribed_Time | datetime |  |  |
| Visitor Score | Visitor_Score | bigint |  |  |
| ZCAMPAIGNID | ZCAMPAIGNID | text |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Address Line 1 | Address_Line_1 | text |  |  |
| Address Line 2 | Address_Line_2 | text |  |  |
| CC to | Alternate_Email | email |  |  |
| App_Password | App_Password | text |  |  |
| Color Code | Color_Code | text |  |  |
| Contact Source | Contact_Source | picklist |  | -None-, Advertisement, Booking Form, Calendly, Chat, +23 more |
| Contact Type | Contact_Type | picklist |  | -None-, Account Payable, Account's Contact, Blacklisted, Presenter, +8 more |
| Country | Country | picklist |  | -None-, Australia, New Zealand |
| Course End Date | Course_End_Date | date |  |  |
| Course For | Course_For | picklist |  | -None-, Myself, My Team |
| Course Name | Course_Name | text |  |  |
| Create task | Create_task | boolean |  |  |
| Created Date | Created_Date | date |  |  |
| Dashboard PIN | Dashboard_PIN | text |  |  |
| Dashboard URL | Dashboard_URL | website |  |  |
| Due Date | Due_Date | date |  |  |
| Interested By | Interested_By | picklist |  | -None-, Immediately, Next Month, Next 3 Months, Undecided |
| Is_Converted | Is_Converted | boolean |  |  |
| Last Course Booked | Last_Course_Booked | text |  |  |
| Lead/Contact Tier | Lead_Contact_Tier | picklist |  | -None-, Tier 1, Tier 2, Tier 3, Tier 4 |
| Lead_ID | Lead_ID | text |  |  |
| Lead_Notes | Lead_Notes | textarea |  |  |
| Marketing Opt Out | Marketing_Opt_Out | boolean |  |  |
| Objections | Multi_Line_3 | textarea |  |  |
| Position | Position | picklist |  | -None-, Admin, CEO, Coordinator, Manager, +6 more |
| Postcode | Postcode | text |  |  |
| Preferred Contact Method | Preferred_Contact_Method | picklist |  | -None-, Phone, Email, SMS |
| Priority | Priority | picklist |  | -None-, High, Medium, Low |
| Referral Form | Referral_Form | subform |  |  |
| Required For | Required_For | picklist |  | -None-, Internal |
| SMS Opt out | SMS_Opt_out | boolean |  |  |
| State | State | picklist |  | -None-, VIC, QLD, WA, SA, +4 more |
| Suburb | Suburb | text |  |  |
| Target Course per Month | Target_Course_per_Month | integer |  |  |
| Task Details | Task_Details | text |  |  |
| Task Name | Task_Name | text |  |  |
| Trainer Status | Trainer_Status | picklist |  | -None-, Active, Inactive |
| Attendee Status | Units | textarea |  |  |
| USI number | Usi_number | text |  |  |
| Venue Location | Venue_Location | text |  |  |
| WP Organizer ID | WP_Organizer_ID | text |  |  |
| Website Account Name | Website_Account_Name | text |  |  |
| Work Drive Link | Work_Drive_Link | website |  |  |
| Xero ID | Xero_ID | text |  |  |
| Date Time | clicksendext__Date_Time | datetime |  |  |
| Date of last visit | googlemapreports__Date_of_last_visit | date |  |  |
| Event Name | googlemapreports__Event_Name | text |  |  |
| Google response Expiration | googlemapreports__Google_response_expire_date | date |  |  |
| Latitude | googlemapreports__Latitude | text |  |  |
| Longitude | googlemapreports__Longitude | text |  |  |
| Social Lead ID | leadchain0__Social_Lead_ID | text |  |  |
| location | location | text |  |  |
| Address For Email To SMS | twiliosmsextension0__Address_For_Email_To_SMS | email |  |  |
| Last Time They Replied To Sinch Message | twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message | datetime |  |  |
| Last Time They Sent Us a Message | twiliosmsextension0__Last_Time_They_Sent_Us_a_Message | datetime |  |  |
| Num Inbound Sinch Messages | twiliosmsextension0__Num_Inbound_Twilio_Messages | integer |  |  |
| Num Outbound Sinch Messages | twiliosmsextension0__Num_Outbound_Twilio_Messages | integer |  |  |
| Sinch Conversation Team Assigned | twiliosmsextension0__Smooth_Conversation_Team_Assigned | text |  |  |
| They sent an SMS and we haven't replied | twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied | boolean |  |  |
| Sinch Auto Responders Enabled | twiliosmsextension0__Twilio_Auto_Responders_Enabled | boolean |  |  |
| Sinch Message Opt Out | twiliosmsextension0__Twilio_SMS_Message_Opt_Out | boolean |  |  |
| We Sent Them An SMS and They Haven't Replied | twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied | boolean |  |  |
| Whatsapp Number | twiliosmsextension0__Whatsapp_Number | text |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Name | Account_Name | → Accounts |  |
| Created By | Created_By | → Unknown |  |
| Modified By | Modified_By | → Unknown |  |
| Contact Owner | Owner | → Unknown |  |
| Task Owner | Task_Owner | → Unknown |  |

**Legend:** 🔄 = Used in workflows

---

## Courses {#module-courses}

**Total Fields:** 137
**Custom Fields:** 121
**Lookup Fields:** 6

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Created Time | Created_Time | datetime |  |  |
| Currency | Currency | picklist |  | AUD |
| Exchange Rate | Exchange_Rate | double |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| CustomModule Name | Name | text | ✓ |  |
| Record Image | Record_Image | profileimage |  |  |
| Record Status | Record_Status__s | picklist |  | Available, Draft, Trash |
| Tag | Tag | text |  |  |
| Unsubscribed Mode | Unsubscribed_Mode | picklist |  | Consent form, Manual, Unsubscribe link, Zoho campaigns |
| Unsubscribed Time | Unsubscribed_Time | datetime |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Accommodation Details For Trainer If Provided | Accommodation_Details_For_Trainer_If_Provided | textarea |  |  |
| Accommodation Location | Accommodation_Location | textarea |  |  |
| Accommodation Required | Accommodation_Required | picklist |  | -None-, Yes, No |
| Accommodation contact Phone for after hours | Accommodation_contact_details_for_after_hours | phone |  |  |
| Accommodation contact name for after hours | Accommodation_contact_name_for_after_hours | text |  |  |
| Add_Trainer_Calendar | Add_Trainer_Calendar | boolean |  |  |
| Additional Trainer Room information | Additional_information | textarea |  |  |
| Additional information - Accommodation | Additional_information_Accommodation | textarea |  |  |
| Next Action Item | Admin_Next_Action_Item | text |  |  |
| Task Status | Admin_Task_Status | picklist |  | -None-, Action Required, Due Soon, On Track |
| Airport Location | Airport_Location | text |  |  |
| Are Meals Provided | Are_Meals_Provided | picklist |  | -None-, Yes, No |
| Batch_Processed_Page | Batch_Processed_Page | integer |  |  |
| CRM Course ID | CRM_Course_ID | text |  |  |
| Certificate Update | Certificate_Update | picklist |  | -None-, Requested, Received, Sent |
| Check in at | Check_in_at | datetime |  |  |
| Check out at | Check_out_at | datetime |  |  |
| Company Car Available? | Company_Car_Available | picklist |  | -None-, Yes, No |
| Course Categories | Course_Categories | multiselectpicklist |  |  |
| Course Code | Course_Code | text |  |  |
| Course_Confirmed | Course_Confirmed | boolean |  |  |
| Course Delivery | Course_Delivery | picklist |  | -None-, Onsite Training Venue, Live Online (webinar style), Client Venue, Hybrid |
| Course Description | Course_Description | textarea |  |  |
| Course End Time | Course_End_Time | datetime |  |  |
| Course Start Time | Course_Start_Time | datetime |  |  |
| Course Status | Course_Status | picklist |  | -None-, Draft, Sync to Wordpress, Published, Cancelled, +3 more |
| Course Summary | Course_Summary | textarea |  |  |
| Course Type | Course_Type | picklist |  | -None-, Private, Public |
| Course Work Uploaded/Competent | Course_Work_Uploaded_Competent | boolean |  |  |
| Course Units To Be Covered | Course_units_to_be_covered | textarea |  |  |
| Create Meeting Record | Create_Meeting_Record | boolean |  |  |
| Created Date | Created_Date | date |  |  |
| Deal ID | Deal_ID | text |  |  |
| Departure Booking Ref | Departure_Booking_Ref | text |  |  |
| Details Food Provided | Details_Food_Provided | textarea |  |  |
| Details of Pick Up Car | Details_of_car_pick_up | textarea |  |  |
| Details of Hire Car | Details_of_hire_Car | textarea |  |  |
| Direct Flight? | Direct_Flight | picklist |  | -None-, Yes, No |
| Duration | Duration | formula |  |  |
| Auto Course ID | Event_ID | autonumber |  |  |
| Course URL | Event_URL | website |  |  |
| Facebook AD | Facebook_AD | boolean |  |  |
| Fee per registrant | Fees | currency |  |  |
| Flight Date | Flight_Date | date |  |  |
| Flight Number | Flight_Number | text |  |  |
| Flight to be booked? | Flight_to_be_booked | picklist |  | -None-, Yes, No |
| Food Provided | Food_Provided | picklist |  | -None-, Yes, No |
| For Client | For_Client | text |  |  |
| Z Form ID - client Onboarding Form | Form_ID | text |  |  |
| client Onboarding Submitted Date | Form_Submitted_Date | date |  |  |
| GST | GST | picklist |  | -None-, Exclusive GST, GST Free, Inclusive GST |
| Google Ad | Google_Ad | boolean |  |  |
| Hire Car? | Hire_Car | picklist |  | -None-, Yes, No |
| Hire Car Additional Information | Hire_Car_Additional_Information | textarea |  |  |
| Hire Car Required | Hire_Car_Required | picklist |  | -None-, Yes, No |
| Hotel Name | Hotel_Name | text |  |  |
| Induction | Induction | picklist |  | -None-, Yes, No |
| Is there any time constrain | Is_there_any_time_constrain | textarea |  |  |
| Luggage amount booked | Luggage_amount_booked | text |  |  |
| Monitor | MONTIOR | picklist |  | -None-, Yes, No |
| Maximum registrations | Maximum_registrations | integer |  |  |
| Minimum registrations | Minimum_registrations | integer |  |  |
| PPE requirements | PPE_requirements | textarea |  |  |
| Pick up Car | Pick_up_Car | picklist |  | -None-, Yes, No |
| Prerequisites | Prerequisites | textarea |  |  |
| Printer | Printer | picklist |  | -None-, Yes, No |
| Printing Being Pickup Or posted? | Printing_Being_Pickup_Or_posted | picklist |  | -None-, Pickup, Posted |
| Printing Pickup Details | Printing_Pickup_Details | textarea |  |  |
| Printing Postage Details | Printing_Postage_Details | textarea |  |  |
| Private Course Status | Private_Course_Status | picklist |  | -None-, Draft, Tentative, Confirmed, Completed, +1 more |
| Published Date | Published_Date | date |  |  |
| Publish on | Published_on | datetime |  |  |
| Registrations Booked | Registrations_Booked | integer |  |  |
| Registrations Confirmed | Registrations_Confirmed | integer |  |  |
| Return Booking Ref | Return_Booking_Ref | text |  |  |
| Return Direct Flight? | Return_Direct_Flight | picklist |  | -None-, Yes, No |
| Return Flight Airport  Location | Return_Flight_Airport_Location | text |  |  |
| Return Flight Number | Return_Flight_Number | text |  |  |
| Return Luggage amount booked | Return_Luggage_amount_booked | text |  |  |
| Return - Stop Over details if required | Return_Stop_Over_details_if_required | textarea |  |  |
| Return flight Date | Return_flight_Date | date |  |  |
| Room Available (Venue) | Room_Available_Venue | textarea |  |  |
| Scanner | SCANNER | picklist |  | -None-, Yes, No |
| SMS Opt Out | SMS_Opt_Out | boolean |  |  |
| Send Attendance PDF to Trainer | Send_Attendance_PDF_to_Trainer | boolean |  |  |
| Send Email to Coordinator | Send_Email_to_Coordinator | boolean |  |  |
| Send Trainer email | Send_Trainer_email | boolean |  |  |
| Site Location | Site_Location | text |  |  |
| Stop Over Details if required | Stop_Over_Details_if_required | textarea |  |  |
| Total Registrations | Total_Registrations | integer |  |  |
| Trainer Comments | Trainer_Comments | textarea |  |  |
| Trainer_Confirmed | Trainer_Confirmed | boolean |  |  |
| Trainer ID | Trainer_ID | text |  |  |
| Trainer_Meeting_ID | Trainer_Meeting_ID | text |  |  |
| Trainer Mobile | Trainer_Mobile | phone |  |  |
| Units | Units | textarea |  |  |
| Update Course | Update_Course | boolean |  |  |
| Update Registration Records | Update_Registration_Records | boolean |  |  |
| Venue Location | Venue_Location | text |  |  |
| Venue Site contact Mobile | Venue_Site_contact_Mobile | phone |  |  |
| Visibility | Visibility | picklist |  | -None-, Publish, Anyone with Link, Unpublished |
| Visitor pass required | Visitor_pass_required | picklist |  | -None-, Yes, No |
| Whiteboard | WHITEBOARD | picklist |  | -None-, Yes, No |
| WIFI | WIFI | picklist |  | -None-, Yes, No |
| WP Course ID | WP_Course_ID | text |  |  |
| WP Ticket ID | WP_Ticket_ID | text |  |  |
| What do you need from onsite for Visitor Pass | What_do_you_need_from_onsite_for_Visitor_Pass | text |  |  |
| What is the closest airport to your site | What_is_the_closest_airport_to_your_site | text |  |  |
| Where to park? | Where_to_park | textarea |  |  |
| Wifi Details | Wifi_Details | text |  |  |
| Workdrive URL | Workdrive_URL | website |  |  |
| Workflow Actions | Workflow_Actions | picklist |  | -None-, Ask for Additional Course Attendees Zform, Ask for Client Venue Details Zform, Send Trainer Email - with PDF, Send Training Coordinator Email (full format), +1 more |
| Xero Account Code | Xero_Account_Code | text |  |  |
| Xero Product Code | Xero_Product_Code | text |  |  |
| Zoom URL | Zoom_URL | website |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Course Qualification | Course_Qualification | → Products |  |
| Course Trainer | Course_Trainer | → Contacts |  |
| Created By | Created_By | → Unknown |  |
| Modified By | Modified_By | → Unknown |  |
| CustomModule Owner | Owner | → Unknown |  |
| Private Course Client | Private_Course_Client | → Accounts |  |
| Select Venue | Select_Venue | → Venues |  |
| Training Coordinator | Training_Coordinator | → Contacts |  |
| Venue Contact | Venue_Contact | → Contacts |  |

**Legend:** 🔄 = Used in workflows

---

## Deals {#module-deals}

**Total Fields:** 96
**Custom Fields:** 51
**Lookup Fields:** 7

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| ADGROUPID | ADGROUPID | text |  |  |
| ADID | ADID | text |  |  |
| Ad | Ad | text |  |  |
| AdGroup Name | AdGroup_Name | text |  |  |
| Ad Campaign Name | Ad_Campaign_Name | text |  |  |
| Ad Click Date | Ad_Click_Date | date |  |  |
| Ad Network | Ad_Network | picklist |  | Search Network, Display Network |
| Amount | Amount | currency |  |  |
| Change Log Time | Change_Log_Time__s | datetime |  |  |
| Click Type | Click_Type | picklist |  | Other, Phone calls, Headline, Product plusbox offer, Sitelink, +8 more |
| Closing Date | Closing_Date | date |  |  |
| Conversion Export Status | Conversion_Export_Status | picklist |  | -None-, Success, Failure, NA - Invalid, Not started |
| Conversion Exported On | Conversion_Exported_On | datetime |  |  |
| Cost per Click | Cost_per_Click | currency |  |  |
| Cost per Conversion | Cost_per_Conversion | currency |  |  |
| Created Time | Created_Time | datetime |  |  |
| Potential Name | Deal_Name | text | ✓ |  |
| Description | Description | textarea |  |  |
| Device Type | Device_Type | picklist |  | Other, Computers, Mobile devices with full browsers, Tablets with full browsers |
| Expected Revenue | Expected_Revenue | currency |  |  |
| GADCONFIGID | GADCONFIGID | text |  |  |
| GCLID | GCLID | text |  |  |
| KEYWORDID | KEYWORDID | text |  |  |
| Keyword | Keyword | text |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Lead Conversion Time | Lead_Conversion_Time | integer |  |  |
| Lead Source | Lead_Source | picklist |  | -None-, Advertisement, Booking Form, Calendly, Chat, +23 more |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Overall Sales Duration | Overall_Sales_Duration | integer |  |  |
| Reason For Loss | Reason_For_Loss__s | picklist |  | -None-, Expectation Mismatch, Price, Unqualified Customer, Lack of response, +5 more |
| Reason for Conversion Failure | Reason_for_Conversion_Failure | picklist |  | -None-, INVALID_CONVERSION_TYPE, UNPARSEABLE_GCLID, CONVERSION_PRECEDES_CLICK, FUTURE_CONVERSION_TIME, +4 more |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| Sales Cycle Duration | Sales_Cycle_Duration | integer |  |  |
| Search Partner Network | Search_Partner_Network | picklist |  | Google search, Search partners, Display Network |
| Stage | Stage | picklist | ✓ | Qualification, Proposal/Price Quote, Negotiation/Review, Needs Analysis, Ready to Quote, +10 more |
| Tag | Tag | text |  |  |
| Type | Type | picklist |  | -None-, Existing Business, New Business |
| ZCAMPAIGNID | ZCAMPAIGNID | text |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Amount Paid (Lead) | Amount_Paid_Lead | currency |  |  |
| Associated Course Code | Associated_Course_Code | text |  |  |
| Attendee Form submitted | Attendee_Form_submitted | date |  |  |
| Attendee Requested on | Attendee_Requested_on | date |  |  |
| Course ID | Course_ID | text |  |  |
| Course Start Date | Course_Start_Date | date |  |  |
| Course Type | Course_Type | picklist |  | -None-, Private, Public |
| Create team task | Create_Follow_up_Task | boolean |  |  |
| Created Date | Created_Date | date |  |  |
| Creation Source | Creation_Source | picklist |  | -None-, ZCheckout, Lead Conversion, Website, Deposit Payment, +2 more |
| Deal CRM ID | Deal_CRM_ID | text |  |  |
| Deal Identifier | Deal_Identifier | autonumber |  |  |
| Task Details | Follow_Up_Notes | textarea |  |  |
| Due Date | Follow_up_date | date |  |  |
| Is_Converted | Is_Converted | boolean |  |  |
| Lead_ID | Lead_ID | text |  |  |
| Loss Reason | Loss_Reason | textarea |  |  |
| Marketing Opt out | Marketing_Opt_out | boolean |  |  |
| Multi-Line 3 | Multi_Line_3 | textarea |  |  |
| Number of Attendees | Number_of_Attendees | integer |  |  |
| Po Expected Date | Po_Expected_Date | date |  |  |
| Po Required? | Po_Required | boolean |  |  |
| Preferred Payment Method | Preferred_Payment_Method | picklist |  | -None-, Bank Transfer, Other, Website - Credit Card, Website - Request a Quote, +2 more |
| Priority | Priority | picklist |  | -None-, High, Medium, Low |
| Purchase Order Number | Purchase_Order_Number | text |  |  |
| Quote incl. GST Amount | Quote_Amount | currency |  |  |
| Quote ID | Quote_ID | text |  |  |
| Request Attendees | Request_Attendees | boolean |  |  |
| Request PO URL | Request_PO_URL | website |  |  |
| Required For | Required_For | picklist |  | -None-, Internal |
| Task Name | Task_Name | text |  |  |
| Update | Udpate | boolean |  |  |
| Website Account Name | Website_Account_Name | text |  |  |
| Workflow Trigger | Workflow_Trigger | picklist |  | -None-, Update Deal ID, Update Stage, Create Quote, Deal Closed Won, +1 more |
| Social Lead ID | leadchain0__Social_Lead_ID | text |  |  |
| Address For Email To SMS | twiliosmsextension0__Address_For_Email_To_SMS | email |  |  |
| Last Time They Replied To Sinch Message | twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message | datetime |  |  |
| Last Time They Sent Us a Message | twiliosmsextension0__Last_Time_They_Sent_Us_a_Message | datetime |  |  |
| Num Inbound Sinch Messages | twiliosmsextension0__Num_Inbound_Twilio_Messages | integer |  |  |
| Num Outbound Sinch Messages | twiliosmsextension0__Num_Outbound_Twilio_Messages | integer |  |  |
| Sinch Conversation Team Assigned | twiliosmsextension0__Smooth_Conversation_Team_Assigned | text |  |  |
| They sent an SMS and we haven't replied | twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied | boolean |  |  |
| Sinch Auto Responders Enabled | twiliosmsextension0__Twilio_Auto_Responders_Enabled | boolean |  |  |
| Sinch SMS Message Opt Out | twiliosmsextension0__Twilio_SMS_Message_Opt_Out | boolean |  |  |
| We Sent Them An SMS and They Haven't Replied | twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied | boolean |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Contact | Account_Contact | → Contacts |  |
| Account Name | Account_Name | → Accounts |  |
| Contact Name | Contact_Name | → Contacts |  |
| Product | Course | → Products |  |
| Course | Courseaa | → Courses |  |
| Created By | Created_By | → Unknown |  |
| Modified By | Modified_By | → Unknown |  |
| Potential Owner | Owner | → Unknown |  |
| Parent Account | Parent_Account | → Accounts |  |
| Task Owner | Task_Owner | → Unknown |  |
| Training Coordinator | Training_Coordinator | → Contacts |  |

**Legend:** 🔄 = Used in workflows

---

## Invoices {#module-invoices}

**Total Fields:** 58
**Custom Fields:** 40
**Lookup Fields:** 6

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Created Time | Created_Time | datetime |  |  |
| Due Date | Due_Date | date |  |  |
| Invoice Date | Invoice_Date | date |  |  |
| Invoiced Items | Invoiced_Items | subform | ✓ |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| Status | Status | picklist |  | Draft, Awaiting Payment, Sent, Approved, Partially Paid, +5 more |
| Subject | Subject | text | ✓ |  |
| Tag | Tag | text |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| AR Crez To be paid on | A_R_Crez_To_be_paid_on | date |  |  |
| Amount Outstanding | Amount_Outstanding | currency |  |  |
| Course Type | Course_Type | text |  |  |
| Created Through | Created_Through | picklist |  | -None-, Lead Conversion, Website Sale, Through Quote Conversion |
| Dealid | Dealid | text |  |  |
| Email for Invoice | Email_for_Invoice | email |  |  |
| Get PO URL | Get_PO_URL | website |  |  |
| Inv. Reciepted | Inv_Reciepted | picklist |  | -None-, Yes |
| Invoice CRM ID | Invoice_CRM_ID | text |  |  |
| Invoice Sent Date | Invoice_Sent_Date | date |  |  |
| Invoice Paid Date | Invoice_Won_Date | date |  |  |
| Is_Converted | Is_Converted | boolean |  |  |
| Last Payment Amount | Last_Payment_Amount | currency |  |  |
| Last Payment Date | Last_Payment_Date | date |  |  |
| Lead_ID | Lead_ID | text |  |  |
| Merchant Fee | Merchant_Fee | currency |  |  |
| Paid In CREZ | Paid_In_CREZ | boolean |  |  |
| Payment Source | Payment_Source | picklist |  | -None-, Bank Transfer, Other, Website - Credit Card, Website - Request a Quote, +2 more |
| Payment Type | Payment_Type | picklist |  | -None-, Credit Card, Invoice |
| Payment Expected in Days | Payment_term_in_days | integer |  |  |
| Po Expected Date | Po_Expected_Date | date |  |  |
| Purchase Order Number | Purchase_Order_Number | text |  |  |
| Invoice Ref Number | Quote_Ref_Number | autonumber |  |  |
| Refresh PO URL | Refresh_PO_URL | boolean |  |  |
| Request Payment URL | Request_Payment_URL | website |  |  |
| Sent | Sent | boolean |  |  |
| Stripe Payment ID | Stripe_ID | text |  |  |
| Sync To Xero | Sync_To_Xero | boolean |  |  |
| Website Account Name | Website_Account_Name | text |  |  |
| Woocommerce Order ID | Woocommerce_Order_ID | text |  |  |
| Xero Invoice Number | Xero_Invoice_Number | text |  |  |
| Xero Invoice URL | Xero_Invoice_URL | website |  |  |
| Amounts Tax Inclusive | sbhtc__Amounts_Tax_Inclusive | boolean |  |  |
| Enable Overall Tax Calculator | sbhtc__Enable_Overall_Tax_Calculator | boolean |  |  |
| Total GST. | sbhtc__GST_Total | currency |  |  |
| Subtotal ex GST. | sbhtc__Subtotal_ex_GST0 | currency |  |  |
| Total inc GST. | sbhtc__Total_inc_GST0 | currency |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Contact | Account_Contact | → Contacts |  |
| Account Name | Account_Name | → Accounts |  |
| Contact Name | Contact_Name | → Contacts |  |
| Course Name | Course_Name | → Courses |  |
| Created By | Created_By | → Unknown |  |
| Potential Name | Deal_Name__s | → Deals |  |
| Modified By | Modified_By | → Unknown |  |
| Invoice Owner | Owner | → Unknown |  |
| Parent Account | Parent_Account | → Accounts |  |

**Legend:** 🔄 = Used in workflows

---

## Leads {#module-leads}

**Total Fields:** 161
**Custom Fields:** 89
**Lookup Fields:** 5

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| ADGROUPID | ADGROUPID | text |  |  |
| ADID | ADID | text |  |  |
| Ad | Ad | text |  |  |
| AdGroup Name | AdGroup_Name | text |  |  |
| Ad Campaign Name | Ad_Campaign_Name | text |  |  |
| Ad Click Date | Ad_Click_Date | date |  |  |
| Ad Network | Ad_Network | picklist |  | Search Network, Display Network |
| Average Time Spent (Minutes) | Average_Time_Spent_Minutes | double |  |  |
| Change Log Time | Change_Log_Time__s | datetime |  |  |
| City | City | text |  |  |
| Click Type | Click_Type | picklist |  | Other, Phone calls, Headline, Product plusbox offer, Sitelink, +8 more |
| Company | Company | text |  |  |
| Conversion Export Status | Conversion_Export_Status | picklist |  | -None-, Success, Failure, NA - Invalid, Not started |
| Conversion Exported On | Conversion_Exported_On | datetime |  |  |
| Converted Date Time | Converted_Date_Time | datetime |  |  |
| Is Converted | Converted__s | boolean |  |  |
| Cost per Click | Cost_per_Click | currency |  |  |
| Cost per Conversion | Cost_per_Conversion | currency |  |  |
| Country | Country | text |  |  |
| Created Time | Created_Time | datetime |  |  |
| Days Visited | Days_Visited | integer |  |  |
| Description | Description | textarea |  |  |
| Designation | Designation | text |  |  |
| Device Type | Device_Type | picklist |  | Other, Computers, Mobile devices with full browsers, Tablets with full browsers |
| Email | Email | email |  |  |
| Email Opt Out | Email_Opt_Out | boolean |  |  |
| Enrich Status | Enrich_Status__s | picklist |  | Available, Enriched, Data not found |
| Fax | Fax | text |  |  |
| First Name | First_Name | text |  |  |
| First Visited Time | First_Visited_Time | datetime |  |  |
| First Visited URL | First_Visited_URL | website |  |  |
| Full Name | Full_Name | text |  |  |
| GADCONFIGID | GADCONFIGID | text |  |  |
| GCLID | GCLID | text |  |  |
| Industry | Industry | picklist |  | -None-, Construction, Mining and Resources, Healthcare, Education and Training, +11 more |
| KEYWORDID | KEYWORDID | text |  |  |
| Keyword | Keyword | text |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Last Enriched Time | Last_Enriched_Time__s | datetime |  |  |
| Last Name | Last_Name | text | ✓ |  |
| Last Visited Time | Last_Visited_Time | datetime |  |  |
| Lead Conversion Time | Lead_Conversion_Time | integer |  |  |
| Lead Source | Lead_Source | picklist |  | -None-, Advertisement, Booking Form, Calendly, Chat, +23 more |
| Lead Status | Lead_Status | picklist |  | -None-, New Lead, New Lead - Website, New Lead - Google Ads, New Lead - Linkedin, +14 more |
| Locked | Locked__s | boolean |  |  |
| Mobile | Mobile | phone |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| No of Employees | No_of_Employees | integer |  |  |
| Number Of Chats | Number_Of_Chats | integer |  |  |
| Phone | Phone | phone |  |  |
| Rating | Rating | picklist |  | -None-, Tier 1, Tier 2, Tier 3, Project Cancelled, +1 more |
| Reason for Conversion Failure | Reason_for_Conversion_Failure | picklist |  | -None-, INVALID_CONVERSION_TYPE, UNPARSEABLE_GCLID, CONVERSION_PRECEDES_CLICK, FUTURE_CONVERSION_TIME, +4 more |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| Referrer | Referrer | website |  |  |
| Salutation | Salutation | picklist |  | -None-, Mr., Mrs., Ms., Dr., +1 more |
| Search Partner Network | Search_Partner_Network | picklist |  | Google search, Search partners, Display Network |
| State | State | text |  |  |
| Street | Street | text |  |  |
| Tag | Tag | text |  |  |
| Unsubscribed Mode | Unsubscribed_Mode | picklist |  | Consent form, Manual, Unsubscribe link, Zoho campaigns |
| Unsubscribed Time | Unsubscribed_Time | datetime |  |  |
| Visitor Score | Visitor_Score | bigint |  |  |
| Website | Website | website |  |  |
| ZCAMPAIGNID | ZCAMPAIGNID | text |  |  |
| Zip Code | Zip_Code | text |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| ABN | ABN | text |  |  |
| Student more 1 attendee | Attendees | subform |  |  |
| Clay search (company size) | Clay_search_company_size | text |  |  |
| Clay search (industries to include) | Clay_search_industries_to_include | text |  |  |
| Clay search (job titles) Training and Development | Clay_search_job_titles_Training_and_Development | text |  |  |
| Clay search (location) | Clay_search_location | text |  |  |
| Cold Call Campaign Name | Cold_Call_Campaign_Name | text |  |  |
| Cold Call Outreach Process | Cold_Call_Outreach_Process | picklist |  | -None-, Linked-In Message Sent / Connection Request, Leads w/o phone number, Leads w/out email address, Ist Email Sent, +6 more |
| Cold Call Tier | Cold_Call_Tier | picklist |  | -None-, Cold Call (Tier 1), Cold Call (Tier 2), Cold Call QLD (Tier 1) |
| Cold Outreach | Cold_Outreach | subform |  |  |
| Company Domain | Company_Domain | website |  |  |
| Send Course Email | Course_Email | boolean |  |  |
| Course For | Course_For | picklist |  | -None-, Myself, My Team |
| Course Status | Course_Status | text |  |  |
| Course Type | Course_Type | picklist |  | -None-, Private, Public, By Location |
| Course URL | Course_URL | website |  |  |
| Create task | Create_task | boolean |  |  |
| Due Date | Due_Date | date |  |  |
| EOI Location | EOI_Location | text |  |  |
| Enrich Person | Enrich_Person | picklist |  | -None-, Option 1, Option 2 |
| EoI Course Name | EoI_Course_Name | text |  |  |
| Course Fee per Student | Fees | currency |  |  |
| Find Mobile Number (2) | Find_Mobile_Number_2 | picklist |  | -None-, Option 1, Option 2 |
| Find Mobile Number (3) | Find_Mobile_Number_3 | picklist |  | -None-, Option 1, Option 2 |
| Find Mobile Number & Professional URLs | Find_Mobile_Number_Professional_URLs | picklist |  | -None-, Option 1, Option 2 |
| Find Mobile Number from LinkedIn | Find_Mobile_Number_from_LinkedIn | picklist |  | -None-, Option 1, Option 2 |
| Find Work Email | Find_Work_Email | text |  |  |
| Find Work Email (2) | Find_Work_Email_2 | picklist |  | -None-, Option 1, Option 2 |
| Find mobile number | Find_mobile_number | picklist |  | -None-, Option 1, Option 2 |
| Find phone number | Find_phone_number | picklist |  | -None-, Option 1, Option 2 |
| Find phone numbers | Find_phone_numbers | text |  |  |
| Find work email (3) | Find_work_email_3 | picklist |  | -None-, Option 1, Option 2 |
| Findymail Find Mobile Phone | Findymail_Find_Mobile_Phone | text |  |  |
| Home Phone | Home_Phone | phone |  |  |
| Interested By | Interested_By | picklist |  | -None-, Immediately, Next Month, Next 3 Months, Undecided, +1 more |
| Is_Converted | Is_Converted | boolean |  |  |
| Is interested in a private course | Is_interested_in_a_private_course | boolean |  |  |
| Last_Attendee_Contacts | Last_Attendee_Contacts | text |  |  |
| Last_Contact_ID | Last_Contact_ID | text |  |  |
| Last_Deal_ID | Last_Deal_ID | text |  |  |
| Last_Invoice_ID | Last_Invoice_ID | text |  |  |
| Lead/Contact Tier | Lead_Contact_Tier | picklist |  | -None-, Tier 1, Tier 2, Tier 3, Tier 4 |
| Lead Notes | Lead_Notes | textarea |  |  |
| Lead Stage | Lead_Stage | picklist |  | -None-, Linked-In Message Sent / Connect requested, Leads w/o phone number, Leads w/out email address, Ist Email Sent, +7 more |
| LinkedIn Profile | LinkedIn_Profile | website |  |  |
| Linked-In URL | Linked_In_URL | text |  |  |
| Location URL | Location_URL | website |  |  |
| Loss Reason | Loss_Reason | textarea |  |  |
| Marketing Opt out | Marketing_Opt_out | boolean |  |  |
| Merchant Fee | Merchant_Fee | currency |  |  |
| Multi-Line 3 | Multi_Line_3 | textarea |  |  |
| Number of Trainers | Number_of_Employees | text |  |  |
| Other Phone | Other_Phone | phone |  |  |
| Payment CODE | Payment_CODE | text |  |  |
| Payment source | Payment_source | picklist |  | -None-, Bank Transfer, Other, Website - Credit Card, Website - Request a Quote, +2 more |
| Position | Position | picklist |  | -None-, Admin, CEO, Coordinator, Manager, +6 more |
| Preferred Call Back | Preferred_Call_Back | datetime |  |  |
| Priority | Priority | picklist |  | -None-, High, Medium, Low |
| RecordID | RecordID | text |  |  |
| Required For | Required_For | picklist |  | -None-, Internal |
| SMS Opt Out | SMS_Opt_Out | boolean |  |  |
| Sale IQ Campaign Source | Sale_IQ_Campaign_Source | text |  |  |
| State. | State1 | picklist |  | -None-, VIC, QLD, WA, SA, +4 more |
| TEST SMS | TEST_SMS | boolean |  |  |
| Task Details | Task_Details | text |  |  |
| Task Name | Task_Name | text |  |  |
| WF Action | WF_Action | picklist |  | -None-, Update Location URL, Generate Payment URL, Ready to Convert, Convert - Non Payment, +3 more |
| Work Email | Work_Email | email |  |  |
| Zoho Form Payment URL | Zoho_Form_Payment_URL | website |  |  |
| Date Time | clicksendext__Date_Time | datetime |  |  |
| Fee ex merchant | fee_ex_merchant | currency |  |  |
| Date of last visit | googlemapreports__Date_of_last_visit | date |  |  |
| Event Name | googlemapreports__Event_Name | text |  |  |
| Google response Expiration | googlemapreports__Google_response_expire_date | date |  |  |
| Latitude | googlemapreports__Latitude | text |  |  |
| Longitude | googlemapreports__Longitude | text |  |  |
| Social Lead ID | leadchain0__Social_Lead_ID | text |  |  |
| Address For Email To SMS | twiliosmsextension0__Address_For_Email_To_SMS | email |  |  |
| Last time We Sent A Sinch Message | twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message | datetime |  |  |
| Last Time They Sent Us a Message | twiliosmsextension0__Last_Time_They_Sent_Us_a_Message | datetime |  |  |
| Num Inbound Sinch Messages | twiliosmsextension0__Num_Inbound_Twilio_Messages | integer |  |  |
| Num Outbound Sinch Messages | twiliosmsextension0__Num_Outbound_Twilio_Messages | integer |  |  |
| Sinch Conversation Team Assigned | twiliosmsextension0__Smooth_Conversation_Team_Assigned | text |  |  |
| They sent SMS - No Reply from us yet | twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied | boolean |  |  |
| Sinch Auto Responders Enabled | twiliosmsextension0__Twilio_Auto_Responders_Enabled | boolean |  |  |
| Sinch Message Opt Out | twiliosmsextension0__Twilio_SMS_Message_Opt_Out | boolean |  |  |
| We sent SMS - No reply from them | twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied | boolean |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Converted Account | Converted_Account | → Accounts |  |
| Converted Contact | Converted_Contact | → Contacts |  |
| Converted Deal | Converted_Deal | → Deals |  |
| Course | Course | → Courses |  |
| Created By | Created_By | → Unknown |  |
| Existing Company Record | Existing_Company_Record | → Accounts |  |
| Modified By | Modified_By | → Unknown |  |
| Lead Owner | Owner | → Unknown |  |

**Legend:** 🔄 = Used in workflows

---

## Quotes {#module-quotes}

**Total Fields:** 40
**Custom Fields:** 23
**Lookup Fields:** 7

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Created Time | Created_Time | datetime |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Quote Stage | Quote_Stage | picklist |  | Draft, Negotiation, Sent, Closed Won, Closed Lost, +3 more |
| Quoted Items | Quoted_Items | subform | ✓ |  |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| Subject | Subject | text | ✓ |  |
| Tag | Tag | text |  |  |
| Valid Till | Valid_Till | date |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Accept Quote URL | Accept_Quote_URL | website |  |  |
| Course_ID | Course_ID | text |  |  |
| Course Type | Course_Type | text |  |  |
| Deal ID | Deal_ID | text |  |  |
| Expected PO Date | Expected_PO_Date | date |  |  |
| Number of Attendees | Number_of_Attendees | integer |  |  |
| PO Number | PO_Number | text |  |  |
| Payment Source | Payment_Source | picklist |  | -None-, Bank Transfer, Other, Website - Credit Card, Website - Request a Quote, +2 more |
| Quote CRM ID | Quote_CRM_ID | text |  |  |
| Quote Ref Number | Quote_Ref_Number | autonumber |  |  |
| Quote Sent Date | Quote_Sent_Date | date |  |  |
| Quote Version | Quote_Version | picklist |  | -None-, 1, 2, 3, 4, +2 more |
| Quote Won Date | Quote_Won_Date | date |  |  |
| Send Quote as EMAIL | Send_Quote_as_EMAIL | boolean |  |  |
| Amounts Tax Inclusive | sbhtc__Amounts_Tax_Inclusive | boolean |  |  |
| Enable Overall Tax Calculator | sbhtc__Enable_Overall_Tax_Calculator | boolean |  |  |
| Subtotal ex GST. | sbhtc__Subtotal_ex_GST0 | currency |  |  |
| Total GST. | sbhtc__Total_GST0 | currency |  |  |
| Total inc GST. | sbhtc__Total_inc_GST0 | currency |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Contact | Account_Contact | → Contacts |  |
| Account Name | Account_Name | → Accounts |  |
| Contact Name | Contact_Name | → Contacts |  |
| Course Name | Course_Name | → Courses |  |
| Created By | Created_By | → Unknown |  |
| Potential Name | Deal_Name | → Deals |  |
| Modified By | Modified_By | → Unknown |  |
| Quote Owner | Owner | → Unknown |  |
| Parent Account | Parent_Account | → Accounts |  |
| Public Attendee | Public_Attendee | → Contacts |  |

**Legend:** 🔄 = Used in workflows

---

## Registration_Records {#module-registration-records}

**Total Fields:** 79
**Custom Fields:** 64
**Lookup Fields:** 9

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Created Time | Created_Time | datetime |  |  |
| Currency | Currency | picklist |  | AUD |
| Exchange Rate | Exchange_Rate | double |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Course Attendee Auto ID | Name | autonumber |  |  |
| Record Status | Record_Status__s | picklist |  | Available, Draft, Trash |
| Tag | Tag | text |  |  |
| Unsubscribed Mode | Unsubscribed_Mode | picklist |  | Consent form, Manual, Unsubscribe link, Zoho campaigns |
| Unsubscribed Time | Unsubscribed_Time | datetime |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Additional Documents Submitted | Additional_Documents_Submitted | boolean |  |  |
| Attendance Confirmed | Attendance_Confirmed | boolean |  |  |
| Attendee CRM ID | Attendee_CRM_ID | text |  |  |
| Attendee Email | Attendee_Email | email |  |  |
| Course Attendee Auto-name | Attendee_Naming | text |  |  |
| Attendee Type | Attendee_Type | picklist |  | -None-, Private Customer, Public Customer |
| CRM Course ID | CRM_Course_ID | text |  |  |
| CV Submitted | CV_Submitted | boolean |  |  |
| Certificate | Certificate | picklist |  | -None-, Pending, With RTO, Sent, Held Back |
| Certificate Held Back Reason | Certificate_Held_Back_Reason | multiselectpicklist |  |  |
| Course Code | Course_Code | text |  |  |
| Course Date and Time | Course_Date_and_Time | datetime |  |  |
| Course Days | Course_Days | subform |  |  |
| Course End Date | Course_End_Date | datetime |  |  |
| Course Status | Course_Status | text |  |  |
| Course Type | Course_Type | picklist |  | -None-, Public, Private |
| Create Team Task | Create_Team_Task | boolean |  |  |
| Created Date | Created_Date | date |  |  |
| Deal Stage | Deal_Stage | text |  |  |
| Post Requisite Evidence Complete | Difficulty_with_IT | picklist |  | -None-, Yes, No |
| Due Date | Due_Date | date |  |  |
| Compliance Check Done | English_second_language | picklist |  | -None-, Yes, No |
| Enrolled (Spec) | Enrolled_Spec | picklist |  | -None-, Yes, No |
| Evidence Received | Evidence_Received | picklist |  | -None-, Yes, No |
| Invoice Status | Invoice_Status | text |  |  |
| Is_Converted | Is_Converted | boolean |  |  |
| Lead_ID | Lead_ID | text |  |  |
| Lead Source | Lead_Source | picklist |  | -None-, Advertisement, Booking Form, Calendly, Chat, +23 more |
| Marketing Opt Out | Marketing_Opt_Out | boolean |  |  |
| Mobile | Mobile | phone |  |  |
| Note for the trainer | Note_for_the_trainer | textarea |  |  |
| Payment Source | Payment_Source | text |  |  |
| Payment Status | Payment_Status | picklist |  | -None-, Pending Confirmation, Confirmed |
| Priority | Priority | picklist |  | -None-, High, Medium, Low |
| Private Course Status | Private_Course_Status | text |  |  |
| SOA Received | Reading_writing_difficulties | picklist |  | -None-, Yes, No |
| Pre Requisite Evidence Complete | Request_3rd_Party_Record | boolean |  |  |
| Result | Result | picklist |  | -None-, Pending, Declared |
| Attending Course - Confirmation | SMS_Confirmation | picklist |  | -None-, Not Confirmed, Yes, No |
| SMS_Link | SMS_Link | text |  |  |
| SMS Opt Out | SMS_Opt_Out | boolean |  |  |
| SOA Sent | SOA_Sent | boolean |  |  |
| Send payment link | Send_payment_link | boolean |  |  |
| Status | Status | picklist |  | -None-, Spot Tentative, Spot Booked, To Be Rebooked, Waiting List, +6 more |
| StripeID | StripeID | text |  |  |
| Task Detail | Task_Detail | text |  |  |
| Task Name | Task_Name | text |  |  |
| Trainer ID | Trainer_ID | text |  |  |
| USI Number | USI_Number | text |  |  |
| Update Course Details | Update | boolean |  |  |
| Venue Address | Venue_Address | text |  |  |
| WP Order ID | WP_Order_ID | text |  |  |
| Website Account Name | Website_Account_Name | text |  |  |
| Workdrive URL | Workdrive_URL | website |  |  |
| send cert email | send_cert_email | boolean |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Name | Account_Name | → Accounts |  |
| Attendee | Attendee | → Contacts |  |
| Course | Course | → Courses |  |
| Created By | Created_By | → Unknown |  |
| Deal | Deal | → Deals |  |
| Invoice | Invoice | → Invoices |  |
| Modified By | Modified_By | → Unknown |  |
| CustomModule Owner | Owner | → Unknown |  |
| Quote | Quote | → Quotes |  |
| Related Deal | Related_Deal | → Deals |  |
| Trainer | Trainer | → Contacts |  |
| Venue | Venue | → Venues |  |

**Legend:** 🔄 = Used in workflows

---

## Sales_Orders {#module-sales-orders}

**Total Fields:** 47
**Custom Fields:** 5
**Lookup Fields:** 4

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Adjustment | Adjustment | currency |  |  |
| Billing City | Billing_City | text |  |  |
| Billing Code | Billing_Code | text |  |  |
| Billing Country | Billing_Country | text |  |  |
| Billing State | Billing_State | text |  |  |
| Billing Street | Billing_Street | text |  |  |
| Carrier | Carrier | picklist |  | FedEX, UPS, USPS, DHL, BlueDart |
| Created Time | Created_Time | datetime |  |  |
| Customer No | Customer_No | text |  |  |
| Description | Description | textarea |  |  |
| Discount | Discount | currency |  |  |
| Due Date | Due_Date | date |  |  |
| Excise Duty | Excise_Duty | currency |  |  |
| Grand Total | Grand_Total | formula |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Ordered Items | Ordered_Items | subform | ✓ |  |
| Pending | Pending | text |  |  |
| Purchase Order | Purchase_Order | text |  |  |
| Record Status | Record_Status__s | picklist |  | Trash, Available, Draft |
| SO Number | SO_Number | autonumber |  |  |
| Sales Commission | Sales_Commission | currency |  |  |
| Shipping City | Shipping_City | text |  |  |
| Shipping Code | Shipping_Code | text |  |  |
| Shipping Country | Shipping_Country | text |  |  |
| Shipping State | Shipping_State | text |  |  |
| Shipping Street | Shipping_Street | text |  |  |
| Status | Status | picklist |  | Created, Approved, Delivered, Cancelled |
| Sub Total | Sub_Total | formula |  |  |
| Subject | Subject | text | ✓ |  |
| Tag | Tag | text |  |  |
| Tax | Tax | currency |  |  |
| Terms and Conditions | Terms_and_Conditions | textarea |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Amounts Tax Inclusive | sbhtc__Amounts_Tax_Inclusive | boolean |  |  |
| Enable Overall Tax Calculator | sbhtc__Enable_Overall_Tax_Calculator | boolean |  |  |
| Subtotal ex GST. | sbhtc__Subtotal_ex_GST0 | currency |  |  |
| Total GST. | sbhtc__Total_GST0 | currency |  |  |
| Total inc GST. | sbhtc__Total_inc_GST0 | currency |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| Account Name | Account_Name | → Accounts |  |
| Contact Name | Contact_Name | → Contacts |  |
| Created By | Created_By | → Unknown |  |
| Potential Name | Deal_Name | → Deals |  |
| Modified By | Modified_By | → Unknown |  |
| Sales Order Owner | Owner | → Unknown |  |
| Quote Name | Quote_Name | → Quotes |  |

**Legend:** 🔄 = Used in workflows

---

## twiliosmsextension0__Sent_SMS {#module-twiliosmsextension0--sent-sms}

**Total Fields:** 59
**Custom Fields:** 43
**Lookup Fields:** 4

### Standard Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| Created Time | Created_Time | datetime |  |  |
| Currency | Currency | picklist |  | AUD |
| Exchange Rate | Exchange_Rate | double |  |  |
| Last Activity Time | Last_Activity_Time | datetime |  |  |
| Locked | Locked__s | boolean |  |  |
| Modified Time | Modified_Time | datetime |  |  |
| Sinch Message Name | Name | text | ✓ |  |
| Record Image | Record_Image | profileimage |  |  |
| Record Status | Record_Status__s | picklist |  | Available, Draft, Trash |
| Tag | Tag | text |  |  |
| Unsubscribed Mode | Unsubscribed_Mode | picklist |  | Consent form, Manual, Unsubscribe link, Zoho campaigns |
| Unsubscribed Time | Unsubscribed_Time | datetime |  |  |
| Record Id | id | bigint |  |  |

### Custom Fields

| Field | API Name | Type | Required | Details |
|-------|----------|------|----------|---------|
| From | From | text |  |  |
| Message | Message | textarea |  |  |
| Message Date | Message_Date | text |  |  |
| Message Type | Message_Type | text |  |  |
| Sid | Sid | text |  |  |
| To | To | text |  |  |
| API Names To Update | twiliosmsextension0__API_Names_To_Update | textarea |  |  |
| Activity ID | twiliosmsextension0__Activity_ID | text |  |  |
| Activity Type | twiliosmsextension0__Activity_Type | picklist |  | -None-, Task, Meeting, Call |
| Autoresponder Debug | twiliosmsextension0__Autoresponder_Debug | textarea |  |  |
| Autoresponder Message | twiliosmsextension0__Autoresponder_Message | boolean |  |  |
| Drip SMS Cancel on prior reply | twiliosmsextension0__Drip_SMS_Cancel_on_prior_reply | boolean |  |  |
| Error | twiliosmsextension0__Error | text |  |  |
| Field updates for parent record after sending | twiliosmsextension0__Field_updates_for_parent_record_after_sending | textarea |  |  |
| Hour Received | twiliosmsextension0__Hour_Received | text |  |  |
| MMS content | twiliosmsextension0__MMS_content | textarea |  |  |
| Message Recipient Replied? | twiliosmsextension0__Message_Recipient_Replied | boolean |  |  |
| Message Reporting Tag | twiliosmsextension0__Message_Reporting_Tag | text |  |  |
| Message Source | twiliosmsextension0__Message_Source | text |  |  |
| Metadata for sending SMS later | twiliosmsextension0__Metadata_for_sending_SMS_later | textarea |  |  |
| Mobile App Sending Metadata | twiliosmsextension0__Mobile_App_Sending_Metadata | textarea |  |  |
| Only use specified To field | twiliosmsextension0__Only_use_specified_To_field | boolean |  |  |
| Out of hours SMS | twiliosmsextension0__Out_of_hours_SMS | boolean |  |  |
| Phone Field API Name To Use | twiliosmsextension0__Phone_Field_API_Name_To_Use | text |  |  |
| Previous Outbound Message (for inbound messages) | twiliosmsextension0__Previous_Outbound_Message_for_inbound_messages | textarea |  |  |
| Previously linked to merged record id | twiliosmsextension0__Previously_linked_to_merged_record_id | text |  |  |
| Replied To Message ID | twiliosmsextension0__Replied_To_Message_ID | text |  |  |
| Reply Stats Updated | twiliosmsextension0__Reply_Stats_Updated | boolean |  |  |
| Response Time Minutes | twiliosmsextension0__Response_Time_Minutes | integer |  |  |
| Retry Count | twiliosmsextension0__Retry_Count | integer |  |  |
| Scheduled time to send | twiliosmsextension0__Scheduled_time_to_send | datetime |  |  |
| Send To User - enter User ID | twiliosmsextension0__Send_To_User_enter_User_ID | text |  |  |
| Skip Reschedule Check | twiliosmsextension0__Skip_Reschedule_Check | boolean |  |  |
| Skip duplicate check | twiliosmsextension0__Skip_duplicate_check | boolean |  |  |
| Status | twiliosmsextension0__Status | text |  |  |
| Sync Result | twiliosmsextension0__Sync_Result | textarea |  |  |
| Synced | twiliosmsextension0__Synced | boolean |  |  |
| Trigger Send via workflow | twiliosmsextension0__Trigger_Send_via_workflow | boolean |  |  |
| Webhook Contents | twiliosmsextension0__Twilio_Webhook_Contents | textarea |  |  |

### Lookup Fields

| Field | API Name | Target Module | Required |
|-------|----------|---------------|----------|
| ContactName | ContactName | → Contacts |  |
| Created By | Created_By | → Unknown |  |
| LeadName | LeadName | → Leads |  |
| Modified By | Modified_By | → Unknown |  |
| CustomModule Owner | Owner | → Unknown |  |
| Campaign | twiliosmsextension0__Campaign | → Campaigns |  |
| DealName | twiliosmsextension0__DealName | → Deals |  |

**Legend:** 🔄 = Used in workflows

---

# Tier 2 Modules - Summary Reference {#tier2}

Summary statistics for supporting modules. See SYSTEM_OVERVIEW.md for complete module relationships.

## Actions_Performed {#module-actions-performed}

**Total Fields:** 7

| Type | Count |
|------|-------|
| text | 1 |
| website | 1 |
| double | 1 |
| datetime | 1 |
| lookup | 1 |
| textarea | 1 |
| bigint | 1 |

**Lookup Fields:**
- Chat Attachment → Attachments

---

## Associated_Attendees {#module-associated-attendees}

**Total Fields:** 12

| Type | Count |
|------|-------|
| text | 6 |
| lookup | 4 |
| datetime | 2 |

**Lookup Fields:**
- Parent Id → Course_Performance
- Course Attendee → Registration_Records
- Deal → Deals
- Invoice → Invoices

---

## Associated_Attendess {#module-associated-attendess}

**Total Fields:** 7

| Type | Count |
|------|-------|
| datetime | 2 |
| lookup | 2 |
| text | 2 |
| boolean | 1 |

**Lookup Fields:**
- Parent Id → Deals
- Attendees → Contacts

---

## Associated_Contacts {#module-associated-contacts}

**Total Fields:** 6

| Type | Count |
|------|-------|
| datetime | 2 |
| lookup | 2 |
| email | 1 |
| phone | 1 |

**Lookup Fields:**
- Parent Id → Accounts
- Contact Name → Contacts

---

## Associated_Deals {#module-associated-deals}

**Total Fields:** 10

| Type | Count |
|------|-------|
| datetime | 2 |
| lookup | 2 |
| currency | 2 |
| text | 2 |
| integer | 2 |

**Lookup Fields:**
- Parent Id → Course_Performance
- Deal Name → Deals

---

## Attachments {#module-attachments}

**Total Fields:** 10

| Type | Count |
|------|-------|
| ownerlookup | 3 |
| datetime | 2 |
| bigint | 2 |
| text | 1 |
| lookup | 1 |
| picklist | 1 |

---

## Attendees {#module-attendees}

**Total Fields:** 8

| Type | Count |
|------|-------|
| text | 3 |
| datetime | 2 |
| lookup | 1 |
| phone | 1 |
| email | 1 |

**Lookup Fields:**
- Parent Id → Leads

---

## Calls {#module-calls}

**Total Fields:** 29

| Type | Count |
|------|-------|
| picklist | 8 |
| text | 6 |
| datetime | 4 |
| ownerlookup | 3 |
| lookup | 2 |
| textarea | 2 |
| integer | 1 |
| boolean | 1 |

**Lookup Fields:**
- Who Id → Contacts
- What Id → se_module

---

## Campaigns {#module-campaigns}

**Total Fields:** 36

| Type | Count |
|------|-------|
| text | 7 |
| picklist | 6 |
| datetime | 4 |
| ownerlookup | 3 |
| currency | 3 |
| bigint | 3 |
| lookup | 3 |
| date | 2 |

**Lookup Fields:**
- Parent Campaign → Campaigns
- Sinch Template → twiliosmsextension0__SMS_Templates
- Sinch From Number to Use → twiliosmsextension0__Twilio_From_Numbers

---

## Cold_Outreach {#module-cold-outreach}

**Total Fields:** 4

| Type | Count |
|------|-------|
| datetime | 2 |
| lookup | 1 |
| text | 1 |

**Lookup Fields:**
- Parent Id → Leads

---

## Course_Days {#module-course-days}

**Total Fields:** 6

| Type | Count |
|------|-------|
| datetime | 2 |
| lookup | 1 |
| textarea | 1 |
| picklist | 1 |
| date | 1 |

**Lookup Fields:**
- Parent Id → Registration_Records

---

## Course_Performance {#module-course-performance}

**Total Fields:** 40

| Type | Count |
|------|-------|
| integer | 10 |
| text | 7 |
| datetime | 5 |
| currency | 5 |
| picklist | 2 |
| subform | 2 |
| formula | 2 |
| boolean | 2 |

**Lookup Fields:**
- Course → Courses

---

## Course_Tasks {#module-course-tasks}

**Total Fields:** 9

| Type | Count |
|------|-------|
| datetime | 2 |
| text | 2 |
| picklist | 2 |
| lookup | 1 |
| integer | 1 |
| userlookup | 1 |

**Lookup Fields:**
- Parent Id → Team_Task_Templates

---

## Course_Type_History {#module-course-type-history}

**Total Fields:** 13

| Type | Count |
|------|-------|
| picklist | 7 |
| datetime | 2 |
| ownerlookup | 1 |
| lookup | 1 |
| bigint | 1 |
| integer | 1 |

**Lookup Fields:**
- Full Name → Leads

---

## DealHistory {#module-dealhistory}

**Total Fields:** 12

| Type | Count |
|------|-------|
| picklist | 2 |
| integer | 2 |
| datetime | 2 |
| currency | 2 |
| lookup | 1 |
| ownerlookup | 1 |
| date | 1 |
| bigint | 1 |

**Lookup Fields:**
- Potential Name → Deals

---

## Email_Analytics {#module-email-analytics}

**Total Fields:** 24

| Type | Count |
|------|-------|
| integer | 18 |
| ownerlookup | 1 |
| picklist | 1 |
| module | 1 |
| datetime | 1 |
| currency | 1 |
| bigint | 1 |

---

## Email_Sentiment {#module-email-sentiment}

**Total Fields:** 8

| Type | Count |
|------|-------|
| integer | 3 |
| datetime | 1 |
| lookup | 1 |
| ownerlookup | 1 |
| module | 1 |
| email | 1 |

---

## Email_Template_Analytics {#module-email-template-analytics}

**Total Fields:** 14

| Type | Count |
|------|-------|
| integer | 8 |
| ownerlookup | 1 |
| lookup | 1 |
| picklist | 1 |
| module | 1 |
| datetime | 1 |
| bigint | 1 |

**Lookup Fields:**
- Template Name → Email_Template__s

---

## Events {#module-events}

**Total Fields:** 40

| Type | Count |
|------|-------|
| text | 10 |
| datetime | 6 |
| ownerlookup | 4 |
| picklist | 4 |
| textarea | 3 |
| lookup | 2 |
| multireminder | 2 |
| bigint | 2 |

**Lookup Fields:**
- Who Id → Contacts
- What Id → se_module

---

## Facebook {#module-facebook}

**Total Fields:** 5

| Type | Count |
|------|-------|
| textarea | 3 |
| picklist | 1 |
| lookup | 1 |

---

## Feedbacks {#module-feedbacks}

**Total Fields:** 45

| Type | Count |
|------|-------|
| picklist | 17 |
| text | 10 |
| textarea | 8 |
| datetime | 3 |
| ownerlookup | 2 |
| lookup | 2 |
| bigint | 1 |
| boolean | 1 |

**Lookup Fields:**
- Attendee Record → Registration_Records
- Trainer Record → Contacts

---

## Functions__s {#module-functions--s}

**Total Fields:** 27

| Type | Count |
|------|-------|
| picklist | 8 |
| text | 5 |
| boolean | 4 |
| textarea | 3 |
| bigint | 2 |
| ownerlookup | 2 |
| datetime | 2 |
| multiselectpicklist | 1 |

---

## Invoiced_Items {#module-invoiced-items}

**Total Fields:** 14

| Type | Count |
|------|-------|
| currency | 3 |
| formula | 3 |
| datetime | 2 |
| lookup | 2 |
| bigint | 1 |
| textarea | 1 |
| double | 1 |
| linetax | 1 |

**Lookup Fields:**
- Parent Id → Invoices
- Product Name → Products

---

## Locking_Information__s {#module-locking-information--s}

**Total Fields:** 9

| Type | Count |
|------|-------|
| bigint | 3 |
| picklist | 2 |
| textarea | 1 |
| multi_module_lookup | 1 |
| datetime | 1 |
| userlookup | 1 |

---

## Notes {#module-notes}

**Total Fields:** 11

| Type | Count |
|------|-------|
| ownerlookup | 3 |
| text | 2 |
| datetime | 2 |
| bigint | 2 |
| multi_module_lookup | 1 |
| picklist | 1 |

---

## Ordered_Items {#module-ordered-items}

**Total Fields:** 14

| Type | Count |
|------|-------|
| currency | 3 |
| formula | 3 |
| datetime | 2 |
| lookup | 2 |
| bigint | 1 |
| textarea | 1 |
| double | 1 |
| linetax | 1 |

**Lookup Fields:**
- Parent Id → Sales_Orders
- Product Name → Products

---

## Products {#module-products}

**Total Fields:** 26

| Type | Count |
|------|-------|
| text | 5 |
| textarea | 5 |
| ownerlookup | 3 |
| boolean | 3 |
| datetime | 3 |
| picklist | 3 |
| currency | 1 |
| multiselectpicklist | 1 |

---

## Projects_Inhouse {#module-projects-inhouse}

**Total Fields:** 25

| Type | Count |
|------|-------|
| picklist | 6 |
| text | 5 |
| datetime | 3 |
| textarea | 2 |
| boolean | 2 |
| date | 2 |
| ownerlookup | 1 |
| bigint | 1 |

---

## Projects_Tasks {#module-projects-tasks}

**Total Fields:** 20

| Type | Count |
|------|-------|
| picklist | 4 |
| text | 4 |
| datetime | 4 |
| date | 3 |
| ownerlookup | 1 |
| bigint | 1 |
| textarea | 1 |
| lookup | 1 |

**Lookup Fields:**
- Associated Project → Projects_Inhouse

---

## Quoted_Items {#module-quoted-items}

**Total Fields:** 14

| Type | Count |
|------|-------|
| currency | 3 |
| formula | 3 |
| datetime | 2 |
| lookup | 2 |
| bigint | 1 |
| textarea | 1 |
| double | 1 |
| linetax | 1 |

**Lookup Fields:**
- Parent Id → Quotes
- Product Name → Products

---

## Recurring_Tasks {#module-recurring-tasks}

**Total Fields:** 9

| Type | Count |
|------|-------|
| picklist | 3 |
| datetime | 2 |
| text | 2 |
| lookup | 1 |
| userlookup | 1 |

**Lookup Fields:**
- Parent Id → Team_Task_Templates

---

## Referral_Form {#module-referral-form}

**Total Fields:** 7

| Type | Count |
|------|-------|
| datetime | 2 |
| lookup | 2 |
| email | 1 |
| phone | 1 |
| text | 1 |

**Lookup Fields:**
- Parent Id → Contacts
- Referred Lead → Leads

---

## Sales_Scripts {#module-sales-scripts}

**Total Fields:** 25

| Type | Count |
|------|-------|
| text | 4 |
| datetime | 4 |
| picklist | 3 |
| ownerlookup | 3 |
| boolean | 3 |
| email | 2 |
| textarea | 2 |
| bigint | 1 |

---

## Tasks {#module-tasks}

**Total Fields:** 23

| Type | Count |
|------|-------|
| datetime | 4 |
| ownerlookup | 3 |
| text | 3 |
| picklist | 3 |
| boolean | 3 |
| lookup | 2 |
| date | 1 |
| RRULE | 1 |

**Lookup Fields:**
- Who Id → Contacts
- What Id → se_module

---

## Team_Task_Templates {#module-team-task-templates}

**Total Fields:** 15

| Type | Count |
|------|-------|
| picklist | 4 |
| datetime | 3 |
| text | 2 |
| ownerlookup | 2 |
| subform | 2 |
| bigint | 1 |
| boolean | 1 |

---

## Team_Tasks {#module-team-tasks}

**Total Fields:** 35

| Type | Count |
|------|-------|
| lookup | 9 |
| text | 8 |
| picklist | 7 |
| datetime | 3 |
| date | 3 |
| ownerlookup | 2 |
| bigint | 1 |
| boolean | 1 |

**Lookup Fields:**
- Course → Courses
- Course Attendee → Registration_Records
- Deal → Deals
- Invoice → Invoices
- Quote → Quotes
- *+4 more*

---

## Twitter {#module-twitter}

**Total Fields:** 5

| Type | Count |
|------|-------|
| textarea | 3 |
| picklist | 1 |
| lookup | 1 |

---

## Venues {#module-venues}

**Total Fields:** 23

| Type | Count |
|------|-------|
| text | 7 |
| picklist | 4 |
| datetime | 3 |
| textarea | 2 |
| ownerlookup | 1 |
| bigint | 1 |
| profileimage | 1 |
| boolean | 1 |

**Lookup Fields:**
- Venue Contact → Contacts

---

## twiliosmsextension0__Inbound_SMS {#module-twiliosmsextension0--inbound-sms}

**Total Fields:** 18

| Type | Count |
|------|-------|
| datetime | 6 |
| picklist | 3 |
| ownerlookup | 3 |
| text | 2 |
| double | 1 |
| bigint | 1 |
| profileimage | 1 |
| boolean | 1 |

---

## twiliosmsextension0__SMS_Templates {#module-twiliosmsextension0--sms-templates}

**Total Fields:** 19

| Type | Count |
|------|-------|
| picklist | 4 |
| datetime | 4 |
| ownerlookup | 3 |
| text | 2 |
| textarea | 2 |
| double | 1 |
| bigint | 1 |
| profileimage | 1 |

---

## twiliosmsextension0__Twilio_Autoresponders {#module-twiliosmsextension0--twilio-autoresponders}

**Total Fields:** 29

| Type | Count |
|------|-------|
| text | 6 |
| picklist | 4 |
| datetime | 4 |
| textarea | 4 |
| ownerlookup | 3 |
| boolean | 3 |
| double | 1 |
| bigint | 1 |

---

## twiliosmsextension0__Twilio_Error_Logs {#module-twiliosmsextension0--twilio-error-logs}

**Total Fields:** 18

| Type | Count |
|------|-------|
| datetime | 4 |
| picklist | 3 |
| ownerlookup | 3 |
| text | 2 |
| double | 1 |
| bigint | 1 |
| profileimage | 1 |
| boolean | 1 |

---

## twiliosmsextension0__Twilio_From_Numbers {#module-twiliosmsextension0--twilio-from-numbers}

**Total Fields:** 26

| Type | Count |
|------|-------|
| text | 8 |
| datetime | 4 |
| boolean | 4 |
| picklist | 3 |
| ownerlookup | 3 |
| double | 1 |
| bigint | 1 |
| profileimage | 1 |

---

## Related Documentation {#related-docs}

- **SYSTEM_OVERVIEW.md** - Module catalogue and relationships
- **WORKFLOW_DEPENDENCY_MAP.md** - Workflow and field dependencies
- **LATEST_CHANGES.md** - Recent field modifications
- **CHANGE_PLANNING_GUIDE.md** - Best practices for field changes

---

*Generated by `tools/generate_ai_kb.py` on 2026-01-08*
