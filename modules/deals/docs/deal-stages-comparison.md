# Deal Stages - Actual vs Kanban Comparison

**Date:** 2025-11-13  
**Source:** zoho-data-model-2025-11-13.json

---

## ❌ **ISSUE FOUND: Kanban Stages Are Incorrect**

The kanban files (`deal_stages_kanban.json` and `DEAL_KANBAN_USAGE_GUIDE.md`) contain **incorrect stage names and order** compared to the actual Zoho CRM data model.

---

## ✅ **ACTUAL Deal Stages (from Data Model)**

Based on the Stage field in the Deals module, here are the **USED** stages (type: "used"):

| Sequence | Stage Name | Deal Category | Probability | Type | Status |
|----------|-----------|---------------|-------------|------|--------|
| 1 | **Qualification** | Open | 10% | used | ✅ Active |
| 2 | **Negotiation/Review** | Open | 90% | used | ✅ Active |
| 3 | **Ready to Quote** | Open | 70% | used | ✅ Active |
| 4 | **Awaiting ZipPay Confirmation** | Open | 80% | used | ✅ Active |
| 5 | **Awaiting Purchase Order** | Open | 90% | used | ✅ Active |
| 6 | **Awaiting Invoice Payment** | Open | 80% | used | ✅ Active |
| 7 | **Unused** | Open | 50% | used | ✅ Active |
| 8 | **Closed Won** | Closed Won | 100% | used | ✅ Active |
| 9 | **Closed Lost** | Closed Lost | 0% | used | ✅ Active |

**Total: 9 USED stages**

---

## ❌ **UNUSED Stages (inactive in system)**

These stages exist in the picklist but are marked as `"type": "unused"`:

| Sequence | Stage Name | Deal Category | Probability | Type | Status |
|----------|-----------|---------------|-------------|------|--------|
| 2 | Proposal/Price Quote | Open | 75% | unused | ❌ Inactive |
| 3 | Needs Analysis | Open | 20% | unused | ❌ Inactive |
| 4 | Value Proposition | Open | 40% | unused | ❌ Inactive |
| 5 | Identify Decision Makers | Open | 60% | unused | ❌ Inactive |
| 6 | Future Opportunity | Open | 95% | unused | ❌ Inactive |
| 7 | Closed Lost to Competition | Closed Lost | 0% | unused | ❌ Inactive |

---

## 🔴 **What's Wrong in the Kanban**

### **Current Kanban Stages (INCORRECT):**
1. Qualification ✅ (correct)
2. **Needs Analysis** ❌ (this is UNUSED in the system!)
3. Ready to Quote ✅ (correct)
4. Negotiation/Review ✅ (correct, but wrong order - should be #2)
5. Closed Won ✅ (correct)
6. Closed Lost ✅ (correct)

### **Missing from Kanban:**
- ❌ **Awaiting ZipPay Confirmation** (sequence 4, used)
- ❌ **Awaiting Purchase Order** (sequence 5, used)
- ❌ **Awaiting Invoice Payment** (sequence 6, used)
- ❌ **Unused** (sequence 7, used)

### **Incorrectly Included:**
- ❌ **Needs Analysis** (marked as unused in system - should NOT be in kanban)

---

## 📊 **Correct Stage Flow**

Based on sequence numbers and deal categories:

### **Open Stages (in order):**
1. **Qualification** (10% probability)
2. **Negotiation/Review** (90% probability)
3. **Ready to Quote** (70% probability)
4. **Awaiting ZipPay Confirmation** (80% probability)
5. **Awaiting Purchase Order** (90% probability)
6. **Awaiting Invoice Payment** (80% probability)
7. **Unused** (50% probability)

### **Closed Stages:**
8. **Closed Won** (100% probability)
9. **Closed Lost** (0% probability)

---

## 🎨 **Actual Stage Colors (from data model)**

| Stage | Colour Code | Hex Equivalent |
|-------|------------|----------------|
| Qualification | #ffc6c6 | Light Red/Pink |
| Negotiation/Review | #ced9ff | Light Blue |
| Ready to Quote | #ffda62 | Yellow |
| Awaiting ZipPay Confirmation | #af38fa | Purple |
| Awaiting Purchase Order | #dbdbdb | Light Grey |
| Awaiting Invoice Payment | #acacac | Grey |
| Unused | #ffc6c6 | Light Red/Pink |
| Closed Won | #25b52a | Green |
| Closed Lost | #eb4d4d | Red |

---

## ⚠️ **Impact**

1. **Workflows may not trigger correctly** - If workflows reference "Needs Analysis" stage, they won't work because that stage is unused.

2. **Missing stages** - The kanban doesn't show 4 active stages:
   - Awaiting ZipPay Confirmation
   - Awaiting Purchase Order
   - Awaiting Invoice Payment
   - Unused

3. **Wrong order** - Negotiation/Review should be stage 2, not stage 4.

---

## 🔧 **Recommended Actions**

1. **Update `deal_stages_kanban.json`** with correct stages
2. **Update `DEAL_KANBAN_USAGE_GUIDE.md`** with correct stage flow
3. **Regenerate Mermaid diagrams** with correct stages
4. **Verify workflows** - Check if any workflows reference "Needs Analysis" (they won't work)
5. **Update stage progression** in documentation

---

## 📝 **Data Model Reference**

**File:** `zoho_export_package/zoho-data-model-2025-11-13.json`  
**Module:** Deals  
**Field:** Stage (api_name: "Stage")  
**Field ID:** 52330000000002361  
**Lines:** 91330-91633

**Key Field Properties:**
- `system_mandatory`: true
- `history_tracking_enabled`: true
- `enable_colour_code`: true
- `data_type`: "picklist"
- Total picklist values: 15 (9 used, 6 unused)

---

**Last Updated:** 2025-11-13  
**Data Model Date:** 2025-11-13


