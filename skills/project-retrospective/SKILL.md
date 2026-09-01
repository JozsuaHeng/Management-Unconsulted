---
name: project-retrospective
description: Runs a structured retrospective on a completed project, program phase, or initiative — what worked, what didn't, root causes, and specific recommendations for next time — so lessons actually change future work instead of being filed away. Use when a project or phase has just finished and the user wants a retrospective, lessons-learned review, or post-mortem (backward-looking; for a forward-looking pre-decision version, see pre-mortem-facilitator).
---

# Project Retrospective

## When to use this

A project, program phase, or initiative has just wrapped up, and the
user wants to capture what actually happened and turn it into
improvements for next time — not just a summary of activities.

## When NOT to use this

- The project hasn't started or finished yet — for a pre-decision
  version of this thinking, use `pre-mortem-facilitator` instead.
- The goal is just a status update, not a lessons-learned exercise —
  use `weekly-ops-report` or `board-investor-memo` instead.

## Workflow

1. **Gather input broadly**, not just from leadership — the people who
   actually did the work see friction and workarounds that a top-down
   view misses entirely.
2. **Separate fact from interpretation.** "The training session ran two
   weeks late" is a fact; "the timeline was unrealistic" is an
   interpretation — capture both, but don't let interpretation pass as
   fact.
3. **Group findings into what worked, what didn't, and root causes** —
   for a recurring or serious "what didn't work" item, apply
   `root-cause-five-whys` rather than stopping at the surface symptom.
4. **Frame findings around the system/process, not blame on
   individuals** — "the approval step had no defined turnaround time"
   leads to a fixable recommendation; "so-and-so was slow to approve"
   doesn't, and makes people defensive in future retros.
5. **Turn every real finding into a specific, actionable recommendation**
   — "communicate better" is not actionable; "add a defined 48-hour
   turnaround expectation to the approval step" is.
6. **Assign an owner to each recommendation.** A retrospective with no
   ownership for its recommendations is a report that gets filed and
   forgotten — its value is entirely in whether it changes the next
   project.

## Output format

```
## Retrospective: [project/phase], [dates]

### Context
[Brief — what this project/phase was]

### What worked
- [Specific, not generic]

### What didn't work (with root cause where it matters)
- [Finding] — Root cause: [from 5-Whys or direct evidence]

### Recommendations for next time
| Recommendation | Owner | Applies to |
|---|---|---|
| ... | ... | [next project / ongoing process] |
```

## Common pitfalls

- Only interviewing leadership/sponsors, missing frontline reality.
- Blame-framed findings that make people defensive rather than useful
  process fixes.
- Vague recommendations ("communicate better," "plan more carefully")
  that no one can actually act on.
- No ownership assigned, so recommendations never make it into the next
  project.

## Quality checklist

- [ ] Input gathered from people who did the work, not just leadership
- [ ] Findings distinguish fact from interpretation
- [ ] "What didn't work" items include root cause, not just symptom
- [ ] Every recommendation is specific, actionable, and has an owner
