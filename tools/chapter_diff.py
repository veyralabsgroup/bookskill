#!/usr/bin/env python3
"""
chapter_diff.py — incremental re-generation support for the Update / Fold-in
workflow (SKILL.md Mode 4).

On a fresh conversion every chapter is "added". On a re-run against an
updated source, this reports which chapters are unchanged / changed / added /
removed since the manifest was last saved, so the agent only has to
regenerate the chapters that actually changed instead of the whole skill.

Usage:
  python3 tools/chapter_diff.py <extracted-text-file> <manifest-path>

Prints a JSON report to stdout, then updates <manifest-path> with the new
hashes (so the next run diffs against this one). Pass --dry-run to skip the
manifest update (e.g. to preview without committing to the new state).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from bookskill.cache import (  # noqa: E402
    build_manifest,
    diff_manifest,
    load_manifest,
    save_manifest,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text_file", type=Path, help="Freshly extracted full_text.txt")
    parser.add_argument("manifest_path", type=Path, help="Where the chapter-hash manifest lives")
    parser.add_argument("--dry-run", action="store_true", help="Report the diff but don't save the new manifest")
    args = parser.parse_args()

    text = args.text_file.read_text(encoding="utf-8")
    new_manifest = build_manifest(text)
    old_manifest = load_manifest(args.manifest_path)

    if old_manifest is None:
        # First run: nothing to compare against, every chapter is new.
        diff = {"unchanged": [], "changed": [], "added": list(range(len(new_manifest["chapters"]))), "removed": []}
    else:
        diff = diff_manifest(old_manifest, new_manifest)

    report = {
        "diff": diff,
        "chapters": [
            {"index": i, "heading": ch["heading"]}
            for i, ch in enumerate(new_manifest["chapters"])
        ],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if not args.dry_run:
        save_manifest(args.manifest_path, new_manifest)


if __name__ == "__main__":
    main()
