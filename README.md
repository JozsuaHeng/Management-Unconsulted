# Management Unconsulted

Real management consulting frameworks and deliverables — the kind you'd
normally pay a consultant for — packaged as **50 Claude Skills** so
Claude can actually apply them for you, on demand, inside a normal
conversation. No slide decks that sit in a folder, no engagement letter,
no consultant. You ask, Claude reaches for the right framework and does
the work.

The frameworks span **strategic analysis, client-facing deliverables,
change and program management, project methodologies (PRINCE2, PMBOK,
Agile, Waterfall, BABOK), research and competitive intelligence,
financial/operational tools, and day-to-day business-owner tasks** —
grounded partly in real consulting practice (issue trees, ADKAR change
management, the Pyramid Principle) and partly in standard PM/BA
methodology, not generic advice.

## The site: Vantage Point

This repo publishes a browsable catalog of the whole library, called
**Vantage Point** (the name on the live page itself — "Management
Unconsulted" is the project/repo, "Vantage Point" is what the site is
branded as once you're on it, the same way a company and its product can
carry different names). It's built as a large animated, colour-coded
radial mindmap — the whole library visible at a glance, organized into 7
categories radiating from a center hub — with search, click-to-zoom into
any category, a "Read more" popup for each skill's full write-up, and a
"How to use this" flip-card guide written for readers who've never
touched Claude Skills before.

## What's in this repo

- **`index.html` / `style.css` / `app.js`** — the site itself.
- **`dl/`** — pre-built `.zip` downloads: one per skill, one per
  category, and one bundling all 50.
- **`build.py`** — regenerates the site from the underlying skill
  content (see "Rebuilding" below).
- **`favicon.svg`**, **`.nojekyll`** — static-site plumbing for GitHub
  Pages.

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
