# Excel Report Guide - Zoho CRM Data Model

## 📊 All 11 Sheets Explained

### **Sheet 1: Modules** (65 modules)
**Purpose:** Overview of all CRM modules
**Useful for:**
- Understanding which modules are creatable, editable, deletable
- Quick counts of fields and workflows per module
- Identifying API-supported modules

**Key columns:** Module Name, API Supported, Field Count, Workflow Count, Blueprint Count

---

### **Sheet 2: All Fields** (1,524 fields)
**Purpose:** Complete field inventory across all modules
**Useful for:**
- Finding all instances of a field across modules
- Identifying custom vs. system fields
- Checking field properties (required, read-only, visible)
- Finding lookup fields and their target modules

**Key columns:** Module, Field API Name, Data Type, Required, Custom Field, Lookup Module

**How to use:**
- Filter by "Custom Field = TRUE" to find custom fields
- Filter by "Data Type = lookup" to find all lookup relationships
- Sort by "Required = TRUE" to find mandatory fields

---

### **Sheet 3: Workflows** (154 workflows, 140 active)
**Purpose:** Complete list of all workflows
**Useful for:**
- Identifying who created/modified each workflow
- Finding inactive workflows that can be deleted
- Checking when workflows were last executed
- Understanding workflow distribution across modules

**Key columns:** Module, Workflow Name, Active, Trigger Type, Created By, Modified By, Last Executed

**Insights:**
- **75 workflows** are "field_update" triggers (run when a field changes)
- **32 workflows** are "create" triggers (run when a record is created)
- **30 workflows** are "date_or_datetime" triggers (run on scheduled dates)
- **Courses module** has the most workflows (37)
- **Registration_Records** has 36 workflows

**How to use:**
- Filter by "Active = FALSE" to find workflows to review/delete
- Filter by "Trigger Type" to understand automation patterns
- Sort by "Last Executed" to find recently used workflows
- Group by "Created By" to see who maintains which workflows

---

### **Sheet 4: Workflow Dependencies** (154 workflows)
**Purpose:** Detailed workflow analysis with condition fields
**Useful for:**
- **75 workflows** show which fields trigger them (Condition Fields column)
- Understanding which workflows run when specific fields change
- Tracking workflow maintenance (Created By, Modified By)

**Key columns:** Module, Workflow Name, Condition Fields, Created By, Modified By

**Example findings:**
- **Create Team task in leads** → triggers on "Create_task" field
- **Course Details Updated** → triggers on "Course" field
- **Update Address** → triggers on "State1" field

**API Limitations:**
- "Updated Fields" column is empty (Zoho API doesn't expose workflow actions)
- "Cross-Module Actions" column is empty (Zoho API doesn't expose this)
- To see what fields a workflow UPDATES, check the workflow in Zoho CRM UI

**How to use:**
- Filter by "Condition Fields" to find workflows triggered by specific fields
- Before deleting a field, check if any workflow uses it as a condition
- Use this with Sheet 5 (Field Usage Matrix) for impact analysis

---

### **Sheet 5: Field Usage Matrix** (1,524 fields)
**Purpose:** Shows where each field is used
**Useful for:**
- Impact analysis before deleting fields
- Finding unused fields
- Understanding field relationships

**Key columns:** Module, Field, Type, Mandatory, Custom, Used in Workflows

**How to use:**
- Filter by "Used in Workflows = (empty)" to find unused fields
- Check "Is Lookup = TRUE" to see relationship fields
- Combine with Sheet 4 to understand full field usage

---

### **Sheet 6: Automation Chains**
**Purpose:** Would show workflows that trigger other workflows
**Current status:** Empty due to API limitation
**Note:** Zoho API doesn't expose workflow actions needed to detect automation chains

---

### **Sheet 7: Lookup Relationships** (115 relationships)
**Purpose:** Module-to-module connections via lookup fields
**Useful for:**
- Understanding module dependencies
- Migration planning
- Data model visualization

**Key columns:** Source Module, Field Name, Target Module, Required

**How to use:**
- Filter by "Target Module" to see what references a specific module
- Check "Required = TRUE" for critical relationships
- Use for migration planning (delete order: least referenced first)

---

### **Sheet 8: Formula Fields** (14 formula fields)
**Purpose:** All calculated fields
**Useful for:**
- Understanding complex calculations
- Troubleshooting formula errors
- Documentation

**Modules with formulas:**
- Courses: 1 formula field (Duration)
- Sales_Orders: 2 formulas (Sub Total, Grand Total)
- Quoted_Items: 3 formulas
- Ordered_Items: 3 formulas
- Invoiced_Items: 3 formulas
- Course_Performance: 2 formulas

---

### **Sheet 9: Mandatory Fields** (58 required fields)
**Purpose:** Fields that must be filled
**Useful for:**
- Form validation
- Import requirements
- API integration requirements

**How to use:**
- Filter by "System Mandatory = TRUE" for Zoho system requirements
- Check before creating records via API (these fields are required)

---

### **Sheet 10: Cross-Module Dependencies** (115 dependencies)
**Purpose:** How modules are interconnected
**Useful for:**
- Migration planning
- Understanding data model architecture
- Impact analysis

**Reference types:**
- **Lookup:** Direct field references (115 total)
- **Workflow:** Workflows creating/updating records in other modules (0 - API limitation)

**Most referenced modules:**
- **Contacts:** Referenced by 25 other modules
- **Accounts:** Referenced by 14 modules
- **Deals:** Referenced by 13 modules
- **Courses:** Referenced by 8 modules

---

### **Sheet 11: Summary** (65 modules)
**Purpose:** High-level statistics per module
**Useful for:**
- Quick overview dashboard
- Identifying complex modules
- Planning cleanup efforts

**Key metrics:**
- Total Fields
- Lookup Fields
- Formula Fields
- Mandatory Fields
- Total Workflows
- Active Workflows

**Most complex modules:**
1. **Leads:** 151 fields, 19 workflows (18 active)
2. **Courses:** 137 fields, 37 workflows (34 active)
3. **Contacts:** 113 fields, 7 workflows
4. **Deals:** 86 fields, 19 workflows (18 active)

---

## 🔍 How to Trace Errors

### Finding Workflow Issues:
1. **Sheet 3** → Find the workflow by name
2. **Sheet 4** → Check "Condition Fields" to see what triggers it
3. **Sheet 5** → Check if those fields exist and are used elsewhere

### Before Deleting a Field:
1. **Sheet 5 (Field Usage Matrix)** → Check "Used in Workflows" column
2. **Sheet 4 (Workflow Dependencies)** → Search for field name in "Condition Fields"
3. **Sheet 7 (Lookup Relationships)** → Check if it's a lookup field
4. **Sheet 8 (Formula Fields)** → Check if it's used in formulas

### Before Deleting a Module:
1. **Sheet 10 (Cross-Module Dependencies)** → See what references it
2. **Sheet 7 (Lookup Relationships)** → Check lookup fields pointing to it
3. **Sheet 11 (Summary)** → See its workflow count

### Finding Inactive/Unused Resources:
1. **Sheet 3** → Filter "Active = FALSE" to find inactive workflows
2. **Sheet 3** → Sort by "Last Executed" to find rarely-used workflows
3. **Sheet 5** → Filter "Used in Workflows = (empty)" to find unused fields

---

## ⚠️ API Limitations

The Zoho CRM REST API has limitations:

### ✅ What IS Available:
- Workflow names, IDs, descriptions
- Active status and trigger types
- **Condition fields** for field_update workflows (75 workflows)
- Created By, Modified By, timestamps
- Last execution times

### ❌ What is NOT Available:
- Workflow actions (what fields get updated)
- Cross-module actions (creating/updating records in other modules)
- Email notifications, webhooks, custom functions
- **Action details must be viewed in Zoho CRM UI**

---

## 💡 Best Practices

### Workflow Maintenance:
1. Check **Sheet 3** for workflows by "Created By" to assign ownership
2. Review **inactive workflows** (14 total) - can they be deleted?
3. Check workflows with **no recent execution** - are they still needed?

### Field Cleanup:
1. Use **Sheet 5** to find fields not used in workflows
2. Cross-reference with **Sheet 7** to ensure not used in lookups
3. Check **Sheet 8** to ensure not used in formulas

### Module Analysis:
1. **Courses** and **Registration_Records** have the most workflows (37 and 36)
   - These are complex modules - be careful with changes
2. Many modules have **0 workflows** - simpler to modify

---

## 📈 Key Statistics

- **154 workflows total** (140 active, 14 inactive)
- **75 workflows** have extractable trigger conditions
- **115 lookup relationships** connecting modules
- **1,524 fields** across 65 modules
- **58 mandatory fields** that must be filled
- **14 formula fields** with calculations

---

## 🎯 Recommended Actions

### Immediate:
1. **Review the 14 inactive workflows** (Sheet 3: Active = FALSE)
   - Can they be deleted or should they be reactivated?

2. **Check workflows not executed recently** (Sheet 3: Last Executed)
   - Sort by "Last Executed" and review old workflows

3. **Identify workflow owners** (Sheet 3: Created By / Modified By)
   - Assign maintenance responsibility

### Long-term:
1. **Document field usage** using Sheet 5 (Field Usage Matrix)
2. **Create data model diagram** from Sheet 10 (Cross-Module Dependencies)
3. **Plan migrations** using lookup relationships (Sheet 7)

---

## 📝 Notes for Power Users

- **Pivot tables:** Create pivot tables on Sheet 3 grouped by "Created By" or "Module"
- **Conditional formatting:** Highlight inactive workflows in red
- **Filters:** Use Excel's filter feature to slice data by module
- **VLOOKUP:** Cross-reference between sheets using Workflow ID or Module name

---

**Generated:** November 13, 2025
**Workflows Analyzed:** 154 (with criteria extraction)
**Modules:** 65 API-enabled modules
**Fields Documented:** 1,524 fields




