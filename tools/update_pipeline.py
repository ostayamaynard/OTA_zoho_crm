#!/usr/bin/env python3
"""
End-to-end update driver for Zoho CRM exports.

Steps (unless skipped):
1) Compare exports → writes reports/export_diff_<new>_vs_<old>.{json,md}
2) Build central model → models/CRM_DATA_MODEL.{json,md}
3) Generate AI Knowledge Base → ai_kb/*.md (5 files, 147 KB) [Added: 2026-01-08]
4) Extract workflows summary
5) Generate module docs (all modules)
6) Refresh Mermaid diagrams
7) Validate data integrity
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
import sys

TOOLS_DIR = Path(__file__).resolve().parent
ROOT_DIR = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export, get_latest_two_exports  # noqa: E402

REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Zoho export processing pipeline")
    parser.add_argument("--date", help="Export date to process (YYYY-MM-DD). Defaults to latest export.")
    parser.add_argument("--previous-date", help="Previous export date for diff (default: auto-select previous)")
    parser.add_argument("--apply", action="store_true", help="Execute steps. If omitted, runs in dry-run mode.")
    parser.add_argument("--skip-diagrams", action="store_true", help="Skip Mermaid regeneration step")
    parser.add_argument("--skip-docs", action="store_true", help="Skip module docs generation")
    parser.add_argument("--skip-workflows", action="store_true", help="Skip workflow extraction summary")
    parser.add_argument("--skip-validate", action="store_true", help="Skip validation pass")
    parser.add_argument("--skip-manual-review", action="store_true", help="Skip generating manual review checklist")
    parser.add_argument("--skip-ai-kb", action="store_true", help="Skip AI Knowledge Base generation")
    return parser.parse_args()


def run_step(label: str, cmd: list[str], dry_run: bool):
    print(f"\n[{label}] {' '.join(cmd)}")
    if dry_run:
        print("  (dry run)")
        return
    subprocess.run(cmd, check=True)


def write_manual_review(diff_json_path: Path, new_date: str, old_date: str):
    """
    Generate a manual review checklist for curated data files based on module changes.
    """
    if not diff_json_path.exists():
        print(f"[manual_review] Diff JSON not found at {diff_json_path}; skipping checklist.")
        return

    diff = json.loads(diff_json_path.read_text())
    modules = set(diff.get("modules", {}).get("modified", {}).keys())
    modules.update(diff.get("modules", {}).get("added", []))
    modules.update(diff.get("modules", {}).get("removed", []))

    if not modules:
        print("[manual_review] No module changes detected; no checklist generated.")
        return

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    outfile = REPORTS_DIR / f"manual_review_{new_date}_vs_{old_date}.md"

    lines = []
    lines.append(f"# Manual Review Checklist ({new_date} vs {old_date})")
    lines.append("")
    lines.append("Curated files are not auto-updated. Review/update as needed for modules with changes.")
    lines.append("")
    for module in sorted(modules):
        mod_slug = module.lower()
        lines.append(f"## {module}")
        lines.append(f"- Check `modules/{mod_slug}/data/customer-journey-*.json` (journey narratives, workflow references)")
        lines.append(f"- Check `modules/{mod_slug}/data/*-stages-kanban.json` if stages/picklists changed")
        lines.append("- Update SOPs or data-flow docs if the business flow changed")
        lines.append("")

    outfile.write_text("\n".join(lines) + "\n")
    print(f"[manual_review] Wrote checklist to {outfile}")


def main():
    args = parse_args()
    dry_run = not args.apply

    export_dir = export_directory()
    new_export = (
        get_export_by_date(args.date, export_dir).ensure_both()
        if args.date
        else get_latest_export(export_dir).ensure_both()
    )
    if args.previous_date:
        old_export = get_export_by_date(args.previous_date, export_dir).ensure_both()
    else:
        older = get_latest_two_exports(export_dir)[1]
        old_export = older.ensure_both()

    print("=" * 80)
    print("ZOHO CRM EXPORT PIPELINE")
    print("=" * 80)
    print(f"New export: {new_export.data_model.name}")
    print(f"Old export: {old_export.data_model.name}")
    print(f"Mode: {'APPLY' if not dry_run else 'DRY RUN'}")

    commands = [
        (
            "diff",
            [
                sys.executable,
                str(TOOLS_DIR / "compare_exports.py"),
                "--new-date",
                new_export.date,
                "--old-date",
                old_export.date,
            ],
        ),
        (
            "build_model",
            [
                sys.executable,
                str(TOOLS_DIR / "data_processing" / "build_crm_data_model.py"),
                "--date",
                new_export.date,
            ],
        ),
    ]

    diff_json_path = REPORTS_DIR / f"export_diff_{new_export.date}_vs_{old_export.date}.json"

    if not args.skip_ai_kb:
        commands.append(
            (
                "ai_kb",
                [
                    sys.executable,
                    str(TOOLS_DIR / "generate_ai_kb.py"),
                    "--date",
                    new_export.date,
                    "--diff-json",
                    str(diff_json_path),
                ],
            )
        )

    if not args.skip_workflows:
        commands.append(
            (
                "extract_workflows",
                [
                    sys.executable,
                    str(TOOLS_DIR / "data_processing" / "extract_workflows.py"),
                    "--date",
                    new_export.date,
                ],
            )
        )

    if not args.skip_docs:
        commands.append(
            (
                "module_docs",
                [
                    sys.executable,
                    str(TOOLS_DIR / "generate_module_docs.py"),
                    "--date",
                    new_export.date,
                ],
            )
        )

    if not args.skip_diagrams:
        commands.append(
            (
                "mermaid",
                [
                    sys.executable,
                    str(TOOLS_DIR / "kanban" / "json_to_mermaid.py"),
                ],
            )
        )

    if not args.skip_validate:
        commands.append(
            (
                "validate",
                [
                    sys.executable,
                    str(TOOLS_DIR / "inspection" / "validate_data.py"),
                    "--date",
                    new_export.date,
                ],
            )
        )

    for label, cmd in commands:
        run_step(label, cmd, dry_run)

    # Manual review checklist (non-destructive)
    if not args.skip_manual_review and not dry_run:
        write_manual_review(diff_json_path, new_export.date, old_export.date)

    print("\nPipeline complete." if not dry_run else "\nDry run complete. Re-run with --apply to execute.")


if __name__ == "__main__":
    main()
