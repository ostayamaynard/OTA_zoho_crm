---
description: What to update when new Zoho exports arrive
globs: tools/**, docs/**, modules/**
alwaysApply: false
---

## Inputs
- Export JSONs in `data/exports/`  
  - `zoho-data-model-YYYY-MM-DD.json`  
  - `zoho-dependencies-YYYY-MM-DD.json`
- Generate new exports: `cd tools/export_client && python3 zoho_export.py`

## One-Command Update
- Dry run: `python tools/update_pipeline.py --date YYYY-MM-DD`
- Apply: `python tools/update_pipeline.py --apply --date YYYY-MM-DD`
- Diff only: `python tools/processing/compare_exports.py --new-date YYYY-MM-DD --old-date <previous>`

## Automatically Regenerated
- `models/CRM_DATA_MODEL.json`, `CRM_DATA_MODEL_SUMMARY.md`
- `modules/*/docs/*-{fields,workflows,workflow-urls,usage}.md`
- `modules/*/diagrams/*.mmd` (from curated journey JSONs)
- `reports/export_diff_<new>_vs_<old>.{json,md}`
- `reports/workflow_extraction_report_<date>.json`
- `reports/manual_review_<new>_vs_<old>.md` (checklist of curated files to inspect)

## Manual / Curated (Review after exports)
- `modules/*/data/customer-journey-*.json`
- `modules/*/data/*-stages-kanban.json`
- SOPs in `sops/` that reference workflow IDs
- High-level docs that cite specific export dates (e.g., `LOGIC_INDEX.md`, `mermaid-readme.md`)

## Validation
- `python tools/validators/validate_data.py --date YYYY-MM-DD`
  - Checks duplicate fields, missing ids, lookup targets
- Allowed polymorphic lookup targets: `se_module`, `Email_Template__s`

## Notes
- File discovery is date-agnostic via `tools/utils/file_discovery.py`
- Export data stored in `data/exports/` (separated from scripts)
- `tools/generators/add_workflow_urls.py` runs in dry-run by default; use `--apply` to write
- Avoid overwriting curated journey JSONs unless intentionally refreshed
