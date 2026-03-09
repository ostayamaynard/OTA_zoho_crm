#!/usr/bin/env python3
"""
Fix import statements in moved scripts after reorganization.

After moving scripts to subdirectories, their sys.path setup needs adjustment.
"""

import re
from pathlib import Path

TOOLS_ROOT = Path(__file__).resolve().parents[1]

# Files that were moved and need import fixes
FILES_TO_FIX = [
    "generators/generate_ai_kb.py",
    "generators/generate_module_docs.py",
    "generators/add_workflow_urls.py",
    "validators/validate_data.py",
    "validators/verify_extra_workflows.py",
    "processing/compare_exports.py",
    "processing/build_crm_data_model.py",
    "processing/extract_workflows.py",
    "processing/extract_model_details.py",
]

# Old pattern: TOOLS_DIR = Path(__file__).resolve().parent
# New pattern: TOOLS_DIR = Path(__file__).resolve().parents[1]  # Get tools/ dir

def fix_file(file_path: Path) -> bool:
    """Fix imports in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False
    
    original_content = content
    
    # Fix TOOLS_DIR assignment - change .parent to .parents[1] for subdirectory scripts
    # Only if it's currently using .parent (not already .parents[1] or .parents[2])
    pattern = r'TOOLS_DIR = Path\(__file__\)\.resolve\(\)\.parent\b(?!\s*\.parent)'
    if re.search(pattern, content):
        content = re.sub(
            pattern,
            'TOOLS_DIR = Path(__file__).resolve().parents[1]  # tools/ directory',
            content
        )
        print(f"✅ Fixed TOOLS_DIR in {file_path.name}")
    
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return False
    else:
        print(f"ℹ️  No changes needed for {file_path.name}")
    
    return False

def main():
    print("=" * 70)
    print("Fix Imports After Script Reorganization")
    print("=" * 70)
    print()
    
    fixed_count = 0
    for file_rel_path in FILES_TO_FIX:
        file_path = TOOLS_ROOT / file_rel_path
        if file_path.exists():
            if fix_file(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  File not found: {file_rel_path}")
    
    print()
    print("=" * 70)
    print(f"Fixed {fixed_count} file(s)")
    print("=" * 70)

if __name__ == "__main__":
    main()
