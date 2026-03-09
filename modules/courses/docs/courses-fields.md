<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Courses Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 137

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
| Name | Course Name | text | Yes |
| Owner | Course Owner | ownerlookup | No |
| Record_Image | Course Image | profileimage | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Accommodation_Details_For_Trainer_If_Provided | Accommodation Details For Trainer If Provided | textarea | No |
| Accommodation_Location | Accommodation Location | textarea | No |
| Accommodation_Required | Accommodation Required | picklist | No |
| Accommodation_contact_details_for_after_hours | Accommodation contact Phone for after hours | phone | No |
| Accommodation_contact_name_for_after_hours | Accommodation contact name for after hours | text | No |
| Add_Trainer_Calendar | Add_Trainer_Calendar | boolean | No |
| Additional_information | Additional Trainer Room information | textarea | No |
| Additional_information_Accommodation | Additional information - Accommodation | textarea | No |
| Admin_Next_Action_Item | Next Action Item | text | No |
| Admin_Task_Status | Task Status | picklist | No |
| Airport_Location | Airport Location | text | No |
| Are_Meals_Provided | Are Meals Provided | picklist | No |
| Batch_Processed_Page | Batch_Processed_Page | integer | No |
| CRM_Course_ID | CRM Course ID | text | No |
| Certificate_Update | Certificate Update | picklist | No |
| Check_in_at | Check in at | datetime | No |
| Check_out_at | Check out at | datetime | No |
| Company_Car_Available | Company Car Available? | picklist | No |
| Course_Categories | Course Categories | multiselectpicklist | No |
| Course_Code | Course Code | text | No |
| Course_Confirmed | Course_Confirmed | boolean | No |
| Course_Delivery | Course Delivery | picklist | No |
| Course_Description | Course Description | textarea | No |
| Course_End_Time | Course End Time | datetime | No |
| Course_Start_Time | Course Start Time | datetime | No |
| Course_Status | Course Status | picklist | No |
| Course_Summary | Course Summary | textarea | No |
| Course_Type | Course Type | picklist | No |
| Course_Work_Uploaded_Competent | Course Work Uploaded/Competent | boolean | No |
| Course_units_to_be_covered | Course Units To Be Covered | textarea | No |
| Create_Meeting_Record | Create Meeting Record | boolean | No |
| Created_Date | Created Date | date | No |
| Deal_ID | Deal ID | text | No |
| Departure_Booking_Ref | Departure Booking Ref | text | No |
| Details_Food_Provided | Details Food Provided | textarea | No |
| Details_of_car_pick_up | Details of Pick Up Car | textarea | No |
| Details_of_hire_Car | Details of Hire Car | textarea | No |
| Direct_Flight | Direct Flight? | picklist | No |
| Duration | Duration | formula | No |
| Event_ID | Auto Course ID | autonumber | No |
| Event_URL | Course URL | website | No |
| Facebook_AD | Facebook AD | boolean | No |
| Fees | Fee per registrant | currency | No |
| Flight_Date | Flight Date | date | No |
| Flight_Number | Flight Number | text | No |
| Flight_to_be_booked | Flight to be booked? | picklist | No |
| Food_Provided | Food Provided | picklist | No |
| For_Client | For Client | text | No |
| Form_ID | Z Form ID - client Onboarding Form | text | No |
| Form_Submitted_Date | client Onboarding Submitted Date | date | No |
| GST | GST | picklist | No |
| Google_Ad | Google Ad | boolean | No |
| Hire_Car | Hire Car? | picklist | No |
| Hire_Car_Additional_Information | Hire Car Additional Information | textarea | No |
| Hire_Car_Required | Hire Car Required | picklist | No |
| Hotel_Name | Hotel Name | text | No |
| Induction | Induction | picklist | No |
| Is_there_any_time_constrain | Is there any time constrain | textarea | No |
| Luggage_amount_booked | Luggage amount booked | text | No |
| MONTIOR | Monitor | picklist | No |
| Maximum_registrations | Maximum registrations | integer | No |
| Minimum_registrations | Minimum registrations | integer | No |
| PPE_requirements | PPE requirements | textarea | No |
| Pick_up_Car | Pick up Car | picklist | No |
| Prerequisites | Prerequisites | textarea | No |
| Printer | Printer | picklist | No |
| Printing_Being_Pickup_Or_posted | Printing Being Pickup Or posted? | picklist | No |
| Printing_Pickup_Details | Printing Pickup Details | textarea | No |
| Printing_Postage_Details | Printing Postage Details | textarea | No |
| Private_Course_Status | Private Course Status | picklist | No |
| Published_Date | Published Date | date | No |
| Published_on | Publish on | datetime | No |
| Registrations_Booked | Registrations Booked | integer | No |
| Registrations_Confirmed | Registrations Confirmed | integer | No |
| Return_Booking_Ref | Return Booking Ref | text | No |
| Return_Direct_Flight | Return Direct Flight? | picklist | No |
| Return_Flight_Airport_Location | Return Flight Airport  Location | text | No |
| Return_Flight_Number | Return Flight Number | text | No |
| Return_Luggage_amount_booked | Return Luggage amount booked | text | No |
| Return_Stop_Over_details_if_required | Return - Stop Over details if required | textarea | No |
| Return_flight_Date | Return flight Date | date | No |
| Room_Available_Venue | Room Available (Venue) | textarea | No |
| SCANNER | Scanner | picklist | No |
| SMS_Opt_Out | SMS Opt Out | boolean | No |
| Send_Attendance_PDF_to_Trainer | Send Attendance PDF to Trainer | boolean | No |
| Send_Email_to_Coordinator | Send Email to Coordinator | boolean | No |
| Send_Trainer_email | Send Trainer email | boolean | No |
| Site_Location | Site Location | text | No |
| Stop_Over_Details_if_required | Stop Over Details if required | textarea | No |
| Total_Registrations | Total Registrations | integer | No |
| Trainer_Comments | Trainer Comments | textarea | No |
| Trainer_Confirmed | Trainer_Confirmed | boolean | No |
| Trainer_ID | Trainer ID | text | No |
| Trainer_Meeting_ID | Trainer_Meeting_ID | text | No |
| Trainer_Mobile | Trainer Mobile | phone | No |
| Units | Units | textarea | No |
| Update_Course | Update Course | boolean | No |
| Update_Registration_Records | Update Registration Records | boolean | No |
| Venue_Location | Venue Location | text | No |
| Venue_Site_contact_Mobile | Venue Site contact Mobile | phone | No |
| Visibility | Visibility | picklist | No |
| Visitor_pass_required | Visitor pass required | picklist | No |
| WHITEBOARD | Whiteboard | picklist | No |
| WIFI | WIFI | picklist | No |
| WP_Course_ID | WP Course ID | text | No |
| WP_Ticket_ID | WP Ticket ID | text | No |
| What_do_you_need_from_onsite_for_Visitor_Pass | What do you need from onsite for Visitor Pass | text | No |
| What_is_the_closest_airport_to_your_site | What is the closest airport to your site | text | No |
| Where_to_park | Where to park? | textarea | No |
| Wifi_Details | Wifi Details | text | No |
| Workdrive_URL | Workdrive URL | website | No |
| Workflow_Actions | Workflow Actions | picklist | No |
| Xero_Account_Code | Xero Account Code | text | No |
| Xero_Product_Code | Xero Product Code | text | No |
| Zoom_URL | Zoom URL | website | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Course_Qualification | Course Qualification | lookup | No |
| Course_Trainer | Course Trainer | lookup | No |
| Private_Course_Client | Private Course Client | lookup | No |
| Select_Venue | Select Venue | lookup | No |
| Training_Coordinator | Training Coordinator | lookup | No |
| Venue_Contact | Venue Contact | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
