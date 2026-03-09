# Registration Records - Stages Comparison

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Purpose

This document validates that the documented Registration Status stages match the actual picklist values in Zoho CRM.

---

## CRM Picklist vs Documentation

| Order | CRM Status Value | Documented Stage | Match |
|-------|------------------|------------------|-------|
| 1 | Spot Tentative | Spot Tentative | ✅ |
| 2 | Spot Booked | Spot Booked | ✅ |
| 3 | To Be Rebooked | To Be Rebooked | ✅ |
| 4 | Waiting List | Waiting List | ✅ |
| 5 | Course Completed | Course Completed | ✅ |
| 6 | Cancelled | Cancelled | ✅ |
| 7 | Details Confirmed | Details Confirmed | ✅ |
| 8 | Fully Attended | Fully Attended | ✅ |
| 9 | Partially Attended | Partially Attended | ✅ |
| 10 | Resources Uploaded | Resources Uploaded | ✅ |

**Status: All 10 stages verified** ✅

---

## Workflow Count Verification

| Stage | Documented Workflows | Verified |
|-------|---------------------|----------|
| Spot Tentative | 6 | ✅ |
| Spot Booked | 14 (8 entry + 6 time-based) | ✅ |
| To Be Rebooked | 0 | ✅ |
| Waiting List | 1 | ✅ |
| Course Completed | 1 | ✅ |
| Cancelled | 1 | ✅ |
| Details Confirmed | 1 | ✅ |
| Fully Attended | 4 | ✅ |
| Partially Attended | 0 | ✅ |
| Resources Uploaded | 1 | ✅ |

**Additional Workflows:**
- Course Change: 3
- Trainer Update: 1
- Invoice Payment: 1
- Manual Triggers: 3

**Total: 36 workflows** ✅

---

## Operational vs CRM Stage Order

### CRM Picklist Order (Actual)
The order as defined in Zoho CRM Status field:

1. Spot Tentative
2. Spot Booked
3. To Be Rebooked
4. Waiting List
5. Course Completed
6. Cancelled
7. Details Confirmed
8. Fully Attended
9. Partially Attended
10. Resources Uploaded

### Operational Flow (Typical)
The order most records actually follow:

1. **Spot Tentative** - Initial booking
2. **Spot Booked** - Payment confirmed
3. **Details Confirmed** - Compliance complete
4. **Fully Attended** / **Partially Attended** - Course delivered
5. **Course Completed** - Post-course processing
6. **Resources Uploaded** - Certificate issued (terminal)

### Exception Paths
- **Waiting List** - Course full (exits to Spot Booked or Cancelled)
- **To Be Rebooked** - Move to different course (exits to Spot Booked)
- **Cancelled** - Withdrawn (terminal)

---

## Notes on Stage Order

The CRM picklist order differs from operational flow:
- **Course Completed** (order 5) actually comes after **Fully Attended** (order 8) in practice
- **Details Confirmed** (order 7) comes after **Spot Booked** (order 2) in practice
- This is typical in CRM systems where picklist order reflects historical additions rather than workflow sequence

---

## Integration Points Verified

| Integration | Workflows | Verified |
|-------------|-----------|----------|
| Zoho Workdrive | 2 | ✅ |
| ClickSend SMS | 6 | ✅ |
| Xero (via Deals) | Indirect | ✅ |

---

## Key Fields Verified

| Field | Purpose | Documented |
|-------|---------|------------|
| Status | Main stage field | ✅ |
| Course | Parent course lookup | ✅ |
| Attendee | Contact lookup | ✅ |
| Account_Name | Company lookup | ✅ |
| Send_payment_link | Manual trigger | ✅ |
| Create_Team_Task | Manual trigger | ✅ |
| send_cert_email | Manual trigger | ✅ |
| Update | Manual trigger | ✅ |

---

## Data Source Verification

**Source File:** `tools/exports/zoho_export_package/zoho-data-model-2025-11-13.json`

**Extraction Method:** Python script to extract Registration_Records module data

**Verification Date:** 2025-11-18

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial validation |
