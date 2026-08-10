"""Incremental chapter cache: hash each chapter so a re-run on an updated
source can tell the agent which chapters actually changed, instead of
re-generating the whole skill every time.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from bookskill.utils import chapter_heading_lines

CACHE_FILENAME = ".bookskill-cache.json"


def split_chapters(text: str) -> list[dict]:
    """Split text into chapter segments at detected chapter-heading lines.

    Falls back to a single segment (heading="") when no numbered chapter
    headings are found — e.g. short docs, specs, or structural-only sources.
    """
    lines = text.splitlines()
    boundaries = chapter_heading_lines(text)
    if not boundaries:
        return [{"heading": "", "text": text}]
    ends = boundaries[1:] + [len(lines)]
    return [
        {"heading": lines[start].strip(), "text": "\n".join(lines[start:end])}
        for start, end in zip(boundaries, ends)
    ]


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_manifest(text: str) -> dict:
    """Build a {chapters: [{heading, hash}]} manifest for extracted text."""
    return {
        "chapters": [
            {"heading": seg["heading"], "hash": _hash(seg["text"])}
            for seg in split_chapters(text)
        ]
    }


def diff_manifest(old: dict, new: dict) -> dict:
    """Compare two manifests, matching chapters by heading (not position) so
    an inserted or reordered chapter doesn't shift every later index into
    "changed". Returns 0-indexed positions into `new["chapters"]`, except for
    "removed" which indexes into `old["chapters"]`.
    """
    old_chapters = old.get("chapters", [])
    by_heading: dict[str, list[tuple[int, str]]] = {}
    for i, ch in enumerate(old_chapters):
        by_heading.setdefault(ch["heading"], []).append((i, ch["hash"]))

    result = {"unchanged": [], "changed": [], "added": [], "removed": []}
    matched_old = set()
    for i, ch in enumerate(new.get("chapters", [])):
        candidates = by_heading.get(ch["heading"], [])
        match = next((c for c in candidates if c[0] not in matched_old), None)
        if match is None:
            result["added"].append(i)
        else:
            matched_old.add(match[0])
            bucket = "unchanged" if match[1] == ch["hash"] else "changed"
            result[bucket].append(i)
    result["removed"] = [i for i in range(len(old_chapters)) if i not in matched_old]
    return result


def load_manifest(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(path: Path, manifest: dict) -> None:
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
