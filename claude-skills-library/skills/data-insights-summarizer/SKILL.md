---
name: data-insights-summarizer
description: Turns a dataset, survey export, or KPI report into a structured summary of what actually matters — key findings, notable patterns, and what's not clear from the data — instead of just restating numbers. Use when the user has raw data (survey results, a KPI export, a spreadsheet) and wants it summarized into insights, not just described.
---

# Data Insights Summarizer

## When to use this

There's raw data — survey results, a KPI export, a spreadsheet — and the
user wants a summary that tells them what it means, not a column-by-
column restatement of the numbers.

## When NOT to use this

- The data hasn't actually been provided or described yet — ask for it
  or the relevant figures rather than inventing plausible-sounding
  findings.

## Workflow

1. **Separate "what the data shows" from "what it means"** and label
   which is which throughout. The first is descriptive fact; the second
   is interpretation — both are useful, but blending them without
   labeling misleads a reader into treating a judgment call as a fact.
2. **Prioritize findings that would actually change a decision**, not
   every statistically-notable blip. A 2% quarter-over-quarter wobble in
   a noisy metric usually isn't worth leading with.
3. **Look for what's surprising or contradicts an assumption.** Routine,
   expected numbers are less valuable to highlight than something a
   reader wouldn't have predicted — that's usually where the real
   insight is.
4. **State sample size and data quality caveats explicitly.** A finding
   from 12 survey responses carries different weight than one from
   1,200 — say so rather than presenting both with equal confidence.
5. **State what the data does NOT tell you or leaves ambiguous.** This
   is as valuable as what it does show, and is the part most often
   skipped — a reader left overconfident by an incomplete picture is a
   real risk.
6. **Lead with the "so what"** (Pyramid Principle logic — see
   `executive-summary-writer`), not a walkthrough of every column in
   the order they appear in the spreadsheet.

## Output format

```
## Insights summary: [dataset/source]

**Headline finding**: [the single most decision-relevant takeaway]

### Supporting findings
- [Finding] — Fact / Interpretation
- [Finding] — Fact / Interpretation

### Data quality notes
[Sample size, known gaps, anything affecting how much weight to put on
this]

### What this doesn't tell us
[Real limits/ambiguity — don't overclaim]
```

## Common pitfalls

- Restating raw numbers ("column X averaged Y") without interpreting
  what they mean for a decision.
- Treating a small-sample or noisy finding with the same confidence as
  a robust, well-supported one.
- Omitting what the data can't tell you, leaving the reader more
  confident in the conclusion than the data actually supports.

## Quality checklist

- [ ] Fact and interpretation are labeled separately throughout
- [ ] Findings are prioritized by decision relevance, not just
      statistical notability
- [ ] Sample size / data quality is stated
- [ ] What the data does NOT show is stated explicitly, not omitted
