<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Registration_Records Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 79

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
| Name | Course Attendee Auto ID | autonumber | No |
| Owner | Course Attendee Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Additional_Documents_Submitted | Additional Documents Submitted | boolean | No |
| Attendance_Confirmed | Attendance Confirmed | boolean | No |
| Attendee_CRM_ID | Attendee CRM ID | text | No |
| Attendee_Email | Attendee Email | email | No |
| Attendee_Naming | Course Attendee Auto-name | text | No |
| Attendee_Type | Attendee Type | picklist | No |
| CRM_Course_ID | CRM Course ID | text | No |
| CV_Submitted | CV Submitted | boolean | No |
| Certificate | Certificate | picklist | No |
| Certificate_Held_Back_Reason | Certificate Held Back Reason | multiselectpicklist | No |
| Course_Code | Course Code | text | No |
| Course_Date_and_Time | Course Date and Time | datetime | No |
| Course_Days | Course Days | subform | No |
| Course_End_Date | Course End Date | datetime | No |
| Course_Status | Course Status | text | No |
| Course_Type | Course Type | picklist | No |
| Create_Team_Task | Create Team Task | boolean | No |
| Created_Date | Created Date | date | No |
| Deal_Stage | Deal Stage | text | No |
| Difficulty_with_IT | Post Requisite Evidence Complete | picklist | No |
| Due_Date | Due Date | date | No |
| English_second_language | Compliance Check Done | picklist | No |
| Enrolled_Spec | Enrolled (Spec) | picklist | No |
| Evidence_Received | Evidence Received | picklist | No |
| Invoice_Status | Invoice Status | text | No |
| Is_Converted | Is_Converted | boolean | No |
| Lead_ID | Lead_ID | text | No |
| Lead_Source | Lead Source | picklist | No |
| Marketing_Opt_Out | Marketing Opt Out | boolean | No |
| Mobile | Mobile | phone | No |
| Note_for_the_trainer | Note for the trainer | textarea | No |
| Payment_Source | Payment Source | text | No |
| Payment_Status | Payment Status | picklist | No |
| Priority | Priority | picklist | No |
| Private_Course_Status | Private Course Status | text | No |
| Reading_writing_difficulties | SOA Received | picklist | No |
| Request_3rd_Party_Record | Pre Requisite Evidence Complete | boolean | No |
| Result | Result | picklist | No |
| SMS_Confirmation | Attending Course - Confirmation | picklist | No |
| SMS_Link | SMS_Link | text | No |
| SMS_Opt_Out | SMS Opt Out | boolean | No |
| SOA_Sent | SOA Sent | boolean | No |
| Send_payment_link | Send payment link | boolean | No |
| Status | Status | picklist | No |
| StripeID | StripeID | text | No |
| Task_Detail | Task Detail | text | No |
| Task_Name | Task Name | text | No |
| Trainer_ID | Trainer ID | text | No |
| USI_Number | USI Number | text | No |
| Update | Update Course Details | boolean | No |
| Venue_Address | Venue Address | text | No |
| WP_Order_ID | WP Order ID | text | No |
| Website_Account_Name | Website Account Name | text | No |
| Workdrive_URL | Workdrive URL | website | No |
| send_cert_email | send cert email | boolean | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Name | Account Name | lookup | No |
| Attendee | Attendee | lookup | No |
| Course | Course | lookup | No |
| Deal | Deal | lookup | No |
| Invoice | Invoice | lookup | No |
| Quote | Quote | lookup | No |
| Related_Deal | Related Deal | lookup | No |
| Trainer | Trainer | lookup | No |
| Venue | Venue | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
