---
name: waterfall-project-plan
description: Structures a traditional sequential (Waterfall) project plan — phases with clear deliverables, gate reviews between phases, formal sign-off, and change control — for projects with stable, well-understood requirements. Use when the user needs a Waterfall or phase-gate project plan, or is planning a project with fixed, well-defined requirements upfront.
---

# Waterfall Project Plan

## When to use this

Requirements are genuinely stable and well understood upfront, there's
low need for iterative feedback, or the project is contractually or
regulatorily required to follow a phase-gate structure.

## When NOT to use this

- Requirements are expected to evolve, or early feedback matters —
  `agile-delivery-setup` fits better.
- Waterfall is being chosen by default/habit rather than genuine fit —
  check `project-methodology-selector` first.

## Workflow

1. **Confirm the fit honestly** — Waterfall's cost is that late-discovered
   changes are expensive; it only makes sense when requirements are
   actually stable enough that this risk is low.
2. **Define phases explicitly** (commonly Requirements → Design → Build
   → Test → Deploy, adapted to context), each with a clear deliverable
   and a named owner.
3. **Define gate criteria for every phase transition** — what must be
   true and formally signed off before moving to the next phase. This
   gate discipline is Waterfall's actual strength; without it, "doing
   things in order" provides none of the model's real benefit.
4. **Build in formal change control from the start** — since late
   changes are expensive in this model, an explicit process (raise,
   assess impact, approve/reject, re-baseline if approved) prevents
   scope creeping in informally mid-phase, which is the most common way
   Waterfall projects go over budget and schedule.
5. **Sequence with explicit dependencies** between phases, and estimate
   realistically — Waterfall's visibility only helps if the plan itself
   is honest about how long things take.

## Output format

```
## Waterfall plan: [project]

| Phase | Deliverable | Owner | Gate criteria (to exit this phase) | Duration |
|---|---|---|---|---|

### Change control
[How a proposed change is raised, assessed, and approved/rejected —
and what happens to the schedule/budget if approved]
```

## Common pitfalls

- No real gate discipline — phases blur together with no formal
  sign-off, losing the model's main advantage.
- Applying Waterfall to genuinely uncertain requirements, forcing
  premature commitment and expensive rework later.
- No change control process, letting scope creep in informally within a
  phase instead of through a visible, assessed process.
- Optimistic phase durations with no acknowledgment of dependency risk
  between phases.

## Quality checklist

- [ ] Every phase has explicit gate criteria, not just a deliverable
      description
- [ ] A formal change control process is defined before it's needed
- [ ] Dependencies between phases are made explicit
- [ ] The choice of Waterfall itself is justified by requirement
      stability, not just habit
