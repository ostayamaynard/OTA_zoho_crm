# Zoho CRM Course Operations Workflow Mapping Guide

**Document Version:** 1.0  
**Data Source:** Zoho CRM Data Model 2025-11-13  
**Last Updated:** 13 November 2025

---

## Table of Contents

1. [Overview](#overview)
2. [Workflow Lifecycle](#workflow-lifecycle)
3. [Stage-by-Stage Breakdown](#stage-by-stage-breakdown)
4. [Field Mapping Reference](#field-mapping-reference)
5. [Workflow Dependencies](#workflow-dependencies)
6. [Integration Points](#integration-points)
7. [Best Practices](#best-practices)

---

## Overview

This document maps the Lucid Chart course operations workflow to actual Zoho CRM fields, modules, and automated workflows. The workflow manages the complete lifecycle of training courses from initial creation through to final archiving.

### Primary Modules Involved

- **Courses** - Main module for course records
- **Registration_Records** - Individual student enrolments
- **Contacts** - Trainers and attendees
- **Deals** - Sales opportunities
- **Invoices** - Billing records
- **Venues** - Training locations
- **Team_Tasks** - Operational tasks
- **Course_Performance** - Analytics and reporting

### Workflow Philosophy

The workflow follows a linear progression through eight distinct stages, with each stage building upon the outputs of previous stages. Automated workflows handle notifications, data synchronisation, and compliance tracking throughout.

---

## Workflow Lifecycle

```
Course Created → Course Approved → Coursework → Course Logistics → 
Course Enrolment → Course Delivery → Certification → Archiving
```

### Stage Progression Summary

| Stage | Primary Module | Key Outcome | Automation Count |
|-------|---------------|-------------|------------------|
| 1. Course Created | Courses | Course record initialised | 5 workflows |
| 2. Course Approved | Courses | Minimum registrations met | 4 workflows |
| 3. Coursework | Courses | Materials prepared | 0 workflows |
| 4. Course Logistics | Courses | Trainer arrangements complete | 5 workflows |
| 5. Course Enrolment | Registration_Records | Students enrolled & compliant | 5 workflows |
| 6. Course Delivery | Registration_Records | Attendance tracked | 7 workflows |
| 7. Certification | Registration_Records | Certificates issued | 5 workflows |
| 8. Archiving | Courses | Records archived | 1 workflow |

---

## Stage-by-Stage Breakdown

### Stage 1: Course Created

**Purpose:** Establish the foundational course record with essential details.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Course Date | `Course_Start_Time` | datetime | Courses | When course begins |
| | `Course_End_Time` | datetime | Courses | When course ends |
| Course Location | `Venue_Location` | text | Courses | Venue description |
| | `Select_Venue` | lookup → Venues | Courses | Structured venue reference |
| Course Trainer | `Course_Trainer` | lookup → Contacts | Courses | Assigned trainer |
| Course Details | `Course_Description` | textarea | Courses | Full course description |
| | `Course_Summary` | textarea | Courses | Brief summary |
| | `Prerequisites` | textarea | Courses | Entry requirements |
| | `Units` | textarea | Courses | Learning units covered |

#### Mandatory Field

- **Name** (Course Name) - System mandatory, auto-generated via naming convention workflow

#### Automated Workflows

1. **Udpate Course ID** (`52330000002444506`)
   - **Trigger:** On create
   - **Action:** Assigns unique course identifier
   - **Field Updated:** `CRM_Course_ID`

2. **Create Tasks for Course** (`52330000002661635`)
   - **Trigger:** On create
   - **Action:** Generates preparation tasks in Team_Tasks module
   - **Dependencies:** Uses Team_Task_Templates based on course type

3. **Naming Convention - Course** (`52330000004013116`)
   - **Trigger:** On create or edit
   - **Action:** Formats course name according to standards
   - **Pattern:** [Course Code] - [Qualification] - [Location] - [Date]

4. **Courses_ZohoFlow_CRM Course to Workdrive Folder** (`52330000002462001`)
   - **Trigger:** On create
   - **Action:** Creates folder structure in Zoho Workdrive
   - **Field Updated:** `Workdrive_URL`

5. **Course Performance Record** (`52330000008928362`)
   - **Trigger:** On create
   - **Action:** Initialises analytics tracking in Course_Performance module

#### Related Fields (Setup Phase)

- `Course_Type` (Public/Private) - Determines workflow variations
- `Course_Code` - Short identifier
- `Course_Qualification` (lookup → Products) - Links to course template
- `Maximum_registrations` - Capacity limit
- `Minimum_registrations` - Viability threshold
- `Fees` - Price per student
- `Course_Delivery` (Face-to-face/Online/Hybrid)
- `Visibility` - Public listing control

#### User Actions Required

1. Create course record with mandatory name
2. Select course qualification/template
3. Set dates and times
4. Assign venue and trainer
5. Define registration limits
6. Set pricing

#### Transition Criteria

Course progresses to **Course Approved** when:
- All mandatory fields completed
- `Course_Status` updated to indicate readiness for approval
- Typically when initial setup complete

---

### Stage 2: Course Approved

**Purpose:** Verify minimum registration thresholds and publish course for enrolment.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Min Trigger Levels Met | `Registrations_Confirmed` | integer | Courses | Count of confirmed students |
| | `Minimum_registrations` | integer | Courses | Required minimum |
| | `Registrations_Booked` | integer | Courses | Total booked (confirmed + tentative) |
| Sent to Spec (for Enrolment) Link | `Event_URL` | website | Courses | Public enrolment URL |
| | `Published_on` | datetime | Courses | Publication timestamp |
| | `Published_Date` | date | Courses | Publication date |
| | `WP_Course_ID` | text | Courses | WordPress course ID |

#### Automated Workflows

1. **Check Min registration** (`52330000003463406`)
   - **Trigger:** Date/datetime based (14 days before course)
   - **Action:** Validates minimum registrations met
   - **Alert:** Notifies if below minimum threshold

2. **Sync Course to Wordpress** (`52330000006315389`)
   - **Trigger:** Field update on `Course_Status`
   - **Active:** Yes
   - **Action:** Publishes/updates course on public website
   - **Condition:** Course_Status = 'Confirmed' or similar

3. **Course Confirmed - Website Calendar** (`52330000011998036`)
   - **Trigger:** Field update on `Course_Confirmed`
   - **Action:** Adds course to public calendar
   - **Integration:** WordPress calendar system

4. **Copy of Check MAX registration** (`52330000003463443`)
   - **Trigger:** Field update on `Registrations_Confirmed`
   - **Action:** Prevents overbooking
   - **Validation:** Registrations_Confirmed ≤ Maximum_registrations

#### Status Field Values

`Course_Status` picklist values:
- Draft
- Tentative
- Confirmed
- Cancelled
- Completed
- Archived

For **Private Courses**, additional field:
- `Private_Course_Status` with separate workflow handling

#### User Actions Required

1. Review registration numbers
2. Confirm course viability (≥ minimum registrations)
3. Set `Course_Confirmed` = true
4. Approve publication to website
5. Monitor registration progress

#### Transition Criteria

Course progresses to **Coursework** when:
- `Registrations_Confirmed` ≥ `Minimum_registrations`
- `Course_Status` = 'Confirmed'
- `Course_Confirmed` = true
- Published to website (if public course)

---

### Stage 3: Coursework

**Purpose:** Prepare, print, and distribute course materials to trainer.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Printed | `Printing_Being_Pickup_Or_posted` | picklist | Courses | Delivery method (Pickup/Posted) |
| | `Printing_Pickup_Details` | textarea | Courses | Collection instructions |
| Sent | `Printing_Postage_Details` | textarea | Courses | Dispatch tracking information |
| Received | `Course_Work_Uploaded_Competent` | boolean | Courses | Trainer confirms receipt |
| | `Workdrive_URL` | website | Courses | Digital materials location |

#### Related Documentation Fields

- `Course_Description` - Content to be covered
- `Course_Summary` - Brief overview
- `Prerequisites` - Required prior knowledge
- `Units` - Specific learning units
- `Course_units_to_be_covered` - Detailed unit list

#### Cross-Module References

**Registration_Records** also tracks per-attendee materials:
- `Workdrive_URL` - Individual attendee folder
- `Note_for_the_trainer` - Special requirements

#### User Actions Required

1. Prepare course materials
2. Arrange printing if required
3. Set `Printing_Being_Pickup_Or_posted` value
4. Complete pickup/postage details
5. Coordinate with trainer for materials receipt
6. Trainer confirms via `Course_Work_Uploaded_Competent` = true

#### Manual Workflows

This stage primarily involves manual operations with minimal automation. Key activities:
- Physical printing coordination
- Courier/postage arrangements
- Digital upload to Workdrive
- Trainer confirmation

#### Transition Criteria

Course progresses to **Course Logistics** when:
- `Course_Work_Uploaded_Competent` = true
- All materials confirmed delivered/accessible
- Typically 2-4 weeks before course start date

---

### Stage 4: Course Logistics

**Purpose:** Arrange trainer travel, accommodation, and venue logistics.

#### Zoho Fields Mapped - Trainer Travel

| Output | Zoho Field | Field Type | Description |
|--------|-----------|-----------|-------------|
| Trainer Travel | `Flight_to_be_booked` | picklist | Yes/No/Not Required |
| | `Flight_Date` | date | Departure date |
| | `Flight_Number` | text | Flight details |
| | `Departure_Booking_Ref` | text | Booking reference |
| | `Airport_Location` | text | Departure airport |
| | `Luggage_amount_booked` | text | Checked baggage |
| | `Direct_Flight` | picklist | Direct or with stops |
| | `Stop_Over_Details_if_required` | textarea | Connection details |
| | `Return_flight_Date` | date | Return date |
| | `Return_Flight_Number` | text | Return flight |
| | `Return_Booking_Ref` | text | Return booking ref |
| | `Return_Flight_Airport_Location` | text | Return airport |
| | `Return_Luggage_amount_booked` | text | Return baggage |
| | `Return_Direct_Flight` | picklist | Return flight type |
| | `Return_Stop_Over_details_if_required` | textarea | Return connections |

#### Zoho Fields Mapped - Accommodation

| Output | Zoho Field | Field Type | Description |
|--------|-----------|-----------|-------------|
| Trainer Accommodation | `Accommodation_Required` | picklist | Yes/No/Provided by client |
| | `Hotel_Name` | text | Hotel name |
| | `Accommodation_Location` | textarea | Full address |
| | `Check_in_at` | datetime | Check-in time |
| | `Check_out_at` | datetime | Check-out time |
| | `Accommodation_Details_For_Trainer_If_Provided` | textarea | Client-provided details |
| | `Additional_information_Accommodation` | textarea | Other notes |
| | `Accommodation_contact_name_for_after_hours` | text | Emergency contact |
| | `Accommodation_contact_details_for_after_hours` | phone | Emergency number |

#### Zoho Fields Mapped - Training Room

| Output | Zoho Field | Field Type | Description |
|--------|-----------|-----------|-------------|
| Training Room | `Select_Venue` | lookup → Venues | Venue record |
| | `Venue_Location` | text | Specific room/area |
| | `Venue_Contact` | lookup → Contacts | Site contact |
| | `Venue_Site_contact_Mobile` | phone | Contact number |
| | `Room_Available_Venue` | textarea | Available rooms |
| | `WIFI` | picklist | WiFi available? |
| | `Wifi_Details` | text | Network credentials |
| | `Printer` | picklist | Printer access |
| | `WHITEBOARD` | picklist | Whiteboard available |
| | `MONTIOR` | picklist | Screen/monitor |
| | `SCANNER` | picklist | Scanner available |
| | `Additional_information` | textarea | Other room facilities |

#### Zoho Fields Mapped - Other Logistics

| Output | Zoho Field | Field Type | Description |
|--------|-----------|-----------|-------------|
| Other | `Hire_Car_Required` | picklist | Vehicle rental needed |
| | `Hire_Car` | picklist | Confirmation of booking |
| | `Details_of_hire_Car` | textarea | Vehicle details |
| | `Hire_Car_Additional_Information` | textarea | Special requirements |
| | `Pick_up_Car` | picklist | Airport/hotel/site |
| | `Details_of_car_pick_up` | textarea | Collection details |
| | `Company_Car_Available` | picklist | Client vehicle available |
| | `Where_to_park` | textarea | Parking instructions |
| | `PPE_requirements` | textarea | Safety equipment |
| | `Visitor_pass_required` | picklist | Site access |
| | `What_do_you_need_from_onsite_for_Visitor_Pass` | text | Pass requirements |
| | `Induction` | picklist | Site induction needed |
| | `Are_Meals_Provided` | picklist | Food arrangements |
| | `Details_Food_Provided` | textarea | Meal details |

#### Automated Workflows

1. **Send Trainer Email** (`52330000002570460`)
   - **Trigger:** Manual - field update on `Send_Trainer_email`
   - **Action:** Emails comprehensive logistics to trainer
   - **Content:** Travel, accommodation, venue, and course details

2. **10 days before course SMS to Trainer** (`52330000002656676`)
   - **Trigger:** Automated - 10 days before `Course_Start_Time`
   - **Action:** SMS reminder to trainer
   - **Requires:** `Trainer_Mobile` and `SMS_Opt_Out` = false

3. **1 day before course SMS to Trainer** (`52330000002656692`)
   - **Trigger:** Automated - 1 day before `Course_Start_Time`
   - **Action:** Final SMS reminder
   - **Content:** Course details and contact information

4. **Trainer Info PDF** (`52330000010838346`)
   - **Trigger:** Automated - 3 days before course
   - **Action:** Generates PDF with all logistics details
   - **Delivery:** Email attachment

5. **Send to Trainer Calendar** (`52330000011998008`)
   - **Trigger:** Manual - field update on `Add_Trainer_Calendar`
   - **Action:** Creates calendar event for trainer
   - **Integration:** Zoho Calendar or external calendar

#### Lookup Dependencies

- `Course_Trainer` → Contacts module
- `Select_Venue` → Venues module
- `Venue_Contact` → Contacts module
- `Training_Coordinator` → Contacts module

#### User Actions Required

1. **Flight Booking** (if required):
   - Set `Flight_to_be_booked` = Yes
   - Enter all flight details and booking references
   - Add luggage and connection information

2. **Accommodation Booking** (if required):
   - Set `Accommodation_Required` = Yes
   - Complete hotel details and check-in/out times
   - Provide emergency contact information

3. **Venue Coordination**:
   - Select or create Venue record
   - Confirm room availability and facilities
   - Obtain WiFi credentials and access details
   - Document PPE and site access requirements

4. **Transport Arrangements**:
   - Arrange hire car if needed
   - Provide parking information
   - Coordinate pick-up/drop-off logistics

5. **Trigger Notifications**:
   - Set `Send_Trainer_email` = true to send logistics email
   - Set `Add_Trainer_Calendar` = true to create calendar event

#### Private Course Considerations

For private courses (`Course_Type` = 'Private'):
- Additional field: `Private_Course_Client` (lookup → Accounts)
- Client may provide accommodation/venue
- Field: `Accommodation_Details_For_Trainer_If_Provided`
- Field: `Site_Location` for client premises

#### Transition Criteria

Course progresses to **Course Enrolment** when:
- All required logistics arrangements confirmed
- Trainer notified and acknowledged
- Venue confirmed and accessible
- Typically 1-2 weeks before course start

---

### Stage 5: Course Enrolment

**Purpose:** Enrol students, verify compliance requirements, and confirm payments.

**Module Shift:** Primary operations now occur in **Registration_Records** module, with each registration linked to the parent Course via lookup field.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Compliance Completed | `English_second_language` | picklist | Registration_Records | Compliance Check Done |
| | `Request_3rd_Party_Record` | boolean | Registration_Records | Pre Requisite Evidence Complete |
| | `Difficulty_with_IT` | picklist | Registration_Records | Post Requisite Evidence Complete |
| | `Reading_writing_difficulties` | picklist | Registration_Records | SOA Received |
| | `USI_Number` | text | Registration_Records | Unique Student Identifier |
| | `CV_Submitted` | boolean | Registration_Records | Resume on file |
| | `Additional_Documents_Submitted` | boolean | Registration_Records | Supporting docs |

#### Mandatory Fields (Registration_Records)

The system automatically creates Registration_Records when students enrol. Each record requires:
- Parent_Id (auto-populated, not shown to users)
- Auto-generated Name (Course Attendee Auto ID)

#### Registration Status Flow

`Status` field (Registration_Records) progression:
1. **Spot Tentative** - Initial enquiry
2. **Pending Payment** - Awaiting payment
3. **Spot Booked** - Payment received
4. **Confirmed** - Compliance complete
5. **Completed** - Attended course
6. **Cancelled** - Withdrawn
7. **Did Not Attend** - No-show

#### Automated Workflows (Registration Creation)

1. **Populate Course Days** (`52330000002460165`)
   - **Trigger:** Registration record created
   - **Action:** Creates subform entries for each course day
   - **Subform:** `Course_Days` with fields: Course_Date, Attendance, Comments

2. **Calculate Registrations and create team task** (`52330000002518044`)
   - **Trigger:** Registration created
   - **Action:** Updates `Registrations_Booked` on parent Course
   - **Creates:** Team task for admin follow-up

3. **Registration_Records_ZohoFlow_Copy of CRM Contact** (`52330000005138075`)
   - **Trigger:** Registration created
   - **Action:** Creates Workdrive folder for attendee documents
   - **Field Updated:** `Workdrive_URL`

4. **Email - Attendee paid via credit card** (`52330000002582386`)
   - **Trigger:** Registration created (credit card payment)
   - **Action:** Sends confirmation email to attendee
   - **Condition:** `Payment_Source` = 'Credit Card'

5. **SMS Attendance Link** (`52330000005789634`)
   - **Trigger:** Registration created
   - **Action:** Sends attendance app link via SMS
   - **Field:** `SMS_Link` populated with shortened URL

#### Payment Processing Workflows

1. **Update Attendee for Payment Update with DEAL** (`52330000004335393`)
   - Links Registration to Deal and tracks payment status

2. **Email - Attendee Payment made for Invoice** (`52330000005157463`)
   - **Trigger:** Status field update
   - **Condition:** Status changed to 'Spot Booked' (payment received)
   - **Action:** Confirmation email sent

#### Attendance Reminder Workflows

1. **1 week prior to Public course** (`52330000002582766`)
   - Email reminder 7 days before course

2. **7 Days before Public course SMS Reminder** (`52330000002597951`)
   - SMS reminder for public courses

3. **14 days SMS Before Attendance Confirmation** (`52330000005789721`)
   - SMS requesting attendance confirmation

4. **SMS - Attendance Acknowledgement** (`52330000006676878`)
   - **Trigger:** `SMS_Confirmation` field updated
   - **Action:** Acknowledges attendee response

#### Private Course Enrolment Variations

Additional workflows for private courses:
- **Private Attendee - Spot Tentative** (`52330000005163090`)
- **Private course Tentative - Attendee Spot Booked** (`52330000005163175`)
- **Private Course Confirmed - Attendee Spot Booked** (`52330000005163264`)
- **1 week prior to Private Confirmed course** (`52330000005163385`)

These workflows handle different status combinations:
- `Status` (registration status)
- `Private_Course_Status` (from parent course)

#### Key Fields

**Registration_Records:**
- `Status` - Registration status
- `Attendee` (lookup → Contacts)
- `Course` (lookup → Courses)
- `USI_Number` - Mandatory for compliance
- `Attendee_Email` - Contact email
- `Mobile` - Contact number
- `SMS_Opt_Out` - Opt-out flag
- `Marketing_Opt_Out` - Marketing preference
- `Attendee_Type` (Public/Private)
- `Payment_Source` (Credit Card/Invoice/Other)
- `Invoice` (lookup → Invoices)
- `Deal` (lookup → Deals)
- `Quote` (lookup → Quotes)

**Course-Level Tracking (Courses module):**
- `Total_Registrations` - All registrations
- `Registrations_Booked` - Confirmed bookings
- `Registrations_Confirmed` - Paid and compliant

#### User Actions Required

1. **For Each Registration:**
   - Verify USI number
   - Complete compliance checks
   - Confirm prerequisite evidence
   - Upload required documents to Workdrive
   - Set compliance fields appropriately

2. **Payment Verification:**
   - Link to Invoice/Deal records
   - Confirm payment received
   - Update Status accordingly

3. **Monitoring:**
   - Track registration counts vs minimums/maximums
   - Follow up on pending payments
   - Chase missing compliance documents

#### Transition Criteria

Course progresses to **Course Delivery** when:
- All (or sufficient) registrations have Status = 'Confirmed'
- Compliance checks complete for all attendees
- Payment confirmed (or PO received for invoiced attendees)
- Course start date approaching (typically within 1 week)

---

### Stage 6: Course Delivery

**Purpose:** Conduct the course and track daily attendance.

**Note:** This stage runs concurrently with the actual course dates.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Attendance Captured | `Course_Days` | subform | Registration_Records | Daily attendance tracking |
| Coursework Received | `Course_Work_Uploaded_Competent` | boolean | Courses | Student work collected |
| | `Trainer_Comments` | textarea | Courses | Trainer observations |

#### Course_Days Subform Structure

The `Course_Days` subform (within Registration_Records) contains:

| Field | Type | Purpose |
|-------|------|---------|
| `Course_Date` | date | Specific day of multi-day course |
| `Attendance` | picklist | Present/Absent/Late/Left Early |
| `Comments` | textarea | Notes about attendance or behaviour |

**Creation:** Auto-populated when Registration created (workflow: Populate Course Days)  
**Updates:** Manually updated during course delivery

#### Automated Workflows - Pre-Delivery

1. **Send Attendance App email 11 days prior to start** (`52330000002569380`)
   - **Module:** Courses
   - **Trigger:** 11 days before `Course_Start_Time`
   - **Action:** Sends attendance app access to trainer

2. **1 Day prior Attendance PDF** (`52330000012545268`)
   - **Module:** Courses
   - **Trigger:** 1 day before `Course_Start_Time`
   - **Action:** Generates attendance list PDF
   - **Distribution:** Email to trainer

#### Automated Workflows - During Delivery

1. **Manual Trigger for Attendance PDF** (`52330000004569126`)
   - **Module:** Courses
   - **Trigger:** Manual - `Workflow_Actions` field update
   - **Action:** Generate attendance PDF on demand
   - **Use Case:** Re-generate if needed during course

2. **Send attendance to Trainer** (`52330000004815267`)
   - **Module:** Courses
   - **Trigger:** `Send_Attendance_PDF_to_Trainer` = true
   - **Action:** Emails current attendance status

#### Automated Workflows - Attendee Communication

1. **1 week prior to Public course** (`52330000002582766`)
   - **Module:** Registration_Records
   - **Trigger:** 7 days before course
   - **Action:** Email reminder to attendees

2. **7 Days before Public course SMS Reminder** (`52330000002597951`)
   - **Module:** Registration_Records
   - **Trigger:** 7 days before course
   - **Action:** SMS reminder

3. **14 days SMS Before Attendance Confirmation** (`52330000005789721`)
   - **Module:** Registration_Records
   - **Trigger:** 14 days before course
   - **Action:** SMS requesting confirmation

4. **SMS - Attendance Acknowledgement** (`52330000006676878`)
   - **Module:** Registration_Records
   - **Trigger:** `SMS_Confirmation` field update
   - **Action:** Acknowledgement SMS

5. **Thank you SMS** (`52330000002656733`)
   - **Module:** Registration_Records
   - **Trigger:** 1 day after `Course_End_Date`
   - **Action:** Thank you message to attendees

#### Status Updates

1. **Update Course Attended 1 week from course date** (`52330000003014483`)
   - Updates attendance flags 1 week post-course

2. **Update Course Attended 1 Day from course** (`52330000003014499`)
   - Updates attendance flags 1 day post-course

#### Key Fields

**Courses Module:**
- `Course_Status` - Overall status
- `Course_Start_Time` / `Course_End_Time`
- `Workflow_Actions` - Manual triggers
- `Send_Attendance_PDF_to_Trainer`
- `Trainer_Comments`

**Registration_Records Module:**
- `Course_Days` (subform) - Daily attendance
- `Attendance_Confirmed` - Pre-course confirmation
- `SMS_Confirmation` - Response to SMS
- `Evidence_Received` - Post-course evidence
- `Note_for_the_trainer` - Special needs/notes

#### User Actions Required

**Before Course Starts:**
1. Review attendance list and confirmations
2. Ensure all attendees have `Attendance_Confirmed` = true
3. Provide final list to trainer
4. Generate and send attendance PDF

**During Course:**
1. Trainer updates `Course_Days` subform daily:
   - Mark attendance status for each day
   - Add comments about issues or observations
2. Collect completed coursework from students
3. Monitor no-shows and late arrivals

**After Course:**
1. Ensure all `Course_Days` entries complete
2. Set `Course_Work_Uploaded_Competent` = true (on Course)
3. Trainer completes `Trainer_Comments`
4. Upload final materials to Workdrive

#### Transition Criteria

Course progresses to **Certification** when:
- Course end date passed
- All `Course_Days` attendance marked
- Coursework collected from students
- `Course_Status` updated to 'Completed' or similar
- Trainer feedback received

---

### Stage 7: Certification

**Purpose:** Process certificates, verify competency, and distribute credentials.

**Module:** Primarily **Registration_Records** for individual certificates, with **Courses** module for overall tracking.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Coursework Sent to RTO | `Course_Work_Uploaded_Competent` | boolean | Courses | Materials submitted for assessment |
| Certificate Received | `Certificate` | picklist | Registration_Records | Certificate status |
| | | | | Values: Not Received, Received, Issued, Held Back |
| Compliance Checks Completed | `Difficulty_with_IT` | picklist | Registration_Records | Post Requisite Evidence Complete |
| | `Reading_writing_difficulties` | picklist | Registration_Records | SOA Received (Statement of Attainment) |
| | `Result` | picklist | Registration_Records | Competent/Not Yet Competent |
| Certificate Sent to Client | `SOA_Sent` | boolean | Registration_Records | Sent to employer (private courses) |
| Certificate Sent to Customer | `send_cert_email` | boolean | Registration_Records | Trigger to send to attendee |

#### Certificate Held Back Handling

If certificate cannot be issued:
- `Certificate` = 'Held Back'
- `Certificate_Held_Back_Reason` (multiselectpicklist) - Reasons:
  - Outstanding fees
  - Missing evidence
  - Incomplete coursework
  - Failed assessment
  - Administrative hold

#### Automated Workflows

1. **Certificate Held Back** (`52330000002667069`)
   - **Module:** Registration_Records
   - **Trigger:** `send_cert_email` field update
   - **Action:** Processes certificate distribution or hold notification
   - **Logic:** Checks if certificate can be released or must be held

2. **Status updated to completed** (`52330000004037507`)
   - **Module:** Courses
   - **Trigger:** `Course_Status` = 'Completed'
   - **Action:** Triggers post-completion workflows
   - **Updates:** Various completion flags and dates

3. **Completed course for WP. course Start Date** (`52330000004065214`)
   - **Module:** Courses
   - **Trigger:** 1 week after `Course_Start_Time`
   - **Action:** Marks course as complete on website
   - **Integration:** WordPress status update

4. **Trainer Feedback Email** (`52330000002656789`)
   - **Module:** Courses
   - **Trigger:** After course end date
   - **Action:** Requests feedback from trainer
   - **Field:** Links to Feedbacks module

5. **Trainer Task - to upload Course material** (`52330000002656953`)
   - **Module:** Courses
   - **Trigger:** After course end
   - **Action:** Reminds trainer to upload final materials

#### Course-Level Certification Tracking

**Courses Module:**
- `Certificate_Update` (picklist) - Overall status
  - All Received
  - Pending
  - Partial
  - Issues

#### Registration-Level Certification

**Registration_Records Module:**
- `Certificate` - Individual status
- `Certificate_Held_Back_Reason` - If applicable
- `Result` - Competency outcome
- `SOA_Sent` - Distributed to client/employer
- `send_cert_email` - Distribution trigger

#### Related Modules

**Feedbacks Module:**
- Linked to Registration_Records
- Fields: `Attendee_Record` (lookup)
- Captures trainer and attendee feedback
- Workflow: **Feedback Email from attendee** (currently inactive)

#### User Actions Required

1. **Submit to RTO:**
   - Upload completed coursework to RTO portal
   - Set `Course_Work_Uploaded_Competent` = true on Course
   - Track submission date

2. **Receive Certificates:**
   - Monitor RTO for certificate return
   - Update `Certificate` = 'Received' for each attendee
   - Record any issues or holds

3. **Compliance Verification:**
   - Complete `Difficulty_with_IT` (Post Requisite Evidence)
   - Confirm `Reading_writing_difficulties` (SOA Received)
   - Set `Result` = 'Competent' or 'Not Yet Competent'

4. **Distribution:**
   - For each attendee with `Certificate` = 'Received':
     - Set `send_cert_email` = true (triggers email)
     - For private courses: Set `SOA_Sent` = true after client notification
   - Handle held certificates appropriately

5. **Held Certificates:**
   - Set `Certificate` = 'Held Back'
   - Select `Certificate_Held_Back_Reason`(s)
   - Create follow-up tasks
   - Communicate with attendee about requirements

#### Private vs Public Course Handling

**Private Courses:**
- Often require SOA sent to client/employer
- Field: `SOA_Sent` tracks distribution
- May need batch processing for multiple attendees

**Public Courses:**
- Direct to attendee
- Individual email distribution
- Self-service download options

#### Transition Criteria

Course progresses to **Archiving** when:
- All certificates processed (received or held status assigned)
- All competent attendees have certificates distributed
- `send_cert_email` triggered for all applicable registrations
- Course-level `Certificate_Update` = 'All Received' or 'Partial'
- No outstanding certificate issues requiring resolution

---

### Stage 8: Archiving

**Purpose:** Finalise documentation, collect trainer materials, and archive records.

**Module:** Returns to **Courses** module for final status updates.

#### Zoho Fields Mapped

| Output | Zoho Field | Field Type | Module | Description |
|--------|-----------|-----------|---------|-------------|
| Paperwork Received from Trainer | `Trainer_Comments` | textarea | Courses | Final trainer notes and feedback |
| | `Course_Work_Uploaded_Competent` | boolean | Courses | All materials returned |
| Paperwork Archived | `Workdrive_URL` | website | Courses | Master folder with all documents |
| | `Course_Status` | picklist | Courses | Final status (Completed/Archived) |

#### Final Status Values

`Course_Status` final states:
- **Completed** - Successfully delivered
- **Cancelled** - Did not proceed
- **Archived** - Completed and archived

#### Automated Workflows

1. **Course Performance** (`52330000008928375`)
   - **Module:** Courses
   - **Trigger:** `Course_Status` field update
   - **Condition:** Status = 'Completed'
   - **Action:** Updates Course_Performance record with final metrics
   - **Updates:**
     - Total deals and revenue
     - Actual vs expected registrations
     - Invoice and payment status
     - Lead source analysis

#### Course Performance Tracking

When course archived, **Course_Performance** module records:

| Metric Field | Description |
|-------------|-------------|
| `Total_Deals` | Number of deals linked to course |
| `Total_Won_Deals` | Successfully closed deals |
| `Total_Lost_Deals` | Lost opportunities |
| `Booked_Registrations` | Final registration count |
| `Tentative_Registrations` | Enquiries that didn't convert |
| `Total_Invoices_Issued` | Number of invoices |
| `Total_Invoice_Amount` | Revenue generated |
| `Total_Paid_Amount` | Payments received |
| `Outstanding_Amount` | Awaiting Payment |
| `Total_Inv_Value_Ex` | Ex-GST total (formula) |
| `Total_Outstanding_Ex_GST` | Ex-GST outstanding (formula) |
| `Top_Lead_Source` | Most effective marketing channel |
| `Ex_GST_Value_of_Won_Deals` | Total deal value |

#### Cancellation Workflows

If course cancelled instead of completed:

1. **Cancelled Course WF** (`52330000003995688`)
   - **Trigger:** `Course_Status` = 'Cancelled'
   - **Action:** Notifies stakeholders, updates registrations

2. **Notification for Course Archive or Cancel** (`52330000011362374`)
   - **Trigger:** `Course_Status` change
   - **Action:** Sends notifications to relevant parties

3. **Registration Cancelled** (`52330000009966152`)
   - **Module:** Registration_Records
   - **Trigger:** `Status` = 'Cancelled'
   - **Action:** Updates course counts, notifies attendee

#### Trainer Feedback Collection

**Feedbacks Module** (linked to Registration_Records):
- `Trainer_Record` (lookup → Contacts)
- `Attendee_Record` (lookup → Registration_Records)
- Multiple rating fields for course quality
- Open feedback fields

#### Archive Checklist

Documentation to be confirmed in Workdrive:
- Attendance records (from Course_Days)
- Completed coursework
- Certificates (copies)
- Trainer materials and feedback
- Payment/invoice records
- Compliance documentation (USI, prerequisites)
- Communication history

#### User Actions Required

1. **Collect Final Materials:**
   - Request any outstanding paperwork from trainer
   - Upload to Workdrive folder
   - Update `Trainer_Comments` with final notes

2. **Verify Course_Performance Record:**
   - Review auto-generated metrics
   - Validate financial figures
   - Check registration accuracy

3. **Final Status Update:**
   - Set `Course_Status` = 'Completed' or 'Archived'
   - Triggers performance calculations

4. **Documentation Review:**
   - Ensure all critical documents in Workdrive
   - Verify `Workdrive_URL` accessible
   - Check all Registration_Records complete

5. **Trainer Feedback:**
   - Review feedback submissions
   - Address any issues raised
   - Update trainer performance notes

#### Final Workflows

**Course Performance** workflow runs automatically when status updated to completed:
- Aggregates data from linked Deals, Invoices, and Registrations
- Populates Course_Performance record
- Updates `Last_Updated` timestamp
- Can be re-run via `Run_Scheduler` = true

#### Transition Criteria

**Workflow Complete** when:
- `Course_Status` = 'Completed' or 'Archived'
- All paperwork received and uploaded
- Course_Performance record populated
- All Registration_Records have final Status values
- No outstanding tasks or issues
- **Next stage:** NULL (workflow terminates)

---

## Field Mapping Reference

### Courses Module - Complete Field List by Stage

#### Stage 1: Course Created
- `Name` (mandatory)
- `Course_Start_Time`, `Course_End_Time`
- `Course_Trainer` (lookup)
- `Venue_Location`
- `Course_Description`, `Course_Summary`
- `Course_Code`, `Course_Type`
- `Course_Qualification` (lookup)
- `Minimum_registrations`, `Maximum_registrations`
- `Fees`

#### Stage 2: Course Approved
- `Course_Status`
- `Course_Confirmed`
- `Registrations_Confirmed`, `Registrations_Booked`
- `Event_URL`
- `Published_on`, `Published_Date`
- `WP_Course_ID`
- `Visibility`

#### Stage 3: Coursework
- `Printing_Being_Pickup_Or_posted`
- `Printing_Pickup_Details`, `Printing_Postage_Details`
- `Course_Work_Uploaded_Competent`
- `Workdrive_URL`

#### Stage 4: Course Logistics
- `Flight_to_be_booked`, flight details fields
- `Accommodation_Required`, accommodation fields
- `Select_Venue` (lookup), venue facility fields
- `Hire_Car_Required`, vehicle fields
- `Send_Trainer_email`, `Add_Trainer_Calendar`
- `Trainer_Mobile`, `SMS_Opt_Out`

#### Stage 6: Course Delivery
- `Workflow_Actions`
- `Send_Attendance_PDF_to_Trainer`
- `Trainer_Comments`
- `Course_Status` (update to Completed)

#### Stage 7: Certification
- `Certificate_Update`
- `Course_Work_Uploaded_Competent`

#### Stage 8: Archiving
- `Course_Status` (final)
- `Workdrive_URL`
- `Trainer_Comments`

### Registration_Records Module - Complete Field List by Stage

#### Stage 5: Course Enrolment
- `Course` (lookup - mandatory)
- `Attendee` (lookup)
- `Status`
- `USI_Number`
- `English_second_language` (Compliance Check Done)
- `Request_3rd_Party_Record` (Pre Requisite Evidence)
- `CV_Submitted`, `Additional_Documents_Submitted`
- `Attendee_Email`, `Mobile`
- `SMS_Opt_Out`, `Marketing_Opt_Out`
- `Payment_Source`, `Invoice`, `Deal`, `Quote` (lookups)
- `Workdrive_URL`
- `SMS_Link`

#### Stage 6: Course Delivery
- `Course_Days` (subform)
  - `Course_Date`
  - `Attendance`
  - `Comments`
- `Attendance_Confirmed`
- `SMS_Confirmation`
- `Note_for_the_trainer`

#### Stage 7: Certification
- `Certificate`
- `Certificate_Held_Back_Reason`
- `Result`
- `Difficulty_with_IT` (Post Requisite Evidence Complete)
- `Reading_writing_difficulties` (SOA Received)
- `SOA_Sent`
- `send_cert_email`
- `Evidence_Received`

---

## Workflow Dependencies

### Workflow Execution Order

#### On Course Creation (Immediate)
1. `Udpate Course ID` - Assigns CRM_Course_ID
2. `Naming Convention - Course` - Formats Name field
3. `Create Tasks for Course` - Generates Team_Tasks
4. `Courses_ZohoFlow_CRM Course to Workdrive Folder` - Creates folders
5. `Course Performance Record` - Initialises analytics

#### Pre-Course (Time-Based)
- **14 days before:** Check Min registration, SMS reminders
- **11 days before:** Send Attendance App email
- **10 days before:** SMS to Trainer
- **3 days before:** Trainer Info PDF
- **1 day before:** Final SMS to Trainer, Attendance PDF

#### During Course
- **Manual triggers:** Attendance PDF generation, trainer emails

#### Post-Course (Time-Based)
- **1 day after:** Thank you SMS, attendance updates
- **1 week after:** Attendance updates, trainer feedback request
- **On completion:** Course Performance update, website update

### Cross-Module Workflow Dependencies

#### Courses → Registration_Records
- Course creation triggers registration-level workflows
- Course updates cascade to registration records
- **Key Workflow:** Update Registration records (`52330000003999102`)

#### Registration_Records → Courses
- Registration status updates affect course counts
- **Key Workflows:**
  - Calculate Registrations (`52330000002518060`)
  - Update course details (`52330000003014626`)

#### Courses → Deals → Invoices
- Payment tracking flows through Deals and Invoices
- **Deal Workflows:**
  - Create Quote - Stage Update Ready to quote (`52330000002460308`)
  - Purchase Order Received (`52330000002460283`)
- **Invoice Workflows:**
  - Push Invoice to Xero (`52330000002460231`)
  - Invoice Udpate (`52330000002610986`)

#### Registration_Records → Invoices
- Individual attendee invoicing
- **Key Fields:** `Invoice` (lookup), `Invoice_Status` (text)

### Conditional Workflow Branching

#### Public vs Private Courses

**Public Course Workflows:**
- Standard SMS and email sequences
- Website publication
- Individual payment processing

**Private Course Workflows:**
- `Private course Status Updates` (`52330000004318762`)
- `Private Course Status changed` (`52330000005069426`)
- `Private Course Client Selected` (`52330000010760918`)
- Batch processing for attendees
- Corporate invoicing
- SOA to client

**Trigger Field:** `Course_Type` picklist (Public/Private)  
**Additional Field (Private):** `Private_Course_Client` (lookup → Accounts)  
**Status Field (Private):** `Private_Course_Status`

---

## Integration Points

### External System Integrations

#### 1. Zoho Workdrive (Document Management)

**Purpose:** Centralised document storage for courses and attendees

**Workflows:**
- `Courses_ZohoFlow_CRM Course to Workdrive Folder` - Creates course folder
- `Registration_Records_ZohoFlow_Copy of CRM Contact` - Creates attendee folders
- `Move Course Attendee Folder on Course Change` (`52330000005375288`)

**Key Fields:**
- `Workdrive_URL` (Courses)
- `Workdrive_URL` (Registration_Records)

**Folder Structure:**
```
Course Folder/
  ├── Course Materials/
  ├── Attendance Records/
  ├── Certificates/
  └── Attendees/
      ├── [Attendee 1]/
      ├── [Attendee 2]/
      └── ...
```

#### 2. WordPress Website (Public Course Listings)

**Purpose:** Public course calendar and enrolment

**Workflows:**
- `Sync Course to Wordpress` - Publishes course
- `Course Confirmed - Website Calendar` - Calendar integration
- `Completed course for WP. course Start Date` - Status updates

**Key Fields:**
- `WP_Course_ID` - WordPress post ID
- `WP_Ticket_ID` - Event ticket ID
- `Event_URL` - Public course URL
- `Published_on`, `Published_Date`
- `Visibility` (Public/Private)

**Synchronised Data:**
- Course name, dates, location
- Trainer information (if public)
- Pricing and availability
- Course status

#### 3. Xero Accounting System

**Purpose:** Financial record synchronisation

**Workflows:**
- `Push Invoice to Xero` (`52330000002460231`)
- `Push Account Updates to Xero` (`52330000002460265`)
- `Push Contact Updates to Xero` (`52330000002460248`)

**Key Fields:**
- `Xero_Invoice_URL`, `Xero_Invoice_Number` (Invoices)
- `Xero_ID` (Contacts, Accounts)
- `Xero_Account_Code`, `Xero_Product_Code` (Courses)

**Triggered On:**
- Invoice status changes
- Contact/Account updates
- Payment processing

#### 4. ClickSend SMS Platform

**Purpose:** SMS notifications to trainers and attendees

**Module:** `clicksendext__Clicksend_SMS`

**SMS Workflows:**
- Trainer reminders (10 days, 1 day before)
- Attendee confirmations (14 days, 7 days before)
- Attendance link distribution
- Thank you messages

**Key Fields (Registration_Records):**
- `Mobile` - Phone number
- `SMS_Opt_Out` - Opt-out flag
- `SMS_Link` - Attendance app URL
- `SMS_Confirmation` - Response tracking

**Key Fields (Courses):**
- `Trainer_Mobile`
- `SMS_Opt_Out`

#### 5. Attendance App (Custom Integration)

**Purpose:** Digital attendance tracking

**Workflows:**
- `Send Attendance App email 11 days prior to start`
- `SMS Attendance Link` - Sends link to attendees
- `Generate SMS Shorten Link` (`52330000005789649`)

**URL Generation:**
Shortened URLs created 15 days before course for easy mobile access.

---

## Best Practices

### Data Entry Standards

#### 1. Course Creation
- Use `Course_Qualification` lookup to auto-populate description and units
- Set realistic `Minimum_registrations` based on viability
- Set `Maximum_registrations` based on venue capacity
- Always assign `Course_Trainer` early to enable logistics planning

#### 2. Registration Management
- Capture `USI_Number` during enrolment (mandatory for RTO compliance)
- Set `SMS_Opt_Out` and `Marketing_Opt_Out` flags correctly
- Link to `Deal` and `Invoice` records for payment tracking
- Use `Note_for_the_trainer` for special requirements

#### 3. Status Management
- Update `Course_Status` progressively (don't skip stages)
- Keep `Registrations_Confirmed` accurate (auto-updated by workflows)
- Mark `Course_Confirmed` = true only when committed to running
- Use `Private_Course_Status` for private courses

### Workflow Triggers

#### Manual Triggers (Boolean Fields)
Set to `true` to trigger workflows:
- `Send_Trainer_email` - Logistics email
- `Add_Trainer_Calendar` - Calendar invite
- `Send_Attendance_PDF_to_Trainer` - Attendance list
- `send_cert_email` - Certificate distribution
- `Update_Registration_Records` - Sync updates
- `Update_Course` - Refresh course data

#### Picklist Triggers (WF_Action Type Fields)
- `Workflow_Actions` (Courses) - Multi-purpose trigger
- `WF_Action` (Leads) - Conversion workflows

### Compliance Requirements

#### Mandatory for RTO Compliance
1. **USI Number** - Every attendee must have valid USI
2. **Pre-Requisite Evidence** - Documented before course
3. **Post-Requisite Evidence** - Verified after course
4. **Attendance Records** - Complete Course_Days subform
5. **Competency Assessment** - `Result` field set
6. **Certificate Distribution** - Tracked and documented

#### Compliance Checklist Fields
- ✓ `English_second_language` (Compliance Check Done)
- ✓ `Request_3rd_Party_Record` (Pre Requisite Evidence)
- ✓ `Difficulty_with_IT` (Post Requisite Evidence)
- ✓ `Reading_writing_difficulties` (SOA Received)
- ✓ `USI_Number` populated
- ✓ `Result` = 'Competent'
- ✓ `Certificate` = 'Received' or 'Issued'

### Performance Optimisation

#### Registration Count Calculations
Workflows auto-calculate registration counts:
- Don't manually update `Registrations_Booked` or `Registrations_Confirmed`
- These update via workflows when Registration_Records created/updated
- **Workflow:** Calculate Registrations (`52330000002518060`)

#### Status-Based Workflow Efficiency
Many workflows trigger on status changes:
- Update status fields in batch when possible
- Be aware status change triggers multiple workflows
- Example: Setting `Course_Status` = 'Completed' triggers:
  - Course Performance update
  - Website update
  - Notification workflows
  - Archive workflows

### Common Pitfalls to Avoid

#### 1. Premature Status Changes
**Don't** set `Course_Status` = 'Confirmed' before:
- Minimum registrations met
- Trainer assigned and confirmed
- Venue booked
- Logistics arranged

#### 2. Missing Lookups
Always populate lookup fields:
- `Course_Trainer` - Required for SMS and emails
- `Select_Venue` - Required for location details
- `Attendee` - Required for each Registration_Record
- `Course` - Required link from Registration to parent Course

#### 3. SMS Opt-Outs
Check before manual communications:
- `SMS_Opt_Out` field on Contacts/Registrations
- Workflows respect this flag automatically
- Manual SMS must check this field

#### 4. Duplicate Registrations
Prevent duplicates:
- Check existing Registration_Records for Course
- Use `Attendee` lookup to link to existing Contact
- Don't create new Contact if already exists

#### 5. Private Course Handling
For `Course_Type` = 'Private':
- Must set `Private_Course_Client` (lookup → Accounts)
- Use `Private_Course_Status` instead of/alongside `Course_Status`
- Different invoice workflow (consolidated vs individual)
- SOA distribution to client, not individuals

### Automation Monitoring

#### Key Workflows to Monitor

**High-Frequency Workflows:**
- Calculate Registrations (runs on every registration create/update)
- Naming Convention workflows (run on create/edit)
- Update Registration records (manual trigger)

**Time-Sensitive Workflows:**
- Check Min registration (14 days before)
- SMS reminders (14 days, 7 days, 1 day before)
- Attendance PDF generation (1 day before)

**Critical Workflows:**
- Certificate Held Back (manages certificate distribution)
- Course Performance (financial reporting)
- Sync to WordPress (public visibility)

#### Workflow Failure Recovery

If workflow fails:
1. Check `Last_Activity_Time` on record
2. Review workflow execution history in Zoho
3. Verify required fields populated
4. Check lookup field references valid
5. For manual triggers, reset boolean field (false → true)

### Data Integrity Checks

#### Before Course Delivery
- [ ] `Course_Trainer` assigned
- [ ] `Venue_Location` or `Select_Venue` populated
- [ ] All `Registration_Records` have `Status` = 'Confirmed'
- [ ] All attendees have `USI_Number`
- [ ] Compliance checks complete (`English_second_language` set)
- [ ] `Course_Days` subform populated for all registrations

#### After Course Delivery
- [ ] All `Course_Days.Attendance` marked
- [ ] `Trainer_Comments` completed
- [ ] `Result` set for all registrations
- [ ] `Course_Status` = 'Completed'
- [ ] `Certificate` status assigned to all registrations

#### Before Archiving
- [ ] All certificates processed
- [ ] `Course_Performance` record populated
- [ ] All paperwork in `Workdrive_URL`
- [ ] No open Team_Tasks for course
- [ ] Financial records complete (Invoices paid or outstanding)

---

## Workflow Dependency Diagram

### Linear Progression (Happy Path)

```
[Course Created] 
    ↓ (automatic workflows execute)
    │ - Udpate Course ID
    │ - Create Tasks for Course
    │ - Naming Convention
    │ - Create Workdrive Folder
    │ - Course Performance Record Init
    ↓
[User: Complete course setup]
    ↓
[Course Approved]
    ↓ (when Registrations_Confirmed ≥ Minimum_registrations)
    │ - Check Min registration
    │ - Sync to WordPress
    │ - Course Confirmed - Website Calendar
    ↓
[User: Prepare materials]
    ↓
[Coursework]
    ↓ (materials ready)
    │ - (Manual processes)
    ↓
[User: Arrange logistics]
    ↓
[Course Logistics]
    ↓ (logistics confirmed)
    │ - Send Trainer Email (manual trigger)
    │ - SMS to Trainer (10 days before)
    │ - SMS to Trainer (1 day before)
    │ - Trainer Info PDF (3 days before)
    │ - Send to Trainer Calendar (manual)
    ↓
[User: Enrol students]
    ↓
[Course Enrolment]
    ↓ (for each registration)
    │ - Populate Course Days
    │ - Calculate Registrations
    │ - Create Workdrive folder
    │ - Email/SMS confirmations
    │ - SMS Attendance Link
    ↓
[Pre-delivery reminders]
    ↓ (time-based)
    │ - 14 days: SMS confirmation request
    │ - 7 days: Email and SMS reminders
    │ - 1 day: Attendance PDF
    ↓
[Course Delivery]
    ↓ (during course)
    │ - Attendance tracking (manual)
    │ - Attendance PDF (on demand)
    ↓
[Post-delivery]
    ↓ (after course end)
    │ - Thank you SMS
    │ - Trainer Feedback request
    │ - Completed course WP update
    ↓
[User: Process certificates]
    ↓
[Certification]
    ↓ (certificates received)
    │ - Certificate Held Back (conditional)
    │ - Status updated to completed
    ↓
[User: Archive documentation]
    ↓
[Archiving]
    ↓ (Course_Status = Completed/Archived)
    │ - Course Performance (final metrics)
    ↓
[Workflow Complete]
```

### Parallel Workflow Streams

Some workflows run in parallel:

**Financial Stream** (Deals/Invoices):
- Runs alongside course workflow
- Links via `Related_Deal`, `Invoice` fields
- Workflows trigger on PO receipt, payment confirmation
- Feeds into Course_Performance at end

**Communication Stream** (SMS/Email):
- Time-based reminders independent of stage progression
- Based on `Course_Start_Time` and `Course_End_Time`
- Respects opt-out flags

**Compliance Stream** (Documentation):
- Workdrive folder creation on course/registration create
- Document uploads tracked separately
- Feeds into certification stage

---

## Integration Architecture

### System Integration Map

```
┌─────────────────────────────────────────────────────────┐
│                    ZOHO CRM CORE                         │
│                                                           │
│  ┌─────────┐   ┌──────────────────┐   ┌──────────────┐ │
│  │ Courses │◄─►│ Registration     │◄─►│   Contacts   │ │
│  │         │   │ Records          │   │              │ │
│  └────┬────┘   └────────┬─────────┘   └──────────────┘ │
│       │                 │                                │
│       │                 │                                │
│  ┌────▼─────────────────▼──────┐                        │
│  │      Team_Tasks              │                        │
│  │   (Operational Tasks)        │                        │
│  └──────────────────────────────┘                        │
│                                                           │
│  ┌──────────────┐    ┌─────────────┐   ┌─────────────┐ │
│  │    Deals     │◄──►│   Invoices  │◄─►│   Quotes    │ │
│  └──────────────┘    └─────────────┘   └─────────────┘ │
│                                                           │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Course_Performance (Analytics)           │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────┬────────────────────┬─────────────────┘
                   │                    │
    ┌──────────────▼──────┐  ┌─────────▼──────────┐
    │  Zoho Workdrive     │  │   WordPress        │
    │  (Documents)        │  │   (Public Site)    │
    └─────────────────────┘  └────────────────────┘
                   │                    │
    ┌──────────────▼──────┐  ┌─────────▼──────────┐
    │   Xero              │  │   ClickSend SMS    │
    │   (Accounting)      │  │   (Notifications)  │
    └─────────────────────┘  └────────────────────┘
```

### Data Flow Patterns

#### Pattern 1: Course Creation → Registration
```
Courses (create)
    ↓
[Workflows create]
    ├─→ Team_Tasks (preparation tasks)
    ├─→ Workdrive Folder (documents)
    └─→ Course_Performance (analytics init)
    ↓
Registration_Records (create per student)
    ↓
[Workflows update]
    ├─→ Courses.Registrations_Booked (count)
    ├─→ Workdrive Folder (per attendee)
    └─→ Team_Tasks (admin tasks)
```

#### Pattern 2: Payment Processing
```
Lead (website enquiry)
    ↓
Deal (sales opportunity)
    ↓
Quote (pricing)
    ↓
Invoice (billing)
    ↓
Registration_Record (enrolment)
    ↓ [links via fields]
    ├─→ Invoice (lookup)
    ├─→ Deal (lookup)
    └─→ Quote (lookup)
    ↓
[Status updates flow back]
    └─→ Deal.Stage (won/lost)
```

#### Pattern 3: Certification Distribution
```
Courses (completed)
    ↓
Registration_Records (all attendees)
    ↓ [for each]
    ├─→ Result = Competent/Not Yet Competent
    ├─→ Certificate = Received
    └─→ send_cert_email = true
        ↓
    [Workflow: Certificate Held Back]
        ├─→ Check Certificate_Held_Back_Reason
        ├─→ If clear: Send email with certificate
        └─→ If held: Send hold notification
```

### Workflow Naming Conventions

Zoho workflows follow patterns:
- **Action-based:** "Send [Type]", "Create [Record]", "Update [Field]"
- **Trigger-based:** "On [Event]", "When [Condition]"
- **Time-based:** "[N] days before/after [Event]"
- **Module-prefixed:** "[Module]_ZohoFlow_[Action]"

Examples:
- ✓ `Send Trainer Email` - Clear action
- ✓ `10 days before course SMS to Trainer` - Clear timing
- ✓ `Courses_ZohoFlow_CRM Course to Workdrive Folder` - Integration
- ✓ `Certificate Held Back` - Conditional action

### Field Naming Patterns

Understanding Zoho field naming helps navigation:

**System Fields:**
- Standard: `Name`, `Owner`, `Created_By`, `Created_Time`
- Audit: `Modified_By`, `Modified_Time`, `Last_Activity_Time`
- Control: `Record_Status__s`, `Locked__s`

**Custom Fields:**
- Descriptive: `Course_Start_Time`, `Trainer_Comments`
- Boolean triggers: `Send_Trainer_email`, `Update_Course`
- Lookup pattern: `[Related]_[Module]` (e.g., `Course_Trainer`)
- Auto-number: `Event_ID`, `Deal_Identifier`

**Extension Fields** (prefixed):
- `zohosign__` - ZohoSign integration
- `clicksendext__` - ClickSend SMS
- `sbhtc__` - Tax calculator extension
- `googlemapreports__` - Google Maps integration

### Reporting and Analytics

#### Course Performance Metrics

Access via **Course_Performance** module:
- One record per course (auto-created)
- Linked via `Course` (lookup → Courses)
- Auto-updated when `Course_Status` = 'Completed'
- Manual refresh: Set `Run_Scheduler` = true

**Key Reports:**
- Revenue per course
- Registration conversion rates
- Outstanding payments
- Lead source effectiveness
- Win/loss analysis

#### Custom Views Recommendations

**Courses Module:**
- Upcoming Courses (Start_Time > today, Status = Confirmed)
- Below Minimum (Registrations_Confirmed < Minimum_registrations)
- Awaiting Logistics (Status = Confirmed, logistics fields empty)
- Completed Pending Archive (Status = Completed, archived = false)

**Registration_Records Module:**
- Compliance Pending (USI_Number empty OR compliance checks incomplete)
- Payment Pending (Status = Pending Payment)
- Certificates Held (Certificate = Held Back)
- Attendance Issues (Course_Days.Attendance = Absent/Did Not Attend)

---

## Appendix: Quick Reference Tables

### Critical Field Cross-Reference

| Business Concept | Courses Module Field | Registration_Records Field | Related Module |
|-----------------|---------------------|---------------------------|----------------|
| Student Name | - | `Attendee` (lookup) | Contacts |
| Student ID | - | `USI_Number` | - |
| Course Name | `Name` | - | - |
| Course Code | `Course_Code` | `Course_Code` (copied) | - |
| Trainer | `Course_Trainer` (lookup) | `Trainer` (lookup) | Contacts |
| Venue | `Select_Venue` (lookup) | `Venue` (lookup) | Venues |
| Start Date/Time | `Course_Start_Time` | `Course_Date_and_Time` | - |
| End Date/Time | `Course_End_Time` | `Course_End_Date` | - |
| Registration Count | `Registrations_Booked` | - | - |
| Attendance | - | `Course_Days` (subform) | - |
| Certificate | `Certificate_Update` | `Certificate` | - |
| Payment | - | `Invoice` (lookup) | Invoices |
| Deal Reference | `Deal_ID` | `Deal` (lookup) | Deals |
| Compliance | - | `English_second_language`, etc. | - |
| Result | - | `Result` | - |

### Workflow Trigger Field Summary

| Field Name | Module | Trigger Type | Purpose |
|-----------|--------|-------------|---------|
| `Send_Trainer_email` | Courses | Boolean manual | Send logistics email |
| `Add_Trainer_Calendar` | Courses | Boolean manual | Add calendar event |
| `Send_Attendance_PDF_to_Trainer` | Courses | Boolean manual | Email attendance list |
| `Workflow_Actions` | Courses | Picklist manual | Multi-purpose trigger |
| `Update_Registration_Records` | Courses | Boolean manual | Sync to registrations |
| `Update_Course` | Courses | Boolean manual | Refresh course data |
| `Course_Confirmed` | Courses | Boolean | Publish to website |
| `send_cert_email` | Registration_Records | Boolean manual | Distribute certificate |
| `Send_Email_to_Coordinator` | Courses | Boolean manual | Notify coordinator |
| `Update` | Registration_Records | Boolean manual | Update course details |
| `Create_Team_Task` | Registration_Records | Boolean manual | Generate admin task |
| `SMS_Confirmation` | Registration_Records | Picklist | Attendance response |

### Module Relationship Summary

```
Leads
  └─[converts to]─→ Contacts + Accounts + Deals

Deals
  └─[related to]─→ Courses (via Courseaa field)
  └─[creates]────→ Quotes
  └─[creates]────→ Invoices

Courses
  ├─[has many]───→ Registration_Records
  ├─[has many]───→ Team_Tasks
  ├─[links to]───→ Course_Qualification (Products)
  ├─[links to]───→ Course_Trainer (Contacts)
  ├─[links to]───→ Select_Venue (Venues)
  ├─[links to]───→ Private_Course_Client (Accounts)
  └─[has one]────→ Course_Performance

Registration_Records
  ├─[belongs to]─→ Course (Courses)
  ├─[links to]───→ Attendee (Contacts)
  ├─[links to]───→ Trainer (Contacts)
  ├─[links to]───→ Deal (Deals)
  ├─[links to]───→ Invoice (Invoices)
  ├─[links to]───→ Quote (Quotes)
  └─[has many]───→ Course_Days (subform)

Venues
  └─[referenced by]─→ Courses.Select_Venue
  └─[has]───────────→ Venue_Contact (Contacts)
```

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-13 | System | Initial creation from Zoho CRM export |

---

## Related Documentation

- `modules/overview/data/lucid-workflow.json` - Original Lucid Chart workflow structure
- `modules/overview/data/lucid-workflow-enhanced.json` - This mapping in JSON format
- `data/exports/zoho-dependencies-2025-11-13.json` - Complete workflow dependency export
- `data/exports/zoho-data-model-2025-11-13.json` - Full field definitions
- `data/exports/Zoho_CRM_Data_Model_2025-11-13.xlsx` - Excel data model

---

**Document End**




