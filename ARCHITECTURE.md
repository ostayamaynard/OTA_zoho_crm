# Architecture and Data Flow

## Source of Truth
- Zoho API exports (metadata):
  - `data/exports/zoho-data-model-YYYY-MM-DD.json`
  - `data/exports/zoho-dependencies-YYYY-MM-DD.json`
- Export client: `tools/export_client/zoho_export.py` (for generating new exports)

## Orchestrated Pipeline (`tools/update_pipeline.py`)
```
ZOHO API export → data/exports/*.json
    → tools/processing/compare_exports.py → reports/export_diff_*.{json,md} + reports/manual_review_*.md
    → tools/processing/build_crm_data_model.py → models/CRM_DATA_MODEL.{json,md}
    → tools/processing/extract_workflows.py → reports/workflow_extraction_report_*.json
    → tools/generators/generate_ai_kb.py → ai_kb/*.md
    → tools/generators/generate_module_docs.py → modules/*/docs/*-{fields,workflows,workflow-urls,usage}.md
    → tools/kanban/json_to_mermaid.py → modules/*/diagrams/*.mmd, docs/mermaid-readme.md
    → tools/validators/validate_data.py → console validation (lookup/field checks)
```

## Auto-Generated (overwritten by pipeline)
- `models/CRM_DATA_MODEL.{json,md}`
- `modules/*/docs/*-{fields,workflows,workflow-urls,usage}.md`
- `modules/*/diagrams/*.mmd`
- `reports/export_diff_*.{json,md}`
- `reports/workflow_extraction_report_*.json`
- `reports/manual_review_*.md`
- `docs/mermaid-readme.md`

## Curated / Manual (never overwritten)
- `modules/*/data/customer-journey-*.json`
- `modules/*/data/*-stages-kanban.json`
- `modules/overview/data/lucid-workflow*.json` (legacy)
- SOPs under `sops/`
- Cross-module flows: `docs/data-flows/*.md`
- Root docs: `README.md`, `LOGIC_INDEX.md`, `GLOSSARY.md`

## Reports
- Current: `reports/export_diff_<new>_vs_<old>.{json,md}`
- Current: `reports/workflow_extraction_report_<date>.json`
- Checklist: `reports/manual_review_<new>_vs_<old>.md`

## Manual Review Checklist
- Produced each run: `reports/manual_review_<new>_vs_<old>.md`
- Review curated files per changed module: journey JSONs, kanban stages, SOPs.

## Deprecated / Archived
- Stale one-off docs moved to `archive/docs/`
- Unused scripts moved to `archive/tools/`
- Legacy exports under `archive/zoho_export_snapshots/`

## How to Update Everything
```
python tools/update_pipeline.py --apply --date YYYY-MM-DD --previous-date <old>
```
Optional flags: `--skip-diagrams`, `--skip-docs`, `--skip-workflows`, `--skip-validate`, `--skip-manual-review`.

## Validation
- `python tools/validators/validate_data.py --date YYYY-MM-DD`
  - Checks fields, lookups, duplicate field names
  - Allowed polymorphic lookups: `se_module`, `Email_Template__s`
