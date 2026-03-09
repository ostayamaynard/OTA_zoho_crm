#!/usr/bin/env python3
"""
Zoho CRM Metadata Export Script (v3.0 - Blueprint State Machine Edition)
Exports complete CRM configuration including REAL blueprint data via record-scoped API.

Key Insight: Blueprint definitions are NOT available via settings API.
They can ONLY be read via: /crm/v8/{module}/{record_id}/actions/blueprint

This script:
1. Exports standard metadata (modules, fields, workflows)
2. Discovers which modules have blueprints
3. Samples records in different stages to reconstruct the full state machine
4. Unions transitions across records to build dependency graph

READ-ONLY - Safe to run, cannot modify any data.
"""

import os
import json
import time
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional, Set, Tuple
from dotenv import load_dotenv
from collections import defaultdict

# Load environment variables
load_dotenv()

# Configuration
CLIENT_ID = os.getenv('ZOHO_CLIENT_ID')
CLIENT_SECRET = os.getenv('ZOHO_CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('ZOHO_REFRESH_TOKEN')
API_BASE = os.getenv('ZOHO_API_BASE', 'https://www.zohoapis.com.au/crm/v6').rstrip('/')
TOKEN_URL = os.getenv('ZOHO_TOKEN_URL', 'https://accounts.zoho.com.au/oauth/v2/token')

# Rate limiting
DELAY_BETWEEN_REQUESTS = 0.5
MAX_RETRIES = 3

# Blueprint sampling configuration
MAX_RECORDS_PER_STAGE = 3  # Sample multiple records per stage for comprehensive coverage
MAX_STAGES_TO_SAMPLE = 20  # Limit for modules with many stages


class ZohoExporter:
    """Handles Zoho CRM metadata export with blueprint state machine extraction"""
    
    def __init__(self):
        self.access_token = None
        self.token_expiry = 0
        self.session = requests.Session()
        
    def get_access_token(self) -> str:
        """Get or refresh access token"""
        current_time = time.time()
        
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
            
            if response.status_code != 200:
                print(f"❌ Token request failed with status {response.status_code}")
                print(f"Response: {response.text}")
                raise Exception(f"Failed to get access token: {response.text}")
            
            data = response.json()
            
            if 'access_token' not in data:
                print(f"❌ No access_token in response: {data}")
                raise Exception(f"Invalid token response: {data}")
            
            self.access_token = data['access_token']
            self.token_expiry = current_time + (data.get('expires_in', 3600) - 300)
            
            print("✅ Access token obtained successfully\n")
            return self.access_token
            
        except Exception as e:
            print(f"❌ Error getting access token: {e}")
            raise
    
    def make_request(self, endpoint: str, params: Dict = None, retry_count: int = 0) -> Optional[Dict]:
        """Make API request with retry logic and graceful 403 handling"""
        url = f"{API_BASE}/{endpoint}"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.get_access_token()}'
        }
        
        try:
            time.sleep(DELAY_BETWEEN_REQUESTS)
            response = self.session.get(url, headers=headers, params=params)
            
            # Handle rate limiting
            if response.status_code == 429:
                if retry_count < MAX_RETRIES:
                    wait_time = 2 ** retry_count
                    print(f"⏸️  Rate limited. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    return self.make_request(endpoint, params, retry_count + 1)
                else:
                    print(f"❌ Max retries reached for {endpoint}")
                    return None
            
            # Handle permission denied gracefully
            if response.status_code == 403:
                print(f"  ⚠️  Permission denied (403) for {endpoint}")
                return None
            
            # Handle not found
            if response.status_code == 404:
                return None
            
            # Handle no content
            if response.status_code == 204:
                return {}
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error requesting {endpoint}: {e}")
            return None

    # =========================================================================
    # STANDARD METADATA METHODS (unchanged from v2)
    # =========================================================================
    
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
        return response.get('fields', []) if response else []
    
    def get_module_layouts(self, module_name: str) -> List[Dict]:
        """Fetch layouts for a specific module"""
        response = self.make_request('settings/layouts', {'module': module_name})
        return response.get('layouts', []) if response else []
    
    def get_module_related_lists(self, module_name: str) -> List[Dict]:
        """Fetch related lists for a specific module"""
        response = self.make_request('settings/related_lists', {'module': module_name})
        return response.get('related_lists', []) if response else []
    
    def get_module_custom_views(self, module_name: str) -> List[Dict]:
        """Fetch custom views for a specific module"""
        response = self.make_request('settings/custom_views', {'module': module_name})
        return response.get('custom_views', []) if response else []
    
    def get_workflow_rules(self, module_name: str) -> List[Dict]:
        """Fetch workflow rules with pagination"""
        all_workflows = []
        page = 1
        per_page = 200
        
        while True:
            params = {'module': module_name, 'page': page, 'per_page': per_page}
            response = self.make_request('settings/automation/workflow_rules', params)
            
            if not response or 'workflow_rules' not in response:
                break
            
            workflows = response['workflow_rules']
            all_workflows.extend(workflows)
            
            info = response.get('info', {})
            if not info.get('more_records') or len(workflows) < per_page:
                break
            
            page += 1
        
        return all_workflows

    # =========================================================================
    # BLUEPRINT STATE MACHINE EXTRACTION (NEW in v3)
    # =========================================================================
    
    def get_blueprint_summary(self, module_name: str) -> List[Dict]:
        """
        Get blueprint SUMMARY from settings endpoint.
        This only tells us IF a blueprint exists, not its structure.
        """
        response = self.make_request('settings/blueprints', {'module': module_name})
        return response.get('blueprints', []) if response else []
    
    def get_record_blueprint(self, module_name: str, record_id: str) -> Optional[Dict]:
        """
        Fetch blueprint state for a SPECIFIC record.
        This is the ONLY way to get actual blueprint structure.
        
        Returns: Blueprint data including current state, available transitions,
                 required fields, validation rules, etc.
        """
        endpoint = f"{module_name}/{record_id}/actions/blueprint"
        response = self.make_request(endpoint)
        
        if response and 'blueprint' in response:
            return response['blueprint']
        return None
    
    def find_stage_field(self, fields: List[Dict]) -> Optional[str]:
        """
        Identify the stage/status field used by blueprint.
        Usually 'Stage', 'Status', 'Lead_Status', etc.
        """
        # Common stage field names (in order of priority)
        stage_candidates = [
            'Stage', 'Status', 'Lead_Status', 'Deal_Stage', 
            'Quote_Stage', 'Invoice_Status', 'Order_Status',
            'Registration_Status', 'Course_Stage'
        ]
        
        # First pass: exact match
        for field in fields:
            api_name = field.get('api_name', '')
            if api_name in stage_candidates:
                return api_name
        
        # Second pass: picklist fields with 'stage' or 'status' in name
        for field in fields:
            api_name = field.get('api_name', '').lower()
            data_type = field.get('data_type', '')
            if data_type == 'picklist' and ('stage' in api_name or 'status' in api_name):
                return field.get('api_name')
        
        return None
    
    def get_stage_values(self, fields: List[Dict], stage_field: str) -> List[str]:
        """Extract all possible stage values from the picklist field"""
        for field in fields:
            if field.get('api_name') == stage_field:
                pick_list_values = field.get('pick_list_values', [])
                return [v.get('display_value') or v.get('actual_value') 
                        for v in pick_list_values if v]
        return []
    
    def get_records_by_stage(self, module_name: str, stage_field: str, 
                             stage_value: str, limit: int = 3) -> List[Dict]:
        """
        Fetch records in a specific stage.
        Returns list of records with their IDs.
        """
        # Use COQL for precise filtering
        # Note: Some modules may not support COQL, fall back to search
        
        # Try search API first
        params = {
            'criteria': f"({stage_field}:equals:{stage_value})",
            'per_page': limit
        }
        
        response = self.make_request(f'{module_name}/search', params)
        
        if response and 'data' in response:
            return response['data']
        
        return []
    
    def get_sample_records(self, module_name: str, limit: int = 50) -> List[Dict]:
        """
        Fetch sample records from a module (fallback when stage search fails).
        Gets a diverse sample to hopefully capture different stages.
        """
        response = self.make_request(module_name, {'per_page': limit})
        
        if response and 'data' in response:
            return response['data']
        
        return []
    
    def extract_blueprint_state_machine(self, module_name: str, 
                                        fields: List[Dict]) -> Dict:
        """
        Main method to extract blueprint state machine by sampling records.
        
        Strategy:
        1. Check if module has blueprints
        2. Find the stage field
        3. Get records in each stage
        4. Query blueprint endpoint for each record
        5. Union all transitions to build complete graph
        
        Returns: Complete blueprint structure with states and transitions
        """
        result = {
            'module': module_name,
            'has_blueprint': False,
            'stage_field': None,
            'states': {},
            'transitions': [],
            'transition_fields': {},
            'role_restrictions': {},
            'validation_rules': [],
            'sampling_info': {
                'records_sampled': 0,
                'stages_covered': [],
                'extraction_time': None
            }
        }
        
        start_time = datetime.now()
        
        # Step 1: Check if blueprint exists
        bp_summary = self.get_blueprint_summary(module_name)
        if not bp_summary:
            return result
        
        result['has_blueprint'] = True
        result['blueprint_summary'] = bp_summary
        print(f"  🗺️  Blueprint found, extracting state machine...")
        
        # Step 2: Find stage field
        stage_field = self.find_stage_field(fields)
        if not stage_field:
            print(f"  ⚠️  Could not identify stage field for {module_name}")
            # Fallback: sample random records
            stage_field = 'Status'  # Common default
        
        result['stage_field'] = stage_field
        
        # Step 3: Get all stage values
        stage_values = self.get_stage_values(fields, stage_field)
        
        # Track all discovered data
        all_transitions = {}  # transition_id -> transition_data
        all_states = {}  # state_name -> state_data
        all_fields_by_transition = {}  # transition_id -> list of fields
        records_sampled = 0
        stages_covered = set()
        
        # Step 4: Sample records from each stage
        if stage_values:
            for stage_value in stage_values[:MAX_STAGES_TO_SAMPLE]:
                records = self.get_records_by_stage(
                    module_name, stage_field, stage_value, MAX_RECORDS_PER_STAGE
                )
                
                if not records:
                    continue
                
                stages_covered.add(stage_value)
                
                for record in records:
                    record_id = record.get('id')
                    if not record_id:
                        continue
                    
                    # Get blueprint for this specific record
                    bp_data = self.get_record_blueprint(module_name, record_id)
                    if not bp_data:
                        continue
                    
                    records_sampled += 1
                    
                    # Extract current state
                    current_state = bp_data.get('current_stage')
                    if current_state:
                        state_id = current_state.get('id')
                        state_name = current_state.get('name')
                        if state_id and state_id not in all_states:
                            all_states[state_id] = {
                                'id': state_id,
                                'name': state_name,
                                'display_name': current_state.get('display_name', state_name),
                                'color': current_state.get('color'),
                                'type': current_state.get('type'),
                                'outgoing_transitions': []
                            }
                    
                    # Extract available transitions
                    transitions = bp_data.get('transitions', [])
                    for trans in transitions:
                        trans_id = trans.get('id')
                        if not trans_id:
                            continue
                        
                        # Store/update transition
                        if trans_id not in all_transitions:
                            all_transitions[trans_id] = {
                                'id': trans_id,
                                'name': trans.get('name'),
                                'display_name': trans.get('display_name'),
                                'type': trans.get('type'),
                                'source_state': current_state.get('name') if current_state else None,
                                'target_state': trans.get('next_field_value'),
                                'next_transitions': trans.get('next_transitions', []),
                                'percent_partial_save': trans.get('percent_partial_save'),
                                'execution_time': trans.get('execution_time'),
                                'criteria_matched': trans.get('criteria_matched'),
                                'data': trans.get('data', {})
                            }
                            
                            # Track outgoing transitions for source state
                            if current_state:
                                state_id = current_state.get('id')
                                if state_id in all_states:
                                    if trans_id not in all_states[state_id]['outgoing_transitions']:
                                        all_states[state_id]['outgoing_transitions'].append(trans_id)
                        
                        # Extract fields for this transition
                        trans_fields = trans.get('fields', [])
                        if trans_fields:
                            if trans_id not in all_fields_by_transition:
                                all_fields_by_transition[trans_id] = []
                            
                            for field in trans_fields:
                                field_entry = {
                                    'api_name': field.get('api_name'),
                                    'field_label': field.get('field_label'),
                                    'required': field.get('_required', False),
                                    'read_only': field.get('read_only', False),
                                    'visible': field.get('visible', True),
                                    'data_type': field.get('data_type'),
                                    'pick_list_values': field.get('pick_list_values', []),
                                    'validation_rule': field.get('validation_rule'),
                                    'default_value': field.get('default_value'),
                                    'webhook': field.get('webhook', False),
                                    'tooltip': field.get('tooltip')
                                }
                                
                                # Check if already captured (avoid duplicates)
                                existing = [f for f in all_fields_by_transition[trans_id] 
                                           if f['api_name'] == field_entry['api_name']]
                                if not existing:
                                    all_fields_by_transition[trans_id].append(field_entry)
        
        # Fallback: if no records found via stage search, try general sample
        if records_sampled == 0:
            print(f"  ⚠️  Stage search returned no results, trying general sample...")
            sample_records = self.get_sample_records(module_name, 20)
            
            for record in sample_records:
                record_id = record.get('id')
                if not record_id:
                    continue
                
                bp_data = self.get_record_blueprint(module_name, record_id)
                if not bp_data:
                    continue
                
                records_sampled += 1
                
                # Same extraction logic as above
                current_state = bp_data.get('current_stage')
                if current_state:
                    state_id = current_state.get('id')
                    state_name = current_state.get('name')
                    if state_id and state_id not in all_states:
                        all_states[state_id] = {
                            'id': state_id,
                            'name': state_name,
                            'display_name': current_state.get('display_name', state_name),
                            'color': current_state.get('color'),
                            'type': current_state.get('type'),
                            'outgoing_transitions': []
                        }
                    stages_covered.add(state_name)
                
                transitions = bp_data.get('transitions', [])
                for trans in transitions:
                    trans_id = trans.get('id')
                    if not trans_id or trans_id in all_transitions:
                        continue
                    
                    all_transitions[trans_id] = {
                        'id': trans_id,
                        'name': trans.get('name'),
                        'display_name': trans.get('display_name'),
                        'type': trans.get('type'),
                        'source_state': current_state.get('name') if current_state else None,
                        'target_state': trans.get('next_field_value'),
                        'next_transitions': trans.get('next_transitions', []),
                        'data': trans.get('data', {})
                    }
                    
                    if current_state:
                        state_id = current_state.get('id')
                        if state_id in all_states:
                            if trans_id not in all_states[state_id]['outgoing_transitions']:
                                all_states[state_id]['outgoing_transitions'].append(trans_id)
                    
                    trans_fields = trans.get('fields', [])
                    if trans_fields and trans_id not in all_fields_by_transition:
                        all_fields_by_transition[trans_id] = [
                            {
                                'api_name': f.get('api_name'),
                                'field_label': f.get('field_label'),
                                'required': f.get('_required', False),
                                'read_only': f.get('read_only', False),
                                'visible': f.get('visible', True),
                                'data_type': f.get('data_type')
                            }
                            for f in trans_fields
                        ]
        
        # Compile results
        result['states'] = all_states
        result['transitions'] = list(all_transitions.values())
        result['transition_fields'] = all_fields_by_transition
        result['sampling_info'] = {
            'records_sampled': records_sampled,
            'stages_covered': list(stages_covered),
            'total_states_discovered': len(all_states),
            'total_transitions_discovered': len(all_transitions),
            'extraction_time': str(datetime.now() - start_time)
        }
        
        print(f"  ✅ Extracted {len(all_states)} states, {len(all_transitions)} transitions from {records_sampled} records")
        
        return result

    # =========================================================================
    # DEPENDENCY EXTRACTION (enhanced for blueprints)
    # =========================================================================
    
    def extract_field_dependencies(self, data_model: Dict) -> Dict:
        """Extract comprehensive field dependencies including blueprint data"""
        dependencies = {
            'workflow_field_usage': {},
            'lookup_relationships': {},
            'picklist_dependencies': {},
            'formula_fields': {},
            'mandatory_fields': {},
            'unique_fields': {},
            'workflow_dependencies': {},
            'blueprint_dependencies': {},  # Enhanced with state machine data
            'automation_chains': [],
            'cross_module_dependencies': {},
            'field_usage_matrix': {}
        }
        
        print("\n🔍 Analysing comprehensive field dependencies...")
        
        for module_name, module_data in data_model.items():
            fields = module_data.get('fields', [])
            workflows = module_data.get('workflows', [])
            blueprint_data = module_data.get('blueprint_state_machine', {})
            
            # Field analysis (unchanged)
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
            
            # Workflow analysis (unchanged)
            for workflow in workflows:
                workflow_id = workflow.get('id', 'unknown')
                workflow_name = workflow.get('name', 'Unknown')
                
                active = False
                if 'status' in workflow and isinstance(workflow['status'], dict):
                    active = workflow['status'].get('active', False)
                elif 'active' in workflow:
                    active = workflow.get('active', False)
                
                trigger_type = ''
                if 'execute_when' in workflow and isinstance(workflow['execute_when'], dict):
                    trigger_type = workflow['execute_when'].get('type', '')
                elif 'type' in workflow:
                    trigger_type = workflow.get('type', '')
                
                workflow_dep = {
                    'workflow_name': workflow_name,
                    'workflow_id': workflow_id,
                    'module': module_name,
                    'active': active,
                    'trigger_type': trigger_type,
                    'condition_fields': [],
                    'updated_fields': [],
                    'cross_module_actions': [],
                    'external_dependencies': []
                }
                
                dependencies['workflow_dependencies'][f"{module_name}_{workflow_id}"] = workflow_dep
            
            # Blueprint dependency analysis (NEW - enhanced)
            if blueprint_data.get('has_blueprint'):
                bp_dep = {
                    'module': module_name,
                    'has_blueprint': True,
                    'stage_field': blueprint_data.get('stage_field'),
                    'states': list(blueprint_data.get('states', {}).keys()),
                    'state_names': [s.get('name') for s in blueprint_data.get('states', {}).values()],
                    'transitions': [
                        {
                            'id': t.get('id'),
                            'name': t.get('name'),
                            'source': t.get('source_state'),
                            'target': t.get('target_state')
                        }
                        for t in blueprint_data.get('transitions', [])
                    ],
                    'required_fields_by_transition': {},
                    'sampling_info': blueprint_data.get('sampling_info', {})
                }
                
                # Extract required fields per transition
                for trans_id, trans_fields in blueprint_data.get('transition_fields', {}).items():
                    required = [f['api_name'] for f in trans_fields if f.get('required')]
                    if required:
                        bp_dep['required_fields_by_transition'][trans_id] = required
                
                dependencies['blueprint_dependencies'][module_name] = bp_dep
        
        print("✅ Dependency analysis complete\n")
        return dependencies

    # =========================================================================
    # MAIN EXPORT ORCHESTRATION
    # =========================================================================
    
    def export_full_metadata(self) -> Dict:
        """Export complete CRM metadata including blueprint state machines"""
        print("=" * 70)
        print("🚀 Starting Zoho CRM Metadata Export (v3.0 - Blueprint Edition)")
        print("=" * 70)
        print()
        
        data_model = {}
        modules = self.get_modules()
        
        api_modules = [m for m in modules if m.get('api_supported')]
        
        print(f"📊 Processing {len(api_modules)} API-enabled modules...\n")
        
        for i, module in enumerate(api_modules, 1):
            module_name = module.get('api_name')
            if not module_name:
                continue
            
            print(f"[{i}/{len(api_modules)}] Processing: {module_name}")
            
            # Standard metadata
            fields = self.get_module_fields(module_name)
            workflows = self.get_workflow_rules(module_name)
            
            data_model[module_name] = {
                'module_info': module,
                'fields': fields,
                'layouts': self.get_module_layouts(module_name),
                'related_lists': self.get_module_related_lists(module_name),
                'custom_views': self.get_module_custom_views(module_name),
                'workflows': workflows,
                'blueprint_summary': self.get_blueprint_summary(module_name),
                'blueprint_state_machine': {}  # Will be populated below
            }
            
            # Check for blueprints and extract state machine
            if data_model[module_name]['blueprint_summary']:
                data_model[module_name]['blueprint_state_machine'] = \
                    self.extract_blueprint_state_machine(module_name, fields)
            
            field_count = len(fields)
            workflow_count = len(workflows)
            has_bp = '🗺️' if data_model[module_name]['blueprint_summary'] else ''
            print(f"  ✅ {field_count} fields, {workflow_count} workflows {has_bp}\n")
        
        return data_model


def save_json(data: Any, filename: str):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"💾 Saved: {filename}")


def create_excel_report(data_model: Dict, dependencies: Dict, filename: str):
    """Create comprehensive Excel workbook with blueprint sheets"""
    try:
        import pandas as pd
        
        print("\n📊 Creating comprehensive Excel report...")
        
        # Sheet 1: Modules Overview
        modules_data = []
        for module_name, module_data in data_model.items():
            info = module_data.get('module_info', {})
            bp_sm = module_data.get('blueprint_state_machine', {})
            modules_data.append({
                'Module Name': module_name,
                'Display Name': info.get('module_name', ''),
                'Singular Label': info.get('singular_label', ''),
                'Field Count': len(module_data.get('fields', [])),
                'Workflow Count': len(module_data.get('workflows', [])),
                'Has Blueprint': '✅' if bp_sm.get('has_blueprint') else '',
                'Blueprint States': bp_sm.get('sampling_info', {}).get('total_states_discovered', 0),
                'Blueprint Transitions': bp_sm.get('sampling_info', {}).get('total_transitions_discovered', 0)
            })
        
        # Sheet 2: All Fields (unchanged)
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
                    'Custom Field': field.get('custom_field', False),
                    'Lookup Module': field.get('lookup', {}).get('module', {}).get('api_name', '') 
                        if field.get('data_type') == 'lookup' else ''
                })
        
        # Sheet 3: Workflows (unchanged)
        workflows_data = []
        for module_name, module_data in data_model.items():
            for workflow in module_data.get('workflows', []):
                active = False
                if 'status' in workflow and isinstance(workflow['status'], dict):
                    active = workflow['status'].get('active', False)
                
                workflows_data.append({
                    'Module': module_name,
                    'Workflow ID': workflow.get('id', ''),
                    'Workflow Name': workflow.get('name', ''),
                    'Active': active,
                    'Last Executed': workflow.get('last_executed_time', '')
                })
        
        # Sheet 4: Blueprint States (NEW)
        bp_states_data = []
        for module_name, module_data in data_model.items():
            bp_sm = module_data.get('blueprint_state_machine', {})
            if not bp_sm.get('has_blueprint'):
                continue
            
            for state_id, state in bp_sm.get('states', {}).items():
                bp_states_data.append({
                    'Module': module_name,
                    'State ID': state_id,
                    'State Name': state.get('name', ''),
                    'Display Name': state.get('display_name', ''),
                    'Type': state.get('type', ''),
                    'Colour': state.get('color', ''),
                    'Outgoing Transitions': len(state.get('outgoing_transitions', []))
                })
        
        # Sheet 5: Blueprint Transitions (NEW)
        bp_transitions_data = []
        for module_name, module_data in data_model.items():
            bp_sm = module_data.get('blueprint_state_machine', {})
            if not bp_sm.get('has_blueprint'):
                continue
            
            for trans in bp_sm.get('transitions', []):
                bp_transitions_data.append({
                    'Module': module_name,
                    'Transition ID': trans.get('id', ''),
                    'Transition Name': trans.get('name', ''),
                    'Source State': trans.get('source_state', ''),
                    'Target State': trans.get('target_state', ''),
                    'Type': trans.get('type', ''),
                    'Criteria Matched': trans.get('criteria_matched', '')
                })
        
        # Sheet 6: Blueprint Required Fields (NEW)
        bp_fields_data = []
        for module_name, module_data in data_model.items():
            bp_sm = module_data.get('blueprint_state_machine', {})
            if not bp_sm.get('has_blueprint'):
                continue
            
            for trans_id, trans_fields in bp_sm.get('transition_fields', {}).items():
                # Get transition name
                trans_name = next(
                    (t.get('name') for t in bp_sm.get('transitions', []) if t.get('id') == trans_id),
                    trans_id
                )
                
                for field in trans_fields:
                    bp_fields_data.append({
                        'Module': module_name,
                        'Transition': trans_name,
                        'Field API Name': field.get('api_name', ''),
                        'Field Label': field.get('field_label', ''),
                        'Required': '✅' if field.get('required') else '',
                        'Read Only': field.get('read_only', False),
                        'Visible': field.get('visible', True),
                        'Data Type': field.get('data_type', '')
                    })
        
        # Sheet 7: Blueprint Sampling Info (NEW)
        bp_sampling_data = []
        for module_name, module_data in data_model.items():
            bp_sm = module_data.get('blueprint_state_machine', {})
            if not bp_sm.get('has_blueprint'):
                continue
            
            sampling = bp_sm.get('sampling_info', {})
            bp_sampling_data.append({
                'Module': module_name,
                'Stage Field': bp_sm.get('stage_field', ''),
                'Records Sampled': sampling.get('records_sampled', 0),
                'Stages Covered': ', '.join(sampling.get('stages_covered', [])),
                'States Discovered': sampling.get('total_states_discovered', 0),
                'Transitions Discovered': sampling.get('total_transitions_discovered', 0),
                'Extraction Time': sampling.get('extraction_time', '')
            })
        
        # Sheet 8: Lookup Relationships (unchanged)
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
        
        # Create Excel writer
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            if modules_data:
                pd.DataFrame(modules_data).to_excel(writer, sheet_name='1. Modules', index=False)
            if fields_data:
                pd.DataFrame(fields_data).to_excel(writer, sheet_name='2. All Fields', index=False)
            if workflows_data:
                pd.DataFrame(workflows_data).to_excel(writer, sheet_name='3. Workflows', index=False)
            if bp_states_data:
                pd.DataFrame(bp_states_data).to_excel(writer, sheet_name='4. Blueprint States', index=False)
            if bp_transitions_data:
                pd.DataFrame(bp_transitions_data).to_excel(writer, sheet_name='5. BP Transitions', index=False)
            if bp_fields_data:
                pd.DataFrame(bp_fields_data).to_excel(writer, sheet_name='6. BP Required Fields', index=False)
            if bp_sampling_data:
                pd.DataFrame(bp_sampling_data).to_excel(writer, sheet_name='7. BP Sampling Info', index=False)
            if lookup_data:
                pd.DataFrame(lookup_data).to_excel(writer, sheet_name='8. Lookup Relationships', index=False)
        
        print(f"💾 Saved: {filename}")
        print(f"   📊 8 sheets created (including 4 new Blueprint sheets)")
        
    except ImportError:
        print("⚠️  pandas or openpyxl not installed. Skipping Excel export.")
        print("   Install with: pip install pandas openpyxl")


def main():
    """Main export process"""
    # Verify credentials
    if not all([CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN]):
        print("❌ Error: Missing credentials in .env file")
        print("Please ensure ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, and ZOHO_REFRESH_TOKEN are set.")
        return
    
    print(f"🌏 Using API Base: {API_BASE}")
    print(f"🔑 Token URL: {TOKEN_URL}\n")
    
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
    print("\n" + "=" * 70)
    print("💾 Saving Export Files")
    print("=" * 70)
    print()
    
    save_json(data_model, json_filename)
    save_json(dependencies, dependencies_filename)
    create_excel_report(data_model, dependencies, excel_filename)
    
    # Summary
    total_modules = len(data_model)
    total_fields = sum(len(m.get('fields', [])) for m in data_model.values())
    total_workflows = sum(len(m.get('workflows', [])) for m in data_model.values())
    
    modules_with_bp = sum(
        1 for m in data_model.values() 
        if m.get('blueprint_state_machine', {}).get('has_blueprint')
    )
    total_bp_states = sum(
        m.get('blueprint_state_machine', {}).get('sampling_info', {}).get('total_states_discovered', 0)
        for m in data_model.values()
    )
    total_bp_transitions = sum(
        m.get('blueprint_state_machine', {}).get('sampling_info', {}).get('total_transitions_discovered', 0)
        for m in data_model.values()
    )
    
    print("\n" + "=" * 70)
    print("✅ Export Complete!")
    print("=" * 70)
    print(f"""
Summary:
  • {total_modules} modules exported
  • {total_fields} fields documented
  • {total_workflows} workflows analysed
  
Blueprint State Machines:
  • {modules_with_bp} modules have blueprints
  • {total_bp_states} states discovered
  • {total_bp_transitions} transitions mapped
  
Output Files:
  • {json_filename} (full metadata + blueprints)
  • {dependencies_filename} (enhanced relationships)
  • {excel_filename} (8-sheet report with blueprint data)
    """)
    print("=" * 70)


if __name__ == '__main__':
    main()
