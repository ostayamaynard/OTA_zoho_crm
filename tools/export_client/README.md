# Zoho CRM Metadata Export

**READ-ONLY Export** - This script safely extracts your Zoho CRM configuration without modifying any data.

---

## 🚀 Quick Start (3 Easy Steps)

### Step 1: Install Python

If you don't have Python installed:

- **Windows**: Download from <https://www.python.org/downloads/>
- **Mac**: Already installed, or use `brew install python3`
- **Linux**: Already installed

Verify installation:

```bash
python --version
```

(Should show Python 3.7 or higher)

---

### Step 2: Install Required Libraries

Open Command Prompt (Windows) or Terminal (Mac/Linux) in this folder, then run:

```bash
pip install requests python-dotenv pandas openpyxl
```

**What this installs:**

- `requests` - To communicate with Zoho API
- `python-dotenv` - To read credentials from .env file
- `pandas` - To create Excel reports
- `openpyxl` - Excel file support

---

### Step 3: Run the Export

In the same Command Prompt/Terminal window:

**Quick method (uses helper scripts):**
```bash
# Mac/Linux
./run_export.sh

# Windows
RUN_EXPORT.bat
```

**Or run directly:**
```bash
python3 zoho_export.py
```

**That's it!** The script will run for 5-15 minutes and show progress messages.

---

## 📦 What You'll Get

After the script finishes, you'll have three files:

### 1. `zoho-data-model-YYYY-MM-DD.json`

- Complete metadata export in JSON format
- Contains all modules, fields, layouts, workflows, etc.
- Use this for technical analysis or importing into other systems

### 2. `zoho-dependencies-YYYY-MM-DD.json`

- Field dependency mapping
- Workflow → Field relationships
- Lookup relationships between modules
- Useful for understanding how your CRM is connected

### 3. `Zoho_CRM_Data_Model_YYYY-MM-DD.xlsx`

- Comprehensive Excel workbook with 11 detailed sheets:
  - **1. Modules** - Overview of all CRM modules with counts
  - **2. All Fields** - Complete field inventory with properties
  - **3. Workflows** - All workflow rules and automation
  - **4. Workflow Dependencies** - Detailed workflow analysis (condition fields, updated fields, cross-module actions)
  - **5. Field Usage Matrix** - See exactly where each field is used (workflows, blueprints)
  - **6. Automation Chains** - Workflows that trigger other workflows
  - **7. Lookup Relationships** - How modules connect via lookup fields
  - **8. Formula Fields** - All formula fields with their expressions
  - **9. Mandatory Fields** - Required and system-mandatory fields
  - **10. Cross-Module Dependencies** - Complete module interconnection map
  - **11. Summary** - High-level statistics dashboard per module

---

## ⏱️ What to Expect

### During Export

```
🔑 Requesting new access token...
✅ Access token obtained successfully

📦 Fetching modules...
✅ Found 23 modules

📊 Processing 23 API-enabled modules...

[1/23] Processing: Leads
  ✅ 52 fields, 3 workflows, 1 blueprints

[2/23] Processing: Contacts
  ✅ 48 fields, 5 workflows, 0 blueprints

...

🔍 Analyzing comprehensive field dependencies...
✅ Dependency analysis complete

💾 Saving Export Files
💾 Saved: zoho-data-model-2026-01-08.json
💾 Saved: zoho-dependencies-2026-01-08.json
📊 Creating comprehensive Excel report...
💾 Saved: Zoho_CRM_Data_Model_2026-01-08.xlsx
   📊 11 sheets created with comprehensive dependency analysis

✅ Export Complete!
```

### Typical Runtime

- **Small CRM** (10-20 modules): 3-5 minutes
- **Medium CRM** (20-40 modules): 5-10 minutes
- **Large CRM** (40+ modules): 10-20 minutes

---

## 🛑 Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"

**Problem:** Python libraries not installed  
**Solution:** Run: `pip install requests python-dotenv pandas openpyxl`

### "Error getting access token: 401"

**Problem:** Invalid credentials  
**Solution:** Check that the `.env` file has the correct credentials from Maynard

### "Error getting access token: Invalid client"

**Problem:** Client ID or Secret is wrong  
**Solution:** Ask Maynard to regenerate credentials

### "Rate limited. Waiting X seconds..."

**This is normal!** The script is handling Zoho's rate limits automatically. Just wait.

### Script runs but creates empty JSON files

**Problem:** Wrong API region or no data  
**Solution:** Verify the `.env` file has `ZOHO_API_BASE=https://www.zohoapis.com.au/crm/v8`

### "Permission denied" for specific modules

**This is normal!** Some modules may not be accessible. The script will continue with others.

---

## 🔒 Security Notes

### What This Script CANNOT Do

- ❌ Create records
- ❌ Update records
- ❌ Delete records
- ❌ Modify fields
- ❌ Change workflows
- ❌ Alter permissions

### What This Script CAN Do

- ✅ Read module configuration
- ✅ Read field definitions
- ✅ Read workflow rules
- ✅ Create local files on your computer

**You cannot accidentally break anything!**

### After Export

- Delete the `.env` file (contains credentials)
- Or keep it secure if you need to run exports again
- Share only the JSON/Excel output files

---

## 📁 File Structure

```
tools/export_client/
├── .env                              ← Your credentials (keep secret!)
├── zoho_export.py                    ← The export script
├── zoho_export_v3.py                 ← Enhanced version with improvements
├── README.md                         ← This file
├── requirements.txt                  ← Python dependencies
├── run_export.sh                     ← Mac/Linux helper script
└── RUN_EXPORT.bat                    ← Windows helper script
```

**After running, JSON files are automatically moved to:** `data/exports/`
```
data/exports/
├── zoho-data-model-2026-01-08.json
└── zoho-dependencies-2026-01-08.json
```

**Excel file stays in this directory:** `Zoho_CRM_Data_Model_2026-01-08.xlsx`

**Next (recommended):** From repo root, run the processing pipeline to diff and regenerate docs:
```bash
python tools/update_pipeline.py --apply
```

This will produce reports under `reports/` and refresh models/docs/diagrams using the latest export.
```

---

## ❓ Common Questions

**Q: Do I need to log in to Zoho?**  
A: No! The credentials in `.env` handle authentication automatically.

**Q: Will this slow down our CRM?**  
A: No. The script uses rate limiting and only reads metadata (not records).

**Q: Can I run this multiple times?**  
A: Yes! Run it anytime to get an updated export. Previous files won't be overwritten (they have dates in filenames).

**Q: How do I know it's working?**  
A: You'll see progress messages. If it's stuck on one module for >2 minutes, that's unusual - contact Maynard.

**Q: Can other people run this?**  
A: Yes, as long as they have the `.env` file with credentials. But remember - credentials should be kept secure!

**Q: What if I want to stop the script?**  
A: Press `Ctrl+C` in the terminal. It's safe to stop anytime.

---

## 🆘 Need Help?

If you encounter issues:

1. **Check the error message** - It usually explains what's wrong
2. **Look at Troubleshooting section above**
3. **Contact Maynard (IT)** - He set up the credentials and can help

---

## 📊 Using the Excel Output

The Excel file provides comprehensive analysis of your CRM structure with 11 detailed sheets:

### Key Sheets for Common Tasks:

**1. Modules** - Overview of all modules with field, workflow, and blueprint counts

**2. All Fields** - Complete field inventory with properties (type, required, custom, etc.)

**3. Workflows** - List of all workflow rules with status and execution timing

**4. Workflow Dependencies** ⭐ - Detailed workflow analysis showing:
- Condition fields used in workflow triggers
- Fields updated by workflows
- Cross-module actions (workflows that create/update records in other modules)
- External dependencies (webhooks, email notifications)

**5. Field Usage Matrix** ⭐ - **Most useful for impact analysis:**
- See exactly where each field is used
- Which workflows use it (as condition or update)
- Which blueprints require it
- Quickly identify unused fields that can be safely deleted

**6. Automation Chains** ⭐ - Understand workflow cascades:
- Workflows that trigger other workflows
- Cross-module automation flows
- Essential for debugging complex automation

**7. Lookup Relationships** - How modules connect via lookup fields (enhanced with required flag)

**8. Formula Fields** - All formula fields with their expressions and return types

**9. Mandatory Fields** - Required and system-mandatory fields by module

**10. Cross-Module Dependencies** ⭐ - Complete interconnection map:
- Which modules reference each other
- Lookup relationships
- Workflow dependencies between modules
- Critical for migration planning

**11. Summary** - High-level statistics dashboard showing counts per module

**Pro Tips:**
- Use **Field Usage Matrix** to find unused fields before cleanup
- Check **Workflow Dependencies** before modifying or deleting fields
- Review **Automation Chains** to understand why multiple workflows fire
- Use **Cross-Module Dependencies** for migration planning
- Use Excel's filter and sort features to analyze the data!

---

**That's it!** If you've followed Steps 1-3 above, you're done. The output files will be in this folder.

Good luck! 🎉
