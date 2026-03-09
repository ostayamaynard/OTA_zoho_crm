#!/usr/bin/env python3
"""
Verification pass for extra workflows identified in audit.
Thorough check against all sections of the CRM export.
"""

import json
import os
import glob
import re
from collections import defaultdict
import argparse
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT_DIR / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export  # noqa: E402

BASE_DIR = ROOT_DIR
DATA_MODEL_PATH = ""
DEPENDENCIES_PATH = ""
MODULES_DIR = ROOT_DIR / "modules"

# Extra workflows identified in audit
EXTRA_WORKFLOWS = {
    "Leads": [
        "52330000012241820", "52330000000013387", "52330000008071684",
        "52330000008071595", "52330000005299515", "52330000005578918",
        "52330000008071597", "52330000002708230", "52330000003101042",
        "52330000008071685", "52330000000013384", "52330000002944730",
        "52330000000013375", "52330000000013378", "52330000008071596",
        "52330000005299514", "52330000000013396", "52330000000002461",
        "52330000000013393", "52330000000013390"
    ],
    "Deals": [
        "52330000000002361"
    ],
    "Invoices": [
        "52330000000023323", "52330000002455459", "52330000004436309",
        "52330000002455461", "52330000002455457", "52330000000023326",
        "52330000009966041", "52330000000023329", "52330000000023332"
    ],
    "Quotes": [
        "52330000000018489", "52330000000018474", "52330000002455442",
        "52330000000018486", "52330000000018483", "52330000000018477",
        "52330000000018492", "52330000000018480"
    ]
}

def load_json(path):
    """Load JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_all_workflow_ids_from_dependencies(dependencies):
    """Extract ALL workflow IDs from dependencies JSON - every section."""
    all_workflows = {}

    # Main workflow_dependencies section
    workflow_deps = dependencies.get('workflow_dependencies', {})
    for key, workflow in workflow_deps.items():
        wf_id = str(workflow.get('workflow_id', ''))
        if wf_id:
            all_workflows[wf_id] = {
                'name': workflow.get('workflow_name', ''),
                'module': workflow.get('module', ''),
                'trigger_type': workflow.get('trigger_type', ''),
                'active': workflow.get('active', False),
                'source': 'workflow_dependencies'
            }

    # Check for automation_chains
    if 'automation_chains' in dependencies:
        chains = dependencies.get('automation_chains', [])
        if isinstance(chains, list):
            for chain in chains:
                if isinstance(chain, dict):
                    wf_id = str(chain.get('id', '') or chain.get('workflow_id', ''))
                    if wf_id and wf_id not in all_workflows:
                        all_workflows[wf_id] = {
                            'name': chain.get('name', '') or chain.get('workflow_name', ''),
                            'module': chain.get('module', ''),
                            'trigger_type': 'automation_chain',
                            'active': chain.get('active', False),
                            'source': 'automation_chains'
                        }
        elif isinstance(chains, dict):
            for key, chain in chains.items():
                wf_id = str(chain.get('id', '') or chain.get('workflow_id', ''))
                if wf_id and wf_id not in all_workflows:
                    all_workflows[wf_id] = {
                        'name': chain.get('name', '') or chain.get('workflow_name', ''),
                        'module': chain.get('module', ''),
                        'trigger_type': 'automation_chain',
                        'active': chain.get('active', False),
                        'source': 'automation_chains'
                    }

    # Check for any other sections that might contain workflow IDs
    for section_name, section_data in dependencies.items():
        if section_name in ['workflow_dependencies', 'automation_chains', 'lookup_relationships']:
            continue

        if isinstance(section_data, dict):
            for key, value in section_data.items():
                if isinstance(value, dict):
                    wf_id = str(value.get('workflow_id', '') or value.get('id', ''))
                    if wf_id and wf_id.startswith('5233') and wf_id not in all_workflows:
                        all_workflows[wf_id] = {
                            'name': value.get('workflow_name', '') or value.get('name', ''),
                            'module': value.get('module', ''),
                            'trigger_type': value.get('trigger_type', 'unknown'),
                            'active': value.get('active', False),
                            'source': section_name
                        }

    return all_workflows

def search_entire_json_for_id(data, search_id, path=""):
    """Recursively search entire JSON structure for an ID."""
    results = []
    search_str = str(search_id)

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key

            # Check if this key or value contains the ID
            if search_str in str(key) or search_str == str(value):
                results.append({
                    'path': current_path,
                    'value': value if not isinstance(value, (dict, list)) else type(value).__name__
                })

            # Recurse into nested structures
            if isinstance(value, (dict, list)):
                results.extend(search_entire_json_for_id(value, search_id, current_path))

    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = f"{path}[{i}]"
            if search_str == str(item):
                results.append({
                    'path': current_path,
                    'value': item
                })
            if isinstance(item, (dict, list)):
                results.extend(search_entire_json_for_id(item, search_id, current_path))

    return results

def extract_documented_workflow_ids(module_dir):
    """Extract all workflow IDs from a module's documentation."""
    documented_ids = {}

    # Search all .md and .json files
    patterns = [
        f"{module_dir}/docs/*.md",
        f"{module_dir}/data/*.json",
        f"{module_dir}/*.md",
        f"{module_dir}/*.json"
    ]

    for pattern in patterns:
        for filepath in glob.glob(pattern):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find all workflow IDs (17-digit numbers starting with 5233)
                ids = re.findall(r'\b(5233\d{13})\b', content)

                for wf_id in ids:
                    if wf_id not in documented_ids:
                        # Try to find workflow name near the ID
                        # Look for patterns like "| Name | ID |" or "Name: ID"
                        context_match = re.search(
                            rf'([^|\n]{{1,60}})\s*\|\s*{wf_id}|{wf_id}\s*\|\s*([^|\n]{{1,60}})',
                            content
                        )
                        name = ""
                        if context_match:
                            name = (context_match.group(1) or context_match.group(2) or "").strip()

                        documented_ids[wf_id] = {
                            'file': os.path.basename(filepath),
                            'name': name
                        }
            except Exception as e:
                pass

    return documented_ids

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify extra workflows against exports")
    parser.add_argument("--date", help="Export date (YYYY-MM-DD). Defaults to latest export.")
    parser.add_argument("--modules-dir", help="Modules directory (default: <repo>/modules)")
    return parser.parse_args()


def main():
    args = parse_args()

    export = (
        get_export_by_date(args.date, export_directory()).ensure_both()
        if args.date
        else get_latest_export(export_directory()).ensure_both()
    )

    global DATA_MODEL_PATH, DEPENDENCIES_PATH, MODULES_DIR
    DATA_MODEL_PATH = str(export.data_model)
    DEPENDENCIES_PATH = str(export.dependencies)
    MODULES_DIR = Path(args.modules_dir) if args.modules_dir else ROOT_DIR / "modules"

    print("=" * 100)
    print(f"WORKFLOW VERIFICATION PASS (export {export.date})")
    print("=" * 100)
    print()

    # Load source files
    print("Loading source-of-truth files...")
    data_model = load_json(DATA_MODEL_PATH)
    dependencies = load_json(DEPENDENCIES_PATH)
    print()

    # Extract ALL workflow IDs from dependencies
    print("Extracting all workflows from dependencies JSON...")
    all_export_workflows = extract_all_workflow_ids_from_dependencies(dependencies)
    print(f"  Total workflows in export: {len(all_export_workflows)}")
    print()

    # List all sections in dependencies
    print("Sections in dependencies JSON:")
    for section in dependencies.keys():
        if isinstance(dependencies[section], dict):
            print(f"  - {section}: {len(dependencies[section])} entries")
        elif isinstance(dependencies[section], list):
            print(f"  - {section}: {len(dependencies[section])} items")
        else:
            print(f"  - {section}: {type(dependencies[section]).__name__}")
    print()

    # Verify each extra workflow
    print("=" * 100)
    print("VERIFICATION RESULTS")
    print("=" * 100)
    print()

    classifications = {
        'confirmed_orphan': [],
        'false_positive': [],
        'different_module': [],
        'historical': []
    }

    module_dirs = {
        "Leads": "leads",
        "Deals": "deals",
        "Invoices": "invoices",
        "Quotes": "quotes"
    }

    for module_name, workflow_ids in EXTRA_WORKFLOWS.items():
        print(f"### {module_name}")
        print()

        module_dir = Path(MODULES_DIR) / module_dirs[module_name]
        documented = extract_documented_workflow_ids(str(module_dir))

        print(f"Checking {len(workflow_ids)} extra workflow IDs...")
        print()

        for wf_id in sorted(workflow_ids):
            print(f"**Workflow ID: {wf_id}**")

            # Get documented name
            doc_info = documented.get(wf_id, {})
            doc_name = doc_info.get('name', 'Unknown')
            doc_file = doc_info.get('file', 'Unknown')
            print(f"  Documented as: {doc_name}")
            print(f"  Found in file: {doc_file}")

            # Check if in export
            if wf_id in all_export_workflows:
                export_info = all_export_workflows[wf_id]
                print(f"  ✓ EXISTS IN EXPORT")
                print(f"    Name: {export_info['name']}")
                print(f"    Module: {export_info['module']}")
                print(f"    Source: {export_info['source']}")
                print(f"    Active: {export_info['active']}")

                if export_info['module'] != module_name:
                    print(f"  ⚠ DIFFERENT MODULE: Listed under {export_info['module']}, documented under {module_name}")
                    classifications['different_module'].append({
                        'id': wf_id,
                        'documented_module': module_name,
                        'actual_module': export_info['module'],
                        'name': export_info['name']
                    })
                else:
                    print(f"  ⚠ FALSE POSITIVE: Exists in export but audit script missed it")
                    classifications['false_positive'].append({
                        'id': wf_id,
                        'module': module_name,
                        'name': export_info['name']
                    })
            else:
                # Deep search in both files
                print(f"  ✗ NOT IN workflow_dependencies")

                # Search entire dependencies JSON
                deps_results = search_entire_json_for_id(dependencies, wf_id)
                if deps_results:
                    print(f"  ? Found in dependencies at:")
                    for result in deps_results[:3]:
                        print(f"    - {result['path']}")
                else:
                    print(f"  ✗ NOT FOUND anywhere in dependencies JSON")

                # Search entire data model JSON
                dm_results = search_entire_json_for_id(data_model, wf_id)
                if dm_results:
                    print(f"  ? Found in data-model at:")
                    for result in dm_results[:3]:
                        print(f"    - {result['path']}")
                else:
                    print(f"  ✗ NOT FOUND anywhere in data-model JSON")

                if not deps_results and not dm_results:
                    print(f"  → CONFIRMED ORPHAN: Safe to remove")
                    classifications['confirmed_orphan'].append({
                        'id': wf_id,
                        'module': module_name,
                        'documented_name': doc_name
                    })
                else:
                    print(f"  → REQUIRES MANUAL REVIEW")
                    classifications['historical'].append({
                        'id': wf_id,
                        'module': module_name,
                        'documented_name': doc_name,
                        'found_in': deps_results + dm_results
                    })

            print()

        print("-" * 50)
        print()

    # Final classification summary
    print("=" * 100)
    print("FINAL CLASSIFICATION SUMMARY")
    print("=" * 100)
    print()

    print("## Confirmed Orphans — Safe to Remove")
    print()
    if classifications['confirmed_orphan']:
        print("| Module | Workflow ID | Documented Name |")
        print("|--------|-------------|-----------------|")
        for item in classifications['confirmed_orphan']:
            print(f"| {item['module']} | {item['id']} | {item['documented_name']} |")
    else:
        print("None")
    print()

    print("## False Positives — Exist in Export (Audit Script Error)")
    print()
    if classifications['false_positive']:
        print("| Module | Workflow ID | Name |")
        print("|--------|-------------|------|")
        for item in classifications['false_positive']:
            print(f"| {item['module']} | {item['id']} | {item['name']} |")
    else:
        print("None")
    print()

    print("## Mis-mapped — Different Module in Export")
    print()
    if classifications['different_module']:
        print("| Workflow ID | Documented Module | Actual Module | Name |")
        print("|-------------|-------------------|---------------|------|")
        for item in classifications['different_module']:
            print(f"| {item['id']} | {item['documented_module']} | {item['actual_module']} | {item['name']} |")
    else:
        print("None")
    print()

    print("## Requires Manual Review")
    print()
    if classifications['historical']:
        for item in classifications['historical']:
            print(f"- **{item['id']}** ({item['module']}): {item['documented_name']}")
            print(f"  Found in: {[r['path'] for r in item.get('found_in', [])]}")
    else:
        print("None")
    print()

    # Summary counts
    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)
    print()
    total_extra = sum(len(ids) for ids in EXTRA_WORKFLOWS.values())
    print(f"Total extra workflows reviewed: {total_extra}")
    print(f"  - Confirmed Orphans (safe to remove): {len(classifications['confirmed_orphan'])}")
    print(f"  - False Positives (audit error): {len(classifications['false_positive'])}")
    print(f"  - Mis-mapped (different module): {len(classifications['different_module'])}")
    print(f"  - Requires Manual Review: {len(classifications['historical'])}")
    print()

if __name__ == "__main__":
    main()
