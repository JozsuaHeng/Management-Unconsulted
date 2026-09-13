---
name: unit-economics-breakdown
description: Breaks revenue and cost down per unit (per trip, per guest, per customer, per order) to show what's actually profitable, separating fixed from variable costs. Use when the user wants to know if a specific offering, trip, or customer segment is actually profitable, or wants to compare profitability across offerings.
---

# Unit Economics Breakdown

## When to use this

The user wants to know whether a specific thing they sell is actually
profitable on its own — not overall company profitability (that's a
broader P&L question), but the economics of one unit: one trip, one
guest, one customer, one order.

## When NOT to use this

- The question is about overall company financial health, not one
  offering — use `financial-ratio-reviewer`.
- Cost data isn't actually available — flag what's needed rather than
  guessing at cost figures.

## Workflow

1. **Define the unit precisely.** "Per trip," "per guest," "per booking" —
   pick one and stay consistent, since mixing units (e.g. some costs
   allocated per trip, others per guest) produces a misleading result.
2. **Separate variable costs from fixed costs, explicitly.**
   - **Variable costs**: scale directly with each unit (fuel per trip,
     food/provisioning per guest, per-booking platform fees).
   - **Fixed costs**: don't change with volume in the short term (boat
     maintenance, crew base salary, insurance, dock fees) — these should
     be allocated across expected volume, not charged to a single unit as
     if they were variable.
3. **Calculate contribution margin first**: revenue per unit minus
   variable cost per unit. This shows what each additional unit actually
   contributes toward covering fixed costs and profit — the single most
   useful number for "should we sell more of this."
4. **Then allocate fixed costs** across expected volume to get a fully-
   loaded per-unit cost and true profit per unit — useful for "is this
   offering worth keeping at all," a different question from contribution
   margin.
5. **Show both numbers, and be clear about what each answers:**
   - Contribution margin → "is it worth selling one more?"
   - Fully-loaded profit per unit → "is this offering worth running at
     all, given the fixed costs it must help cover?"
6. **Flag if any cost input is an estimate rather than an actual figure.**

## Output format

```
## Unit economics: [offering], per [unit]

**Revenue per unit**: [amount]

**Variable costs per unit**:
- [Cost item]: [amount]
- ...
Total variable cost: [amount]

**Contribution margin per unit**: [revenue - variable cost] ([%] margin)

**Fixed costs allocated** (based on [expected volume] units/period):
- [Cost item]: [amount allocated per unit]
- ...
Total fixed cost per unit: [amount]

**Fully-loaded profit per unit**: [contribution margin - fixed cost
allocation]

### So what
[Whether this is worth selling more of, keeping, or reconsidering, and why]
```

## Common pitfalls

- Mixing fixed and variable costs together without distinction — hides
  whether the real problem is per-unit economics or overall volume/scale.
- Charging a fixed cost as if it were variable (e.g. dividing annual
  insurance by trips-so-far instead of expected annual volume) — distorts
  the picture, especially early in a season.
- Confusing contribution margin with true profit — a positive contribution
  margin can still mean the offering loses money overall if fixed costs
  aren't covered by volume.
- Using invented cost figures instead of flagging what real data is
  needed.

## Quality checklist

- [ ] Unit is defined precisely and used consistently throughout
- [ ] Fixed and variable costs are clearly separated
- [ ] Both contribution margin and fully-loaded profit are shown, labeled
      for what each answers
- [ ] Any estimated (vs. actual) cost input is flagged
