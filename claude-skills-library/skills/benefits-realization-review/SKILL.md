---
name: benefits-realization-review
description: Reviews whether a completed project or program actually delivered the benefits it was originally justified by, comparing promised outcomes to what really happened months after go-live. Use when a project has been live for a while and the user wants to check whether it achieved what it promised, or needs a benefits realization report — distinct from project-retrospective, which reviews delivery process rather than outcomes.
---

# Benefits Realization Review

## When to use this

A project or program has been live for a meaningful period, and the
user wants to check whether the business benefits it was originally
justified by actually materialized — not how smoothly it was delivered.

## When NOT to use this

- The project just finished and the focus is on delivery process (what
  worked/didn't in how it was run) — use `project-retrospective` for
  that; this skill is specifically about outcome measurement, ideally
  run separately and later, once there's been time for benefits to show.

## Workflow

1. **Pull the original promised benefits** from the initial
   justification (e.g. a `cost-benefit-analysis` or business case). Each
   should have been stated in a measurable way originally — if it
   wasn't, that's a finding in itself, worth flagging now for next
   time's business cases.
2. **Measure actual performance against each promised benefit using real
   data**, not impressions or a general sense that "it's going well."
3. **For benefits not yet realized, distinguish three different
   situations** — they need different responses:
   - **Still in progress** — genuinely needs more time
   - **Blocked** — needs a specific intervention to get unstuck
   - **Was never realistic** — a planning lesson for next time's
     business cases, not a delivery failure
4. **Identify what's needed to close any real gap** — a specific fixable
   blocker, or a case for formally writing the benefit off rather than
   leaving it in limbo indefinitely.
5. **Report honestly even when the answer is uncomfortable.** The entire
   value of this review is catching benefit shortfall while there's
   still time to act on it — a review that only reports good news
   defeats its own purpose.

## Output format

```
## Benefits realization review: [project], [time since go-live]

| Promised benefit | Target | Actual | Status | Action |
|---|---|---|---|---|
| ... | ... | ... | Realized / In progress / Blocked / Not realistic | ... |

### Overall
[Honest summary — did this investment deliver what it promised]
```

## Common pitfalls

- Skipping this review entirely once a project goes live — the single
  most common failure; benefit tracking usually stops the moment
  delivery is declared "done."
- Vague original benefit statements that can't actually be measured
  against real data.
- Treating every unrealized benefit the same, instead of distinguishing
  in-progress from blocked from never-realistic.

## Quality checklist

- [ ] Actual performance is measured with real data, not impression
- [ ] Unrealized benefits are categorized (in progress / blocked / not
      realistic), not lumped together
- [ ] Each gap has a stated action — close it or formally write it off
- [ ] The report is honest even where the finding is unfavorable
