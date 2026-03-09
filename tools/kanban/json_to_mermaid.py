#!/usr/bin/env python3
"""
JSON to Mermaid Diagram Converter for Zoho CRM Workflows
Converts customer journey JSON files into Mermaid.js diagram syntax

Usage: python3 json_to_mermaid.py
Output: Multiple .mmd files ready for rendering
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parents[2]
JSON_SOURCES = {
    'overview': ROOT_DIR / 'modules/overview/data/customer-journey-overview.json',
    'leads': ROOT_DIR / 'modules/leads/data/customer-journey-leads.json',
    'deals': ROOT_DIR / 'modules/deals/data/customer-journey-deals.json',
    'courses': ROOT_DIR / 'modules/courses/data/customer-journey-courses.json',
    'course_attendees': ROOT_DIR / 'modules/courses/data/customer-journey-course-attendees.json',
    'invoices': ROOT_DIR / 'modules/invoices/data/customer-journey-invoices.json',
    'quotes': ROOT_DIR / 'modules/quotes/data/customer-journey-quotes.json'
}
OUTPUT_DESTINATIONS = {
    'overview-complete-journey.mmd': ROOT_DIR / 'modules/overview/diagrams/overview-complete-journey.mmd',
    'leads-workflow.mmd': ROOT_DIR / 'modules/leads/diagrams/leads-workflow.mmd',
    'deals-workflow.mmd': ROOT_DIR / 'modules/deals/diagrams/deals-workflow.mmd',
    'courses-workflow.mmd': ROOT_DIR / 'modules/courses/diagrams/courses-workflow.mmd',
    'course-attendees-journey.mmd': ROOT_DIR / 'modules/courses/diagrams/course-attendees-journey.mmd',
    'invoices-payment-flow.mmd': ROOT_DIR / 'modules/invoices/diagrams/invoices-payment-flow.mmd',
    'quotes-lifecycle.mmd': ROOT_DIR / 'modules/quotes/diagrams/quotes-lifecycle.mmd',
    'module-relationships.mmd': ROOT_DIR / 'modules/overview/diagrams/module-relationships.mmd',
    'integration-architecture.mmd': ROOT_DIR / 'modules/overview/diagrams/integration-architecture.mmd',
    'registration-timeline.mmd': ROOT_DIR / 'modules/courses/diagrams/registration-timeline.mmd'
}
DEFAULT_OUTPUT_DIR = ROOT_DIR / 'modules/overview/diagrams'
README_PATH = ROOT_DIR / 'docs/mermaid-readme.md'

# Color scheme based on trigger types
COLORS = {
    'automatic': '#90EE90',  # Green
    'manual': '#2196F3',     # Blue
    'third_party': '#FF9800', # Orange
    'human_input': '#FFEB3B', # Yellow
    'error': '#F44336'        # Red
}

class MermaidGenerator:
    """Generate Mermaid diagrams from Zoho CRM workflow JSON files"""
    
    def __init__(self, output_dir: Optional[Path] = None):
        if output_dir is None:
            output_dir = DEFAULT_OUTPUT_DIR
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.json_files = {}
        
    def load_json_files(self):
        """Load all customer journey JSON files"""
        for key, filepath in JSON_SOURCES.items():
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.json_files[key] = json.load(f)
                    relative = filepath.relative_to(ROOT_DIR)
                    print(f"✓ Loaded {relative}")
            else:
                relative = filepath.relative_to(ROOT_DIR)
                print(f"✗ Not found: {relative}")
                
        return len(self.json_files)
    
    def sanitize_id(self, text: str) -> str:
        """Convert text to valid Mermaid node ID"""
        return text.replace(' ', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '').replace('.', '_')
    
    def escape_label(self, text: str) -> str:
        """Escape special characters in labels"""
        return text.replace('"', "'").replace('[', '(').replace(']', ')')
    
    def get_trigger_color(self, trigger_type: str) -> str:
        """Get color for trigger type"""
        return COLORS.get(trigger_type, '#CCCCCC')
    
    def generate_flowchart(self, data: Dict, module_name: str) -> str:
        """Generate flowchart for a specific module"""
        mermaid = f"graph TD\n"
        mermaid += f"    %% {module_name.title()} Customer Journey\n\n"
        
        if 'customer_journey' not in data:
            return mermaid + "    NoData[No Journey Data Available]\n"
        
        journey = data['customer_journey']
        stages = sorted(journey.items(), key=lambda x: journey[x[0]].get('stage_order', 0))
        
        # Generate nodes
        for stage_name, stage_data in stages:
            node_id = self.sanitize_id(stage_name)
            stage_order = stage_data.get('stage_order', 0)
            description = self.escape_label(stage_data.get('description', stage_name))
            
            mermaid += f"    {node_id}[\"{stage_order}. {stage_name.replace('_', ' ')}<br/>{description}\"]\n"
        
        mermaid += "\n"
        
        # Generate connections
        for stage_name, stage_data in stages:
            node_id = self.sanitize_id(stage_name)
            next_stage = stage_data.get('next')
            
            if next_stage:
                next_id = self.sanitize_id(next_stage)
                mermaid += f"    {node_id} --> {next_id}\n"
            
            # Add decision points
            if stage_data.get('decision_point'):
                outcomes = stage_data.get('outcomes', {})
                for outcome_name, outcome_data in outcomes.items():
                    if isinstance(outcome_data, dict) and 'path' in outcome_data:
                        decision_id = f"{node_id}_Decision"
                        path_label = self.escape_label(outcome_data['path'])
                        mermaid += f"    {node_id} --> {decision_id}{{{outcome_name.replace('_', ' ')}}}\n"
                        break
        
        mermaid += "\n"
        
        # Add styling for workflows
        for stage_name, stage_data in stages:
            node_id = self.sanitize_id(stage_name)
            workflows = stage_data.get('related_workflows', [])
            
            if workflows:
                for idx, wf in enumerate(workflows[:3]):  # Limit to 3 for readability
                    wf_id = f"{node_id}_WF{idx}"
                    wf_name = self.escape_label(wf.get('workflow_name', ''))
                    trigger = wf.get('trigger', 'automatic')
                    color = self.get_trigger_color(trigger)
                    
                    mermaid += f"    {wf_id}[\"{wf_name}<br/>ID: {wf.get('workflow_id', 'N/A')}\"]\n"
                    mermaid += f"    style {wf_id} fill:{color}\n"
                    mermaid += f"    {node_id} -.->|triggers| {wf_id}\n"
        
        return mermaid
    
    def generate_swimlane_diagram(self) -> str:
        """Generate overview diagram with module swimlanes"""
        if 'overview' not in self.json_files:
            return "graph TD\n    NoData[Overview data not available]\n"
        
        data = self.json_files['overview']
        mermaid = "graph TB\n"
        mermaid += "    %% Complete Customer Journey - All Modules\n\n"
        
        if 'complete_customer_journey' in data:
            journey = data['complete_customer_journey']
            
            # Group by module
            modules = {
                'Leads': [],
                'Deals': [],
                'Quotes': [],
                'Invoices': [],
                'Courses': [],
                'Registration_Records': []
            }
            
            for stage_name, stage_data in journey.items():
                module = stage_data.get('module', 'Unknown')
                if module in modules:
                    modules[module].append((stage_name, stage_data))
            
            # Generate subgraphs for each module
            for module_name, stages in modules.items():
                if stages:
                    mermaid += f"    subgraph {self.sanitize_id(module_name)}[\"{module_name}\"]\n"
                    for stage_name, stage_data in stages:
                        node_id = self.sanitize_id(stage_name)
                        desc = self.escape_label(stage_data.get('description', ''))[:40]
                        mermaid += f"        {node_id}[\"{stage_name.replace('_', ' ')}<br/>{desc}\"]\n"
                    mermaid += "    end\n\n"
            
            # Add connections between stages
            for stage_name, stage_data in journey.items():
                node_id = self.sanitize_id(stage_name)
                next_stage = stage_data.get('next_stage')
                if next_stage:
                    next_id = self.sanitize_id(next_stage)
                    mermaid += f"    {node_id} --> {next_id}\n"
        
        return mermaid
    
    def generate_er_diagram(self) -> str:
        """Generate entity-relationship diagram for modules"""
        if 'overview' not in self.json_files:
            return "erDiagram\n    NODATA ||--|| NODATA : missing\n"
        
        data = self.json_files['overview']
        mermaid = "erDiagram\n"
        mermaid += "    %% Module Relationships - Lookup Fields\n\n"
        
        if 'module_dependency_map' in data:
            deps = data['module_dependency_map']
            
            for module, module_data in deps.items():
                converts_to = module_data.get('converts_to', [])
                for target in converts_to:
                    mermaid += f"    {module} ||--o{{ {target} : converts\n"
                
                creates = module_data.get('creates_directly', [])
                for target in creates:
                    mermaid += f"    {module} ||--o{{ {target} : creates\n"
                
                lookups = module_data.get('lookup_relationships', {})
                outgoing = lookups.get('outgoing', [])
                for lookup in outgoing[:5]:  # Limit for readability
                    # Extract target module from lookup field name
                    if isinstance(lookup, str):
                        mermaid += f"    {module} }}o--|| RELATED : \"{lookup}\"\n"
        
        return mermaid
    
    def generate_timeline(self) -> str:
        """Generate Gantt chart for time-based workflows"""
        if 'course_attendees' not in self.json_files:
            return "gantt\n    title No Timeline Data\n    dateFormat YYYY-MM-DD\n"
        
        data = self.json_files['course_attendees']
        mermaid = "gantt\n"
        mermaid += "    title Registration Communications Timeline\n"
        mermaid += "    dateFormat YYYY-MM-DD\n"
        mermaid += "    axisFormat %d days\n\n"
        
        if 'customer_journey' in data and 'Pre_Course_Communications' in data['customer_journey']:
            comm_stage = data['customer_journey']['Pre_Course_Communications']
            workflows = comm_stage.get('related_workflows', [])
            
            # Group by timing
            timeline_events = []
            for wf in workflows:
                timing = wf.get('timing', '')
                if 'days before' in timing:
                    days = timing.split(' days')[0]
                    if days.isdigit():
                        timeline_events.append((int(days), wf))
            
            timeline_events.sort(key=lambda x: -x[0])  # Sort by days descending
            
            base_date = 2024
            for days, wf in timeline_events:
                task_name = self.escape_label(wf.get('workflow_name', ''))[:30]
                # Create date relative to course day
                date_offset = 16 - days  # If course is day 16
                mermaid += f"    {task_name} :2024-01-{date_offset:02d}, 1d\n"
            
            mermaid += f"    Course Day :2024-01-16, 1d\n"
            mermaid += f"    Thank You SMS :2024-01-17, 1d\n"
        
        return mermaid
    
    def generate_integration_map(self) -> str:
        """Generate integration architecture diagram"""
        if 'overview' not in self.json_files:
            return "graph LR\n    NoData[No Integration Data]\n"
        
        data = self.json_files['overview']
        mermaid = "graph LR\n"
        mermaid += "    %% External System Integrations\n\n"
        
        mermaid += "    ZohoCRM[Zoho CRM Core]\n"
        mermaid += "    style ZohoCRM fill:#E3F2FD,stroke:#1976D2,stroke-width:3px\n\n"
        
        if 'integration_dependency_map' in data:
            integrations = data['integration_dependency_map']
            
            for system_name, system_data in integrations.items():
                system_id = self.sanitize_id(system_name)
                sync_dir = system_data.get('sync_direction', 'Outbound')
                modules = system_data.get('modules_synced', [])
                
                # Add integration node
                mermaid += f"    {system_id}[{system_name.replace('_', ' ')}]\n"
                mermaid += f"    style {system_id} fill:{COLORS['third_party']}\n"
                
                # Add connection
                if 'Bidirectional' in sync_dir:
                    mermaid += f"    ZohoCRM <-->|{', '.join(modules[:2])}| {system_id}\n"
                else:
                    mermaid += f"    ZohoCRM -->|{', '.join(modules[:2])}| {system_id}\n"
        
        return mermaid
    
    def generate_all_diagrams(self):
        """Generate all Mermaid diagram files"""
        diagrams = []
        
        # 1. Overview complete journey (swimlanes)
        if 'overview' in self.json_files:
            content = self.generate_swimlane_diagram()
            self.write_mermaid_file('overview-complete-journey.mmd', content)
            diagrams.append('overview-complete-journey.mmd')
        
        # 2-7. Individual module flowcharts
        module_mapping = {
            'leads': ('leads-workflow.mmd', 'Leads'),
            'deals': ('deals-workflow.mmd', 'Deals'),
            'courses': ('courses-workflow.mmd', 'Courses'),
            'course_attendees': ('course-attendees-journey.mmd', 'Course Attendees'),
            'invoices': ('invoices-payment-flow.mmd', 'Invoices'),
            'quotes': ('quotes-lifecycle.mmd', 'Quotes')
        }
        
        for key, (filename, title) in module_mapping.items():
            if key in self.json_files:
                content = self.generate_flowchart(self.json_files[key], title)
                self.write_mermaid_file(filename, content)
                diagrams.append(filename)
        
        # 8. Module relationships (ER diagram)
        er_content = self.generate_er_diagram()
        self.write_mermaid_file('module-relationships.mmd', er_content)
        diagrams.append('module-relationships.mmd')
        
        # 9. Integration architecture
        integration_content = self.generate_integration_map()
        self.write_mermaid_file('integration-architecture.mmd', integration_content)
        diagrams.append('integration-architecture.mmd')
        
        # 10. Timeline (Gantt chart)
        timeline_content = self.generate_timeline()
        self.write_mermaid_file('registration-timeline.mmd', timeline_content)
        diagrams.append('registration-timeline.mmd')
        
        return diagrams
    
    def write_mermaid_file(self, filename: str, content: str):
        """Write Mermaid content to file"""
        target_path = OUTPUT_DESTINATIONS.get(filename, self.output_dir / filename)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
        try:
            relative = target_path.relative_to(ROOT_DIR)
        except ValueError:
            relative = target_path
        print(f"✓ Generated {relative}")
    
    def generate_readme(self, diagrams: List[str]):
        """Generate README with usage instructions"""
        readme = """# Zoho CRM Workflow Mermaid Diagrams

## Generated Diagrams

"""
        for diagram in diagrams:
            title = diagram.replace('.mmd', '').replace('_', ' ').replace('-', ' ').title()
            readme += f"- `{diagram}` - {title}\n"
        
        readme += """

## How to View

### Option 1: Mermaid Live Editor (Easiest)
1. Go to https://mermaid.live
2. Copy contents of any .mmd file
3. Paste into editor
4. Diagram renders automatically

### Option 2: VSCode (Best for Editing)
1. Install extension: "Markdown Preview Mermaid Support"
2. Open any .mmd file
3. Right-click → "Open Preview"

### Option 3: GitHub (Version Control)
1. Commit .mmd files to repository
2. GitHub auto-renders Mermaid diagrams in .md files
3. Create markdown file with:
   ```markdown
   ```mermaid
   [paste .mmd content here]
   ```
   ```

## How to Export to PNG/SVG

### Install Mermaid CLI
```bash
npm install -g @mermaid-js/mermaid-cli
```

### Render Individual File
```bash
mmdc -i modules/overview/diagrams/overview-complete-journey.mmd -o modules/overview/diagrams/overview-complete-journey.png
mmdc -i modules/overview/diagrams/overview-complete-journey.mmd -o modules/overview/diagrams/overview-complete-journey.svg
```

### Batch Render (Use provided script)
```bash
chmod +x tools/kanban/render_mermaid.sh
./tools/kanban/render_mermaid.sh
```

## Color Coding Legend

- **Green (#90EE90)** - Automatic workflows (triggered by system)
- **Blue (#2196F3)** - Manual triggers (user sets field)
- **Orange (#FF9800)** - 3rd party integrations (Stripe, Xero, etc.)
- **Yellow (#FFEB3B)** - Human input required
- **Red (#F44336)** - Error/failure paths

## Diagram Descriptions

### 1. Overview Complete Journey
Master diagram showing all 11 customer journey stages across modules using swimlanes.

### 2. Leads Workflow
Lead entry points through to conversion (4 conversion paths).

### 3. Deals Workflow
Sales opportunity progression from creation to closed won/lost.

### 4. Courses Workflow
Course operations lifecycle (8 stages, 23 workflows).

### 5. Course Attendees Journey
Individual student journey from registration to certification.

### 6. Invoices Payment Flow
Invoice creation through to payment completion.

### 7. Quotes Lifecycle
Quote generation, sending, and acceptance/rejection.

### 8. Module Relationships
Entity-relationship diagram showing lookups between modules.

### 9. Integration Architecture
External system connections (Xero, WordPress, Stripe, etc.).

### 10. Registration Timeline
Gantt chart showing time-based SMS/email workflows.

## Troubleshooting

### Diagram Not Rendering
- Check for syntax errors (missing quotes, brackets)
- Ensure node IDs don't have special characters
- Try Mermaid Live Editor for better error messages

### Labels Cut Off
- Reduce label text length
- Use `<br/>` for line breaks
- Adjust diagram width in renderer settings

### Too Many Nodes
- Filter to show only key workflows
- Create separate diagrams for sub-processes
- Use subgraphs to organize related nodes

## Updating Diagrams

1. Update source JSON files as Zoho workflows change
2. Re-run: `python3 json_to_mermaid.py`
3. New .mmd files generated automatically
4. Re-render to PNG/SVG if needed

## Links

- Mermaid Documentation: https://mermaid.js.org/
- Mermaid Live Editor: https://mermaid.live
- Mermaid CLI: https://github.com/mermaid-js/mermaid-cli

---

**Generated:** {datetime.now().strftime('%Y-%m-%d')}  
**Source:** Customer journey JSONs (manual)  
**Generator:** json_to_mermaid.py
"""
        
        README_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(readme)
        print(f"✓ Updated {README_PATH.relative_to(ROOT_DIR)}")

def main():
    """Main execution function"""
    print("=" * 60)
    print("Zoho CRM Workflow → Mermaid Diagram Generator")
    print("=" * 60)
    print()
    
    generator = MermaidGenerator()
    
    # Load JSON files
    print("Loading JSON files...")
    count = generator.load_json_files()
    print(f"\n✓ Loaded {count} JSON files\n")
    
    # Generate diagrams
    print("Generating Mermaid diagrams...")
    diagrams = generator.generate_all_diagrams()
    print(f"\n✓ Generated {len(diagrams)} diagram files\n")
    
    # Generate README
    print("Generating documentation...")
    generator.generate_readme(diagrams)
    print()
    
    print("=" * 60)
    print("✓ Complete! Diagrams stored under modules/*/diagrams")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. View diagrams: https://mermaid.live")
    print("2. Or install VSCode extension: Markdown Preview Mermaid Support")
    print("3. To export PNG/SVG: npm install -g @mermaid-js/mermaid-cli")
    print()

if __name__ == '__main__':
    main()



