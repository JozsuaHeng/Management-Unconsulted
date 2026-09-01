---
name: financial-ratio-reviewer
description: Sanity-checks basic financial statements and calculates/explains key ratios (liquidity, profitability, efficiency) in plain English, flagging anything that looks off. Use when the user wants a financial statement reviewed, asks if their numbers look healthy, or wants financial ratios calculated and explained.
---

# Financial Ratio Reviewer

## When to use this

The user has financial statements (P&L, balance sheet) or key figures and
wants to know what they indicate about the business's health — not a full
audit or formal accounting review, but a plain-English sanity check and
interpretation.

## When NOT to use this

- This isn't a substitute for a qualified accountant or auditor for
  formal filings, tax, or compliance purposes — say so if the request is
  actually for that kind of formal work.
- No real figures are available — don't fabricate financial statements to
  analyze; ask for the actual numbers or flag what's needed.

## Workflow

1. **Confirm what statements/figures are actually available.** Ratios
   need real inputs — revenue, costs, assets, liabilities, cash. Work with
   what's provided; flag which ratios can't be calculated if inputs are
   missing, rather than estimating financial figures.
2. **Calculate ratios grouped by what they measure** (see
   `references/ratio-definitions.md` for formulas):
   - **Profitability** — gross margin, net margin: is the business making
     money on what it sells?
   - **Liquidity** — current ratio, quick ratio: can short-term
     obligations be covered?
   - **Efficiency** — inventory/receivables turnover if relevant: how well
     are assets being used?
3. **Explain every ratio in plain English, not just the number.** "Current
   ratio of 1.8" means little on its own — say what it means: "for every
   $1 of short-term obligation, there's $1.80 of short-term assets to
   cover it, which is generally considered healthy."
4. **Compare to a sensible reference point** where possible — prior
   period (is it improving or declining), or a stated general benchmark
   range (with the caveat that "healthy" varies significantly by
   industry).
5. **Flag anything that looks unusual or inconsistent**, not just report
   numbers neutrally — a negative or wildly outlying ratio is worth
   calling out explicitly rather than stating flatly alongside normal
   ones.
6. **Don't give definitive medical-style diagnoses** ("the business is
   failing") — flag concerns clearly, but frame this as informed
   observation, not a certified financial assessment, and suggest a
   professional review for anything serious.

## Output format

```
## Financial review: [business/period]

### Profitability
| Ratio | Value | What it means |
|---|---|---|
| Gross margin | ...% | ... |
| Net margin | ...% | ... |

### Liquidity
| Ratio | Value | What it means |
|---|---|---|
| Current ratio | ... | ... |

### Efficiency
[if applicable]

### Flags
[Anything unusual, inconsistent, or concerning, stated plainly]

### Trend (if prior period available)
[Improving / declining / stable, and on what]

Note: this is a plain-English sanity check, not a substitute for review
by a qualified accountant, especially for anything used in formal
filings or major decisions.
```

## Common pitfalls

- Reporting a ratio number without explaining what it actually means in
  plain terms.
- Comparing to a generic benchmark without noting that "healthy" varies a
  lot by industry and business stage.
- Overstating confidence — presenting an informal review as a certified
  financial assessment.
- Calculating a ratio from incomplete or inconsistent inputs without
  flagging the limitation.

## Quality checklist

- [ ] Every ratio has a plain-English explanation, not just a number
- [ ] Missing inputs are flagged, not estimated
- [ ] Unusual findings are explicitly called out as flags
- [ ] The review is framed as a sanity check, with a note to involve a
      professional for formal/serious matters
