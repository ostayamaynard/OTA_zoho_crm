# Zoho CRM Workflow Mermaid Diagrams

## Generated Diagrams

- `overview-complete-journey.mmd` - Overview Complete Journey
- `leads-workflow.mmd` - Leads Workflow
- `deals-workflow.mmd` - Deals Workflow
- `courses-workflow.mmd` - Courses Workflow
- `course-attendees-journey.mmd` - Course Attendees Journey
- `invoices-payment-flow.mmd` - Invoices Payment Flow
- `quotes-lifecycle.mmd` - Quotes Lifecycle
- `module-relationships.mmd` - Module Relationships
- `integration-architecture.mmd` - Integration Architecture
- `registration-timeline.mmd` - Registration Timeline


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
