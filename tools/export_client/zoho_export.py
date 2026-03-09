#!/usr/bin/env python3
"""
Zoho CRM Metadata Export Script
Exports complete CRM configuration: modules, fields, layouts, workflows, etc.
READ-ONLY - Safe to run, cannot modify any data.

Features:
- Pagination for workflows and blueprints (no data loss)
- Comprehensive dependency analysis (formulas, mandatory fields, etc.)
- 11 detailed Excel sheets with field usage matrix
- Automation chain detection
- Cross-module dependency mapping
"""

import os
import json
import time
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
CLIENT_ID = os.getenv('ZOHO_CLIENT_ID')
CLIENT_SECRET = os.getenv('ZOHO_CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('ZOHO_REFRESH_TOKEN')
API_BASE = os.getenv('ZOHO_API_BASE')
TOKEN_URL = os.getenv('ZOHO_TOKEN_URL')

# Rate limiting
DELAY_BETWEEN_REQUESTS = 0.5  # 500ms between requests
MAX_RETRIES = 3


class ZohoExporter:
    """Handles Zoho CRM metadata export"""
    
    def __init__(self):
        self.access_token = None
        self.token_expiry = 0
        self.session = requests.Session()
        
    def get_access_token(self) -> str:
        """Get or refresh access token"""
        current_time = time.time()
        
        # Return cached token if still valid
        if self.access_token and current_time < self.token_expiry:
            return self.access_token
        
        print("🔑 Requesting new access token...")
        
        payload = {
            'grant_type': 'refresh_token',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'refresh_token': REFRESH_TOKEN
        }
        
        try:
            response = requests.post(TOKEN_URL, data=payload)
            
            # Check if request was successful
            if response.status_code != 200:
                print(f"❌ Token request failed with status {response.status_code}")
                print(f"Response: {response.text}")
                raise Exception(f"Failed to get access token: {response.text}")
            
            data = response.json()
            
            # Check if access_token is in response
            if 'access_token' not in data:
                print(f"❌ No access_token in response")
                print(f"Response: {data}")
                raise Exception(f"Invalid token response: {data}")
            
            self.access_token = data['access_token']
            # Token expires in 1 hour, refresh 5 minutes early
            self.token_expiry = current_time + (data.get('expires_in', 3600) - 300)
            
            print("✅ Access token obtained successfully\n")
            return self.access_token
            
        except Exception as e:
            print(f"❌ Error getting access token: {e}")
            raise
    
    def make_request(self, endpoint: str, params: Dict = None, retry_count: int = 0) -> Optional[Dict]:
        """Make API request with retry logic"""
        url = f"{API_BASE}/{endpoint}"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.get_access_token()}'
        }
        
        try:
            time.sleep(DELAY_BETWEEN_REQUESTS)  # Rate limiting
            response = self.session.get(url, headers=headers, params=params)
            
            # Handle rate limiting
            if response.status_code == 429:
                if retry_count < MAX_RETRIES:
                    wait_time = 2 ** retry_count  # Exponential backoff
                    print(f"⏸️  Rate limited. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    return self.make_request(endpoint, params, retry_count + 1)
                else:
                    print(f"❌ Max retries reached for {endpoint}")
                    return None
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error requesting {endpoint}: {e}")
            return None
    
    def get_modules(self) -> List[Dict]:
        """Fetch all CRM modules"""
        print("📦 Fetching modules...")
        response = self.make_request('settings/modules')
        
        if response and 'modules' in response:
            modules = response['modules']
            print(f"✅ Found {len(modules)} modules\n")
            return modules
        
        print("⚠️  No modules found\n")
        return []
    
    def get_module_fields(self, module_name: str) -> List[Dict]:
        """Fetch fields for a specific module"""
        response = self.make_request('settings/fields', {'module': module_name})
        
        if response and 'fields' in response:
            return response['fields']
        
        return []
    
    def get_module_layouts(self, module_name: str) -> List[Dict]:
        """Fetch layouts for a specific module"""
        response = self.make_request('settings/layouts', {'module': module_name})
        
        if response and 'layouts' in response:
            return response['layouts']
        
        return []
    
    def get_module_related_lists(self, module_name: str) -> List[Dict]:
        """Fetch related lists for a specific module"""
        response = self.make_request('settings/related_lists', {'module': module_name})
        
        if response and 'related_lists' in response:
            return response['related_lists']
        
        return []
    
    def get_module_custom_views(self, module_name: str) -> List[Dict]:
        """Fetch custom views for a specific module"""
        response = self.make_request('settings/custom_views', {'module': module_name})
        
        if response and 'custom_views' in response:
            return response['custom_views']
        
        return []
    
    def get_workflow_rules(self, module_name: str) -> List[Dict]:
        """Fetch workflow rules for a specific module with pagination"""
        all_workflows = []
        page = 1
        per_page = 200
        
        while True:
            params = {
                'module': module_name,
                'page': page,
                'per_page': per_page
            }
            
            response = self.make_request('settings/automation/workflow_rules', params)
            
            if not response or 'workflow_rules' not in response:
                break
            
            workflows = response['workflow_rules']
            all_workflows.extend(workflows)
            
            # Check if there are more pages
            info = response.get('info', {})
            if not info.get('more_records') or len(workflows) < per_page:
                break
            
            page += 1
        
        return all_workflows
    
    def get_blueprints(self, module_name: str) -> List[Dict]:
        """Fetch blueprints for a specific module with pagination"""
        all_blueprints = []
        page = 1
        per_page = 200
        
        while True:
            params = {
                'module': module_name,
                'page': page,
                'per_page': per_page
            }
            
            response = self.make_request('settings/blueprints', params)
            
            if not response or 'blueprints' not in response:
                break
            
            blueprints = response['blueprints']
            all_blueprints.extend(blueprints)
            
            # Check if there are more pages
            info = response.get('info', {})
            if not info.get('more_records') or len(blueprints) < per_page:
                break
            
            page += 1
        
        return all_blueprints
    
    def extract_field_dependencies(self, data_model: Dict) -> Dict:
        """Extract comprehensive field dependencies"""
        dependencies = {
            'workflow_field_usage': {},
            'lookup_relationships': {},
            'picklist_dependencies': {},
            'formula_fields': {},
            'mandatory_fields': {},
            'unique_fields': {},
            'workflow_dependencies': {},
            'blueprint_dependencies': {},
            'automation_chains': [],
            'cross_module_dependencies': {},
            'field_usage_matrix': {}
        }
        
        print("\n🔍 Analyzing comprehensive field dependencies...")
        
        for module_name, module_data in data_model.items():
            fields = module_data.get('fields', [])
            workflows = module_data.get('workflows', [])
            blueprints = module_data.get('blueprints', [])
            
            # 1. Analyze Fields
            for field in fields:
                field_name = field.get('api_name', '')
                
                # Lookup relationships
                if field.get('data_type') == 'lookup':
                    lookup_module = field.get('lookup', {}).get('module', {}).get('api_name', '')
                    if lookup_module:
                        if module_name not in dependencies['lookup_relationships']:
                            dependencies['lookup_relationships'][module_name] = []
                        dependencies['lookup_relationships'][module_name].append({
                            'field_name': field_name,
                            'field_label': field.get('field_label', ''),
                            'lookup_module': lookup_module,
                            'required': field.get('required', False)
                        })
                
                # Formula fields
                if field.get('formula'):
                    if module_name not in dependencies['formula_fields']:
                        dependencies['formula_fields'][module_name] = []
                    dependencies['formula_fields'][module_name].append({
                        'field_name': field_name,
                        'field_label': field.get('field_label', ''),
                        'formula': field.get('formula', {}).get('expression', ''),
                        'return_type': field.get('data_type', '')
                    })
                
                # Mandatory fields
                if field.get('required') or field.get('system_mandatory'):
                    if module_name not in dependencies['mandatory_fields']:
                        dependencies['mandatory_fields'][module_name] = []
                    dependencies['mandatory_fields'][module_name].append({
                        'field_name': field_name,
                        'field_label': field.get('field_label', ''),
                        'data_type': field.get('data_type', ''),
                        'system_mandatory': field.get('system_mandatory', False)
                    })
                
                # Unique fields
                if field.get('unique'):
                    if module_name not in dependencies['unique_fields']:
                        dependencies['unique_fields'][module_name] = []
                    dependencies['unique_fields'][module_name].append({
                        'field_name': field_name,
                        'field_label': field.get('field_label', ''),
                        'case_sensitive': field.get('unique', {}).get('casesensitive', False)
                    })
            
            # 2. Analyze Workflow Dependencies
            for workflow in workflows:
                workflow_id = workflow.get('id', 'unknown')
                workflow_name = workflow.get('name', 'Unknown')
                
                # Get active status (can be in status.active or active)
                active = False
                if 'status' in workflow and isinstance(workflow['status'], dict):
                    active = workflow['status'].get('active', False)
                elif 'active' in workflow:
                    active = workflow.get('active', False)
                
                # Get trigger type (can be in execute_when.type or type)
                trigger_type = ''
                if 'execute_when' in workflow and isinstance(workflow['execute_when'], dict):
                    trigger_type = workflow['execute_when'].get('type', '')
                elif 'type' in workflow:
                    trigger_type = workflow.get('type', '')
                
                # Get created by and modified by
                created_by = ''
                if 'created_by' in workflow and isinstance(workflow['created_by'], dict):
                    created_by = workflow['created_by'].get('name', '')
                
                modified_by = ''
                if 'modified_by' in workflow and isinstance(workflow['modified_by'], dict):
                    modified_by = workflow['modified_by'].get('name', '')
                
                workflow_dep = {
                    'workflow_name': workflow_name,
                    'workflow_id': workflow_id,
                    'module': module_name,
                    'active': active,
                    'trigger_type': trigger_type,
                    'created_by': created_by,
                    'modified_by': modified_by,
                    'created_time': workflow.get('created_time', ''),
                    'modified_time': workflow.get('modified_time', ''),
                    'last_executed_time': workflow.get('last_executed_time', ''),
                    'condition_fields': [],
                    'updated_fields': [],
                    'cross_module_actions': [],
                    'external_dependencies': []
                }
                
                # Extract fields from criteria in execute_when.details.criteria
                exec_when = workflow.get('execute_when', {})
                if isinstance(exec_when, dict):
                    details = exec_when.get('details', {})
                    if isinstance(details, dict) and 'criteria' in details:
                        criteria_fields = self._extract_fields_from_criteria(details['criteria'])
                        workflow_dep['condition_fields'] = criteria_fields
                
                # Also check for direct criteria field (legacy support)
                if 'criteria' in workflow:
                    criteria_fields = self._extract_fields_from_criteria(workflow['criteria'])
                    workflow_dep['condition_fields'].extend(criteria_fields)
                    # Remove duplicates
                    workflow_dep['condition_fields'] = list(set(workflow_dep['condition_fields']))
                
                # Extract fields from actions (if available)
                if 'actions' in workflow:
                    actions = workflow['actions']
                    if isinstance(actions, list):
                        for action in actions:
                            action_type = action.get('type', '')
                            
                            # Field updates
                            if action_type == 'field_update':
                                field_name = action.get('field', {}).get('api_name', '')
                                if field_name:
                                    workflow_dep['updated_fields'].append({
                                        'field_name': field_name,
                                        'update_type': action.get('value', {}).get('type', ''),
                                        'value': str(action.get('value', {}).get('value', ''))
                                    })
                            
                            # Cross-module actions
                            elif action_type in ['create_record', 'update_related_record']:
                                target_module = action.get('module', '')
                                if target_module:
                                    workflow_dep['cross_module_actions'].append({
                                        'action_type': action_type,
                                        'target_module': target_module,
                                        'field_mappings': action.get('field_mappings', [])
                                    })
                            
                            # External dependencies
                            elif action_type in ['webhook', 'email_notification', 'custom_function']:
                                workflow_dep['external_dependencies'].append({
                                    'type': action_type,
                                    'name': action.get('name', ''),
                                    'details': action.get('url', '') or action.get('function_name', '')
                                })
                
                dependencies['workflow_dependencies'][f"{module_name}_{workflow_id}"] = workflow_dep
            
            # 3. Analyze Blueprint Dependencies
            for blueprint in blueprints:
                blueprint_id = blueprint.get('id', 'unknown')
                blueprint_name = blueprint.get('name', 'Unknown')
                
                blueprint_dep = {
                    'blueprint_name': blueprint_name,
                    'blueprint_id': blueprint_id,
                    'module': module_name,
                    'active': blueprint.get('active', False),
                    'states': [],
                    'transition_fields': [],
                    'criteria_fields': []
                }
                
                # Extract states
                if 'transitions' in blueprint:
                    for transition in blueprint['transitions']:
                        state = transition.get('name', '')
                        if state:
                            blueprint_dep['states'].append(state)
                        
                        # Fields in transitions
                        if 'fields' in transition:
                            for field in transition['fields']:
                                blueprint_dep['transition_fields'].append({
                                    'field_name': field.get('api_name', ''),
                                    'state': state,
                                    'required': field.get('required', False)
                                })
                
                # Extract criteria fields
                if 'criteria' in blueprint:
                    blueprint_dep['criteria_fields'] = self._extract_fields_from_criteria(
                        blueprint['criteria']
                    )
                
                dependencies['blueprint_dependencies'][f"{module_name}_{blueprint_id}"] = blueprint_dep
        
        # 4. Build Automation Chains
        dependencies['automation_chains'] = self._identify_automation_chains(dependencies)
        
        # 5. Build Cross-Module Dependency Map
        dependencies['cross_module_dependencies'] = self._build_cross_module_map(dependencies)
        
        # 6. Build Field Usage Matrix
        dependencies['field_usage_matrix'] = self._build_field_usage_matrix(data_model, dependencies)
        
        print("✅ Dependency analysis complete\n")
        return dependencies
    
    def _extract_fields_from_criteria(self, criteria: Any) -> List[str]:
        """Extract field names from workflow/blueprint criteria"""
        fields = []
        
        if isinstance(criteria, dict):
            # Direct field reference
            if 'field' in criteria:
                field_name = criteria.get('field')
                if isinstance(field_name, dict):
                    field_name = field_name.get('api_name', '')
                if field_name:
                    fields.append(field_name)
            
            # Nested criteria
            for key, value in criteria.items():
                if key in ['group', 'criteria']:
                    fields.extend(self._extract_fields_from_criteria(value))
        
        elif isinstance(criteria, list):
            for item in criteria:
                fields.extend(self._extract_fields_from_criteria(item))
        
        return list(set(fields))  # Remove duplicates
    
    def _extract_fields_from_actions(self, actions: List[Dict]) -> List[str]:
        """Extract field names from workflow actions"""
        fields = []
        
        for action in actions:
            # Field update actions
            if action.get('type') == 'field_update':
                field_name = action.get('field', {}).get('api_name')
                if field_name:
                    fields.append(field_name)
        
        return list(set(fields))
    
    def _identify_automation_chains(self, dependencies: Dict) -> List[Dict]:
        """Identify workflows that trigger other workflows"""
        chains = []
        
        for workflow_key, workflow in dependencies['workflow_dependencies'].items():
            for cross_module_action in workflow.get('cross_module_actions', []):
                target_module = cross_module_action['target_module']
                
                # Find workflows in target module that might be triggered
                triggered_workflows = [
                    w['workflow_name'] 
                    for k, w in dependencies['workflow_dependencies'].items()
                    if w['module'] == target_module and w['active']
                ]
                
                if triggered_workflows:
                    chains.append({
                        'source_module': workflow['module'],
                        'source_workflow': workflow['workflow_name'],
                        'action': cross_module_action['action_type'],
                        'target_module': target_module,
                        'possible_triggered_workflows': triggered_workflows
                    })
        
        return chains
    
    def _build_cross_module_map(self, dependencies: Dict) -> Dict:
        """Build a map of cross-module dependencies"""
        module_map = {}
        
        # From lookup relationships
        for module_name, lookups in dependencies.get('lookup_relationships', {}).items():
            for lookup in lookups:
                target_module = lookup['lookup_module']
                if target_module not in module_map:
                    module_map[target_module] = {
                        'referenced_by': [],
                        'workflows': [],
                        'relationships': []
                    }
                module_map[target_module]['referenced_by'].append({
                    'source_module': module_name,
                    'field': lookup['field_name'],
                    'required': lookup['required']
                })
        
        # From workflow cross-module actions
        for workflow_key, workflow in dependencies.get('workflow_dependencies', {}).items():
            for action in workflow.get('cross_module_actions', []):
                target_module = action['target_module']
                if target_module not in module_map:
                    module_map[target_module] = {
                        'referenced_by': [],
                        'workflows': [],
                        'relationships': []
                    }
                module_map[target_module]['workflows'].append({
                    'source_module': workflow['module'],
                    'workflow_name': workflow['workflow_name'],
                    'action_type': action['action_type']
                })
        
        return module_map
    
    def _build_field_usage_matrix(self, data_model: Dict, dependencies: Dict) -> Dict:
        """Build a matrix showing where each field is used"""
        matrix = {}
        
        for module_name, module_data in data_model.items():
            for field in module_data.get('fields', []):
                field_name = field.get('api_name', '')
                
                usage = {
                    'module': module_name,
                    'field_name': field_name,
                    'field_label': field.get('field_label', ''),
                    'data_type': field.get('data_type', ''),
                    'is_mandatory': field.get('required', False),
                    'is_custom': field.get('custom_field', False),
                    'used_in_workflows': [],
                    'used_in_blueprints': [],
                    'is_lookup': field.get('data_type') == 'lookup',
                    'is_formula': bool(field.get('formula'))
                }
                
                # Check workflow usage
                for workflow_key, workflow in dependencies.get('workflow_dependencies', {}).items():
                    if workflow['module'] == module_name:
                        # Check condition fields
                        if field_name in workflow.get('condition_fields', []):
                            usage['used_in_workflows'].append({
                                'workflow': workflow['workflow_name'],
                                'usage_type': 'condition'
                            })
                        
                        # Check updated fields
                        for updated_field in workflow.get('updated_fields', []):
                            if updated_field['field_name'] == field_name:
                                usage['used_in_workflows'].append({
                                    'workflow': workflow['workflow_name'],
                                    'usage_type': 'update'
                                })
                
                # Check blueprint usage
                for blueprint_key, blueprint in dependencies.get('blueprint_dependencies', {}).items():
                    if blueprint['module'] == module_name:
                        # Check transition fields
                        for trans_field in blueprint.get('transition_fields', []):
                            if trans_field['field_name'] == field_name:
                                usage['used_in_blueprints'].append({
                                    'blueprint': blueprint['blueprint_name'],
                                    'state': trans_field['state']
                                })
                
                matrix[f"{module_name}.{field_name}"] = usage
        
        return matrix
    
    def export_full_metadata(self) -> Dict:
        """Export complete CRM metadata"""
        print("=" * 60)
        print("🚀 Starting Zoho CRM Metadata Export")
        print("=" * 60)
        print()
        
        data_model = {}
        modules = self.get_modules()
        
        # Filter to API-enabled modules
        api_modules = [m for m in modules if m.get('api_supported')]
        
        print(f"📊 Processing {len(api_modules)} API-enabled modules...\n")
        
        for i, module in enumerate(api_modules, 1):
            module_name = module.get('api_name')
            if not module_name:
                continue
            
            print(f"[{i}/{len(api_modules)}] Processing: {module_name}")
            
            data_model[module_name] = {
                'module_info': module,
                'fields': self.get_module_fields(module_name),
                'layouts': self.get_module_layouts(module_name),
                'related_lists': self.get_module_related_lists(module_name),
                'custom_views': self.get_module_custom_views(module_name),
                'workflows': self.get_workflow_rules(module_name),
                'blueprints': self.get_blueprints(module_name)
            }
            
            field_count = len(data_model[module_name]['fields'])
            workflow_count = len(data_model[module_name]['workflows'])
            blueprint_count = len(data_model[module_name]['blueprints'])
            print(f"  ✅ {field_count} fields, {workflow_count} workflows, {blueprint_count} blueprints\n")
        
        return data_model


def save_json(data: Any, filename: str):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"💾 Saved: {filename}")


def create_excel_report(data_model: Dict, dependencies: Dict, filename: str):
    """Create comprehensive Excel workbook with multiple sheets"""
    try:
        import pandas as pd
        
        print("\n📊 Creating comprehensive Excel report...")
        
        # Sheet 1: Modules Overview
        modules_data = []
        for module_name, module_data in data_model.items():
            info = module_data.get('module_info', {})
            modules_data.append({
                'Module Name': module_name,
                'Display Name': info.get('module_name', ''),
                'Singular Label': info.get('singular_label', ''),
                'Plural Label': info.get('plural_label', ''),
                'API Supported': info.get('api_supported', False),
                'Creatable': info.get('creatable', False),
                'Editable': info.get('editable', False),
                'Deletable': info.get('deletable', False),
                'Field Count': len(module_data.get('fields', [])),
                'Workflow Count': len(module_data.get('workflows', [])),
                'Blueprint Count': len(module_data.get('blueprints', []))
            })
        
        # Sheet 2: All Fields
        fields_data = []
        for module_name, module_data in data_model.items():
            for field in module_data.get('fields', []):
                fields_data.append({
                    'Module': module_name,
                    'Field API Name': field.get('api_name', ''),
                    'Field Label': field.get('field_label', ''),
                    'Data Type': field.get('data_type', ''),
                    'Required': field.get('required', False),
                    'Read Only': field.get('read_only', False),
                    'Visible': field.get('visible', True),
                    'Custom Field': field.get('custom_field', False),
                    'Length': field.get('length', ''),
                    'Lookup Module': field.get('lookup', {}).get('module', {}).get('api_name', '') 
                        if field.get('data_type') == 'lookup' else ''
                })
        
        # Sheet 3: Workflow Overview
        workflows_data = []
        for module_name, module_data in data_model.items():
            for workflow in module_data.get('workflows', []):
                # Extract active status
                active = False
                if 'status' in workflow and isinstance(workflow['status'], dict):
                    active = workflow['status'].get('active', False)
                elif 'active' in workflow:
                    active = workflow.get('active', False)
                
                # Extract trigger type
                trigger_type = ''
                if 'execute_when' in workflow and isinstance(workflow['execute_when'], dict):
                    trigger_type = workflow['execute_when'].get('type', '')
                elif 'type' in workflow:
                    trigger_type = workflow.get('type', '')
                
                # Extract created by and modified by
                created_by = ''
                if 'created_by' in workflow and isinstance(workflow['created_by'], dict):
                    created_by = workflow['created_by'].get('name', '')
                
                modified_by = ''
                if 'modified_by' in workflow and isinstance(workflow['modified_by'], dict):
                    modified_by = workflow['modified_by'].get('name', '')
                
                workflows_data.append({
                    'Module': module_name,
                    'Workflow ID': workflow.get('id', ''),
                    'Workflow Name': workflow.get('name', ''),
                    'Description': workflow.get('description', ''),
                    'Active': active,
                    'Trigger Type': trigger_type,
                    'Created By': created_by,
                    'Modified By': modified_by,
                    'Created': workflow.get('created_time', ''),
                    'Last Executed': workflow.get('last_executed_time', ''),
                    'Modified': workflow.get('modified_time', '')
                })
        
        # Sheet 4: Workflow Dependencies
        workflow_deps_data = []
        for workflow_key, workflow in dependencies.get('workflow_dependencies', {}).items():
            condition_fields = ', '.join(workflow.get('condition_fields', []))
            updated_fields = ', '.join([f['field_name'] for f in workflow.get('updated_fields', [])])
            cross_module = ', '.join([
                f"{a['action_type']} → {a['target_module']}" 
                for a in workflow.get('cross_module_actions', [])
            ])
            external = ', '.join([f"{e['type']}: {e['name']}" for e in workflow.get('external_dependencies', [])])
            
            workflow_deps_data.append({
                'Module': workflow['module'],
                'Workflow Name': workflow['workflow_name'],
                'Active': workflow['active'],
                'Trigger Type': workflow['trigger_type'],
                'Condition Fields': condition_fields if condition_fields else '(API Limitation: Not available)',
                'Updated Fields': updated_fields if updated_fields else '(API Limitation: Not available)',
                'Cross-Module Actions': cross_module if cross_module else '',
                'External Dependencies': external if external else '',
                'Created By': workflow.get('created_by', ''),
                'Modified By': workflow.get('modified_by', ''),
                'Last Executed': workflow.get('last_executed_time', '')
            })
        
        # Sheet 5: Field Usage Matrix
        field_usage_data = []
        for field_key, usage in dependencies.get('field_usage_matrix', {}).items():
            workflow_usage = '; '.join([
                f"{w['workflow']} ({w['usage_type']})" 
                for w in usage.get('used_in_workflows', [])
            ])
            blueprint_usage = '; '.join([
                f"{b['blueprint']} - {b['state']}" 
                for b in usage.get('used_in_blueprints', [])
            ])
            
            field_usage_data.append({
                'Module': usage['module'],
                'Field': usage['field_name'],
                'Label': usage['field_label'],
                'Type': usage['data_type'],
                'Mandatory': usage['is_mandatory'],
                'Custom': usage['is_custom'],
                'Is Lookup': usage['is_lookup'],
                'Is Formula': usage['is_formula'],
                'Used in Workflows': workflow_usage,
                'Used in Blueprints': blueprint_usage
            })
        
        # Sheet 6: Automation Chains
        automation_data = []
        chains = dependencies.get('automation_chains', [])
        if chains:
            for chain in chains:
                automation_data.append({
                    'Source Module': chain['source_module'],
                    'Source Workflow': chain['source_workflow'],
                    'Action': chain['action'],
                    'Target Module': chain['target_module'],
                    'Possible Triggered Workflows': ', '.join(chain['possible_triggered_workflows'])
                })
        else:
            # Add placeholder row explaining why this is empty
            automation_data.append({
                'Source Module': '(No automation chains detected)',
                'Source Workflow': 'Automation chains require workflows with cross-module actions.',
                'Action': 'The Zoho API does not expose workflow actions.',
                'Target Module': 'See Sheet 4 for available workflow data.',
                'Possible Triggered Workflows': 'To view workflow actions, check Zoho CRM UI.'
            })
        
        # Sheet 7: Lookup Relationships
        lookup_data = []
        for module_name, lookups in dependencies.get('lookup_relationships', {}).items():
            for lookup in lookups:
                lookup_data.append({
                    'Source Module': module_name,
                    'Field Name': lookup['field_name'],
                    'Field Label': lookup['field_label'],
                    'Target Module': lookup['lookup_module'],
                    'Required': lookup['required']
                })
        
        # Sheet 8: Formula Fields
        formula_data = []
        for module_name, formulas in dependencies.get('formula_fields', {}).items():
            for formula in formulas:
                formula_data.append({
                    'Module': module_name,
                    'Field Name': formula['field_name'],
                    'Field Label': formula['field_label'],
                    'Formula': formula['formula'],
                    'Return Type': formula['return_type']
                })
        
        # Sheet 9: Mandatory Fields
        mandatory_data = []
        for module_name, fields in dependencies.get('mandatory_fields', {}).items():
            for field in fields:
                mandatory_data.append({
                    'Module': module_name,
                    'Field Name': field['field_name'],
                    'Field Label': field['field_label'],
                    'Data Type': field['data_type'],
                    'System Mandatory': field['system_mandatory']
                })
        
        # Sheet 10: Cross-Module Dependencies
        cross_module_data = []
        for target_module, refs in dependencies.get('cross_module_dependencies', {}).items():
            # Lookup references
            for ref in refs.get('referenced_by', []):
                cross_module_data.append({
                    'Target Module': target_module,
                    'Reference Type': 'Lookup',
                    'Source Module': ref['source_module'],
                    'Field': ref['field'],
                    'Required': ref['required'],
                    'Details': ''
                })
            
            # Workflow references
            for wf in refs.get('workflows', []):
                cross_module_data.append({
                    'Target Module': target_module,
                    'Reference Type': 'Workflow',
                    'Source Module': wf['source_module'],
                    'Field': '',
                    'Required': '',
                    'Details': f"{wf['workflow_name']} ({wf['action_type']})"
                })
        
        # Sheet 11: Dependency Summary
        summary_data = []
        for module_name, module_data in data_model.items():
            workflows = [w for k, w in dependencies.get('workflow_dependencies', {}).items() 
                        if w['module'] == module_name]
            blueprints = [b for k, b in dependencies.get('blueprint_dependencies', {}).items() 
                         if b['module'] == module_name]
            
            summary_data.append({
                'Module': module_name,
                'Total Fields': len(module_data.get('fields', [])),
                'Lookup Fields': len(dependencies.get('lookup_relationships', {}).get(module_name, [])),
                'Formula Fields': len(dependencies.get('formula_fields', {}).get(module_name, [])),
                'Mandatory Fields': len(dependencies.get('mandatory_fields', {}).get(module_name, [])),
                'Total Workflows': len(workflows),
                'Active Workflows': sum(1 for w in workflows if w['active']),
                'Workflows with Cross-Module Actions': sum(
                    1 for w in workflows if w.get('cross_module_actions')
                ),
                'Total Blueprints': len(blueprints),
                'Active Blueprints': sum(1 for b in blueprints if b['active'])
            })
        
        # Create Excel writer
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Always create all sheets in order
            if modules_data:
                pd.DataFrame(modules_data).to_excel(writer, sheet_name='1. Modules', index=False)
            if fields_data:
                pd.DataFrame(fields_data).to_excel(writer, sheet_name='2. All Fields', index=False)
            if workflows_data:
                pd.DataFrame(workflows_data).to_excel(writer, sheet_name='3. Workflows', index=False)
            if workflow_deps_data:
                pd.DataFrame(workflow_deps_data).to_excel(writer, sheet_name='4. Workflow Dependencies', index=False)
            if field_usage_data:
                pd.DataFrame(field_usage_data).to_excel(writer, sheet_name='5. Field Usage Matrix', index=False)
            # Always create Sheet 6 (even if empty/placeholder)
            pd.DataFrame(automation_data).to_excel(writer, sheet_name='6. Automation Chains', index=False)
            if lookup_data:
                pd.DataFrame(lookup_data).to_excel(writer, sheet_name='7. Lookup Relationships', index=False)
            if formula_data:
                pd.DataFrame(formula_data).to_excel(writer, sheet_name='8. Formula Fields', index=False)
            if mandatory_data:
                pd.DataFrame(mandatory_data).to_excel(writer, sheet_name='9. Mandatory Fields', index=False)
            if cross_module_data:
                pd.DataFrame(cross_module_data).to_excel(writer, sheet_name='10. Cross-Module Deps', index=False)
            if summary_data:
                pd.DataFrame(summary_data).to_excel(writer, sheet_name='11. Summary', index=False)
        
        # Count sheets with actual data
        sheets_with_data = sum([
            bool(modules_data), bool(fields_data), bool(workflows_data),
            bool(workflow_deps_data), bool(field_usage_data), True,  # automation always created
            bool(lookup_data), bool(formula_data), bool(mandatory_data),
            bool(cross_module_data), bool(summary_data)
        ])
        
        print(f"💾 Saved: {filename}")
        print(f"   📊 {sheets_with_data} sheets created with comprehensive dependency analysis")
        
    except ImportError:
        print("⚠️  pandas or openpyxl not installed. Skipping Excel export.")
        print("   Install with: pip install pandas openpyxl")


def main():
    """Main export process"""
    # Verify credentials
    if not all([CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, API_BASE, TOKEN_URL]):
        print("❌ Error: Missing credentials in .env file")
        print("Please ensure all required environment variables are set.")
        return
    
    # Create exporter
    exporter = ZohoExporter()
    
    # Export data
    data_model = exporter.export_full_metadata()
    
    # Extract dependencies
    dependencies = exporter.extract_field_dependencies(data_model)
    
    # Generate filenames with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d')
    json_filename = f'zoho-data-model-{timestamp}.json'
    dependencies_filename = f'zoho-dependencies-{timestamp}.json'
    excel_filename = f'Zoho_CRM_Data_Model_{timestamp}.xlsx'
    
    # Save outputs
    print("\n" + "=" * 60)
    print("💾 Saving Export Files")
    print("=" * 60)
    print()
    
    save_json(data_model, json_filename)
    save_json(dependencies, dependencies_filename)
    create_excel_report(data_model, dependencies, excel_filename)
    
    # Summary
    total_modules = len(data_model)
    total_fields = sum(len(m.get('fields', [])) for m in data_model.values())
    total_workflows = sum(len(m.get('workflows', [])) for m in data_model.values())
    total_blueprints = sum(len(m.get('blueprints', [])) for m in data_model.values())
    
    print("\n" + "=" * 60)
    print("✅ Export Complete!")
    print("=" * 60)
    print(f"""
Summary:
  • {total_modules} modules exported
  • {total_fields} fields documented
  • {total_workflows} workflows analyzed
  • {total_blueprints} blueprints captured
  
Output Files:
  • {json_filename} (full metadata)
  • {dependencies_filename} (enhanced relationships)
  • {excel_filename} (11-sheet comprehensive report)
    """)
    print("=" * 60)


if __name__ == '__main__':
    main()
