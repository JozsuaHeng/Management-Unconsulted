# CLAUDE.md

## What this project is

`claude-skills-library` is a personal library of **Claude Skills** built for
management consulting and business-owner work. It is the source of truth —
each skill lives here in `skills/<skill-name>/SKILL.md` (plus any
`references/` files), gets edited and version-controlled here, and is then
copied into `~/.claude/skills/` to actually become active in Claude Code.

If you edit a skill, edit it **here first**, then re-copy it to
`~/.claude/skills/` (see `GUIDE.md` for the copy command) — don't edit the
live copy directly or the two will drift apart.

## Structure

- `GUIDE.md` — how Claude Skills work and how to use this library (start here)
- `catalog.md` — a table of every skill in this library: name, category,
  one-line description, and when it triggers
- `skills/<skill-name>/SKILL.md` — each individual skill
- `skills/<skill-name>/references/` — deeper methodology notes some skills
  bundle (only loaded by Claude when actually needed, so they don't cost
  context unless used)

## About the owner

Jozsua works in management consulting and also runs Golden Island Cruises
(a phinisi boat charter business in Lombok, Indonesia — see the
`golden-island-cruises/` project elsewhere on this shelf). These skills are
written to be useful for both: client-facing consulting deliverables, and
running GIC day to day. Jozsua is a beginner with coding — SKILL.md files
are plain Markdown, not code, so this project stays approachable, but if
scripts are ever added to a skill, keep them simple and explain what they do.

## Conventions for skills in this library

- Every skill's `description` field must say **both** what it does and
  **when** Claude should use it — that field is literally what Claude
  matches a request against, so a vague description means the skill never
  triggers.
- Keep each `SKILL.md` body under ~500 lines. Longer methodology goes in a
  `references/*.md` file, only loaded when the skill actually needs it.
- No skill should fabricate numbers (market sizes, financial figures,
  competitor data). Every skill that produces analysis must label claims as
  fact (sourced), estimate (stated assumption), or open question — never
  state a made-up number as if it were known.
