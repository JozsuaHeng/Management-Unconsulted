---
name: process-map-simplifier
description: Documents a current operational process step by step, then proposes a simplified version by identifying redundant, delayed, or unnecessary steps. Use when the user wants to map out how a process currently works, says a workflow is too slow or complicated, or wants to simplify an existing process.
---

# Process Map Simplifier

## When to use this

There's an existing, repeated operational process (booking handling,
onboarding a new client, trip preparation, invoicing) that the user wants
documented and/or improved.

## When NOT to use this

- The process doesn't exist yet (it's being designed from scratch) — this
  skill is for mapping and simplifying an existing process, not designing
  a new one from nothing.
- The issue is really about one specific tool/system being broken, not
  the overall process flow — a narrower technical fix may be more direct.

## Workflow

1. **Map the process exactly as it currently happens**, not as it's
   supposed to happen on paper — ask what actually occurs at each step,
   including workarounds, since the gap between the documented and actual
   process is often where the real problem lives.
2. **Break it into discrete steps**, each with: what happens, who does it,
   how long it typically takes, and what triggers the next step.
3. **Look for these specific improvement opportunities** at each step:
   - **Redundant steps** — is this step duplicated elsewhere, or does it
     re-verify something already confirmed?
   - **Unnecessary handoffs** — does this step require passing to another
     person/system where it could stay with one owner?
   - **Waiting/delay points** — where does work sit idle waiting on
     something (approval, response, a batch process)?
   - **Manual steps that could be simpler** — not necessarily automated
     with new tools, but is there a manual step doing more than it needs
     to (e.g. re-entering the same information twice)?
4. **Propose a simplified version**, keeping the essential checks/steps
   and removing or merging the rest — explicitly note what's being
   removed and why it's safe to remove (or flag if removing it introduces
   a new risk worth accepting consciously).
5. **Note what would need to change to implement the simplified version**
   (a new habit, a shared document, a small tool change) — a proposal
   without an implementation note tends to stay theoretical.

## Output format

```
## Process map: [process name]

### Current process
1. [Step] — who: [...] — time: [...] — triggers: [...]
2. ...

### Issues found
- [Redundant/delayed/unnecessary step] — why it's a problem

### Simplified process
1. [Step] — who: [...] — time: [...]
2. ...

### What changed and why
[Each removed/merged step, and why it's safe to remove]

### To implement this
[What would actually need to change]
```

## Common pitfalls

- Mapping the process as it's supposed to work rather than how it
  actually works, missing the real friction points.
- Removing a step without checking why it existed in the first place —
  some "redundant-looking" steps exist because of a past incident; ask
  before assuming it's safe to cut.
- Proposing a simplified process with no note on how to actually
  implement the change.

## Quality checklist

- [ ] Current process reflects actual practice, not just the documented
      ideal
- [ ] Each issue found is tied to a specific step, not a vague complaint
- [ ] Removed/merged steps have a stated reason they're safe to remove
- [ ] Simplified process includes an implementation note
