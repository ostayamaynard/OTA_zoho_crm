#!/usr/bin/env python3
"""
Utilities for locating Zoho export files by date without hardcoded paths.

Primary helpers:
- list_exports(): return all discovered exports sorted newest → oldest
- get_latest_export(): latest export that has both data model and dependencies
- get_latest_two_exports(): latest pair for diffing (new, previous)
- get_export_by_date(date): specific export by YYYY-MM-DD
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re

EXPORT_DIR = Path(__file__).resolve().parents[2] / "data" / "exports"
EXPORT_PATTERN = re.compile(r"zoho-(data-model|dependencies)-(\d{4}-\d{2}-\d{2})\.json$")


@dataclass(frozen=True)
class ExportFiles:
    date: str
    data_model: Optional[Path] = None
    dependencies: Optional[Path] = None

    @property
    def both_present(self) -> bool:
        return self.data_model is not None and self.dependencies is not None

    def ensure_both(self) -> "ExportFiles":
        if not self.both_present:
            missing = []
            if self.data_model is None:
                missing.append("data_model")
            if self.dependencies is None:
                missing.append("dependencies")
            raise FileNotFoundError(f"Missing export files for {self.date}: {', '.join(missing)}")
        return self


def _scan_exports(export_dir: Path) -> Dict[str, ExportFiles]:
    exports: Dict[str, ExportFiles] = {}
    for entry in export_dir.iterdir():
        if not entry.is_file():
            continue
        match = EXPORT_PATTERN.match(entry.name)
        if not match:
            continue
        kind, date = match.group(1), match.group(2)
        existing = exports.get(date, ExportFiles(date=date))
        if kind == "data-model":
            existing = ExportFiles(date=date, data_model=entry, dependencies=existing.dependencies)
        else:
            existing = ExportFiles(date=date, data_model=existing.data_model, dependencies=entry)
        exports[date] = existing
    return exports


def list_exports(export_dir: Path | str | None = None) -> List[ExportFiles]:
    directory = Path(export_dir) if export_dir else EXPORT_DIR
    if not directory.exists():
        raise FileNotFoundError(f"Export directory not found: {directory}")
    exports = _scan_exports(directory)
    return sorted(exports.values(), key=lambda e: e.date, reverse=True)


def get_export_by_date(date: str, export_dir: Path | str | None = None, require_both: bool = True) -> ExportFiles:
    for export in list_exports(export_dir):
        if export.date == date:
            return export.ensure_both() if require_both else export
    raise FileNotFoundError(f"No export found for date {date}")


def get_latest_export(export_dir: Path | str | None = None, require_both: bool = True) -> ExportFiles:
    exports = list_exports(export_dir)
    for export in exports:
        if not require_both or export.both_present:
            return export.ensure_both() if require_both else export
    raise FileNotFoundError("No complete exports (data model + dependencies) found")


def get_latest_two_exports(export_dir: Path | str | None = None, require_both: bool = True) -> Tuple[ExportFiles, ExportFiles]:
    exports = list_exports(export_dir)
    filtered = [e.ensure_both() if require_both else e for e in exports if (not require_both or e.both_present)]
    if len(filtered) < 2:
        raise FileNotFoundError("Fewer than two complete exports available for comparison")
    return filtered[0], filtered[1]


def export_dates(export_dir: Path | str | None = None) -> List[str]:
    return [e.date for e in list_exports(export_dir)]


def export_directory(export_dir: Path | str | None = None) -> Path:
    return Path(export_dir) if export_dir else EXPORT_DIR

