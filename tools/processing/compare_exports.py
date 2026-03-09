#!/usr/bin/env python3
"""
Compare two Zoho CRM export snapshots (data model + dependencies) and
emit JSON and Markdown change reports.

Defaults:
- Uses the latest two complete exports discovered in
  tools/exports/zoho_export_package/.
- Writes reports to tools/reports/export_diff_<new>_vs_<old>.json/.md
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from utils.file_discovery import (
    ExportFiles,
    export_directory,
    get_export_by_date,
    get_latest_two_exports,
    list_exports,
)


BASE_DIR = Path(__file__).resolve().parents[1]
REPORT_DIR = BASE_DIR / "reports"

FIELD_KEYS_TO_TRACK = [
    "data_type",
    "custom_field",
    "system_mandatory",
    "required",
    "unique",
    "read_only",
    "length",
]

WORKFLOW_KEYS_TO_TRACK = [
    "name",
    "status",
    "description",
    "execute_when",
]

# Runtime metadata keys - excluded by default to reduce noise
WORKFLOW_METADATA_KEYS = [
    "last_executed_time",
    "modified_time",
    "created_time",
]


@dataclass
class ModuleDiff:
    fields_added: List[str]
    fields_removed: List[str]
    fields_changed: List[Dict]
    picklists_changed: List[Dict]
    workflows_added: List[str]
    workflows_removed: List[str]
    workflows_changed: List[Dict]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare two Zoho CRM exports")
    parser.add_argument("--new-date", dest="new_date", help="YYYY-MM-DD for new export (defaults to latest)")
    parser.add_argument("--old-date", dest="old_date", help="YYYY-MM-DD for old export (defaults to previous)")
    parser.add_argument("--output-dir", dest="output_dir", help="Directory for reports (default: tools/reports)")
    parser.add_argument("--json-only", action="store_true", help="Write only JSON (skip Markdown)")
    parser.add_argument("--markdown-only", action="store_true", help="Write only Markdown (skip JSON)")
    parser.add_argument(
        "--include-execution-metadata",
        action="store_true",
        help="Include last_executed_time, modified_time, created_time in workflow diff (noisy)",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def picklist_values(field: dict) -> List[str]:
    values = field.get("pick_list_values") or []
    actual_values = []
    for item in values:
        actual = item.get("actual_value") or item.get("display_value")
        if actual:
            actual_values.append(actual)
    return actual_values


def normalize_fields(module_data: dict) -> Dict[str, dict]:
    return {
        f["api_name"]: f
        for f in module_data.get("fields", [])
        if f.get("api_name")
    }


def normalize_workflows(module_data: dict) -> Dict[str, dict]:
    workflows = module_data.get("workflows") or []
    normalized = {}
    for wf in workflows:
        key = wf.get("id") or wf.get("name")
        if key:
            normalized[key] = wf
    return normalized


def normalize_lookup_relationships(dependencies: dict) -> Dict[str, Dict[str, dict]]:
    result: Dict[str, Dict[str, dict]] = {}
    for module, relationships in (dependencies.get("lookup_relationships") or {}).items():
        result[module] = {rel.get("field_name"): rel for rel in relationships if rel.get("field_name")}
    return result


def compare_field(old: dict, new: dict) -> Optional[Dict]:
    changes = {}
    for key in FIELD_KEYS_TO_TRACK:
        if old.get(key) != new.get(key):
            changes[key] = {"old": old.get(key), "new": new.get(key)}

    old_pick = set(picklist_values(old))
    new_pick = set(picklist_values(new))
    if old_pick != new_pick:
        changes["pick_list_values"] = {"old": sorted(old_pick), "new": sorted(new_pick)}

    if changes:
        return {"field": new.get("api_name") or old.get("api_name"), "changes": changes}
    return None


def compare_workflow(old: dict, new: dict, include_metadata: bool = False) -> Optional[Dict]:
    changes = {}
    keys = WORKFLOW_KEYS_TO_TRACK + (WORKFLOW_METADATA_KEYS if include_metadata else [])
    for key in keys:
        if old.get(key) != new.get(key):
            changes[key] = {"old": old.get(key), "new": new.get(key)}
    if changes:
        identifier = new.get("id") or new.get("name") or old.get("id") or old.get("name")
        return {"workflow": identifier, "changes": changes}
    return None


def diff_modules(old_data: dict, new_data: dict, include_metadata: bool = False) -> Tuple[Dict[str, ModuleDiff], List[str], List[str]]:
    old_modules = set(old_data.keys())
    new_modules = set(new_data.keys())

    added_modules = sorted(new_modules - old_modules)
    removed_modules = sorted(old_modules - new_modules)
    common = old_modules & new_modules

    module_diffs: Dict[str, ModuleDiff] = {}
    for module in common:
        old_fields = normalize_fields(old_data[module])
        new_fields = normalize_fields(new_data[module])
        old_workflows = normalize_workflows(old_data[module])
        new_workflows = normalize_workflows(new_data[module])

        fields_added = sorted(set(new_fields) - set(old_fields))
        fields_removed = sorted(set(old_fields) - set(new_fields))

        changed_fields = []
        for fname in set(old_fields) & set(new_fields):
            change = compare_field(old_fields[fname], new_fields[fname])
            if change:
                changed_fields.append(change)

        workflows_added = sorted(set(new_workflows) - set(old_workflows))
        workflows_removed = sorted(set(old_workflows) - set(new_workflows))

        changed_workflows = []
        for wname in set(old_workflows) & set(new_workflows):
            change = compare_workflow(old_workflows[wname], new_workflows[wname], include_metadata)
            if change:
                changed_workflows.append(change)

        picklist_changes = [c for c in changed_fields if "pick_list_values" in c["changes"]]

        module_diffs[module] = ModuleDiff(
            fields_added=fields_added,
            fields_removed=fields_removed,
            fields_changed=changed_fields,
            picklists_changed=picklist_changes,
            workflows_added=workflows_added,
            workflows_removed=workflows_removed,
            workflows_changed=changed_workflows,
        )

    return module_diffs, added_modules, removed_modules


def diff_lookup_relationships(old_dep: dict, new_dep: dict) -> Dict[str, Dict[str, List[str]]]:
    old_lookup = normalize_lookup_relationships(old_dep)
    new_lookup = normalize_lookup_relationships(new_dep)

    modules = set(old_lookup) | set(new_lookup)
    result: Dict[str, Dict[str, List[str]]] = {}

    for module in modules:
        old_rel = old_lookup.get(module, {})
        new_rel = new_lookup.get(module, {})
        added = sorted(set(new_rel) - set(old_rel))
        removed = sorted(set(old_rel) - set(new_rel))
        result[module] = {
            "added_lookup_fields": added,
            "removed_lookup_fields": removed,
        }
    return result


def make_markdown(diff: dict) -> str:
    lines = []
    lines.append(f"# Export Diff {diff['new_date']} vs {diff['old_date']}")
    lines.append("")
    
    # Executive Summary
    modules_added = len(diff['modules']['added'])
    modules_removed = len(diff['modules']['removed'])
    modules_with_changes = sum(
        1 for m in diff['modules']['modified'].values()
        if m['fields_added'] or m['fields_removed'] or m['fields_changed']
        or m['workflows_added'] or m['workflows_removed'] or m['workflows_changed']
    )
    total_field_changes = sum(
        len(m['fields_added']) + len(m['fields_removed']) + len(m['fields_changed'])
        for m in diff['modules']['modified'].values()
    )
    total_workflow_changes = sum(
        len(m['workflows_added']) + len(m['workflows_removed']) + len(m['workflows_changed'])
        for m in diff['modules']['modified'].values()
    )
    
    lines.append("## Executive Summary")
    lines.append("")
    if modules_added == 0 and modules_removed == 0 and total_field_changes == 0 and total_workflow_changes == 0:
        lines.append("> **No configuration changes detected.**")
    else:
        lines.append(f"| Category | Count |")
        lines.append(f"|----------|-------|")
        lines.append(f"| Modules Added | {modules_added} |")
        lines.append(f"| Modules Removed | {modules_removed} |")
        lines.append(f"| Modules with Changes | {modules_with_changes} |")
        lines.append(f"| Total Field Changes | {total_field_changes} |")
        lines.append(f"| Total Workflow Changes | {total_workflow_changes} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    lines.append("## Modules")
    lines.append(f"- Added: {', '.join(diff['modules']['added']) or 'None'}")
    lines.append(f"- Removed: {', '.join(diff['modules']['removed']) or 'None'}")
    lines.append("")

    lines.append("## Field Changes")
    for module, changes in diff["modules"]["modified"].items():
        if changes["fields_added"] or changes["fields_removed"] or changes["fields_changed"]:
            lines.append(f"### {module}")
            if changes["fields_added"]:
                lines.append(f"- Fields added: {', '.join(changes['fields_added'])}")
            if changes["fields_removed"]:
                lines.append(f"- Fields removed: {', '.join(changes['fields_removed'])}")
            for change in changes["fields_changed"]:
                field = change["field"]
                deltas = ", ".join(change["changes"].keys())
                lines.append(f"  - {field}: {deltas}")
    lines.append("")

    lines.append("## Workflow Status Changes")
    status_changes_found = False
    for module, changes in diff["modules"]["modified"].items():
        status_entries = []
        for change in changes["workflows_changed"]:
            status_change = change["changes"].get("status")
            if status_change:
                status_entries.append(
                    f"- {change['workflow']}: {status_change.get('old')} -> {status_change.get('new')}"
                )
        if status_entries:
            status_changes_found = True
            lines.append(f"### {module}")
            lines.extend(status_entries)
    if not status_changes_found:
        lines.append("- None")
    lines.append("")

    lines.append("## Workflow Changes")
    for module, changes in diff["modules"]["modified"].items():
        if changes["workflows_added"] or changes["workflows_removed"] or changes["workflows_changed"]:
            lines.append(f"### {module}")
            if changes["workflows_added"]:
                lines.append(f"- Workflows added: {', '.join(changes['workflows_added'])}")
            if changes["workflows_removed"]:
                lines.append(f"- Workflows removed: {', '.join(changes['workflows_removed'])}")
            for change in changes["workflows_changed"]:
                wf = change["workflow"]
                parts = []
                if "status" in change["changes"]:
                    sc = change["changes"]["status"]
                    parts.append(f"status {sc.get('old')} -> {sc.get('new')}")
                if "last_executed_time" in change["changes"]:
                    parts.append("last_executed_time updated")
                remaining = [k for k in change["changes"].keys() if k not in {"status", "last_executed_time"}]
                if remaining:
                    parts.extend(remaining)
                summary = ", ".join(parts) if parts else ", ".join(change["changes"].keys())
                lines.append(f"  - {wf}: {summary}")
    lines.append("")

    lines.append("## Lookup Relationship Changes")
    for module, rel in diff["lookup_relationships"].items():
        if rel["added_lookup_fields"] or rel["removed_lookup_fields"]:
            lines.append(f"### {module}")
            if rel["added_lookup_fields"]:
                lines.append(f"- Added lookup fields: {', '.join(rel['added_lookup_fields'])}")
            if rel["removed_lookup_fields"]:
                lines.append(f"- Removed lookup fields: {', '.join(rel['removed_lookup_fields'])}")

    return "\n".join(lines) + "\n"


def diff_exports(old_export: ExportFiles, new_export: ExportFiles, include_metadata: bool = False) -> dict:
    old_data = load_json(old_export.data_model)
    new_data = load_json(new_export.data_model)
    old_dep = load_json(old_export.dependencies)
    new_dep = load_json(new_export.dependencies)

    module_diffs, added_modules, removed_modules = diff_modules(old_data, new_data, include_metadata)

    modules_serialized = {
        name: {
            "fields_added": diff.fields_added,
            "fields_removed": diff.fields_removed,
            "fields_changed": diff.fields_changed,
            "picklists_changed": diff.picklists_changed,
            "workflows_added": diff.workflows_added,
            "workflows_removed": diff.workflows_removed,
            "workflows_changed": diff.workflows_changed,
        }
        for name, diff in module_diffs.items()
    }

    lookup_diff = diff_lookup_relationships(old_dep, new_dep)

    return {
        "old_date": old_export.date,
        "new_date": new_export.date,
        "modules": {
            "added": added_modules,
            "removed": removed_modules,
            "modified": modules_serialized,
        },
        "lookup_relationships": lookup_diff,
    }


def resolve_exports(new_date: Optional[str], old_date: Optional[str]) -> Tuple[ExportFiles, ExportFiles]:
    export_dir = export_directory()
    if new_date and old_date:
        new_export = get_export_by_date(new_date, export_dir).ensure_both()
        old_export = get_export_by_date(old_date, export_dir).ensure_both()
        return old_export, new_export
    if new_date:
        exports = list_exports(export_dir)
        selected = [e for e in exports if e.date == new_date]
        if not selected:
            raise FileNotFoundError(f"No export found for date {new_date}")
        new_export = selected[0]
        idx = exports.index(new_export)
        if idx + 1 >= len(exports):
            raise FileNotFoundError(f"No older export available before {new_date}")
        old_export = exports[idx + 1]
        return old_export.ensure_both(), new_export.ensure_both()
    old_export, new_export = get_latest_two_exports(export_dir)
    return old_export.ensure_both(), new_export.ensure_both()


def main():
    args = parse_args()
    output_dir = Path(args.output_dir) if args.output_dir else REPORT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    old_export, new_export = resolve_exports(args.new_date, args.old_date)
    include_metadata = getattr(args, 'include_execution_metadata', False)
    diff = diff_exports(old_export, new_export, include_metadata)

    json_path = output_dir / f"export_diff_{new_export.date}_vs_{old_export.date}.json"
    md_path = output_dir / f"export_diff_{new_export.date}_vs_{old_export.date}.md"

    if not args.markdown_only:
        json_path.write_text(json.dumps(diff, indent=2))
        print(f"Wrote JSON diff to {json_path}")
    if not args.json_only:
        md_path.write_text(make_markdown(diff))
        print(f"Wrote Markdown diff to {md_path}")


if __name__ == "__main__":
    main()

