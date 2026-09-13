---
name: competitor-research-brief
description: Produces a structured secondary-research brief on a single named competitor, with strict fact/estimate/assumption labeling and sourcing. Use when the user wants deep research on one specific competitor, asks "what do we know about [company]," or needs a research brief before a strategic decision.
---

# Competitor Research Brief

## When to use this

The user wants depth on one specific, named competitor — not a comparison
across several (use `competitive-landscape-mapper` for that).

## When NOT to use this

- Multiple competitors need comparing side by side — use
  `competitive-landscape-mapper`.
- The research would require private/confidential data not publicly
  available — this skill is for secondary (publicly available) research;
  say so if the ask requires information that can't legitimately be
  obtained this way.

## Workflow

1. **Confirm exactly which entity is being researched**, including
   checking it isn't the user's own brand or a partner under a different
   name — verify this before treating anything as a competitor finding.
2. **Structure the brief around fixed sections** so it's comparable across
   different competitor briefs done at different times:
   - Overview (what they do, since when, scale if known)
   - Offering (products/services, how they're positioned)
   - Pricing (if publicly available — note if it isn't)
   - Target customer / positioning
   - Strengths (from the user's business's perspective — what makes them
     a real threat)
   - Weaknesses / vulnerabilities (if any are actually evident)
   - Recent moves (anything notably new: launches, pricing changes,
     expansion)
3. **Label every claim fact / estimate / assumption**, with a source noted
   for facts. If something can't be verified, say so rather than filling
   the gap with a plausible-sounding guess.
4. **Note the date the research was done** — competitor information ages
   quickly, and a brief without a date invites false confidence later.
5. **End with implications for the user's business**, not just a
   description of the competitor — the brief should answer "so what does
   this mean for us," not just "here's what they do."

## Output format

```
## Competitor brief: [Name], as of [date]

**Overview**: ...
**Offering**: ...
**Pricing**: ... (or "not publicly available")
**Target customer / positioning**: ...
**Strengths**: ...
**Weaknesses / vulnerabilities**: ... (only if genuinely evident, not
invented for balance)
**Recent moves**: ...

**Sources**: [list]
**Facts vs. assumptions**: [flag anything not directly sourced]

### So what for us
[Implications for the user's own strategy/positioning]
```

## Common pitfalls

- Mistaking the user's own brand, sub-brand, or a partner for a
  competitor — always verify identity/ownership first.
- Inventing a "weaknesses" section for balance when none are actually
  evident — an honest "no clear weaknesses observed" is better than a
  fabricated one.
- Presenting outdated or unsourced pricing as current fact.
- Stopping at description without the "so what" for the user's own
  business.

## Quality checklist

- [ ] Competitor identity/ownership verified, not assumed
- [ ] Every claim is labeled fact/estimate/assumption with sources for
      facts
- [ ] Research date is stated
- [ ] Brief ends with implications for the user's own strategy
