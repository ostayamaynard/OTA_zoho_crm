# Deal Kanban Workflow - Usage Guide

**Created:** 2025-11-13
**Last Updated:** 18/11/2025
**Purpose:** Visual Kanban board for Deal stages with clickable workflow URLs

---

## Changelog

### 18/11/2025
- **Added clickable Zoho CRM workflow links** to both diagram files using proper Mermaid `click` directive syntax
  - `deal-kanban-attendee.mmd` - 5 workflows with direct links
  - `deal-kanban-commercial.mmd` - 14 workflows with direct links
- **Unified stage node styling** - All stage nodes now have black dashed 3px stroke outlines for consistency
- **Added Legend subgraphs** to both diagrams showing node types (Deal Stage, Workflow Rule, Module, etc.)
- **Created `deal-pipeline-management-sop.md`** - Full SOP documentation for pipeline management
- **Created `sop-workflow-accuracy-report.md`** - Accuracy analysis comparing SOP to actual workflows
  - Identified stage name mismatches (SOP: New/Qualified vs CRM: Qualification/Negotiation_Review)
  - Found 15 of 19 workflows (79%) undocumented in SOP
  - Listed missing automations (Quote Sent tracking, Course Booked stage, etc.)

---

## Module Structure Reference

Use this structure as a template when building other modules (e.g., Leads):

```
modules/deals/
├── data/
│   └── deal-stages-kanban.json       # Stage config with workflow IDs, colors, triggers
├── diagrams/
│   ├── deal-kanban-commercial.mmd    # Commercial workflows (14 WFs) with clickable links
│   ├── deal-kanban-attendee.mmd      # Attendee workflows (5 WFs) with clickable links
│   ├── deal-kanban-detailed.mmd      # Full detailed diagram
│   └── deal-kanban-simple.mmd        # Quick overview diagram
└── docs/
    ├── deal-kanban-usage.md          # This usage guide
    ├── deal-workflow-urls.md         # Workflow URL reference
    ├── deal-pipeline-management-sop.md # SOP documentation
    └── sop-workflow-accuracy-report.md # Accuracy analysis
```

### Key Patterns for New Modules

1. **Mermaid Diagram Conventions:**
   - Use `flowchart TD` for top-down flow
   - Stage nodes: `["emoji Stage Name"]` with `classDef` for colors
   - Workflow nodes: `["Workflow Name<br/>ID: xxx<br/>Action: description"]`
   - Add `click` directives for Zoho CRM links: `click NodeID "url" "tooltip"`
   - Include Legend subgraph for node type reference

2. **Click Directive Syntax (Correct Mermaid format):**
   ```mermaid
   %% Node definition
   WF_Example["Workflow Name<br/>ID: 12345<br/>Action: Does something"]

   %% Click directive (separate from node)
   click WF_Example "https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/12345" "Open in Zoho CRM"
   ```

3. **Stage Styling Pattern:**
   ```mermaid
   classDef stageName fill:#COLOR,stroke:#000,stroke-width:3px,stroke-dasharray:5 5
   ```

4. **URL Pattern for Zoho Workflows:**
   ```
   https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/{WORKFLOW_ID}
   ```

5. **SOP to Workflow Comparison:**
   - Always create accuracy report comparing documentation to actual system
   - Track stage name mismatches, undocumented automations, and gaps

---

## 🎯 What You Now Have

### 1. **deal-stages-kanban.json** (20 KB)
Complete Deal stage mapping with:
- ✅ 6 Kanban stages (Qualification → Closed Won/Lost)
- ✅ 13 workflows documented with Zoho URLs
- ✅ Color codes for each stage
- ✅ Human action checklists
- ✅ Workflow trigger conditions
- ✅ Exit criteria for each stage

### 2. **deal-kanban-detailed.mmd** (7 KB)
Full Mermaid diagram with:
- ✅ All 6 stages shown as connected boxes
- ✅ Workflows displayed with **clickable URLs** 🔗
- ✅ Color-coded by trigger type (automatic/manual/time-based)
- ✅ Human action boxes at each stage
- ✅ Decision diamonds for win/loss paths

### 3. **deal-kanban-simple.mmd** (1.2 KB)
Quick overview showing:
- ✅ 6 stages as Kanban columns
- ✅ Workflow counts per stage
- ✅ Color-coded stage boxes
- ✅ Flow arrows showing progression

### 4. **deal-workflow-urls.md** (12 KB)
Reference document with:
- ✅ All workflows organized by stage
- ✅ Clickable URLs to open in Zoho
- ✅ Trigger conditions
- ✅ Human action checklists
- ✅ Quick reference table

---

## 🚀 How to Use - Clickable Workflow Diagrams

### **Option 1: Mermaid Live Editor (BEST for clickable URLs)**

1. **Go to:** https://mermaid.live

2. **Copy diagram:**
   ```bash
   cat modules/deals/diagrams/deal-kanban-detailed.mmd
   ```

3. **Paste into editor**

4. **Click workflow boxes** - Opens Zoho CRM workflow directly! 🔗

**Example:**
- Click "Update Deal ID" box → Opens workflow 52330000002444572 in your Zoho instance
- Click "Create Quote" box → Opens workflow 52330000002460308
- Each workflow box has a 🔗 icon indicating it's clickable

### **Option 2: GitHub Markdown (For team documentation)**

1. **Create markdown file:**
   ```markdown
   # Deal Workflow Kanban
   
   ```mermaid
   [paste deal-kanban-detailed.mmd content here]
   ```
   ```

2. **Commit to GitHub repository**

3. **View in GitHub** - Diagram renders with clickable links!

### **Option 3: Interactive HTML (For presentations)**

Coming soon - Can create standalone HTML with embedded Mermaid + tooltips.

---

## 📋 Stage-by-Stage Breakdown

### **Stage 1: Qualification** 🔍
**Color:** Light Red/Pink (#ffc6c6)  
**Duration:** 1-3 days  
**Workflow Count:** 5 automatic

**What Happens:**
- ✅ 5 workflows fire automatically when Deal created
- ✅ Deal ID assigned
- ✅ Deal Name formatted
- ✅ Amount calculated
- ✅ Course details populated if from website

**Human Actions:**
1. Verify all deal details
2. Select Course (Courseaa lookup field)
3. Set Number_of_Attendees
4. Change Stage to "Negotiation/Review" when ready

**Workflow URLs:**
- [Update Deal ID](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002444572)
- [Deal Naming Convention](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967279)
- [Update Amount on create](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000003995130)

---

### **Stage 2: Negotiation/Review** 💬
**Color:** Light Blue (#ced9ff)  
**Duration:** 7-30 days  
**Workflow Count:** 5 (2 manual + 4 time-based)

**What Happens:**
- 🔵 Manual workflows available (field-based triggers - work in any stage):
  - Set Request_Attendees = TRUE → Emails Training Coordinator
  - Set Create_Follow_up_Task = TRUE → Creates Team Task
- ⏰ 4 reminder workflows fire on schedule based on Course_Start_Date:
  - 28 days before → Team Task created
  - 14 days before → Team Task created
  - 5 days before → Team Task created
  - 1 day before → Urgent Team Task created

**Human Actions:**
1. Chase purchase order from client
2. **Optional:** Set Request_Attendees = TRUE to email coordinator
3. **Optional:** Set Create_Follow_up_Task = TRUE to create task
4. Set Course_Start_Date (enables PO reminders)
5. **When PO received:**
   - Enter Purchase_Order_Number directly on Deal
   - Or enter Expected_PO_Date and PO_Number in Quotes module
6. **When client accepts:**
   - In Quotes module: Set Quote_Stage = "Accepted"
   - This will AUTO-UPDATE Deal to Closed Won
7. **If client declines:**
   - Change Stage to "Closed Lost"

**Manual Workflow Triggers (field-based - work in any stage):**
- [Email to Coordinator](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002967852) - Set Request_Attendees = TRUE
- [Create Team Task](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460147) - Set Create_Follow_up_Task = TRUE

**Time-Based Workflow URLs:**
- [28 days before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311)
- [14 days before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269)
- [5 days before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085891)
- [1 day before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638411)

---

### **Stage 3: Ready to Quote** 📝
**Color:** Yellow (#ffda62)  
**Duration:** 1-2 days  
**Workflow Count:** 1 automatic (CRITICAL)

**⚠️ IMPORTANT:** Quote is **AUTO-CREATED** when you change Stage to "Ready to Quote"

**What Happens:**
- ⚡ [Create Quote workflow](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308) fires immediately
- 📄 New Quote record created in Quotes module
- 🔗 Quote linked to this Deal
- 💰 Quote populated with Deal details and pricing

**Human Actions:**
1. **Go to Quotes module** - Find new quote linked to this Deal
2. Review auto-generated Quoted_Items
3. Adjust pricing if needed
4. Set Valid_Till date
5. In Quotes module: Set Send_Quote_as_EMAIL = TRUE to send to client
6. Change Stage to "Negotiation/Review" or "Awaiting ZipPay Confirmation" when quote sent

**Workflow URL:**
- [Create Quote - Stage Update](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308) ⚡ **AUTO-FIRES**

---

### **Stage 4: Awaiting ZipPay Confirmation** 💳
**Color:** Purple (#af38fa)  
**Duration:** 1-3 days  
**Workflow Count:** 0

**What Happens:**
- 💳 Deal awaiting ZipPay payment confirmation
- No automated workflows

**Human Actions:**
1. Monitor ZipPay payment status
2. Set Course_Start_Date if known
3. **When payment confirmed:**
   - Change Stage to "Awaiting Purchase Order" or "Closed Won"
4. **If payment declined:**
   - Change Stage to "Closed Lost"
   - Enter Loss_Reason

---

### **Stage 5: Awaiting Purchase Order** 📋
**Color:** Light Grey (#dbdbdb)  
**Duration:** 7-14 days  
**Workflow Count:** 0

**What Happens:**
- 📋 Quote accepted, awaiting PO from client
- No automated workflows

**Human Actions:**
1. Chase purchase order from client
2. **When PO received:**
   - Enter Purchase_Order_Number (triggers 2 workflows)
   - Or change Stage to "Closed Won"
3. **If PO not received:**
   - Change Stage to "Closed Lost"
   - Enter Loss_Reason

---

### **Stage 6: Awaiting Invoice Payment** 💰
**Color:** Grey (#acacac)  
**Duration:** 7-30 days  
**Workflow Count:** 0

**What Happens:**
- 💰 Invoice sent, awaiting payment
- No automated workflows

**Human Actions:**
1. Monitor invoice payment status (Invoices module)
2. Follow up on payment if overdue
3. **When payment received:**
   - Change Stage to "Closed Won"
4. **If payment not received:**
   - Change Stage to "Closed Lost"
   - Enter Loss_Reason

---

### **Stage 7: Unused** ⏸️
**Color:** Light Red/Pink (#ffc6c6)  
**Duration:** Variable  
**Workflow Count:** 0

**What Happens:**
- ⏸️ Deal temporarily on hold or set aside
- No automated workflows

**Human Actions:**
1. Document reason for hold in Follow_Up_Notes
2. Set Follow_up_date (triggers "Follow up future deals" workflow)
3. **When deal reactivated:**
   - Change Stage to appropriate active stage

---

### **Stage 8: Closed Won** ✅
**Color:** Green (#25b52a)  
**Duration:** Ongoing  
**Workflow Count:** 3 automatic

**What Happens:**
- ✅ When PO Number entered → 2 workflows fire:
  - Updates Deal status
  - Updates ALL Registration_Records to Status = Confirmed
- ✅ When Stage set to Closed Won → 1 workflow fires:
  - Updates attendee records
  - 5 days before → Team Task created
  - 1 day before → Urgent Team Task created

**Human Actions:**
1. Chase purchase order from client
2. **When PO received:**
   - Go to Quotes module
   - Enter Expected_PO_Date and PO_Number
   - Or enter Purchase_Order_Number directly on Deal
3. **When client accepts:**
   - In Quotes module: Set Quote_Stage = "Accepted"
   - This will AUTO-UPDATE Deal to Closed Won
4. **If client declines:**
   - Change Stage to "Closed Lost"

**Workflow URLs:**
- [28 days before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311)
- [14 days before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269)
- [5 days before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085891)
- [1 day before reminder](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638411)

---


**What Happens:**
- ✅ When PO Number entered → 2 workflows fire:
  - Updates Deal status
  - Updates ALL Registration_Records to Status = Confirmed
- ✅ When Stage set to Closed Won → 1 workflow fires:
  - Updates attendee records

**Human Actions:**
1. **Enter Purchase_Order_Number** (triggers 2 workflows)
2. Verify Invoice was created (should be auto-created from Quote)
3. Monitor Invoice payment status
4. Verify all Registration_Records show Status = Confirmed

**Workflow URLs:**
- [Purchase Order Received](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460283) - Fires when PO# entered
- [Update Registration records](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006993545) - Updates attendees
- [On stage Update related Attendees](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000004335567) - Stage change trigger

---

### **Stage 9: Closed Lost** ❌
**Color:** Red (#eb4d4d)  
**Duration:** N/A (terminal)  
**Workflow Count:** 0

**Human Actions:**
1. **Enter Loss_Reason** (MANDATORY field)
2. In Quotes module: Set Quote_Stage = "Declined"
3. If registrations created: Cancel them (Status = Cancelled)

**No automated workflows** - Manual stage only

---

## 🎨 Visual Legend

### Stage Colors
- 🔴 **Qualification** (#ffc6c6) - Initial setup
- 🔵 **Negotiation/Review** (#ced9ff) - Client decision pending
- 🟡 **Ready to Quote** (#ffda62) - Quote generation
- 🟣 **Awaiting ZipPay Confirmation** (#af38fa) - Payment confirmation
- ⚪ **Awaiting Purchase Order** (#dbdbdb) - PO pending
- ⚫ **Awaiting Invoice Payment** (#acacac) - Payment pending
- ⏸️ **Unused** (#ffc6c6) - On hold
- 🟢 **Closed Won** (#25b52a) - Deal won
- 🔴 **Closed Lost** (#eb4d4d) - Deal lost

### Workflow Colors
- 🟢 **Green boxes** = Automatic workflows (fire without user action)
- 🔵 **Blue boxes** = Manual workflows (user must set field to trigger)
- 🟠 **Orange boxes** = Time-based workflows (fire on schedule)

### Icons
- ⚡ = Auto-fires immediately
- ⏰ = Time-based trigger
- 🔗 = Clickable URL (opens workflow in Zoho)
- 👤 = Human action required

---

## 🔧 How to Use for Different Purposes

### **For Training New Staff**
1. Open `modules/deals/diagrams/deal-kanban-simple.mmd` in Mermaid Live
2. Show the 9 stages and flow
3. Explain progression: Qualification → Negotiation/Review → Ready to Quote → etc.
4. Then open `modules/deals/diagrams/deal-kanban-detailed.mmd` for in-depth view

### **For Troubleshooting**
1. Deal stuck? Open `modules/deals/diagrams/deal-kanban-detailed.mmd`
2. Find the stage where deal is stuck
3. Click workflow boxes to open in Zoho
4. Verify workflow is active
5. Check if trigger conditions are met

### **For Process Documentation**
1. Use `modules/deals/docs/deal-workflow-urls.md` for written documentation
2. Copy workflow URLs for process manuals
3. Link directly to Zoho workflows from your docs

### **For Dashboard Design**
1. Use `modules/deals/data/deal-stages-kanban.json` for data structure
2. See `kanban_board_config` section for field display recommendations
3. Use stage colors in dashboard
4. Track workflow counts per stage

---

## ⚡ Key Automation Points

### **Automatic Record Creation**
| User Action | Workflow Fires | Creates Record |
|------------|---------------|----------------|
| Change Stage to "Ready to Quote" | Create Quote - Stage Update | **Quote** in Quotes module |
| Quote.Quote_Stage = "Accepted" | Update Deal and Invoice on Quote Closed Won | **Invoice** in Invoices module |
| Enter Purchase_Order_Number | Purchase Order Received | Updates exist registrations |

### **Critical Manual Triggers**
| Field to Set | Workflow Fires | Action |
|-------------|---------------|--------|
| Request_Attendees = TRUE | Email to training Coordinator | Sends email |
| Create_Follow_up_Task = TRUE | Create Team Task from Deals | Creates task |
| Purchase_Order_Number = [value] | 2 workflows | Updates deal & registrations |

---

## 🔍 Troubleshooting Guide

### **Problem: Quote Not Auto-Creating**

**Check:**
1. Open workflow: [Create Quote - Stage Update Ready to quote](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308)
2. Verify workflow is **Active** ✓
3. Check Stage field is set to exact value: "Ready to Quote"
4. Verify Deal has Courseaa field populated

**Solution:**
- Activate workflow if inactive
- Manually create Quote if needed
- Contact admin if workflow broken

### **Problem: Registrations Not Confirming**

**Check:**
1. Did you enter Purchase_Order_Number?
2. Open workflow: [Update Registration records when PO Is received](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006993545)
3. Verify workflow is **Active** ✓
4. Check if Registration_Records exist for this Deal

**Solution:**
- Enter PO# to trigger automatic update
- Or manually update Registration statuses
- Verify Registration_Records are linked to correct Course

### **Problem: PO Reminders Not Firing**

**Check:**
1. Is Course_Start_Date field populated?
2. Open workflows:
   - [28 days before](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311)
   - [14 days before](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269)
3. Has the trigger date passed?
4. Are workflows **Active** ✓

**Solution:**
- Set Course_Start_Date if missing
- Wait for trigger date to arrive
- Check Team_Tasks module for created tasks

---

## 📊 Kanban Board Configuration

If building a custom Kanban dashboard, use these settings:

### **Column Config:**
```json
{
  "Qualification": {
    "color": "#FFC107",
    "icon": "🔍",
    "show_fields": ["Deal_Name", "Account_Name", "Courseaa", "Amount"]
  },
  "Needs Analysis": {
    "color": "#2196F3",
    "icon": "📋",
    "show_fields": ["Training_Coordinator", "Course_Start_Date"]
  },
  "Ready to Quote": {
    "color": "#9C27B0",
    "icon": "📝",
    "show_fields": ["Quote_ID", "Quote_Amount", "Valid_Till"]
  },
  "Negotiation/Review": {
    "color": "#FF9800",
    "icon": "💬",
    "show_fields": ["Po_Expected_Date", "Purchase_Order_Number"]
  },
  "Closed Won": {
    "color": "#4CAF50",
    "icon": "✅",
    "show_fields": ["Purchase_Order_Number", "Closing_Date"]
  },
  "Closed Lost": {
    "color": "#F44336",
    "icon": "❌",
    "show_fields": ["Loss_Reason", "Closing_Date"]
  }
}
```

### **Card Template:**
- **Header:** Deal_Name
- **Subheader:** Account_Name
- **Body:** Courseaa, Course_Start_Date, Amount
- **Badge:** Number_of_Attendees
- **Footer:** Last_Activity_Time
- **Workflow Indicator:** Show count of active workflows (e.g., "⚡ 3 workflows")

---

## 🎯 Quick Actions by Stage

### In **Qualification** Stage:
```
☑️ Verify Deal_Name, Account_Name, Contact_Name
☑️ Select Course → Triggers "Copy of Deal Naming Convention"
☑️ Enter Number_of_Attendees → Triggers "Update Amount"
☑️ Change Stage to "Negotiation/Review"
```

### In **Negotiation/Review** Stage:
```
☑️ Optional: Set Request_Attendees = TRUE → Emails coordinator
☑️ Optional: Set Create_Follow_up_Task = TRUE → Creates task
☑️ Set Course_Start_Date (enables PO reminders)
☑️ Chase purchase order
☑️ When PO received: Enter Purchase_Order_Number
☑️ Change Stage to "Ready to Quote" or "Awaiting Purchase Order"
```

### In **Ready to Quote** Stage:
```
⚠️ Quote AUTO-CREATED - Check Quotes module!
☑️ Review Quote (go to Quotes module)
☑️ Adjust pricing if needed
☑️ In Quotes: Set Send_Quote_as_EMAIL = TRUE
☑️ Change Stage to "Negotiation/Review" or "Awaiting ZipPay Confirmation"
```

### In **Awaiting ZipPay Confirmation** Stage:
```
☑️ Monitor ZipPay payment status
☑️ Set Course_Start_Date if known
☑️ When payment confirmed: Change Stage to "Awaiting Purchase Order" or "Closed Won"
☑️ If declined: Change Stage to "Closed Lost"
```

### In **Awaiting Purchase Order** Stage:
```
☑️ Chase purchase order from client
☑️ When PO received: Enter Purchase_Order_Number
☑️ Change Stage to "Awaiting Invoice Payment" or "Closed Won"
```

### In **Awaiting Invoice Payment** Stage:
```
☑️ Monitor invoice payment status
☑️ Follow up on payment if overdue
☑️ When payment received: Change Stage to "Closed Won"
```

### In **Unused** Stage:
```
☑️ Document reason for hold in Follow_Up_Notes
☑️ Set Follow_up_date (triggers follow-up workflow)
☑️ When reactivated: Change Stage to appropriate active stage
```

### In **Closed Won** Stage:
```
☑️ Enter Purchase_Order_Number if not already done
☑️ Verify Invoice created (check Invoices module)
☑️ Monitor Invoice.Status (Sent → Awaiting Payment → Paid)
☑️ Verify Registration_Records Status = Confirmed
☑️ Deal complete when payment received
```

### In **Closed Won** Stage:
```
☑️ Enter Purchase_Order_Number if not already done
☑️ Verify Invoice created (check Invoices module)
☑️ Monitor Invoice.Status (Sent → Awaiting Payment → Paid)
☑️ Verify Registration_Records Status = Confirmed
☑️ Deal complete when payment received
```

### In **Closed Lost** Stage:
```
☑️ Enter Loss_Reason (MANDATORY)
☑️ Update Quote.Quote_Stage = "Declined"
☑️ Cancel registrations if any exist
☑️ No further action needed
```

---

## 🔗 Direct Links to Key Workflows

### **Most Important Workflows:**

1. **Create Quote** (Ready to Quote stage)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460308
   - ⚡ Auto-fires when Stage = "Ready to Quote"
   - Creates Quote record automatically

2. **Purchase Order Received** (Closed Won stage)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002460283
   - ⚡ Auto-fires when Purchase_Order_Number entered
   - Updates deal status and timestamps

3. **Update Registration records when PO Is received** (Closed Won stage)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006993545
   - ⚡ Auto-fires when Purchase_Order_Number entered
   - Updates all attendees to Status = Confirmed

### **PO Reminder Workflows:**

All fire automatically when in Negotiation stage:

- [28 days before](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638311)
- [14 days before](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638269)
- [5 days before](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000009085891)
- [1 day before](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002638411)

---

## 💡 Pro Tips

### **Avoid Multiple Reminder Tasks**
- ⚠️ If Deal sits in Negotiation too long, you'll get 4 reminder tasks
- Set Course_Start_Date accurately to get appropriate reminders
- Move to Closed Won or Closed Lost promptly when decided

### **Quote Auto-Creation**
- ⚠️ Don't manually create Quote BEFORE changing to "Ready to Quote"
- Let the workflow do it automatically
- You can edit the auto-created Quote after

### **PO Entry Triggers Multiple Updates**
- ✅ Enter Purchase_Order_Number to trigger 2 workflows simultaneously
- This updates both Deal and all Registration_Records
- Saves manual updates to individual registrations

### **Use Manual Workflows Strategically**
- Request_Attendees = Useful for private courses only
- Create_Follow_up_Task = Use for complex deals needing tracking
- Don't trigger unless actually needed

---

## 📈 Success Metrics by Stage

| Stage | Key Metric | Target |
|-------|-----------|--------|
| Qualification | All fields populated | 100% |
| Needs Analysis | Course_Start_Date set | 100% |
| Ready to Quote | Quote sent within | 2 days |
| Negotiation/Review | PO received before | 7 days |
| Closed Won | Payment confirmed | Before course |
| Closed Lost | Loss_Reason documented | 100% |

---

## 🔄 Update Instructions

When workflows change in Zoho:

1. Update `modules/deals/data/deal-stages-kanban.json`:
   - Change workflow IDs
   - Update workflow names
   - Modify URLs if instance changes

2. Re-run generator:
   ```bash
   python3 generate_deal_kanban_mermaid.py
   ```

3. New diagrams generated with updated URLs

4. Commit changes to Git for version control

---

## 📋 Critical Field Reference

The following fields are critical to Deal operations and workflow logic.

### Attendee Form submitted (`Attendee_Form_submitted`)
**Type:** date
**Purpose:** Tracks when attendee details form was submitted for a deal. Used to monitor attendee data collection progress and trigger follow-up actions when forms are outstanding.
**Known Workflow Usage:** None found
**Notes:** Custom field. Typically populated after Request_Attendees workflow emails the Training Coordinator and the form is completed.

### Attendee Requested on (`Attendee_Requested_on`)
**Type:** date
**Purpose:** Records the date when attendee information was requested from the client or training coordinator. Helps track response time and identify deals waiting for attendee details.
**Known Workflow Usage:** None found
**Notes:** Custom field. Set when Request_Attendees checkbox triggers the "Email to training Coordinator from DEALS" workflow.

### Lead Source (`Lead_Source`)
**Type:** picklist
**Purpose:** Identifies the origin channel of the deal/lead for marketing attribution and sales analysis. Critical for measuring campaign effectiveness and ROI.
**Known Workflow Usage:** None found
**Picklist Values:** Advertisement, Booking Form, Calendly, Chat, Cold Call, Email Campaign, Employee Referral, External Referral, Facebook Ads, Google Ads, LinkedIn Ads, Partner, Public Training, Seminar Partner, Trade Show, Web Download, Web Research, Website, Word of Mouth, and others (27 total)
**Notes:** Standard Zoho field. Often inherited from Lead record during conversion.

### Reason For Loss (`Reason_For_Loss__s`)
**Type:** picklist
**Purpose:** Documents the primary reason why a deal was lost. Essential for sales analysis, identifying improvement areas, and understanding competitive landscape.
**Known Workflow Usage:** None found
**Picklist Values:** -None-, Expectation Mismatch, Price, Unqualified Customer, Lack of response, Missed Follow Ups, Wrong Target, Competition, Other, Future Interest
**Notes:** System field. Should be populated when Stage is set to "Closed Lost". Complements the Loss_Reason text field for additional details.

### Reason for Conversion Failure (`Reason_for_Conversion_Failure`)
**Type:** picklist
**Purpose:** Tracks Google Ads conversion tracking failures for deals that originated from ad campaigns. Used for debugging ad attribution and ensuring accurate conversion reporting.
**Known Workflow Usage:** None found
**Picklist Values:** -None-, INVALID_CONVERSION_TYPE, UNPARSEABLE_GCLID, CONVERSION_PRECEDES_CLICK, FUTURE_CONVERSION_TIME, EXPIRED_CLICK, UNKNOWN, TOO_RECENT_CLICK, CLICK_MISSING_CONVERSION_LABEL
**Notes:** System field for Google Ads integration. Only relevant for deals with GCLID tracking. Helps diagnose why conversions may not appear in Google Ads reports.

### Record Status (`Record_Status__s`)
**Type:** picklist
**Purpose:** Indicates the record's lifecycle status within Zoho CRM. Controls visibility and editability of the deal record.
**Known Workflow Usage:** None found
**Picklist Values:** Trash, Available, Draft
**Notes:** System field. "Available" is the normal state for active deals. "Draft" indicates incomplete records. "Trash" indicates soft-deleted records that can be restored.

### Workflow Trigger (`Workflow_Trigger`)
**Type:** picklist
**Purpose:** Manual trigger field that allows users to invoke specific workflows on demand. Provides a controlled way to execute automation actions without checkbox fields.
**Known Workflow Usage:** None found (used as trigger field, not target)
**Picklist Values:** -None-, Update Deal ID, Update Stage, Create Quote, Deal Closed Won, Deal Cancelled
**Notes:** Custom field. Select a value to trigger the corresponding workflow action. Returns to -None- after workflow execution. Useful for re-running automations or manual workflow triggering.

### Parent Account (`Parent_Account`)
**Type:** lookup → Accounts
**Purpose:** Links the deal to a parent account in a hierarchical account structure. Used when a deal is associated with a subsidiary or division that reports to a larger organization. Enables rollup reporting and organizational hierarchy tracking.
**Known Workflow Usage:** None found
**Notes:** Custom lookup field. Populated when the deal's primary Account_Name has a parent organization. Useful for enterprise sales where deals may be negotiated at subsidiary level but invoiced or reported at parent company level. Distinct from Account_Name which is the direct account relationship.

---

**Last Updated:** 18/11/2025
**Zoho Instance:** https://crm.zoho.com.au/crm/org7003757385
**Workflow Rules Base URL:** https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/



