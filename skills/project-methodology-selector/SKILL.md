---
name: project-methodology-selector
description: Helps choose which delivery methodology — PRINCE2, PMBOK, Agile/Scrum, Waterfall, or a hybrid — actually fits a specific project's characteristics, instead of defaulting to whichever one the team already knows. Use when starting a new project and unsure which methodology to use, comparing PRINCE2 vs Agile vs Waterfall, or needing a justified case for a delivery approach.
---

# Project Methodology Selector

## When to use this

A project is starting (or an existing one feels like a poor fit for its
current approach) and the user wants a reasoned recommendation on
delivery methodology, not just a default or a preference.

## When NOT to use this

- The methodology is already fixed by contract, regulation, or
  organisational mandate — there's no real decision to make; go straight
  to the relevant structuring skill (`prince2-project-structuring`,
  `pmbok-project-planning`, `agile-delivery-setup`,
  `waterfall-project-plan`).

## Workflow

1. **Characterize the project honestly against the factors that actually
   drive fit** — not against which methodology is most familiar or
   fashionable:
   - **Requirement stability** — stable and well understood → Waterfall/
     PRINCE2-friendly; expected to evolve → Agile-friendly
   - **Need for early/frequent stakeholder feedback** — high → Agile
   - **Governance/compliance requirements** — formal stage-gates or a
     contractual/regulatory requirement → PRINCE2/PMBOK-friendly
   - **Team experience** — a team's first-ever attempt at an unfamiliar
     methodology on something high-stakes is a real risk factor, not
     just a preference to override
   - **Organisational context** — does this project need to interface
     with a wider program that already runs a particular way
2. **Don't force a binary choice.** Most real projects are hybrids — a
   PRINCE2 or PMBOK governance wrapper around Agile delivery sprints is
   common and often the genuinely correct answer, not a compromise to
   apologize for.
3. **State the recommendation with the reasoning explicit**, tied to the
   specific factors above — a recommendation without stated reasoning is
   just an opinion.
4. **Name what has to remain true for the recommendation to hold**, and
   flag it if that assumption changes later (e.g. "this assumes
   requirements stay stable through Q2 — if that changes, revisit
   toward a more iterative approach").

## Output format

```
## Methodology recommendation: [project]

| Factor | This project's situation | Implication |
|---|---|---|

### Recommendation
[Methodology or hybrid, with the reasoning stated explicitly]

### Holds as long as
[The assumption(s) this recommendation depends on]
```

## Common pitfalls

- Choosing a methodology because it's fashionable or because leadership
  has a preference, rather than because it fits the project.
- Treating "hybrid" as an embarrassing compromise instead of what it
  often genuinely is: the correct answer for a mixed-characteristic
  project.
- No stated reasoning — a recommendation that's really just an opinion
  dressed up as analysis.
- Not naming the assumption the recommendation depends on, so a changed
  situation goes unnoticed.

## Quality checklist

- [ ] Each factor is assessed against this specific project, not
      generic methodology preferences
- [ ] The recommendation states its reasoning explicitly
- [ ] A hybrid approach is considered seriously, not dismissed by default
- [ ] The assumption the recommendation depends on is named
