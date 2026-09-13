---
name: pmbok-project-planning
description: Plans a project using the PMBOK framework's knowledge areas (scope, schedule, cost, quality, risk, resources, communications, procurement, stakeholders) and process groups — the PMI/US-style counterpart to PRINCE2. Use when the user needs a PMBOK-structured project plan, mentions PMI/PMBOK, or wants a knowledge-area-based planning approach.
---

# PMBOK Project Planning

## When to use this

The organisation follows or references PMI/PMBOK conventions (common in
US-oriented and many corporate PMOs), and the user needs a plan
structured around its knowledge areas and process groups.

## When NOT to use this

- The organisation runs PRINCE2 instead — use `prince2-project-structuring`,
  which is stage/tolerance-based rather than knowledge-area-based, even
  though the two overlap conceptually.
- Unsure PMBOK is the right fit — use `project-methodology-selector`.

## Workflow

1. **Identify which process group the project is in** — Initiating,
   Planning, Executing, Monitoring & Controlling, or Closing — since
   PMBOK's guidance and the right level of detail differ by phase.
2. **Apply the knowledge areas proportionally to the project's size**,
   not as a rigid checklist to fill out regardless of relevance:
   - **Scope** — what's in/out, decomposed into a Work Breakdown
     Structure (WBS)
   - **Schedule** — milestones and dependencies
   - **Cost** — budget baseline
   - **Quality** — acceptance criteria for deliverables
   - **Risk** — cross-reference `raid-log-builder` rather than
     duplicating a separate risk process
   - **Resources** — who and what's needed
   - **Communications** — cross-reference `communication-engagement-plan`
   - **Procurement** — only if external vendors/contracts are involved
   - **Stakeholders** — cross-reference `stakeholder-influence-map`
3. **Build the Work Breakdown Structure first** — decompose deliverables
   into manageable work packages before building a task list or
   schedule. This is PMBOK's core planning discipline: define what must
   exist, then how to produce it — the same deliverable-first logic as
   PRINCE2's Product-Based Planning, phrased differently.
4. **Cross-reference other skills in this library rather than
   duplicating them** — PMBOK's breadth means several knowledge areas
   map directly onto dedicated skills already in this library; use
   those for depth and keep this skill's output as the overall
   integrating plan.

## Output format

```
## PMBOK plan: [project]
Process group: [Initiating/Planning/Executing/M&C/Closing]

### Work Breakdown Structure (top level)
1. [Deliverable]
   1.1 [Work package]
   ...

### Knowledge area summary
| Area | Plan / cross-reference |
|---|---|
| Scope | ... |
| Schedule | ... |
| Cost | ... |
| Quality | ... |
| Risk | See RAID log |
| Resources | ... |
| Communications | See communication & engagement plan |
| Procurement | ... (or "not applicable") |
| Stakeholders | See stakeholder influence map |
```

## Common pitfalls

- Treating all nine knowledge areas as equally weighty regardless of
  project size — a small project needs a light touch on most of them.
- Skipping the WBS and jumping straight to a task list, losing the
  deliverable-first framing that makes scope actually controllable.
- Duplicating a separate risk/comms/stakeholder process instead of
  cross-referencing the dedicated skills already built for that depth.

## Quality checklist

- [ ] WBS exists and is deliverable-based, not just a task list
- [ ] Each knowledge area is addressed proportionally to project size
- [ ] Risk, communications, and stakeholder detail cross-reference the
      dedicated skills rather than being duplicated shallowly here
- [ ] Process group is stated, since it changes what's actually needed
