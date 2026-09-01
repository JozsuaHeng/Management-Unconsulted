# How to use this library

## What a Claude Skill actually is

A Skill is a folder with a `SKILL.md` file inside it — plain Markdown, no
code required. It has two parts:

1. **A short header** (`name` and `description`) that Claude always has
   loaded, for every skill you have installed, all the time. This costs
   almost nothing — about 100 tokens per skill.
2. **The instructions body** — the actual step-by-step guidance — which
   Claude only reads when your request matches the `description`.

So the `description` field is doing the real work: it's the trigger. If you
ask "help me figure out if this market is worth entering," Claude scans the
descriptions of every installed skill, notices `porters-five-forces` says
*"...use when assessing whether a market or segment is attractive to enter
or defend"*, and reads that skill's full instructions before responding.
You never have to remember skill names or type commands — you just describe
what you need, in normal language, and the right skill (if one matches)
loads itself in.

You *can* also invoke one by name directly if you want to be explicit —
e.g. "use the swot-strategic-review skill on GIC's current position" — which
is useful when a task is ambiguous or you want a specific framework rather
than whichever one Claude guesses is closest.

## Where skills live, and how "installing" works

Claude Code looks for skills in two folders:

- `~/.claude/skills/` — **personal**, active in every project, every chat,
  on this machine
- `.claude/skills/` inside a specific project folder — active only when
  you're working inside that project

This library keeps the **master copies** in
`claude-skills-library/skills/`. To make a skill actually usable, copy it
into `~/.claude/skills/`:

```bash
cp -r claude-skills-library/skills/swot-strategic-review ~/.claude/skills/
```

To install *all* of them at once:

```bash
cp -r claude-skills-library/skills/* ~/.claude/skills/
```

If you edit a skill later, edit the copy inside `claude-skills-library/`
(the source of truth, tracked in git) and re-run the copy command — don't
edit the live copy in `~/.claude/skills/` directly, or the two will drift
and you'll lose track of what changed.

## Using skills in claude.ai instead of Claude Code

Skills work a bit differently on claude.ai (the website/app, as opposed to
this terminal tool):

1. Zip up a skill folder (e.g. `zip -r swot.zip swot-strategic-review`)
2. In claude.ai, go to **Settings → Features → Skills** and upload the zip
3. It needs "code execution" enabled, and only works on Pro/Max/Team/
   Enterprise plans

Skills uploaded to claude.ai are **separate** from Claude Code skills —
uploading here doesn't sync there, and vice versa. If you want a skill
available in both places, install it in both.

## How to actually use these day to day

- **In a normal chat/conversation**: just describe the task. "Help me
  structure why our September bookings are down" will likely trigger
  `root-cause-five-whys` or `mece-problem-structuring` on its own.
- **In a project** (e.g. while working inside `golden-island-cruises/`):
  personal skills (`~/.claude/skills/`) are active automatically — you don't
  need to do anything extra.
- **Combining skills**: you can ask for something that chains a few
  together — e.g. "run a SWOT on GIC, then turn the findings into an
  executive summary" will pull in `swot-strategic-review` and then
  `executive-summary-writer`.
- **If a skill doesn't trigger when you expect it to**: be more explicit —
  name the skill, or describe the task using language closer to its
  `description` (check `catalog.md` for exact wording).

## Writing your own new skill

Use this as a starting template:

```markdown
---
name: your-skill-name
description: What this skill does, in one clear sentence. Use when [specific situation]. Mention keywords the user might actually say.
---

# Your Skill Name

## When to use this
[Situations that should trigger it]

## When NOT to use this
[Situations that look similar but shouldn't trigger it — prevents false triggers]

## Workflow
1. [Step-by-step instructions Claude should follow]
2. ...

## Output format
[What the final deliverable should look like]

## Common pitfalls
[Mistakes to avoid — things Claude tends to get wrong on this kind of task]
```

Rules that keep a skill working well:

- `name`: lowercase letters, numbers, hyphens only, max 64 characters, can't
  contain "claude" or "anthropic"
- `description`: max 1024 characters, must state both **what** it does and
  **when** to use it — this is the single most important field
- Keep the body under ~500 lines. If a framework needs a lot of detailed
  methodology, put that in a `references/some-topic.md` file inside the
  skill's folder and mention it in `SKILL.md` (e.g. "see
  `references/framework-details.md` for the full scoring rubric") — Claude
  only reads that file if it actually needs it, so it's free until used.

## A note on trust and security

Only use skills you wrote yourself or that come from Anthropic directly.
A skill's instructions can direct Claude to run commands and access files,
so a skill from an untrusted source is like installing software you
haven't reviewed. Everything in this library is written for you, so that's
not a concern here — but if you ever download a skill from GitHub or
Reddit, read through its `SKILL.md` and any scripts before installing it.

## Sources used to build this library

- [Agent Skills overview — platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [anthropics/skills — official example skills repo](https://github.com/anthropics/skills)
- [ComposioHQ/awesome-claude-skills — curated community list](https://github.com/ComposioHQ/awesome-claude-skills)
- [gcamilo/management-consulting — a public consulting-frameworks skill, used as a structural reference](https://github.com/gcamilo/management-consulting)
