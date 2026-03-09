#!/usr/bin/env python3
"""
Validation helper for Zoho CRM exports.

What it checks:
- Basic schema presence for modules, fields, workflows
- Duplicate field names per module
- Lookup relationships reference existing modules/fields
- Summary counts (modules/fields/workflows)

Usage:
  python tools/inspection/validate_data.py          # latest export
  python tools/inspection/validate_data.py --date 2025-12-10
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple
import sys

TOOLS_DIR = Path(__file__).resolve().parents[1]
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import ExportFiles, get_export_by_date, get_latest_export

# Polymorphic or external lookup targets that may not appear as modules in the export.
ALLOWED_EXTERNAL_LOOKUPS = {"se_module", "Email_Template__s"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Zoho export integrity")
    parser.add_argument("--date", help="Export date (YYYY-MM-DD). Defaults to latest export.")
    parser.add_argument("--json", action="store_true", help="Emit JSON report instead of human-readable text")
    return parser.parse_args()


def load_export(date: str | None) -> Tuple[ExportFiles, dict, dict]:
    export = get_export_by_date(date, None).ensure_both() if date else get_latest_export().ensure_both()
    data_model = json.loads(export.data_model.read_text())
    dependencies = json.loads(export.dependencies.read_text())
    return export, data_model, dependencies


def validate_modules(data_model: dict) -> Tuple[Dict[str, int], List[str]]:
    issues: List[str] = []
    module_count = len(data_model)
    field_total = 0
    workflow_total = 0

    for module_name, module in data_model.items():
        fields = module.get("fields", [])
        workflows = module.get("workflows", [])
        field_total += len(fields)
        workflow_total += len(workflows)

        if not isinstance(fields, list):
            issues.append(f"{module_name}: fields is not a list")
            continue

        api_names = [f.get("api_name") for f in fields if f.get("api_name")]
        duplicates = [name for name, count in Counter(api_names).items() if count > 1]
        if duplicates:
            issues.append(f"{module_name}: duplicate field api_name(s): {', '.join(duplicates)}")

        for field in fields:
            if not field.get("api_name"):
                issues.append(f"{module_name}: field missing api_name")
            if not field.get("data_type"):
                issues.append(f"{module_name}: field {field.get('api_name')} missing data_type")

        for wf in workflows:
            if not wf.get("id"):
                issues.append(f"{module_name}: workflow missing id ({wf.get('name')})")
            if not wf.get("name"):
                issues.append(f"{module_name}: workflow missing name ({wf.get('id')})")

    stats = {
        "modules": module_count,
        "fields": field_total,
        "workflows": workflow_total,
    }
    return stats, issues


def validate_lookup_relationships(dependencies: dict, data_model: dict) -> List[str]:
    issues: List[str] = []
    lookup_rel = dependencies.get("lookup_relationships") or {}
    for module_name, rels in lookup_rel.items():
        if module_name not in data_model:
            issues.append(f"Lookup module missing from data model: {module_name}")
            continue
        fields = {f.get("api_name") for f in data_model[module_name].get("fields", [])}
        for rel in rels:
            field_name = rel.get("field_name")
            target = rel.get("lookup_module")
            if field_name and field_name not in fields:
                issues.append(f"{module_name}: lookup field '{field_name}' not found in module fields")
            if target and target not in data_model and target not in ALLOWED_EXTERNAL_LOOKUPS:
                issues.append(f"{module_name}: lookup target '{target}' not found as module")
    return issues


def render_text(export: ExportFiles, stats: Dict[str, int], issues: List[str]) -> str:
    lines = [
        f"Validated export {export.date}",
        f"Modules: {stats['modules']}, Fields: {stats['fields']}, Workflows: {stats['workflows']}",
    ]
    if issues:
        lines.append("Issues:")
        lines.extend(f"- {issue}" for issue in issues)
    else:
        lines.append("No issues found.")
    return "\n".join(lines)


def main():
    args = parse_args()
    export, data_model, dependencies = load_export(args.date)

    stats, module_issues = validate_modules(data_model)
    lookup_issues = validate_lookup_relationships(dependencies, data_model)
    issues = module_issues + lookup_issues

    if args.json:
        print(
            json.dumps(
                {
                    "export_date": export.date,
                    "stats": stats,
                    "issues": issues,
                },
                indent=2,
            )
        )
    else:
        print(render_text(export, stats, issues))


if __name__ == "__main__":
    main()
