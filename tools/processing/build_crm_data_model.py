#!/usr/bin/env python3
"""
Zoho CRM Data Model Builder

Loads and analyzes Zoho CRM data exports to build a comprehensive internal model
representing the complete schema and module relationships.

Data Sources:
- zoho-data-model-2025-11-13.json (13 MB)
- zoho-dependencies-2025-11-13.json (672 KB)
- Zoho_CRM_Data_Model_2025-11-13.xlsx (181 KB)

Reference Documents:
- EXCEL_GUIDE.md
- workflow-mapping-guide.md
- README.md
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, field
from collections import defaultdict

TOOLS_DIR = Path(__file__).resolve().parents[1]
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export  # noqa: E402


@dataclass
class FieldSchema:
    """Represents a single field in a Zoho module"""
    api_name: str
    display_label: str
    data_type: str
    required: bool = False
    custom_field: bool = False
    read_only: bool = False
    visible: bool = True
    lookup_module: str = None
    picklist_values: List[str] = field(default_factory=list)
    formula: str = None
    default_value: Any = None
    length: int = None
    unique: bool = False
    system_mandatory: bool = False

    def __repr__(self):
        parts = [f"{self.api_name} ({self.data_type})"]
        if self.required:
            parts.append("REQUIRED")
        if self.lookup_module:
            parts.append(f"→ {self.lookup_module}")
        return " ".join(parts)


@dataclass
class WorkflowRule:
    """Represents a workflow automation rule"""
    workflow_id: str
    name: str
    module: str
    active: bool
    trigger_type: str  # create, field_update, date_or_datetime, etc.
    description: str = ""
    condition_fields: List[str] = field(default_factory=list)
    created_by: str = ""
    modified_by: str = ""
    last_executed: str = None

    def __repr__(self):
        status = "ACTIVE" if self.active else "INACTIVE"
        return f"{self.name} ({self.trigger_type}) [{status}]"


@dataclass
class ModuleSchema:
    """Represents a complete Zoho CRM module"""
    api_name: str
    singular_label: str
    plural_label: str
    fields: Dict[str, FieldSchema] = field(default_factory=dict)
    workflows: Dict[str, WorkflowRule] = field(default_factory=dict)
    api_supported: bool = True
    creatable: bool = True
    editable: bool = True
    deletable: bool = True

    # Relationships
    lookup_relationships: Dict[str, str] = field(default_factory=dict)  # field_name -> target_module
    referenced_by: List[str] = field(default_factory=list)  # modules that reference this one

    # Counts
    @property
    def field_count(self) -> int:
        return len(self.fields)

    @property
    def workflow_count(self) -> int:
        return len(self.workflows)

    @property
    def active_workflow_count(self) -> int:
        return sum(1 for wf in self.workflows.values() if wf.active)

    @property
    def lookup_field_count(self) -> int:
        return len(self.lookup_relationships)

    @property
    def mandatory_field_count(self) -> int:
        return sum(1 for f in self.fields.values() if f.required)

    @property
    def custom_field_count(self) -> int:
        return sum(1 for f in self.fields.values() if f.custom_field)

    def __repr__(self):
        return f"{self.api_name}: {self.field_count} fields, {self.active_workflow_count}/{self.workflow_count} workflows"


@dataclass
class CRMDataModel:
    """
    Complete internal representation of Zoho CRM data model

    This model captures:
    - All modules and their schemas
    - All fields with complete metadata
    - All workflow automations
    - Module relationships and dependencies
    - Lookup relationships between modules
    """
    modules: Dict[str, ModuleSchema] = field(default_factory=dict)

    # Cross-module analytics
    total_fields: int = 0
    total_workflows: int = 0
    total_active_workflows: int = 0
    total_lookup_relationships: int = 0

    # Module dependency map: source_module -> list of target modules
    module_dependencies: Dict[str, List[str]] = field(default_factory=lambda: defaultdict(list))

    # Reverse lookup: target_module -> list of source modules
    module_references: Dict[str, List[str]] = field(default_factory=lambda: defaultdict(list))

    def add_module(self, module: ModuleSchema):
        """Add a module to the data model"""
        self.modules[module.api_name] = module

    def build_dependency_graph(self):
        """Build module dependency relationships from lookup fields"""
        self.module_dependencies.clear()
        self.module_references.clear()

        for module_name, module in self.modules.items():
            for field_name, target_module in module.lookup_relationships.items():
                # Add to dependencies
                if target_module not in self.module_dependencies[module_name]:
                    self.module_dependencies[module_name].append(target_module)

                # Add to reverse references
                if module_name not in self.module_references[target_module]:
                    self.module_references[target_module].append(module_name)

        # Update referenced_by lists
        for target_module, source_modules in self.module_references.items():
            if target_module in self.modules:
                self.modules[target_module].referenced_by = source_modules

    def calculate_statistics(self):
        """Calculate aggregate statistics"""
        self.total_fields = sum(m.field_count for m in self.modules.values())
        self.total_workflows = sum(m.workflow_count for m in self.modules.values())
        self.total_active_workflows = sum(m.active_workflow_count for m in self.modules.values())
        self.total_lookup_relationships = sum(m.lookup_field_count for m in self.modules.values())

    def get_most_referenced_modules(self, top_n: int = 10) -> List[tuple]:
        """Get modules that are most frequently referenced by other modules"""
        return sorted(
            [(module, len(refs)) for module, refs in self.module_references.items()],
            key=lambda x: x[1],
            reverse=True
        )[:top_n]

    def get_most_complex_modules(self, top_n: int = 10) -> List[tuple]:
        """Get modules with most fields and workflows"""
        return sorted(
            [(name, module.field_count, module.active_workflow_count)
             for name, module in self.modules.items()],
            key=lambda x: (x[1] + x[2] * 5),  # Weight workflows more heavily
            reverse=True
        )[:top_n]

    def get_module(self, name: str) -> ModuleSchema:
        """Get a module by name"""
        return self.modules.get(name)

    def get_field(self, module_name: str, field_name: str) -> FieldSchema:
        """Get a specific field from a module"""
        module = self.modules.get(module_name)
        if module:
            return module.fields.get(field_name)
        return None

    def __repr__(self):
        return f"CRMDataModel: {len(self.modules)} modules, {self.total_fields} fields, {self.total_active_workflows} workflows"


def load_zoho_data_model(json_path: Path) -> Dict:
    """Load the main Zoho data model JSON"""
    print(f"Loading {json_path.name}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✓ Loaded {len(data.get('modules', []))} modules")
    return data


def load_zoho_dependencies(json_path: Path) -> Dict:
    """Load the Zoho dependencies JSON"""
    print(f"Loading {json_path.name}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✓ Loaded dependency data")
    return data


def parse_field(field_data: Dict) -> FieldSchema:
    """Parse a field from Zoho API format into FieldSchema"""
    # Extract data type - could be in 'data_type', 'json_type', or 'type'
    data_type = field_data.get('data_type') or field_data.get('json_type') or field_data.get('type') or 'unknown'

    # Extract lookup module if this is a lookup field
    lookup_module = None
    if field_data.get('lookup'):
        lookup_module = field_data.get('lookup', {}).get('module', {}).get('api_name')

    # Handle different picklist formats
    picklist_values = []
    if field_data.get('pick_list_values'):
        picklist_values = [pv.get('display_value', '') for pv in field_data.get('pick_list_values', [])]

    return FieldSchema(
        api_name=field_data.get('api_name', ''),
        display_label=field_data.get('display_label', field_data.get('field_label', '')),
        data_type=data_type,
        required=field_data.get('required', False),
        custom_field=field_data.get('custom_field', False),
        read_only=field_data.get('read_only', field_data.get('field_read_only', False)),
        visible=field_data.get('visible', True),
        lookup_module=lookup_module,
        picklist_values=picklist_values,
        formula=field_data.get('formula', {}).get('expression') if field_data.get('formula') else None,
        default_value=field_data.get('default_value'),
        length=field_data.get('length'),
        unique=field_data.get('unique', False),
        system_mandatory=field_data.get('system_mandatory', False)
    )


def parse_workflow(workflow_data: Dict, module_name: str) -> WorkflowRule:
    """Parse a workflow from Zoho API format into WorkflowRule"""
    return WorkflowRule(
        workflow_id=str(workflow_data.get('id', '')),
        name=workflow_data.get('name', ''),
        module=module_name,
        active=workflow_data.get('active', False),
        trigger_type=workflow_data.get('trigger_type', 'unknown'),
        description=workflow_data.get('description', ''),
        condition_fields=workflow_data.get('condition_fields', []),
        created_by=workflow_data.get('created_by', {}).get('name', ''),
        modified_by=workflow_data.get('modified_by', {}).get('name', ''),
        last_executed=workflow_data.get('last_execution_time')
    )


def build_crm_data_model(data_model_path: Path, dependencies_path: Path) -> CRMDataModel:
    """
    Build the complete CRM_DATA_MODEL from exported JSON files

    Args:
        data_model_path: Path to zoho-data-model-*.json
        dependencies_path: Path to zoho-dependencies-*.json

    Returns:
        CRMDataModel: Complete internal representation
    """
    print("\n" + "="*60)
    print("BUILDING CRM_DATA_MODEL")
    print("="*60 + "\n")

    # Load raw data
    data_model_json = load_zoho_data_model(data_model_path)
    dependencies_json = load_zoho_dependencies(dependencies_path)

    # Initialize model
    crm_model = CRMDataModel()

    print("\nProcessing modules...")

    # Process each module - top level keys are module names
    for module_api_name, module_data in data_model_json.items():
        if not isinstance(module_data, dict):
            continue

        # Extract module_info
        module_info = module_data.get('module_info', {})

        # Create module schema
        module = ModuleSchema(
            api_name=module_api_name,
            singular_label=module_info.get('singular_label', module_api_name),
            plural_label=module_info.get('plural_label', module_api_name),
            api_supported=module_info.get('api_supported', True),
            creatable=module_info.get('creatable', True),
            editable=module_info.get('editable', True),
            deletable=module_info.get('deletable', True)
        )

        # Parse fields
        for field_data in module_data.get('fields', []):
            if not field_data.get('api_name'):
                continue

            field = parse_field(field_data)
            module.fields[field.api_name] = field

            # Track lookup relationships
            if field.lookup_module:
                module.lookup_relationships[field.api_name] = field.lookup_module

        # Parse workflows
        for workflow_data in module_data.get('workflows', []):
            if not workflow_data.get('id'):
                continue
            workflow = parse_workflow(workflow_data, module_api_name)
            module.workflows[workflow.workflow_id] = workflow

        # Add module to model
        crm_model.add_module(module)

        print(f"  [{len(crm_model.modules):2d}] {module}")

    # Build dependency graph
    print("\nBuilding dependency graph...")
    crm_model.build_dependency_graph()
    print(f"✓ {len(crm_model.module_dependencies)} modules have dependencies")
    print(f"✓ {len(crm_model.module_references)} modules are referenced")

    # Calculate statistics
    print("\nCalculating statistics...")
    crm_model.calculate_statistics()

    print("\n" + "="*60)
    print("CRM DATA MODEL SUMMARY")
    print("="*60)
    print(f"Total Modules:              {len(crm_model.modules)}")
    print(f"Total Fields:               {crm_model.total_fields:,}")
    print(f"Total Workflows:            {crm_model.total_workflows}")
    print(f"Active Workflows:           {crm_model.total_active_workflows}")
    print(f"Lookup Relationships:       {crm_model.total_lookup_relationships}")

    print("\n" + "-"*60)
    print("MOST REFERENCED MODULES (Top 10)")
    print("-"*60)
    for module_name, ref_count in crm_model.get_most_referenced_modules(10):
        print(f"  {module_name:30s} referenced by {ref_count:2d} modules")

    print("\n" + "-"*60)
    print("MOST COMPLEX MODULES (Top 10)")
    print("-"*60)
    for module_name, field_count, workflow_count in crm_model.get_most_complex_modules(10):
        print(f"  {module_name:30s} {field_count:3d} fields, {workflow_count:2d} workflows")

    print("\n" + "="*60)
    print("✓ CRM_DATA_MODEL BUILD COMPLETE")
    print("="*60 + "\n")

    return crm_model


def save_model_summary(crm_model: CRMDataModel, output_path: Path, source_label: str):
    """Save a human-readable summary of the CRM data model"""
    print(f"Saving model summary to {output_path}...")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n")
        f.write("# Zoho CRM Data Model Summary\n\n")
        f.write(f"Generated from: zoho-data-model-{source_label}.json\n\n")
        f.write("## Statistics\n\n")
        f.write(f"- **Total Modules**: {len(crm_model.modules)}\n")
        f.write(f"- **Total Fields**: {crm_model.total_fields:,}\n")
        f.write(f"- **Total Workflows**: {crm_model.total_workflows}\n")
        f.write(f"- **Active Workflows**: {crm_model.total_active_workflows}\n")
        f.write(f"- **Lookup Relationships**: {crm_model.total_lookup_relationships}\n\n")

        f.write("## Most Referenced Modules\n\n")
        f.write("| Module | Referenced By |\n")
        f.write("|--------|---------------|\n")
        for module_name, ref_count in crm_model.get_most_referenced_modules(15):
            f.write(f"| {module_name} | {ref_count} modules |\n")

        f.write("\n## Most Complex Modules\n\n")
        f.write("| Module | Fields | Active Workflows |\n")
        f.write("|--------|--------|------------------|\n")
        for module_name, field_count, workflow_count in crm_model.get_most_complex_modules(15):
            f.write(f"| {module_name} | {field_count} | {workflow_count} |\n")

        f.write("\n## All Modules\n\n")
        for module_name in sorted(crm_model.modules.keys()):
            module = crm_model.modules[module_name]
            f.write(f"### {module_name}\n\n")
            f.write(f"- **Singular**: {module.singular_label}\n")
            f.write(f"- **Plural**: {module.plural_label}\n")
            f.write(f"- **Fields**: {module.field_count} ({module.custom_field_count} custom)\n")
            f.write(f"- **Workflows**: {module.active_workflow_count} active / {module.workflow_count} total\n")
            f.write(f"- **Lookup Fields**: {module.lookup_field_count}\n")
            f.write(f"- **Mandatory Fields**: {module.mandatory_field_count}\n")
            f.write(f"- **Referenced By**: {len(module.referenced_by)} modules\n")

            if module.lookup_relationships:
                f.write(f"\n**Lookup Relationships**:\n")
                for field_name, target_module in sorted(module.lookup_relationships.items()):
                    f.write(f"- `{field_name}` → {target_module}\n")

            f.write("\n")

    print(f"✓ Summary saved to {output_path}")


def save_model_json(crm_model: CRMDataModel, output_path: Path):
    """Save the CRM data model as JSON for programmatic access"""
    print(f"Saving model JSON to {output_path}...")

    # Convert to JSON-serializable format
    model_dict = {
        'metadata': {
            'total_modules': len(crm_model.modules),
            'total_fields': crm_model.total_fields,
            'total_workflows': crm_model.total_workflows,
            'total_active_workflows': crm_model.total_active_workflows,
            'total_lookup_relationships': crm_model.total_lookup_relationships
        },
        'modules': {}
    }

    for module_name, module in crm_model.modules.items():
        model_dict['modules'][module_name] = {
            'api_name': module.api_name,
            'singular_label': module.singular_label,
            'plural_label': module.plural_label,
            'api_supported': module.api_supported,
            'creatable': module.creatable,
            'editable': module.editable,
            'deletable': module.deletable,
            'field_count': module.field_count,
            'workflow_count': module.workflow_count,
            'active_workflow_count': module.active_workflow_count,
            'lookup_field_count': module.lookup_field_count,
            'mandatory_field_count': module.mandatory_field_count,
            'custom_field_count': module.custom_field_count,
            'referenced_by': module.referenced_by,
            'fields': {
                field_name: {
                    'api_name': field.api_name,
                    'display_label': field.display_label,
                    'data_type': field.data_type,
                    'required': field.required,
                    'custom_field': field.custom_field,
                    'read_only': field.read_only,
                    'visible': field.visible,
                    'lookup_module': field.lookup_module,
                    'picklist_values': field.picklist_values,
                    'formula': field.formula,
                    'unique': field.unique,
                    'system_mandatory': field.system_mandatory
                }
                for field_name, field in module.fields.items()
            },
            'workflows': {
                workflow_id: {
                    'workflow_id': workflow.workflow_id,
                    'name': workflow.name,
                    'module': workflow.module,
                    'active': workflow.active,
                    'trigger_type': workflow.trigger_type,
                    'description': workflow.description,
                    'condition_fields': workflow.condition_fields,
                    'created_by': workflow.created_by,
                    'modified_by': workflow.modified_by,
                    'last_executed': workflow.last_executed
                }
                for workflow_id, workflow in module.workflows.items()
            },
            'lookup_relationships': module.lookup_relationships
        }

    model_dict['module_dependencies'] = dict(crm_model.module_dependencies)
    model_dict['module_references'] = dict(crm_model.module_references)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(model_dict, f, indent=2)

    print(f"✓ Model JSON saved to {output_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build CRM data model from Zoho exports")
    parser.add_argument("--date", help="Export date (YYYY-MM-DD). Defaults to latest export.")
    parser.add_argument(
        "--output-dir",
        help="Directory for generated outputs. Defaults to <repo>/models",
    )
    return parser.parse_args()


def main():
    """Main execution"""
    args = parse_args()

    export = (
        get_export_by_date(args.date, export_directory()).ensure_both()
        if args.date
        else get_latest_export(export_directory()).ensure_both()
    )

    data_model_path = export.data_model
    dependencies_path = export.dependencies

    output_dir = Path(args.output_dir) if args.output_dir else Path(__file__).resolve().parents[2] / 'models'
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_path = output_dir / 'CRM_DATA_MODEL_SUMMARY.md'
    json_path = output_dir / 'CRM_DATA_MODEL.json'

    # Build the model
    crm_model = build_crm_data_model(data_model_path, dependencies_path)

    # Save outputs
    save_model_summary(crm_model, summary_path, export.date)
    save_model_json(crm_model, json_path)

    print("\n✓ All outputs generated successfully")
    print(f"\nOutputs:")
    print(f"  - {summary_path}")
    print(f"  - {json_path}")

    return crm_model


if __name__ == '__main__':
    main()
