---
name: raci-matrix-generator
description: Generates a RACI (Responsible, Accountable, Consulted, Informed) matrix for a project or initiative, clarifying who does the work, who owns the outcome, who must be consulted, and who just needs to be kept informed. Use when the user needs to clarify roles and responsibilities, asks "who owns what," or a project has role confusion or duplicated/dropped work.
---

# RACI Matrix Generator

## When to use this

A project or initiative has multiple people/roles involved and there's
confusion (or risk of confusion) about who actually does what, who
decides, and who just needs visibility.

## When NOT to use this

- Only one person is doing the work — a RACI matrix adds no value.
- The question is about external stakeholder buy-in/influence rather than
  internal task ownership — use `stakeholder-influence-map` instead.

## Workflow

1. **List the actual tasks/decisions**, not vague activity areas — "draft
   the proposal," "approve the final proposal," and "send it to the
   client" are three distinct RACI rows; "handle the proposal" is too
   vague to assign roles to meaningfully.
2. **For each task, assign exactly one Accountable person.** This is the
   single most important RACI rule: Accountable means the buck stops with
   them — there must be exactly one, never zero, never more than one, or
   the whole point of the matrix (clear ownership) breaks down.
3. **Assign Responsible to whoever actually does the work** — can be more
   than one person, but keep it to who's hands-on, not everyone tangential
   to the task.
4. **Assign Consulted sparingly** — people whose input is needed before
   the task is done (two-way communication). Over-listing Consulted people
   slows everything down; only include those whose input genuinely
   changes the outcome.
5. **Assign Informed to those who need to know the outcome but have no
   input role** (one-way communication) — keep this list light too;
   informing everyone about everything defeats the purpose.
6. **Check every row has exactly one Accountable**, and that no single
   person is Accountable for so many rows it's unrealistic.

## Output format

```
## RACI matrix: [project/initiative]

| Task/Decision | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| ... | [name(s)] | [exactly one name] | [name(s), if any] | [name(s), if any] |

### Flags
[Any row missing a clear Accountable owner, or any person overloaded
across too many Accountable rows]
```

## Common pitfalls

- More than one Accountable person on a task — reintroduces the exact
  ambiguity RACI is meant to remove.
- No Accountable person at all — same problem, opposite cause.
- Over-listing Consulted or Informed roles, which slows decisions down
  and defeats the purpose of clarifying who's actually needed.
- Vague task rows that can't be meaningfully assigned to specific people.

## Quality checklist

- [ ] Tasks are specific and assignable, not vague activity areas
- [ ] Every row has exactly one Accountable person
- [ ] Consulted and Informed lists are kept lean, not padded
- [ ] Any overloaded person (Accountable on too many rows) is flagged
