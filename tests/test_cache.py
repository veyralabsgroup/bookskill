"""Tests for bookskill/cache.py — incremental chapter hashing and diffing."""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from bookskill.cache import build_manifest, diff_manifest, split_chapters

NUMBERED_BOOK = """Title Page

Chapter 1
Foundations text here.

Chapter 2
Mechanisms text here.

Chapter 3
Anti-patterns text here.
"""

NO_HEADINGS_DOC = "Just a short spec with no chapter markers at all.\n"


def test_split_chapters_numbered_book():
    segments = split_chapters(NUMBERED_BOOK)
    assert [s["heading"] for s in segments] == ["Chapter 1", "Chapter 2", "Chapter 3"]
    assert "Foundations" in segments[0]["text"]
    assert "Mechanisms" in segments[1]["text"]
    # Preamble before the first heading is dropped, not silently glued onto ch1.
    assert "Title Page" not in segments[0]["text"]


def test_split_chapters_no_headings_falls_back_to_one_segment():
    segments = split_chapters(NO_HEADINGS_DOC)
    assert len(segments) == 1
    assert segments[0]["heading"] == ""
    assert segments[0]["text"] == NO_HEADINGS_DOC


def test_diff_manifest_first_run_is_all_added():
    new = build_manifest(NUMBERED_BOOK)
    diff = diff_manifest({"chapters": []}, new)
    assert diff == {"unchanged": [], "changed": [], "added": [0, 1, 2], "removed": []}


def test_diff_manifest_unchanged_source_is_all_unchanged():
    manifest = build_manifest(NUMBERED_BOOK)
    diff = diff_manifest(manifest, manifest)
    assert diff["unchanged"] == [0, 1, 2]
    assert not diff["changed"] and not diff["added"] and not diff["removed"]


def test_diff_manifest_detects_a_single_edited_chapter():
    old = build_manifest(NUMBERED_BOOK)
    edited = NUMBERED_BOOK.replace("Mechanisms text here.", "Mechanisms text, revised.")
    new = build_manifest(edited)
    diff = diff_manifest(old, new)
    assert diff == {"unchanged": [0, 2], "changed": [1], "added": [], "removed": []}


def test_diff_manifest_detects_added_and_removed_chapters():
    old = build_manifest(NUMBERED_BOOK)
    shorter = NUMBERED_BOOK.replace("Chapter 3\nAnti-patterns text here.\n", "")
    with_new_chapter = shorter + "Chapter 4\nA brand new chapter.\n"
    new = build_manifest(with_new_chapter)
    diff = diff_manifest(old, new)
    assert diff["unchanged"] == [0, 1]
    assert diff["added"] == [2]  # Chapter 4, matched by heading, not position
    assert diff["removed"] == [2]  # old Chapter 3, no longer present
