# CRM_DATA_MODEL - Zoho CRM Internal Data Model

This directory contains the complete internal representation of the Zoho CRM data model, built from authoritative export sources.

## Files

### Core Model Files
- **`CRM_DATA_MODEL.json`** - Complete programmatic representation of the CRM schema
  - All 65 modules with complete metadata
  - 1,524 fields with data types, constraints, and relationships
  - 115 lookup relationships mapping module dependencies
  - Module dependency graph (forward and reverse references)

- **`CRM_DATA_MODEL_SUMMARY.md`** - Human-readable summary and documentation
  - Quick reference for module statistics
  - Most referenced and most complex modules
  - Complete module listing with field counts

### Builder Script
- **`../tools/processing/build_crm_data_model.py`** - Python script that builds the model
  - Loads and parses `zoho-data-model-2025-11-10.json` (12.1 MB)
  - Loads and parses `zoho-dependencies-2025-11-10.json` (569 KB)
  - Generates both JSON and Markdown outputs

## Data Model Structure

### ModuleSchema
Each module contains:
- **api_name**: Module identifier (e.g., "Courses", "Registration_Records")
- **labels**: Singular and plural display names
- **fields**: Dictionary of all fields in the module
- **lookup_relationships**: Fields that reference other modules
- **referenced_by**: List of modules that reference this module
- **capabilities**: creatable, editable, deletable, api_supported flags
- **statistics**: field counts, workflow counts, lookup counts

### FieldSchema
Each field contains:
- **api_name**: Field identifier
- **display_label**: Human-readable name
- **data_type**: Field type (text, number, lookup, picklist, datetime, etc.)
- **required**: Mandatory field flag
- **custom_field**: Custom vs system field
- **read_only**: Editability flag
- **lookup_module**: Target module for lookup fields
- **picklist_values**: Available options for picklist fields
- **formula**: Formula expression for calculated fields
- **unique**: Uniqueness constraint
- **system_mandatory**: Zoho system-required fields

## Key Statistics

| Metric | Count |
|--------|-------|
| Total Modules | 65 |
| Total Fields | 1,524 |
| Total Workflows | 154 |
| Lookup Relationships | 115 |
| Modules with Dependencies | 46 |
| Referenced Modules | 21 |

## Most Referenced Modules

These modules are central to the CRM data model, referenced by many other modules:

1. **Contacts** - 20 references
2. **Accounts** - 12 references
3. **Deals** - 12 references
4. **Courses** - 8 references
5. **Leads** - 8 references

## Most Complex Modules

These modules have the most fields and complexity:

1. **Leads** - 151 fields
2. **Courses** - 137 fields
3. **Contacts** - 113 fields
4. **Deals** - 86 fields
5. **Registration_Records** - 78 fields

## Core Business Modules

### Course Operations Modules
- **Courses** - Main course records (137 fields)
- **Registration_Records** - Student enrollments (78 fields, links to Courses)
- **Course_Performance** - Analytics and metrics (40 fields)
- **Course_Days** - Daily attendance tracking (6 fields, subform)
- **Venues** - Training locations (23 fields)

### Sales Modules
- **Leads** - Prospective customers (151 fields)
- **Contacts** - People (113 fields)
- **Accounts** - Organizations (61 fields)
- **Deals** - Sales opportunities (86 fields)
- **Quotes** - Price quotations (40 fields)
- **Invoices** - Billing records (57 fields)
- **Sales_Orders** - Order processing (47 fields)

### Task & Activity Modules
- **Tasks** - General tasks (21 fields)
- **Team_Tasks** - Operational tasks (35 fields)
- **Events** - Calendar events (40 fields)
- **Calls** - Phone call tracking (27 fields)

### Product & Inventory
- **Products** - Course catalogs and offerings (26 fields)
- **Price_Books** - Pricing structures
- **Quoted_Items** / **Ordered_Items** / **Invoiced_Items** - Line items (14 fields each)

## Module Dependencies

The model includes a complete dependency graph showing:
- **module_dependencies**: Which modules each module depends on (via lookup fields)
- **module_references**: Which modules reference each module (reverse lookup)

### Example: Courses Module Dependencies

**Courses depends on:**
- Contacts (for Course_Trainer)
- Venues (for Select_Venue)
- Products (for Course_Qualification)
- Accounts (for Private_Course_Client)

**Courses is referenced by:**
- Registration_Records
- Course_Performance
- Team_Tasks
- Deals
- Course_Days
- Course_Type_History
- Associated_Deals
- Associated_Attendees

## Usage

### Python Access

```python
import json

# Load the model
with open('CRM_DATA_MODEL.json', 'r') as f:
    model = json.load(f)

# Get module information
courses = model['modules']['Courses']
print(f"Courses has {courses['field_count']} fields")

# Get specific field
trainer_field = courses['fields']['Course_Trainer']
print(f"Course_Trainer is a {trainer_field['data_type']} to {trainer_field['lookup_module']}")

# Check dependencies
print(f"Courses is referenced by: {courses['referenced_by']}")

# Find all lookup fields in a module
lookups = [
    (field_name, field['lookup_module'])
    for field_name, field in courses['fields'].items()
    if field['lookup_module']
]
print(f"Lookup fields: {lookups}")
```

### Command Line Access

```bash
# View summary
cat CRM_DATA_MODEL_SUMMARY.md

# Query with jq
jq '.modules.Courses.field_count' CRM_DATA_MODEL.json
jq '.modules | keys | sort' CRM_DATA_MODEL.json
jq '.module_references.Contacts' CRM_DATA_MODEL.json
```

## Rebuilding the Model

To rebuild from updated export files:

```bash
# Update the export files in archive/zoho_export_snapshots/
# Then run:
python3 ../tools/processing/build_crm_data_model.py
```

The script will:
1. Load JSON exports
2. Parse all modules and fields
3. Build dependency graph
4. Calculate statistics
5. Generate CRM_DATA_MODEL.json and CRM_DATA_MODEL_SUMMARY.md

## Data Sources

### Primary Sources
- `data/exports/zoho-data-model-2025-11-13.json` (13 MB)
  - Complete module and field definitions
  - Export from Zoho CRM REST API
  - Contains 65 modules, 1,524 fields, 154 workflows

- `data/exports/zoho-dependencies-2025-11-13.json` (672 KB)
  - Dependency analysis
  - Field usage matrices
  - Lookup relationships
  - Cross-module dependencies

- `data/exports/Zoho_CRM_Data_Model_2025-11-13.xlsx` (181 KB)
  - 11-sheet Excel workbook with comprehensive analysis
  - Workflow dependencies and field usage matrices
  - Cross-module dependency mapping

### Reference Documentation
- `data/exports/EXCEL_GUIDE.md`
  - Explains Excel export structure
  - Field usage patterns
  - Workflow interpretation

- `docs/workflow-mapping-guide.md`
  - Course operations lifecycle
  - Stage-by-stage field mapping
  - Workflow dependencies
  - Integration points

- `README.md`
  - Repository structure
  - Module quick map

## Limitations

### Workflow Data
Workflow automation details are NOT included in this export because:
- Zoho CRM REST API does not expose workflow actions
- Only workflow metadata (name, trigger type) is available via API
- Workflow actions must be viewed in Zoho CRM UI

For workflow information, refer to:
- `docs/workflow-mapping-guide.md` - Manual documentation of workflows
- `data/exports/EXCEL_GUIDE.md` - Workflow analysis guidance

### Blueprint Data
Blueprint transitions and stages are partially available:
- Blueprint existence is tracked
- Full blueprint logic requires manual documentation

## Related Documentation

- **Field Type Reference**: See Zoho CRM API documentation for data type details
- **Workflow Guide**: `docs/workflow-mapping-guide.md`
- **Excel Export Guide**: `data/exports/EXCEL_GUIDE.md`
- **Module Docs**: `modules/*/docs/` for module-specific documentation

## Version History

| Version | Date | Source Files | Notes |
|---------|------|--------------|-------|
| 1.1 | 2025-11-18 | zoho-data-model-2025-11-13.json | Updated with 2025-11-13 exports, includes 154 workflows |
| 1.0 | 2025-11-18 | zoho-data-model-2025-11-10.json | Initial build |

## Contact & Support

This model is automatically generated from Zoho CRM exports. For questions about:
- **CRM structure**: Refer to Zoho CRM documentation
- **Custom fields**: Check with your CRM administrator
- **Workflows**: See `docs/workflow-mapping-guide.md`
- **Export updates**: Run `python3 ../tools/processing/build_crm_data_model.py` after obtaining new exports
