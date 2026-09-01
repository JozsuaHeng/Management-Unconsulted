---
name: impact-effort-prioritizer
description: Scores a list of initiatives, ideas, or fixes on impact versus effort and recommends what to tackle first. Use when the user has more ideas or possible initiatives than time to do them all and needs help deciding what to prioritize.
---

# Impact/Effort Prioritizer

## When to use this

There's a list of possible initiatives, fixes, or ideas — more than can
realistically all be done at once — and the user needs a structured way
to decide what to do first.

## When NOT to use this

- Only one or two options exist — a full matrix is unnecessary ceremony
  for a two-way choice; just reason through it directly.
- The items aren't actually comparable (wildly different time horizons or
  categories) — group into comparable sets first, or the ranking will be
  misleading.

## Workflow

1. **List every candidate initiative clearly** — specific enough to
   actually estimate impact and effort for (not "improve marketing" but
   "run a targeted ad campaign for the low season").
2. **Rate Impact**: what real difference would this make if done well?
   Consider magnitude (how big) and confidence (how sure is this estimate)
   separately if impact estimates are especially uncertain — a
   high-magnitude but low-confidence item shouldn't be treated the same
   as a high-magnitude, high-confidence one.
3. **Rate Effort**: how much time, money, or organizational complexity
   does this actually take? Include ramp-up/coordination effort, not just
   raw hours of work.
4. **Plot into the four quadrants:**
   - High impact, low effort → **Do first** (quick wins)
   - High impact, high effort → **Plan carefully** (worth doing, needs a
     real plan and likely staged execution)
   - Low impact, low effort → **Do if there's slack time** (fine to do,
     not a priority)
   - Low impact, high effort → **Don't do** (or deprioritize explicitly,
     rather than leaving it ambiguously on the list forever)
5. **Recommend a sequence, not just a quadrant placement** — quick wins
   first (builds momentum and frees capacity), then the highest-value
   high-effort item, staged appropriately.
6. **Flag any item where impact is highly uncertain** — recommend a small,
   low-cost validation step before committing full effort, rather than
   guessing at impact and going straight to a big investment.

## Output format

```
## Prioritization: [list/context]

| Initiative | Impact | Effort | Quadrant | Notes |
|---|---|---|---|---|
| ... | High/Low | High/Low | ... | ... |

### Recommended sequence
1. [Quick win first]
2. [Next highest-value item]
...

### Deprioritized (low impact, high effort)
[Items explicitly set aside, so they don't linger ambiguously]
```

## Common pitfalls

- Vague initiatives that can't actually be rated for impact or effort.
- Treating impact estimates as equally certain when some are
  well-grounded and others are pure guesses.
- Listing everything in a quadrant without a recommended sequence — the
  matrix alone doesn't tell someone what to actually do Monday morning.
- Leaving low-impact/high-effort items on the list indefinitely instead of
  explicitly deprioritizing them.

## Quality checklist

- [ ] Each initiative is specific enough to rate meaningfully
- [ ] Impact and effort ratings have a stated reason, not just a gut call
- [ ] Output includes a recommended sequence, not just a static matrix
- [ ] Low-priority items are explicitly set aside, not left ambiguous
