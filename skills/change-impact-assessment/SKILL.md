---
name: change-impact-assessment
description: Assesses who and what is impacted by a planned change (people, process, systems, culture) before it's rolled out, so change-management effort targets what actually needs it instead of guessing. Use when the user is planning a system rollout, process change, reorg, or any initiative that changes how people work, and needs to understand impact before building a change plan.
---

# Change Impact Assessment (CIA)

## When to use this

A change is planned (new system, new process, org restructure) and, before
building a rollout or communication plan, the user needs to know
specifically who is affected, how much, and in what way.

## When NOT to use this

- The change is trivial/low-impact enough that a full assessment is more
  process than the decision needs — say so rather than over-formalizing a
  small tweak.
- Impact is already well understood and documented — update the existing
  assessment rather than starting over.

## Workflow

1. **Describe the change precisely.** "New booking system" is vague;
   "replacing the shared spreadsheet booking process with a dedicated
   booking platform, changing how bookings are entered and how
   availability is checked" is assessable.
2. **Identify every group touched**, not just the obvious one — direct
   users, adjacent teams whose workflow depends on the changed thing,
   customers/external parties, and anyone whose role changes even if the
   system/process itself doesn't touch them directly.
3. **For each group, assess impact across dimensions:**
   - **Process** — what they do differently, step by step
   - **Systems/tools** — what they now use instead of / in addition to
     before
   - **People/roles** — whether responsibilities, reporting lines, or
     required skills change
   - **Culture/ways of working** — anything that shifts how the group
     operates day to day, beyond the mechanical change
4. **Rate the magnitude honestly** (e.g. Small / Medium / Large) per
   group — don't rate everything as "large" for emphasis; a mixed
   picture is more useful and more credible than uniform severity.
5. **Get this from the people affected, not just from planning
   assumptions** — a quick check with someone actually doing the work
   catches impacts a top-down view misses.
6. **Feed the result forward** — this assessment is normally the input to
   a change roadmap (`change-management-roadmap`), a readiness check
   (`change-readiness-assessment`), or a communications plan
   (`communication-engagement-plan`), not an end in itself.

## Output format

```
## Change impact assessment: [change, precisely described]

| Group | Process impact | Systems impact | People/role impact | Culture impact | Magnitude |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | Small/Medium/Large |

### Groups needing the most support
[Who's most affected and why, in plain language]

### Confidence
[Where this is based on direct input from affected people vs. assumption]
```

## Common pitfalls

- Guessing impact from a planning document instead of checking with
  people actually doing the affected work.
- Rating every group as equally impacted, which tells the reader nothing
  about where to focus effort.
- Stopping at the obvious/direct users and missing adjacent teams or
  external parties who are also affected.
- Treating this as a one-off exercise when the change design itself
  changes — re-check if scope shifts.

## Quality checklist

- [ ] Every genuinely affected group is included, not just the obvious
      direct users
- [ ] Each group is rated across process/systems/people/culture, not
      just one dimension
- [ ] Magnitude ratings are differentiated, not uniformly high
- [ ] Based on input from affected people where possible, with
      confidence noted where it's assumption instead
