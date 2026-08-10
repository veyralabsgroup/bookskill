---
description: "Turn any book, PDF or EPUB into a structured agent skill for Claude Code, GitHub Copilot CLI and Amp. Named frameworks and decision rules, loaded on demand."
seo_title: "bookskill - Turn Any Book Into an AI Agent Skill"
hide:
  - navigation
  - toc
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "bookskill",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Linux, macOS, Windows",
  "description": "Converts books and documents (PDF, EPUB, DOCX, HTML, Markdown, RTF, MOBI/AZW) into structured, on-demand agent skills for Claude Code, GitHub Copilot CLI and Amp.",
  "url": "https://veyralabsgroup.github.io/bookskill/",
  "codeRepository": "https://github.com/veyralabsgroup/bookskill",
  "license": "https://opensource.org/licenses/MIT",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
  "author": { "@type": "Organization", "name": "VeyraLabs", "url": "https://github.com/veyralabsgroup" }
}
</script>

# bookskill

<p style="font-size: 1.25rem; max-width: 42rem;">
Turn any book or document into a structured, on-demand agent skill — named frameworks, decision rules, and anti-patterns. <strong>Structure, not a summary.</strong>
</p>

[Get started](guide.md){ .md-button .md-button--primary }
[Skill reference](skill-reference.md){ .md-button }
[GitHub](https://github.com/veyralabsgroup/bookskill){ .md-button }

---

## Why bookskill

<div class="grid cards" markdown>

-   :material-file-document-multiple:{ .lg .middle } __Multi-format__

    ---

    PDF, EPUB, DOCX, HTML, Markdown, RTF, MOBI/AZW (via Calibre). Extraction runs
    locally with graceful stdlib fallbacks — no upload, no lock-in.

-   :material-brain:{ .lg .middle } __Structure, not summaries__

    ---

    Named frameworks, mental models, decision rules, and anti-patterns — the
    author's toolkit, captured with their exact terms, not a book report.

-   :material-flash:{ .lg .middle } __On-demand chapters__

    ---

    Per-chapter files load only when the topic is relevant, so a 200-page book
    costs tokens proportional to the question, not the page count.

-   :material-robot-happy:{ .lg .middle } __Multi-agent__

    ---

    One `SKILL.md` runs on Claude Code, GitHub Copilot CLI, and Amp through the
    open Agent Skills standard.

</div>

## Install

**As an agent skill** (gives you the `/bookskill` command in Claude Code, Copilot CLI, Amp):

```bash
git clone https://github.com/veyralabsgroup/bookskill.git ~/.claude/skills/bookskill
# then, in your agent session:
/bookskill /path/to/book.pdf [skill-name]
```

**As a standalone CLI** (just the text extractor, optional):

```bash
pip install "bookskill[pdf,epub,docx]"
bookskill /path/to/book.pdf --mode text
```

## Learn more

<div class="grid cards" markdown>

-   :material-sitemap:{ .lg .middle } __[Architecture](architecture.md)__

    ---

    How the deterministic extractor and the spec-driven generator fit together.

-   :material-speedometer:{ .lg .middle } __[Performance](performance.md)__

    ---

    The measured Discovery Loop Tax and real per-conversion token cost.

-   :material-book-open-page-variant:{ .lg .middle } __[Skill Reference](skill-reference.md)__

    ---

    The full `SKILL.md` spec: every step, depth budget, and quality rule.

</div>
