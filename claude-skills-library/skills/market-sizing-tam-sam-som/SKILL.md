---
name: market-sizing-tam-sam-som
description: Builds a defensible market size estimate broken into Total Addressable Market, Serviceable Addressable Market, and Serviceable Obtainable Market, with every assumption shown explicitly rather than presented as a known fact. Use when the user asks how big a market or opportunity is, wants a TAM/SAM/SOM estimate, or is sizing a new offering before investing in it.
---

# Market Sizing (TAM / SAM / SOM)

## When to use this

The user needs a market size number — for a business case, a pitch, an
investment decision, or to judge whether an opportunity is worth pursuing.

## When NOT to use this

- Real market data already exists and is available (a market research
  report, industry association data) — use that as the primary source and
  only fall back to estimation for gaps, don't estimate what's already
  known.
- The decision doesn't actually hinge on the exact number — if a rough
  "this is clearly big enough" or "clearly too small" judgment is enough,
  a full TAM/SAM/SOM build may be more rigor than the decision needs.

## Workflow

1. **Define the three layers precisely, for this specific case:**
   - **TAM (Total Addressable Market)**: everyone who could theoretically
     want this category of product/service, if there were no constraints.
   - **SAM (Serviceable Addressable Market)**: the slice of TAM this
     specific business could realistically reach given its actual model —
     geography, channel, price point, positioning.
   - **SOM (Serviceable Obtainable Market)**: the slice of SAM this
     business could realistically capture in a defined time period, given
     competition and its own capacity/resources.
2. **Pick a build method and be explicit about which one:**
   - **Top-down**: start from a large known figure (e.g. "X million
     tourists visit Lombok/Bali per year") and narrow it with stated
     percentages at each step.
   - **Bottom-up**: start from a unit (e.g. "Y bookings per month at
     current capacity, Z if capacity doubled") and build up. Bottom-up is
     usually more defensible for SOM specifically, since it's grounded in
     actual operating capacity.
   - Where possible, do both and sanity-check that they roughly agree —
     large disagreement usually means a bad assumption somewhere.
3. **Label every number's source.** Three categories only:
   - **Fact** — from a cited source (say what the source is).
   - **Estimate** — a calculated number based on stated assumptions (show
     the calculation).
   - **Assumption** — a judgment call with no hard backing (say so plainly,
     don't dress it up as a fact).
4. **Show the math, not just the final number.** Every multiplication or
   percentage narrowing should be visible so the user (or a client) can
   challenge any one step.
5. **State the sensitivity.** If the number depends heavily on one
   uncertain assumption, say which one and what the range looks like if
   that assumption is wrong.

## Output format

```
## Market sizing: [subject]

### TAM: [number]
Method: [top-down / bottom-up]
[Calculation shown step by step, each figure labeled Fact/Estimate/Assumption]

### SAM: [number]
[Narrowing logic from TAM, e.g. geography/channel/price-point filter]

### SOM: [number]
[Narrowing logic from SAM, grounded in actual capacity/resources/timeframe]

### Sensitivity
The estimate is most sensitive to: [assumption]. If that assumption is
[X instead], SOM would be closer to [range].
```

## Common pitfalls

- Presenting an assumption as a fact — the single most common way market
  sizing loses credibility. Always disclose the weakest link.
- Confusing SAM with SOM — SAM is "could theoretically reach," SOM is
  "could actually capture given real constraints" (capacity, competition,
  time). Conflating them overstates the near-term opportunity.
- Only doing top-down — a top-down number with no bottom-up sanity check
  is easy to get wrong by an order of magnitude without noticing.
- Fabricating a source-sounding number ("studies show...") without an
  actual citation — if there's no real source, call it an assumption.

## Quality checklist

- [ ] TAM, SAM, and SOM are each defined for this specific case, not
      generic definitions
- [ ] Every number is labeled fact / estimate / assumption
- [ ] The calculation is shown, not just the result
- [ ] The most sensitive assumption is named explicitly
