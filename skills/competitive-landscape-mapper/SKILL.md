---
name: competitive-landscape-mapper
description: Builds a structured side-by-side comparison of named competitors — positioning, pricing, offering, and ownership — with sourcing discipline and verification of who actually owns/operates what. Use when the user wants a competitor comparison, asks "who else is in this space," or wants to understand the competitive landscape before a pricing or positioning decision.
---

# Competitive Landscape Mapper

## When to use this

The user wants to compare specific named competitors against each other
and against their own business — not a general market-structure question
(that's `porters-five-forces`) and not deep research on one single
competitor (that's `competitor-research-brief`).

## When NOT to use this

- Only one competitor is in scope and the need is depth, not comparison —
  use `competitor-research-brief` instead.
- The question is about overall market attractiveness, not specific named
  players — use `porters-five-forces`.

## Workflow

1. **Check the user's own brands/entities first.** Before treating
   anything as a "competitor," confirm it isn't actually the user's own
   business under a different name or sub-brand, or a partner rather than
   a rival. This is a common mistake in market maps assembled from public
   listings.
2. **Verify ownership before listing an entity as a distinct competitor.**
   Two differently-named boats or brands are sometimes owned by the same
   operator. Where ownership can't be confirmed, mark it as unverified
   rather than presenting it as fact.
3. **Pick comparison dimensions relevant to the actual decision** — don't
   default to a generic list. For a charter/tourism business, useful
   dimensions are typically: offering (route/duration), price point,
   positioning/target customer, fleet size or scale, and review
   reputation (rating + volume). For other industries, adapt accordingly.
4. **Build the comparison as a table**, one row per competitor, one column
   per dimension, plus a row for the user's own business so the comparison
   is relative, not just descriptive of others.
5. **Prefer a static, sourced snapshot over claiming real-time accuracy.**
   Pricing and offerings change; state the date the information was
   gathered and note that it may be stale.
6. **Separate fact from inference.** "Their website lists 3 boats" is a
   fact; "they appear to target a younger backpacker segment" is an
   inference — label which is which.

## Output format

```
## Competitive landscape: [market/segment], as of [date]

| Competitor | Offering | Price point | Positioning | Scale | Reputation |
|---|---|---|---|---|---|
| [Us] | ... | ... | ... | ... | ... |
| [Competitor A] | ... | ... | ... | ... | ... |
| [Competitor B] | ... | ... | ... | ... | ... |

### Notes
- Ownership verified for: [...]. Unverified/unclear ownership: [...]
- Sources: [where each figure came from]
- Facts vs. inferences: [flag anything that's a judgment call, not a
  confirmed fact]

### So what
[1-3 sentences on what this comparison implies for positioning/pricing]
```

## Common pitfalls

- Treating the user's own sub-brand or a business partner as a competitor
  by mistake — always check this first, per `[[feedback_competitor_research_market_maps]]`-style
  discipline.
- Presenting stale or guessed pricing as current fact.
- Skipping ownership verification and double-counting one operator as two
  separate competitors.
- A comparison table with no "so what" — the point is to inform a
  decision, not just catalogue competitors.

## Quality checklist

- [ ] User's own brands/entities excluded or clearly marked if included
      for context
- [ ] Ownership verified or explicitly marked unverified
- [ ] Data snapshot dated, sources noted
- [ ] Facts and inferences clearly distinguished
- [ ] Ends with a "so what," not just a table
