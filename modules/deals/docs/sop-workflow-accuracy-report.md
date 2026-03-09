# Deal SOP vs Workflow Accuracy Report

**Generated:** 2025-11-18
**Comparing:** `deal-pipeline-management-sop.md` vs `deal-kanban-commercial.mmd` & `deal-kanban-attendee.mmd`

---

## Executive Summary

The SOP and Zoho workflows have **significant discrepancies** in stage naming, stage coverage, and automated actions. The workflows automate many processes not explicitly documented in the SOP, while the SOP describes stages and actions that don't exist in the current workflow implementation.

---

## 1. Stage Name Discrepancies

### SOP Stages vs CRM Workflow Stages

| SOP Stage | CRM Stage | Status |
|-----------|-----------|--------|
| **New** | Not found | **MISSING** - CRM uses "Qualification" instead |
| **Qualified** | Not found | **MISSING** - CRM uses "Negotiation/Review" instead |
| Qualification (not in SOP) | Qualification | **EXTRA** - In CRM but not in SOP |
| Negotiation/Review (not in SOP) | Negotiation_Review | **EXTRA** - In CRM but not in SOP |
| Ready to Quote | Ready_to_Quote | **MATCH** |
| **Quote Sent** | Not found | **MISSING** - No separate stage in CRM |
| Awaiting ZipPay (not in SOP) | Awaiting_ZipPay_Confirmation | **EXTRA** - Payment method stage not in SOP |
| Awaiting PO | Awaiting_PO | **MATCH** |
| **Course Booked** | Not found | **MISSING** - No stage in CRM |
| Awaiting Invoice Payment | Awaiting_Invoice_Payment | **MATCH** |
| Closed - Won | Closed_Won | **MATCH** |
| Closed - Lost | Closed_Lost | **MATCH** |
| Closed - Unused | Unused | **PARTIAL** - Different naming/positioning |
| UnAccounted (not in SOP) | UnAccounted | **EXTRA** - Kanban filter only |

### Critical Issues

1. **Stage Mismatch**: SOP describes "New" → "Qualified" but CRM has "Qualification" → "Negotiation/Review"
2. **Missing "Quote Sent" Stage**: SOP requires recording when quote is emailed, but CRM has no dedicated stage
3. **Missing "Course Booked" Stage**: SOP describes this as a distinct stage for confirming dates/trainer, but CRM doesn't have it
4. **Undocumented ZipPay Stage**: CRM has payment confirmation stage not mentioned in SOP

---

## 2. Automated Actions - What EXISTS

### Deal Creation Automations (Step 1 - Supported)

| SOP Requirement | Workflow | Status |
|-----------------|----------|--------|
| Naming convention: `P - [Company] - [Location] - [Course/Contact]` | WF_DealNaming (ID: 52330000002967279 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967279))) | **AUTOMATED** |
| Assign Deal ID | WF_UpdateDealID (ID: 52330000002444572 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002444572))) | **AUTOMATED** |
| Calculate Amount | WF_UpdateAmount (ID: 52330000003995130 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995130))) | **AUTOMATED** |
| Assign Account for web deals | WF_WebsiteAccount (ID: 52330000005157945 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005157945))) | **AUTOMATED** |

### Quote Generation (Step 3 - Partially Supported)

| SOP Requirement | Workflow | Status |
|-----------------|----------|--------|
| Click "Ready to Quote" generates quote | WF_CreateQuote (ID: 52330000002460308 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308))) | **AUTOMATED** |
| Mark quote as "Sent" | None | **MANUAL** - No workflow |
| Mark quote as "Closed - Won" | None | **MANUAL** - No workflow |
| Mark quote as "Unused" | None | **MANUAL** - No workflow |

### Task Management & Follow-Up (Step 4 - Partially Supported)

| SOP Requirement | Workflow | Status |
|-----------------|----------|--------|
| Create follow-up task after stage update | Partial | **PARTIALLY AUTOMATED** |
| Due date 3-5 business days | Not configurable | **HARDCODED** in workflows |
| PO follow-up 28 days before course | WF_PO28Days (ID: 52330000002638311 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311))) | **AUTOMATED** |
| PO follow-up 14 days before course | WF_PO14Days (ID: 52330000002638269 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269))) | **AUTOMATED** |
| PO follow-up 1 day before course | WF_PO1Day (ID: 52330000002638411 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638411))) | **AUTOMATED** |
| Follow up future deals | WF_FollowUpFuture (ID: 52330000001178038 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000001178038))) | **AUTOMATED** |
| Manual task creation per stage | WF_CreateTeamTask (ID: 52330000002460147 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460147))) | **AVAILABLE** (field-triggered) |

---

## 3. What's MISSING from Workflows

### Not Automated - Requires Manual Action

| SOP Requirement | Gap Description |
|-----------------|-----------------|
| **Classify as New/Existing Business** | No workflow - manual field entry |
| **Populate mandatory fields** (attendees, Product Type, Course Code) | No validation workflow |
| **Record quote send date** | No timestamp workflow when quote emailed |
| **Set follow-up task after quote sent** | No "Quote Sent" stage trigger |
| **Enter final booking info** | No "Course Booked" stage or validation |
| **Assign confirmed trainer** | No trainer assignment workflow |
| **Monitor invoice payment status** | No payment tracking automation |
| **Match quotes/invoices to deals for reporting** | No reconciliation workflow |
| **Tier 1/Tier 2 tracking** | No tier-based workflow logic |
| **Region/industry segment tagging** | No segment-based automation |

### SOP Actions with No CRM Equivalent

1. **Quote lifecycle tracking** - SOP describes marking quotes as Sent/Won/Unused but no workflows handle this
2. **Course booking confirmation** - No stage or workflow for trainer assignment and logistics
3. **Invoice-to-deal matching** - No automated reconciliation
4. **Pipeline review reminders** - No end-of-week/month review automation

---

## 4. What's IN WORKFLOWS but NOT in SOP

### Undocumented Automations

| Workflow | Action | Documentation Status |
|----------|--------|---------------------|
| WF_CopyDealNaming (ID: 52330000004013962 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004013962))) | Updates Deal_Name on Course field change | **UNDOCUMENTED** |
| WF_UpdateDealID2 (ID: 52330000004452015 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004452015))) | Maintains Deal ID on edit | **UNDOCUMENTED** |
| WF_FastTrack (ID: 52330000004434048 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004434048))) | Fast-tracks 1-attendee public deals (INACTIVE) | **UNDOCUMENTED** |
| WF_PO5Days (ID: 52330000009085891 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085891))) | PO follow-up 5 days before (stage-triggered) | **UNDOCUMENTED** |
| WF_EmailCoordinator (ID: 52330000002967852 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967852))) | Emails coordinator for attendee details | **UNDOCUMENTED** |
| WF_AccountUpdate (ID: 52330000005069264 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005069264))) | Propagates Account_Name to related records | **UNDOCUMENTED** |
| WF_StageUpdateAttendees (ID: 52330000004335567 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004335567))) | Updates Registration_Records status on Closed_Won | **UNDOCUMENTED** |
| WF_POUpdateRegistrations (ID: 52330000006993545 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006993545))) | Updates Registration_Records when PO received | **UNDOCUMENTED** |
| WF_POReceived (ID: 52330000002460283 ([Open](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460283))) | Updates deal status, notifies team, timestamps PO | **UNDOCUMENTED** |

### Undocumented Stages

- **Awaiting ZipPay Confirmation** - Payment method handling not in SOP
- **UnAccounted** - Kanban filter stage not mentioned

---

## 5. Stage Flow Discrepancies

### SOP Implied Flow
```
New → Qualified → Ready to Quote → Quote Sent → Awaiting PO → Course Booked → Awaiting Invoice Payment → Closed
```

### Actual CRM Flow (from workflows)
```
Qualification → Negotiation/Review → Ready to Quote → [Awaiting ZipPay] → Awaiting PO → Awaiting Invoice Payment → Closed Won
                                  ↘ Unused (can return)
                                  ↘ Closed Lost (from any stage)
```

### Key Flow Issues

1. **No "Quote Sent" transition** - Quote generation happens at "Ready to Quote" but no subsequent stage
2. **No "Course Booked" stage** - Logistics confirmation not tracked as a stage
3. **ZipPay pathway undocumented** - Alternative payment flow exists but not in SOP
4. **Direct Closed Won from Awaiting PO** - Workflow allows skipping invoice stage

---

## 6. Recommendations

### SOP Updates Needed

1. **Rename stages** to match CRM: New → Qualification, Qualified → Negotiation/Review
2. **Remove or clarify** "Quote Sent" and "Course Booked" stages
3. **Document ZipPay flow** as an alternative payment pathway
4. **Add attendee management section** covering email coordinator and registration workflows
5. **Document automated naming convention** format used by WF_DealNaming
6. **Add PO follow-up schedule** (28, 14, 5, 1 days before course)

### Workflow Gaps to Address

1. **Add Quote Sent tracking** - Either a stage or timestamp field with workflow
2. **Add Course Booked stage** - Or document where this confirmation happens
3. **Invoice payment monitoring** - No workflow tracks payment status changes
4. **Tier/segment automation** - Consider priority-based task assignment

### Immediate Alignment Actions

1. Verify which document is authoritative (SOP or CRM configuration)
2. Reconcile stage names between documentation and system
3. Decide if "Quote Sent" and "Course Booked" should be CRM stages or just task checkpoints
4. Document all 19 workflows referenced in the mermaid files

---

## 7. Workflow Coverage Summary

| Category | Total Workflows | Documented in SOP |
|----------|-----------------|-------------------|
| Deal Creation | 6 | 1 (naming) |
| Follow-up Tasks | 5 | 1 (general mention) |
| Quote Generation | 1 | 1 |
| PO Processing | 1 | 1 (implied) |
| Attendee/Registration | 5 | 0 |
| **TOTAL** | **19** | **4 (21%)** |

---

## Conclusion

The SOP and CRM workflows are **misaligned** in terminology and coverage. The CRM automates significantly more than documented, while the SOP describes stages that don't exist in the system. A reconciliation effort is needed to:

1. Update the SOP to reflect actual CRM stages and automation
2. OR modify CRM to match the documented process
3. Document the 15 workflows (79%) not mentioned in the SOP
