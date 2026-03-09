#!/usr/bin/env python3
"""
Example usage of CRM_DATA_MODEL

This script demonstrates how to use the CRM_DATA_MODEL.json file
to query and analyze the Zoho CRM schema.
"""

import json
from pathlib import Path
from typing import List, Dict, Any


class CRMDataModelQuery:
    """Helper class to query the CRM data model"""

    def __init__(self, model_path: Path):
        """Load the CRM data model"""
        with open(model_path, 'r', encoding='utf-8') as f:
            self.model = json.load(f)

        self.modules = self.model['modules']
        self.metadata = self.model['metadata']
        self.module_dependencies = self.model['module_dependencies']
        self.module_references = self.model['module_references']

    def get_module(self, module_name: str) -> Dict:
        """Get complete module information"""
        return self.modules.get(module_name)

    def get_field(self, module_name: str, field_name: str) -> Dict:
        """Get specific field from a module"""
        module = self.get_module(module_name)
        if module:
            return module['fields'].get(field_name)
        return None

    def get_lookup_fields(self, module_name: str) -> List[tuple]:
        """Get all lookup fields for a module"""
        module = self.get_module(module_name)
        if not module:
            return []

        return [
            (field_name, field['lookup_module'])
            for field_name, field in module['fields'].items()
            if field.get('lookup_module')
        ]

    def get_mandatory_fields(self, module_name: str) -> List[str]:
        """Get all required fields for a module"""
        module = self.get_module(module_name)
        if not module:
            return []

        return [
            field_name
            for field_name, field in module['fields'].items()
            if field.get('required') or field.get('system_mandatory')
        ]

    def get_custom_fields(self, module_name: str) -> List[str]:
        """Get all custom fields for a module"""
        module = self.get_module(module_name)
        if not module:
            return []

        return [
            field_name
            for field_name, field in module['fields'].items()
            if field.get('custom_field')
        ]

    def get_formula_fields(self, module_name: str) -> List[tuple]:
        """Get all formula fields with their expressions"""
        module = self.get_module(module_name)
        if not module:
            return []

        return [
            (field_name, field.get('formula'))
            for field_name, field in module['fields'].items()
            if field.get('formula')
        ]

    def get_picklist_fields(self, module_name: str) -> Dict[str, List[str]]:
        """Get all picklist fields with their values"""
        module = self.get_module(module_name)
        if not module:
            return {}

        return {
            field_name: field.get('picklist_values', [])
            for field_name, field in module['fields'].items()
            if field.get('data_type') in ['picklist', 'multiselectpicklist']
            and field.get('picklist_values')
        }

    def find_field_across_modules(self, field_name: str) -> List[str]:
        """Find which modules have a field with given name"""
        modules_with_field = []
        for module_name, module in self.modules.items():
            if field_name in module['fields']:
                modules_with_field.append(module_name)
        return modules_with_field

    def get_module_dependencies_tree(self, module_name: str) -> Dict:
        """Get complete dependency tree for a module"""
        return {
            'depends_on': self.module_dependencies.get(module_name, []),
            'referenced_by': self.module_references.get(module_name, [])
        }

    def find_path_between_modules(self, source: str, target: str, max_depth: int = 3) -> List[List[str]]:
        """Find all paths between two modules via lookup relationships"""
        paths = []

        def dfs(current: str, path: List[str], visited: set):
            if current == target:
                paths.append(path.copy())
                return

            if len(path) > max_depth:
                return

            for next_module in self.module_dependencies.get(current, []):
                if next_module not in visited:
                    visited.add(next_module)
                    path.append(next_module)
                    dfs(next_module, path, visited)
                    path.pop()
                    visited.remove(next_module)

        dfs(source, [source], {source})
        return paths


def example_queries():
    """Demonstrate various queries on the CRM data model"""

    # Load model
    model_path = Path(__file__).parent / 'CRM_DATA_MODEL.json'
    crm = CRMDataModelQuery(model_path)

    print("=" * 70)
    print("CRM DATA MODEL QUERY EXAMPLES")
    print("=" * 70)

    # Example 1: Get module overview
    print("\n1. MODULE OVERVIEW: Courses")
    print("-" * 70)
    courses = crm.get_module('Courses')
    print(f"   API Name: {courses['api_name']}")
    print(f"   Display: {courses['singular_label']} / {courses['plural_label']}")
    print(f"   Fields: {courses['field_count']} ({courses['custom_field_count']} custom)")
    print(f"   Mandatory Fields: {courses['mandatory_field_count']}")
    print(f"   Lookup Fields: {courses['lookup_field_count']}")
    print(f"   Referenced By: {len(courses['referenced_by'])} modules")

    # Example 2: Get lookup relationships
    print("\n2. LOOKUP RELATIONSHIPS: Courses")
    print("-" * 70)
    lookups = crm.get_lookup_fields('Courses')
    for field_name, target_module in sorted(lookups):
        print(f"   {field_name:40s} → {target_module}")

    # Example 3: Get mandatory fields
    print("\n3. MANDATORY FIELDS: Registration_Records")
    print("-" * 70)
    mandatory = crm.get_mandatory_fields('Registration_Records')
    for field_name in sorted(mandatory):
        field = crm.get_field('Registration_Records', field_name)
        print(f"   {field_name:40s} ({field['data_type']})")

    # Example 4: Find formula fields
    print("\n4. FORMULA FIELDS: Courses")
    print("-" * 70)
    formulas = crm.get_formula_fields('Courses')
    if formulas:
        for field_name, formula in formulas:
            print(f"   {field_name}: {formula[:60]}...")
    else:
        print("   No formula fields found")

    # Example 5: Get picklist values
    print("\n5. PICKLIST FIELDS: Registration_Records (Status)")
    print("-" * 70)
    status_field = crm.get_field('Registration_Records', 'Status')
    if status_field and status_field.get('picklist_values'):
        for value in status_field['picklist_values']:
            print(f"   - {value}")

    # Example 6: Find field across modules
    print("\n6. FIND FIELD ACROSS MODULES: USI_Number")
    print("-" * 70)
    modules_with_usi = crm.find_field_across_modules('USI_Number')
    print(f"   Found in {len(modules_with_usi)} modules:")
    for module in modules_with_usi:
        print(f"   - {module}")

    # Example 7: Module dependency tree
    print("\n7. MODULE DEPENDENCIES: Registration_Records")
    print("-" * 70)
    deps = crm.get_module_dependencies_tree('Registration_Records')
    print("   Depends on:")
    for dep in sorted(deps['depends_on']):
        print(f"   - {dep}")
    print("\n   Referenced by:")
    for ref in sorted(deps['referenced_by']):
        print(f"   - {ref}")

    # Example 8: Find path between modules
    print("\n8. FIND PATH: Leads → Courses")
    print("-" * 70)
    paths = crm.find_path_between_modules('Leads', 'Courses', max_depth=3)
    if paths:
        for i, path in enumerate(paths[:5], 1):
            print(f"   Path {i}: {' → '.join(path)}")
    else:
        print("   No path found")

    # Example 9: Get custom fields
    print("\n9. CUSTOM FIELDS: Courses (first 10)")
    print("-" * 70)
    custom_fields = crm.get_custom_fields('Courses')
    for field_name in sorted(custom_fields)[:10]:
        field = crm.get_field('Courses', field_name)
        print(f"   {field_name:40s} ({field['data_type']})")

    # Example 10: Most referenced modules
    print("\n10. MOST REFERENCED MODULES")
    print("-" * 70)
    ref_counts = [(mod, len(refs)) for mod, refs in crm.module_references.items()]
    ref_counts.sort(key=lambda x: x[1], reverse=True)
    for module_name, count in ref_counts[:10]:
        print(f"   {module_name:30s} {count:2d} references")

    print("\n" + "=" * 70)
    print("Examples complete!")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    example_queries()
