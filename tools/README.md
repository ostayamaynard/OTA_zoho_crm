# Tools Directory - Developer Guide

This directory contains Python scripts for processing Zoho CRM exports, generating documentation, and maintaining the repository.

---

## 📂 Directory Structure

```
tools/
├── generators/         # Documentation and AI KB generators
├── validators/         # Validation and audit scripts
├── processing/         # Data processing and comparison
├── export_client/      # Zoho CRM export client package
├── kanban/             # Kanban diagram generators
├── utils/              # Shared utilities
└── update_pipeline.py  # Main orchestrator (run this!)
```

---

## 🚀 Quick Start - Most Common Workflow

### For Regular Updates (When You Get New Zoho Exports)

**Step 1:** Get fresh export data from Zoho CRM
```bash
cd tools/export_client
python3 zoho_export.py
cd ../..
```
This creates files in `data/exports/zoho-data-model-YYYY-MM-DD.json` and `zoho-dependencies-YYYY-MM-DD.json`

**Step 2:** Run the full pipeline (does everything automatically)
```bash
python3 tools/update_pipeline.py --apply
```

**Step 3:** Review the changes
```bash
cat reports/export_diff_<new>_vs_<old>.md
cat reports/manual_review_<new>_vs_<old>.md
```

**That's it!** The pipeline updates all documentation, generates reports, and validates data.

---

## 📋 Main Pipeline Tool

### `update_pipeline.py` - The Orchestrator

**What it does:** Runs all processing steps in the correct order.

**Basic usage:**
```bash
# Dry run (shows what would be done)
python3 tools/update_pipeline.py

# Apply changes (actually update files)
python3 tools/update_pipeline.py --apply

# Use specific export date
python3 tools/update_pipeline.py --apply --date 2026-01-08

# Skip specific steps
python3 tools/update_pipeline.py --apply --skip-diagrams --skip-ai-kb
```

**Pipeline Steps (in order):**

1. **Compare Exports** → `reports/export_diff_*.{json,md}`
2. **Build Data Model** → `models/CRM_DATA_MODEL.json`
3. **Generate AI KB** → `ai_kb/*.md` (5 files)
4. **Extract Workflows** → `reports/workflow_extraction_report_*.json`
5. **Generate Module Docs** → `modules/*/docs/*.md`
6. **Generate Diagrams** → `modules/*/diagrams/*.mmd`
7. **Validate Data** → Console output
8. **Create Manual Review Checklist** → `reports/manual_review_*.md`

**Options:**
- `--date YYYY-MM-DD` - Export date to process (defaults to latest)
- `--previous-date YYYY-MM-DD` - Previous export for comparison (defaults to auto-select)
- `--apply` - Execute changes (without this, it's a dry run)
- `--skip-diagrams` - Skip Mermaid diagram regeneration
- `--skip-docs` - Skip module documentation generation
- `--skip-workflows` - Skip workflow extraction
- `--skip-validate` - Skip data validation
- `--skip-manual-review` - Skip manual review checklist
- `--skip-ai-kb` - Skip AI Knowledge Base generation

---

## 🏭 Generators

### `generators/generate_module_docs.py`

**Purpose:** Generate documentation for all CRM modules

**Generates:**
- `modules/*/docs/*-fields.md` - Complete field listings
- `modules/*/docs/*-workflows.md` - Workflow details
- `modules/*/docs/*-workflow-urls.md` - Clickable workflow URLs
- `modules/*/docs/*-usage.md` - Usage guides
- `modules/*/docs/*-status-map.md` - Status/picklist mappings

**Usage:**
```bash
# Generate for all modules (latest export)
python3 tools/generators/generate_module_docs.py --date 2026-01-08

# Dry run (show what would be generated)
python3 tools/generators/generate_module_docs.py --date 2026-01-08 --dry-run
```

**When to run:** After new Zoho exports (automatically done by pipeline)

---

### `generators/generate_ai_kb.py`

**Purpose:** Generate AI Knowledge Base for Claude Projects

**Generates:** 5 optimized markdown files in `ai_kb/`:
- `SYSTEM_OVERVIEW.md` - Module catalog and stats
- `LATEST_CHANGES.md` - Human-readable diff
- `WORKFLOW_DEPENDENCY_MAP.md` - Impact analysis (73KB)
- `FIELD_REFERENCE.md` - Field specifications (76KB)
- `CHANGE_PLANNING_GUIDE.md` - Best practices

**Usage:**
```bash
# Generate all 5 files
python3 tools/generators/generate_ai_kb.py

# Preview without writing
python3 tools/generators/generate_ai_kb.py --dry-run

# Use specific export date
python3 tools/generators/generate_ai_kb.py --date 2026-01-08

# Custom output directory
python3 tools/generators/generate_ai_kb.py --output-dir /path/to/output
```

**When to run:** After export updates (automatically done by pipeline)

**Total size:** ~180KB (5 files)

---

### `generators/add_workflow_urls.py`

**Purpose:** Add clickable Zoho CRM workflow URLs to documentation

**What it does:**
- Scans all module documentation
- Adds URLs for workflow IDs found in the export
- Updates `*-workflow-urls.md` files

**Usage:**
```bash
# Dry run (show what would be added)
python3 tools/generators/add_workflow_urls.py

# Apply changes
python3 tools/generators/add_workflow_urls.py --apply

# Specific export date
python3 tools/generators/add_workflow_urls.py --date 2026-01-08 --apply
```

**When to run:** After workflows change in Zoho CRM

---

## 🔍 Validators

### `validators/validate_data.py`

**Purpose:** Validate Zoho export data integrity

**Checks:**
- Schema presence (modules, fields, workflows)
- Duplicate field names per module
- Lookup relationships (target modules/fields exist)
- Summary counts

**Usage:**
```bash
# Validate latest export
python3 tools/validators/validate_data.py

# Validate specific date
python3 tools/validators/validate_data.py --date 2026-01-08
```

**When to run:** After each export (automatically done by pipeline)

**Known valid polymorphic lookups:** `se_module`, `Email_Template__s`

---

### `validators/audit_mermaid_syntax.py`

**Purpose:** Validate Mermaid diagram syntax

**Checks:**
- Valid Mermaid syntax
- Node naming (no spaces in IDs)
- Special character handling
- Reserved keyword usage

**Usage:**
```bash
# Audit all .mmd files
python3 tools/validators/audit_mermaid_syntax.py

# Generate report
python3 tools/validators/audit_mermaid_syntax.py --output-report audit_report.json
```

**When to run:** After diagram generation or manual edits

---

### `validators/verify_extra_workflows.py`

**Purpose:** Verify extra workflows identified during audits

**What it does:**
- Cross-references workflow IDs from multiple sources
- Identifies workflows present in CRM but missing from docs
- Validates workflow existence across all export sections

**Usage:**
```bash
# Verify workflows
python3 tools/validators/verify_extra_workflows.py

# Specific export date
python3 tools/validators/verify_extra_workflows.py --date 2026-01-08
```

**When to run:** During manual audits or workflow reconciliation

---

## ⚙️ Processing

### `processing/compare_exports.py`

**Purpose:** Compare two Zoho export snapshots and generate diff reports

**Generates:**
- `reports/export_diff_<new>_vs_<old>.json` - Machine-readable diff
- `reports/export_diff_<new>_vs_<old>.md` - Human-readable report

**Usage:**
```bash
# Compare latest two exports (auto-discovery)
python3 tools/processing/compare_exports.py

# Compare specific dates
python3 tools/processing/compare_exports.py --new-date 2026-01-08 --old-date 2025-12-10

# Custom output location
python3 tools/processing/compare_exports.py --output-dir custom_reports/
```

**When to run:** After each new export (automatically done by pipeline)

**Reports include:**
- Module additions/removals
- Field changes (added, removed, modified)
- Workflow changes
- Picklist value differences
- Lookup relationship changes

---

### `processing/build_crm_data_model.py`

**Purpose:** Build consolidated CRM data model from exports

**Generates:**
- `models/CRM_DATA_MODEL.json` - Complete data model
- `models/CRM_DATA_MODEL_SUMMARY.md` - Human-readable summary

**Usage:**
```bash
# Build from latest export
python3 tools/processing/build_crm_data_model.py

# Build from specific date
python3 tools/processing/build_crm_data_model.py --date 2026-01-08

# Custom output location
python3 tools/processing/build_crm_data_model.py --output models/custom_model.json
```

**When to run:** After each export (automatically done by pipeline)

**Data sources:**
- `data/exports/zoho-data-model-*.json`
- `data/exports/zoho-dependencies-*.json`

---

### `processing/extract_model_details.py`

**Purpose:** Extract specific field details from exports

**Usage:**
```bash
# Extract specific field
python3 tools/processing/extract_model_details.py Leads Email

# Use specific export
python3 tools/processing/extract_model_details.py --date 2026-01-08 Deals Amount
```

**When to run:** Ad-hoc queries for specific field information

---

### `processing/extract_workflows.py`

**Purpose:** Extract workflow information from dependencies JSON

**Generates:**
- `reports/workflow_extraction_report_<date>.json`

**Usage:**
```bash
# Extract from latest export
python3 tools/processing/extract_workflows.py

# Extract from specific date
python3 tools/processing/extract_workflows.py --date 2026-01-08

# Custom output
python3 tools/processing/extract_workflows.py --output custom_report.json
```

**When to run:** After each export (automatically done by pipeline)

---

## 🎨 Kanban Generators

### `kanban/generate_deal_kanban_mermaid.py`

**Purpose:** Generate Kanban-style flowchart for Deal stages

**Generates:**
- `modules/deals/diagrams/deal-kanban-detailed.mmd` - Full diagram with URLs
- Various other Deal kanban views

**Usage:**
```bash
python3 tools/kanban/generate_deal_kanban_mermaid.py
```

**When to run:** After Deal stage changes

---

### `kanban/json_to_mermaid.py`

**Purpose:** Convert customer journey JSON to Mermaid diagrams

**Generates:**
- Multiple `.mmd` files in `modules/*/diagrams/`
- `docs/mermaid-readme.md` - Rendering instructions

**Reads from:**
- `modules/*/data/customer-journey-*.json`
- `modules/*/data/*-stages-kanban.json`

**Usage:**
```bash
# Generate all diagrams
python3 tools/kanban/json_to_mermaid.py

# Generate specific module
python3 tools/kanban/json_to_mermaid.py --module deals
```

**When to run:** After journey JSON updates (automatically done by pipeline)

---

## 🔧 Utilities

### `utils/file_discovery.py`

**Purpose:** Date-agnostic export file discovery

**Functions:**
- `list_exports()` - List all exports sorted by date
- `get_latest_export()` - Get most recent export
- `get_latest_two_exports()` - Get latest pair for diffing
- `get_export_by_date(date)` - Get specific export
- `export_directory()` - Get export directory path

**Usage:**
```python
from tools.utils.file_discovery import get_latest_export, export_directory

# Get latest export
export = get_latest_export()
print(export.data_model)  # Path to data model JSON
print(export.dependencies)  # Path to dependencies JSON
print(export.date)  # Export date (YYYY-MM-DD)

# Get export directory
dir_path = export_directory()
```

**Export location:** `data/exports/`

---

### `utils/convert_md_to_pdf.py`

**Purpose:** Convert Markdown files to PDF using ReportLab

**Usage:**
```python
from tools.utils.convert_md_to_pdf import parse_markdown_to_pdf

parse_markdown_to_pdf('input.md', 'output.pdf')
```

**When to run:** Ad-hoc for PDF generation needs

---

## 📦 Export Client

### `export_client/` Directory

**Purpose:** Self-contained package for exporting Zoho CRM metadata

**Main scripts:**
- `zoho_export.py` - Main export script
- `zoho_export_v3.py` - Enhanced version

**See:** `tools/export_client/README.md` for complete documentation

**Quick usage:**
```bash
cd tools/export_client
python3 zoho_export.py
```

**Generates:**
- `data/exports/zoho-data-model-YYYY-MM-DD.json`
- `data/exports/zoho-dependencies-YYYY-MM-DD.json`
- `tools/export_client/Zoho_CRM_Data_Model_YYYY-MM-DD.xlsx` (stays here)

**Requirements:**
- Python 3.7+
- `.env` file with Zoho credentials
- See `requirements.txt`

---

## 📊 Typical Workflow Sequences

### 1. Monthly Export Update

```bash
# 1. Export from Zoho CRM
cd tools/export_client
python3 zoho_export.py
cd ../..

# 2. Run full pipeline
python3 tools/update_pipeline.py --apply

# 3. Review changes
cat reports/export_diff_<new>_vs_<old>.md
cat reports/manual_review_<new>_vs_<old>.md

# 4. Commit changes
git add .
git commit -m "Update CRM exports: YYYY-MM-DD"
```

### 2. Documentation Only (No New Export)

```bash
# Regenerate docs from existing export
python3 tools/generators/generate_module_docs.py --date 2026-01-08
```

### 3. Diagram Only

```bash
# Regenerate diagrams from journey JSONs
python3 tools/kanban/json_to_mermaid.py
```

### 4. AI KB Only

```bash
# Regenerate AI Knowledge Base
python3 tools/generators/generate_ai_kb.py
```

### 5. Quick Validation

```bash
# Validate latest export
python3 tools/validators/validate_data.py

# Audit Mermaid syntax
python3 tools/validators/audit_mermaid_syntax.py
```

### 6. Compare Two Exports

```bash
# Generate diff report
python3 tools/processing/compare_exports.py \
  --new-date 2026-01-08 \
  --old-date 2025-12-10
```

---

## 🎯 When to Run Each Tool

| Tool | Frequency | Trigger |
|------|-----------|---------|
| `update_pipeline.py` | Monthly | After new Zoho export |
| `export_client/zoho_export.py` | Monthly | To get latest CRM config |
| `compare_exports.py` | Monthly | After new export |
| `generate_module_docs.py` | Monthly | After export (auto in pipeline) |
| `generate_ai_kb.py` | Monthly | After export (auto in pipeline) |
| `validate_data.py` | Monthly | After export (auto in pipeline) |
| `json_to_mermaid.py` | As needed | After journey JSON edits |
| `add_workflow_urls.py` | As needed | After workflow changes |
| `audit_mermaid_syntax.py` | As needed | After diagram edits |
| `extract_model_details.py` | Ad-hoc | For specific queries |

---

## 💡 Pro Tips

1. **Always use --dry-run first** when testing new commands
2. **Review diff reports** before committing export updates
3. **Check manual_review checklist** after pipeline runs
4. **Validate after major changes** using validators
5. **Keep journey JSONs updated** when business processes change
6. **Use file_discovery utilities** instead of hardcoding dates
7. **Run full pipeline** rather than individual tools when possible

---

## 🐛 Troubleshooting

### "No export found"
```bash
# List available exports
python3 -c "from tools.utils.file_discovery import list_exports; print('\n'.join(e.date for e in list_exports()))"
```

### "Module not found"
```bash
# Ensure you're in repo root
cd /path/to/zoho_crm
python3 tools/update_pipeline.py --apply
```

### "Permission denied"
```bash
# Make scripts executable (Mac/Linux)
chmod +x tools/export_client/run_export.sh
```

### Pipeline fails mid-run
- Check error message - pipeline aborts on first failure
- Fix the issue and re-run
- Use --skip-* flags to bypass problem steps temporarily

---

## 📚 Additional Documentation

- **Main README:** `../README.md` - Repository overview
- **Architecture:** `../ARCHITECTURE.md` - Data flow and architecture
- **AI KB Documentation:** `../ai_kb/README.md` - AI Knowledge Base details
- **Export Client:** `export_client/README.md` - Zoho export instructions
- **Module Standards:** `../docs/module-documentation-standard.md` - Documentation standards
- **Update Guide:** `../docs/UPDATE_DEPENDENCIES.md` - What to update when

---

## 🔗 Quick Reference

**Export Data Location:** `data/exports/`  
**Reports Location:** `reports/`  
**Module Docs:** `modules/*/docs/`  
**AI KB:** `ai_kb/`  
**Models:** `models/`

**Python Version:** 3.7+  
**Main Command:** `python3 tools/update_pipeline.py --apply`

---

*Last Updated: 2026-01-08*  
*Repository: Zoho CRM Source Data*
