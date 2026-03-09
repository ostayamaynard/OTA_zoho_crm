# Module Documentation Standard

**Purpose:** Define a consistent structure for documenting all Zoho CRM modules to enable workflow tracing, field impact analysis, and CRM optimization.

**Goal:** When a stage or field is updated, trace exactly what happens - enabling removal of unnecessary workflows, modules, or fields while maintaining the CRM as the source of truth for all 3rd party integrations.

---

## Modules to Document

| Module | API Name | Primary Status Field | Priority |
|--------|----------|---------------------|----------|
| Leads | Leads | Lead_Status | ✅ Complete |
| Contacts | Contacts | - | ✅ Complete |
| Accounts | Accounts | - | ✅ Complete |
| Deals | Deals | Stage | ✅ Complete |
| Courses | Courses | Course_Status | ✅ Complete |
| Course Attendees | Course_Attendees / Registration_Records | Attendee_Status | ✅ Complete |
| Venues | Venues | - | ✅ Complete |
| Quotes | Quotes | Quote_Stage | ✅ Complete |
| Invoices | Invoices | Status | ✅ Complete |

---

## Directory Structure

Each module should have the following structure:

```
modules/{module_name}/
├── data/
│   ├── {module}-stages-kanban.json    # Stage/status data with workflows
│   └── customer-journey-{module}.json  # Customer journey mapping
├── diagrams/
│   ├── {module}-kanban-simple.mmd     # Simplified Mermaid diagram
│   ├── {module}-kanban-detailed.mmd   # Detailed Mermaid with workflows
│   └── {module}-workflow.mmd          # Workflow flow diagram
└── docs/
    ├── {module}-fields.md             # Complete field reference
    ├── {module}-workflows.md          # Complete workflow reference
    ├── {module}-status-map.md         # Status/stage picklist mapping
    ├── {module}-workflow-urls.md      # Quick reference with URLs
    └── {module}-usage.md              # Usage guide and kanban setup
```

---

## Required Documentation Files

### 1. `{module}-fields.md`

**Purpose:** Complete field reference with data types and relationships

**Content:**
- Field count and source metadata
- Standard fields table (api_name, label, data_type, required)
- Custom fields organized by category
- Lookup relationships
- Workflow trigger fields (fields that trigger automations when updated)

**Template:**
```markdown
# {Module} Module - Field Reference

**Generated from:** zoho-data-model-YYYY-MM-DD.json
**Total Fields:** {count}

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| ... | ... | ... | ... |

---

## Custom Fields by Category

### {Category Name}

| API Name | Label | Data Type |
|----------|-------|-----------|
| ... | ... | ... |

---

## Lookup Relationships

| Field API Name | Field Label | Target Module | Required |
|----------------|-------------|---------------|----------|
| ... | ... | ... | ... |

---

## Workflow Trigger Fields

These fields trigger automated workflows when updated:

| API Name | Label | Workflows Triggered |
|----------|-------|---------------------|
| ... | ... | ... |

---

**Last Updated:** YYYY-MM-DD
**Source:** Zoho CRM Export YYYY-MM-DD
```

---

### 2. `{module}-workflows.md`

**Purpose:** Complete workflow reference with IDs, triggers, and URLs

**Content:**
- Workflow summary by trigger type
- Each workflow with full details:
  - Workflow ID
  - Status (Active/Inactive)
  - Trigger type (create, field_update, date_or_datetime)
  - Trigger fields and conditions
  - Created/Modified by and timestamps
  - Records created by workflow
  - Direct URL to workflow in Zoho
- Quick reference table

**Template:**
```markdown
# {Module} Module - Workflow Reference

**Generated from:** zoho-dependencies-YYYY-MM-DD.json
**Total Workflows:** {count}
**Active Workflows:** {count}
**Inactive Workflows:** {count}

---

## Workflow Summary by Trigger Type

| Trigger Type | Count | Description |
|--------------|-------|-------------|
| create | ... | Fire when record is created |
| field_update | ... | Fire when specific fields are updated |
| date_or_datetime | ... | Fire based on date/time conditions |

---

## Create Trigger Workflows

### {Workflow Name}

| Property | Value |
|----------|-------|
| **Workflow ID** | ... |
| **Status** | Active/Inactive |
| **Trigger Type** | create |
| **Created By** | ... |
| **Modified By** | ... |
| **Created Time** | ... |
| **Modified Time** | ... |
| **Last Executed** | ... |

**Creates:** {List of records created}

**URL:** https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/{id}

---

## Quick Reference Table

| Workflow Name | ID | Trigger Type | Status | URL |
|--------------|-----|--------------|--------|-----|
| ... | ... | ... | ... | [Open](...) |

---

**Last Updated:** YYYY-MM-DD
**Source:** Zoho CRM Export YYYY-MM-DD
```

---

### 3. `{module}-status-map.md`

**Purpose:** Status/stage picklist mapping with colors and sequence

**Content:**
- Status field API information
- Complete sequence table with:
  - Sequence number
  - Display value
  - Colour code
  - Type (used/unused)
  - ID
- Status categories (Entry, Active, Terminal, etc.)
- Color palette reference
- Status flow diagram
- Transition rules

**Template:**
```markdown
# {Module} Module - Status Map

**Generated from:** zoho-data-model-YYYY-MM-DD.json
**Field API Name:** {Status_Field}
**Total Statuses:** {count} ({used} used, {unused} unused)

---

## Status Sequence (CRM Export Order)

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| ... | ... | ... | ... | ... |

---

## Status Categories

### {Category Name}

| Status | Colour | Description |
|--------|--------|-------------|
| ... | ... | ... |

---

## Status Flow Diagram

```
[diagram here]
```

---

## Status Transitions

### From {Status}
- **To {Next Status}:** {Condition}

---

**Last Updated:** YYYY-MM-DD
**Source:** Zoho CRM Export YYYY-MM-DD
```

---

## Data Extraction Process

### Step 1: Extract from CRM Exports

Use these files as the single source of truth:
- `data/exports/zoho-data-model-YYYY-MM-DD.json`
- `data/exports/zoho-dependencies-YYYY-MM-DD.json`

### Step 2: Extract Fields

```python
# Extract all fields for a module
import json

with open('zoho-data-model-YYYY-MM-DD.json', 'r') as f:
    data = json.load(f)

module = data.get('{ModuleName}', {})
fields = module.get('fields', [])

for field in fields:
    api_name = field.get('api_name', '')
    label = field.get('field_label', '')
    data_type = field.get('data_type', '')
    custom = field.get('custom_field', False)
    required = field.get('system_mandatory', False)
```

### Step 3: Extract Status Picklist

```python
# Find status field and extract picklist values
for field in fields:
    if field.get('api_name') == '{Status_Field}':
        for value in field.get('pick_list_values', []):
            display = value.get('display_value')
            color = value.get('colour_code')
            seq = value.get('sequence_number')
            type_ = value.get('type')
            id_ = value.get('id')
```

### Step 4: Extract Workflows

```python
# Extract workflows for a module
with open('zoho-dependencies-YYYY-MM-DD.json', 'r') as f:
    deps = json.load(f)

workflows = deps.get('workflow_dependencies', {})

for key, workflow in workflows.items():
    if workflow.get('module') == '{ModuleName}':
        name = workflow.get('workflow_name')
        id_ = workflow.get('workflow_id')
        active = workflow.get('active')
        trigger = workflow.get('trigger_type')
```

### Step 5: Extract Lookup Relationships

```python
# Extract lookups for a module
lookups = deps.get('lookup_relationships', {})
module_lookups = lookups.get('{ModuleName}', [])

for lookup in module_lookups:
    field_name = lookup.get('field_name')
    label = lookup.get('field_label')
    target = lookup.get('lookup_module')
    required = lookup.get('required')
```

---

## Field Impact Analysis

For each module, identify:

### 1. Workflow Trigger Fields
Fields that when updated, trigger workflows:
- Which workflows fire
- What records are created
- What fields are updated

### 2. Cross-Module Dependencies
Fields that affect other modules:
- Lookup fields
- Formula fields referencing other modules
- Workflows that create/update other modules

### 3. Integration Fields
Fields used by 3rd party integrations:
- Stripe: Payment_CODE, Stripe_ID
- Google Ads: GCLID, ZCAMPAIGNID, etc.
- ClickSend: SMS fields
- Google Maps: Latitude, Longitude

### 4. Conversion Fields
Fields involved in record conversion:
- Converted__s
- Converted_Account, Converted_Contact, Converted_Deal

---

## Optimization Checklist

Use this checklist when auditing each module:

### Workflows
- [ ] Are all workflows active and needed?
- [ ] Are there duplicate workflows doing similar things?
- [ ] Can workflows be consolidated?
- [ ] Are trigger conditions correct?

### Fields
- [ ] Are all custom fields being used?
- [ ] Are there duplicate fields?
- [ ] Are field types correct?
- [ ] Are required fields actually required?

### Status/Stages
- [ ] Are all statuses being used?
- [ ] Is the sequence logical?
- [ ] Are color codes consistent?
- [ ] Are transitions documented?

### Integrations
- [ ] Are integration fields populated correctly?
- [ ] Is data flowing to/from 3rd parties?
- [ ] Is CRM the source of truth?

---

## Cross-Module Traceability

### Leads → Other Modules

When a Lead is converted:
- Creates: Contact, Account, Deal
- May create: Registration_Record, Invoice
- Fields mapped:
  - Lead.First_Name → Contact.First_Name
  - Lead.Email → Contact.Email
  - Lead.Company → Account.Account_Name

### Deals → Other Modules

When a Deal progresses:
- May create: Quote, Invoice, Registration_Record
- Updates: Contact, Account

### Invoices → Other Modules

When Invoice created:
- Links to: Account, Contact, Deal
- Affects: Account balance

---

## Documentation Maintenance

### When to Update
- After CRM export refresh
- After adding/removing workflows
- After adding/removing fields
- After changing status/stage values

### How to Update
1. Run fresh CRM export
2. Run extraction scripts
3. Update documentation files
4. Commit with clear message

### Version Control
- All documentation in Git
- Commit message format: "Update {Module} documentation from CRM export YYYY-MM-DD"

---

## Quick Start for New Module

1. Create directory structure:
   ```bash
   mkdir -p modules/{module}/data modules/{module}/diagrams modules/{module}/docs
   ```

2. Extract data from exports using Python scripts

3. Create documentation files following templates above

4. Verify against CRM export (audit for gaps)

5. Commit and push

---

**Document Created:** 2025-11-18
**Maintained By:** Zoho CRM Documentation Team
