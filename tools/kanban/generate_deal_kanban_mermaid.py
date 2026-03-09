#!/usr/bin/env python3
"""
Deal Kanban Mermaid Generator
Creates a Kanban-style flowchart for Deal stages with clickable workflow URLs

Usage: python3 generate_deal_kanban_mermaid.py
Output: deal_kanban_detailed.mmd with clickable workflow links
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT_DIR / 'modules/deals/data/deal-stages-kanban.json'
DIAGRAM_DIR = ROOT_DIR / 'modules/deals/diagrams'
DOCS_DIR = ROOT_DIR / 'modules/deals/docs'

def generate_deal_kanban_mermaid():
    """Generate Deal Kanban diagram with clickable workflows"""
    
    # Load the Deal Kanban JSON
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    mermaid = """graph TB
    %% Deal Stages Kanban Board
    %% Click on workflow boxes to open in Zoho CRM
    
    classDef stageQual fill:#FFF9C4,stroke:#FFC107,stroke-width:3px
    classDef stageNeeds fill:#BBDEFB,stroke:#2196F3,stroke-width:3px
    classDef stageQuote fill:#E1BEE7,stroke:#9C27B0,stroke-width:3px
    classDef stageNegot fill:#FFE0B2,stroke:#FF9800,stroke-width:3px
    classDef stageWon fill:#C8E6C9,stroke:#4CAF50,stroke-width:3px
    classDef stageLost fill:#FFCDD2,stroke:#F44336,stroke-width:3px
    classDef autoWF fill:#90EE90,stroke:#2E7D32,stroke-width:2px
    classDef manualWF fill:#2196F3,stroke:#0D47A1,stroke-width:2px
    classDef timeWF fill:#FF9800,stroke:#E65100,stroke-width:2px
    
"""
    
    # Extract stages
    stages = data['kanban_stages']
    
    # Stage 1: Qualification
    mermaid += """
    %% ========== QUALIFICATION STAGE ==========
    Stage1["🔍 QUALIFICATION<br/>Verify deal details, select course"]
    class Stage1 stageQual
    
"""
    
    # Add workflows for Qualification
    qual = stages['Qualification']
    for idx, wf in enumerate(qual['workflows_on_enter'][:3]):
        wf_id = f"Q_WF{idx+1}"
        wf_name = wf['workflow_name'].replace('"', "'")
        wf_url = wf['url']
        zoho_id = wf['workflow_id']
        
        mermaid += f'    {wf_id}["{wf_name}<br/>ID: {zoho_id}<br/>🔗 Click to view"]\n'
        mermaid += f'    click {wf_id} "{wf_url}" _blank\n'
        mermaid += f'    class {wf_id} autoWF\n'
        mermaid += f'    Stage1 -.->|fires on create| {wf_id}\n'
    
    # Human actions
    mermaid += '\n    Q_Human["👤 HUMAN ACTIONS:<br/>• Verify deal details<br/>• Select course (Courseaa)<br/>• Set attendee count"]\n'
    mermaid += '    Stage1 --> Q_Human\n\n'
    
    # Stage 2: Needs Analysis
    mermaid += """    %% ========== NEEDS ANALYSIS STAGE ==========
    Q_Human --> Stage2["📋 NEEDS ANALYSIS<br/>Assess requirements"]
    class Stage2 stageNeeds
    
"""
    
    needs = stages['Needs_Analysis']
    for idx, wf in enumerate(needs['workflows_available']):
        wf_id = f"N_WF{idx+1}"
        wf_name = wf['workflow_name'].replace('"', "'")
        wf_url = wf['url']
        zoho_id = wf['workflow_id']
        trigger_field = wf.get('condition_fields', [''])[0]
        
        mermaid += f'    {wf_id}["{wf_name}<br/>ID: {zoho_id}<br/>Trigger: {trigger_field} = true<br/>🔗 Click to view"]\n'
        mermaid += f'    click {wf_id} "{wf_url}" _blank\n'
        mermaid += f'    class {wf_id} manualWF\n'
        mermaid += f'    Stage2 -.->|manual trigger| {wf_id}\n'
    
    mermaid += '\n    N_Human["👤 HUMAN ACTIONS:<br/>• Assign Training Coordinator<br/>• Set course start date<br/>• Request attendee details (optional)"]\n'
    mermaid += '    Stage2 --> N_Human\n\n'
    
    # Stage 3: Ready to Quote
    mermaid += """    %% ========== READY TO QUOTE STAGE ==========
    N_Human --> Stage3["📝 READY TO QUOTE<br/>⚠️ Quote AUTO-CREATED"]
    class Stage3 stageQuote
    
"""
    
    quote = stages['Ready_to_Quote']
    for idx, wf in enumerate(quote['workflows_on_enter']):
        wf_id = f"R_WF{idx+1}"
        wf_name = wf['workflow_name'].replace('"', "'")
        wf_url = wf['url']
        zoho_id = wf['workflow_id']
        
        mermaid += f'    {wf_id}["⚡ {wf_name}<br/>ID: {zoho_id}<br/>CREATES: Quote record<br/>🔗 Click to view"]\n'
        mermaid += f'    click {wf_id} "{wf_url}" _blank\n'
        mermaid += f'    class {wf_id} autoWF\n'
        mermaid += f'    Stage3 ==>|AUTO-FIRES| {wf_id}\n'
    
    mermaid += '\n    R_Human["👤 HUMAN ACTIONS:<br/>• Review auto-generated Quote<br/>• Adjust pricing in Quotes module<br/>• Send quote to client"]\n'
    mermaid += '    Stage3 --> R_Human\n\n'
    
    # Stage 4: Negotiation
    mermaid += """    %% ========== NEGOTIATION/REVIEW STAGE ==========
    R_Human --> Stage4["💬 NEGOTIATION/REVIEW<br/>Awaiting PO & decision"]
    class Stage4 stageNegot
    
"""
    
    negot = stages['Negotiation_Review']
    for idx, wf in enumerate(negot['time_based_workflows'][:4]):
        wf_id = f"NEG_WF{idx+1}"
        wf_name = wf['workflow_name'].replace('"', "'")
        wf_url = wf['url']
        zoho_id = wf['workflow_id']
        timing = wf.get('timing', 'scheduled')
        
        mermaid += f'    {wf_id}["⏰ {wf_name}<br/>ID: {zoho_id}<br/>Timing: {timing}<br/>🔗 Click to view"]\n'
        mermaid += f'    click {wf_id} "{wf_url}" _blank\n'
        mermaid += f'    class {wf_id} timeWF\n'
        mermaid += f'    Stage4 -.->|time-based| {wf_id}\n'
    
    mermaid += '\n    NEG_Human["👤 HUMAN ACTIONS:<br/>• Chase purchase order<br/>• Negotiate terms<br/>• Enter PO# when received"]\n'
    mermaid += '    Stage4 --> NEG_Human\n\n'
    
    # Decision point
    mermaid += """    %% ========== DECISION POINT ==========
    NEG_Human --> Decision{Quote Accepted?}
    
"""
    
    # Stage 5: Closed Won
    mermaid += """    %% ========== CLOSED WON STAGE ==========
    Decision -->|Yes + PO received| Stage5["✅ CLOSED WON<br/>Deal won, process payment"]
    class Stage5 stageWon
    
"""
    
    won = stages['Closed_Won']
    for idx, wf in enumerate(won['workflows_on_enter']):
        wf_id = f"W_WF{idx+1}"
        wf_name = wf['workflow_name'].replace('"', "'")
        wf_url = wf['url']
        zoho_id = wf['workflow_id']
        action = wf.get('action', '')[:60]
        
        mermaid += f'    {wf_id}["{wf_name}<br/>ID: {zoho_id}<br/>{action}<br/>🔗 Click to view"]\n'
        mermaid += f'    click {wf_id} "{wf_url}" _blank\n'
        mermaid += f'    class {wf_id} autoWF\n'
        mermaid += f'    Stage5 ==>|fires| {wf_id}\n'
    
    mermaid += '\n    W_Human["👤 HUMAN ACTIONS:<br/>• Enter PO number<br/>• Verify invoice created<br/>• Monitor payment"]\n'
    mermaid += '    Stage5 --> W_Human\n\n'
    
    # Stage 6: Closed Lost
    mermaid += """    %% ========== CLOSED LOST STAGE ==========
    Decision -->|No / Declined| Stage6["❌ CLOSED LOST<br/>Deal lost"]
    class Stage6 stageLost
    
    L_Human["👤 HUMAN ACTIONS:<br/>• Enter Loss_Reason (MANDATORY)<br/>• Update Quote to Declined<br/>• Cancel any registrations"]
    Stage6 --> L_Human
    
"""
    
    # Add legend
    mermaid += """
    %% ========== LEGEND ==========
    subgraph Legend
        L1[🟢 Automatic Workflow<br/>Fires without user action]
        L2[🔵 Manual Workflow<br/>User sets field to trigger]
        L3[🟠 Time-Based Workflow<br/>Fires on schedule]
        L4[👤 Human Actions Required]
        class L1 autoWF
        class L2 manualWF
        class L3 timeWF
    end
"""
    
    return mermaid

def generate_deal_kanban_simple():
    """Generate simplified Deal Kanban for quick overview"""
    
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    stages = data['kanban_stages']
    
    mermaid = """graph LR
    %% Simplified Deal Kanban Board
    
    classDef qual fill:#FFF9C4,stroke:#FFC107,stroke-width:4px
    classDef needs fill:#BBDEFB,stroke:#2196F3,stroke-width:4px
    classDef quote fill:#E1BEE7,stroke:#9C27B0,stroke-width:4px
    classDef negot fill:#FFE0B2,stroke:#FF9800,stroke-width:4px
    classDef won fill:#C8E6C9,stroke:#4CAF50,stroke-width:4px
    classDef lost fill:#FFCDD2,stroke:#F44336,stroke-width:4px
    
    S1["🔍<br/>QUALIFICATION<br/>━━━━━━━<br/>5 auto workflows<br/>Verify details"]
    S2["📋<br/>NEEDS ANALYSIS<br/>━━━━━━━<br/>2 manual workflows<br/>Assess requirements"]
    S3["📝<br/>READY TO QUOTE<br/>━━━━━━━<br/>⚡ Quote auto-created<br/>Review & send"]
    S4["💬<br/>NEGOTIATION<br/>━━━━━━━<br/>4 PO reminder workflows<br/>Chase PO"]
    S5["✅<br/>CLOSED WON<br/>━━━━━━━<br/>3 auto workflows<br/>Process payment"]
    S6["❌<br/>CLOSED LOST<br/>━━━━━━━<br/>Document loss"]
    
    S1 --> S2 --> S3 --> S4
    S4 -->|PO received| S5
    S4 -->|Declined| S6
    
    class S1 qual
    class S2 needs
    class S3 quote
    class S4 negot
    class S5 won
    class S6 lost
"""
    
    return mermaid

def generate_workflow_urls_reference():
    """Generate a reference document with all workflow URLs"""
    
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    doc = """# Deal Workflow URLs Reference

Quick access to all Deal-related workflows in Zoho CRM

## By Stage

"""
    
    stages = data['kanban_stages']
    
    for stage_name, stage_data in stages.items():
        doc += f"\n### {stage_name.replace('_', ' ').title()}\n\n"
        doc += f"**Stage Order:** {stage_data.get('stage_order', 'N/A')}  \n"
        doc += f"**Description:** {stage_data.get('description', 'N/A')}  \n\n"
        
        # Workflows on enter
        if 'workflows_on_enter' in stage_data and stage_data['workflows_on_enter']:
            doc += "**Workflows (fire automatically on entry):**\n\n"
            for wf in stage_data['workflows_on_enter']:
                doc += f"- **{wf['workflow_name']}**\n"
                doc += f"  - ID: `{wf['workflow_id']}`\n"
                doc += f"  - Trigger: {wf.get('trigger', 'N/A')}\n"
                doc += f"  - Action: {wf.get('action', 'N/A')}\n"
                doc += f"  - 🔗 [Open in Zoho]({wf['url']})\n\n"
        
        # Time-based workflows
        if 'time_based_workflows' in stage_data:
            doc += "**Time-Based Workflows:**\n\n"
            for wf in stage_data['time_based_workflows']:
                doc += f"- **{wf['workflow_name']}**\n"
                doc += f"  - ID: `{wf['workflow_id']}`\n"
                doc += f"  - Timing: {wf.get('timing', 'N/A')}\n"
                doc += f"  - Action: {wf.get('action', 'N/A')}\n"
                doc += f"  - 🔗 [Open in Zoho]({wf['url']})\n\n"
        
        # Manual workflows
        if 'workflows_available' in stage_data:
            doc += "**Manual Workflows (user triggers):**\n\n"
            for wf in stage_data['workflows_available']:
                doc += f"- **{wf['workflow_name']}**\n"
                doc += f"  - ID: `{wf['workflow_id']}`\n"
                doc += f"  - How to trigger: {wf.get('how_to_trigger', 'N/A')}\n"
                doc += f"  - Action: {wf.get('action', 'N/A')}\n"
                doc += f"  - 🔗 [Open in Zoho]({wf['url']})\n\n"
        
        # Field updates
        if 'workflows_on_field_update' in stage_data:
            doc += "**Field Update Workflows:**\n\n"
            for wf in stage_data['workflows_on_field_update']:
                doc += f"- **{wf['workflow_name']}**\n"
                doc += f"  - ID: `{wf['workflow_id']}`\n"
                doc += f"  - Triggers when: {', '.join(wf.get('condition_fields', []))} changes\n"
                doc += f"  - Action: {wf.get('action', 'N/A')}\n"
                doc += f"  - 🔗 [Open in Zoho]({wf['url']})\n\n"
        
        # Human actions
        if 'human_actions_required' in stage_data:
            doc += "**Human Actions Required:**\n\n"
            for action in stage_data['human_actions_required']:
                doc += f"- {action['action']}\n"
                if 'fields' in action:
                    doc += f"  - Fields: {', '.join(action['fields'])}\n"
                if 'triggers_workflow' in action:
                    doc += f"  - ⚡ Triggers: {action['triggers_workflow']}\n"
                doc += f"  - {action.get('description', '')}\n\n"
        
        doc += "---\n"
    
    # Add quick reference
    doc += """
## Quick Reference - All Workflow URLs

| Workflow Name | ID | Stage | Type | URL |
|--------------|----|----|------|-----|
"""
    
    for stage_name, stage_data in stages.items():
        for wf_list_key in ['workflows_on_enter', 'workflows_available', 'time_based_workflows', 'workflows_on_field_update']:
            if wf_list_key in stage_data:
                for wf in stage_data[wf_list_key]:
                    name = wf['workflow_name']
                    wf_id = wf['workflow_id']
                    trigger = wf.get('trigger', 'auto')
                    url = wf['url']
                    doc += f"| {name} | `{wf_id}` | {stage_name} | {trigger} | [Open]({url}) |\n"
    
    return doc

def main():
    print("=" * 60)
    print("Deal Kanban Mermaid Generator")
    print("=" * 60)
    print()
    
    # Generate detailed kanban
    print("Generating detailed Deal Kanban diagram...")
    kanban_mermaid = generate_deal_kanban_mermaid()
    
    DIAGRAM_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(DIAGRAM_DIR / 'deal-kanban-detailed.mmd', 'w', encoding='utf-8') as f:
        f.write(kanban_mermaid)
    print("✓ Created deal-kanban-detailed.mmd")
    
    # Generate simple kanban
    print("Generating simplified Deal Kanban diagram...")
    simple_mermaid = generate_deal_kanban_simple()
    
    with open(DIAGRAM_DIR / 'deal-kanban-simple.mmd', 'w', encoding='utf-8') as f:
        f.write(simple_mermaid)
    print("✓ Created deal-kanban-simple.mmd")
    
    # Generate URL reference doc
    print("Generating workflow URL reference...")
    url_doc = generate_workflow_urls_reference()
    
    with open(DOCS_DIR / 'deal-workflow-urls.md', 'w', encoding='utf-8') as f:
        f.write(url_doc)
    print("✓ Created deal-workflow-urls.md")
    
    print()
    print("=" * 60)
    print("✓ Complete!")
    print("=" * 60)
    print()
    print("Files created:")
    rel_diagram = Path('modules/deals/diagrams')
    rel_docs = Path('modules/deals/docs')
    print(f"1. {rel_diagram / 'deal-kanban-detailed.mmd'} - Full diagram with clickable URLs")
    print(f"2. {rel_diagram / 'deal-kanban-simple.mmd'} - Quick overview")
    print(f"3. {rel_docs / 'deal-workflow-urls.md'} - Reference doc with all URLs")
    print()
    print("⚠️ IMPORTANT: Clickable links work in:")
    print("   - Mermaid Live Editor (https://mermaid.live)")
    print("   - GitHub (when embedded in markdown)")
    print("   - Some documentation tools")
    print()
    print("   Links may NOT work in:")
    print("   - VSCode preview (static rendering)")
    print("   - PNG/SVG exports (links removed)")
    print()

if __name__ == '__main__':
    main()



