# Course → Registration Data Flow

**Last Updated:** 10 December 2025 (aligned to 2025-12-10 export)
**Modules:** Courses, Registration_Records
**Flow Type:** Bi-directional
**Primary Relationship:** Registration_Records.Course (lookup) → Courses

---

## Overview

This document details how data flows between the **Courses** and **Registration_Records** modules. Unlike module-specific documentation, this focuses on the **connections** and **field propagation** between these modules.

### Key Points

- ✅ **Bi-directional flow**: Courses update Registrations, Registrations update Courses
- ⚡ **Automatic date sync**: Course date changes immediately propagate to all registrations
- 🔵 **Manual trigger for other fields**: Venue/trainer changes require manual approval
- 📊 **Count rollups**: Registrations update course count fields (Registrations_Confirmed, Registrations_Booked)

---

## Relationship Structure

### Lookup Field

| Property | Value |
|----------|-------|
| **Field** | `Registration_Records.Course` |
| **Type** | lookup → Courses |
| **Cardinality** | Many-to-One |
| **Related List** | "Registrations/Attendees" in Courses module |

### Visual Representation

```
┌─────────────┐         ┌───────────────────┐
│   Courses   │◄───────│Registration_Records│
│             │  Course │                   │
│             │  lookup │                   │
└─────────────┘         └───────────────────┘
      │                         │
      │  Dates → Auto           │ Status → Auto
      │  Venue → Manual         │ Creates → Auto
      │                         │
      └─────────────────────────┘
           Bi-directional
```

---

## Field Propagation

### Courses → Registration_Records

| Course Field | Registration Field | Data Type | Propagation Method | Automatic? |
|--------------|-------------------|-----------|-------------------|------------|
| `Course_Start_Time` | `Course_Date_and_Time` | datetime | WF: 52330000002460179 | ✅ Auto |
| `Course_End_Time` | `Course_End_Date` | datetime | WF: 52330000002460179 | ✅ Auto |
| `Select_Venue` | `Venue` | lookup (Venues) | On create + WF: 52330000003999102 | ⚡ Auto on create, 🔵 Manual update |
| `Course_Trainer` | `Trainer` | lookup (Contacts) | On create + WF: 52330000003999102 | ⚡ Auto on create, 🔵 Manual update |
| `Course_Code` | `Course_Code` | text | On create + WF: 52330000003999102 | ⚡ Auto on create, 🔵 Manual update |
| `Course_Type` | `Course_Type` | picklist | On create + WF: 52330000003999102 | ⚡ Auto on create, 🔵 Manual update |
| `Course_Status` | `Course_Status` | picklist → text | WF: 52330000003999102 | 🔵 Manual update only |
| `Private_Course_Status` | `Private_Course_Status` | picklist → text | WF: 52330000003999102 | 🔵 Manual update only |
| `Venue.Address` | `Venue_Address` | text | Via lookup | ✅ Auto |

### Registration_Records → Courses

| Registration Action | Course Field Updated | Data Type | Update Method | Automatic? |
|--------------------|---------------------|-----------|---------------|------------|
| Registration created | `Registrations_Booked` | integer | WF: 52330000002518044 | ✅ Auto |
| Registration created | `Registrations_Confirmed` | integer | WF: 52330000002518044 | ✅ Auto |
| Registration created | `Total_Registrations` | integer | WF: 52330000002518044 | ✅ Auto |
| Status changed | `Registrations_Booked` | integer | WF: 52330000002518060 | ✅ Auto |
| Status changed | `Registrations_Confirmed` | integer | WF: 52330000002518060 | ✅ Auto |
| Status → "Cancelled" | All count fields | integer | WF: 52330000009966152 | ✅ Auto |

---

## Workflow Details

### Courses → Registrations Workflows

#### 1. Update Registration Course Days (Auto)

| Property | Value |
|----------|-------|
| **Workflow ID** | 52330000002460179 |
| **Trigger** | `Course_Start_Time` OR `Course_End_Time` changes |
| **Direction** | Courses → Registration_Records |
| **Automatic** | ✅ Yes |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460179) |

**What it does:**
- Updates `Course_Date_and_Time` in ALL linked registrations
- Updates `Course_End_Date` in ALL linked registrations
- Fires immediately when course dates change
- No human intervention required

**Use Case Example:**
```
Course CPCCWHS1001 rescheduled from Nov 25 → Dec 5
→ WF fires automatically
→ All 15 registrations update to Dec 5
→ Students receive notification (separate workflow)
```

---

#### 2. Update Registration Records (Manual Trigger)

| Property | Value |
|----------|-------|
| **Workflow ID** | 52330000003999102 |
| **Trigger** | User checks `Update_Registration_Records` checkbox |
| **Direction** | Courses → Registration_Records |
| **Automatic** | 🔵 No - Manual trigger required |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003999102) |

**What it does:**
- Syncs venue, trainer, course code, type, and status to ALL linked registrations
- Updates `Venue_Address` from venue lookup

**Fields Updated:**
- `Venue` (lookup)
- `Trainer` (lookup)
- `Course_Code` (text)
- `Course_Type` (picklist)
- `Course_Status` (text)
- `Private_Course_Status` (text)
- `Venue_Address` (text)

**How to Use:**
1. Edit course field (e.g., change `Select_Venue`)
2. Check the `Update_Registration_Records` checkbox
3. Save the record
4. Workflow fires and updates ALL linked registrations

**⚠️ Warning:**
- Propagates to ALL existing registrations
- Does NOT update invoices (finance must manually edit)
- Use only when course details change significantly

---

### Registrations → Courses Workflows

#### 3. Calculate Registrations (On Create)

| Property | Value |
|----------|-------|
| **Workflow ID** | 52330000002518044 |
| **Trigger** | Registration_Record created |
| **Direction** | Registration_Records → Courses |
| **Automatic** | ✅ Yes |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518044) |

**What it does:**
- Increments count fields in parent Course
- Creates Team_Task if conditions met

**Logic:**
```
IF Registration.Status IN ("Spot Booked", "Details Confirmed"):
  Course.Registrations_Booked += 1
  Course.Registrations_Confirmed += 1
ELSE IF Registration.Status == "Spot Tentative":
  Course.Registrations_Booked += 1

Course.Total_Registrations += 1
```

---

#### 4. Calculate Registrations (On Status Change)

| Property | Value |
|----------|-------|
| **Workflow ID** | 52330000002518060 |
| **Trigger** | Registration_Records.Status changes |
| **Direction** | Registration_Records → Courses |
| **Automatic** | ✅ Yes |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002518060) |

**What it does:**
- Recalculates ALL registration counts by querying ALL registrations for this course
- Updates `Registrations_Booked`, `Registrations_Confirmed`, `Total_Registrations`

**Logic:**
```
Registrations_Booked = COUNT(
  WHERE Course == this.Course
  AND Status IN ("Spot Booked", "Spot Tentative", "Details Confirmed", "Course Completed", "Fully Attended", "Partially Attended", "Resources Uploaded")
)

Registrations_Confirmed = COUNT(
  WHERE Course == this.Course
  AND Status IN ("Spot Booked", "Details Confirmed", "Course Completed", "Fully Attended", "Partially Attended", "Resources Uploaded")
)

Total_Registrations = COUNT(
  WHERE Course == this.Course
  AND Status NOT IN ("Cancelled", "To Be Rebooked")
)
```

---

#### 5. Registration Cancelled

| Property | Value |
|----------|-------|
| **Workflow ID** | 52330000009966152 |
| **Trigger** | Registration_Records.Status → "Cancelled" |
| **Direction** | Registration_Records → Courses |
| **Automatic** | ✅ Yes |
| **URL** | [Open Workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009966152) |

**What it does:**
- Decrements registration counts on parent Course
- May trigger cancellation notifications

**Logic:**
```
ON Registration.Status CHANGE TO "Cancelled":
  Course.Registrations_Booked -= 1
  Course.Registrations_Confirmed -= 1
  Course.Total_Registrations -= 1
```

---

## Registration Status Lifecycle

### Status Values and Count Impact

| Status | Booked? | Confirmed? | Total? | Description |
|--------|---------|-----------|--------|-------------|
| -None- | ❌ | ❌ | ❌ | No status set |
| Spot Tentative | ✅ | ❌ | ✅ | Student interested but not paid |
| Spot Booked | ✅ | ✅ | ✅ | Student paid, spot reserved |
| Details Confirmed | ✅ | ✅ | ✅ | All details verified |
| Waiting List | ❌ | ❌ | ✅ | Course full, on waitlist |
| Course Completed | ✅ | ✅ | ✅ | Course finished |
| Fully Attended | ✅ | ✅ | ✅ | Attended all sessions |
| Partially Attended | ✅ | ✅ | ✅ | Attended some sessions |
| Resources Uploaded | ✅ | ✅ | ✅ | Materials uploaded |
| Cancelled | ❌ | ❌ | ❌ | Registration cancelled |
| To Be Rebooked | ❌ | ❌ | ❌ | Will reschedule |

### Status Flow Diagram

```
-None- → Spot Tentative → Spot Booked → Details Confirmed → Course Completed
                   ↓             ↓                                   ↓
              Waiting List   Cancelled                    Fully Attended / Partially Attended
                   ↓             ↓                                   ↓
              Spot Booked   To Be Rebooked                   Resources Uploaded
```

---

## Common Scenarios

### Scenario 1: Course Date Rescheduled

**User Action:**
1. Open Courses record
2. Edit `Course_Start_Time` from "2025-11-25 09:00" to "2025-12-05 09:00"
3. Save record

**System Response:**
1. ⚡ WF: 52330000002460179 fires automatically
2. ALL 15 linked registrations update:
   - `Course_Date_and_Time` → "2025-12-05 09:00"
   - `Course_End_Date` → new end date
3. Separate notification workflow sends emails to students
4. Trainer receives notification

**Manual Actions Required:**
- None - fully automatic

---

### Scenario 2: Venue Changed

**User Action:**
1. Open Courses record
2. Edit `Select_Venue` from "Melbourne CBD" to "Southbank"
3. **Check** `Update_Registration_Records` checkbox
4. Save record

**System Response:**
1. 🔵 WF: 52330000003999102 fires (manual trigger)
2. ALL 15 linked registrations update:
   - `Venue` → "Southbank"
   - `Venue_Address` → Southbank address
3. Separate notification workflow sends venue change emails

**Manual Actions Required:**
- Must check `Update_Registration_Records` checkbox

**⚠️ If checkbox NOT checked:**
- New registrations get new venue automatically
- Existing registrations keep old venue (inconsistency)

---

### Scenario 3: Student Registers for Course

**User Action:**
1. Create new Registration_Record
2. Set `Course` lookup to course record
3. Set `Status` to "Spot Booked"
4. Set `Attendee` to Contact record
5. Save record

**System Response:**
1. ⚡ WF: 52330000002518044 fires automatically
2. Fields auto-populate from Course:
   - `Course_Date_and_Time` ← `Course_Start_Time`
   - `Course_End_Date` ← `Course_End_Time`
   - `Venue` ← `Select_Venue`
   - `Trainer` ← `Course_Trainer`
   - `Course_Code` ← `Course_Code`
   - `Course_Type` ← `Course_Type`
3. Parent Course updates:
   - `Registrations_Booked` += 1
   - `Registrations_Confirmed` += 1
   - `Total_Registrations` += 1
4. Confirmation email sent to student

**Manual Actions Required:**
- None after record creation - all automatic

---

### Scenario 4: Student Cancels Registration

**User Action:**
1. Open Registration_Record
2. Change `Status` from "Spot Booked" to "Cancelled"
3. Save record

**System Response:**
1. ⚡ WF: 52330000009966152 fires automatically
2. Parent Course updates:
   - `Registrations_Booked` -= 1
   - `Registrations_Confirmed` -= 1
   - `Total_Registrations` -= 1
3. Cancellation email sent to student
4. Spot becomes available for waiting list students

**Manual Actions Required:**
- None - fully automatic

---

### Scenario 5: Course Cancelled

**User Action:**
1. Open Courses record
2. Change `Course_Status` to "Cancelled"
3. **Check** `Update_Registration_Records` checkbox
4. Save record

**System Response:**
1. 🔵 WF: 52330000003999102 fires (manual trigger)
2. ALL linked registrations update:
   - `Course_Status` → "Cancelled"
3. Notification workflow sends cancellation emails to all students
4. WF: 52330000003995688 "Cancelled Course WF" fires in Courses module

**Manual Actions Required:**
- Must check `Update_Registration_Records` checkbox
- Finance team must manually process refunds
- May need to manually update Registration.Status to "To Be Rebooked"

---

## Data Integrity Rules

### Rule 1: Date Changes Are Immediate

**Rule:** Course date changes MUST propagate to all registrations immediately

**Enforcement:** WF: 52330000002460179 fires automatically on `Course_Start_Time` or `Course_End_Time` change

**Impact:**
- Students notified within minutes
- No manual intervention required
- Invoice dates do NOT auto-update (finance must manually edit)

---

### Rule 2: Venue/Trainer Changes Require Approval

**Rule:** Venue or trainer changes do NOT auto-propagate (prevents accidental overwrites)

**Enforcement:** User MUST check `Update_Registration_Records` checkbox

**Why:** Prevents accidental propagation when editing course templates or testing changes

**Process:**
1. Edit `Select_Venue` or `Course_Trainer`
2. System prompts: "Update all registrations?"
3. User decides: check box if yes, leave unchecked if no
4. Save → if checked, WF: 52330000003999102 fires

---

### Rule 3: Registration Counts Are Workflow-Managed

**Rule:** Registration count fields (`Registrations_Booked`, `Registrations_Confirmed`, `Total_Registrations`) MUST NOT be manually edited

**Enforcement:** Fields are managed by workflows only (should be read-only)

**Validation:** If counts appear incorrect:
1. Verify all registrations have correct `Status` values
2. Check for orphaned registrations (`Course` lookup missing)
3. Re-trigger calculation by editing and saving a registration `Status`

---

### Rule 4: Fee Changes Do NOT Auto-Update Invoices

**Rule:** When `Course.Fees` changes, existing invoices do NOT auto-update

**Impact:**
- Finance team must manually edit invoices
- Risk of billing discrepancies

**Recommended SOP:** Before changing `Fees`, check if any invoices exist. If yes, coordinate with finance team.

---

## Troubleshooting

### Problem: Registration Counts Incorrect

**Symptoms:**
- `Registrations_Confirmed` doesn't match actual confirmed registrations
- `Registrations_Booked` shows wrong number

**Causes:**
- Workflow failed to fire
- Registration `Status` values incorrect
- Orphaned registrations (no `Course` lookup)

**Solution:**
1. Review all Registration_Records for this Course
2. Verify `Status` values are correct
3. Verify `Course` lookup is set
4. Edit one registration's `Status` field (change and change back)
5. Save → triggers WF: 52330000002518060 to recalculate

---

### Problem: Dates Not Updating

**Symptoms:**
- Course `Course_Start_Time` changed but registrations still show old date

**Causes:**
- Workflow WF: 52330000002460179 is inactive
- Workflow failed due to error

**Solution:**
1. Verify workflow is active: [Check WF Status](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460179)
2. Check workflow execution log for errors
3. Manually update registrations using `Update_Registration_Records` checkbox as workaround

---

### Problem: Venue Changes Not Propagating

**Symptoms:**
- Changed `Select_Venue` but registrations still show old venue

**Cause:**
- `Update_Registration_Records` checkbox was NOT checked

**Solution:**
1. Edit course record again
2. **Check** `Update_Registration_Records` checkbox
3. Save record
4. WF: 52330000003999102 will fire and update registrations

---

## Integration Points

### Registration_Records → Deals → Invoices

**Flow:**
```
Registration_Record
    ↓ (Deal lookup)
Deal
    ↓ (Quote created)
Quote
    ↓ (Invoice created)
Invoice (inherits Course_Name, Course_Type, Fees)
```

**Course Data in Invoices:**
- `Invoice.Course_Name` (lookup to Courses)
- `Invoice.Course_Type` (from Deal/Registration)
- Invoice line items include course fees

**⚠️ Important:** Invoice amounts do NOT auto-update when course fees change

See: [registration-invoice-flow.md](registration-invoice-flow.md)

---

### WorkDrive Folder Structure

**Course Folder:**
```
/Courses/{Course_Name}/
```

**Registration Subfolders:**
```
/Courses/{Course_Name}/Attendees/{Attendee_Name}/
```

**Workflow:** WF: 52330000005375288 moves attendee folder when registration moved to new course

---

## Related Workflows (Not Covered Above)

### Course-Related Registration Workflows

| Workflow ID | Name | Purpose |
|-------------|------|---------|
| 52330000002460165 | Populate Course Days | Populates registration dates on create |
| 52330000003014626 | Update course details | Manual trigger to pull latest course details |
| 52330000004112123 | Trainer Edited | Updates trainer info from course |
| 52330000005375288 | Move Course Attendee Folder on Course Change | Moves WorkDrive folder |
| 52330000009066119 | Update Name on Course Change | Updates naming convention |

---

## Related Documentation

### Module-Specific Documentation
- [Courses Module - Fields](../../modules/courses/docs/courses-fields.md)
- [Courses Module - Workflows](../../modules/courses/docs/courses-workflows.md)
- [Courses Module - Kanban Usage](../../modules/courses/docs/courses-kanban-usage.md)
- [Registration_Records Module - README](../../modules/registration_records/docs/registration-records-readme.md)

### Other Data Flow Documentation
- [Registration → Invoice Flow](registration-invoice-flow.md)
- [Invoice → Deal Flow](invoice-deal-flow.md)
- [Course Integration Flows](course-integration-flows.md)

---

## Summary

**Key Takeaways:**
1. ⚡ **Automatic date sync** - Course dates propagate immediately to registrations
2. 🔵 **Manual approval for other fields** - Venue/trainer changes require checkbox
3. 📊 **Bi-directional counts** - Registration status changes update course counts
4. ⚠️ **No invoice updates** - Fee changes don't propagate to existing invoices
5. ✅ **Workflow-driven** - All updates managed by 5 key workflows

**Workflow Count:**
- Courses → Registrations: 2 workflows
- Registrations → Courses: 5 workflows
- Total: 7 workflows managing bi-directional relationship

---

**Last Updated:** 2025-11-21
**Reviewed By:** Training Operations Team
**Next Review:** 2026-02-21
