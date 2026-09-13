---
name: root-cause-five-whys
description: Drills from an observed symptom down to its root cause using the 5-Whys method (and a fishbone/cause-category checklist for more complex cases), so fixes address the actual problem instead of a surface symptom. Use when something is going wrong repeatedly, the user asks "why did this happen," or a fix keeps not working.
---

# Root Cause Analysis (5-Whys)

## When to use this

Something specific and observable went wrong (a metric dropped, a process
failed, a complaint pattern emerged) and the user wants to know the actual
cause, not just the symptom — especially useful when a first attempted fix
didn't work, which usually means the wrong layer was targeted.

## When NOT to use this

- The problem is broad and undefined ("why is the business struggling") —
  structure it first with `mece-problem-structuring`, then apply this to
  one specific branch.
- The cause is already known and confirmed — this skill is for finding an
  unknown cause, not documenting a known one.

## Workflow

1. **State the symptom precisely and factually.** "Bookings dropped" is
   vague; "confirmed bookings for September fell 30% versus August" is a
   stated symptom that can actually be traced.
2. **Ask "why" and answer with a real mechanism, not a restatement.**
   Each answer must be a cause that, if true, would actually produce the
   effect above it — not a synonym for the symptom.
3. **Repeat until you hit a cause that is either (a) actionable — something
   the business can actually change, or (b) external and fixed — a
   constraint to plan around rather than solve. Stop there.** Five is a
   guideline, not a rule: some chains resolve in three whys, others need
   seven. Stop when you hit something real, not at an arbitrary count.
4. **At each step, note whether the answer is a confirmed fact or a
   hypothesis to test.** "Why did response time increase — because a team
   member left last month" is a fact if true; "why did response time
   increase — because inquiries got more complex" is a hypothesis until
   checked against actual inquiry data.
5. **For problems with multiple plausible contributing causes**, don't
   force a single chain — use the fishbone categories in
   `references/fishbone-categories.md` to check across People, Process,
   Tools/Systems, and External factors, then trace the most likely one(s)
   with 5-Whys.
6. **End with the fix aimed at the root cause, not the symptom** — and
   note if a quick symptom-level mitigation is also worth doing in the
   meantime while the root cause fix takes effect.

## Output format

```
## Root cause: [symptom, stated precisely]

1. Why? → [cause] (fact / hypothesis to test)
2. Why? → [cause] (fact / hypothesis to test)
3. Why? → [cause] (fact / hypothesis to test)
   ...continue until root cause reached...

### Root cause
[The cause the chain bottoms out at]

### Recommended fix
Aimed at root cause: [...]
Symptom-level mitigation in the meantime (if needed): [...]
```

## Common pitfalls

- Stopping at the first plausible-sounding answer instead of continuing to
  ask why that's true.
- Answers that just restate the symptom in different words ("bookings
  dropped because fewer people booked") rather than naming a mechanism.
- Assuming a single linear chain when the real cause is actually two or
  three contributing factors — check the fishbone categories before
  committing to one chain.
- Treating every "why" answer as a confirmed fact rather than flagging
  which ones are still hypotheses needing a data check.

## Quality checklist

- [ ] Symptom is stated precisely and factually, not vaguely
- [ ] Each "why" step names a real mechanism, not a restatement
- [ ] Fact vs. hypothesis is labeled at each step
- [ ] The chain stops at something actionable or a confirmed external
      constraint, not arbitrarily at five
- [ ] The fix targets the root cause, with symptom mitigation noted
      separately if relevant
