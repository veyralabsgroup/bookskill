---
description: "Every way to run /bookskill: a single file, a folder, a glob, or a list of paths, with extraction modes, skill naming, and worked command examples."
seo_title: "Usage - Convert a Book, Folder, or Glob into an Agent Skill"
---

## 🚀 Usage

```
/bookskill <path-to-document-folder-or-glob>... [skill-name-slug]
```

Supported document formats: PDF, EPUB, DOCX, TXT, Markdown, reStructuredText, AsciiDoc, HTML, RTF, MOBI/AZW/AZW3.

**Examples:**

```bash
# Process several files together into a unified skill
/bookskill ~/papers/paper1.pdf ~/notes/export.txt unified-research

# Process all supported files in a folder together
/bookskill ~/workspace/project-docs/ project-knowledge

# Process files matching a glob pattern
/bookskill "~/books/*.epub" my-library

# Update/fold new material into an existing skill folder
/bookskill ~/articles/new-paper.pdf ~/.claude/skills/project-knowledge
```

After the skill is created, use it like any other agent skill:

```bash
/designing-data-intensive-apps                  # load core mental models
/designing-data-intensive-apps replication      # find and explain a topic
/designing-data-intensive-apps ch05             # dive into chapter 5
/designing-data-intensive-apps "what chapters do you have?"
```

In GitHub Copilot CLI you may need to run `/skills reload` after the file is written so the new skill appears in `/skills list`. Claude Code and Amp pick it up on the next session.

## Update / fold-in

Pointing `/bookskill` at an existing skill folder (or a slug that already exists in `SKILLS_HOME`) triggers Mode 4 instead of a fresh conversion — new sources get folded into the existing chapters, glossary, patterns, and cheatsheet rather than replacing them.

Every conversion writes a `.bookskill-cache.json` manifest next to the skill's `SKILL.md`, hashing each chapter. On an update run, `tools/chapter_diff.py` diffs the freshly extracted text against that manifest **before** any chapter file is touched, so the agent only regenerates chapters that actually changed:

```bash
python3 tools/chapter_diff.py <extracted-text> ~/.claude/skills/my-book/.bookskill-cache.json
```

Chapters matched by heading and untouched since the last run are skipped outright — fixing a typo in one chapter of a 400-page book costs one chapter's worth of regeneration, not the whole skill.

---


---

[← Back to the README](../README.md)
