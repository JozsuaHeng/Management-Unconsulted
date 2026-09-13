---
name: benchmark-comparator
description: Compares a business's own metrics or offering against named, cited benchmarks instead of vague "industry standard" claims. Use when the user asks how they compare to industry, whether a number is normal, or wants to benchmark performance/pricing against known reference points.
---

# Benchmark Comparator

## When to use this

The user has a specific metric or practice (a price, a conversion rate, a
response time, a margin) and wants to know if it's good, bad, or normal
relative to something real — not a vague sense of "the industry."

## When NOT to use this

- No real benchmark data exists or is accessible, and none can be found —
  say so plainly rather than inventing an "industry standard" figure. A
  benchmark comparator without an actual benchmark isn't useful; it's
  guessing dressed up as analysis.
- The comparison being asked for is really a competitor comparison (one
  specific competitor) — use `competitive-landscape-mapper` or
  `competitor-research-brief` instead.

## Workflow

1. **State exactly what's being benchmarked and why it matters.** "Our
   response time" is vague; "average time from inquiry to first response"
   is benchmarkable.
2. **Find or ask for a real reference point.** Options, roughly in order
   of reliability:
   - A cited industry report or association statistic
   - A named comparable business's publicly disclosed number (rare, but
     sometimes available)
   - Multiple data points averaged from public sources (e.g. several
     competitors' listed response commitments) to construct a rough range
   - If none of the above is available, say explicitly that no reliable
     benchmark exists, rather than presenting a guess as one.
3. **Compare like-for-like.** Check that definitions match — "response
   time" measured differently by two sources isn't a fair comparison; flag
   any definitional mismatch rather than comparing anyway.
4. **State the comparison, then the "so what."** A number sitting next to
   another number isn't insight until it's connected to whether that gap
   matters and what (if anything) to do about it.
5. **Avoid false precision.** If the benchmark itself is a rough estimate
   (built from a few public data points), say the comparison is
   directional, not exact — don't present "we're 23% below industry
   average" when the underlying data doesn't support that precision.

## Output format

```
## Benchmark: [metric], [business] vs. [reference point]

**Our number**: [value] (source/method)
**Benchmark**: [value] (source/method, or "no reliable benchmark found")
**Comparison**: [above/below/in line, with actual magnitude]
**Confidence**: [high — cited source / moderate — constructed estimate /
low — directional only]

### So what
[What this comparison implies, if anything actionable]
```

## Common pitfalls

- Citing a vague "industry standard" with no actual source — the single
  most common way benchmarking becomes fake rigor.
- Comparing two numbers measured differently without flagging the
  mismatch.
- Overstating precision from a rough, self-constructed benchmark.
- Producing a comparison with no "so what" — a number next to another
  number isn't yet an insight.

## Quality checklist

- [ ] The benchmark has a real, stated source or is explicitly labeled as
      unavailable
- [ ] Definitions are checked to be comparable, mismatches flagged
- [ ] Confidence level in the benchmark is stated
- [ ] Comparison ends with a "so what," not just the numbers
