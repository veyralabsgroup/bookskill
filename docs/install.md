---
description: "Install bookskill as an agent skill for Claude Code, GitHub Copilot CLI and Amp, or as a standalone pip CLI. Every host path and optional extractor covered."
seo_title: "Install bookskill - Claude Code, Copilot CLI, Amp, or pip"
---

## 📥 Install

> **Two ways to use it, do not confuse them:**
> - **As an agent skill** (the `/bookskill` command in Claude Code, Copilot CLI, or Amp) → **`git clone` into your skills folder** (below). This is what gives you the slash command and the full convert-a-book flow.
> - **As a standalone CLI** (just the text extractor) → `pip install bookskill`, then `bookskill --help`. This does **not** register the agent skill; it only installs the extraction engine. See [the CLI section](#standalone-cli-pip).

The skill follows the open [Agent Skills](https://github.com/agentskills/agentskills) standard, so a single install works for any compatible host.

**GitHub Copilot CLI** (personal skill):

```bash
git clone https://github.com/veyralabsgroup/bookskill.git ~/.copilot/skills/bookskill
# then, in a `copilot` session:
/skills reload
/skills info bookskill
```

Or the cross-agent path that Copilot CLI and Amp both discover:

```bash
git clone https://github.com/veyralabsgroup/bookskill.git ~/.agents/skills/bookskill
```

**Claude Code**:

Copy this into your Claude Code session:

```
Install bookskill: https://raw.githubusercontent.com/veyralabsgroup/bookskill/master/SKILL.md
```

Or manually using standard `git clone` (ensures modular engine files are fetched correctly):

```bash
git clone https://github.com/veyralabsgroup/bookskill.git ~/.claude/skills/bookskill
```

Then in any agent session:

```bash
/bookskill ~/path/to/your-book.pdf
# or
/bookskill ~/path/to/your-book.epub
```

### Standalone CLI (pip)

`pip install bookskill` is a **separate, optional** path. It installs only the
text-extraction engine as a CLI, for scripting or to grab the optional extractors;
it does **not** register the `/bookskill` agent skill (use the `git clone` above
for that).

```bash
pip install "bookskill[pdf,epub,docx]"   # engine + optional extractors
bookskill ~/path/to/book.pdf --mode text  # or: python -m bookskill ...
bookskill --check                          # report which extractors are installed
```

---


---

[← Back to the README](../README.md)
