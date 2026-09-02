---
name: prince2-project-structuring
description: Structures a project using PRINCE2 (Projects IN Controlled Environments) — a live business case, clearly separated governance roles, stages with defined tolerances, and exception-based reporting. Use when the user needs a PRINCE2-structured project plan, mentions PRINCE2, or needs formal stage-gated governance with tolerances (common in UK/ANZ public-sector work).
---

# PRINCE2 Project Structuring

## When to use this

An organisation uses or requires PRINCE2 governance (common in UK/ANZ
public sector and formal enterprise programs), and the user needs the
project structured that way — business case, roles, stages, tolerances.

## When NOT to use this

- A small, informal project — full PRINCE2 ceremony is bureaucratic
  overkill for it.
- Unsure PRINCE2 is even the right fit — use
  `project-methodology-selector` first.

## Workflow

1. **Establish the Business Case and keep it alive.** PRINCE2's defining
   principle is "continued business justification" — the business case
   isn't written once and filed; it's checked at every stage boundary,
   and the project is stopped if it no longer holds up.
2. **Define the organisation as accountabilities, not job titles.** The
   Project Board (Executive, Senior User, Senior Supplier), Project
   Manager, and Team Manager are roles — on a small project one person
   may hold several, but keep the accountabilities distinct so it's
   clear who owns what decision.
3. **Break the project into Management Stages, each with tolerances**
   (time, cost, scope, risk, quality, benefit) set by the Board. This is
   "management by exception": the Project Manager runs the stage day to
   day and only escalates to the Board if a tolerance is breached — the
   Board doesn't need to be in every decision.
4. **Apply the relevant themes**, not all seven mechanically: Business
   Case, Organization, Quality, Plans, Risk, Change, Progress. Use only
   what the project's size and risk actually warrant.
5. **Plan products before activities** (Product-Based Planning) — define
   what deliverables/products are needed and their quality criteria
   first, then the activities to produce them, rather than jumping
   straight to a task list.
6. **Set reporting rules explicitly**: routine Highlight Reports on a
   cadence, and an Exception Report only when a tolerance is actually
   breached — this is what keeps the Board's time focused on real
   decisions, not status theatre.

## Output format

```
## PRINCE2 structure: [project]

**Business case (one line)**: [justification]

### Organisation
| Role | Held by | Accountable for |
|---|---|---|

### Stage plan
| Stage | Deliverables | Time tolerance | Cost tolerance | Escalation trigger |
|---|---|---|---|---|

### Reporting
Highlight report: [cadence]. Exception report: [trigger conditions].
```

## Common pitfalls

- Full PRINCE2 ceremony applied to a project too small to need it.
- Treating roles as literal job titles rather than accountabilities that
  can be combined on a small project.
- Losing "continued business justification" — never re-checking the
  business case as the project evolves.
- No real tolerance discipline, so everything escalates to the Board
  regardless (defeats management by exception).

## Quality checklist

- [ ] Business case has a re-check point at every stage boundary
- [ ] Roles are accountabilities, explicitly assigned, even if combined
- [ ] Every stage has stated tolerances and an escalation trigger
- [ ] Products/deliverables are planned before the activity list
