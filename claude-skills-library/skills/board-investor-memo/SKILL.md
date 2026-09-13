---
name: board-investor-memo
description: Drafts a structured board or investor update memo covering progress, key metrics, risks, and specific asks. Use when the user needs to write a board update, investor update, or periodic (monthly/quarterly) stakeholder memo.
---

# Board / Investor Memo

## When to use this

The user needs to write a periodic update to people with oversight or
financial stake in the business (a board, investors, or key partners) —
distinct from an internal team report (`weekly-ops-report`) or a
client-facing summary of analysis (`executive-summary-writer`).

## When NOT to use this

- The audience is internal team members, not board/investor-level
  stakeholders — use `weekly-ops-report`.
- There's no real update since the last one — say that plainly rather
  than padding a memo with filler.

## Workflow

1. **Confirm the reporting period and cadence** (monthly, quarterly,
   ad-hoc) — this sets how much ground the memo needs to cover.
2. **Lead with a short headline summary** — 2-3 sentences on the overall
   state of the business this period, before any detail.
3. **Report the key metrics that actually matter to this business**, not a
   generic list — for a charter business, likely bookings, revenue,
   occupancy/utilization, and customer satisfaction; for other businesses,
   adapt. Show period-over-period comparison, not just the current number.
4. **Cover progress against previously stated goals or asks.** If a
   previous memo said "we will do X by this quarter," report on it
   explicitly — don't let commitments quietly disappear.
5. **State risks and challenges honestly**, not just wins. A memo that
   only reports good news loses credibility and hides problems until
   they're bigger. Pair each risk with what's being done about it.
6. **End with specific asks, if any** — what does the board/investor need
   to decide, approve, or help with? If there's no ask, say "no action
   needed this period" explicitly rather than leaving it ambiguous.

## Output format

```
## [Business name] — [Period] Update

**Headline**: [2-3 sentence overall state]

### Key metrics
| Metric | This period | Last period | Change |
|---|---|---|---|
| ... | ... | ... | ... |

### Progress on prior commitments
- [Prior commitment] — [status: done / on track / delayed, and why]

### Risks & challenges
- [Risk] — [what's being done about it]

### Asks
- [Specific ask, or "no action needed this period"]
```

## Common pitfalls

- Only reporting good news — erodes trust once a real problem surfaces
  without warning.
- Vague metrics without period-over-period comparison, making it
  impossible to tell if things are improving or not.
- Letting previous commitments go unmentioned instead of explicitly
  tracking them.
- A vague or missing ask, leaving the reader unsure if they need to do
  anything.

## Quality checklist

- [ ] Headline states the overall picture in 2-3 sentences
- [ ] Metrics show period-over-period comparison, not just current state
- [ ] Prior commitments are explicitly tracked, not dropped
- [ ] Risks are included, each with a stated mitigation
- [ ] Ends with a clear, specific ask (or explicit "none")
