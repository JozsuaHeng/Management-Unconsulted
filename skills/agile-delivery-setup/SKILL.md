---
name: agile-delivery-setup
description: Sets up an Agile/Scrum delivery structure — a groomed backlog, sprint cadence, ceremonies (standup, planning, review, retro), clearly separated roles, and an enforced Definition of Done. Use when the user needs to set up Agile/Scrum delivery, structure a backlog and sprints, or asks about Agile ceremonies and roles.
---

# Agile / Scrum Delivery Setup

## When to use this

A team is delivering work iteratively — requirements are expected to
evolve, or early/frequent feedback matters more than a fixed upfront
plan — and needs its Agile/Scrum structure actually set up properly, not
just declared.

## When NOT to use this

- Requirements are genuinely stable and fixed-scope delivery fits better
  — use `waterfall-project-plan`, or check `project-methodology-selector`
  first if unsure.
- The team already has a working setup and just needs one ceremony
  designed — `workshop-agenda-designer` may be the more precise tool for
  a single session like sprint planning.

## Workflow

1. **Confirm Agile genuinely fits** before setting it up — changing
   requirements or a real need for frequent stakeholder feedback are the
   actual justifications, not "Agile is more modern." If unsure, use
   `project-methodology-selector`.
2. **Define roles distinctly and don't blur them:**
   - **Product Owner** — owns and prioritizes the backlog, makes the
     "what and why" calls
   - **Scrum Master** — facilitates, removes blockers, protects the
     team's process; not a manager assigning tasks
   - **Delivery team** — self-organizes on *how* the work gets done
3. **Set up the backlog as a prioritized, continuously groomed list of
   user-facing items** — not a dumping ground of tasks. Define a
   Definition of Ready (what makes an item pull-able into a sprint).
4. **Define sprint cadence and the four core ceremonies:**
   - **Planning** — what the team commits to this sprint, and roughly how
   - **Daily standup** — brief peer sync (what's done, what's next,
     what's blocked) — not a status report upward to a manager
   - **Review** — demo real work to stakeholders, gather actual feedback
   - **Retro** — the team reflects on how it worked (for a deeper,
     less-frequent version, see `project-retrospective`)
5. **Define a Definition of Done and actually enforce it** — "done"
   needs to mean the same thing every sprint (tested, reviewed, meets
   acceptance criteria), not a shifting, informal standard.

## Output format

```
## Agile setup: [team/project]

### Roles
| Role | Held by | Owns |
|---|---|---|

### Backlog
Definition of Ready: [criteria]
Grooming cadence: [...]

### Sprint cadence
Sprint length: [...]

| Ceremony | Purpose | Cadence | Attendees |
|---|---|---|---|

### Definition of Done
[Explicit, checkable criteria]
```

## Common pitfalls

- "Cargo cult Agile" — ceremonies performed on schedule without the
  underlying empowerment or iteration actually happening.
- Product Owner and Scrum Master roles collapsed into one overloaded
  person on a team large enough to need both distinct.
- A backlog that's really an undifferentiated task list, with no
  prioritization discipline.
- Standups that turn into status meetings for a manager rather than
  peer coordination.
- A Definition of Done that exists on paper but isn't actually enforced
  sprint to sprint.

## Quality checklist

- [ ] Roles are distinct, not blurred into one person unnecessarily
- [ ] Backlog has a real Definition of Ready, not just a list
- [ ] All four ceremonies have a stated purpose, not just a calendar slot
- [ ] Definition of Done is specific and actually enforced
