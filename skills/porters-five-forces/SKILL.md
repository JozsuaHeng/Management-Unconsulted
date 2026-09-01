---
name: porters-five-forces
description: Assesses competitive intensity in a market or industry across five forces (rivalry, buyer power, supplier power, threat of new entrants, threat of substitutes) to judge whether a market is structurally attractive to enter, defend, or exit. Use when evaluating market entry, industry attractiveness, or why margins in a market are compressed.
---

# Porter's Five Forces

## When to use this

The user is asking a structural question about a market — "is this market
worth entering," "why are margins so thin in this industry," "how
defensible is our position" — not a question about one specific
competitor (use `competitive-landscape-mapper` for that) or about internal
capability (use `swot-strategic-review` for that).

## When NOT to use this

- The question is about one specific competitor's move — that's
  competitive analysis, not industry structure.
- The market is extremely narrow or personal-scale (e.g. "should I raise
  my own freelance rate") — five forces is built for industry-level
  questions, not individual pricing decisions.

## Workflow

1. **Define the market boundary precisely.** "Tourism" is too broad;
   "multi-day phinisi charter tours out of Lombok" is analyzable. A vague
   boundary makes every force impossible to assess honestly.
2. **Work through each force, and for each, state the finding as
   High / Medium / Low intensity plus the reason:**
   - **Rivalry among existing competitors** — how many players, how
     similar their offerings, how much they compete on price vs.
     differentiation.
   - **Bargaining power of buyers (customers)** — how easily customers can
     switch, compare prices, or negotiate. Concentrated, price-sensitive
     buyers = high power.
   - **Bargaining power of suppliers** — how much leverage the people you
     buy from (fuel, dock access, crew labor market, boat builders) have
     over you.
   - **Threat of new entrants** — how hard it is for someone new to start
     competing. Capital requirements, licensing, reputation-building time,
     access to key assets (boats, docks) all raise this barrier.
   - **Threat of substitutes** — not direct competitors, but different
     ways to meet the same underlying need (e.g. a resort stay instead of
     a boat charter; a day-trip instead of overnight).
3. **Synthesize, don't just list five ratings.** State the 1-2 forces that
   actually matter most for this business right now, and what that implies
   (e.g. "rivalry and substitute threat are the two real pressures here;
   supplier and buyer power are low — so competing on differentiation
   matters more than cost").
4. **Separate facts from assumptions.** If entrant barriers or buyer power
   aren't actually known, say "assumed" and flag it as something to verify,
   rather than asserting it with false confidence.

## Output format

```
## Five Forces: [market, precisely defined]

| Force | Intensity | Why |
|---|---|---|
| Rivalry among competitors | High/Med/Low | ... |
| Buyer power | High/Med/Low | ... |
| Supplier power | High/Med/Low | ... |
| Threat of new entrants | High/Med/Low | ... |
| Threat of substitutes | High/Med/Low | ... |

### What this means
[1-2 forces that matter most, and the strategic implication]
```

## Common pitfalls

- Treating all five forces as equally important — usually one or two
  dominate; naming them is the actual insight.
- Confusing "competitors" (rivalry) with "substitutes" — a rival phinisi
  operator is rivalry; a resort or a plane ticket to a different
  destination is a substitute.
- Doing the analysis and stopping at ratings without a "so what" for the
  business's actual strategy.
- Asserting entrant barriers or supplier power without evidence — these
  are the two forces most often guessed rather than known.

## Quality checklist

- [ ] Market boundary is specific enough to actually assess
- [ ] Each force has a stated reason, not just a rating
- [ ] Facts vs. assumptions are labeled
- [ ] Synthesis names which 1-2 forces matter most and why
