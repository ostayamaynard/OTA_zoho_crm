#!/usr/bin/env python3
"""
Extract workflow information from Zoho dependencies JSON file.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path
import sys

TOOLS_DIR = Path(__file__).resolve().parents[1]
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract workflow details from dependencies export")
    parser.add_argument("--date", help="Export date (YYYY-MM-DD). Defaults to latest export.")
    parser.add_argument(
        "--output",
        help="Path to write JSON summary (default: <repo>/reports/workflow_extraction_report.json)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    export = (
        get_export_by_date(args.date, export_directory()).ensure_both()
        if args.date
        else get_latest_export(export_directory()).ensure_both()
    )

    with export.dependencies.open() as f:
        data = json.load(f)

    workflow_deps = data.get('workflow_dependencies', {})
    workflows_by_module = defaultdict(list)

    for _, workflow in workflow_deps.items():
        module = workflow.get('module', 'Unknown')
        workflow_info = {
            'workflow_name': workflow.get('workflow_name', 'N/A'),
            'workflow_id': workflow.get('workflow_id', 'N/A'),
            'active': workflow.get('active', False),
            'trigger_type': workflow.get('trigger_type', 'N/A'),
            'created_by': workflow.get('created_by', 'N/A'),
            'modified_by': workflow.get('modified_by', 'N/A'),
            'created_time': workflow.get('created_time', 'N/A'),
            'modified_time': workflow.get('modified_time', 'N/A'),
            'last_executed_time': workflow.get('last_executed_time', 'N/A'),
            'condition_fields': workflow.get('condition_fields', []),
            'updated_fields': workflow.get('updated_fields', []),
            'cross_module_actions': workflow.get('cross_module_actions', []),
            'external_dependencies': workflow.get('external_dependencies', [])
        }
        workflows_by_module[module].append(workflow_info)

    print("=" * 80)
    print(f"WORKFLOW SUMMARY BY MODULE (export {export.date})")
    print("=" * 80)
    print()

    total_workflows = 0
    for module in sorted(workflows_by_module.keys()):
        count = len(workflows_by_module[module])
        total_workflows += count
        active_count = sum(1 for w in workflows_by_module[module] if w['active'])
        print(f"{module}: {count} workflows ({active_count} active, {count - active_count} inactive)")

    print()
    print(f"TOTAL WORKFLOWS: {total_workflows}")
    print("=" * 80)
    print()

    for module in sorted(workflows_by_module.keys()):
        print("=" * 80)
        print(f"MODULE: {module}")
        print("=" * 80)
        print()

        workflows = workflows_by_module[module]

        for i, workflow in enumerate(workflows, 1):
            print(f"{i}. {workflow['workflow_name']}")
            print(f"   ID: {workflow['workflow_id']}")
            print(f"   Active: {workflow['active']}")
            print(f"   Trigger Type: {workflow['trigger_type']}")

            if workflow['condition_fields']:
                print(f"   Condition Fields: {', '.join(workflow['condition_fields'])}")

            if workflow['updated_fields']:
                print(f"   Updated Fields: {', '.join(workflow['updated_fields'])}")

            if workflow['cross_module_actions']:
                print(f"   Cross-Module Actions: {len(workflow['cross_module_actions'])} action(s)")

            if workflow['external_dependencies']:
                print(f"   External Dependencies: {len(workflow['external_dependencies'])} dependency(ies)")

            print(f"   Created By: {workflow['created_by']} on {workflow['created_time']}")
            print(f"   Last Modified By: {workflow['modified_by']} on {workflow['modified_time']}")

            if workflow['last_executed_time'] and workflow['last_executed_time'] != 'N/A':
                print(f"   Last Executed: {workflow['last_executed_time']}")
            else:
                print("   Last Executed: Never")

            print()

        print()

    output_data = {
        'summary': {
            'total_workflows': total_workflows,
            'modules': {
                module: {
                    'count': len(workflows),
                    'active': sum(1 for w in workflows if w['active']),
                    'inactive': sum(1 for w in workflows if not w['active'])
                } for module, workflows in workflows_by_module.items()
            }
        },
        'workflows_by_module': {module: workflows for module, workflows in workflows_by_module.items()}
    }

    report_dir = Path(__file__).resolve().parents[2] / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    output_path = Path(args.output) if args.output else report_dir / f"workflow_extraction_report_{export.date}.json"
    output_path.write_text(json.dumps(output_data, indent=2))

    print("=" * 80)
    print(f"Report saved to: {output_path}")
    print("=" * 80)


if __name__ == "__main__":
    main()
