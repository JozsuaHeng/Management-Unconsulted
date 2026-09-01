---
name: weekly-ops-report
description: Turns scattered updates, notes, or raw information into a structured weekly business operations report. Use when the user wants to summarize the week, write an ops update, or turn loose notes into a regular team report.
---

# Weekly Ops Report

## When to use this

The user has a week's worth of scattered information (notes, numbers,
things that happened) and needs it turned into a structured internal
report — for themselves, a team, or record-keeping. This is internal/
operational, distinct from `board-investor-memo` which is for external
oversight stakeholders.

## When NOT to use this

- The audience is a board or investor, not an internal team — use
  `board-investor-memo` instead, which has different framing (asks,
  formal metrics) appropriate to that audience.
- There's genuinely nothing to report — a short "quiet week, nothing
  notable" is more honest and useful than padding a report with filler.

## Workflow

1. **Gather what actually happened this week** from whatever raw input
   exists (notes, memory, numbers provided) — don't invent activity that
   wasn't mentioned.
2. **Organize into consistent sections** so reports stay comparable week
   to week:
   - Headline (1-2 sentences on the overall week)
   - Key numbers (whatever metrics matter to this business, with a
     comparison to last week if available)
   - What happened (brief, bulleted — not a narrative essay)
   - Issues/blockers (anything that needs attention)
   - Coming up next week
3. **Keep it scannable.** A weekly report that takes 10 minutes to read
   won't get read regularly — bullets over paragraphs, numbers over
   descriptions where possible.
4. **Be honest about a quiet week.** Padding a slow week to look busier
   than it was undermines trust in every future report.
5. **Flag blockers clearly, not buried in a bullet list** — anything that
   needs someone else's attention or decision should stand out.

## Output format

```
## Weekly ops report: [week of / date range]

**Headline**: [1-2 sentences]

### Key numbers
| Metric | This week | Last week | Change |
|---|---|---|---|
| ... | ... | ... | ... |

### What happened
- [bullet]
- [bullet]

### Issues / blockers
- [anything needing attention, or "none this week"]

### Coming up next week
- [bullet]
```

## Common pitfalls

- Inventing detail not actually provided, to make the report feel more
  complete.
- Padding a quiet week instead of just saying it was quiet.
- Burying a real blocker inside a generic bullet list instead of calling
  it out.
- Inconsistent format week to week, making it hard to compare trends over
  time.

## Quality checklist

- [ ] Based only on information actually provided, nothing invented
- [ ] Key numbers include a week-over-week comparison where available
- [ ] Blockers are called out clearly, not buried
- [ ] Format is consistent with prior reports (for comparability)
