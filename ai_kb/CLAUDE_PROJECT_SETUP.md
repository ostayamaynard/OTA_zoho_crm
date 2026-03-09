# Setting Up a Claude Project for Zoho CRM Intelligence

This guide explains how to create a Claude Project using the AI Knowledge Base files to create an intelligent chatbot for your Zoho CRM system.

---

## What You'll Get

A Claude-powered assistant that can:
- ✅ Answer questions about your CRM structure (modules, fields, relationships)
- ✅ Show what changed between exports
- ✅ Perform impact analysis ("If I change field X, what breaks?")
- ✅ Guide CRM configuration changes with best practices
- ✅ Look up field specifications, picklist values, and workflow details
- ✅ Assess risk before making changes

---

## Prerequisites

- **Claude Pro or Team account** (required for Claude Projects)
- **5 AI KB files** from the `ai_kb/` folder:
  1. `SYSTEM_OVERVIEW.md` (~5 KB)
  2. `LATEST_CHANGES.md` (~6 KB)
  3. `WORKFLOW_DEPENDENCY_MAP.md` (~73 KB)
  4. `FIELD_REFERENCE.md` (~76 KB)
  5. `CHANGE_PLANNING_GUIDE.md` (~8 KB)

**Total upload size:** ~165-180 KB

---

## Step-by-Step Setup

### Step 1: Access Claude Projects

1. Go to [claude.ai](https://claude.ai)
2. Sign in with your Claude Pro or Team account
3. Click **"Projects"** in the left sidebar
4. Click **"+ Create Project"**

### Step 2: Create the Project

1. **Name:** `Zoho CRM Assistant` (or your preferred name)
2. **Description:** 
   ```
   AI assistant for Zoho CRM configuration, impact analysis, 
   and change planning. Has knowledge of all modules, fields, 
   workflows, and dependencies.
   ```
3. Click **"Create"**

### Step 3: Configure Project Settings

1. In your new project, click **"Project Settings"** (gear icon)
2. **Model Selection:** Choose **Claude Opus 4.5** (recommended for complex analysis)
   - Opus provides the most thorough impact analysis
   - Alternatively, use Sonnet 4 for faster responses
3. Save settings

### Step 4: Upload Knowledge Base Files

1. In the project, click **"Add Content"** or **"Project Knowledge"**
2. Click **"Upload Files"**
3. Select all 5 files from your `ai_kb/` folder:
   - `SYSTEM_OVERVIEW.md`
   - `LATEST_CHANGES.md`
   - `WORKFLOW_DEPENDENCY_MAP.md`
   - `FIELD_REFERENCE.md`
   - `CHANGE_PLANNING_GUIDE.md`
4. Wait for upload to complete
5. Verify all 5 files appear in the knowledge base

### Step 5: Add Custom Instructions

1. Click **"Custom Instructions"** (or "System Prompt")
2. Paste the following:

```
You are a Zoho CRM expert assistant with complete knowledge of this organization's CRM configuration. You have access to:

1. **SYSTEM_OVERVIEW.md** - Module catalogue with 66 modules, relationships, and statistics
2. **LATEST_CHANGES.md** - Recent configuration changes between exports
3. **WORKFLOW_DEPENDENCY_MAP.md** - 183 workflows with triggers, risk levels, and impact analysis
4. **FIELD_REFERENCE.md** - 1,500+ field specifications with picklist values
5. **CHANGE_PLANNING_GUIDE.md** - Best practices for CRM changes

## Your Role

Help users:
- Understand the CRM structure and module relationships
- Plan configuration changes safely
- Assess impact before making changes ("What will break if I...")
- Look up field specifications, picklist values, and workflows
- Review what changed in recent exports
- Follow best practices for CRM administration

## Response Guidelines

1. **Always cite your sources** - Reference the specific KB file and section
2. **Highlight risks** - Use 🔴 HIGH, 🟡 MEDIUM, 🟢 LOW indicators
3. **Be specific** - Quote field names, workflow IDs, and exact values
4. **Suggest verification** - Recommend testing in sandbox first
5. **Cross-reference** - Connect related information across KB files

## When answering questions about changes:

1. First check WORKFLOW_DEPENDENCY_MAP.md for workflows that use the field
2. Then check FIELD_REFERENCE.md for field specifications
3. Reference CHANGE_PLANNING_GUIDE.md for the recommended approach
4. Mention any recent changes from LATEST_CHANGES.md that might be relevant

## Key Module Information

Core modules (Tier 1): Leads, Contacts, Accounts, Deals, Courses, Registration_Records, Invoices, Quotes, Call_Analytics, Sales_Orders

The CRM instance is: https://crm.zoho.com.au/crm/org7003757385/

When referencing workflow IDs, you can construct URLs like:
https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/{workflow_id}
```

3. Click **"Save"**

### Step 6: Test the Assistant

Start a new chat in the project and try these test queries:

**Test 1 - Basic Query:**
```
What modules exist in our CRM and how many fields does each have?
```

**Test 2 - Impact Analysis:**
```
I want to change the Cold_Call_Tier field in Leads. What workflows use this field and what might break?
```

**Test 3 - Change Planning:**
```
I need to add a new required field to the Deals module. What's the safest approach?
```

**Test 4 - Recent Changes:**
```
What configuration changes were made in the most recent export?
```

---

## Example Conversations

### Scenario 1: Field Impact Analysis

**You:** I'm thinking of removing the "Lead Source" field from Leads. What would break?

**Claude:** Based on the WORKFLOW_DEPENDENCY_MAP.md, the Lead_Source field in Leads is used by:

🔴 **HIGH RISK** - 3 workflows depend on this field:
1. **Lead Assignment Rule** (ID: 52330000000427010) - Uses Lead_Source as trigger condition
2. **Lead Scoring Workflow** - Updates score based on Lead_Source value
3. **Campaign Attribution** - Records source for reporting

**Recommendation from CHANGE_PLANNING_GUIDE.md:**
- Before removing, audit all 3 workflows
- Check if Lead_Source is referenced in any reports
- Consider deprecating rather than removing (set to non-required, hide from layouts)
- Test in sandbox first

---

### Scenario 2: Understanding Workflows

**You:** Show me all workflows in the Courses module that have cross-module actions.

**Claude:** From WORKFLOW_DEPENDENCY_MAP.md, the Courses module has 37 workflows. Here are those with cross-module actions:

1. **Course Confirmation Email** (🟡 MEDIUM)
   - Triggers: On Course creation
   - Cross-module: Creates Task in Tasks module
   - Creates notification in Registration_Records

2. **Trainer Assignment** (🔴 HIGH)
   - Triggers: When Course_Trainer field changes
   - Cross-module: Updates Contact record
   - Sends email notification

[... continues with specific details ...]

---

### Scenario 3: Change Planning

**You:** We need to add a new picklist value "Enterprise" to the Account_Type field. What's the process?

**Claude:** Based on CHANGE_PLANNING_GUIDE.md, here's the safe process:

**Pre-Change Checklist:**
1. ✅ Check FIELD_REFERENCE.md - Account_Type current values: [Small Business, Mid-Market, Corporate]
2. ✅ Check WORKFLOW_DEPENDENCY_MAP.md - 2 workflows reference Account_Type
3. ✅ No recent changes to this field (per LATEST_CHANGES.md)

**Recommended Steps:**
1. Add "Enterprise" to picklist in sandbox
2. Test the 2 dependent workflows still function
3. Check any reports filtering by Account_Type
4. Deploy to production during low-usage hours
5. Document the change for next export

**Risk Assessment:** 🟢 LOW - Adding a value is low risk; existing workflows won't break

---

## Tips for Effective Use

### Best Practices

1. **Be specific** - Instead of "tell me about Leads", ask "what lookup fields in Leads point to other modules?"

2. **Ask for impact analysis** - Always include "what might break" or "what's the impact" in change-related questions

3. **Request citations** - Ask Claude to "cite the specific workflow IDs" or "show me the exact field names"

4. **Follow up** - Claude remembers context, so you can ask follow-up questions

### Power User Queries

```
"Show me all HIGH risk workflows across all modules"

"What fields in Deals are used by more than 3 workflows?"

"Compare the Registration_Records module structure to Courses - what fields link them?"

"I want to disable workflow 52330000000427010 - walk me through the impact analysis"

"What picklist fields have changed in the last export?"
```

### Queries to Avoid

- Asking about actual customer data (the KB only contains configuration, not records)
- Real-time CRM status (the KB is a snapshot from the export date)
- Creating or modifying CRM configuration (Claude can only advise, not execute)

---

## Keeping the Knowledge Base Updated

### When to Update

Update the AI KB files when:
1. New Zoho export is processed
2. Major CRM configuration changes are made
3. Monthly (recommended schedule)

### How to Update

1. Run the pipeline to regenerate AI KB files:
   ```bash
   python3 tools/update_pipeline.py --apply
   ```

2. In Claude Project settings, remove old files

3. Upload the 5 new files from `ai_kb/`

4. Verify the updated timestamps in each file

### Version Tracking

Each AI KB file includes metadata:
- Generation date
- Source export date
- File size

Check these match your latest export to ensure the KB is current.

---

## Troubleshooting

### "Claude doesn't seem to know about [specific field/workflow]"

**Cause:** The KB files may be outdated or not fully uploaded
**Solution:**
1. Check upload status in Project Knowledge
2. Verify all 5 files are present
3. Re-upload if necessary
4. Ask Claude: "What's the source date for your Zoho CRM knowledge?"

### "Responses are slow"

**Cause:** Large KB files require processing
**Solution:**
1. Opus 4.5 is more thorough but slower
2. Switch to Sonnet 4 for faster responses
3. Ask more specific questions to reduce search scope

### "Impact analysis seems incomplete"

**Cause:** Complex dependencies may span multiple files
**Solution:**
1. Ask Claude to "check all KB files for references to [field/workflow]"
2. Request a "comprehensive impact analysis including all cross-references"
3. Follow up with specific module checks

---

## Advanced: API Access

If you have Claude API access, you can also use these KB files programmatically:

```python
import anthropic

client = anthropic.Anthropic()

# Load KB files as system context
with open('ai_kb/WORKFLOW_DEPENDENCY_MAP.md') as f:
    workflow_kb = f.read()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=8096,
    system=f"""You are a Zoho CRM expert. Use this knowledge base:
    
{workflow_kb}

Answer questions about CRM workflows and dependencies.""",
    messages=[
        {"role": "user", "content": "What workflows in Leads are HIGH risk?"}
    ]
)
```

---

## Quick Reference Card

| Task | Ask Claude |
|------|------------|
| Module overview | "Describe the [module] module" |
| Field lookup | "What are the picklist values for [field] in [module]?" |
| Impact analysis | "What breaks if I change [field] in [module]?" |
| Workflow details | "Explain workflow [ID] and its dependencies" |
| Change planning | "How do I safely [add/remove/modify] [field/workflow]?" |
| Recent changes | "What changed in the latest export?" |
| Risk assessment | "What's the risk level for changing [field/workflow]?" |
| Cross-module | "How does [module A] connect to [module B]?" |

---

## Support

**For KB generation issues:**
- See `tools/README.md` for generator documentation
- Run `python3 tools/generators/generate_ai_kb.py --help`

**For Claude Projects issues:**
- Check [Claude documentation](https://docs.anthropic.com)
- Verify account has Projects feature enabled

**For CRM-specific questions:**
- The assistant itself is the best resource!
- Ask: "How should I approach [your question]?"

---

*Guide Version: 1.0*  
*Compatible with: Claude Opus 4.5, Claude Sonnet 4*  
*AI KB Version: 2026-01-08*
