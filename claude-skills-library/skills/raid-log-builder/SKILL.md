---
name: raid-log-builder
description: Builds and maintains a RAID log (Risks, Assumptions, Issues, Dependencies) — the standard project-governance artifact tracking what could go wrong, what's being assumed, what's already gone wrong, and what the project depends on. Use when the user needs a RAID log, project governance tracking, or wants to track assumptions and dependencies alongside risks, not just risks alone.
---

# RAID Log Builder

## When to use this

An ongoing project or program needs a single governance artifact
tracking risks, assumptions, issues, and dependencies together — the
standard format used for regular project status reporting.

## When NOT to use this

- Only risks need deep treatment (with likelihood/impact scoring and
  detailed mitigation planning) — use `risk-register-builder` for that
  focused exercise; a RAID log is broader but shallower per item, meant
  for ongoing tracking rather than deep risk analysis.

## Workflow

1. **Keep the four categories genuinely distinct — this is the
   discipline that makes a RAID log useful, not just a list:**
   - **Risk** — something that *might* happen and would have a negative
     effect if it did (hasn't happened yet)
   - **Assumption** — something believed to be true, not yet verified,
     that the plan depends on (if wrong, the plan needs to change)
   - **Issue** — something that *has already* happened and needs
     resolving now (not hypothetical anymore)
   - **Dependency** — something the project needs from outside itself to
     proceed (another team, a decision, an external delivery)
2. **Don't let a risk sit in "issue" before it's happened**, and don't
   leave an issue miscategorized as a risk once it's real — reclassify
   promptly as status changes.
3. **Assign an owner and a status to every item** — an item with no
   owner doesn't get worked.
4. **Review and update on a set cadence** (e.g. weekly), not just at
   creation — a RAID log that isn't maintained becomes actively
   misleading (it looks current but isn't).
5. **Convert unverified assumptions into confirmed facts or explicit
   risks as they resolve** — an assumption that's been quietly wrong for
   weeks is a common source of project surprises.

## Output format

```
## RAID log: [project], updated [date]

### Risks
| Risk | Likelihood | Impact | Owner | Status |
|---|---|---|---|---|

### Assumptions
| Assumption | If wrong, impact is... | Owner | Status (unverified/confirmed/false) |
|---|---|---|---|

### Issues
| Issue | Impact | Owner | Status | Resolution target |
|---|---|---|---|---|

### Dependencies
| Dependency | Needed from | Needed by (date) | Owner | Status |
|---|---|---|---|---|
```

## Common pitfalls

- Blurring risk and issue (something that's already happened still
  tracked as a "risk").
- Assumptions written once and never revisited to confirm or invalidate.
- No owner on an item, so it never actually moves.
- Treating the log as a one-time deliverable rather than a living
  document reviewed on a cadence.

## Quality checklist

- [ ] Each item is in the correct one of the four categories
- [ ] Every item has an owner and a current status
- [ ] Assumptions are being actively verified, not just logged and
      forgotten
- [ ] The log has an update date and is reviewed on a real cadence
