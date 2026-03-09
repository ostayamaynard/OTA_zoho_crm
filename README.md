# Zoho CRM Source Data

This repository contains the raw source of truth for Zoho CRM data model and dependencies, along with comprehensive module documentation.

## 🚀 Start Here

Welcome to the Zoho CRM Source Data repository. This repo is organized to help you quickly find documentation, data models, and tools.

### 📂 Directory Structure

* **`ai_kb/`**: AI Knowledge Base for Claude Projects (5 optimised markdown files, ~180KB total).
* **`data/exports/`**: Zoho CRM export files (JSON data models and dependencies).
* **`modules/`**: The core documentation. Contains fields, workflows, and diagrams for each CRM module (Leads, Deals, etc.).
* **`models/`**: Centralized data model definitions.
* **`tools/`**: Python scripts organized by function:
  * `tools/generators/`: Documentation generation scripts.
  * `tools/validators/`: Validation and audit scripts.
  * `tools/processing/`: Data processing and comparison scripts.
  * `tools/export_client/`: Zoho CRM export client package.
  * `tools/kanban/`: Kanban diagram generators.
  * `tools/utils/`: Helper utilities (e.g., PDF conversion, file discovery).
* **`docs/`**: General documentation, reports, and standards.
* **`reports/`**: Generated audit reports and export diffs.
* **`sops/`**: Standard Operating Procedures (raw and processed).

### 🔍 Quick Links

* **[Logic Index](LOGIC_INDEX.md)**: Master index of all system logic.
* **[System Overview](modules/overview/docs/overview-readme.md)**: High-level architecture and integration points.
* **[Repository Inventory](REPOSITORY_INVENTORY.md)**: Detailed list of all files.

---

## Source Files

* Latest export: `data/exports/zoho-data-model-2026-01-08.json`
* Latest dependencies: `data/exports/zoho-dependencies-2026-01-08.json`
* Date-agnostic access: see `tools/utils/file_discovery.py` and `tools/update_pipeline.py`
* Export client: `tools/export_client/` (for generating new exports from Zoho CRM)
* Polymorphic lookup targets (expected, not first-class modules): `se_module`, `Email_Template__s`

## Usage

These files are the authoritative source for:

* Module structure and field definitions
* Workflow dependencies
* Relationship mappings
* Data model documentation

## Project Goals (for humans and AI helpers)

* Keep an accurate, date-agnostic mirror of the Zoho CRM configuration (modules, fields, workflows, lookups).

* Generate human-friendly docs/diagrams from raw exports.
* Surface deltas between exports so changes are visible before docs are refreshed.
* Preserve curated journey/process content separately so it is never overwritten automatically.

## Update Workflow (what to run)

Preferred one-command flow (latest export by default):

```bash
python tools/update_pipeline.py --apply
```

Typical with explicit dates:

```bash
python tools/update_pipeline.py --apply --date 2026-01-08 --previous-date 2025-12-10
```

What it does:

1) Diff exports → `reports/export_diff_<new>_vs_<old>.{json,md}`
2) Rebuild central model → `models/CRM_DATA_MODEL.{json,md}`
3) Generate AI Knowledge Base → `ai_kb/*.md` (skip with `--skip-ai-kb`)
4) Extract workflow summary → `reports/workflow_extraction_report_<date>.json`
5) Regenerate module docs (fields/workflows/usage/status-map)
6) Regenerate diagrams (skip with `--skip-diagrams`)
7) Validate data → `tools/validators/validate_data.py`
8) Emit manual review checklist → `reports/manual_review_<new>_vs_<old>.md`

## 🚀 Quick Start for New Team Members

**Adding a new Zoho export:**

1. Export from Zoho CRM using the export client:
   ```bash
   cd tools/export_client
   python3 zoho_export.py
   ```
   This will create files in `data/exports/`:
   * `zoho-data-model-YYYY-MM-DD.json`
   * `zoho-dependencies-YYYY-MM-DD.json`
2. Run the pipeline: `python3 tools/update_pipeline.py --apply`
3. Review the diff report: `reports/export_diff_<new>_vs_<old>.md`
4. Review the manual checklist: `reports/manual_review_<new>_vs_<old>.md`
5. Commit your changes

**Example of a clean diff report (this is what "good" looks like):**

```
## Executive Summary

| Category              | Count |
|-----------------------|-------|
| Modules Added         | 2     |
| Modules Removed       | 0     |
| Modules with Changes  | 3     |
| Total Field Changes   | 5     |
| Total Workflow Changes| 4     |
```

If your diff has dozens of `last_executed_time updated` entries, something is wrong—the pipeline should filter those out by default.

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `command not found: python` | Use `python3` instead, or activate your virtual environment |
| Diff shows hundreds of `last_executed_time` changes | You may be using an old version of `compare_exports.py`; pull latest |
| Status-map docs show old dates | Run the full pipeline with `--apply` to regenerate all docs |
| Pipeline fails mid-run | Check the error message—pipeline aborts on first failure. Fix the issue and re-run. |
| Curated files were overwritten | This should NOT happen. The pipeline never writes to `modules/*/data/*.json` unless `--write-journey` is passed |

Key standalone commands:

* Diff only: `python tools/processing/compare_exports.py --new-date YYYY-MM-DD --old-date YYYY-MM-DD`
* Validate only: `python tools/validators/validate_data.py --date YYYY-MM-DD`
* Docs only: `python tools/generators/generate_module_docs.py --date YYYY-MM-DD`
* AI KB only: `python tools/generators/generate_ai_kb.py` (see `ai_kb/README.md`)
* Export from Zoho: `cd tools/export_client && python3 zoho_export.py`

## Auto-generated vs curated (what is NOT overwritten)

* Auto-generated:
  * `models/CRM_DATA_MODEL.{json,md}`
  * `modules/*/docs/*` (fields/workflows/status/usage)
  * `modules/*/diagrams/*.mmd`
  * `reports/export_diff_*.{json,md}`, `reports/workflow_extraction_report_*.json`
  * `reports/manual_review_*.md` (checklist)

* Curated/manual (never overwritten; review after changes):
  * `modules/*/data/customer-journey-*.json`
  * `modules/*/data/*-stages-kanban.json`
  * SOPs and data-flow docs under `docs/` and `sops/`
  * Any bespoke narrative or process documentation

## Manual review checklist

After each pipeline run, open `reports/manual_review_<new>_vs_<old>.md`. For every module with changes, it reminds you to review the curated journey and stage JSONs and related SOPs.

## Module Documentation

### Documentation Status

| Module | Fields | Workflows | Status |
|--------|--------|-----------|--------|
| Leads | 151 | 20 | ✅ Complete |
| Deals | 86 | 20 | ✅ Complete |
| Invoices | 57 | 16 | ✅ Complete |
| Quotes | 40 | 9 | ✅ Complete |
| Venues | 23 | 0 | ✅ Complete |
| Contacts | 113 | 7 | ✅ Complete |
| Accounts | 61 | 4 | ✅ Complete |
| Courses | 137 | 37 | ✅ Complete |
| Registration_Records | 78 | 36 | ✅ Complete |

### Module Directories

Each documented module follows the standard structure:

```
modules/{module_name}/
├── data/           # JSON data files
├── diagrams/       # Mermaid diagrams
└── docs/           # Markdown documentation
```

### Key Documentation Files

* `{module}-fields.md` - Complete field reference
* `{module}-workflows.md` - Workflow details with URLs
* `{module}-status-map.md` - Status/stage picklist mapping
* `{module}-usage.md` - Usage guide and best practices

## Documentation Standards

See `docs/module-documentation-standard.md` for the complete documentation standard including:

* Required file structure
* Template formats
* Data extraction process
* Field impact analysis guidelines

## System Overview

See `modules/overview/docs/overview-readme.md` for:

* Complete module inventory
* System architecture
* Integration points
* Workflow summary

## AI Knowledge Base (Added: 2026-01-08)

A complete AI Knowledge Base optimised for Claude Projects has been generated in `ai_kb/`. These 5 markdown files (180 KB total) provide:

* **SYSTEM_OVERVIEW.md** - Module catalogue and statistics
* **LATEST_CHANGES.md** - Human-readable diff between exports
* **WORKFLOW_DEPENDENCY_MAP.md** - Impact analysis for workflow/field changes
* **FIELD_REFERENCE.md** - Field specifications with picklist values
* **CHANGE_PLANNING_GUIDE.md** - Best practices with real CRM examples

**Generate/update:** `python3 tools/generators/generate_ai_kb.py`

See `ai_kb/README.md` for complete documentation.

## Export Date

**2026-01-08** (see `reports/export_diff_2026-01-08_vs_2025-12-10.md` for changes)

---

*Generated from Zoho CRM instance: <https://crm.zoho.com.au/crm/org7003757385>*
