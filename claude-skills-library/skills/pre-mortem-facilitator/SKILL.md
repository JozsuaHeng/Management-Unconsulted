---
name: pre-mortem-facilitator
description: Runs a pre-mortem before a big decision, launch, or commitment — imagines it already failed, then works backward to surface risks while there's still time to act on them. Use when the user is about to make a significant decision or launch and wants to pressure-test it, or explicitly asks for a pre-mortem.
---

# Pre-Mortem Facilitator

## When to use this

There's a significant, not-yet-final decision or upcoming launch, and the
user wants to surface risks and blind spots before committing — this is
specifically framed around one upcoming decision, run once, rather than
an ongoing risk document (use `risk-register-builder` for that broader,
ongoing case).

## When NOT to use this

- The decision is small/reversible enough that a full pre-mortem is more
  process than the stakes warrant.
- The decision has already been made and executed — a pre-mortem is a
  pre-decision tool; after the fact, this becomes a post-mortem instead
  (a different, retrospective exercise, not what this skill does).

## Workflow

1. **State the decision/plan precisely.** What exactly is being decided
   or launched, and when? A vague framing produces a vague pre-mortem.
2. **Jump forward in imagination: it's [time period] later, and this
   failed.** Not "might fail" — assume it definitively failed, then work
   backward. This framing (borrowed from Gary Klein's prospective
   hindsight technique) surfaces more and more specific risks than asking
   "what could go wrong" directly, because it removes the social
   awkwardness of predicting failure and instead treats failure as an
   already-established fact to explain.
3. **Generate specific reasons it failed** — not vague ("bad luck") but
   concrete and plausible ("the scouting trip revealed the dock wasn't
   viable, but we'd already started marketing the route"). Push for
   several distinct reasons, not just the first one that comes to mind.
4. **For each reason, ask: was this foreseeable now?** Most pre-mortem
   value comes from reasons that, once said out loud, were clearly
   foreseeable — those are the ones worth acting on before committing.
5. **For each foreseeable reason, define a concrete pre-commitment
   safeguard** — a specific check, threshold, or sequencing change made
   now, before the decision is executed, not a vague "we'll be careful."
6. **Note what's genuinely unforeseeable or low-probability** too — not
   every imagined failure needs a safeguard; separating "worth acting on
   now" from "acceptable risk" keeps the exercise useful rather than
   paralyzing.

## Output format

```
## Pre-mortem: [decision/plan]

**The scenario**: It's [time period] later. [Decision] has failed.

### Reasons it failed
1. [Specific, concrete reason] — Foreseeable now: Yes/No
2. [Specific, concrete reason] — Foreseeable now: Yes/No
...

### Safeguards to put in place now
- [For each "Yes" reason] [Specific pre-commitment action]

### Accepted risks (foreseeable but not acted on, or genuinely
unforeseeable)
- [Reason] — [why it's being accepted as-is]
```

## Common pitfalls

- Staying vague ("it could fail if things go wrong") instead of forcing
  specific, plausible failure stories.
- Treating every imagined failure as equally worth a safeguard, instead
  of separating foreseeable-and-actionable from genuinely low-probability
  or unforeseeable.
- Vague safeguards ("we'll monitor closely") instead of a specific
  pre-commitment action taken before execution.
- Running this after the decision is already committed, when it can no
  longer change the plan.

## Quality checklist

- [ ] The failure scenario is stated as a definite past event, not a
      hedge ("might fail")
- [ ] Reasons are specific and plausible, not vague
- [ ] Each reason is marked foreseeable or not
- [ ] Foreseeable reasons get a specific, concrete safeguard — not a
      vague intention
