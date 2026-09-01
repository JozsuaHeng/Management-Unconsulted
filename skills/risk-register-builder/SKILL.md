---
name: risk-register-builder
description: Builds a structured risk register — risk, likelihood, impact, mitigation, and owner — for a project, decision, or ongoing operation. Use when the user asks what could go wrong, wants a risk assessment, or needs to document risks before a decision or launch.
---

# Risk Register Builder

## When to use this

The user needs a structured, documented view of what could go wrong with
a project, decision, launch, or ongoing operation — more formal and
ongoing than a one-time `pre-mortem-facilitator` session (which is
specifically framed around a single upcoming decision).

## When NOT to use this

- A single upcoming decision needs a quick pressure-test, not an ongoing
  document — `pre-mortem-facilitator` is a better fit for that framing.
- Risks are already well understood and documented — update the existing
  register rather than rebuilding from scratch.

## Workflow

1. **Scope the register clearly** — one project, one decision, or one
   operating area. A register that tries to cover everything becomes
   unusable.
2. **Brainstorm risks broadly before scoring anything** — pulling from
   multiple categories (operational, financial, reputational, regulatory/
   legal, market/external) so nothing obvious gets missed by only
   thinking from one angle.
3. **For each risk, rate likelihood and impact** — a simple High/Medium/
   Low scale is usually sufficient; avoid false precision with numeric
   scores unless the user specifically wants a scoring model.
4. **Prioritize by the combination**, not either dimension alone — a
   high-likelihood, low-impact risk and a low-likelihood, high-impact
   risk need very different handling, and both differ from a risk that's
   low on both (worth noting, not worth much effort).
5. **Write a specific mitigation for each risk that's Medium or High on
   either dimension** — a mitigation should be an actual action, not a
   restatement of the risk ("monitor closely" is weak; "set a trigger
   threshold and a named backup plan" is specific).
6. **Assign an owner to each risk with a mitigation** — an unowned risk
   tends not to get managed.
7. **Note which risks are worth actively managing vs. simply accepting**
   — not every risk needs a mitigation plan; low-likelihood, low-impact
   risks can often just be accepted and monitored.

## Output format

```
## Risk register: [project/decision/area]

| Risk | Category | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| ... | Operational/Financial/Reputational/Regulatory/Market | H/M/L | H/M/L | ... | ... |

### Top priorities
[The 2-3 risks that combine highest likelihood and impact — call these
out explicitly, don't leave them buried in the table]

### Accepted risks (monitored, not actively mitigated)
[Low/low risks worth naming but not over-investing in]
```

## Common pitfalls

- Brainstorming risks from only one angle (e.g. only operational),
  missing reputational or regulatory risks entirely.
- Vague mitigations that don't describe an actual action.
- No owner assigned, so nothing actually gets managed.
- Treating every risk as equally worth mitigation effort instead of
  prioritizing by likelihood × impact.

## Quality checklist

- [ ] Risks brainstormed across multiple categories, not just one
- [ ] Likelihood and impact both rated, with combination used to
      prioritize
- [ ] Each Medium/High risk has a specific, actionable mitigation and a
      named owner
- [ ] Low-priority risks are explicitly marked as accepted/monitored,
      not left ambiguous
