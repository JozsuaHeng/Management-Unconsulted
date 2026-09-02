---
name: rapid-decision-framework
description: Clarifies decision-making roles using the RAPID framework (Recommend, Agree, Perform, Input, Decide) — who proposes, who must sign off, who executes, who's consulted, and who holds final decision authority. Use when a decision has stalled because ownership is unclear, or to clarify decision rights specifically — distinct from raci-matrix-generator, which covers task/work ownership, not who gets to decide.
---

# RAPID Decision Framework

## When to use this

A decision (not a task) has unclear ownership — it's stalling, being
re-litigated, or nobody's sure who actually gets the final call.

## When NOT to use this

- This is about task/work ownership on a project, not a single decision
  — use `raci-matrix-generator` instead. The two frameworks answer
  different questions and are easy to conflate.

## Workflow

1. **Confirm this is genuinely about decision rights**, not task
   execution. "Who does the analysis" is a RACI question; "who gets to
   decide once the analysis is done" is a RAPID question.
2. **Assign each RAPID role explicitly for this specific decision:**
   - **Recommend** — who proposes an option and does the supporting
     analysis
   - **Agree** — who must sign off before it proceeds. Keep this list
     as small as possible — every additional person here is a de facto
     veto holder
   - **Perform** — who executes once the decision is made
   - **Input** — who is consulted but doesn't have to be agreed with
   - **Decide** — exactly one person or body with the final call. This
     is the single most important assignment in the whole framework
3. **Watch for the most common failure**: too many people holding
   "Agree." This creates gridlock, since any one of them can block
   indefinitely — push back on this explicitly if it happens.
4. **Make the assignment visible before the decision process starts**,
   not after it's already stalled — RAPID is most valuable as a
   preventive structure, not a post-mortem tool.

## Output format

```
## Decision rights: [decision]

| Role | Held by | Note |
|---|---|---|
| Recommend | ... | |
| Agree | ... | keep this list minimal |
| Perform | ... | |
| Input | ... | |
| Decide | ... | exactly one |
```

## Common pitfalls

- Confusing this with RACI — they answer different questions (decision
  rights vs. task ownership).
- Too many people holding "Agree," creating gridlock through de facto
  veto power.
- No single clear "Decide" holder, leaving the decision bouncing
  between people indefinitely.

## Quality checklist

- [ ] This is confirmed to be about decision rights, not task ownership
- [ ] "Agree" is held by as few people as the decision genuinely
      requires
- [ ] Exactly one person or body holds "Decide"
- [ ] Roles are assigned before the decision process starts, not after
      it stalls
