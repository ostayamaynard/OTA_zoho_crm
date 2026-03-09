# Workflow Dependency Map

**Generated:** 2026-01-08 16:20:23
**Source Export:** 2026-01-08
**Purpose:** Impact analysis for workflow and field changes

---

## Executive Summary {#summary}

| Metric | Count |
|--------|-------|
| Total Workflows | 182 |
| Modules with Workflows | 15 |
| HIGH Risk Workflows | 0 |
| MEDIUM Risk Workflows | 0 |
| LOW Risk Workflows | 182 |

**Risk Levels:**
- **HIGH**: Cross-module actions or complex field dependencies (3+ fields)
- **MEDIUM**: Triggers with field dependencies or create/update workflows
- **LOW**: Simple workflows with minimal dependencies

---

## Table of Contents {#toc}

- [Courses (37 workflows)](#module-courses)
- [Registration_Records (37 workflows)](#module-registration_records)
- [Deals (25 workflows)](#module-deals)
- [Leads (24 workflows)](#module-leads)
- [Invoices (17 workflows)](#module-invoices)
- [Contacts (12 workflows)](#module-contacts)
- [Quotes (9 workflows)](#module-quotes)
- [twiliosmsextension0__Sent_SMS (8 workflows)](#module-twiliosmsextension0__sent_sms)
- [Accounts (4 workflows)](#module-accounts)
- [Team_Tasks (3 workflows)](#module-team_tasks)
- [Projects_Inhouse (2 workflows)](#module-projects_inhouse)
- [Events (1 workflows)](#module-events)
- [Calls (1 workflows)](#module-calls)
- [Sales_Orders (1 workflows)](#module-sales_orders)
- [twiliosmsextension0__Twilio_From_Numbers (1 workflows)](#module-twiliosmsextension0__twilio_from_numbers)

---

## Courses {#module-courses}

**Total Workflows:** 37
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 37

**Outbound Lookups:**
- Course Trainer → Contacts
- Course Qualification → Products
- Select Venue → Venues
- Venue Contact → Contacts
- Training Coordinator → Contacts
- *+1 more*

---

### 🟢 Update course from product {#courses-52330000003995088}

| Property | Value |
|----------|-------|
| **ID** | `52330000003995088` |
| **Status** | ✅ Active |
| **Trigger** | Edit |
| **Risk Level** | LOW |

**Trigger:** edit

**Impact Analysis:**
- **If disabled:** edit triggers won't fire

---

### 🟢 Update Registration records {#courses-52330000003999102}

| Property | Value |
|----------|-------|
| **ID** | `52330000003999102` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Registration Course Days {#courses-52330000002460179}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460179` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Udpate Course ID {#courses-52330000002444506}

| Property | Value |
|----------|-------|
| **ID** | `52330000002444506` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Courses records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Trainer Task - to upload Course material {#courses-52330000002656953}

| Property | Value |
|----------|-------|
| **ID** | `52330000002656953` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Trainer Info PDF {#courses-52330000010838346}

| Property | Value |
|----------|-------|
| **ID** | `52330000010838346` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Trainer Feedback Email {#courses-52330000002656789}

| Property | Value |
|----------|-------|
| **ID** | `52330000002656789` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Sync Course to Wordpress {#courses-52330000002460212}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460212` |
| **Status** | ❌ Inactive |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Sync Course to Wordpress {#courses-52330000006315389}

| Property | Value |
|----------|-------|
| **ID** | `52330000006315389` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Status updated to completed {#courses-52330000004037507}

| Property | Value |
|----------|-------|
| **ID** | `52330000004037507` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Send to Trainer Calendar {#courses-52330000011998008}

| Property | Value |
|----------|-------|
| **ID** | `52330000011998008` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Send attendance to Trainer {#courses-52330000004815267}

| Property | Value |
|----------|-------|
| **ID** | `52330000004815267` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Send Trainer Email {#courses-52330000002570460}

| Property | Value |
|----------|-------|
| **ID** | `52330000002570460` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Send Attendance App email 11 days prior to start {#courses-52330000002569380}

| Property | Value |
|----------|-------|
| **ID** | `52330000002569380` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Private course Status Updates {#courses-52330000004318762}

| Property | Value |
|----------|-------|
| **ID** | `52330000004318762` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Private Course Status changed {#courses-52330000005069426}

| Property | Value |
|----------|-------|
| **ID** | `52330000005069426` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Private Course Client Selected {#courses-52330000010760918}

| Property | Value |
|----------|-------|
| **ID** | `52330000010760918` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Notification for Course Archive or Cancel {#courses-52330000011362374}

| Property | Value |
|----------|-------|
| **ID** | `52330000011362374` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Naming Convention - Course {#courses-52330000004013116}

| Property | Value |
|----------|-------|
| **ID** | `52330000004013116` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Manual Trigger for Attendance PDF {#courses-52330000004569126}

| Property | Value |
|----------|-------|
| **ID** | `52330000004569126` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Email to Training Coordinator from Courses {#courses-52330000002582583}

| Property | Value |
|----------|-------|
| **ID** | `52330000002582583` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Create Tasks for Course {#courses-52330000002661635}

| Property | Value |
|----------|-------|
| **ID** | `52330000002661635` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Courses records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Create Meetings for Trainer on EDIT {#courses-52330000003664428}

| Property | Value |
|----------|-------|
| **ID** | `52330000003664428` |
| **Status** | ❌ Inactive |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Create Meetings for Trainer {#courses-52330000003561188}

| Property | Value |
|----------|-------|
| **ID** | `52330000003561188` |
| **Status** | ❌ Inactive |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Courses_ZohoFlow_CRM Course to Workdrive Folder {#courses-52330000002462001}

| Property | Value |
|----------|-------|
| **ID** | `52330000002462001` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Courses records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Course Qualification lookup Edited {#courses-52330000002638166}

| Property | Value |
|----------|-------|
| **ID** | `52330000002638166` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Course Performance Record {#courses-52330000008928362}

| Property | Value |
|----------|-------|
| **ID** | `52330000008928362` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Courses records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Course Performance {#courses-52330000008928375}

| Property | Value |
|----------|-------|
| **ID** | `52330000008928375` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Course Confirmed - Website Calendar {#courses-52330000011998036}

| Property | Value |
|----------|-------|
| **ID** | `52330000011998036` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Copy of Check MAX registration {#courses-52330000003463443}

| Property | Value |
|----------|-------|
| **ID** | `52330000003463443` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Completed course for WP. course Start Date {#courses-52330000004065214}

| Property | Value |
|----------|-------|
| **ID** | `52330000004065214` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Check for Registration Booked Lower than Minimum Registrations {#courses-52330000002569868}

| Property | Value |
|----------|-------|
| **ID** | `52330000002569868` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Check Min registration {#courses-52330000003463406}

| Property | Value |
|----------|-------|
| **ID** | `52330000003463406` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Cancelled Course WF {#courses-52330000003995688}

| Property | Value |
|----------|-------|
| **ID** | `52330000003995688` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 10 days before course SMS to Trainer {#courses-52330000002656676}

| Property | Value |
|----------|-------|
| **ID** | `52330000002656676` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 1 day before course SMS to Trainer {#courses-52330000002656692}

| Property | Value |
|----------|-------|
| **ID** | `52330000002656692` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 1 Day prior Attendance PDF {#courses-52330000012545268}

| Property | Value |
|----------|-------|
| **ID** | `52330000012545268` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

## Registration_Records {#module-registration-records}

**Total Workflows:** 37
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 37

**Outbound Lookups:**
- Course → Courses
- Related Deal → Deals
- Account Name → Accounts
- Venue → Venues
- Trainer → Contacts
- *+4 more*

---

### 🟢 status update {#registration-records-52330000004045787}

| Property | Value |
|----------|-------|
| **ID** | `52330000004045787` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Waitlist Record {#registration-records-52330000007034348}

| Property | Value |
|----------|-------|
| **ID** | `52330000007034348` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Update course details {#registration-records-52330000003014626}

| Property | Value |
|----------|-------|
| **ID** | `52330000003014626` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Name on Course Change {#registration-records-52330000009066119}

| Property | Value |
|----------|-------|
| **ID** | `52330000009066119` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Course Attended 1 week from course date {#registration-records-52330000003014483}

| Property | Value |
|----------|-------|
| **ID** | `52330000003014483` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Update Course Attended 1 Day from course {#registration-records-52330000003014499}

| Property | Value |
|----------|-------|
| **ID** | `52330000003014499` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Update Attendee for Payment Update with DEAL {#registration-records-52330000004335393}

| Property | Value |
|----------|-------|
| **ID** | `52330000004335393` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Trainer Edited {#registration-records-52330000004112123}

| Property | Value |
|----------|-------|
| **ID** | `52330000004112123` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Thank you SMS {#registration-records-52330000002656733}

| Property | Value |
|----------|-------|
| **ID** | `52330000002656733` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Set Opt-Outs to False {#registration-records-52330000007826269}

| Property | Value |
|----------|-------|
| **ID** | `52330000007826269` |
| **Status** | ❌ Inactive |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Send payment link {#registration-records-52330000003024548}

| Property | Value |
|----------|-------|
| **ID** | `52330000003024548` |
| **Status** | ❌ Inactive |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 SMS Attendance Link {#registration-records-52330000005789634}

| Property | Value |
|----------|-------|
| **ID** | `52330000005789634` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 SMS - Attendance Acknowledgement {#registration-records-52330000006676878}

| Property | Value |
|----------|-------|
| **ID** | `52330000006676878` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Registration_Records_ZohoFlow_Copy of CRM Contact {#registration-records-52330000005138075}

| Property | Value |
|----------|-------|
| **ID** | `52330000005138075` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Registration Cancelled {#registration-records-52330000009966152}

| Property | Value |
|----------|-------|
| **ID** | `52330000009966152` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Private course Tentative - Attendee Spot Booked {#registration-records-52330000005163175}

| Property | Value |
|----------|-------|
| **ID** | `52330000005163175` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Private Course Confirmed - Attendee Spot Booked {#registration-records-52330000005163264}

| Property | Value |
|----------|-------|
| **ID** | `52330000005163264` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Private Attendee - Spot Tentative {#registration-records-52330000005163090}

| Property | Value |
|----------|-------|
| **ID** | `52330000005163090` |
| **Status** | ❌ Inactive |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Populate Course Days {#registration-records-52330000002460165}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460165` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Payment Confirmation {#registration-records-52330000013645165}

| Property | Value |
|----------|-------|
| **ID** | `52330000013645165` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Move Course Attendee Folder on Course Change {#registration-records-52330000005375288}

| Property | Value |
|----------|-------|
| **ID** | `52330000005375288` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 IF paid via credcard {#registration-records-52330000004534986}

| Property | Value |
|----------|-------|
| **ID** | `52330000004534986` |
| **Status** | ❌ Inactive |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Generate SMS Shorten Link {#registration-records-52330000005789649}

| Property | Value |
|----------|-------|
| **ID** | `52330000005789649` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Generate SMS Link 15 days prior if Empty {#registration-records-52330000005789664}

| Property | Value |
|----------|-------|
| **ID** | `52330000005789664` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Feedback Email from attendee {#registration-records-52330000002633996}

| Property | Value |
|----------|-------|
| **ID** | `52330000002633996` |
| **Status** | ❌ Inactive |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Email - Attendee paid via credit card {#registration-records-52330000002582386}

| Property | Value |
|----------|-------|
| **ID** | `52330000002582386` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Email - Attendee Payment made for Invoice {#registration-records-52330000005157463}

| Property | Value |
|----------|-------|
| **ID** | `52330000005157463` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Email - Attendee Created - Public - Pay via Invoice {#registration-records-52330000005157446}

| Property | Value |
|----------|-------|
| **ID** | `52330000005157446` |
| **Status** | ❌ Inactive |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Create Team Task {#registration-records-52330000003121331}

| Property | Value |
|----------|-------|
| **ID** | `52330000003121331` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Certificate Held Back {#registration-records-52330000002667069}

| Property | Value |
|----------|-------|
| **ID** | `52330000002667069` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Calculate Registrations and create team task {#registration-records-52330000002518044}

| Property | Value |
|----------|-------|
| **ID** | `52330000002518044` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Registration_Records records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Calculate Registrations {#registration-records-52330000002518060}

| Property | Value |
|----------|-------|
| **ID** | `52330000002518060` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 7 Days before Public course SMS Reminder {#registration-records-52330000002597951}

| Property | Value |
|----------|-------|
| **ID** | `52330000002597951` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 7 Days before Private Confirmed course SMS Reminder {#registration-records-52330000005163433}

| Property | Value |
|----------|-------|
| **ID** | `52330000005163433` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 14 days SMS Before Attendance Confirmation {#registration-records-52330000005789721}

| Property | Value |
|----------|-------|
| **ID** | `52330000005789721` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 1 week prior to Public course {#registration-records-52330000002582766}

| Property | Value |
|----------|-------|
| **ID** | `52330000002582766` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 1 week prior to Private Confirmed course {#registration-records-52330000005163385}

| Property | Value |
|----------|-------|
| **ID** | `52330000005163385` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

## Deals {#module-deals}

**Total Workflows:** 25
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 25

**Outbound Lookups:**
- Account Name → Accounts
- Contact Name → Contacts
- Parent Account → Accounts
- Product → Products
- Course → Courses
- *+2 more*

---

### 🟢 copy converted lead messages to deal {#deals-52330000013919513}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919513` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Deals records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Workflow - Update Deal ID {#deals-52330000004452015}

| Property | Value |
|----------|-------|
| **ID** | `52330000004452015` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 When Account name is not blank {#deals-52330000005069264}

| Property | Value |
|----------|-------|
| **ID** | `52330000005069264` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update dealopt out status when manually changed {#deals-52330000013919832}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919832` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Registration records when PO Is received {#deals-52330000006993545}

| Property | Value |
|----------|-------|
| **ID** | `52330000006993545` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Deal stage when 1 attendee, qualification and public {#deals-52330000004434048}

| Property | Value |
|----------|-------|
| **ID** | `52330000004434048` |
| **Status** | ❌ Inactive |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Update Deal ID {#deals-52330000002444572}

| Property | Value |
|----------|-------|
| **ID** | `52330000002444572` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Deals records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Update Amount on create {#deals-52330000003995130}

| Property | Value |
|----------|-------|
| **ID** | `52330000003995130` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Transfer messages from converted lead to a deal {#deals-52330000013919583}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919583` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Sync Deal to backend {#deals-52330000013919697}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919697` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Deals records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Purchase Order Received {#deals-52330000002460283}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460283` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 On stage Update related Attendees {#deals-52330000004335567}

| Property | Value |
|----------|-------|
| **ID** | `52330000004335567` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 If Website Account Name {#deals-52330000005157945}

| Property | Value |
|----------|-------|
| **ID** | `52330000005157945` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Deals records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Follow up on Purchase Order 5 days before course {#deals-52330000009085891}

| Property | Value |
|----------|-------|
| **ID** | `52330000009085891` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Follow up on Purchase Order 28 days before {#deals-52330000002638311}

| Property | Value |
|----------|-------|
| **ID** | `52330000002638311` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Follow up on Purchase Order 14 days before course {#deals-52330000002638269}

| Property | Value |
|----------|-------|
| **ID** | `52330000002638269` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Follow up on Purchase Order 1 days before {#deals-52330000002638411}

| Property | Value |
|----------|-------|
| **ID** | `52330000002638411` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Follow up future deals {#deals-52330000001178038}

| Property | Value |
|----------|-------|
| **ID** | `52330000001178038` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Email to training Coordinator from DEALS {#deals-52330000002967852}

| Property | Value |
|----------|-------|
| **ID** | `52330000002967852` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Deal Naming Convention {#deals-52330000002967279}

| Property | Value |
|----------|-------|
| **ID** | `52330000002967279` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Deals records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Create Team Task from Deals {#deals-52330000002460147}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460147` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Create Quote - Stage Update Ready to quote {#deals-52330000002460308}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460308` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Course Change {#deals-52330000013445263}

| Property | Value |
|----------|-------|
| **ID** | `52330000013445263` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Copy of Deal Naming Convention {#deals-52330000004013962}

| Property | Value |
|----------|-------|
| **ID** | `52330000004013962` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Close conversation if deal deleted {#deals-52330000013919745}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919745` |
| **Status** | ✅ Active |
| **Trigger** | Delete |
| **Risk Level** | LOW |

**Trigger:** delete

**Impact Analysis:**
- **If disabled:** delete triggers won't fire

---

## Leads {#module-leads}

**Total Workflows:** 24
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 24

**Outbound Lookups:**
- Converted Account → Accounts
- Converted Contact → Contacts
- Converted Deal → Deals
- Course → Courses
- Existing Company Record → Accounts

---

### 🟢 updateLeadAddressAndRemoveMapFileds {#leads-52330000010756411}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756411` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 setLeadGMapFiledsAsEmpty {#leads-52330000010756363}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756363` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Update Location URL {#leads-52330000008158816}

| Property | Value |
|----------|-------|
| **ID** | `52330000008158816` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Address {#leads-52330000005569800}

| Property | Value |
|----------|-------|
| **ID** | `52330000005569800` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Tag G-Series Leadership Leads {#leads-52330000007732209}

| Property | Value |
|----------|-------|
| **ID** | `52330000007732209` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Leads records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 TEST SMS {#leads-52330000008493195}

| Property | Value |
|----------|-------|
| **ID** | `52330000008493195` |
| **Status** | ❌ Inactive |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Sync lead to backend when phone changes {#leads-52330000013919761}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919761` |
| **Status** | ❌ Inactive |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Sync Lead to backend on create {#leads-52330000013919665}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919665` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Leads records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Send Course email {#leads-52330000006093561}

| Property | Value |
|----------|-------|
| **ID** | `52330000006093561` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Reactivate Lost Lead from Brochure Download {#leads-52330000013574105}

| Property | Value |
|----------|-------|
| **ID** | `52330000013574105` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 New Lead Notification {#leads-52330000000427010}

| Property | Value |
|----------|-------|
| **ID** | `52330000000427010` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Leads records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 LeadUpdate opt out on server after Manual opt out {#leads-52330000013919848}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919848` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Lead Owner Assignment {#leads-52330000007257288}

| Property | Value |
|----------|-------|
| **ID** | `52330000007257288` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Leads records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Generate Payment URL {#leads-52330000008228472}

| Property | Value |
|----------|-------|
| **ID** | `52330000008228472` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Format Number on Edit {#leads-52330000005817040}

| Property | Value |
|----------|-------|
| **ID** | `52330000005817040` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Format Number {#leads-52330000005789994}

| Property | Value |
|----------|-------|
| **ID** | `52330000005789994` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Leads records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Create Team task in leads {#leads-52330000002758376}

| Property | Value |
|----------|-------|
| **ID** | `52330000002758376` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Course Details Udpated {#leads-52330000005569771}

| Property | Value |
|----------|-------|
| **ID** | `52330000005569771` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Convert to Only Create a contact {#leads-52330000008405346}

| Property | Value |
|----------|-------|
| **ID** | `52330000008405346` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Convert on Payment Success {#leads-52330000008292523}

| Property | Value |
|----------|-------|
| **ID** | `52330000008292523` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Convert Pay Via Invoice {#leads-52330000008920352}

| Property | Value |
|----------|-------|
| **ID** | `52330000008920352` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Convert Non Paying Lead {#leads-52330000008250081}

| Property | Value |
|----------|-------|
| **ID** | `52330000008250081` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Close conversation if lead deleted {#leads-52330000013919713}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919713` |
| **Status** | ✅ Active |
| **Trigger** | Delete |
| **Risk Level** | LOW |

**Trigger:** delete

**Impact Analysis:**
- **If disabled:** delete triggers won't fire

---

### 🟢 CallWithIn24Hours and Team Task {#leads-52330000000864146}

| Property | Value |
|----------|-------|
| **ID** | `52330000000864146` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Leads records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

## Invoices {#module-invoices}

**Total Workflows:** 17
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 17

**Outbound Lookups:**
- Account Name → Accounts
- Contact Name → Contacts
- Deal Name → Deals
- Parent Account → Accounts
- Account Contact → Contacts
- *+1 more*

---

### 🟢 When Po is received {#invoices-52330000005069778}

| Property | Value |
|----------|-------|
| **ID** | `52330000005069778` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update URL {#invoices-52330000008519048}

| Property | Value |
|----------|-------|
| **ID** | `52330000008519048` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Due Date {#invoices-52330000005069739}

| Property | Value |
|----------|-------|
| **ID** | `52330000005069739` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Invoices records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Update Amount in Deal when Inv is paid {#invoices-52330000009085784}

| Property | Value |
|----------|-------|
| **ID** | `52330000009085784` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update All Fields {#invoices-52330000008512961}

| Property | Value |
|----------|-------|
| **ID** | `52330000008512961` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Invoices records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Send on create - Awaiting Payment {#invoices-52330000008694463}

| Property | Value |
|----------|-------|
| **ID** | `52330000008694463` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Invoices records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Send Invoice {#invoices-52330000004534311}

| Property | Value |
|----------|-------|
| **ID** | `52330000004534311` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Refresh Payment URL {#invoices-52330000008776519}

| Property | Value |
|----------|-------|
| **ID** | `52330000008776519` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Push to XERO on Create when PAID {#invoices-52330000005517247}

| Property | Value |
|----------|-------|
| **ID** | `52330000005517247` |
| **Status** | ❌ Inactive |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Push Invoice to Xero {#invoices-52330000002460231}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460231` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Paid in Crez {#invoices-52330000002460196}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460196` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 New - Update deal and Reg record {#invoices-52330000004251591}

| Property | Value |
|----------|-------|
| **ID** | `52330000004251591` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Invoice Udpate {#invoices-52330000002610986}

| Property | Value |
|----------|-------|
| **ID** | `52330000002610986` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Invoice Reminder {#invoices-52330000013638031}

| Property | Value |
|----------|-------|
| **ID** | `52330000013638031` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Invoices records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Inhouse - Calculate Overall Tax for Invoice {#invoices-52330000004975124}

| Property | Value |
|----------|-------|
| **ID** | `52330000004975124` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Checkbox Sync to XERO {#invoices-52330000014037247}

| Property | Value |
|----------|-------|
| **ID** | `52330000014037247` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Calculate Overall Tax for Invoice {#invoices-52330000002375206}

| Property | Value |
|----------|-------|
| **ID** | `52330000002375206` |
| **Status** | ❌ Inactive |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

## Contacts {#module-contacts}

**Total Workflows:** 12
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 12

**Outbound Lookups:**
- Account Name → Accounts

---

### 🟢 updateContactAddressAndRemoveMapFileds {#contacts-52330000010756331}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756331` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 transfer messages from converted lead to contact {#contacts-52330000013919474}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919474` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 setContactsGMapFiledsAsEmpty {#contacts-52330000010756379}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756379` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 find_messages_for_new_contact {#contacts-52330000013919458}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919458` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Contacts records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Update contactopt out status when manually changed {#contacts-52330000013919816}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919816` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Sync Contact to backend {#contacts-52330000013919681}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919681` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Contacts records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Push Contact Updates to Xero {#contacts-52330000002460248}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460248` |
| **Status** | ✅ Active |
| **Trigger** | Edit |
| **Risk Level** | LOW |

**Trigger:** edit

**Impact Analysis:**
- **If disabled:** edit triggers won't fire

---

### 🟢 On Edit - Format Phone field {#contacts-52330000005817052}

| Property | Value |
|----------|-------|
| **ID** | `52330000005817052` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Format Phone field {#contacts-52330000005817024}

| Property | Value |
|----------|-------|
| **ID** | `52330000005817024` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Contacts records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Create task in contacts {#contacts-52330000002758242}

| Property | Value |
|----------|-------|
| **ID** | `52330000002758242` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Contacts_ZohoFlow_CRM Contact to Workdrive Folder {#contacts-52330000002820175}

| Property | Value |
|----------|-------|
| **ID** | `52330000002820175` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Contacts records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Close conversation if contact deleted {#contacts-52330000013919729}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919729` |
| **Status** | ✅ Active |
| **Trigger** | Delete |
| **Risk Level** | LOW |

**Trigger:** delete

**Impact Analysis:**
- **If disabled:** delete triggers won't fire

---

## Quotes {#module-quotes}

**Total Workflows:** 9
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 9

**Outbound Lookups:**
- Deal Name → Deals
- Contact Name → Contacts
- Account Name → Accounts
- Parent Account → Accounts
- Account Contact → Contacts
- *+2 more*

---

### 🟢 Update quote when quote is sent or won {#quotes-52330000003995201}

| Property | Value |
|----------|-------|
| **ID** | `52330000003995201` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Quote Naming convention {#quotes-52330000002856364}

| Property | Value |
|----------|-------|
| **ID** | `52330000002856364` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Update Quote Details {#quotes-52330000002597194}

| Property | Value |
|----------|-------|
| **ID** | `52330000002597194` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Quotes records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Update Deal with PO Number and Date {#quotes-52330000006993468}

| Property | Value |
|----------|-------|
| **ID** | `52330000006993468` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Update Deal and Invoice on Quote Closed Won {#quotes-52330000002460325}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460325` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Send Quote {#quotes-52330000006984913}

| Property | Value |
|----------|-------|
| **ID** | `52330000006984913` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Qoutes status update {#quotes-52330000013638051}

| Property | Value |
|----------|-------|
| **ID** | `52330000013638051` |
| **Status** | ❌ Inactive |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Inhouse - Calculate Overall Tax for Quote {#quotes-52330000004975235}

| Property | Value |
|----------|-------|
| **ID** | `52330000004975235` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Calculate Overall Tax for Quote {#quotes-52330000002375246}

| Property | Value |
|----------|-------|
| **ID** | `52330000002375246` |
| **Status** | ❌ Inactive |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

## twiliosmsextension0__Sent_SMS {#module-twiliosmsextension0--sent-sms}

**Total Workflows:** 8
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 8

**Outbound Lookups:**
- LeadName → Leads
- ContactName → Contacts
- DealName → Deals
- Campaign → Campaigns

---

### 🟢 Update reply stats {#twiliosmsextension0--sent-sms-52330000013919793}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919793` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Try sending auto SMS again if it didn't go out-mod {#twiliosmsextension0--sent-sms-52330000013919625}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919625` |
| **Status** | ✅ Active |
| **Trigger** | Edit |
| **Risk Level** | LOW |

**Trigger:** edit

**Impact Analysis:**
- **If disabled:** edit triggers won't fire

---

### 🟢 Try sending auto SMS again if it didn't go out {#twiliosmsextension0--sent-sms-52330000013919537}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919537` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Trigger scheduled message {#twiliosmsextension0--sent-sms-52330000013919602}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919602` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Sync sent messages to backend {#twiliosmsextension0--sent-sms-52330000013919645}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919645` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

### 🟢 Send message triggered by workflow {#twiliosmsextension0--sent-sms-52330000013919493}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919493` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New twiliosmsextension0__Sent_SMS records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

### 🟢 Retry sending if headers not authorised {#twiliosmsextension0--sent-sms-52330000013919864}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919864` |
| **Status** | ❌ Inactive |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **Currently Inactive** - No immediate impact from changes

---

### 🟢 Report error if To/From are not set {#twiliosmsextension0--sent-sms-52330000013919560}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919560` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

## Accounts {#module-accounts}

**Total Workflows:** 4
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 4

**Outbound Lookups:**
- Parent Account → Accounts
- Primary Contact → Contacts
- Last Course → Courses
- Account Contact → Contacts
- Account Payable → Contacts
- *+1 more*

---

### 🟢 updateAccountsAddressAndRemoveMapFileds	 {#accounts-52330000010756347}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756347` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 setAccountsGMapFiledsAsEmpty {#accounts-52330000010756395}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756395` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

### 🟢 Send Update Your Details {#accounts-52330000005584202}

| Property | Value |
|----------|-------|
| **ID** | `52330000005584202` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Push Account Updates to Xero {#accounts-52330000002460265}

| Property | Value |
|----------|-------|
| **ID** | `52330000002460265` |
| **Status** | ✅ Active |
| **Trigger** | Edit |
| **Risk Level** | LOW |

**Trigger:** edit

**Impact Analysis:**
- **If disabled:** edit triggers won't fire

---

## Team_Tasks {#module-team-tasks}

**Total Workflows:** 3
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 3

**Outbound Lookups:**
- Course → Courses
- Course Attendee → Registration_Records
- Deal → Deals
- Invoice → Invoices
- Quote → Quotes
- *+4 more*

---

### 🟢 Assign Related To Fields on Update {#team-tasks-52330000006206296}

| Property | Value |
|----------|-------|
| **ID** | `52330000006206296` |
| **Status** | ✅ Active |
| **Trigger** | Section Update |
| **Risk Level** | LOW |

**Trigger:** section_update

**Impact Analysis:**
- **If disabled:** section_update triggers won't fire

---

### 🟢 Assign Related To Fields on Update {#team-tasks-52330000006206312}

| Property | Value |
|----------|-------|
| **ID** | `52330000006206312` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Assign Related To Fields on Create {#team-tasks-52330000006206281}

| Property | Value |
|----------|-------|
| **ID** | `52330000006206281` |
| **Status** | ✅ Active |
| **Trigger** | Create |
| **Risk Level** | LOW |

**Trigger:** Fires when a new record is created

**Impact Analysis:**
- **If disabled:** New Team_Tasks records won't trigger this automation
- **If trigger modified:** N/A (always fires on create)

---

## Projects_Inhouse {#module-projects-inhouse}

**Total Workflows:** 2
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 2

---

### 🟢 New Task to be created {#projects-inhouse-52330000005367166}

| Property | Value |
|----------|-------|
| **ID** | `52330000005367166` |
| **Status** | ✅ Active |
| **Trigger** | Field Update |
| **Risk Level** | LOW |

**Trigger:** Fires on any field update

**Impact Analysis:**
- **If disabled:** Field updates won't trigger this automation

---

### 🟢 Create Project Folder in Workdrive {#projects-inhouse-52330000005353218}

| Property | Value |
|----------|-------|
| **ID** | `52330000005353218` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

## Events {#module-events}

**Total Workflows:** 1
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 1

**Outbound Lookups:**
- Contact Name → Contacts
- Related To → se_module

---

### 🟢 updateLastVisitedDate {#events-52330000010756312}

| Property | Value |
|----------|-------|
| **ID** | `52330000010756312` |
| **Status** | ✅ Active |
| **Trigger** | Date Or Datetime |
| **Risk Level** | LOW |

**Trigger:** Time-based (scheduled)

**Impact Analysis:**
- **If disabled:** date_or_datetime triggers won't fire

---

## Calls {#module-calls}

**Total Workflows:** 1
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 1

**Outbound Lookups:**
- Contact Name → Contacts
- Related To → se_module

---

### 🟢 CallLogs {#calls-52330000000464146}

| Property | Value |
|----------|-------|
| **ID** | `52330000000464146` |
| **Status** | ✅ Active |
| **Trigger** | Outgoing Call Createedit |
| **Risk Level** | LOW |

**Trigger:** outgoing_call_createedit

**Impact Analysis:**
- **If disabled:** outgoing_call_createedit triggers won't fire

---

## Sales_Orders {#module-sales-orders}

**Total Workflows:** 1
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 1

**Outbound Lookups:**
- Deal Name → Deals
- Quote Name → Quotes
- Contact Name → Contacts
- Account Name → Accounts

---

### 🟢 Calculate Overall Tax for Sales Order {#sales-orders-52330000002375226}

| Property | Value |
|----------|-------|
| **ID** | `52330000002375226` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

## twiliosmsextension0__Twilio_From_Numbers {#module-twiliosmsextension0--twilio-from-numbers}

**Total Workflows:** 1
**Risk Distribution:** HIGH: 0, MEDIUM: 0, LOW: 1

---

### 🟢 Sync from numbers on add or edit {#twiliosmsextension0--twilio-from-numbers-52330000013919777}

| Property | Value |
|----------|-------|
| **ID** | `52330000013919777` |
| **Status** | ✅ Active |
| **Trigger** | Create Or Edit |
| **Risk Level** | LOW |

**Trigger:** create_or_edit

**Impact Analysis:**
- **If disabled:** create_or_edit triggers won't fire

---

## Related Documentation {#related-docs}

- **SYSTEM_OVERVIEW.md** - Module catalogue and relationship summary
- **FIELD_REFERENCE.md** - Detailed field specifications
- **CHANGE_PLANNING_GUIDE.md** - Pre-change checklists and best practices
- **LATEST_CHANGES.md** - Recent workflow modifications

---

*Generated by `tools/generate_ai_kb.py` on 2026-01-08*
