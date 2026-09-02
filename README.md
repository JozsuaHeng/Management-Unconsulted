# Vantage Point

A browsable library of **50 Claude Skills for management consulting and
running a business** — strategic analysis, client deliverables, change
and program management, project methodologies (PRINCE2, PMBOK, Agile,
Waterfall, BABOK), research, financial/operational tools, and day-to-day
business-owner tasks.

Each skill is a self-contained package Claude can actually use — not a
slide deck or a template that sits in a folder, but something you
install once and then Claude applies automatically when it's relevant to
what you're asking.

## What's here

- **`index.html` / `style.css` / `app.js`** — the site itself: an
  animated radial mindmap of all 50 skills grouped into 7 categories,
  with search, a "How to use this" walkthrough for non-technical
  readers, and a download link for every skill.
- **`dl/`** — pre-built `.zip` downloads: one per skill, one per
  category, and one bundling all 50.
- **`build.py`** — regenerates the site from the underlying skill
  content (see "Rebuilding" below).

## Using a skill

1. Download the skill (or the whole set) from the site.
2. Unzip it.
3. Drop the resulting folder into `~/.claude/skills/` (Claude Code) or
   upload it via Settings → Customize → Skills (claude.ai / Claude
   Desktop app, requires the Code execution capability turned on).

The site's own **"How to use this"** button walks through this
step-by-step for readers who haven't used Skills before, including what
a Skill actually is and where each of the three "Claudes" (claude.ai,
the Desktop app, Claude Code) looks for them.

## Rebuilding the site

The actual skill content (`SKILL.md` + reference files) lives in a
sibling `claude-skills-library/` folder that is **not part of this
repo** — it's a separate project in the same local workspace. If you
have that folder checked out as a sibling directory, you can regenerate
`index.html` and `dl/*.zip` after editing a skill:

```bash
python3 build.py
```

This only rewrites the mindmap and skill-content sections of
`index.html` (marked by HTML comments) — everything else (styling,
animation, the guide modal) is untouched.

Without that sibling folder present, `build.py` won't run — but the
already-built `index.html` and `dl/*.zip` in this repo work fine as a
static site on their own.

## License

No license file yet — treat as "all rights reserved" unless/until one is
added.
