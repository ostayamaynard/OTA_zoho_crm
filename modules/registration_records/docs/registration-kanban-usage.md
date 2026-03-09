# Registration Records Module - Kanban Board Usage Guide

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

This guide documents the complete Kanban board workflow for the **Registration_Records** module (Course Attendees) in Zoho CRM. This module manages individual student enrolments from initial booking through course completion and certification.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Stages | 10 |
| Total Workflows | 36 |
| Automatic Workflows | 33 |
| Manual Trigger Workflows | 3 |
| Time-Based Workflows | 10 |

---

## Stage-by-Stage Breakdown

### Stage 1: Spot Tentative ⏳

**Color:** `#FFF3E0` (Light Orange)
**Workflow Count:** 6
**Typical Duration:** 1-7 days

#### What Happens Automatically

When a registration record is created:

| Workflow | Action | Creates |
|----------|--------|---------|
| [Populate Course Days](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460165) | Creates attendance subform entries | - |
| [Calculate Registrations and create team task](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518044) | Updates course counts, creates task | Team_Task |
| [Workdrive Folder Creation](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005138075) | Creates document folder | - |
| [Generate SMS Shorten Link](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789649) | Creates attendance SMS link | - |
| [Private Attendee - Spot Tentative](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163090) | Confirms private booking | - |
| [Set Opt-Outs to False](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007826269) | Resets opt-out preferences | - |

#### Human Actions Required

- [ ] Verify attendee details (`Attendee`, `Account_Name`)
- [ ] Link to deal (`Related_Deal`)
- [ ] Set `Send_payment_link` = true to email payment URL

#### Exit Criteria

- **→ Spot Booked:** Payment received or PO confirmed
- **→ Waiting List:** Course full
- **→ Cancelled:** Booking cancelled

---

### Stage 2: Spot Booked ✅

**Color:** `#E8F5E9` (Light Green)
**Workflow Count:** 14+ (most active stage)
**Typical Duration:** 1-14 days (until course)

#### Payment Confirmation Workflows

| Workflow | Condition | Action |
|----------|-----------|--------|
| [Email - Credit Card Payment](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002582386) | Credit card | Sends confirmation |
| [Email - Invoice Payment](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005157463) | Invoice payment | Sends confirmation |
| [IF paid via credcard](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004534986) | Credit card | Processes payment |
| [Calculate Registrations](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518060) | Status change | Updates course count |
| [SMS Attendance Link](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789634) | Spot Booked | Sends app link |
| [Update with DEAL](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004335393) | Payment | Links to deal |

#### Time-Based Reminder Workflows

| Workflow | Timing | Type |
|----------|--------|------|
| [Generate SMS Link 15 days prior](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789664) | 15 days before | SMS |
| [SMS 14 days prior](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789721) | 14 days before | SMS |
| [Email 7 days (Public)](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002582766) | 7 days before | Email |
| [SMS 7 days (Public)](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002597951) | 7 days before | SMS |
| [Email 7 days (Private)](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163385) | 7 days before | Email |
| [SMS 7 days (Private)](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005163433) | 7 days before | SMS |

#### Manual Trigger Workflows 🔵

| Workflow | Trigger Field | Action |
|----------|---------------|--------|
| [Send payment link](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003024548) | `Send_payment_link` = true | Emails payment URL |
| [Create Team Task](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003121331) | `Create_Team_Task` = true | Creates follow-up task |

#### Human Actions Required

- [ ] Verify payment received (`Payment_Source`, `Invoice`)
- [ ] Complete compliance (`USI_Number`, `CV_Submitted`, `Additional_Documents_Submitted`)
- [ ] Confirm attendance (`Attendance_Confirmed`)

#### Exit Criteria

- **→ Details Confirmed:** All compliance requirements met
- **→ To Be Rebooked:** Needs different course
- **→ Cancelled:** Attendee withdraws

---

### Stage 3: To Be Rebooked 🔄

**Color:** `#FCE4EC` (Light Pink)
**Workflow Count:** 0
**Typical Duration:** 1-7 days

#### Human Actions Required

- [ ] Find alternative course
- [ ] Update `Course` lookup to new course
- [ ] Notify attendee of change

#### Exit Criteria

- **→ Spot Booked:** Rebooked to new course
- **→ Cancelled:** Cannot find suitable alternative

---

### Stage 4: Waiting List 📝

**Color:** `#FFF8E1` (Light Yellow)
**Workflow Count:** 1

#### Automatic Workflow

| Workflow | Action |
|----------|--------|
| [Waitlist Record](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007034348) | Notifies attendee of waitlist status |

#### Human Actions Required

- [ ] Monitor for cancellations
- [ ] Offer alternative courses
- [ ] Contact when spot available

#### Exit Criteria

- **→ Spot Booked:** Spot becomes available
- **→ Cancelled:** No longer interested

---

### Stage 5: Course Completed 📚

**Color:** `#B2DFDB` (Light Teal)
**Workflow Count:** 1

#### Automatic Workflow

| Workflow | Timing | Action |
|----------|--------|--------|
| [Update 1 week after](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003014483) | 1 week after | Final attendance update |

#### Human Actions Required

- [ ] Submit coursework to RTO
- [ ] Set `send_cert_email` = true when certificate ready

#### Exit Criteria

- **→ Resources Uploaded:** Certificate issued and documents archived

---

### Stage 6: Cancelled ❌

**Color:** `#FFCDD2` (Light Red)
**Workflow Count:** 1
**Terminal Stage**

#### Automatic Workflow

| Workflow | Action |
|----------|--------|
| [Registration Cancelled](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009966152) | Updates counts, notifies |

#### Human Actions Required

- [ ] Document cancellation reason
- [ ] Process refund if applicable
- [ ] Update course registration count

---

### Stage 7: Details Confirmed 📋

**Color:** `#E3F2FD` (Light Blue)
**Workflow Count:** 1

Ready for course delivery - all compliance complete.

#### Exit Criteria

- **→ Fully Attended:** Attended all days
- **→ Partially Attended:** Missed some days

---

### Stage 8: Fully Attended 🎓

**Color:** `#C8E6C9` (Light Green)
**Workflow Count:** 4

#### Automatic Workflows

| Workflow | Timing | Action |
|----------|--------|--------|
| [Update 1 Day after](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003014499) | 1 day after | Updates attendance |
| [Thank you SMS](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002656733) | After course | Thanks attendee |
| [Feedback Email](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002633996) | After course | Requests feedback |
| [Attendance Acknowledgement](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006676878) | When confirmed | Acknowledges completion |

#### Exit Criteria

- **→ Course Completed:** Course finished

---

### Stage 9: Partially Attended ⚠️

**Color:** `#FFECB3` (Light Amber)
**Workflow Count:** 0

#### Human Actions Required

- [ ] Document which days missed in `Course_Days` subform
- [ ] Arrange makeup session if required

#### Exit Criteria

- **→ Course Completed:** Requirements met
- **→ To Be Rebooked:** Must complete missed content

---

### Stage 10: Resources Uploaded 🏆

**Color:** `#DCEDC8` (Light Lime)
**Workflow Count:** 1
**Terminal Stage**

Certificate issued and all documents archived. Registration complete.

---

## Course Change Workflows

These workflows fire when the `Course` lookup is changed:

| Workflow | Action |
|----------|--------|
| [Move Folder on Course Change](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005375288) | Moves Workdrive folder |
| [Update Name on Course Change](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009066119) | Updates record name |
| [Update course details](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003014626) | Syncs course info (when Update = true) |

---

## Manual Trigger Fields

| Field | Workflow | How to Use |
|-------|----------|------------|
| `Send_payment_link` | Send payment link | Set to true to email payment URL |
| `Create_Team_Task` | Create Team Task | Set to true to create follow-up task |
| `send_cert_email` | Certificate email | Set to true to email certificate |
| `Update` | Update course details | Set to true to sync course info |

---

## Compliance Fields

| Field | Purpose |
|-------|---------|
| `USI_Number` | Unique Student Identifier |
| `CV_Submitted` | Resume on file |
| `Additional_Documents_Submitted` | Supporting docs |
| `Request_3rd_Party_Record` | Pre-requisite evidence |
| `SOA_Sent` | Statement of Attainment sent |

---

## Integration Points

### Zoho Workdrive
- Creates attendee document folder on registration
- Moves folder when course changes

### ClickSend SMS
- Payment confirmations
- Attendance reminders (14, 7 days before)
- Thank you messages

### Xero (via Deals/Invoices)
- Payment tracking
- Invoice synchronization

---

## Quick Actions by Status

### Spot Tentative
```
☐ Verify attendee and account
☐ Link to deal
☐ Set Send_payment_link = true
→ Payment confirmed → Status = 'Spot Booked'
```

### Spot Booked
```
☐ Verify payment received
☐ Collect USI_Number
☐ Collect CV and documents
☐ Confirm attendance
→ Compliance complete → Status = 'Details Confirmed'
```

### After Course Delivery
```
☐ Mark attendance in Course_Days
☐ Set Status = 'Fully Attended' or 'Partially Attended'
☐ Submit coursework
☐ Set send_cert_email = true
→ Status = 'Resources Uploaded'
```

---

## Troubleshooting

### Payment Confirmation Not Sent

**Check:**
1. Is Status exactly 'Spot Booked'?
2. Is Payment_Source set?
3. Is attendee email valid?

**Solution:** Verify all fields populated correctly

### Course Count Not Updating

**Check:**
1. Is Calculate Registrations workflow active?
2. Is Course lookup populated?

**Solution:** Ensure workflow active and course linked

### Reminders Not Firing

**Check:**
1. Is Course_Start_Time set on parent Course?
2. Is attendee contact info complete?
3. Has trigger date passed?

**Solution:** Ensure dates and contact info complete

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial creation |
