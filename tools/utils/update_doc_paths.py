#!/usr/bin/env python3
"""
Update documentation files with new directory structure paths.

This script performs safe find/replace operations to update old paths
to the new reorganized structure.

Usage:
    python3 tools/utils/update_doc_paths.py --dry-run  # Preview changes
    python3 tools/utils/update_doc_paths.py --apply    # Apply changes
"""

import argparse
import re
from pathlib import Path
from typing import List, Tuple

# Define path replacements
PATH_REPLACEMENTS = [
    # Tools reorganization
    ("tools/data_processing/", "tools/processing/"),
    ("tools/inspection/", "tools/validators/"),
    ("tools/generate_ai_kb.py", "tools/generators/generate_ai_kb.py"),
    ("tools/generate_module_docs.py", "tools/generators/generate_module_docs.py"),
    ("tools/add_workflow_urls.py", "tools/generators/add_workflow_urls.py"),
    ("tools/compare_exports.py", "tools/processing/compare_exports.py"),
    ("tools/audit_mermaid", "tools/validators/audit_mermaid"),
    ("tools/verify_extra", "tools/validators/verify_extra"),
    
    # Export location
    ("tools/exports/zoho_export_package/", "data/exports/"),
    
    # SOPs directory
    ("SOPs/processed_sops/", "sops/processed/"),
    ("SOPs/raw_sops/", "sops/raw/"),
    ("SOPs/", "sops/"),
]

# Files to update (expand as needed)
FILES_TO_UPDATE = [
    "README.md",
    "GLOSSARY.md",
    "LOGIC_INDEX.md",
    "models/CRM_DATA_MODEL_README.md",
    "docs/DATA-FLOW-DOCUMENTATION-ROADMAP.md",
    "docs/workflow-mapping-guide.md",
    "docs/module-documentation-standard.md",
]

# Files to EXCLUDE (auto-generated or should not be touched)
EXCLUDE_PATTERNS = [
    "ai_kb/*.md",  # Auto-generated, will be fixed on next generation
    "modules/*/docs/*.md",  # Module docs are auto-generated
    "reports/*.md",  # Reports are auto-generated
]


def should_exclude(file_path: Path, base_dir: Path) -> bool:
    """Check if file matches exclusion patterns."""
    rel_path = str(file_path.relative_to(base_dir))
    for pattern in EXCLUDE_PATTERNS:
        if Path(rel_path).match(pattern):
            return True
    return False


def update_file_paths(file_path: Path, replacements: List[Tuple[str, str]], dry_run: bool = True) -> Tuple[bool, List[str]]:
    """
    Update paths in a single file.
    
    Returns:
        (changed, changes_made) - Whether file was changed and list of changes
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False, []
    
    original_content = content
    changes_made = []
    
    for old_path, new_path in replacements:
        if old_path in content:
            # Count occurrences
            count = content.count(old_path)
            content = content.replace(old_path, new_path)
            changes_made.append(f"  • {old_path} → {new_path} ({count} occurrence{'s' if count > 1 else ''})")
    
    if content != original_content:
        if not dry_run:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True, changes_made
            except Exception as e:
                print(f"❌ Error writing {file_path}: {e}")
                return False, []
        else:
            return True, changes_made
    
    return False, []


def main():
    parser = argparse.ArgumentParser(
        description="Update documentation with new directory structure paths"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Preview changes without applying (default)"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes to files"
    )
    parser.add_argument(
        "--include-sops",
        action="store_true",
        help="Include sops/ directory files (needs manual review)"
    )
    args = parser.parse_args()
    
    # Determine if we're applying changes
    dry_run = not args.apply
    
    # Get repository root
    repo_root = Path(__file__).resolve().parents[2]
    
    print("=" * 70)
    print("Documentation Path Updater")
    print("=" * 70)
    print(f"Repository: {repo_root}")
    print(f"Mode: {'DRY RUN (preview only)' if dry_run else 'APPLY CHANGES'}")
    print("=" * 70)
    print()
    
    # Build file list
    files_to_process = []
    for file_pattern in FILES_TO_UPDATE:
        file_path = repo_root / file_pattern
        if file_path.exists():
            files_to_process.append(file_path)
        else:
            print(f"⚠️  File not found: {file_pattern}")
    
    # Add sops files if requested
    if args.include_sops:
        print("⚠️  Including sops/ directory (manual review recommended)")
        sops_files = list((repo_root / "sops").rglob("*.md"))
        files_to_process.extend(sops_files)
    
    # Process files
    total_files = 0
    changed_files = 0
    
    for file_path in files_to_process:
        if should_exclude(file_path, repo_root):
            continue
        
        total_files += 1
        changed, changes = update_file_paths(file_path, PATH_REPLACEMENTS, dry_run)
        
        if changed:
            changed_files += 1
            rel_path = file_path.relative_to(repo_root)
            print(f"{'📝' if dry_run else '✅'} {rel_path}")
            for change in changes:
                print(change)
            print()
    
    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Files processed: {total_files}")
    print(f"Files {'that would be' if dry_run else ''} changed: {changed_files}")
    print(f"Files unchanged: {total_files - changed_files}")
    print()
    
    if dry_run and changed_files > 0:
        print("💡 To apply these changes, run:")
        print("   python3 tools/utils/update_doc_paths.py --apply")
        print()
        print("💡 To include sops/ directory (needs review):")
        print("   python3 tools/utils/update_doc_paths.py --apply --include-sops")
    elif changed_files > 0:
        print("✅ Changes applied successfully!")
        print()
        print("⚠️  NOTE: Auto-generated files (ai_kb/*.md) will be fixed")
        print("   automatically the next time you run:")
        print("   python3 tools/generators/generate_ai_kb.py")
    else:
        print("✅ All files are up to date!")
    
    print()


if __name__ == "__main__":
    main()
