#!/usr/bin/env python3
"""
Add workflow URLs to all documentation files.
Only adds URLs for valid workflow IDs from the CRM export.
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

BASE_URL = "https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/"

def load_json(path):
    """Load JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_valid_workflow_ids():
    """Extract all valid workflow IDs from exports."""
    valid_ids = {}

    # Load dependencies
    dependencies = load_json(DEPENDENCIES_PATH)

    # Extract from workflow_dependencies
    for key, workflow in dependencies.get('workflow_dependencies', {}).items():
        wf_id = str(workflow.get('workflow_id', ''))
        if wf_id:
            valid_ids[wf_id] = {
                'name': workflow.get('workflow_name', ''),
                'module': workflow.get('module', '')
            }

    # Also check data model for workflows
    data_model = load_json(DATA_MODEL_PATH)
    for module_name, module_data in data_model.items():
        if 'workflows' in module_data:
            for wf in module_data.get('workflows', []):
                wf_id = str(wf.get('id', '') or wf.get('workflow_id', ''))
                if wf_id and wf_id not in valid_ids:
                    valid_ids[wf_id] = {
                        'name': wf.get('name', '') or wf.get('workflow_name', ''),
                        'module': module_name
                    }

    return valid_ids

def should_skip_file(filepath):
    """Check if file should be skipped."""
    filename = os.path.basename(filepath).lower()

    # Skip status-map and stage comparison files
    if 'status' in filename and 'map' in filename:
        return True
    if 'stage' in filename and 'comparison' in filename:
        return True

    return False

def find_workflow_ids_in_content(content, valid_ids):
    """Find all valid workflow IDs in content."""
    found = []
    # Find all 17-digit numbers starting with 5233
    for match in re.finditer(r'\b(5233\d{13})\b', content):
        wf_id = match.group(1)
        if wf_id in valid_ids:
            found.append({
                'id': wf_id,
                'start': match.start(),
                'end': match.end(),
                'info': valid_ids[wf_id]
            })
    return found

def update_markdown_content(content, valid_ids):
    """Update markdown content to add workflow URLs."""
    changes = []

    # Find all workflow IDs
    found_ids = find_workflow_ids_in_content(content, valid_ids)

    if not found_ids:
        return content, changes

    # Process in reverse order to maintain positions
    new_content = content
    for item in reversed(found_ids):
        wf_id = item['id']
        url = f"{BASE_URL}{wf_id}"

        # Check context to decide how to add URL
        start = item['start']
        end = item['end']

        # Get surrounding context
        before = new_content[max(0, start-50):start]
        after = new_content[end:end+50]

        # Check if URL already exists
        if url in new_content[start:end+200]:
            continue
        if f"[Open]({url})" in new_content:
            continue

        # Different patterns for different contexts

        # Pattern 1: In a table cell like "| ID |"
        if '|' in before[-10:] and '|' in after[:10]:
            # Check if there's already a URL column after
            if '[Open]' in after[:50]:
                continue
            # Don't add if already has URL
            new_content = new_content[:end] + f" | [Open]({url})" + new_content[end:]
            changes.append(f"Added URL after {wf_id} in table")

        # Pattern 2: Standalone ID (like in a list or after a label)
        elif re.search(r'(ID|id):\s*$', before) or re.search(r'^\s*$', after[:5]):
            if f"({url})" not in new_content[end:end+100]:
                new_content = new_content[:end] + f" ([Open]({url}))" + new_content[end:]
                changes.append(f"Added URL after standalone {wf_id}")

    return new_content, changes

def update_json_content(content, valid_ids, filepath):
    """Update JSON content to add workflow URLs."""
    changes = []

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return content, changes

    def add_urls_recursive(obj, path=""):
        """Recursively add workflow_url fields."""
        nonlocal changes

        if isinstance(obj, dict):
            # Check for workflow_id field
            wf_id = None
            for key in ['workflow_id', 'id']:
                if key in obj:
                    wf_id = str(obj[key])
                    break

            if wf_id and wf_id in valid_ids:
                if 'workflow_url' not in obj:
                    obj['workflow_url'] = f"{BASE_URL}{wf_id}"
                    changes.append(f"Added workflow_url for {wf_id} at {path}")

            # Recurse into children
            for key, value in obj.items():
                add_urls_recursive(value, f"{path}.{key}")

        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                add_urls_recursive(item, f"{path}[{i}]")

    add_urls_recursive(data)

    if changes:
        new_content = json.dumps(data, indent=2, ensure_ascii=False)
        return new_content, changes

    return content, changes

def process_module(module_dir, valid_ids, dry_run=True):
    """Process all files in a module directory."""
    results = {
        'module': os.path.basename(module_dir),
        'files_updated': [],
        'files_skipped': [],
        'total_changes': 0
    }

    # Find all relevant files
    patterns = [
        f"{module_dir}/docs/*.md",
        f"{module_dir}/data/*.json",
        f"{module_dir}/diagrams/*.mmd"
    ]

    for pattern in patterns:
        for filepath in glob.glob(pattern):
            if should_skip_file(filepath):
                results['files_skipped'].append(os.path.basename(filepath))
                continue

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                continue

            # Determine file type and process
            filename = os.path.basename(filepath)
            changes = []
            new_content = content

            if filepath.endswith('.md'):
                new_content, changes = update_markdown_content(content, valid_ids)
            elif filepath.endswith('.json'):
                new_content, changes = update_json_content(content, valid_ids, filepath)
            elif filepath.endswith('.mmd'):
                # For Mermaid, we'll handle separately
                pass

            if changes:
                results['files_updated'].append({
                    'file': filename,
                    'changes': changes,
                    'path': filepath
                })
                results['total_changes'] += len(changes)

                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

    return results

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add workflow URLs to docs based on exports")
    parser.add_argument("--apply", action="store_true", help="Write changes to files (default: dry run)")
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

    dry_run = not args.apply

    print("=" * 80)
    print("ADD WORKFLOW URLs TO DOCUMENTATION")
    print("=" * 80)
    print()

    if dry_run:
        print("** DRY RUN MODE - No files will be modified **")
        print("Run with --apply to make changes")
        print()

    # Extract valid workflow IDs
    print("Extracting valid workflow IDs from exports...")
    valid_ids = extract_valid_workflow_ids()
    print(f"  Found {len(valid_ids)} valid workflow IDs")
    print()

    # Process each module
    all_results = []

    for module_name in os.listdir(MODULES_DIR):
        module_dir = os.path.join(MODULES_DIR, module_name)
        if not os.path.isdir(module_dir):
            continue

        results = process_module(module_dir, valid_ids, dry_run)
        all_results.append(results)

    # Print summary
    print("=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    print()

    total_files = 0
    total_changes = 0

    for results in all_results:
        if results['files_updated']:
            print(f"### {results['module']}")
            print()

            for file_info in results['files_updated']:
                print(f"  **{file_info['file']}**")
                for change in file_info['changes'][:5]:  # Limit output
                    print(f"    - {change}")
                if len(file_info['changes']) > 5:
                    print(f"    - ... and {len(file_info['changes']) - 5} more")
                print()

            if results['files_skipped']:
                print(f"  Skipped: {', '.join(results['files_skipped'])}")
                print()

            total_files += len(results['files_updated'])
            total_changes += results['total_changes']

    print("=" * 80)
    print(f"Total files to update: {total_files}")
    print(f"Total changes: {total_changes}")
    print("=" * 80)

    if dry_run:
        print()
        print("To apply these changes, run: python3 tools/add_workflow_urls.py --apply")

if __name__ == "__main__":
    main()
