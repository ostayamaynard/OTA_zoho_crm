# CRM Change Planning Guide

**Generated:** 2026-01-08 16:20:23
**Purpose:** Best practices and checklists for safe CRM changes

---

## Pre-Change Checklist {#checklist}

Before making any CRM configuration change, verify:

1. **Workflow Dependencies**
   - Check WORKFLOW_DEPENDENCY_MAP.md for workflows using the field/module
   - Identify trigger fields and condition fields
   - Note any cross-module actions

2. **Lookup Relationships**
   - Review SYSTEM_OVERVIEW.md for modules that reference this one
   - Check for cascading deletes or required lookups
   - Identify integration points

3. **Active Integrations**
   - API integrations (Xero, WorkDrive, external systems)
   - Webhooks and scheduled workflows
   - Third-party extensions (ZohoSign, ClickSend)

4. **User Impact**
   - Identify users/teams affected by the change
   - Check custom views and filters using the field
   - Review reports and dashboards

5. **Data Impact**
   - Estimate records affected
   - Check for required fields that may block updates
   - Verify data migration plan if needed

6. **Testing Plan**
   - Sandbox/test environment available?
   - Test data prepared
   - Rollback procedure documented

7. **Documentation**
   - Change ticket/request logged
   - Approval obtained
   - User communication drafted

---

## Common Change Scenarios {#scenarios}

### Scenario A: Adding a Required Field {#scenario-required-field}

**Example:** Adding a required field to the Leads module

**Steps:**

1. **Pre-Change Analysis**
   - Current Leads fields: 5 fields
   - Check for existing similar fields
   - Review lookup relationships (Leads has 5 lookup fields)

2. **Data Preparation**
   - Export current Leads data
   - Identify records with missing data for new field
   - Prepare default values or data import

3. **Implementation Sequence**
   - Step 1: Add field as optional first
   - Step 2: Populate data for all existing records
   - Step 3: Verify data completeness (100% populated)
   - Step 4: Change field to required

4. **Workflow Updates**
   - Update any create/edit workflows to include new field
   - Check validation rules
   - Test automation with new required field

5. **User Communication**
   - Notify users before making field required
   - Provide field usage guidelines
   - Update training materials

**Rollback:** Remove required flag, optionally hide field from layouts

---

### Scenario B: Modifying a Workflow Trigger {#scenario-workflow-trigger}

**Example:** Changing trigger fields for a Courses workflow

**Current Configuration:**
- Module: Courses
- Active Workflows: 37
- Example: 'Update Registration Course Days' (triggered by Course_Start_Time, Course_End_Time)

**Steps:**

1. **Document Current Behaviour**
   - Export workflow configuration
   - Test current trigger conditions
   - Document expected actions

2. **Impact Analysis**
   - Check WORKFLOW_DEPENDENCY_MAP.md for this workflow
   - Identify fields read by the workflow
   - Check for cross-module actions
   - Review recent execution history

3. **Testing Sequence**
   - Clone workflow with new trigger configuration
   - Test cloned workflow with sample data
   - Verify actions execute correctly
   - Compare results with original workflow

4. **Implementation**
   - Disable original workflow
   - Activate new workflow
   - Monitor for 24-48 hours
   - Archive old workflow after validation period

**Rollback:** Re-enable original workflow, disable new one

---

### Scenario C: Changing Picklist Values {#scenario-picklist}

**Recent Example:** Deals.Lead_Source

- **Added values:** LinkedIn

**Steps:**

1. **Adding New Values** (Low Risk)
   - Check for duplicate/similar existing values
   - Add new value via field settings
   - Update workflows using the picklist (if needed)
   - Update filters and reports
   - Communicate new option to users

2. **Removing Values** (HIGH RISK)
   - **Pre-Change Analysis:**
     * Count records using the value
     * Check workflow conditions using this value
     * Review reports/dashboards filtering on this value
   - **Data Migration:**
     * Decide replacement value
     * Bulk update existing records
     * Verify 0 records use old value
   - **Configuration Update:**
     * Update workflow conditions
     * Update filters and reports
     * Remove the picklist value

3. **Reordering Values** (Low Risk)
   - No data migration needed
   - Update via drag-and-drop in field settings
   - Communicate change if order has business meaning

**Rollback:**
- Adding: Hide new value from layouts (doesn't break data)
- Removing: Re-add value immediately (data may be lost if not backed up)

---

### Scenario D: Disabling a Workflow {#scenario-disable-workflow}

**Example:** Disabling an active workflow from Courses module

**Steps:**

1. **Pre-Disable Analysis**
   - Review WORKFLOW_DEPENDENCY_MAP.md for this workflow
   - Check risk level (HIGH/MEDIUM/LOW)
   - Identify what stops working when disabled
   - Review last execution time and frequency

2. **Impact Assessment**
   - HIGH RISK: Cross-module actions or 3+ field dependencies
   - MEDIUM RISK: Field updates with business logic
   - LOW RISK: Simple notifications or logging

3. **Communication**
   - Notify affected users/teams
   - Document manual process (if automation is critical)
   - Set expectations for alternative workflow

4. **Disable Process**
   - Export workflow configuration (backup)
   - Set workflow to Inactive
   - Monitor for 1-2 weeks
   - Archive if no issues reported

**Rollback:** Re-enable workflow (configuration preserved)

---

## Risk Assessment Quick Reference {#risk-reference}

| Change Type | Risk Level | Key Concerns |
|-------------|------------|--------------|
| Add optional field | LOW | Layout updates, user training |
| Add required field | MEDIUM-HIGH | Data migration, workflow updates |
| Remove field | HIGH | Data loss, workflow breaks, integration issues |
| Add picklist value | LOW | Workflow updates, user training |
| Remove picklist value | HIGH | Data migration, workflow conditions |
| Modify workflow trigger | MEDIUM-HIGH | Automation behaviour change |
| Disable workflow | VARIES | See WORKFLOW_DEPENDENCY_MAP.md |
| Add lookup field | MEDIUM | Relationship complexity, data integrity |
| Modify field type | HIGH | Data conversion, compatibility |

---

## Testing Recommendations {#testing}

### Sandbox Testing (Recommended)

1. **Refresh sandbox** from production
2. **Apply changes** in sandbox
3. **Test workflows** with real-world scenarios
4. **Verify reports** and dashboards
5. **User acceptance testing** with key stakeholders

### Production Testing (If No Sandbox)

1. **Off-peak hours** deployment
2. **Phased rollout** (one module/team at a time)
3. **Monitor closely** for first 24-48 hours
4. **Quick rollback** capability ready

### Validation Checks

- ✓ Workflows execute without errors
- ✓ Required fields accept valid data
- ✓ Picklist values display correctly
- ✓ Lookup relationships resolve properly
- ✓ Reports return expected results
- ✓ API integrations still function
- ✓ User layouts display correctly

---

## Rollback Guidance {#rollback}

### Field Changes

**Easy Rollback:**
- Remove optional field (data preserved)
- Hide field from layouts
- Change required → optional

**Difficult Rollback:**
- Change field type (may lose data)
- Delete field (data lost)
- Remove picklist values (data may be lost)

**Best Practice:** Export data before ANY field deletion or type change

### Workflow Changes

**Easy Rollback:**
- Re-enable disabled workflow
- Revert workflow status (Active ↔ Inactive)
- Restore from exported configuration

**Requires Caution:**
- Workflows with external dependencies (API calls, webhooks)
- Workflows that create records (may cause duplicates)
- Time-based workflows (may trigger unexpectedly)

### Picklist Changes

**Easy Rollback:**
- Re-add removed values (if data was preserved)
- Restore value order

**Data Recovery:**
- Use export from before change
- Bulk update records to restore values
- May require CSV import

---

## Related Documentation {#related-docs}

- **WORKFLOW_DEPENDENCY_MAP.md** - Check workflow dependencies before changes
- **FIELD_REFERENCE.md** - Field specifications and current configuration
- **LATEST_CHANGES.md** - Learn from recent changes
- **SYSTEM_OVERVIEW.md** - Module relationships and lookup dependencies

---

*Generated by `tools/generate_ai_kb.py` on 2026-01-08*
