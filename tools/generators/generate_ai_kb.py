#!/usr/bin/env python3
"""
AI Knowledge Base Generator for Claude Projects.

Generates optimised markdown documentation from Zoho CRM exports
for use as context in Claude AI conversations.

Output: ai_kb/*.md (~100-150KB total)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

TOOLS_DIR = Path(__file__).resolve().parents[1]  # tools/ directory
ROOT_DIR = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export  # noqa: E402

# Output configuration
OUTPUT_DIR = ROOT_DIR / "ai_kb"
REPORTS_DIR = ROOT_DIR / "reports"
MODELS_DIR = ROOT_DIR / "models"

# Module classification
TIER1_MODULES = {
    "Leads", "Contacts", "Accounts", "Deals", "Courses",
    "Registration_Records", "Invoices", "Quotes"
}
EXCLUDED_PREFIXES = ("zohosign__", "clicksendext__")
EXCLUDED_SUFFIXES = ("_Insights__s",)

# Export diff filename pattern
DIFF_PATTERN = re.compile(r"export_diff_(\d{4}-\d{2}-\d{2})_vs_(\d{4}-\d{2}-\d{2})\.json$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate AI Knowledge Base documentation from Zoho CRM exports"
    )
    parser.add_argument(
        "--date",
        help="Export date (YYYY-MM-DD). Defaults to latest export."
    )
    parser.add_argument(
        "--diff-json",
        help="Path to export_diff_*.json file. Defaults to latest in reports/"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be generated without writing files"
    )
    parser.add_argument(
        "--output-dir",
        help=f"Override output directory (default: {OUTPUT_DIR})"
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    """Load JSON file."""
    return json.loads(path.read_text())


def get_latest_diff(reports_dir: Path) -> Optional[Path]:
    """Find most recent export_diff_*.json by filename date."""
    diffs = []
    for entry in reports_dir.glob("export_diff_*.json"):
        match = DIFF_PATTERN.match(entry.name)
        if match:
            new_date = match.group(1)
            diffs.append((new_date, entry))
    
    if not diffs:
        return None
    
    # Sort by new_date descending
    diffs.sort(reverse=True)
    return diffs[0][1]


def is_excluded_module(module_name: str) -> bool:
    """Check if module should be excluded from documentation."""
    if module_name.startswith(EXCLUDED_PREFIXES):
        return True
    if module_name.endswith(EXCLUDED_SUFFIXES):
        return True
    return False


def classify_modules(data_model: dict) -> Tuple[List[str], List[str], List[str]]:
    """
    Returns (tier1, tier2, excluded) module lists.
    
    Tier1: Always-include list + top modules by activity
    Tier2: Remaining non-excluded modules
    Excluded: Prefix/suffix matches
    """
    modules_metadata = data_model.get("modules", {})
    
    tier1 = []
    tier2 = []
    excluded = []
    
    # Calculate activity score for auto-detection
    activity_scores = []
    for module_name, module_data in modules_metadata.items():
        if is_excluded_module(module_name):
            excluded.append(module_name)
            continue
        
        field_count = module_data.get("field_count", 0)
        workflow_count = module_data.get("workflow_count", 0)
        score = field_count + (workflow_count * 5)  # Weight workflows higher
        activity_scores.append((module_name, score))
    
    # Sort by activity score
    activity_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Build tier1: forced includes + high activity modules
    for module_name, score in activity_scores:
        if module_name in TIER1_MODULES or score > 50:  # Threshold for auto-inclusion
            tier1.append(module_name)
        else:
            tier2.append(module_name)
    
    # Ensure all forced tier1 modules are included
    for module in TIER1_MODULES:
        if module not in tier1 and module in modules_metadata:
            tier1.append(module)
            if module in tier2:
                tier2.remove(module)
    
    return sorted(tier1), sorted(tier2), sorted(excluded)


def generate_system_overview(data_model: dict, export_date: str) -> str:
    """
    Generate SYSTEM_OVERVIEW.md with module catalogue and stats.
    Target size: ~15-20 KB
    """
    metadata = data_model.get("metadata", {})
    modules_data = data_model.get("modules", {})
    
    # Classify modules
    tier1, tier2, excluded = classify_modules(data_model)
    
    lines = []
    
    # Header
    lines.append("# Zoho CRM System Overview")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Source Export:** {export_date}")
    lines.append(f"**Data Model:** `models/CRM_DATA_MODEL.json`")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Executive Summary
    lines.append("## Executive Summary {#executive-summary}")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Modules | {metadata.get('total_modules', 0)} |")
    lines.append(f"| Total Fields | {metadata.get('total_fields', 0)} |")
    lines.append(f"| Total Workflows | {metadata.get('total_workflows', 0)} |")
    lines.append(f"| Active Workflows | {metadata.get('total_active_workflows', 0)} |")
    lines.append(f"| Lookup Relationships | {metadata.get('total_lookup_relationships', 0)} |")
    lines.append(f"| Tier 1 Modules (Core) | {len(tier1)} |")
    lines.append(f"| Tier 2 Modules | {len(tier2)} |")
    lines.append(f"| Excluded Modules | {len(excluded)} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Module Catalogue - Tier 1
    lines.append("## Tier 1 Modules (Core Business) {#tier1-modules}")
    lines.append("")
    lines.append("These are the primary business modules with significant configuration.")
    lines.append("")
    lines.append("| Module | Fields | Workflows | Active WF | Lookups | Referenced By |")
    lines.append("|--------|--------|-----------|-----------|---------|---------------|")
    
    for module_name in tier1:
        if module_name not in modules_data:
            continue
        mod = modules_data[module_name]
        fields = mod.get("field_count", 0)
        workflows = mod.get("workflow_count", 0)
        active_wf = mod.get("active_workflow_count", 0)
        lookups = mod.get("lookup_field_count", 0)
        ref_by = len(mod.get("referenced_by", []))
        lines.append(f"| {module_name} | {fields} | {workflows} | {active_wf} | {lookups} | {ref_by} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Module Catalogue - Tier 2
    lines.append("## Tier 2 Modules (Supporting) {#tier2-modules}")
    lines.append("")
    lines.append("Supporting modules with lighter configuration.")
    lines.append("")
    lines.append("| Module | Fields | Workflows | Lookups |")
    lines.append("|--------|--------|-----------|---------|")
    
    for module_name in tier2:
        if module_name not in modules_data:
            continue
        mod = modules_data[module_name]
        fields = mod.get("field_count", 0)
        workflows = mod.get("workflow_count", 0)
        lookups = mod.get("lookup_field_count", 0)
        lines.append(f"| {module_name} | {fields} | {workflows} | {lookups} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Business Domain Groupings
    lines.append("## Business Domain Groupings {#domain-groupings}")
    lines.append("")
    
    # Group modules by common patterns
    domains = {
        "Sales Pipeline": ["Leads", "Contacts", "Accounts", "Deals", "Campaigns"],
        "Quoting & Billing": ["Quotes", "Sales_Orders", "Invoices", "Purchase_Orders", "Products", "Price_Books"],
        "Education & Training": ["Courses", "Registration_Records", "Attendees", "Venues", "Course_Days", 
                                "Course_Tasks", "Course_Performance", "Course_Type_History"],
        "Task Management": ["Tasks", "Team_Tasks", "Recurring_Tasks", "Projects_Tasks", "Events"],
        "Customer Service": ["Cases", "Solutions", "Feedbacks"],
        "Marketing": ["Campaigns", "Cold_Outreach", "Referral_Form"],
        "Analytics": ["Email_Analytics", "Email_Sentiment"],
    }
    
    for domain, expected_modules in domains.items():
        found = [m for m in expected_modules if m in modules_data and not is_excluded_module(m)]
        if found:
            lines.append(f"### {domain}")
            lines.append("")
            lines.append(", ".join(found))
            lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Relationship Summary
    lines.append("## Most Referenced Modules {#most-referenced}")
    lines.append("")
    lines.append("Modules that are frequently referenced by other modules (high integration points).")
    lines.append("")
    
    # Calculate reference counts
    ref_counts = []
    for module_name, mod in modules_data.items():
        if is_excluded_module(module_name):
            continue
        ref_by = mod.get("referenced_by", [])
        if ref_by:
            ref_counts.append((module_name, len(ref_by), ref_by))
    
    ref_counts.sort(key=lambda x: x[1], reverse=True)
    
    lines.append("| Module | Referenced By (Count) | Referencing Modules |")
    lines.append("|--------|----------------------|---------------------|")
    
    for module_name, count, ref_by in ref_counts[:15]:  # Top 15
        ref_list = ", ".join(ref_by[:5])  # Show first 5
        if len(ref_by) > 5:
            ref_list += f", +{len(ref_by) - 5} more"
        lines.append(f"| {module_name} | {count} | {ref_list} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Cross-references
    lines.append("## Related Documentation {#related-docs}")
    lines.append("")
    lines.append("- **LATEST_CHANGES.md** - Recent configuration changes between exports")
    lines.append("- **WORKFLOW_DEPENDENCY_MAP.md** - Impact analysis for workflow modifications")
    lines.append("- **FIELD_REFERENCE.md** - Detailed field specifications and picklist values")
    lines.append("- **CHANGE_PLANNING_GUIDE.md** - Best practices for making CRM changes")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by `tools/generate_ai_kb.py` on {datetime.now().strftime('%Y-%m-%d')}*")
    lines.append("")
    
    return "\n".join(lines)


def build_field_workflow_index(dependencies: dict) -> Dict[str, Dict[str, List[Dict]]]:
    """
    Build reverse index: module -> field -> list of workflows using that field.
    
    Returns: {module: {field_name: [{"workflow": "...", "usage_type": "..."}]}}
    """
    field_deps = dependencies.get("field_dependencies", {})
    index = defaultdict(lambda: defaultdict(list))
    
    for field_key, field_info in field_deps.items():
        # Parse "Module.FieldName" format
        if "." not in field_key:
            continue
        module, field_name = field_key.split(".", 1)
        
        workflows = field_info.get("used_in_workflows", [])
        if workflows:
            index[module][field_name] = workflows
    
    return dict(index)


def assess_workflow_risk(workflow: dict, field_usage_count: int, has_cross_module: bool) -> str:
    """
    Assess risk level for workflow changes.
    
    HIGH: Cross-module actions or heavy field usage
    MEDIUM: Create/update triggers with field dependencies
    LOW: Simple, isolated workflows
    """
    if has_cross_module or field_usage_count > 3:
        return "HIGH"
    
    trigger = workflow.get("trigger_type", "unknown")
    if trigger in ("create", "field_update", "date_or_datetime") and field_usage_count > 0:
        return "MEDIUM"
    
    return "LOW"


def generate_workflow_dependency_map(
    data_model: dict,
    dependencies: dict,
    export_date: str
) -> str:
    """
    Generate WORKFLOW_DEPENDENCY_MAP.md with impact analysis.
    Target size: ~25-35 KB
    """
    # Build field-to-workflow index
    field_workflow_index = build_field_workflow_index(dependencies)
    
    # Get workflow details from dependencies (more accurate than data_model)
    workflow_deps = dependencies.get("workflow_dependencies", {})
    lookup_rels = dependencies.get("lookup_relationships", {})
    
    # Group workflows by module
    modules_workflows = defaultdict(list)
    risk_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    
    for wf_key, wf_data in workflow_deps.items():
        module = wf_data.get("module")
        if not module or is_excluded_module(module):
            continue
        
        # Enrich with field usage
        fields_used = []
        if module in field_workflow_index:
            wf_name = wf_data.get("workflow_name", "")
            for field_name, workflows in field_workflow_index[module].items():
                for wf_ref in workflows:
                    if wf_ref.get("workflow") == wf_name:
                        fields_used.append({
                            "field": field_name,
                            "usage": wf_ref.get("usage_type", "unknown")
                        })
        
        # Assess risk
        has_cross_module = len(wf_data.get("cross_module_actions", [])) > 0
        field_usage_count = len(fields_used)
        risk = assess_workflow_risk(wf_data, field_usage_count, has_cross_module)
        risk_counts[risk] += 1
        
        # Store enriched workflow
        modules_workflows[module].append({
            "id": wf_data.get("workflow_id"),
            "name": wf_data.get("workflow_name", "Unnamed"),
            "active": wf_data.get("active", False),
            "trigger_type": wf_data.get("trigger_type", "unknown"),
            "condition_fields": wf_data.get("condition_fields", []),
            "updated_fields": wf_data.get("updated_fields", []),
            "cross_module_actions": wf_data.get("cross_module_actions", []),
            "fields_used": fields_used,
            "risk": risk,
        })
    
    # Sort modules by workflow count
    sorted_modules = sorted(modules_workflows.items(), key=lambda x: len(x[1]), reverse=True)
    
    lines = []
    
    # Header
    lines.append("# Workflow Dependency Map")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Source Export:** {export_date}")
    lines.append(f"**Purpose:** Impact analysis for workflow and field changes")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Executive Summary
    lines.append("## Executive Summary {#summary}")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Workflows | {sum(len(wfs) for _, wfs in sorted_modules)} |")
    lines.append(f"| Modules with Workflows | {len(sorted_modules)} |")
    lines.append(f"| HIGH Risk Workflows | {risk_counts['HIGH']} |")
    lines.append(f"| MEDIUM Risk Workflows | {risk_counts['MEDIUM']} |")
    lines.append(f"| LOW Risk Workflows | {risk_counts['LOW']} |")
    lines.append("")
    lines.append("**Risk Levels:**")
    lines.append("- **HIGH**: Cross-module actions or complex field dependencies (3+ fields)")
    lines.append("- **MEDIUM**: Triggers with field dependencies or create/update workflows")
    lines.append("- **LOW**: Simple workflows with minimal dependencies")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Table of Contents
    lines.append("## Table of Contents {#toc}")
    lines.append("")
    for module, wfs in sorted_modules[:20]:  # Top 20 modules
        count = len(wfs)
        high_risk = sum(1 for w in wfs if w["risk"] == "HIGH")
        risk_indicator = f" ⚠️ {high_risk} high-risk" if high_risk > 0 else ""
        lines.append(f"- [{module} ({count} workflows)](#module-{module.lower()}){risk_indicator}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Workflows by Module
    for module, workflows in sorted_modules:
        module_anchor = module.lower().replace("_", "-")
        lines.append(f"## {module} {{#module-{module_anchor}}}")
        lines.append("")
        lines.append(f"**Total Workflows:** {len(workflows)}")
        
        # Count by risk
        module_risk_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        for wf in workflows:
            module_risk_counts[wf["risk"]] += 1
        
        lines.append(f"**Risk Distribution:** HIGH: {module_risk_counts['HIGH']}, MEDIUM: {module_risk_counts['MEDIUM']}, LOW: {module_risk_counts['LOW']}")
        lines.append("")
        
        # Lookup relationships for this module
        module_lookups = lookup_rels.get(module, [])
        if module_lookups:
            lines.append("**Outbound Lookups:**")
            for lookup in module_lookups[:5]:  # Show first 5
                lines.append(f"- {lookup.get('field_label', lookup.get('field_name'))} → {lookup.get('lookup_module')}")
            if len(module_lookups) > 5:
                lines.append(f"- *+{len(module_lookups) - 5} more*")
            lines.append("")
        
        lines.append("---")
        lines.append("")
        
        # List workflows (compact view for most, detailed for high-risk)
        for wf in sorted(workflows, key=lambda w: (w["risk"] == "HIGH", w["risk"] == "MEDIUM", w["name"]), reverse=True):
            wf_anchor = f"{module_anchor}-{wf['id']}"
            risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(wf["risk"], "⚪")
            
            lines.append(f"### {risk_emoji} {wf['name']} {{#{wf_anchor}}}")
            lines.append("")
            lines.append("| Property | Value |")
            lines.append("|----------|-------|")
            lines.append(f"| **ID** | `{wf['id']}` |")
            lines.append(f"| **Status** | {'✅ Active' if wf['active'] else '❌ Inactive'} |")
            lines.append(f"| **Trigger** | {wf['trigger_type'].replace('_', ' ').title()} |")
            lines.append(f"| **Risk Level** | {wf['risk']} |")
            lines.append("")
            
            # Trigger details
            if wf["trigger_type"] == "create":
                lines.append("**Trigger:** Fires when a new record is created")
            elif wf["trigger_type"] == "field_update":
                if wf["condition_fields"]:
                    lines.append(f"**Trigger Fields:** {', '.join(wf['condition_fields'])}")
                else:
                    lines.append("**Trigger:** Fires on any field update")
            elif wf["trigger_type"] == "date_or_datetime":
                lines.append("**Trigger:** Time-based (scheduled)")
            else:
                lines.append(f"**Trigger:** {wf['trigger_type']}")
            lines.append("")
            
            # Field dependencies
            if wf["fields_used"]:
                condition_fields = [f["field"] for f in wf["fields_used"] if f["usage"] == "condition"]
                action_fields = [f["field"] for f in wf["fields_used"] if f["usage"] == "action"]
                
                if condition_fields:
                    lines.append(f"**Fields Read (Conditions):** {', '.join(condition_fields)}")
                if action_fields:
                    lines.append(f"**Fields Updated (Actions):** {', '.join(action_fields)}")
                if not condition_fields and not action_fields:
                    lines.append(f"**Fields Referenced:** {', '.join(f['field'] for f in wf['fields_used'])}")
                lines.append("")
            
            # Cross-module actions
            if wf["cross_module_actions"]:
                lines.append("**Cross-Module Actions:**")
                for action in wf["cross_module_actions"][:3]:  # Show first 3
                    lines.append(f"- {action}")
                if len(wf["cross_module_actions"]) > 3:
                    lines.append(f"- *+{len(wf['cross_module_actions']) - 3} more*")
                lines.append("")
            
            # Impact analysis
            lines.append("**Impact Analysis:**")
            
            if not wf["active"]:
                lines.append("- **Currently Inactive** - No immediate impact from changes")
            else:
                if wf["trigger_type"] == "create":
                    lines.append(f"- **If disabled:** New {module} records won't trigger this automation")
                    lines.append("- **If trigger modified:** N/A (always fires on create)")
                elif wf["trigger_type"] == "field_update":
                    if wf["condition_fields"]:
                        lines.append(f"- **If disabled:** Changes to {', '.join(wf['condition_fields'])} won't trigger automation")
                        lines.append(f"- **If trigger fields renamed/removed:** Workflow will break")
                    else:
                        lines.append("- **If disabled:** Field updates won't trigger this automation")
                else:
                    lines.append(f"- **If disabled:** {wf['trigger_type']} triggers won't fire")
                
                if wf["fields_used"]:
                    field_count = len(wf["fields_used"])
                    lines.append(f"- **Field dependencies:** {field_count} field(s) - changes may break conditions/actions")
                
                if wf["cross_module_actions"]:
                    lines.append("- **⚠️ Cross-module impact:** Changes may affect related modules")
            
            lines.append("")
            lines.append("---")
            lines.append("")
    
    # Footer with cross-references
    lines.append("## Related Documentation {#related-docs}")
    lines.append("")
    lines.append("- **SYSTEM_OVERVIEW.md** - Module catalogue and relationship summary")
    lines.append("- **FIELD_REFERENCE.md** - Detailed field specifications")
    lines.append("- **CHANGE_PLANNING_GUIDE.md** - Pre-change checklists and best practices")
    lines.append("- **LATEST_CHANGES.md** - Recent workflow modifications")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by `tools/generate_ai_kb.py` on {datetime.now().strftime('%Y-%m-%d')}*")
    lines.append("")
    
    return "\n".join(lines)


def generate_latest_changes(diff: dict) -> str:
    """
    Generate LATEST_CHANGES.md from export diff.
    Target size: ~10-15 KB
    """
    old_date = diff.get("old_date", "unknown")
    new_date = diff.get("new_date", "unknown")
    modules_diff = diff.get("modules", {})
    
    lines = []
    
    # Header
    lines.append("# Latest CRM Configuration Changes")
    lines.append("")
    lines.append(f"**Comparison:** {new_date} vs {old_date}")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Source:** `reports/export_diff_{new_date}_vs_{old_date}.json`")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Executive Summary
    lines.append("## Executive Summary {#summary}")
    lines.append("")
    
    modules_added = modules_diff.get("added", [])
    modules_removed = modules_diff.get("removed", [])
    modules_modified = modules_diff.get("modified", {})
    
    # Count changes
    modules_with_changes = 0
    total_fields_added = 0
    total_fields_removed = 0
    total_fields_changed = 0
    total_workflows_added = 0
    total_workflows_removed = 0
    total_workflows_changed = 0
    
    for mod_name, changes in modules_modified.items():
        has_changes = (
            changes.get("fields_added") or
            changes.get("fields_removed") or
            changes.get("fields_changed") or
            changes.get("workflows_added") or
            changes.get("workflows_removed") or
            changes.get("workflows_changed")
        )
        if has_changes:
            modules_with_changes += 1
        total_fields_added += len(changes.get("fields_added", []))
        total_fields_removed += len(changes.get("fields_removed", []))
        total_fields_changed += len(changes.get("fields_changed", []))
        total_workflows_added += len(changes.get("workflows_added", []))
        total_workflows_removed += len(changes.get("workflows_removed", []))
        total_workflows_changed += len(changes.get("workflows_changed", []))
    
    lines.append("| Category | Count |")
    lines.append("|----------|-------|")
    lines.append(f"| Modules Added | {len(modules_added)} |")
    lines.append(f"| Modules Removed | {len(modules_removed)} |")
    lines.append(f"| Modules Modified | {modules_with_changes} |")
    lines.append(f"| Fields Added | {total_fields_added} |")
    lines.append(f"| Fields Removed | {total_fields_removed} |")
    lines.append(f"| Fields Changed | {total_fields_changed} |")
    lines.append(f"| Workflows Added | {total_workflows_added} |")
    lines.append(f"| Workflows Removed | {total_workflows_removed} |")
    lines.append(f"| Workflows Changed | {total_workflows_changed} |")
    lines.append("")
    
    if not any([modules_added, modules_removed, modules_with_changes]):
        lines.append("> **No configuration changes detected between these exports.**")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Modules Added/Removed
    lines.append("## Module Changes {#module-changes}")
    lines.append("")
    
    if modules_added:
        lines.append("### Added Modules")
        lines.append("")
        for mod in modules_added:
            lines.append(f"- **{mod}** (new module)")
        lines.append("")
    
    if modules_removed:
        lines.append("### Removed Modules")
        lines.append("")
        for mod in modules_removed:
            lines.append(f"- **{mod}** (deleted)")
        lines.append("")
    
    if not modules_added and not modules_removed:
        lines.append("No modules added or removed.")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Field Changes by Module
    lines.append("## Field Changes by Module {#field-changes}")
    lines.append("")
    
    field_changes_found = False
    for mod_name in sorted(modules_modified.keys()):
        changes = modules_modified[mod_name]
        fields_added = changes.get("fields_added", [])
        fields_removed = changes.get("fields_removed", [])
        fields_changed = changes.get("fields_changed", [])
        
        if not (fields_added or fields_removed or fields_changed):
            continue
        
        field_changes_found = True
        lines.append(f"### {mod_name}")
        lines.append("")
        
        if fields_added:
            lines.append(f"**Added ({len(fields_added)}):** {', '.join(fields_added)}")
            lines.append("")
        
        if fields_removed:
            lines.append(f"**Removed ({len(fields_removed)}):** {', '.join(fields_removed)}")
            lines.append("")
        
        if fields_changed:
            lines.append(f"**Modified ({len(fields_changed)}):**")
            lines.append("")
            for change in fields_changed:
                field_name = change.get("field", "unknown")
                change_types = change.get("changes", {})
                
                lines.append(f"- **{field_name}**")
                
                # Show picklist changes inline
                if "pick_list_values" in change_types:
                    pl_change = change_types["pick_list_values"]
                    old_vals = set(pl_change.get("old", []))
                    new_vals = set(pl_change.get("new", []))
                    added_vals = new_vals - old_vals
                    removed_vals = old_vals - new_vals
                    
                    if added_vals:
                        lines.append(f"  - Added values: {', '.join(sorted(added_vals))}")
                    if removed_vals:
                        lines.append(f"  - Removed values: {', '.join(sorted(removed_vals))}")
                
                # Show other property changes
                other_changes = [k for k in change_types.keys() if k != "pick_list_values"]
                if other_changes:
                    lines.append(f"  - Properties changed: {', '.join(other_changes)}")
                
                lines.append("")
        
        lines.append("---")
        lines.append("")
    
    if not field_changes_found:
        lines.append("No field changes detected.")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Workflow Changes by Module
    lines.append("## Workflow Changes by Module {#workflow-changes}")
    lines.append("")
    
    workflow_changes_found = False
    for mod_name in sorted(modules_modified.keys()):
        changes = modules_modified[mod_name]
        workflows_added = changes.get("workflows_added", [])
        workflows_removed = changes.get("workflows_removed", [])
        workflows_changed = changes.get("workflows_changed", [])
        
        if not (workflows_added or workflows_removed or workflows_changed):
            continue
        
        workflow_changes_found = True
        lines.append(f"### {mod_name}")
        lines.append("")
        
        if workflows_added:
            lines.append(f"**Added ({len(workflows_added)}):**")
            for wf_id in workflows_added:
                lines.append(f"- Workflow ID: `{wf_id}`")
            lines.append("")
        
        if workflows_removed:
            lines.append(f"**Removed ({len(workflows_removed)}):**")
            for wf_id in workflows_removed:
                lines.append(f"- Workflow ID: `{wf_id}`")
            lines.append("")
        
        if workflows_changed:
            lines.append(f"**Modified ({len(workflows_changed)}):**")
            lines.append("")
            for change in workflows_changed:
                wf_id = change.get("workflow", "unknown")
                change_types = change.get("changes", {})
                
                lines.append(f"- **{wf_id}**")
                
                # Show status changes prominently
                if "status" in change_types:
                    status_change = change_types["status"]
                    old_status = status_change.get("old", "unknown")
                    new_status = status_change.get("new", "unknown")
                    lines.append(f"  - Status: {old_status} → {new_status}")
                
                # Show other changes
                other_changes = [k for k in change_types.keys() if k != "status"]
                if other_changes:
                    lines.append(f"  - Also changed: {', '.join(other_changes)}")
                
                lines.append("")
        
        lines.append("---")
        lines.append("")
    
    if not workflow_changes_found:
        lines.append("No workflow changes detected.")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Lookup Relationship Changes
    lines.append("## Lookup Relationship Changes {#lookup-changes}")
    lines.append("")
    
    lookup_diff = diff.get("lookup_relationships", {})
    lookup_changes_found = False
    
    for mod_name in sorted(lookup_diff.keys()):
        rel_changes = lookup_diff[mod_name]
        added = rel_changes.get("added_lookup_fields", [])
        removed = rel_changes.get("removed_lookup_fields", [])
        
        if not (added or removed):
            continue
        
        lookup_changes_found = True
        lines.append(f"### {mod_name}")
        lines.append("")
        
        if added:
            lines.append(f"**Added lookup fields:** {', '.join(added)}")
            lines.append("")
        
        if removed:
            lines.append(f"**Removed lookup fields:** {', '.join(removed)}")
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    if not lookup_changes_found:
        lines.append("No lookup relationship changes detected.")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Impact Notes
    lines.append("## Impact Assessment {#impact}")
    lines.append("")
    lines.append("**Important:** Changes to fields, workflows, and lookups can have downstream effects.")
    lines.append("")
    lines.append("- **Added/removed fields:** Check dependent workflows and API integrations")
    lines.append("- **Picklist changes:** Verify workflow conditions and filters")
    lines.append("- **New workflows:** Review for conflicts with existing automations")
    lines.append("- **Lookup changes:** Validate related module dependencies")
    lines.append("")
    lines.append("**See also:** CHANGE_PLANNING_GUIDE.md for pre-change checklists and WORKFLOW_DEPENDENCY_MAP.md for detailed impact analysis.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by `tools/generate_ai_kb.py` on {datetime.now().strftime('%Y-%m-%d')}*")
    lines.append("")
    
    return "\n".join(lines)


def generate_field_reference(
    data_model: dict,
    dependencies: dict,
    export_date: str
) -> str:
    """
    Generate FIELD_REFERENCE.md with field specifications.
    Target size: 40-50 KB
    
    Tier 1: Full detail with picklist values
    Tier 2: Summary only
    """
    modules_data = data_model.get("modules", {})
    field_workflow_index = build_field_workflow_index(dependencies)
    tier1, tier2, excluded = classify_modules(data_model)
    
    lines = []
    
    # Header
    lines.append("# Field Reference Guide")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Source Export:** {export_date}")
    lines.append(f"**Purpose:** Quick field lookup and specification reference")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Executive Summary
    total_fields = sum(m.get("field_count", 0) for m in modules_data.values())
    tier1_fields = sum(modules_data.get(m, {}).get("field_count", 0) for m in tier1 if m in modules_data)
    
    lines.append("## Overview {#overview}")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Fields (All Modules) | {total_fields} |")
    lines.append(f"| Tier 1 Module Fields | {tier1_fields} |")
    lines.append(f"| Tier 1 Modules (Full Detail) | {len(tier1)} |")
    lines.append(f"| Tier 2 Modules (Summary) | {len(tier2)} |")
    lines.append("")
    lines.append("**Documentation Levels:**")
    lines.append("- **Tier 1**: Complete field listings with picklist values and lookup targets")
    lines.append("- **Tier 2**: Summary statistics and lookup fields only")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Table of Contents
    lines.append("## Table of Contents {#toc}")
    lines.append("")
    lines.append("### Tier 1 Modules (Full Detail)")
    for module in sorted(tier1):
        if module in modules_data:
            count = modules_data[module].get("field_count", 0)
            lines.append(f"- [{module} ({count} fields)](#module-{module.lower()})")
    lines.append("")
    lines.append("### Tier 2 Modules (Summary)")
    for module in sorted(tier2)[:15]:  # First 15
        if module in modules_data:
            count = modules_data[module].get("field_count", 0)
            lines.append(f"- [{module} ({count} fields)](#module-{module.lower()})")
    if len(tier2) > 15:
        lines.append(f"- *+{len(tier2) - 15} more modules*")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Tier 1 Modules - Full Detail
    lines.append("# Tier 1 Modules - Full Field Reference {#tier1}")
    lines.append("")
    
    for module_name in sorted(tier1):
        if module_name not in modules_data:
            continue
        
        module = modules_data[module_name]
        fields = module.get("fields", {})
        
        if not fields:
            continue
        
        module_anchor = module_name.lower().replace("_", "-")
        lines.append(f"## {module_name} {{#module-{module_anchor}}}")
        lines.append("")
        lines.append(f"**Total Fields:** {len(fields)}")
        lines.append(f"**Custom Fields:** {module.get('custom_field_count', 0)}")
        lines.append(f"**Lookup Fields:** {module.get('lookup_field_count', 0)}")
        lines.append("")
        
        # Group fields by type
        standard_fields = []
        custom_fields = []
        lookup_fields = []
        
        for field_name, field_data in fields.items():
            field_info = {
                "name": field_data.get("display_label", field_name),
                "api_name": field_name,
                "type": field_data.get("data_type", "unknown"),
                "required": field_data.get("system_mandatory", False) or field_data.get("required", False),
                "custom": field_data.get("custom_field", False),
                "picklist": field_data.get("picklist_values", []),
                "lookup_module": field_data.get("lookup_module"),
                "in_workflow": field_name in field_workflow_index.get(module_name, {})
            }
            
            if field_info["type"] in ("lookup", "ownerlookup", "userlookup"):
                lookup_fields.append(field_info)
            elif field_info["custom"]:
                custom_fields.append(field_info)
            else:
                standard_fields.append(field_info)
        
        # Standard Fields Table
        if standard_fields:
            lines.append("### Standard Fields")
            lines.append("")
            lines.append("| Field | API Name | Type | Required | Details |")
            lines.append("|-------|----------|------|----------|---------|")
            
            for field in sorted(standard_fields, key=lambda f: f["api_name"]):
                req = "✓" if field["required"] else ""
                wf = " 🔄" if field["in_workflow"] else ""
                
                # Format picklist values inline (truncate if too long)
                details = ""
                if field["picklist"] and field["type"] == "picklist":
                    values = []
                    for v in field["picklist"][:5]:
                        if isinstance(v, dict):
                            val = v.get("actual_value") or v.get("display_value")
                        else:
                            val = str(v)
                        if val:
                            values.append(val)
                    details = ", ".join(values)
                    if len(field["picklist"]) > 5:
                        details += f", +{len(field['picklist']) - 5} more"
                
                lines.append(f"| {field['name']}{wf} | {field['api_name']} | {field['type']} | {req} | {details} |")
            
            lines.append("")
        
        # Custom Fields Table
        if custom_fields:
            lines.append("### Custom Fields")
            lines.append("")
            lines.append("| Field | API Name | Type | Required | Details |")
            lines.append("|-------|----------|------|----------|---------|")
            
            for field in sorted(custom_fields, key=lambda f: f["api_name"]):
                req = "✓" if field["required"] else ""
                wf = " 🔄" if field["in_workflow"] else ""
                
                details = ""
                if field["picklist"] and field["type"] == "picklist":
                    values = []
                    for v in field["picklist"][:5]:
                        if isinstance(v, dict):
                            val = v.get("actual_value") or v.get("display_value")
                        else:
                            val = str(v)
                        if val:
                            values.append(val)
                    details = ", ".join(values)
                    if len(field["picklist"]) > 5:
                        details += f", +{len(field['picklist']) - 5} more"
                
                lines.append(f"| {field['name']}{wf} | {field['api_name']} | {field['type']} | {req} | {details} |")
            
            lines.append("")
        
        # Lookup Fields Table
        if lookup_fields:
            lines.append("### Lookup Fields")
            lines.append("")
            lines.append("| Field | API Name | Target Module | Required |")
            lines.append("|-------|----------|---------------|----------|")
            
            for field in sorted(lookup_fields, key=lambda f: f["api_name"]):
                req = "✓" if field["required"] else ""
                target = field["lookup_module"] or "Unknown"
                wf = " 🔄" if field["in_workflow"] else ""
                lines.append(f"| {field['name']}{wf} | {field['api_name']} | → {target} | {req} |")
            
            lines.append("")
        
        lines.append("**Legend:** 🔄 = Used in workflows")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Tier 2 Modules - Summary Only
    lines.append("# Tier 2 Modules - Summary Reference {#tier2}")
    lines.append("")
    lines.append("Summary statistics for supporting modules. See SYSTEM_OVERVIEW.md for complete module relationships.")
    lines.append("")
    
    for module_name in sorted(tier2):
        if module_name not in modules_data:
            continue
        
        module = modules_data[module_name]
        fields = module.get("fields", {})
        
        if not fields:
            continue
        
        module_anchor = module_name.lower().replace("_", "-")
        lines.append(f"## {module_name} {{#module-{module_anchor}}}")
        lines.append("")
        lines.append(f"**Total Fields:** {len(fields)}")
        lines.append("")
        
        # Count by type
        type_counts = defaultdict(int)
        lookup_fields_list = []
        
        for field_name, field_data in fields.items():
            field_type = field_data.get("data_type", "unknown")
            type_counts[field_type] += 1
            
            if field_type in ("lookup", "ownerlookup", "userlookup"):
                lookup_module = field_data.get("lookup_module")
                if lookup_module:
                    lookup_fields_list.append(f"{field_data.get('display_label', field_name)} → {lookup_module}")
        
        # Type distribution table
        if type_counts:
            lines.append("| Type | Count |")
            lines.append("|------|-------|")
            for dtype, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True)[:8]:
                lines.append(f"| {dtype} | {count} |")
            lines.append("")
        
        # Lookup fields
        if lookup_fields_list:
            lines.append("**Lookup Fields:**")
            for lookup in lookup_fields_list[:5]:
                lines.append(f"- {lookup}")
            if len(lookup_fields_list) > 5:
                lines.append(f"- *+{len(lookup_fields_list) - 5} more*")
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    # Footer
    lines.append("## Related Documentation {#related-docs}")
    lines.append("")
    lines.append("- **SYSTEM_OVERVIEW.md** - Module catalogue and relationships")
    lines.append("- **WORKFLOW_DEPENDENCY_MAP.md** - Workflow and field dependencies")
    lines.append("- **LATEST_CHANGES.md** - Recent field modifications")
    lines.append("- **CHANGE_PLANNING_GUIDE.md** - Best practices for field changes")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by `tools/generate_ai_kb.py` on {datetime.now().strftime('%Y-%m-%d')}*")
    lines.append("")
    
    return "\n".join(lines)


def generate_change_planning_guide(
    data_model: dict,
    dependencies: dict,
    diff: dict
) -> str:
    """
    Generate CHANGE_PLANNING_GUIDE.md with best practices.
    Target size: 10-15 KB
    
    Uses real examples from current CRM data.
    """
    modules_data = data_model.get("modules", {})
    
    # Extract real examples
    leads_module = modules_data.get("Leads", {})
    courses_module = modules_data.get("Courses", {})
    reg_module = modules_data.get("Registration_Records", {})
    
    # Get some real field names
    lead_fields = list(leads_module.get("fields", {}).keys())[:5]
    
    # Get recent changes for examples
    modules_diff = diff.get("modules", {})
    recent_field_changes = []
    for mod_name, changes in modules_diff.get("modified", {}).items():
        for change in changes.get("picklists_changed", [])[:2]:
            recent_field_changes.append({
                "module": mod_name,
                "field": change.get("field"),
                "change": change.get("changes", {})
            })
    
    lines = []
    
    # Header
    lines.append("# CRM Change Planning Guide")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Purpose:** Best practices and checklists for safe CRM changes")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 1: Pre-Change Checklist
    lines.append("## Pre-Change Checklist {#checklist}")
    lines.append("")
    lines.append("Before making any CRM configuration change, verify:")
    lines.append("")
    lines.append("1. **Workflow Dependencies**")
    lines.append("   - Check WORKFLOW_DEPENDENCY_MAP.md for workflows using the field/module")
    lines.append("   - Identify trigger fields and condition fields")
    lines.append("   - Note any cross-module actions")
    lines.append("")
    lines.append("2. **Lookup Relationships**")
    lines.append("   - Review SYSTEM_OVERVIEW.md for modules that reference this one")
    lines.append("   - Check for cascading deletes or required lookups")
    lines.append("   - Identify integration points")
    lines.append("")
    lines.append("3. **Active Integrations**")
    lines.append("   - API integrations (Xero, WorkDrive, external systems)")
    lines.append("   - Webhooks and scheduled workflows")
    lines.append("   - Third-party extensions (ZohoSign, ClickSend)")
    lines.append("")
    lines.append("4. **User Impact**")
    lines.append("   - Identify users/teams affected by the change")
    lines.append("   - Check custom views and filters using the field")
    lines.append("   - Review reports and dashboards")
    lines.append("")
    lines.append("5. **Data Impact**")
    lines.append("   - Estimate records affected")
    lines.append("   - Check for required fields that may block updates")
    lines.append("   - Verify data migration plan if needed")
    lines.append("")
    lines.append("6. **Testing Plan**")
    lines.append("   - Sandbox/test environment available?")
    lines.append("   - Test data prepared")
    lines.append("   - Rollback procedure documented")
    lines.append("")
    lines.append("7. **Documentation**")
    lines.append("   - Change ticket/request logged")
    lines.append("   - Approval obtained")
    lines.append("   - User communication drafted")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 2: Common Scenarios
    lines.append("## Common Change Scenarios {#scenarios}")
    lines.append("")
    
    # Scenario A: Adding Required Field
    lines.append("### Scenario A: Adding a Required Field {#scenario-required-field}")
    lines.append("")
    lines.append(f"**Example:** Adding a required field to the Leads module")
    lines.append("")
    lines.append("**Steps:**")
    lines.append("")
    lines.append("1. **Pre-Change Analysis**")
    lines.append(f"   - Current Leads fields: {len(lead_fields)} fields")
    lines.append("   - Check for existing similar fields")
    lines.append("   - Review lookup relationships (Leads has 5 lookup fields)")
    lines.append("")
    lines.append("2. **Data Preparation**")
    lines.append("   - Export current Leads data")
    lines.append("   - Identify records with missing data for new field")
    lines.append("   - Prepare default values or data import")
    lines.append("")
    lines.append("3. **Implementation Sequence**")
    lines.append("   - Step 1: Add field as optional first")
    lines.append("   - Step 2: Populate data for all existing records")
    lines.append("   - Step 3: Verify data completeness (100% populated)")
    lines.append("   - Step 4: Change field to required")
    lines.append("")
    lines.append("4. **Workflow Updates**")
    lines.append("   - Update any create/edit workflows to include new field")
    lines.append("   - Check validation rules")
    lines.append("   - Test automation with new required field")
    lines.append("")
    lines.append("5. **User Communication**")
    lines.append("   - Notify users before making field required")
    lines.append("   - Provide field usage guidelines")
    lines.append("   - Update training materials")
    lines.append("")
    lines.append("**Rollback:** Remove required flag, optionally hide field from layouts")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Scenario B: Modifying Workflow Trigger
    lines.append("### Scenario B: Modifying a Workflow Trigger {#scenario-workflow-trigger}")
    lines.append("")
    lines.append("**Example:** Changing trigger fields for a Courses workflow")
    lines.append("")
    lines.append("**Current Configuration:**")
    lines.append("- Module: Courses")
    lines.append("- Active Workflows: 37")
    lines.append("- Example: 'Update Registration Course Days' (triggered by Course_Start_Time, Course_End_Time)")
    lines.append("")
    lines.append("**Steps:**")
    lines.append("")
    lines.append("1. **Document Current Behaviour**")
    lines.append("   - Export workflow configuration")
    lines.append("   - Test current trigger conditions")
    lines.append("   - Document expected actions")
    lines.append("")
    lines.append("2. **Impact Analysis**")
    lines.append("   - Check WORKFLOW_DEPENDENCY_MAP.md for this workflow")
    lines.append("   - Identify fields read by the workflow")
    lines.append("   - Check for cross-module actions")
    lines.append("   - Review recent execution history")
    lines.append("")
    lines.append("3. **Testing Sequence**")
    lines.append("   - Clone workflow with new trigger configuration")
    lines.append("   - Test cloned workflow with sample data")
    lines.append("   - Verify actions execute correctly")
    lines.append("   - Compare results with original workflow")
    lines.append("")
    lines.append("4. **Implementation**")
    lines.append("   - Disable original workflow")
    lines.append("   - Activate new workflow")
    lines.append("   - Monitor for 24-48 hours")
    lines.append("   - Archive old workflow after validation period")
    lines.append("")
    lines.append("**Rollback:** Re-enable original workflow, disable new one")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Scenario C: Changing Picklist Values
    if recent_field_changes:
        example_change = recent_field_changes[0]
        lines.append("### Scenario C: Changing Picklist Values {#scenario-picklist}")
        lines.append("")
        lines.append(f"**Recent Example:** {example_change['module']}.{example_change['field']}")
        lines.append("")
        
        change_data = example_change.get("change", {}).get("pick_list_values", {})
        if change_data:
            old_vals = change_data.get("old", [])
            new_vals = change_data.get("new", [])
            added = set(new_vals) - set(old_vals)
            removed = set(old_vals) - set(new_vals)
            
            if added:
                lines.append(f"- **Added values:** {', '.join(list(added)[:3])}")
            if removed:
                lines.append(f"- **Removed values:** {', '.join(list(removed)[:3])}")
        lines.append("")
    else:
        lines.append("### Scenario C: Changing Picklist Values {#scenario-picklist}")
        lines.append("")
        lines.append("**Example:** Adding/removing values from Lead_Status or Cold_Call_Tier")
        lines.append("")
    
    lines.append("**Steps:**")
    lines.append("")
    lines.append("1. **Adding New Values** (Low Risk)")
    lines.append("   - Check for duplicate/similar existing values")
    lines.append("   - Add new value via field settings")
    lines.append("   - Update workflows using the picklist (if needed)")
    lines.append("   - Update filters and reports")
    lines.append("   - Communicate new option to users")
    lines.append("")
    lines.append("2. **Removing Values** (HIGH RISK)")
    lines.append("   - **Pre-Change Analysis:**")
    lines.append("     * Count records using the value")
    lines.append("     * Check workflow conditions using this value")
    lines.append("     * Review reports/dashboards filtering on this value")
    lines.append("   - **Data Migration:**")
    lines.append("     * Decide replacement value")
    lines.append("     * Bulk update existing records")
    lines.append("     * Verify 0 records use old value")
    lines.append("   - **Configuration Update:**")
    lines.append("     * Update workflow conditions")
    lines.append("     * Update filters and reports")
    lines.append("     * Remove the picklist value")
    lines.append("")
    lines.append("3. **Reordering Values** (Low Risk)")
    lines.append("   - No data migration needed")
    lines.append("   - Update via drag-and-drop in field settings")
    lines.append("   - Communicate change if order has business meaning")
    lines.append("")
    lines.append("**Rollback:**")
    lines.append("- Adding: Hide new value from layouts (doesn't break data)")
    lines.append("- Removing: Re-add value immediately (data may be lost if not backed up)")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Scenario D: Disabling a Workflow
    lines.append("### Scenario D: Disabling a Workflow {#scenario-disable-workflow}")
    lines.append("")
    lines.append("**Example:** Disabling an active workflow from Courses module")
    lines.append("")
    lines.append("**Steps:**")
    lines.append("")
    lines.append("1. **Pre-Disable Analysis**")
    lines.append("   - Review WORKFLOW_DEPENDENCY_MAP.md for this workflow")
    lines.append("   - Check risk level (HIGH/MEDIUM/LOW)")
    lines.append("   - Identify what stops working when disabled")
    lines.append("   - Review last execution time and frequency")
    lines.append("")
    lines.append("2. **Impact Assessment**")
    lines.append("   - HIGH RISK: Cross-module actions or 3+ field dependencies")
    lines.append("   - MEDIUM RISK: Field updates with business logic")
    lines.append("   - LOW RISK: Simple notifications or logging")
    lines.append("")
    lines.append("3. **Communication**")
    lines.append("   - Notify affected users/teams")
    lines.append("   - Document manual process (if automation is critical)")
    lines.append("   - Set expectations for alternative workflow")
    lines.append("")
    lines.append("4. **Disable Process**")
    lines.append("   - Export workflow configuration (backup)")
    lines.append("   - Set workflow to Inactive")
    lines.append("   - Monitor for 1-2 weeks")
    lines.append("   - Archive if no issues reported")
    lines.append("")
    lines.append("**Rollback:** Re-enable workflow (configuration preserved)")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 3: Risk Assessment Quick Reference
    lines.append("## Risk Assessment Quick Reference {#risk-reference}")
    lines.append("")
    lines.append("| Change Type | Risk Level | Key Concerns |")
    lines.append("|-------------|------------|--------------|")
    lines.append("| Add optional field | LOW | Layout updates, user training |")
    lines.append("| Add required field | MEDIUM-HIGH | Data migration, workflow updates |")
    lines.append("| Remove field | HIGH | Data loss, workflow breaks, integration issues |")
    lines.append("| Add picklist value | LOW | Workflow updates, user training |")
    lines.append("| Remove picklist value | HIGH | Data migration, workflow conditions |")
    lines.append("| Modify workflow trigger | MEDIUM-HIGH | Automation behaviour change |")
    lines.append("| Disable workflow | VARIES | See WORKFLOW_DEPENDENCY_MAP.md |")
    lines.append("| Add lookup field | MEDIUM | Relationship complexity, data integrity |")
    lines.append("| Modify field type | HIGH | Data conversion, compatibility |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 4: Testing Recommendations
    lines.append("## Testing Recommendations {#testing}")
    lines.append("")
    lines.append("### Sandbox Testing (Recommended)")
    lines.append("")
    lines.append("1. **Refresh sandbox** from production")
    lines.append("2. **Apply changes** in sandbox")
    lines.append("3. **Test workflows** with real-world scenarios")
    lines.append("4. **Verify reports** and dashboards")
    lines.append("5. **User acceptance testing** with key stakeholders")
    lines.append("")
    lines.append("### Production Testing (If No Sandbox)")
    lines.append("")
    lines.append("1. **Off-peak hours** deployment")
    lines.append("2. **Phased rollout** (one module/team at a time)")
    lines.append("3. **Monitor closely** for first 24-48 hours")
    lines.append("4. **Quick rollback** capability ready")
    lines.append("")
    lines.append("### Validation Checks")
    lines.append("")
    lines.append("- ✓ Workflows execute without errors")
    lines.append("- ✓ Required fields accept valid data")
    lines.append("- ✓ Picklist values display correctly")
    lines.append("- ✓ Lookup relationships resolve properly")
    lines.append("- ✓ Reports return expected results")
    lines.append("- ✓ API integrations still function")
    lines.append("- ✓ User layouts display correctly")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 5: Rollback Guidance
    lines.append("## Rollback Guidance {#rollback}")
    lines.append("")
    lines.append("### Field Changes")
    lines.append("")
    lines.append("**Easy Rollback:**")
    lines.append("- Remove optional field (data preserved)")
    lines.append("- Hide field from layouts")
    lines.append("- Change required → optional")
    lines.append("")
    lines.append("**Difficult Rollback:**")
    lines.append("- Change field type (may lose data)")
    lines.append("- Delete field (data lost)")
    lines.append("- Remove picklist values (data may be lost)")
    lines.append("")
    lines.append("**Best Practice:** Export data before ANY field deletion or type change")
    lines.append("")
    lines.append("### Workflow Changes")
    lines.append("")
    lines.append("**Easy Rollback:**")
    lines.append("- Re-enable disabled workflow")
    lines.append("- Revert workflow status (Active ↔ Inactive)")
    lines.append("- Restore from exported configuration")
    lines.append("")
    lines.append("**Requires Caution:**")
    lines.append("- Workflows with external dependencies (API calls, webhooks)")
    lines.append("- Workflows that create records (may cause duplicates)")
    lines.append("- Time-based workflows (may trigger unexpectedly)")
    lines.append("")
    lines.append("### Picklist Changes")
    lines.append("")
    lines.append("**Easy Rollback:**")
    lines.append("- Re-add removed values (if data was preserved)")
    lines.append("- Restore value order")
    lines.append("")
    lines.append("**Data Recovery:**")
    lines.append("- Use export from before change")
    lines.append("- Bulk update records to restore values")
    lines.append("- May require CSV import")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Footer
    lines.append("## Related Documentation {#related-docs}")
    lines.append("")
    lines.append("- **WORKFLOW_DEPENDENCY_MAP.md** - Check workflow dependencies before changes")
    lines.append("- **FIELD_REFERENCE.md** - Field specifications and current configuration")
    lines.append("- **LATEST_CHANGES.md** - Learn from recent changes")
    lines.append("- **SYSTEM_OVERVIEW.md** - Module relationships and lookup dependencies")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by `tools/generate_ai_kb.py` on {datetime.now().strftime('%Y-%m-%d')}*")
    lines.append("")
    
    return "\n".join(lines)


def write_outputs(files: Dict[str, str], output_dir: Path, dry_run: bool):
    """Write generated files and report sizes."""
    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 70)
    print("AI KNOWLEDGE BASE GENERATION")
    print("=" * 70)
    print()
    
    file_sizes = []
    for name, content in sorted(files.items()):
        size_kb = len(content.encode('utf-8')) / 1024
        file_sizes.append((name, size_kb))
        
        if dry_run:
            print(f"[DRY RUN] Would write {name}: {size_kb:.1f} KB")
        else:
            filepath = output_dir / name
            filepath.write_text(content, encoding='utf-8')
            print(f"✓ Wrote {name}: {size_kb:.1f} KB")
    
    total_kb = sum(size for _, size in file_sizes)
    print()
    print("=" * 70)
    print(f"Total size: {total_kb:.1f} KB")
    
    if total_kb > 150:
        print(f"⚠ WARNING: Total size exceeds 150 KB budget by {total_kb - 150:.1f} KB")
    elif total_kb > 100:
        print(f"✓ Within budget (target: 100-150 KB)")
    else:
        print(f"✓ Well within budget (target: 100-150 KB)")
    
    print("=" * 70)
    print()


def main():
    args = parse_args()
    
    # Resolve output directory
    output_dir = Path(args.output_dir) if args.output_dir else OUTPUT_DIR
    
    # Load CRM data model
    data_model_path = MODELS_DIR / "CRM_DATA_MODEL.json"
    if not data_model_path.exists():
        print(f"ERROR: CRM data model not found at {data_model_path}")
        print("Run `python tools/data_processing/build_crm_data_model.py` first.")
        sys.exit(1)
    
    print(f"Loading CRM data model from {data_model_path.name}...")
    data_model = load_json(data_model_path)
    
    # Determine export date
    if args.date:
        export_date = args.date
    else:
        # Infer from latest export or data model metadata
        export = get_latest_export(export_directory())
        export_date = export.date
    
    # Load diff
    if args.diff_json:
        diff_path = Path(args.diff_json)
        if not diff_path.exists():
            print(f"ERROR: Diff file not found: {diff_path}")
            sys.exit(1)
    else:
        diff_path = get_latest_diff(REPORTS_DIR)
        if not diff_path:
            print("WARNING: No export diff found in reports/")
            print("Run `python tools/compare_exports.py` first to enable LATEST_CHANGES.md")
            diff_path = None
    
    if diff_path:
        print(f"Loading diff from {diff_path.name}...")
        diff = load_json(diff_path)
    else:
        diff = {"old_date": "unknown", "new_date": export_date, "modules": {}, "lookup_relationships": {}}
    
    # Load dependencies file (for workflow dependency map)
    try:
        export = get_latest_export(export_directory())
        dependencies_path = export.dependencies
        print(f"Loading dependencies from {dependencies_path.name}...")
        dependencies = load_json(dependencies_path)
    except Exception as e:
        print(f"WARNING: Could not load dependencies file: {e}")
        print("WORKFLOW_DEPENDENCY_MAP.md will be limited without dependencies data")
        dependencies = {"workflow_dependencies": {}, "field_dependencies": {}, "lookup_relationships": {}}
    
    # Generate documentation
    print("\nGenerating AI Knowledge Base files...")
    print()
    
    files = {}
    
    print("1/5 Generating SYSTEM_OVERVIEW.md...")
    files["SYSTEM_OVERVIEW.md"] = generate_system_overview(data_model, export_date)
    
    print("2/5 Generating LATEST_CHANGES.md...")
    files["LATEST_CHANGES.md"] = generate_latest_changes(diff)
    
    print("3/5 Generating WORKFLOW_DEPENDENCY_MAP.md...")
    files["WORKFLOW_DEPENDENCY_MAP.md"] = generate_workflow_dependency_map(data_model, dependencies, export_date)
    
    print("4/5 Generating FIELD_REFERENCE.md...")
    files["FIELD_REFERENCE.md"] = generate_field_reference(data_model, dependencies, export_date)
    
    print("5/5 Generating CHANGE_PLANNING_GUIDE.md...")
    files["CHANGE_PLANNING_GUIDE.md"] = generate_change_planning_guide(data_model, dependencies, diff)
    
    # Write outputs
    write_outputs(files, output_dir, args.dry_run)
    
    if not args.dry_run:
        print(f"\nFiles written to: {output_dir}")
        print("\nAll 5 AI Knowledge Base files complete!")
        print("\nNext steps:")
        print("- Review generated files in ai_kb/")
        print("- Upload to Claude Project Knowledge")
        print("- Use as context for CRM change planning and queries")


if __name__ == "__main__":
    main()

