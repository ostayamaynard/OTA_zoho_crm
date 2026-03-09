# Automation Coverage Matrix

**Purpose:** Calculate automation coverage percentages per SOP
**Generated:** 2025-11-19
**Status:** Phase 5 Complete

---

## Executive Summary

This matrix quantifies the automation support for each SOP step, showing which procedures have CRM workflow backing and which remain fully manual.

### Overall Coverage

| Metric | Value |
|--------|-------|
| Total SOP Steps | 72 |
| Steps with Automation Support | 22 (31%) |
| Steps Requiring Manual Action | 44 (61%) |
| Steps with Conflicts | 6 (8%) |

---

## Coverage by SOP

### Summary Table

| SOP | Total Steps | Automated | Manual | Conflicts | Coverage % |
|-----|-------------|-----------|--------|-----------|------------|
| Public Invoice | 13 | 6 | 5 | 2 | **46%** |
| Private Attendee Invoicing | 14 | 4 | 10 | 0 | **29%** |
| Deal Pipeline Management | 15 | 2 | 10 | 3 | **13%** |
| Quoting Process | 15 | 8 | 7 | 0 | **53%** |
| Registration Process | 15 | 2 | 12 | 1 | **13%** |

### Coverage Calculation Method

```
Coverage % = (Automated Steps / Total Steps) × 100

Where:
- Automated = ALIGNED (✅) + PARTIAL (⚠️) + UNDOCUMENTED (🟡)
- Manual = MISSING (🔴)
- Conflicts = CONTRADICTS (❌)
```

---

## Detailed Breakdown by SOP

### SOP 1: Public Invoice

**Coverage: 46%**

| Category | Steps | Count | Percentage |
|----------|-------|-------|------------|
| ✅ ALIGNED | 1.2, 3.3 | 2 | 15% |
| ⚠️ PARTIAL | 1.3, 3.2, 4.3 | 3 | 23% |
| 🟡 UNDOCUMENTED | 2.2 | 1 | 8% |
| ❌ CONTRADICTS | 3.1, 4.1 | 2 | 15% |
| 🔴 MISSING | 1.1, 2.1, 2.3, 3.4, 4.2 | 5 | 38% |

#### Automation Heatmap

| Step | Description | Status | Workflow Support |
|------|-------------|--------|------------------|
| 1.1 | Navigate to Deal | 🔴 | None |
| 1.2 | Set stage to Ready to Quote | ✅ | WF: 52330000002460308 |
| 1.3 | Refresh screen | ⚠️ | Quote auto-creates but not explained |
| 2.1 | Open Quote | 🔴 | None |
| 2.2 | Type "Public" in title | 🟡 | WF: 52330000002856364 (may override) |
| 2.3 | Review student details | 🔴 | None |
| 3.1 | Convert to Invoice | ❌ | WF: 52330000002460325 (different trigger) |
| 3.2 | Add Invoice Date | ⚠️ | May auto-populate |
| 3.3 | Due Date auto-fills | ✅ | WF: 52330000005069739 |
| 3.4 | Leave as Draft | 🔴 | None |
| 4.1 | Click Send Email | ❌ | WF: 52330000004534311 (Status trigger) |
| 4.2 | Choose template | 🔴 | None |
| 4.3 | Click Next and Send | ⚠️ | Workflow handles send |

---

### SOP 2: Private Attendee Invoicing

**Coverage: 29%**

| Category | Steps | Count | Percentage |
|----------|-------|-------|------------|
| ✅ ALIGNED | 4.3 | 1 | 7% |
| ⚠️ PARTIAL | 2.2, 4.1 | 2 | 14% |
| 🟡 UNDOCUMENTED | 3.2 | 1 | 7% |
| ❌ CONTRADICTS | - | 0 | 0% |
| 🔴 MISSING | 1.1-1.4, 2.1, 2.3, 3.1, 3.3, 4.2, 4.4 | 10 | 71% |

#### Automation Heatmap

| Step | Description | Status | Workflow Support |
|------|-------------|--------|------------------|
| 1.1 | Navigate to course | 🔴 | None |
| 1.2 | Check if student registered | 🔴 | None |
| 1.3 | Check if Deal created | 🔴 | None |
| 1.4 | Follow Registration SOP | 🔴 | None |
| 2.1 | Find Deal for private student | 🔴 | None |
| 2.2 | Ensure Deal linked | ⚠️ | WF: 52330000005069264 (partial) |
| 2.3 | Verify billing details | 🔴 | None |
| 3.1 | Open invoice | 🔴 | None |
| 3.2 | Review items, pricing, tax | 🟡 | WF: 52330000004975124 (auto-tax) |
| 3.3 | Adjust course fees | 🔴 | None |
| 4.1 | Use email template | ⚠️ | WF: 52330000004534311 (partial) |
| 4.2 | Confirm recipient email | 🔴 | None |
| 4.3 | Send invoice | ✅ | WF: 52330000004534311 |
| 4.4 | Note payment terms | 🔴 | None |

---

### SOP 3: Deal Pipeline Management

**Coverage: 13%**

| Category | Steps | Count | Percentage |
|----------|-------|-------|------------|
| ✅ ALIGNED | 3.2 | 1 | 7% |
| ⚠️ PARTIAL | 3.4 | 1 | 7% |
| 🟡 UNDOCUMENTED | - | 0 | 0% |
| ❌ CONTRADICTS | 2.2, 3.1, 3.3 | 3 | 20% |
| 🔴 MISSING | 1.1, 2.1, 2.3-2.5, 3.5, 4.1-4.4 | 10 | 67% |

#### Automation Heatmap

| Step | Description | Status | Workflow Support |
|------|-------------|--------|------------------|
| 1.1 | Understand Main/Sub Deals | 🔴 | None |
| 2.1 | Create Sub Deals | 🔴 | None |
| 2.2 | Populate Deal Name | ❌ | WF: 52330000002967279 (auto-names) |
| 2.3 | Populate Course/Service Type | 🔴 | None |
| 2.4 | Populate Location | 🔴 | None |
| 2.5 | Populate Start Date | 🔴 | None |
| 3.1 | Move to New stage | ❌ | Stage doesn't exist |
| 3.2 | Move to Ready to Quote | ✅ | WF: 52330000002460308 |
| 3.3 | Move to Quoted | ❌ | Stage doesn't exist |
| 3.4 | Move to Won | ⚠️ | WF: 52330000002460283 (PO trigger) |
| 3.5 | Move to Lost | 🔴 | None |
| 4.1 | Regularly review Deals | 🔴 | None |
| 4.2 | Ensure stages current | 🔴 | None |
| 4.3 | Check for duplicates | 🔴 | None |
| 4.4 | Update Closed Deals | 🔴 | None |

---

### SOP 4: Quoting Process

**Coverage: 53%**

| Category | Steps | Count | Percentage |
|----------|-------|-------|------------|
| ✅ ALIGNED | 3.3 | 1 | 7% |
| ⚠️ PARTIAL | 3.4, 4.5 | 2 | 13% |
| 🟡 UNDOCUMENTED | 2.1, 3.1, 3.2, 4.2, 4.3 | 5 | 33% |
| ❌ CONTRADICTS | - | 0 | 0% |
| 🔴 MISSING | 1.1, 1.2, 2.2, 2.3, 4.1, 4.4, 4.6 | 7 | 47% |

#### Automation Heatmap

| Step | Description | Status | Workflow Support |
|------|-------------|--------|------------------|
| 1.1 | Navigate to course | 🔴 | None |
| 1.2 | Confirm course details | 🔴 | None |
| 2.1 | Add student as attendee | 🟡 | WF: 52330000002518044 (task created) |
| 2.2 | Ensure contact details | 🔴 | None |
| 2.3 | Ensure billing details | 🔴 | None |
| 3.1 | Create Deal | 🟡 | WF: 52330000002444572 (ID assigned) |
| 3.2 | Use student name/course | 🟡 | WF: 52330000002967279 (auto-name) |
| 3.3 | Set stage Ready to Quote | ✅ | WF: 52330000002460308 |
| 3.4 | Refresh page | ⚠️ | Quote auto-creates |
| 4.1 | Open Quote | 🔴 | None |
| 4.2 | Check pricing | 🟡 | WF: 52330000004975235 (auto-tax) |
| 4.3 | Check course details | 🟡 | WF: 52330000002597194 (auto-populated) |
| 4.4 | Check student information | 🔴 | None |
| 4.5 | Send Quote | ⚠️ | WF: 52330000006984913 (field trigger) |
| 4.6 | Use appropriate template | 🔴 | None |

---

### SOP 5: Registration Process

**Coverage: 13%**

| Category | Steps | Count | Percentage |
|----------|-------|-------|------------|
| ✅ ALIGNED | - | 0 | 0% |
| ⚠️ PARTIAL | 2.4 | 1 | 7% |
| 🟡 UNDOCUMENTED | 4.1 | 1 | 7% |
| ❌ CONTRADICTS | 2.3 | 1 | 7% |
| 🔴 MISSING | 1.1-1.5, 2.1-2.2, 3.1-3.4, 4.2 | 12 | 80% |

#### Automation Heatmap

| Step | Description | Status | Workflow Support |
|------|-------------|--------|------------------|
| 1.1 | Go to Courses module | 🔴 | None |
| 1.2 | Find in dropdown | 🔴 | None |
| 1.3 | Filter by location | 🔴 | None |
| 1.4 | Filter by month | 🔴 | None |
| 1.5 | Select correct course | 🔴 | None |
| 2.1 | Scroll to Deals section | 🔴 | None |
| 2.2 | Click New Deal | 🔴 | None |
| 2.3 | Fill in deal name | ❌ | WF: 52330000002967279 (auto-names) |
| 2.4 | Select/create Account | ⚠️ | WF: 52330000005069264 (propagates) |
| 3.1 | Link Contact to Deal | 🔴 | None |
| 3.2 | Add/confirm Email | 🔴 | None |
| 3.3 | Add/confirm Mobile | 🔴 | None |
| 3.4 | Add special notes | 🔴 | None |
| 4.1 | Save the Deal | 🟡 | WF: 52330000002444572 (ID assigned) |
| 4.2 | Confirm in Deals list | 🔴 | None |

---

## Coverage Visualization

### Coverage Ranking (Best to Worst)

```
Quoting Process      ████████████████████████████░░░░░░░░░░░░░░░░░░░░  53%
Public Invoice       ███████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  46%
Private Attendee     ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  29%
Deal Pipeline        ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  13%
Registration         ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  13%
```

### Coverage by Category

```
ALIGNED (✅)         ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   7%
PARTIAL (⚠️)         ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  12%
UNDOCUMENTED (🟡)    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  11%
CONTRADICTS (❌)     ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   8%
MISSING (🔴)         ██████████████████████████████░░░░░░░░░░░░░░░░░░  61%
```

---

## Automation Support Analysis

### Workflows Most Used Across SOPs

| Workflow ID | Name | SOPs Using | Steps Covered |
|-------------|------|------------|---------------|
| 52330000002460308 | Create Quote - Stage Update | 3 | Public 1.2, Pipeline 3.2, Quoting 3.3 |
| 52330000002967279 | Deal Naming Convention | 3 | Pipeline 2.2, Quoting 3.2, Registration 2.3 |
| 52330000004534311 | Send Invoice | 2 | Public 4.1/4.3, Private 4.1/4.3 |
| 52330000004975124 | Calculate Tax (Invoice) | 2 | Public 3.2, Private 3.2 |
| 52330000002444572 | Update Deal ID | 2 | Quoting 3.1, Registration 4.1 |

### SOPs with Highest Manual Burden

| SOP | Manual Steps | % Manual |
|-----|--------------|----------|
| Registration Process | 12 | 80% |
| Private Attendee Invoicing | 10 | 71% |
| Deal Pipeline Management | 10 | 67% |

### Steps Most Commonly Missing Automation

| Step Type | Occurrences | SOPs Affected |
|-----------|-------------|---------------|
| Navigation/Search | 8 | All 5 SOPs |
| Validation | 6 | Public, Private, Quoting, Registration |
| Template Selection | 3 | Public, Private, Quoting |

---

## Improvement Opportunities

### Quick Wins (Low Effort, High Impact)

| Opportunity | SOPs Affected | Coverage Increase |
|-------------|---------------|-------------------|
| Document auto-naming in SOPs | 3 | +4% per SOP |
| Add auto-tax calculation notes | 3 | +3% per SOP |
| Clarify Stage names | 1 | +20% for Pipeline |

### Medium Effort

| Opportunity | SOPs Affected | Coverage Increase |
|-------------|---------------|-------------------|
| Add validation workflows | 4 | +8% average |
| Implement template auto-selection | 3 | +5% average |

### High Effort (New Development)

| Opportunity | SOPs Affected | Coverage Increase |
|-------------|---------------|-------------------|
| Navigation aids/quick links | 5 | +15% average |
| Duplicate detection | 1 | +7% for Pipeline |

---

## Target Coverage After Remediation

### Conservative Target (SOP Updates Only)

| SOP | Current | Target | Improvement |
|-----|---------|--------|-------------|
| Public Invoice | 46% | 62% | +16% |
| Private Attendee | 29% | 43% | +14% |
| Deal Pipeline | 13% | 40% | +27% |
| Quoting Process | 53% | 67% | +14% |
| Registration | 13% | 33% | +20% |
| **Average** | **31%** | **49%** | **+18%** |

### Aggressive Target (SOP Updates + New Workflows)

| SOP | Current | Target | Improvement |
|-----|---------|--------|-------------|
| Public Invoice | 46% | 77% | +31% |
| Private Attendee | 29% | 64% | +35% |
| Deal Pipeline | 13% | 60% | +47% |
| Quoting Process | 53% | 80% | +27% |
| Registration | 13% | 53% | +40% |
| **Average** | **31%** | **67%** | **+36%** |

---

## Appendix: Raw Data

### Step Count by Status

| SOP | ✅ | ⚠️ | 🟡 | ❌ | 🔴 | Total |
|-----|-----|-----|-----|-----|-----|-------|
| Public Invoice | 2 | 3 | 1 | 2 | 5 | 13 |
| Private Attendee | 1 | 2 | 1 | 0 | 10 | 14 |
| Deal Pipeline | 1 | 1 | 0 | 3 | 10 | 15 |
| Quoting Process | 1 | 2 | 5 | 0 | 7 | 15 |
| Registration | 0 | 1 | 1 | 1 | 12 | 15 |
| **Total** | **5** | **9** | **8** | **6** | **44** | **72** |

### Calculation Notes

- **Automated** = ✅ + ⚠️ + 🟡 (steps with any workflow support)
- **Manual** = 🔴 (steps with no workflow support)
- **Conflicts** = ❌ (steps where SOP contradicts CRM)
- Coverage % does not include conflicts in numerator

---

**Next Phase:** Phase 6 - Annotated SOPs
