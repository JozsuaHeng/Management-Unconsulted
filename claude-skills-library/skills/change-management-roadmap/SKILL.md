---
name: change-management-roadmap
description: Builds a change management strategy and roadmap using the ADKAR model (Awareness, Desire, Knowledge, Ability, Reinforcement) so a change actually sticks after go-live instead of just being announced. Use when the user needs a change management plan or roadmap for a rollout, system implementation, or organisational change, or explicitly mentions ADKAR.
---

# Change Management Roadmap (ADKAR)

## When to use this

A change is planned or underway and the user needs a structured plan for
how people move from not knowing about it to actually working the new
way, sustainably — not just a communications announcement.

## When NOT to use this

- Only a communications plan is needed (who says what, when) without the
  fuller change-adoption structure — `communication-engagement-plan`
  covers that on its own.
- The change is too small to need structured change management — a
  one-line heads-up may be all that's needed.

## Workflow

1. **Use impact data as the input**, ideally from `change-impact-assessment`
   — the roadmap should target groups by how much they're actually
   affected, not treat everyone identically.
2. **Build activities against each ADKAR stage, in order — skipping a
   stage is the most common reason change doesn't stick:**
   - **Awareness** — people know the change is coming and why
   - **Desire** — people are willing to support and participate in it
     (this requires addressing "what's in it for me / what am I
     worried about," not just announcing)
   - **Knowledge** — people know how to change (training, documentation)
   - **Ability** — people can actually demonstrate the new skill/behavior
     in practice, not just in a training session
   - **Reinforcement** — the change is sustained after go-live (this
     stage is the one most often skipped, and skipping it is why changes
     regress to old behavior weeks after launch)
3. **Sequence activities across a timeline** — pre-launch (Awareness,
   Desire, Knowledge), launch (Ability — go-live support), post-launch
   (Reinforcement — this needs real duration, not a single follow-up
   email).
4. **Assign an owner to each activity** — an unowned change activity
   doesn't happen.
5. **Plan reinforcement concretely**: what specifically happens at 2
   weeks, 6 weeks, 3 months post-launch to catch regression to old
   behavior and address it.

## Output format

```
## Change roadmap: [change]

| Stage | Activity | Audience | Timing | Owner |
|---|---|---|---|---|
| Awareness | ... | ... | ... | ... |
| Desire | ... | ... | ... | ... |
| Knowledge | ... | ... | ... | ... |
| Ability | ... | ... | ... | ... |
| Reinforcement | ... | ... | ... | ... |

### Reinforcement plan (the stage most often skipped)
[Specific checks/support at defined intervals post-launch]
```

## Common pitfalls

- Treating "Awareness" (an announcement) as if it covers the whole
  change — the other four stages are where adoption actually happens.
- Designing Knowledge (training) without Ability (practice/support) —
  people can pass a training session and still fail at applying it live.
- No Reinforcement plan, or a token one — this is why changes visibly
  succeed at launch and quietly regress a month later.
- One-size-fits-all activities for groups with very different impact
  levels (see `change-impact-assessment`).

## Quality checklist

- [ ] All five ADKAR stages have specific activities, not just
      Awareness and Knowledge
- [ ] Activities are targeted by group/impact level, not uniform
- [ ] Every activity has an owner
- [ ] Reinforcement has concrete, timed check-ins, not a single
      post-launch email
