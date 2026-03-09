# Courses Module - Kanban Board Usage Guide

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

This guide documents the complete Kanban board workflow for the **Courses** module in Zoho CRM. The Courses module manages the complete lifecycle of training courses from initial creation through delivery to final archiving.

### What You Now Have

1. **Kanban Data File** (`courses-stages-kanban.json`)
   - Complete workflow mapping for all 7 Course_Status stages
   - 37 workflows with clickable URLs
   - Human actions required at each stage
   - Exit criteria and transition rules

2. **Visual Diagrams**
   - `courses-kanban-simple.mmd` - Quick overview of all stages
   - `courses-kanban-detailed.mmd` - Full workflow detail with clickable links
   - `courses-workflow.mmd` - Operational workflow by stage
   - `course-attendees-journey.mmd` - Attendee lifecycle
   - `registration-timeline.mmd` - Time-based workflow Gantt chart

3. **Documentation**
   - This usage guide
   - `courses-workflow-urls.md` - Quick reference for all workflow URLs
   - `courses-stages-comparison.md` - Data validation

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Stages | 7 |
| Total Workflows | 37 |
| Automatic Workflows | ~30 |
| Manual Trigger Workflows | 7 |
| Integration Workflows | 6 |
| Fields | 137 |

---

## How to Use the Clickable Diagrams

### Viewing Diagrams

1. **VSCode with Mermaid Extension**
   - Install "Markdown Preview Mermaid Support" extension
   - Open `.mmd` file and click preview

2. **Mermaid Live Editor**
   - Go to [mermaid.live](https://mermaid.live)
   - Paste diagram content
   - Click workflow links directly

3. **GitHub Preview**
   - GitHub renders Mermaid in `.md` files
   - Wrap diagram in ```mermaid code blocks

### Clickable Workflow Links

All workflow boxes in the detailed diagram contain clickable links to Zoho CRM workflow settings:
```
https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/{workflow_id}
```

---

## Stage-by-Stage Breakdown

### Stage 1: Draft 📝

**Color:** `#E3F2FD` (Light Blue)
**Operational Stage:** Course Created
**Workflow Count:** 5 automatic + 2 field update = 7 total
**Typical Duration:** 1-3 days

#### What Happens Automatically

When a course record is created, 5 workflows fire immediately:

| Workflow | Action | Creates Record |
|----------|--------|----------------|
| [Udpate Course ID](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002444506) | Assigns CRM_Course_ID | - |
| [Create Tasks for Course](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002661635) | Generates prep tasks | Team_Tasks |
| [Naming Convention - Course](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004013116) | Formats course name | - |
| [Workdrive Folder Creation](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002462001) | Creates Workdrive folder | - |
| [Course Performance Record](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008928362) | Initializes analytics | Course_Performance |

#### Human Actions Required

- [ ] Create course record with mandatory Name
- [ ] Set course dates (`Course_Start_Time`, `Course_End_Time`)
- [ ] Select `Course_Qualification` (links to product template)
- [ ] Assign `Course_Trainer` (lookup to Contacts)
- [ ] Select `Select_Venue` (lookup to Venues)
- [ ] Define `Minimum_registrations` and `Maximum_registrations`
- [ ] Set `Fees` (price per student)
- [ ] Set `Course_Type` (Public/Private)

#### Exit Criteria

**To advance to Sync to Wordpress:**
- All mandatory fields completed
- Course ready for website publication
- Change `Course_Status` = `'Sync to Wordpress'`

---

### Stage 2: Sync to Wordpress 🔄

**Color:** `#FFF3E0` (Light Orange)
**Operational Stage:** Course Approved (Pre-Publication)
**Workflow Count:** 1
**Typical Duration:** 1 day

#### What Happens Automatically

| Workflow | Trigger | Action |
|----------|---------|--------|
| [Sync Course to Wordpress](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006315389) | Course_Status = 'Sync to Wordpress' | Publishes to WordPress, populates WP_Course_ID |

#### Human Actions Required

- [ ] Review registration numbers against minimum
- [ ] Verify course appears correctly on WordPress
- [ ] Check `WP_Course_ID` and `Event_URL` are populated

#### Exit Criteria

**To advance to Published:**
- WordPress sync confirmed
- Change `Course_Status` = `'Published'`

---

### Stage 3: Published 🌐

**Color:** `#E8F5E9` (Light Green)
**Operational Stage:** Course Approved / Enrolment / Logistics / Delivery
**Workflow Count:** 25+ (most complex stage)
**Typical Duration:** 2-8 weeks (until course delivery)

This is the **most active stage** where the majority of course operations occur. The course is live on the website, accepting enrolments, and you're preparing for delivery.

#### Automatic Workflows

**Registration Management:**
| Workflow | Trigger | Action |
|----------|---------|--------|
| [Course Confirmed - Website Calendar](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000011998036) | Course_Confirmed = true | Adds to public calendar |
| [Check MAX registration](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003463443) | Registrations_Confirmed updated | Prevents overbooking |
| [Update Registration Days](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460179) | Course dates changed | Updates linked registrations |

**Time-Based Workflows:**
| Workflow | Timing | Action |
|----------|--------|--------|
| [Check Min registration](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003463406) | 14 days before | Validates minimum met |
| [Attendance App email](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002569380) | 11 days before | Sends app to trainer |
| [SMS to Trainer (10 days)](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002656676) | 10 days before | SMS reminder |
| [Trainer Info PDF](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010838346) | 3 days before | Generates info PDF |
| [Attendance PDF](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000012545268) | 1 day before | Generates attendance list |
| [SMS to Trainer (1 day)](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002656692) | 1 day before | Final SMS reminder |

#### Manual Trigger Workflows 🔵

These workflows require you to set a checkbox field to TRUE:

| Workflow | Trigger Field | Action |
|----------|---------------|--------|
| [Send Trainer Email](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002570460) | `Send_Trainer_email` = true | Emails logistics to trainer |
| [Send to Trainer Calendar](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000011998008) | `Add_Trainer_Calendar` = true | Creates calendar event |
| [Email to Coordinator](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002582583) | `Send_Email_to_Coordinator` = true | Emails training coordinator |
| [Update Registration records](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003999102) | `Update_Registration_Records` = true | Syncs course changes |
| [Manual Attendance PDF](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004569126) | `Workflow_Actions` | Generates PDF on demand |
| [Send Attendance to Trainer](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004815267) | `Send_Attendance_PDF_to_Trainer` = true | Emails attendance list |

#### Private Course Workflows

If `Course_Type` = 'Private':
| Workflow | Trigger | Action |
|----------|---------|--------|
| [Private course Status Updates](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004318762) | Private_Course_Status changed | Status transitions |
| [Private Course Status changed](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005069426) | Private_Course_Status changed | Updates related records |
| [Private Course Client Selected](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000010760918) | Private_Course_Client selected | Populates client details |

#### Human Actions Required

**Confirmation:**
- [ ] Set `Course_Confirmed` = true when minimum registrations met
- [ ] Monitor `Registrations_Booked` and `Registrations_Confirmed`

**Coursework Preparation:**
- [ ] Arrange printing of materials
- [ ] Set `Printing_Being_Pickup_Or_posted` value
- [ ] Upload digital materials to Workdrive
- [ ] Trainer confirms via `Course_Work_Uploaded_Competent` = true

**Logistics:**
- [ ] Book flights if `Flight_to_be_booked` = Yes
- [ ] Book accommodation if `Accommodation_Required` = Yes
- [ ] Arrange hire car if `Hire_Car_Required` = Yes
- [ ] Set `Send_Trainer_email` = true to send logistics
- [ ] Set `Add_Trainer_Calendar` = true for calendar event

#### Exit Criteria

**To advance to Completed:**
- Course delivered successfully
- Change `Course_Status` = `'Completed'`

**To move to Cancelled:**
- Course cancelled (low registration, trainer unavailable, etc.)
- Change `Course_Status` = `'Cancelled'`

---

### Stage 4: Published but via link 🔗

**Color:** `#FFF8E1` (Light Yellow)
**Operational Stage:** Course Approved (Private Access)
**Workflow Count:** 0 (uses Published stage workflows when applicable)
**Typical Duration:** Variable

This stage is for courses that should not appear on the public calendar but can be accessed via direct link. Used for:
- Private corporate courses
- Special invitation-only events
- Testing new courses

#### Human Actions Required

- [ ] Share `Event_URL` with specific recipients
- [ ] Monitor registrations from direct link
- [ ] All other logistics same as Published stage

#### Exit Criteria

Same as Published stage.

---

### Stage 5: Completed ✅

**Color:** `#C8E6C9` (Light Green)
**Operational Stage:** Certification / Archiving
**Workflow Count:** 5
**Typical Duration:** 1-4 weeks (certificate processing)

#### What Happens Automatically

| Workflow | Trigger | Action |
|----------|---------|--------|
| [Status updated to completed](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004037507) | Course_Status = 'Completed' | Triggers post-completion |
| [Course Performance](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008928375) | Course_Status = 'Completed' | Updates analytics |
| [Completed course for WP](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004065214) | 1 week after start | Marks complete on WordPress |
| [Trainer Feedback Email](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002656789) | After course end | Requests feedback |
| [Trainer Task - upload materials](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002656953) | After course end | Creates upload reminder |

#### Human Actions Required

- [ ] Collect trainer feedback into `Trainer_Comments`
- [ ] Verify `Course_Work_Uploaded_Competent` = true
- [ ] Submit coursework to RTO
- [ ] Process certificates in Registration_Records
- [ ] Review Course_Performance metrics

#### Exit Criteria

**To advance to Archived:**
- All certificates issued
- Documentation complete
- Change `Course_Status` = `'Archived'`

---

### Stage 6: Cancelled ❌

**Color:** `#FFCDD2` (Light Red)
**Operational Stage:** N/A (Terminal)
**Workflow Count:** 2
**Typical Duration:** N/A (Terminal)

#### What Happens Automatically

| Workflow | Trigger | Action |
|----------|---------|--------|
| [Cancelled Course WF](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995688) | Course_Status = 'Cancelled' | Notifies stakeholders |
| [Notification for Cancel/Archive](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000011362374) | Course_Status = 'Cancelled' | Additional notifications |

#### Human Actions Required

- [ ] Document cancellation reason in `Trainer_Comments`
- [ ] Notify all enrolled registrants
- [ ] Process refunds (related Invoices/Deals)
- [ ] Cancel trainer flights, accommodation, hire car

#### Terminal Stage

This is a terminal stage. No further progression.

---

### Stage 7: Archived 📦

**Color:** `#ECEFF1` (Light Grey)
**Operational Stage:** Archiving
**Workflow Count:** 1
**Typical Duration:** N/A (Terminal)

#### What Happens Automatically

| Workflow | Trigger | Action |
|----------|---------|--------|
| [Notification for Cancel/Archive](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000011362374) | Course_Status = 'Archived' | Notifies stakeholders |

#### Human Actions Required

- [ ] Verify all documentation complete in Workdrive
- [ ] Final review of Course_Performance metrics
- [ ] Course record preserved for reporting

#### Terminal Stage

This is a terminal stage. Course lifecycle complete.

---

## Visual Legend

### Workflow Types

| Symbol | Meaning |
|--------|---------|
| ⚡ | Automatic workflow (fires without user action) |
| ⏰ | Time-based workflow (scheduled) |
| 🔵 | Manual trigger (requires checkbox = true) |

### Stage Colors

| Color | Hex | Meaning |
|-------|-----|---------|
| Light Blue | `#E3F2FD` | Setup/Draft |
| Light Orange | `#FFF3E0` | Sync/Processing |
| Light Green | `#E8F5E9` | Active/Published |
| Light Yellow | `#FFF8E1` | Private/Link Only |
| Green | `#C8E6C9` | Completed |
| Light Red | `#FFCDD2` | Cancelled |
| Light Grey | `#ECEFF1` | Archived |

---

## Troubleshooting Guide

### WordPress Not Syncing

**Symptom:** Course not appearing on website after setting status to 'Sync to Wordpress'

**Check:**
1. Is [workflow 52330000006315389](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006315389) active?
2. Is `Course_Status` exactly `'Sync to Wordpress'` (case-sensitive)?
3. Is `Course_Type` = 'Public'? (Private courses may not sync)
4. Check WordPress connection in Zoho Flow

**Solution:** Verify workflow active, status exact match, and course type

---

### Trainer Not Receiving Emails

**Symptom:** Trainer doesn't get logistics email when `Send_Trainer_email` = true

**Check:**
1. Is `Course_Trainer` lookup populated?
2. Does trainer Contact have valid email?
3. Did you set `Send_Trainer_email` = true?
4. Is [workflow 52330000002570460](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002570460) active?

**Solution:** Ensure trainer assigned with email, checkbox set

---

### Registrations Not Updating on Course

**Symptom:** `Registrations_Booked` or `Registrations_Confirmed` not reflecting actual registrations

**Check:**
1. Are Registration_Records linked via `Course` lookup?
2. Is Calculate Registrations workflow active in Registration_Records?
3. Try setting `Update_Registration_Records` = true

**Solution:** Manually trigger [Update Registration records](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003999102)

---

### Performance Record Not Created

**Symptom:** No Course_Performance record after course creation

**Check:**
1. Is [workflow 52330000008928362](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008928362) active?
2. Check Course_Performance module for record
3. Verify workflow criteria

**Solution:** Ensure Course Performance Record workflow active on create

---

### Time-Based Workflows Not Firing

**Symptom:** SMS reminders, attendance PDF not generated at expected times

**Check:**
1. Is `Course_Start_Time` populated?
2. Has the trigger date passed?
3. Are time-based workflows active?
4. Check Zoho scheduled workflow queue

**Solution:** Ensure date fields populated, workflows active, check scheduler

---

## Quick Actions by Status

### Draft
```
☐ Create course record
☐ Set Course_Qualification → triggers Course Qualification lookup Edited
☐ Set dates, venue, trainer
☐ Define registration limits and fees
→ Change Course_Status = 'Sync to Wordpress'
```

### Published
```
☐ Set Course_Confirmed = true → triggers Website Calendar
☐ Set Send_Trainer_email = true → sends logistics
☐ Set Add_Trainer_Calendar = true → creates calendar
☐ Monitor registrations
☐ [Time-based workflows fire automatically]
→ Course delivered → Change Course_Status = 'Completed'
```

### Completed
```
☐ Enter Trainer_Comments
☐ Verify Course_Work_Uploaded_Competent = true
☐ Process certificates in Registration_Records
→ Change Course_Status = 'Archived'
```

---

## Integration Points

### WordPress Integration

**Workflows:**
- Sync Course to Wordpress
- Course Confirmed - Website Calendar
- Completed course for WP

**Fields Updated:**
- `WP_Course_ID`
- `WP_Ticket_ID`
- `Event_URL`
- `Published_on`

---

### Zoho Workdrive Integration

**Workflow:** Courses_ZohoFlow_CRM Course to Workdrive Folder

**Field Updated:** `Workdrive_URL`

---

### ClickSend SMS Integration

**Workflows:**
- 10 days before course SMS to Trainer
- 1 day before course SMS to Trainer

**Required Fields:**
- `Course_Trainer` → Contact with mobile
- `SMS_Opt_Out` = false

---

## Related Modules

| Module | Relationship | Key Fields |
|--------|-------------|------------|
| **Contacts** | Course_Trainer, Venue_Contact | Full_Name, Email, Mobile |
| **Products** | Course_Qualification | Name, Price |
| **Venues** | Select_Venue | Name, Address, Facilities |
| **Accounts** | Private_Course_Client | Name, Contacts |
| **Registration_Records** | Course lookup | Status, Certificate, Attendance |
| **Team_Tasks** | Course lookup | Subject, Due_Date, Status |
| **Course_Performance** | Course lookup | Metrics, Analytics |
| **Invoices** | Via Deals | Status, Amount |
| **Deals** | Via Registration_Records | Stage, Amount |

---

## Pro Tips

### 1. Use Manual Triggers Wisely
Manual trigger workflows (🔵) give you control over when notifications are sent. Set the checkbox when you're ready, not before.

### 2. Monitor Time-Based Workflows
Time-based workflows fire automatically. Ensure `Course_Start_Time` is set correctly so reminders go out at the right times.

### 3. Private Course Handling
Private courses use additional `Private_Course_Status` field with separate workflow handling. Don't forget to set `Private_Course_Client`.

### 4. Registration Sync
After making significant course changes, set `Update_Registration_Records` = true to sync changes to all linked registrations.

### 5. Check Workflow Queue
If workflows aren't firing, check the Zoho CRM workflow queue under Setup → Automation → Workflow Rules → Scheduled Actions.

---

## Success Metrics by Stage

| Stage | Success Indicators |
|-------|-------------------|
| Draft | All fields complete, trainer/venue assigned |
| Sync to Wordpress | WP_Course_ID populated, Event_URL available |
| Published | Min registrations met, logistics complete, materials distributed |
| Completed | Trainer feedback collected, certificates issued, performance logged |
| Archived | All docs in Workdrive, records accessible |

---

## Direct Workflow Links

For quick access to all workflow settings, see [courses-workflow-urls.md](courses-workflow-urls.md).

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial creation from Zoho data model |
