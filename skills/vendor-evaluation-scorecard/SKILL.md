---
name: vendor-evaluation-scorecard
description: Builds a weighted scorecard for evaluating and comparing vendor or supplier proposals received, so a selection decision is defensible rather than a gut call. Use when the user is choosing between vendor/supplier proposals, evaluating RFP responses received, or needs a vendor selection scorecard — distinct from writing a tender response.
---

# Vendor Evaluation Scorecard

## When to use this

Multiple vendor or supplier proposals have come in and need to be
compared and scored to support a selection decision — the receiving
side of a tender process (compare to `government-tender-response`,
which is about writing a response, not evaluating ones received).

## When NOT to use this

- Only one vendor is genuinely in scope — a scorecard adds no
  comparative value; just assess the one option directly.

## Workflow

1. **Define evaluation criteria before reviewing proposals in detail**,
   if at all possible — deciding criteria after seeing proposals risks
   unconsciously reverse-engineering them to favor a preferred vendor.
2. **Weight criteria by actual importance to this specific decision**,
   not equal weighting by default. Price matters more for a commodity
   purchase; track record and risk matter more for a high-stakes
   engagement.
3. **Score each vendor against each criterion with a brief written
   justification** — not just a number. The justification is what makes
   the score defensible later and lets someone else understand the
   reasoning without re-reading every proposal.
4. **Calculate weighted totals, but treat them as an input to judgment,
   not an automatic decision.** A close score gap, or a hard
   disqualifying factor (compliance failure, unacceptable risk), should
   be able to override a marginal total-score win.
5. **Document the decision rationale explicitly if the top-scored
   option isn't the one chosen** — this is exactly the situation an
   audit or a stakeholder is most likely to question later.

## Output format

```
## Vendor scorecard: [decision]

| Criterion | Weight | Vendor A (score + note) | Vendor B (score + note) | ... |
|---|---|---|---|---|
| ... | ...% | ... | ... | |
| **Weighted total** | | ... | ... | |

### Recommendation
[Pick, with rationale — especially explicit if it differs from the raw
top score]
```

## Common pitfalls

- Setting criteria after seeing proposals, shaping them to justify a
  preferred pick.
- Equal-weighting every criterion regardless of what actually matters
  for this decision.
- Treating the weighted total as automatically final, with no room for
  judgment on disqualifying factors.
- No written justification per score, making the scorecard
  unreviewable later.

## Quality checklist

- [ ] Criteria and weights were set with real reasoning, ideally before
      or independent of reading proposals in full detail
- [ ] Every score has a brief justification, not just a number
- [ ] A disqualifying factor, if any, is called out explicitly
- [ ] If the recommendation isn't the top raw score, the reason is
      stated
