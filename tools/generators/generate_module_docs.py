#!/usr/bin/env python3
"""
Generate complete documentation for Contacts and Accounts modules.
"""

import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

TOOLS_DIR = Path(__file__).resolve().parents[1]  # tools/ directory
ROOT_DIR = TOOLS_DIR.parent
if str(ROOT_DIR / "tools") not in sys.path:
    sys.path.append(str(ROOT_DIR / "tools"))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export  # noqa: E402

BASE_URL = "https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/"
DATA_MODEL_PATH = ""
DEPENDENCIES_PATH = ""
MODULES_DIR = ROOT_DIR / "modules"
SOURCE_LABEL = ""
SOURCE_DEP_LABEL = ""
AUTO_HEADER = "<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\\n\\n"

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_module_fields(data_model, module_name):
    """Extract all fields for a module."""
    if module_name not in data_model:
        return []

    fields = data_model[module_name].get('fields', [])
    return fields

def extract_module_workflows(dependencies, module_name):
    """Extract all workflows for a module."""
    workflows = []

    for key, wf in dependencies.get('workflow_dependencies', {}).items():
        if wf.get('module') == module_name:
            workflows.append({
                'id': wf.get('workflow_id', ''),
                'name': wf.get('workflow_name', ''),
                'trigger_type': wf.get('trigger_type', ''),
                'active': wf.get('active', False),
                'created_by': wf.get('created_by', ''),
                'modified_by': wf.get('modified_by', ''),
                'created_time': wf.get('created_time', ''),
                'modified_time': wf.get('modified_time', '')
            })

    return sorted(workflows, key=lambda x: x['name'])

def extract_module_lookups(dependencies, module_name):
    """Extract lookup relationships for a module."""
    return dependencies.get('lookup_relationships', {}).get(module_name, [])

def generate_fields_md(module_name, fields):
    """Generate {module}-fields.md content."""

    # Separate standard and custom fields
    standard_fields = []
    custom_fields = []
    lookup_fields = []

    for field in fields:
        field_info = {
            'api_name': field.get('api_name', ''),
            'label': field.get('field_label', ''),
            'data_type': field.get('data_type', ''),
            'required': field.get('system_mandatory', False)
        }

        if field.get('data_type') == 'lookup':
            lookup_fields.append(field_info)
        elif field.get('custom_field', False):
            custom_fields.append(field_info)
        else:
            standard_fields.append(field_info)

    content = f"""{AUTO_HEADER}# {module_name} Module - Field Reference

**Generated from:** {SOURCE_LABEL}
**Total Fields:** {len(fields)}

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
"""

    for f in sorted(standard_fields, key=lambda x: x['api_name']):
        req = "Yes" if f['required'] else "No"
        content += f"| {f['api_name']} | {f['label']} | {f['data_type']} | {req} |\n"

    content += """
---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
"""

    for f in sorted(custom_fields, key=lambda x: x['api_name']):
        req = "Yes" if f['required'] else "No"
        content += f"| {f['api_name']} | {f['label']} | {f['data_type']} | {req} |\n"

    if lookup_fields:
        content += """
---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
"""
        for f in sorted(lookup_fields, key=lambda x: x['api_name']):
            req = "Yes" if f['required'] else "No"
            content += f"| {f['api_name']} | {f['label']} | {f['data_type']} | {req} |\n"

    content += f"""
---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
**Source:** Zoho CRM Export {SOURCE_LABEL}
"""

    return content

def generate_workflows_md(module_name, workflows):
    """Generate {module}-workflows.md content."""

    # Group by trigger type
    by_trigger = {}
    for wf in workflows:
        trigger = wf['trigger_type']
        if trigger not in by_trigger:
            by_trigger[trigger] = []
        by_trigger[trigger].append(wf)

    active_count = sum(1 for wf in workflows if wf['active'])
    inactive_count = len(workflows) - active_count

    content = f"""{AUTO_HEADER}# {module_name} Module - Workflow Reference

**Generated from:** {SOURCE_DEP_LABEL}
**Total Workflows:** {len(workflows)}
**Active Workflows:** {active_count}
**Inactive Workflows:** {inactive_count}

---

## Workflow Summary by Trigger Type

| Trigger Type | Count |
|--------------|-------|
"""

    for trigger, wfs in sorted(by_trigger.items()):
        content += f"| {trigger} | {len(wfs)} |\n"

    content += "\n---\n\n## All Workflows\n\n"

    for trigger, wfs in sorted(by_trigger.items()):
        content += f"### {trigger.replace('_', ' ').title()} Triggers\n\n"

        for wf in wfs:
            status = "Active" if wf['active'] else "Inactive"
            url = f"{BASE_URL}{wf['id']}"

            content += f"""#### {wf['name']}

| Property | Value |
|----------|-------|
| **Workflow ID** | {wf['id']} |
| **Status** | {status} |
| **Trigger Type** | {wf['trigger_type']} |
| **Created By** | {wf['created_by']} |
| **Modified By** | {wf['modified_by']} |

**URL:** [{url}]({url})

---

"""

    content += f"""
## Quick Reference Table

| Workflow Name | ID | Trigger Type | Status | URL |
|--------------|-----|--------------|--------|-----|
"""

    for wf in workflows:
        status = "Active" if wf['active'] else "Inactive"
        url = f"{BASE_URL}{wf['id']}"
        content += f"| {wf['name']} | {wf['id']} | {wf['trigger_type']} | {status} | [Open]({url}) |\n"

    content += f"""
---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
**Source:** Zoho CRM Export {SOURCE_DEP_LABEL}
"""

    return content

def generate_workflow_urls_md(module_name, workflows):
    """Generate {module}-workflow-urls.md content."""

    content = f"""{AUTO_HEADER}# {module_name} Module - Workflow URL Reference

**Document Version:** 1.0
**Zoho Instance:** https://crm.zoho.com.au/crm/org7003757385
**Last Updated:** {datetime.now().strftime('%d %B %Y')}

---

## Quick Reference

| Total Workflows | {len(workflows)} |
|-----------------|-----|
| Base URL | `{BASE_URL}` |

---

## All Workflows

| Workflow | ID | Trigger Type | Status | URL |
|----------|-----|--------------|--------|-----|
"""

    for wf in workflows:
        status = "Active" if wf['active'] else "Inactive"
        url = f"{BASE_URL}{wf['id']}"
        content += f"| {wf['name']} | {wf['id']} | {wf['trigger_type']} | {status} | [Open]({url}) |\n"

    content += f"""
---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {datetime.now().strftime('%Y-%m-%d')} | System | Initial creation |
"""

    return content

def generate_usage_md(module_name, fields, workflows, lookups):
    """Generate {module}-usage.md content."""

    content = f"""{AUTO_HEADER}# {module_name} Module - Usage Guide

**Document Version:** 1.0
**Last Updated:** {datetime.now().strftime('%d %B %Y')}

---

## Overview

The {module_name} module contains {len(fields)} fields and {len(workflows)} workflows.

---

## Key Statistics

| Metric | Value |
|--------|-------|
| Total Fields | {len(fields)} |
| Total Workflows | {len(workflows)} |
| Lookup Relationships | {len(lookups)} |

---

## Workflows

"""

    for wf in workflows:
        url = f"{BASE_URL}{wf['id']}"
        content += f"- **{wf['name']}** - [Open]({url})\n"

    content += """
---

## Lookup Relationships

"""

    if lookups:
        content += "| Field | Target Module |\n|-------|---------------|\n"
        for lookup in lookups:
            content += f"| {lookup.get('field_label', '')} | {lookup.get('lookup_module', '')} |\n"
    else:
        content += "No outbound lookups defined.\n"

    content += f"""
---

## Best Practices

1. Keep records up to date with accurate information
2. Use workflows to automate repetitive tasks
3. Maintain proper relationships between modules

---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
"""

    return content

def generate_customer_journey_json(module_name, workflows):
    """Generate customer-journey-{module}.json content."""

    journey = {
        "module": module_name,
        "generated_from": SOURCE_DEP_LABEL,
        "last_updated": datetime.now().strftime('%Y-%m-%d'),
        "total_workflows": len(workflows),
        "customer_journey": {
            f"{module_name}_Created": {
                "description": f"When a {module_name.lower()[:-1] if module_name.endswith('s') else module_name.lower()} record is created",
                "related_workflows": []
            },
            f"{module_name}_Updated": {
                "description": f"When a {module_name.lower()[:-1] if module_name.endswith('s') else module_name.lower()} record is updated",
                "related_workflows": []
            }
        }
    }

    for wf in workflows:
        wf_entry = {
            "workflow_id": wf['id'],
            "workflow_name": wf['name'],
            "workflow_url": f"{BASE_URL}{wf['id']}"
        }

        if wf['trigger_type'] == 'create':
            journey['customer_journey'][f"{module_name}_Created"]['related_workflows'].append(wf_entry)
        else:
            journey['customer_journey'][f"{module_name}_Updated"]['related_workflows'].append(wf_entry)

    return journey

# Common status/stage field patterns to look for in status-map generation
STATUS_FIELD_PATTERNS = [
    "status", "stage", "lead_status", "deal_stage", "invoice_status",
    "quote_stage", "registration_status", "course_status"
]

def generate_status_map_md(module_name, fields):
    """Generate {module}-status-map.md content from picklist fields."""
    
    # Find status/stage picklist fields
    status_fields = []
    for field in fields:
        api_name = field.get('api_name', '').lower()
        if field.get('data_type') == 'picklist':
            # Check if it's a status/stage field
            for pattern in STATUS_FIELD_PATTERNS:
                if pattern in api_name:
                    status_fields.append(field)
                    break
    
    if not status_fields:
        return None  # No status fields found
    
    content = f"""{AUTO_HEADER}# {module_name} Module - Status Map

**Generated from:** {SOURCE_LABEL}

---

"""
    
    for field in status_fields:
        api_name = field.get('api_name', '')
        label = field.get('field_label', api_name)
        pick_list_values = field.get('pick_list_values', [])
        enable_colour = field.get('enable_colour_code', False)
        
        used_count = sum(1 for v in pick_list_values if v.get('type', 'used') == 'used')
        unused_count = len(pick_list_values) - used_count
        
        content += f"""## {label}

**Field API Name:** {api_name}
**Total Values:** {len(pick_list_values)} ({used_count} used, {unused_count} unused)
**Colour Coding:** {'Enabled' if enable_colour else 'Disabled'}

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
"""
        
        for i, val in enumerate(pick_list_values, 1):
            display = val.get('display_value', val.get('actual_value', ''))
            colour = val.get('colour_code') or 'null'
            val_type = val.get('type', 'used')
            val_id = val.get('id', '')
            content += f"| {i} | {display} | {colour} | {val_type} | {val_id} |\n"
        
        # Group by colour if colour coding is enabled
        if enable_colour:
            content += "\n### Colour Palette\n\n```\n"
            colour_groups = {}
            for val in pick_list_values:
                colour = val.get('colour_code')
                if colour:
                    if colour not in colour_groups:
                        colour_groups[colour] = []
                    colour_groups[colour].append(val.get('display_value', val.get('actual_value', '')))
            
            for colour, values in sorted(colour_groups.items()):
                content += f"{colour}: {', '.join(values)}\n"
            content += "```\n"
        
        content += "\n---\n\n"
    
    content += f"""## API Reference

| Field | API Name | Data Type | Colour Coding |
|-------|----------|-----------|---------------|
"""
    
    for field in status_fields:
        api_name = field.get('api_name', '')
        label = field.get('field_label', api_name)
        enable_colour = 'Yes' if field.get('enable_colour_code', False) else 'No'
        content += f"| {label} | {api_name} | picklist | {enable_colour} |\n"
    
    content += f"""\n---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
**Source:** Zoho CRM Export {SOURCE_LABEL}
"""
    
    return content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate module documentation from Zoho exports")
    parser.add_argument("--date", help="Export date (YYYY-MM-DD). Defaults to latest export.")
    parser.add_argument("--modules", help="Comma-separated module API names. Defaults to all modules in export.")
    parser.add_argument("--write-journey", action="store_true", help="Also write customer journey JSON (manual files).")
    return parser.parse_args()


def create_module_docs(module_name, data_model, dependencies, write_journey=False):
    """Create all documentation files for a module."""

    print(f"Generating documentation for {module_name}...")

    fields = extract_module_fields(data_model, module_name)
    workflows = extract_module_workflows(dependencies, module_name)
    lookups = extract_module_lookups(dependencies, module_name)

    print(f"  Fields: {len(fields)}")
    print(f"  Workflows: {len(workflows)}")
    print(f"  Lookups: {len(lookups)}")

    module_dir = MODULES_DIR / module_name.lower()
    docs_dir = module_dir / 'docs'
    data_dir = module_dir / 'data'
    diagrams_dir = module_dir / 'diagrams'

    docs_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    diagrams_dir.mkdir(parents=True, exist_ok=True)

    files_created = []

    fields_content = generate_fields_md(module_name, fields)
    fields_path = docs_dir / f"{module_name.lower()}-fields.md"
    fields_path.write_text(fields_content)
    files_created.append(fields_path)

    workflows_content = generate_workflows_md(module_name, workflows)
    workflows_path = docs_dir / f"{module_name.lower()}-workflows.md"
    workflows_path.write_text(workflows_content)
    files_created.append(workflows_path)

    urls_content = generate_workflow_urls_md(module_name, workflows)
    urls_path = docs_dir / f"{module_name.lower()}-workflow-urls.md"
    urls_path.write_text(urls_content)
    files_created.append(urls_path)

    usage_content = generate_usage_md(module_name, fields, workflows, lookups)
    usage_path = docs_dir / f"{module_name.lower()}-usage.md"
    usage_path.write_text(usage_content)
    files_created.append(usage_path)

    # Generate status-map if status/stage fields exist
    status_map_content = generate_status_map_md(module_name, fields)
    if status_map_content:
        status_map_path = docs_dir / f"{module_name.lower()}-status-map.md"
        status_map_path.write_text(status_map_content)
        files_created.append(status_map_path)

    if write_journey:
        journey_data = generate_customer_journey_json(module_name, workflows)
        journey_path = data_dir / f"customer-journey-{module_name.lower()}.json"
        journey_path.write_text(json.dumps(journey_data, indent=2))
        files_created.append(journey_path)

    print(f"  Created {len(files_created)} files")

    return files_created


def main():
    args = parse_args()

    export = (
        get_export_by_date(args.date, export_directory()).ensure_both()
        if args.date
        else get_latest_export(export_directory()).ensure_both()
    )

    global DATA_MODEL_PATH, DEPENDENCIES_PATH, SOURCE_LABEL, SOURCE_DEP_LABEL, MODULES_DIR
    DATA_MODEL_PATH = export.data_model
    DEPENDENCIES_PATH = export.dependencies
    SOURCE_LABEL = export.data_model.name
    SOURCE_DEP_LABEL = export.dependencies.name
    MODULES_DIR = ROOT_DIR / "modules"

    data_model = load_json(DATA_MODEL_PATH)
    dependencies = load_json(DEPENDENCIES_PATH)

    modules = (
        [m.strip() for m in args.modules.split(",") if m.strip()]
        if args.modules
        else sorted(data_model.keys())
    )

    print("=" * 60)
    print(f"GENERATE MODULE DOCUMENTATION (export {export.date})")
    print("=" * 60)
    print()

    all_files = []

    for module in modules:
        files = create_module_docs(module, data_model, dependencies, write_journey=args.write_journey)
        all_files.extend(files)
        print()

    print("=" * 60)
    print(f"Total files created: {len(all_files)}")
    print("=" * 60)

    for f in all_files:
        print(f"  - {f.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()
