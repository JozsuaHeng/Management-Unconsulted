---
name: stakeholder-influence-map
description: Maps stakeholders on an influence-vs-interest grid and recommends an engagement approach for each one. Use when the user needs to identify who needs to be on board for a decision or change, plan how to communicate with different stakeholders, or navigate organizational buy-in.
---

# Stakeholder Influence Map

## When to use this

A decision, project, or change involves multiple people or groups with
different levels of power and interest, and the user needs a plan for how
to engage each of them — not just a list of who's involved.

## When NOT to use this

- Only one or two stakeholders are relevant — a simple direct
  conversation plan is enough, a full grid is overkill.
- The question is about internal task ownership on a project, not
  influence/buy-in — use `raci-matrix-generator` for that instead.

## Workflow

1. **List every stakeholder who could affect or be affected by the
   decision** — include people who might resist as well as obvious
   supporters; an incomplete list is the most common failure mode here.
2. **Rate each on two dimensions:**
   - **Influence** — how much power they have to help or block this
     (formal authority, informal sway, control of resources)
   - **Interest** — how much this actually matters to them personally or
     to their goals
3. **Plot into the four quadrants** and use the standard engagement
   approach for each (see `references/quadrant-strategies.md` for detail):
   - High influence, high interest → **Manage closely** (actively involve)
   - High influence, low interest → **Keep satisfied** (don't overwhelm,
     but don't neglect)
   - Low influence, high interest → **Keep informed** (they care, give
     them visibility even without needing their active buy-in)
   - Low influence, low interest → **Monitor** (minimal effort, watch for
     change)
4. **For each stakeholder, note what they likely care about** — their
   actual motivation, not an assumption — since the engagement approach
   only works if it's aimed at what they actually value.
5. **Flag any stakeholder whose position might change** (e.g. someone
   gaining influence soon, or someone whose interest will spike once the
   decision becomes visible) — a static map misses this.

## Output format

```
## Stakeholder map: [decision/project]

| Stakeholder | Influence | Interest | Quadrant | What they likely care about | Engagement approach |
|---|---|---|---|---|---|
| ... | High/Low | High/Low | ... | ... | ... |

### Notes
- [Any stakeholder whose position is likely to shift, and when]
- [Any stakeholder missing from initial brainstorm that should be
  double-checked]
```

## Common pitfalls

- An incomplete stakeholder list — missing a quiet-but-high-influence
  person is the most common and costly mistake here.
- Guessing at what a stakeholder cares about instead of noting it as an
  assumption to verify (or actually asking them).
- Treating the map as static when a reorg, promotion, or upcoming
  visibility of the decision will change someone's influence or interest.
- Using the same engagement approach for everyone regardless of quadrant —
  the point of the grid is that different stakeholders need different
  handling.

## Quality checklist

- [ ] Stakeholder list is genuinely comprehensive, including likely
      resistors
- [ ] Influence and interest are rated with a stated reason, not just
      guessed
- [ ] Each stakeholder has a specific engagement approach, not a generic
      one
- [ ] Any likely change in someone's position is flagged
