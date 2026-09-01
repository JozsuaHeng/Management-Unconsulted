---
name: program-governance-structure
description: Defines the governance structure for a program or project — decision-making forums, escalation paths, meeting cadence, and a decision log — so decisions get made at the right level without every issue escalating to the top. Use when the user is setting up a new program or project and needs a governance model, decision rights, or an escalation structure.
---

# Program Governance Structure

## When to use this

A program or project of meaningful size is starting, or an existing one
is struggling with unclear decision-making (everything escalates, or
nothing gets decided), and needs an explicit governance structure.

## When NOT to use this

- A small, single-owner initiative — formal governance structure adds
  overhead a simple project doesn't need.
- The ask is really about one specific decision, not an ongoing
  structure — just make the decision.

## Workflow

1. **Map decision types to the right level**, roughly:
   - **Operational/day-to-day** — the delivery team decides directly,
     no meeting needed
   - **Scope/budget/timeline changes within tolerance** — a working
     group or steering-level forum
   - **Strategic direction, major budget/scope changes** — sponsor or
     executive-level forum
2. **Define each forum explicitly**: purpose, who's in it (and why —
   membership should be the minimum needed to decide, not everyone
   interested), cadence, and exactly what decisions it has authority
   over.
3. **Define an escalation path**: what specifically triggers escalation
   (e.g. "impact beyond X budget or Y week delay"), and to which forum —
   vague escalation criteria are why everything ends up escalating by
   default.
4. **Set up a decision log** — what was decided, by whom, when, and the
   rationale — so decisions aren't quietly re-argued weeks later by
   someone who wasn't in the room.
5. **Right-size the structure** — too many forums creates governance
   fatigue and slows delivery; too few creates a bottleneck at the top.
   Match the number of forums to the program's actual complexity, not a
   template.

## Output format

```
## Governance structure: [program]

| Forum | Purpose | Membership | Cadence | Decision authority |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### Escalation triggers
| Trigger | Escalates to |
|---|---|
| ... | ... |

### Decision log
| Date | Decision | Made by | Rationale |
|---|---|---|---|
```

## Common pitfalls

- Too many governance layers for the program's actual size, slowing
  delivery without adding real oversight value.
- Vague escalation criteria, causing everything (or nothing) to
  escalate.
- Membership padded with "interested parties" rather than the minimum
  needed to actually decide.
- No decision log, so settled decisions get quietly re-opened later.

## Quality checklist

- [ ] Each forum has a clearly stated decision authority, not just a
      general purpose
- [ ] Escalation triggers are specific and measurable, not vague
- [ ] Number of forums matches the program's actual size/complexity
- [ ] A decision log exists and captures rationale, not just outcomes
