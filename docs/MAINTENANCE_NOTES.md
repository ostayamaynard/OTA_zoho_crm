# Repository Maintenance Notes

This document contains notes for maintaining the repository, including when to use automation vs AI assistance.

---

## Path Updates & Reorganization

### When Directory Structure Changes

**What can be automated:**
- Path replacements in documentation files
- Simple find/replace operations
- Bulk updates across multiple files

**Use the script:**
```bash
# Preview changes
python3 tools/utils/update_doc_paths.py --dry-run

# Apply changes
python3 tools/utils/update_doc_paths.py --apply

# Include sops/ directory (needs review)
python3 tools/utils/update_doc_paths.py --apply --include-sops
```

**Edit the script to add new path mappings:**
- Open `tools/utils/update_doc_paths.py`
- Add new entries to `PATH_REPLACEMENTS` list
- Add files to `FILES_TO_UPDATE` list if needed

### When AI Assistance is Needed

**Use Claude Code/AI for:**

1. **Contextual Updates**
   - When paths need context-aware changes
   - When examples in docs need updating with new patterns
   - When comments in code need rephrasing

2. **Complex Reorganization**
   - Moving content between files
   - Restructuring documentation sections
   - Updating cross-references that have changed meaning

3. **Content Generation**
   - Writing new READMEs for new directories
   - Creating comprehensive developer guides
   - Generating migration guides

4. **Code Refactoring**
   - Updating import statements across Python files
   - Renaming functions/classes and updating callers
   - Refactoring with logic changes

### Hybrid Approach

**Best Practice:**
1. Use script for bulk path replacements
2. Use AI to review special cases (sops/, examples, historical docs)
3. Use AI to generate new documentation
4. Use script to maintain consistency going forward

---

## Auto-Generated vs Manual Files

### Auto-Generated (Updated by Scripts)

**These will fix themselves on next generation - DON'T manually edit:**
- `ai_kb/*.md` - Run `python3 tools/generators/generate_ai_kb.py`
- `modules/*/docs/*.md` - Run `python3 tools/generators/generate_module_docs.py`
- `reports/*.md` - Run `python3 tools/processing/compare_exports.py`
- `models/CRM_DATA_MODEL*.md` - Run `python3 tools/processing/build_crm_data_model.py`

**To update these:** Just run the pipeline
```bash
python3 tools/update_pipeline.py --apply
```

### Manual Files (Require Human/AI Review)

**These need careful review when updating:**
- `README.md` - Repository introduction
- `ARCHITECTURE.md` - System architecture
- `GLOSSARY.md` - Business terminology
- `LOGIC_INDEX.md` - System logic overview
- `sops/**/*.md` - Standard Operating Procedures
- `docs/*.md` - General documentation

**For these files:**
1. Review each change in context
2. Consider historical references (may be intentional)
3. Update examples to match new structure
4. Verify cross-references still work

---

## Using Claude Code for Updates

### When to Use Claude Code

**Recommended scenarios:**
1. Large-scale reorganization (like the 2026-01-08 restructure)
2. Writing new comprehensive documentation
3. Complex path updates with contextual changes
4. Reviewing SOP files for accuracy after structure changes

### How to Use Claude Code

**For documentation updates:**
```
Prompt: "Update all documentation files to reflect the new directory 
structure. The tools/ directory has been reorganized with these changes:
- tools/data_processing/ → tools/processing/
- tools/inspection/ → tools/validators/
- Loose scripts → tools/generators/

Review each file for context and update paths, examples, and explanations."
```

**For creating new docs:**
```
Prompt: "Create a comprehensive README.md for the tools/ directory that 
explains each subdirectory, provides usage examples, and includes workflow 
sequences for common developer tasks."
```

**For reviewing special cases:**
```
Prompt: "Review the sops/ directory documentation and update path references 
where appropriate. Some references may be intentionally historical - use 
judgment to determine which to update."
```

---

## Future Reorganization Checklist

If you reorganize the repository again:

### Step 1: Plan the Changes
- [ ] Document old → new path mappings
- [ ] Identify which files are auto-generated (can regenerate)
- [ ] Identify which files need manual review

### Step 2: Update Code First
- [ ] Move/rename directories
- [ ] Update Python import statements
- [ ] Update path constants in code (like `file_discovery.py`)
- [ ] Test that scripts still run

### Step 3: Update Documentation (Automated)
- [ ] Edit `tools/utils/update_doc_paths.py` with new mappings
- [ ] Run in dry-run mode to preview
- [ ] Review the preview output
- [ ] Run with `--apply` to update files

### Step 4: Regenerate Auto-Generated Docs
- [ ] Run `python3 tools/update_pipeline.py --apply`
- [ ] This regenerates ai_kb, module docs, reports, etc.

### Step 5: Manual Review (Use AI)
- [ ] Review sops/ directory with Claude Code
- [ ] Update examples in documentation
- [ ] Verify cross-references
- [ ] Update any historical context as needed

### Step 6: Create Developer Guide
- [ ] If new directories created, write README for them
- [ ] Update main README.md with new structure
- [ ] Update tools/README.md with new tool locations

### Step 7: Verify
- [ ] Test all scripts run correctly
- [ ] Check git status - review all changes
- [ ] Test a full pipeline run
- [ ] Commit changes

---

## Script Maintenance

### Keeping `update_doc_paths.py` Current

**When to update the script:**
- After each major reorganization
- When you find path patterns not covered
- When you add new types of documentation files

**How to update:**
1. Open `tools/utils/update_doc_paths.py`
2. Add new mappings to `PATH_REPLACEMENTS`
3. Add new files to `FILES_TO_UPDATE`
4. Test with `--dry-run` first
5. Document the changes in this file

**Example addition:**
```python
PATH_REPLACEMENTS = [
    # ... existing replacements ...
    ("old/path/pattern/", "new/path/pattern/"),
]

FILES_TO_UPDATE = [
    # ... existing files ...
    "new_doc_file.md",
]
```

---

## Common Pitfalls

### ❌ Don't Do This

1. **Don't manually edit auto-generated files**
   - They'll be overwritten on next generation
   - Edit the generators instead

2. **Don't bulk replace without context**
   - Some references may be intentionally historical
   - SOPs may document old processes
   - Examples may show evolution over time

3. **Don't forget to regenerate after code changes**
   - Run the pipeline after path updates
   - Auto-generated files won't fix themselves

### ✅ Do This Instead

1. **Use the script for bulk safe replacements**
2. **Use AI for contextual review**
3. **Regenerate auto-generated docs**
4. **Test before committing**

---

## Emergency Rollback

If documentation updates break something:

### Quick Rollback
```bash
# Revert all changes
git checkout HEAD -- .

# Or revert specific files
git checkout HEAD -- README.md ARCHITECTURE.md

# Or revert to specific commit
git reset --hard <commit-hash>
```

### Selective Recovery
```bash
# See what changed
git diff HEAD

# Restore specific sections
git checkout HEAD -- path/to/file.md
```

---

## Questions to Ask Before Updates

Before updating documentation after reorganization:

1. **Is this path reference factual or historical?**
   - Factual → Update it
   - Historical → May keep as-is with note

2. **Is this file auto-generated?**
   - Yes → Don't manually edit, regenerate instead
   - No → Safe to edit

3. **Does this path appear in multiple contexts?**
   - Same context everywhere → Script can handle
   - Different contexts → May need AI review

4. **Is this example or instruction?**
   - Example → Update to match new structure
   - Historical documentation → May keep with context

---

## Contact & Support

**For questions about maintenance:**
1. Check this file first
2. Review `tools/README.md` for tool usage
3. Check `docs/UPDATE_DEPENDENCIES.md` for update process
4. Use Claude Code for complex analysis

**For large reorganizations:**
- Use Claude Code to plan the changes
- Use scripts for bulk operations  
- Use Claude Code to review special cases
- Document the process for future reference

---

*Last Updated: 2026-01-08*  
*After: tools/ directory reorganization*  
*Created: tools/utils/update_doc_paths.py automation script*
