# AI Knowledge Base for Claude Projects

**Created:** 8 January 2026  
**Purpose:** Optimised markdown documentation for use as context in Claude AI conversations  
**Total Size:** ~180 KB (5 files)  
**Source Export:** 2026-01-08

---

## Overview

This directory contains 5 markdown files specifically designed for upload to Claude Projects as knowledge base context. These files provide comprehensive, searchable documentation of the Zoho CRM configuration with cross-references and Claude-optimised anchors for citation.

## Files

| File | Size | Lines | Purpose |
|------|------|-------|---------|
| **SYSTEM_OVERVIEW.md** | 5.3 KB | 168 | Module catalogue, statistics, and relationship summary |
| **LATEST_CHANGES.md** | 5.6 KB | 212 | Human-readable diff between exports (2026-01-08 vs 2025-12-10) |
| **WORKFLOW_DEPENDENCY_MAP.md** | 73 KB | 3,191 | Impact analysis for workflow and field changes |
| **FIELD_REFERENCE.md** | 76 KB | 2,048 | Field specifications with picklist values and lookup targets |
| **CHANGE_PLANNING_GUIDE.md** | 8.5 KB | 292 | Best practices and checklists with real CRM examples |

## File Descriptions

### SYSTEM_OVERVIEW.md

**What it contains:**

- Executive summary (66 modules, 1,798 fields, 183 workflows)
- Tier 1 modules (10 core business modules) with full details
- Tier 2 modules (45 supporting modules) with summary stats
- Business domain groupings (Sales, Education, Tasks, etc.)
- Most referenced modules analysis
- Cross-references to other KB files

**Use for:**

- Getting module counts and statistics
- Understanding module relationships
- Finding which modules reference each other
- Quick CRM structure overview

### LATEST_CHANGES.md

**What it contains:**

- Comparison between 2026-01-08 and 2025-12-10 exports
- Executive summary of changes
- Field changes by module with picklist value deltas
- Workflow additions, removals, and modifications
- Lookup relationship changes
- Impact assessment notes

**Use for:**

- Understanding recent CRM configuration changes
- Learning from past modifications
- Identifying patterns in how the CRM evolves
- Examples for change planning

### WORKFLOW_DEPENDENCY_MAP.md

**What it contains:**

- 183 workflows across modules
- Risk assessment for each workflow (HIGH/MEDIUM/LOW)
- Trigger types and trigger fields
- Impact analysis ("If disabled..." scenarios)
- Outbound lookup relationships per module
- Table of contents with top 20 modules

**Use for:**

- **Impact analysis:** "If I change field X, what breaks?"
- **Workflow planning:** Understanding trigger dependencies
- **Risk assessment:** Identifying high-risk changes
- **Dependency mapping:** Finding cross-module effects

**Key features:**

- Risk indicators: 🔴 HIGH, 🟡 MEDIUM, 🟢 LOW
- Active/Inactive status: ✅ Active, ❌ Inactive
- Module-specific sections with anchors (e.g., `#module-leads`)
- Individual workflow anchors (e.g., `#leads-52330000000427010`)

### FIELD_REFERENCE.md

**What it contains:**

- 834 fields from 10 Tier 1 modules (full detail)
- 753 fields from 45 Tier 2 modules (summary only)
- Picklist values shown inline (critical for users)
- Lookup targets with arrow notation (→)
- Workflow usage indicators (🔄)
- Fields grouped by: Standard, Custom, Lookup

**Tier 1 modules (full detail):**

- Leads (151 fields)
- Contacts (113 fields)
- Accounts (61 fields)
- Deals (86 fields)
- Courses (137 fields)
- Registration_Records (78 fields)
- Invoices (57 fields)
- Quotes (40 fields)
- Call_Analytics (64 fields)
- Sales_Orders (47 fields)

**Use for:**

- Field lookups and specifications
- Finding picklist values
- Understanding lookup relationships
- Identifying custom vs standard fields
- Checking field requirements

### CHANGE_PLANNING_GUIDE.md

**What it contains:**

- Pre-change checklist (7 key areas)
- 4 common change scenarios with real examples:
  1. Adding a required field (Leads example)
  2. Modifying a workflow trigger (Courses workflow example)
  3. Changing picklist values (Recent Cold_Call_Tier change)
  4. Disabling a workflow (Impact analysis)
- Risk assessment quick reference table
- Testing recommendations (sandbox and production)
- Rollback guidance for fields, workflows, and picklists

**Use for:**

- Planning CRM configuration changes
- Understanding change risks
- Following best practices
- Learning rollback procedures
- Pre-change checklists

## Generation

### Command

Generate all 5 files:

```bash
python3 tools/generators/generate_ai_kb.py
```

Preview without writing:

```bash
python3 tools/generators/generate_ai_kb.py --dry-run
```

Use specific export date:

```bash
python3 tools/generators/generate_ai_kb.py --date 2026-01-08
```

Custom output directory:

```bash
python3 tools/generators/generate_ai_kb.py --output-dir /path/to/output
```

### Options

- `--date YYYY-MM-DD` - Export date (defaults to latest)
- `--diff-json PATH` - Path to export_diff_*.json (defaults to latest in reports/)
- `--dry-run` - Report what would be generated without writing files
- `--output-dir PATH` - Override output directory (default: ai_kb/)

### Integration with Pipeline

The AI KB generator is integrated into the main update pipeline:

```bash
python3 tools/update_pipeline.py --apply
```

This runs all pipeline steps including AI KB generation. To skip AI KB:

```bash
python3 tools/update_pipeline.py --apply --skip-ai-kb
```

## Data Sources

The generator uses three primary data sources:

1. **`models/CRM_DATA_MODEL.json`** (27,749 lines)
   - Consolidated data model built by `tools/processing/build_crm_data_model.py`
   - Module structure, field definitions, workflow metadata
   - Used by: All generators

2. **`data/exports/zoho-dependencies-*.json`**
   - Workflow dependencies with accurate trigger types
   - Field-to-workflow mappings
   - Lookup relationships
   - Used by: WORKFLOW_DEPENDENCY_MAP, FIELD_REFERENCE

3. **`reports/export_diff_*.json`**
   - Changes between exports
   - Recent field/workflow modifications
   - Used by: LATEST_CHANGES, CHANGE_PLANNING_GUIDE (for examples)

## Architecture

### Module Classification

Files use a tier-based approach to manage size:

- **Tier 1 (10 modules):** Always-include list + high-activity modules
  - Full field listings, picklist values, lookup details
  - Used in: FIELD_REFERENCE (full tables), WORKFLOW_DEPENDENCY_MAP (detailed)
  
- **Tier 2 (45 modules):** Supporting modules
  - Summary statistics, lookup fields only
  - Used in: FIELD_REFERENCE (summaries), WORKFLOW_DEPENDENCY_MAP (listed)

- **Excluded (5 modules):** Integration/system modules
  - Prefixes: `zohosign__*`, `clicksendext__*`
  - Suffix: `*_Insights__s`

### Cross-References

All files include cross-references to each other using consistent formatting:

```markdown
See WORKFLOW_DEPENDENCY_MAP.md for impact analysis
See FIELD_REFERENCE.md for field specifications
See CHANGE_PLANNING_GUIDE.md for best practices
```

### Claude-Optimised Anchors

Section anchors enable precise citation:

```markdown
## Executive Summary {#executive-summary}
### Leads {#module-leads}
#### Scenario A: Adding a Required Field {#scenario-required-field}
```

Claude can cite: "According to SYSTEM_OVERVIEW.md#executive-summary..."

## Size Budget

**Target:** 150-200 KB total  
**Actual:** ~180 KB

Individual file targets:

- SYSTEM_OVERVIEW.md: 5-10 KB → **~5 KB** ✅
- LATEST_CHANGES.md: 5-10 KB → **~5 KB** ✅
- WORKFLOW_DEPENDENCY_MAP.md: 60-80 KB → **~73 KB** (comprehensive detail)
- FIELD_REFERENCE.md: 60-80 KB → **~76 KB** ✅
- CHANGE_PLANNING_GUIDE.md: 10-15 KB → **~8 KB** ✅

**Note:** WORKFLOW_DEPENDENCY_MAP and FIELD_REFERENCE are detailed to support comprehensive AI analysis. Total size remains within reasonable context window limits.

## Usage with Claude Projects

### Complete Setup Guide

For detailed step-by-step instructions on setting up a Claude Project, see:

**[CLAUDE_PROJECT_SETUP.md](CLAUDE_PROJECT_SETUP.md)** - Comprehensive guide including:
- Project creation and configuration
- Recommended model settings (Opus 4.5)
- Custom instructions to copy/paste
- Example conversations and queries
- Power user tips
- Troubleshooting guide
- API access examples

### Quick Setup

1. Upload all 5 markdown files to your Claude Project
2. Enable "Project Knowledge" in conversation settings
3. Add custom instructions from `CLAUDE_PROJECT_SETUP.md`
4. Query the knowledge base naturally

### Example Queries

**System overview:**

- "What modules exist in the CRM?"
- "How many workflows are in the Courses module?"
- "Which modules reference Accounts?"

**Change planning:**

- "I want to add a required field to Leads. What should I check first?"
- "What happens if I disable a workflow?"
- "How do I safely remove a picklist value?"

**Impact analysis:**

- "If I change the Lead_Status field, what workflows will break?"
- "What fields trigger workflows in the Courses module?"
- "Show me all workflows with cross-module actions"

**Field lookups:**

- "What are the picklist values for Cold_Call_Tier?"
- "Which fields in Leads are lookups?"
- "Is Email_Address a required field in Contacts?"

## Technical Implementation

### Generator Functions

**File:** `tools/generators/generate_ai_kb.py` (~1,600 lines)

**Main generators:**

1. `generate_system_overview()` - Module catalogue and stats
2. `generate_latest_changes()` - Human-readable diff
3. `generate_workflow_dependency_map()` - Impact analysis
4. `generate_field_reference()` - Field specifications
5. `generate_change_planning_guide()` - Best practices

**Helper functions:**

- `classify_modules()` - Tier 1/2/excluded classification
- `build_field_workflow_index()` - Reverse index: field → workflows
- `assess_workflow_risk()` - HIGH/MEDIUM/LOW risk assessment
- `get_latest_diff()` - Auto-discover latest diff file

### Update History

**8 January 2026:**

- Initial implementation complete
- All 5 files generated and tested
- Integrated into update pipeline
- Updated with 2026-01-08 export data
- Total size: ~180 KB
- Source export: 2026-01-08

## Maintenance

### When to Regenerate

Regenerate the AI KB when:

1. New Zoho export is processed
2. Significant configuration changes occur
3. Major workflow modifications are made
4. Module structure changes (added/removed modules)

### Regeneration Frequency

**Recommended:** After each export processing (monthly or as-needed)

**Command:**

```bash
python3 tools/update_pipeline.py --apply
```

This ensures the AI KB reflects the latest CRM configuration.

### Manual Updates

The KB files are auto-generated and should **not** be manually edited. Instead:

- Update source data models if corrections are needed
- Regenerate using `generate_ai_kb.py`
- For temporary notes, use separate documentation files

## Troubleshooting

### Generator fails with "CRM_DATA_MODEL.json not found"

**Solution:** Run the data model builder first:

```bash
python3 tools/processing/build_crm_data_model.py --date 2026-01-08
```

### Files are larger than expected

**Cause:** More workflows/fields than estimated  
**Solution:** This is normal. The 150 KB budget has 2.8 KB headroom. If files exceed 150 KB significantly, consider:

- Reducing Tier 1 module count
- Shortening picklist value displays
- Summarising more Tier 2 modules

### Diff file not found

**Solution:** Generate diff first:

```bash
python3 tools/processing/compare_exports.py --new-date 2026-01-08 --old-date 2025-12-10
```

Or run full pipeline:

```bash
python3 tools/update_pipeline.py --apply
```

### Picklist values not showing

**Cause:** Field data format variation  
**Solution:** The generator handles both dict and string picklist formats. If values still don't show, check field structure in `CRM_DATA_MODEL.json`.

## Future Enhancements

Possible future additions (not yet implemented):

1. **Interactive filtering:** Generate filtered versions for specific modules
2. **Change highlights:** Auto-highlight recent changes in field reference
3. **Workflow visualisation:** Generate Mermaid diagrams of workflow chains
4. **API integration:** Direct Zoho API queries for real-time data
5. **Version comparison:** Compare multiple historical exports
6. **Custom tier definitions:** User-configurable module tiers

## Contact & Support

For questions about the AI KB:

1. Check this README
2. Review `CLAUDE_PROJECT_SETUP.md` for Claude Projects setup
3. Review `tools/generators/generate_ai_kb.py` source code
4. Consult main project README: `../README.md`
5. Check pipeline documentation: `tools/update_pipeline.py`

---

*Last updated: 8 January 2026*  
*Generator version: 1.0*  
*Python 3.x required*
