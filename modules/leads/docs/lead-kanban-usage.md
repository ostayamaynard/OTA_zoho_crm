# Lead Status Kanban Workflow - Usage Guide

**Created:** 2025-11-13
**Updated:** 2025-11-18
**Source:** zoho-data-model-2025-11-13.json, zoho-dependencies-2025-11-13.json
**Purpose:** Visual Kanban board for Lead Status with clickable workflow URLs

---

## 🎯 What You Now Have

### 1. **leads_stages_kanban.json** (~25 KB)
Complete Lead Status mapping with:
- ✅ 18 Lead Status values (17 used, 1 unused)
- ✅ 18 workflows documented with Zoho URLs (17 active, 1 inactive)
- ✅ Color codes for each status
- ✅ Human action checklists
- ✅ Workflow trigger conditions
- ✅ Conversion paths documented

### 2. **lead-kanban-detailed.mmd** (Coming soon)
Full Mermaid diagram with:
- ✅ All statuses shown as connected boxes
- ✅ Workflows displayed with **clickable URLs** 🔗
- ✅ Color-coded by trigger type (automatic/manual)
- ✅ Human action boxes at each status
- ✅ Conversion path decision points

### 3. **lead-kanban-simple.mmd** (Coming soon)
Quick overview showing:
- ✅ Statuses as Kanban columns
- ✅ Workflow counts per status
- ✅ Color-coded status boxes
- ✅ Flow arrows showing progression

### 4. **lead-workflow-urls.md** (Coming soon)
Reference document with:
- ✅ All workflows organized by status
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
   cat modules/leads/diagrams/lead-kanban-detailed.mmd
   ```

3. **Paste into editor**

4. **Click workflow boxes** - Opens Zoho CRM workflow directly! 🔗

**Example:**
- Click "New Lead Notification" box → Opens workflow 52330000000427010 in your Zoho instance
- Click "Generate Payment URL" box → Opens workflow 52330000008228472
- Each workflow box has a 🔗 icon indicating it's clickable

### **Option 2: GitHub Markdown (For team documentation)**

1. **Create markdown file:**
   ```markdown
   # Lead Workflow Kanban
   
   ```mermaid
   [paste lead-kanban-detailed.mmd content here]
   ```
   ```

2. **Commit to GitHub repository**

3. **View in GitHub** - Diagram renders with clickable links!

---

## 📋 Status-by-Status Breakdown

### **Status 1: New Lead** 🆕
**Color:** Yellow (#ffda62)  
**Duration:** 0-24 hours  
**Workflow Count:** 5 automatic

**What Happens:**
- ✅ 5 workflows fire automatically when Lead created
- ✅ Email notification sent to team
- ✅ Call task created (call within 24 hours)
- ✅ Phone numbers formatted
- ✅ Lead owner assigned
- ✅ G-Series leads tagged

**Human Actions:**
1. Contact lead within 24 hours (task created automatically)
2. Select Course (Course lookup field) → Triggers "Course Details Udpated"
3. Update lead details (name, phone, email, company)
4. Change Status to "Contacted" when reached, or "Attempted to Contact" if no answer

**Workflow URLs:**
- [New Lead Notification](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000427010)
- [CallWithIn24Hours and Team Task](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000864146)
- [Format Number](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000005789994)
- [Lead Owner Assignment](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007257288)
- [Tag G-Series Leadership Leads](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000007732209)

---

### **Status 2-5: New Lead Variants** 🌐📢💼📱

**New Lead - Website** (Status 2)
- Same workflows as New Lead
- Typically has Course pre-selected from website form
- **Priority:** High (website leads usually more qualified)

**New Lead - Google Ads** (Status 3)
- Same workflows as New Lead
- Check campaign details (GCLID, Keyword fields)
- **Priority:** Medium-High

**New Lead - Linkedin** (Status 4)
- Same workflows as New Lead
- **Priority:** Medium

**New Lead - Facebook** (Status 5)
- Same workflows as New Lead
- **Priority:** Medium

---

### **Status 6: Contacted** ✅
**Color:** Green (#98d681)  
**Duration:** 1-3 days  
**Workflow Count:** 2 manual

**What Happens:**
- 🔵 Manual workflows available (user must trigger)
- 📧 Can send course email
- 📋 Can create follow-up tasks

**Human Actions:**
1. Assess lead interest and qualification
2. Determine payment method (credit card, invoice, private)
3. **Optional:** Set Create_task = TRUE → Creates Team Task
4. **Optional:** Set Course_Email = TRUE → Sends course details email
5. **If qualified:** Set WF_Action field to conversion option
6. Change Status to "Interested" if qualified, or "Not Qualified"/"Lost Lead" if not

**Manual Workflow Triggers:**
- [Create Team task in leads](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000002758376) - Set Create_task = TRUE
- [Send Course email](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000006093561) - Set Course_Email = TRUE

---

### **Status 7-10: Contact Attempts** 📞🔄

**Attempted to Contact** (Status 7)
- No automated workflows
- Schedule follow-up date
- Try alternative contact method
- Move to "Contacted" if reached, or "Re-Attempt 1" if another try needed

**Re-Attempt 1** (Status 8)
- First re-attempt
- Try different contact method
- Move to "Contacted" if reached, or "Re-Attempt 2" if needed

**Re-Attempt 2** (Status 9)
- Second re-attempt
- Final attempt before marking as lost
- Move to "Contacted" if reached, or "Re-Attempt 3" if one more try

**Re-Attempt 3** (Status 10)
- Third and final re-attempt
- ⚠️ After this, should mark as "Lost Lead" or "Junk Lead"
- Move to "Contacted" if reached, otherwise mark as lost

---

### **Status 11: Interested** 👍
**Color:** Green (#25b52a)  
**Duration:** 1-7 days  
**Workflow Count:** 2 manual

**⚠️ IMPORTANT:** This is where conversion decisions are made

**What Happens:**
- 🔵 Manual workflows available based on WF_Action field
- 💳 Can generate payment URL for credit card payment
- 📍 Can generate location selection URL

**Human Actions:**
1. **Determine conversion path:**
   - **Credit Card Payment:** Set WF_Action = "Generate Payment URL"
   - **Invoice Payment:** Set WF_Action = "Convert Pay Via Invoice"
   - **Private Course:** Set WF_Action = "Convert Non Paying Lead"
   - **Contact Only:** Set WF_Action = "Convert to Only Create a contact"
2. **If credit card:** Set WF_Action = "Generate Payment URL"
   - This generates payment link
   - Send link to lead
   - Wait for payment
   - Status may auto-change to "Course Purchased - Convert" when payment received
3. **If invoice/private/contact:** Set appropriate WF_Action
   - Conversion happens immediately
   - Status changes to "Convert - Create Records"

**Workflow URLs:**
- [Generate Payment URL](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008228472) - Set WF_Action = "Generate Payment URL"
- [Update Location URL](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008158816) - Generates location form

---

### **Status 12: Course Purchased - Convert** 💳
**Color:** Yellow (#ffda62)  
**Duration:** Immediate (automatic)  
**Workflow Count:** 1 automatic

**⚠️ IMPORTANT:** This status is set automatically when Stripe payment received

**What Happens:**
- ⚡ [Convert on Payment Success](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523) fires automatically
- 📄 Creates: Contact, Account, Deal, Registration_Record, Invoice
- 🔗 All records linked together
- ✅ Lead marked as Converted__s = TRUE

**Human Actions:**
1. Verify payment received (check Stripe_ID, Payment_CODE fields)
2. Verify conversion records created
3. Check Converted_Contact, Converted_Account, Converted_Deal fields
4. Status will change to "Convert - Create Records" after conversion

**Workflow URL:**
- [Convert on Payment Success](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523) ⚡ **AUTO-FIRES**

---

### **Status 13: Convert - Create Records** ✨
**Color:** Light Green (#c4f0b3)  
**Duration:** Ongoing (terminal)  
**Workflow Count:** 0 (conversion already happened)

**What Happens:**
- ✅ Lead has been converted
- ✅ Records created in related modules
- ✅ Converted__s = TRUE

**Human Actions:**
1. Verify conversion records:
   - Check Contacts module for created Contact
   - Check Accounts module for created Account
   - Check Deals module for created Deal (if applicable)
   - Check Registration_Records module (if course purchased)
   - Check Invoices module (if invoice created)
2. Verify Converted__s = TRUE
3. Lead remains in this status after conversion

**Conversion Workflows (already executed):**
- [Convert on Payment Success](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523) - Credit card payment
- [Convert Pay Via Invoice](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008920352) - Invoice payment
- [Convert Non Paying Lead](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008250081) - Private course
- [Convert to Only Create a contact](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008405346) - Contact only

---

### **Status 14: Private Lead** 🏢
**Color:** Blue (#5cb3fd)  
**Duration:** 1-7 days  
**Workflow Count:** 0

**What Happens:**
- 🏢 Lead identified as private course enquiry
- No automated workflows

**Human Actions:**
1. Gather private course requirements
2. Document in Description field
3. Set Course and Course_Type fields
4. Set WF_Action = "Convert Non Paying Lead"
5. This triggers conversion workflow
6. Status changes to "Convert - Create Records"

**Exit Criteria:**
- Set WF_Action = "Convert Non Paying Lead"
- Creates Deal for quote/PO process
- Status changes to "Convert - Create Records"

---

### **Status 15: Junk Lead** 🗑️
**Color:** Red (#eb4d4d)  
**Duration:** N/A (terminal)  
**Workflow Count:** 0

**Human Actions:**
1. **Document reason** in Description field
2. No further action needed

**No automated workflows** - Terminal status

---

### **Status 16: Lost Lead** ❌
**Color:** Dark Red (#9a2e47)  
**Duration:** N/A (terminal)  
**Workflow Count:** 0

**Human Actions:**
1. **Document loss reason** in Description field
2. Note why lead was lost (not interested, unresponsive, etc.)
3. No further action needed

**No automated workflows** - Terminal status

---

### **Status 17: Not Qualified** 🚫
**Color:** Light Red (#ffc6c6)  
**Duration:** N/A (terminal)  
**Workflow Count:** 0

**Human Actions:**
1. **Document qualification reason** in Description field
2. Note why lead is not qualified
3. **Optional:** May still convert to Contact only if useful for future
4. No further action needed

**No automated workflows** - Terminal status

---

## 🎨 Visual Legend

### Status Colors
- 🟡 **New Lead variants** (#ffda62, #f8e199) - Initial entry
- 🟢 **Contacted** (#98d681) - Successfully contacted
- 🔵 **Attempted to Contact** (#add9ff) - Contact attempt
- 🔴 **Re-Attempts** (#ffc6c6, #fd8989, #eb4d4d) - Multiple attempts
- 🟢 **Interested** (#25b52a) - Qualified and interested
- 🟡 **Course Purchased** (#ffda62) - Payment received
- 🟢 **Convert - Create Records** (#c4f0b3) - Conversion complete
- 🔵 **Private Lead** (#5cb3fd) - Private course enquiry
- 🔴 **Terminal Statuses** (#eb4d4d, #9a2e47, #ffc6c6) - Lost/Junk/Not Qualified

### Workflow Colors
- 🟢 **Green boxes** = Automatic workflows (fire without user action)
- 🔵 **Blue boxes** = Manual workflows (user must set field to trigger)

### Icons
- ⚡ = Auto-fires immediately
- 🔗 = Clickable URL (opens workflow in Zoho)
- 👤 = Human action required

---

## 🔧 How to Use for Different Purposes

### **For Training New Staff**
1. Open `modules/leads/diagrams/lead-kanban-simple.mmd` in Mermaid Live
2. Show the status flow from New Lead → Contacted → Interested → Convert
3. Explain conversion paths
4. Then open `modules/leads/diagrams/lead-kanban-detailed.mmd` for in-depth view

### **For Troubleshooting**
1. Lead stuck? Open `modules/leads/diagrams/lead-kanban-detailed.mmd`
2. Find the status where lead is stuck
3. Click workflow boxes to open in Zoho
4. Verify workflow is active
5. Check if trigger conditions are met

### **For Process Documentation**
1. Use `modules/leads/docs/lead-workflow-urls.md` for written documentation
2. Copy workflow URLs for process manuals
3. Link directly to Zoho workflows from your docs

### **For Dashboard Design**
1. Use `leads_stages_kanban.json` for data structure
2. See `kanban_board_config` section for field display recommendations
3. Use status colors in dashboard
4. Track workflow counts per status

---

## ⚡ Key Automation Points

### **Automatic Record Creation**
| User Action | Workflow Fires | Creates Record |
|------------|---------------|----------------|
| Lead created | 5 automatic workflows | **Team_Task** (call within 24 hours) |
| Stripe payment received | Convert on Payment Success | **Contact, Account, Deal, Registration_Record, Invoice** |
| WF_Action = Convert Pay Via Invoice | Convert Pay Via Invoice | **Contact, Account, Deal, Registration_Record, Invoice** |
| WF_Action = Convert Non Paying Lead | Convert Non Paying Lead | **Contact, Account, Deal** |
| WF_Action = Convert to Only Create a contact | Convert to Only Create a contact | **Contact** |

### **Additional Workflows**
| Workflow | Trigger Type | Purpose |
|----------|-------------|---------|
| setLeadGMapFiledsAsEmpty | date_or_datetime | Clears Google Maps fields on schedule |
| TEST SMS | field_update (inactive) | Testing workflow for SMS functionality |

### **Critical Manual Triggers**
| Field to Set | Workflow Fires | Action |
|-------------|---------------|--------|
| WF_Action = "Generate Payment URL" | Generate Payment URL | Generates payment link |
| WF_Action = "Convert Pay Via Invoice" | Convert Pay Via Invoice | Converts lead (invoice path) |
| WF_Action = "Convert Non Paying Lead" | Convert Non Paying Lead | Converts lead (private course) |
| WF_Action = "Convert to Only Create a contact" | Convert to Only Create a contact | Creates Contact only |
| Create_task = TRUE | Create Team task in leads | Creates task |
| Course_Email = TRUE | Send Course email | Sends course email |

---

## 🔍 Troubleshooting Guide

### **Problem: Lead Not Contacted Within 24 Hours**

**Check:**
1. Open workflow: [CallWithIn24Hours and Team Task](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000864146)
2. Verify workflow is **Active** ✓
3. Check Team_Tasks module for created task
4. Verify Lead Owner is assigned

**Solution:**
- Activate workflow if inactive
- Check Team_Tasks module
- Manually create task if needed

### **Problem: Payment URL Not Generated**

**Check:**
1. Open workflow: [Generate Payment URL](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008228472)
2. Verify workflow is **Active** ✓
3. Did you set WF_Action to exact value "Generate Payment URL"?
4. Check Zoho_Form_Payment_URL field for generated URL

**Solution:**
- Verify workflow is active in Zoho
- Ensure WF_Action value matches exactly
- Check Zoho_Form_Payment_URL field

### **Problem: Lead Not Converting**

**Check:**
1. Is conversion workflow active?
2. Did you set WF_Action field?
3. Are required fields populated (First_Name, Last_Name, Email)?
4. Check workflows:
   - [Convert on Payment Success](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523)
   - [Convert Pay Via Invoice](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008920352)
   - [Convert Non Paying Lead](https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008250081)

**Solution:**
- Verify workflow is active
- Set WF_Action field to appropriate value
- Ensure all required fields are populated
- Check Converted__s field after conversion

---

## 📊 Kanban Board Configuration

If building a custom Kanban dashboard, use these settings:

### **Column Config:**
```json
{
  "New Lead": {
    "color": "#ffda62",
    "icon": "🆕",
    "show_fields": ["First_Name", "Last_Name", "Company", "Email", "Mobile"]
  },
  "Contacted": {
    "color": "#98d681",
    "icon": "✅",
    "show_fields": ["First_Name", "Last_Name", "Course", "WF_Action"]
  },
  "Interested": {
    "color": "#25b52a",
    "icon": "👍",
    "show_fields": ["First_Name", "Last_Name", "Course", "WF_Action", "Payment_source"]
  },
  "Convert - Create Records": {
    "color": "#c4f0b3",
    "icon": "✨",
    "show_fields": ["First_Name", "Last_Name", "Converted__s", "Converted_Contact"]
  }
}
```

### **Card Template:**
- **Header:** First_Name + Last_Name
- **Subheader:** Company
- **Body:** Course, Email, Mobile
- **Badge:** Lead_Status
- **Footer:** Last_Activity_Time
- **Workflow Indicator:** Show count of active workflows

---

## 🎯 Quick Actions by Status

### In **New Lead** Status:
```
☑️ Contact lead within 24 hours (task created automatically)
☑️ Select Course → Triggers "Course Details Udpated"
☑️ Update lead details (name, phone, email)
☑️ Change Status to "Contacted" when reached
```

### In **Contacted** Status:
```
☑️ Assess lead interest and qualification
☑️ Determine payment method
☑️ Optional: Set Create_task = TRUE → Creates task
☑️ Optional: Set Course_Email = TRUE → Sends course email
☑️ If qualified: Set WF_Action field
☑️ Change Status to "Interested" if qualified
```

### In **Interested** Status:
```
⚠️ Set WF_Action field to conversion option:
  • "Generate Payment URL" (credit card)
  • "Convert Pay Via Invoice" (invoice)
  • "Convert Non Paying Lead" (private)
  • "Convert to Only Create a contact" (contact only)
☑️ If credit card: Send payment link to lead
☑️ Wait for payment or conversion
```

### In **Course Purchased - Convert** Status:
```
☑️ Verify payment received (Stripe_ID, Payment_CODE)
☑️ Verify conversion records created
☑️ Check Converted_Contact, Converted_Account, Converted_Deal
☑️ Status auto-changes to "Convert - Create Records"
```

### In **Convert - Create Records** Status:
```
☑️ Verify conversion records in related modules
☑️ Verify Converted__s = TRUE
☑️ Lead remains in this status after conversion
☑️ Deal progresses through Deal stages
```

### In **Terminal Statuses** (Junk/Lost/Not Qualified):
```
☑️ Document reason in Description field
☑️ No further action needed
```

---

## 🔗 Direct Links to Key Workflows

### **Most Important Workflows:**

1. **CallWithIn24Hours and Team Task** (New Lead status)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000000864146
   - ⚡ Auto-fires when Lead created
   - Creates Team Task for follow-up

2. **Generate Payment URL** (Interested status)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008228472
   - 🔵 Manual trigger - Set WF_Action = "Generate Payment URL"
   - Generates payment link for credit card payment

3. **Convert on Payment Success** (Course Purchased - Convert status)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008292523
   - ⚡ Auto-fires when Stripe payment received
   - Creates Contact, Account, Deal, Registration, Invoice

4. **Convert Pay Via Invoice** (Interested status)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008920352
   - 🔵 Manual trigger - Set WF_Action = "Convert Pay Via Invoice"
   - Creates Contact, Account, Deal, Registration, Invoice

5. **Convert Non Paying Lead** (Interested/Private Lead status)
   - https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/52330000008250081
   - 🔵 Manual trigger - Set WF_Action = "Convert Non Paying Lead"
   - Creates Contact, Account, Deal (for private courses)

---

## 💡 Pro Tips

### **24-Hour Contact Rule**
- ⚠️ Workflow creates task automatically - don't ignore it!
- Contact within 24 hours improves conversion rates
- Check Team_Tasks module for follow-up tasks

### **WF_Action Field is Critical**
- ⚠️ This field controls conversion workflows
- Must set exact value (case-sensitive)
- Options:
  - "Generate Payment URL"
  - "Convert Pay Via Invoice"
  - "Convert Non Paying Lead"
  - "Convert to Only Create a contact"

### **Payment URL Generation**
- ✅ Generates secure payment link
- ✅ Send link to lead via email
- ✅ Payment triggers automatic conversion
- ✅ No manual conversion needed after payment

### **Conversion Paths**
- **Credit Card:** Generate Payment URL → Payment → Auto-convert
- **Invoice:** Convert Pay Via Invoice → Creates Invoice → Manual payment tracking
- **Private:** Convert Non Paying Lead → Creates Deal → Quote/PO process
- **Contact Only:** Convert to Only Create a contact → Creates Contact only

### **Re-Attempt Strategy**
- ⚠️ Don't let leads sit in Re-Attempt 3
- After 3 attempts, mark as Lost Lead or Junk Lead
- Document reason in Description field

---

## 📈 Success Metrics by Status

| Status | Key Metric | Target |
|--------|-----------|--------|
| New Lead | Contacted within 24 hours | 100% |
| Contacted | Qualification rate | > 50% |
| Interested | Conversion rate | > 30% |
| Course Purchased - Convert | Payment success rate | > 90% |
| Convert - Create Records | Records created | 100% |
| Lost Lead | Reason documented | 100% |

---

## 🔄 Update Instructions

When workflows change in Zoho:

1. Update `leads_stages_kanban.json`:
   - Change workflow IDs
   - Update workflow names
   - Modify URLs if instance changes

2. Re-run generator (if applicable):
   ```bash
   python3 generate_lead_kanban_mermaid.py
   ```

3. New diagrams generated with updated URLs

4. Commit changes to Git for version control

---

**Last Updated:** 2025-11-18
**Source:** Zoho CRM Export 2025-11-13
**Zoho Instance:** https://crm.zoho.com.au/crm/org7003757385
**Workflow Rules Base URL:** https://crm.zoho.com.au/crm/org7003757385/settings/workflow-rules/

