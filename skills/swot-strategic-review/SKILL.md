---
name: swot-strategic-review
description: Runs a disciplined SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis that forces every finding to connect to a strategic implication, instead of producing four disconnected bullet lists. Use when the user asks for a SWOT, wants to know "where do we stand," or is evaluating strategic position before a decision.
---

# SWOT Strategic Review

## When to use this

The user wants a structured view of a business's (or a specific
initiative's) strategic position — internal strengths/weaknesses, external
opportunities/threats — usually as an input to a bigger decision.

## When NOT to use this

- The user just wants a quick pro/con list for a small, tactical decision
  (a SWOT is overkill for "should I use vendor A or B").
- A SWOT has already been done recently and nothing material has changed —
  say so rather than re-running one for its own sake.

## Workflow

1. **Confirm the unit of analysis.** A SWOT needs a clear subject: the
   whole business, one product line, one market entry decision, one
   initiative. Ask if it's ambiguous — a SWOT of "the company" and a SWOT
   of "our new charter route to the Gilis" are different analyses.
2. **Strengths and Weaknesses are internal, and controllable.** Only
   include things the business itself does, has, or controls — team
   skills, reputation, cost structure, asset quality, brand. Do not put
   market conditions here.
3. **Opportunities and Threats are external, and largely uncontrollable.**
   Market trends, competitor moves, regulation, seasonality, currency,
   customer behavior shifts. Do not put internal weaknesses here disguised
   as threats.
4. **Cap each quadrant at 4-6 items.** More than that dilutes into noise —
   force prioritization instead of listing everything.
5. **For every item, state the "so what."** A strength or threat that
   doesn't change what the business should do isn't worth including. Pair
   each finding with a one-line implication.
6. **Cross the quadrants (TOWS step).** This is what most SWOTs skip and
   what actually makes it useful:
   - Strength + Opportunity → where to go on offense
   - Weakness + Opportunity → what to fix to capture upside
   - Strength + Threat → what to defend with
   - Weakness + Threat → what's genuinely at risk

## Output format

```
## SWOT: [subject]

### Strengths (internal, controllable)
- [Finding] → So what: [implication]

### Weaknesses (internal, controllable)
- [Finding] → So what: [implication]

### Opportunities (external, largely uncontrollable)
- [Finding] → So what: [implication]

### Threats (external, largely uncontrollable)
- [Finding] → So what: [implication]

### So what — strategic implications (TOWS)
- Offense (Strength × Opportunity): ...
- Fix-to-capture (Weakness × Opportunity): ...
- Defense (Strength × Threat): ...
- Risk (Weakness × Threat): ...
```

## Common pitfalls

- Internal/external mix-ups: "the market is shrinking" is a threat, not a
  weakness; "we're slow to respond to inquiries" is a weakness, not a
  threat.
- Listing without prioritizing — a 12-item quadrant is a brainstorm, not an
  analysis.
- Skipping the TOWS cross — a SWOT without it is four lists that don't add
  up to a recommendation.
- Stating findings as facts without evidence when they're really
  assumptions — flag anything unverified as such rather than asserting it.

## Quality checklist

- [ ] Every item is clearly internal (S/W) or external (O/T) — no mix-ups
- [ ] Each item has a stated "so what," not just a description
- [ ] Quadrants are prioritized (4-6 items), not exhaustive lists
- [ ] The TOWS cross produces at least one concrete recommendation
