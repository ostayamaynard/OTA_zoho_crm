# Courses Module - Stages Comparison

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

This document compares the **Course_Status** picklist values (actual CRM stages) against the **operational workflow stages** documented in the customer journey. This validation ensures alignment between system configuration and operational documentation.

---

## Course_Status Picklist Values (Actual CRM)

Source: `zoho-data-model-2025-11-13.json` → Courses → fields → Course_Status

| Order | Picklist Value | Actual Value | Stage Order |
|-------|----------------|--------------|-------------|
| 0 | -None- | -None- | - |
| 1 | Draft | Draft | 1 |
| 2 | Sync to Wordpress | Sync to Wordpress | 2 |
| 3 | Published | Published | 3 |
| 4 | Cancelled | Cancelled | 4 |
| 5 | Completed | Completed | 5 |
| 6 | Archived | Archived | 6 |
| 7 | Published but via link | Published but via link | 7 |

**Total Active Values:** 8 (including -None-)

**Note:** Stage order in documentation now matches actual CRM picklist sequence

---

## Operational Workflow Stages (Documentation)

Source: `customer-journey-courses.json` and `workflow-mapping-guide.md`

| Order | Stage Name | Description |
|-------|------------|-------------|
| 1 | Course Created | Initial course record creation and setup |
| 2 | Course Approved | Validate minimum registrations and publish |
| 3 | Coursework | Prepare and distribute course materials |
| 4 | Course Logistics | Arrange trainer travel and venue |
| 5 | Course Enrolment | Student enrolment and compliance |
| 6 | Course Delivery | Actual course delivery and attendance |
| 7 | Certification | Certificate processing and distribution |
| 8 | Archiving | Final documentation and performance metrics |

---

## Mapping: CRM Stages to Operational Stages

| CRM Stage (Course_Status) | Maps to Operational Stage(s) | Notes |
|---------------------------|------------------------------|-------|
| **Draft** | Course Created | Initial setup before publication |
| **Sync to Wordpress** | Course Approved (pre-publication) | Intermediate sync state |
| **Published** | Course Approved, Coursework, Course Logistics, Course Enrolment, Course Delivery, Certification | Main active state covering multiple operational stages |
| **Published but via link** | Course Approved (private access) | For private/invitation-only courses |
| **Completed** | Certification, Archiving | Post-delivery processing |
| **Cancelled** | N/A (Terminal) | Course cancelled before delivery |
| **Archived** | Archiving | Final archive state |

---

## Stage Transition Analysis

### Valid Transitions

```
Draft → Sync to Wordpress → Published → Completed → Archived
Draft → Published but via link → Completed → Archived

Any Active Stage → Cancelled (terminal)
```

### Key Observations

1. **Published is Multi-Purpose**
   - The "Published" CRM status covers operational stages 2-7
   - Most workflows fire during this status
   - Progress through operational stages is tracked via other fields, not Course_Status

2. **Two Publication Paths**
   - `Sync to Wordpress` → `Published`: Public courses on website calendar
   - Direct to `Published but via link`: Private/invitation courses

3. **Operational vs CRM Stages**
   - Operational stages (8) > CRM statuses (7 active)
   - One-to-many mapping from CRM to operational stages

---

## Workflow Distribution by CRM Stage

| CRM Stage | Workflow Count | Primary Activities |
|-----------|----------------|-------------------|
| Draft | 7 | Record creation, task generation, folder setup |
| Sync to Wordpress | 1 | WordPress publication |
| Published | 25+ | Registration, logistics, delivery, attendance |
| Published but via link | 0 | Uses Published stage workflows as needed |
| Completed | 5 | Performance logging, feedback, cleanup |
| Cancelled | 2 | Notifications, stakeholder alerts |
| Archived | 1 | Final notification |

---

## Field-Based Progress Tracking

Since the "Published" CRM status covers multiple operational stages, progress is tracked via these fields:

### Coursework Stage
- `Printing_Being_Pickup_Or_posted` - Delivery method set
- `Course_Work_Uploaded_Competent` = true - Materials confirmed

### Course Logistics Stage
- `Send_Trainer_email` - Logistics sent
- `Add_Trainer_Calendar` - Calendar created
- Flight/Accommodation/Hire car fields populated

### Course Enrolment Stage
- `Registrations_Booked` - Total registrations
- `Registrations_Confirmed` - Confirmed count
- `Course_Confirmed` = true - Minimum met

### Course Delivery Stage
- `Send_Attendance_PDF_to_Trainer` - Attendance sent
- Time-based workflows fire automatically

### Certification Stage
- Managed in Registration_Records module
- `Certificate` field on registration records

---

## Discrepancies & Recommendations

### Finding 1: Missing Explicit Workflow Stages

**Observation:** Operational stages 3 (Coursework), 4 (Logistics), 5 (Enrolment), 6 (Delivery), and 7 (Certification) don't have corresponding Course_Status values.

**Impact:** All these stages happen while Course_Status = 'Published'

**Recommendation:**
- This is by design - progress is tracked via boolean/date fields
- Consider adding a separate `Operational_Stage` picklist for granular tracking
- Alternatively, use Team_Tasks completion to track stage progress

### Finding 2: Picklist Order vs Workflow Order

**Observation:** "Published but via link" (order 7) appears after "Archived" (order 6) in picklist

**Impact:** Minor - does not affect functionality

**Recommendation:** Reorder picklist to:
1. Draft
2. Sync to Wordpress
3. Published
4. Published but via link
5. Completed
6. Cancelled
7. Archived

### Finding 3: No Explicit "In Progress" Status

**Observation:** No status indicates "course currently running"

**Impact:** Cannot distinguish between "scheduled but not started" vs "currently in delivery"

**Recommendation:**
- Use `Course_Start_Time` and `Course_End_Time` for date-based filtering
- Or add "In Progress" status between "Published" and "Completed"

---

## Validation Checklist

### Picklist Values ✅

- [x] Draft exists and is active
- [x] Sync to Wordpress exists and is active
- [x] Published exists and is active
- [x] Cancelled exists and is active
- [x] Completed exists and is active
- [x] Archived exists and is active
- [x] Published but via link exists and is active

### Workflow Triggers ✅

- [x] Draft: 5 create workflows documented
- [x] Sync to Wordpress: 1 status change workflow documented
- [x] Published: Multiple workflows documented (25+)
- [x] Completed: 5 workflows documented
- [x] Cancelled: 2 workflows documented
- [x] Archived: 1 workflow documented

### Transition Paths ✅

- [x] Draft → Sync to Wordpress valid
- [x] Sync to Wordpress → Published valid
- [x] Published → Completed valid
- [x] Completed → Archived valid
- [x] Any → Cancelled valid (terminal)

---

## Summary

| Aspect | Status | Notes |
|--------|--------|-------|
| Picklist Values | ✅ Complete | All 7 active statuses documented |
| Workflow Mapping | ✅ Complete | All 37 workflows mapped to stages |
| Operational Alignment | ⚠️ Partial | Multiple operational stages map to single CRM status |
| Transition Logic | ✅ Valid | Clear progression paths |
| Terminal States | ✅ Clear | Cancelled and Archived are terminal |

### Overall Assessment

The Courses module is **well-configured** with a simplified status field that covers complex operational workflows. The design uses:
- **Course_Status** for high-level lifecycle stages
- **Boolean trigger fields** for granular workflow control
- **Date/time fields** for automated time-based actions

This approach keeps the Kanban board clean while still supporting complex multi-stage operations.

---

## Data Quality Notes

1. **Typo Preserved:** "Udpate Course ID" workflow name contains typo in source data
2. **Duplicate Names:** Two workflows named "Sync Course to Wordpress" (different IDs: 52330000002460212, 52330000006315389)
3. **-None- Value:** Default empty value present in picklist

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial creation from Zoho data model |
