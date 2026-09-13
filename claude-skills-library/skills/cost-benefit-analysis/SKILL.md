---
name: cost-benefit-analysis
description: Builds a structured cost-benefit case for a proposed investment or initiative — quantified costs, quantified and qualitative benefits kept clearly separate, and a stated net position with sensitivity — so a go/no-go decision rests on an honest comparison, not optimism. Use when the user needs to justify an investment, build a business case with costs and benefits, or wants a CBA/ROI analysis.
---

# Cost-Benefit Analysis

## When to use this

A proposed investment or initiative needs a structured case comparing
what it costs against what it delivers, to support a go/no-go decision.

## When NOT to use this

- The decision is really about ongoing per-unit profitability, not a
  one-off investment case — use `unit-economics-breakdown` instead.

## Workflow

1. **List all real costs, not just the obvious upfront one** —
   implementation, training, ongoing maintenance, and the opportunity
   cost of the team's time spent on it instead of something else.
2. **List benefits and label each explicitly as quantified or
   qualitative.** Quantified means a real number with the calculation
   shown; qualitative means real but not easily monetized (staff
   morale, reputation, risk reduction). Don't force a qualitative
   benefit into an invented number just to make the arithmetic cleaner
   — that fabricated precision undermines the whole case once someone
   questions it.
3. **State the time horizon and whether figures are one-off or
   recurring** — a benefit that recurs annually needs to be treated
   differently from a one-time saving.
4. **Calculate the net position** (quantified benefits minus costs)
   over the stated horizon, and the payback period if relevant.
5. **State the key assumptions the case depends on, and how sensitive
   the conclusion is to them** — label each as fact, estimate, or
   assumption (same discipline as `market-sizing-tam-sam-som`), and name
   which one the conclusion is most sensitive to.
6. **Present qualitative benefits alongside the number, not buried in an
   appendix** — they're often what actually tips a close decision, even
   though they don't appear in the net-position arithmetic.

## Output format

```
## Cost-benefit analysis: [initiative]
Time horizon: [period]

### Costs
| Cost | One-off / recurring | Amount |
|---|---|---|

### Benefits — quantified
| Benefit | Calculation | Amount |
|---|---|---|

### Benefits — qualitative (real, not monetized)
- [Benefit]

### Net position
[Quantified benefits − costs, over the horizon; payback period if relevant]

### Sensitivity
Most sensitive to: [assumption]. If that assumption is wrong, the net
position becomes [range/direction].
```

## Common pitfalls

- Hiding real costs (implementation time, opportunity cost) to make the
  case look more favorable than it is.
- Forcing qualitative benefits into invented numbers instead of
  presenting them honestly alongside the quantified case.
- A single-point estimate with no sensitivity or assumption disclosure,
  hiding how fragile the conclusion actually is.

## Quality checklist

- [ ] Costs include implementation/maintenance/opportunity cost, not
      just the headline spend
- [ ] Every benefit is labeled quantified or qualitative, not blended
- [ ] Time horizon and one-off vs. recurring is stated
- [ ] The most sensitive assumption is named explicitly
