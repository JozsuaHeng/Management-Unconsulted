---
name: mece-problem-structuring
description: Breaks an ambiguous, open-ended business question into a MECE (Mutually Exclusive, Collectively Exhaustive) issue tree so every possible cause or option is captured once and only once. Use when the user asks a broad "why" or "what should we do" question, wants to structure a problem before analyzing it, or explicitly mentions MECE, an issue tree, or problem structuring.
---

# MECE Problem Structuring

## When to use this

The user has a broad, fuzzy business question and needs it broken into
parts before it can be analyzed or answered — e.g. "why did bookings drop,"
"what should we do about rising costs," "what are our options here." The
goal is structure, not yet an answer.

## When NOT to use this

- The question is already narrow and specific (e.g. "what was our
  cancellation rate last month" — just answer it).
- The user wants a quick opinion, not a structured breakdown.
- Don't force a tree onto a problem that's genuinely simple — see
  "MECE theater" under pitfalls.

## Workflow

1. **Restate the question as a decision question.** Turn "bookings are
   down" into "what is driving the drop in bookings, and what (if
   anything) should we do about it?" A clear question makes the branching
   obvious; a vague one doesn't.
2. **Choose one branching logic for the top level** and hold it constant.
   Common choices: by driver type (e.g. Demand vs. Supply vs. Price), by
   P&L line (Revenue vs. Cost), by stakeholder (Customer vs. Internal vs.
   Partner), by process step, or by internal vs. external. Pick whichever
   makes the branches genuinely non-overlapping — see
   `references/branching-menus.md` for a fuller list with examples.
3. **Test MECE at every level before going deeper:**
   - *Mutually exclusive* — could one real-world fact belong to two
     branches? If yes, redraw the split.
   - *Collectively exhaustive* — is there an "other / none of the above"
     bucket needed? If the branches obviously don't cover everything, add
     one rather than pretend they do.
4. **Go two to three levels deep, only where it adds value.** Don't
   decompose a branch further just because you can — stop once a branch is
   specific enough to actually investigate or test.
5. **Label each end branch as a hypothesis, not a conclusion.** Each leaf
   of the tree is something to check against evidence, not something known
   to be true yet.

## Output format

A plain indented-bullet tree by default:

```
What is driving the drop in Q3 bookings?
├── Demand-side
│   ├── Fewer inquiries reaching us
│   └── Lower conversion from inquiry to booking
├── Supply-side
│   ├── Fewer available boat/date slots
│   └── Cancellations from our side
└── Price/positioning
    ├── Priced above what the market will bear
    └── Losing share to a specific competitor
```

If working in an environment that can render diagrams (e.g. an Artifact),
offer an SVG version — see `references/branching-menus.md` for layout
notes.

## Common pitfalls

- **MECE theater**: forcing a rigid tree onto something that's actually
  simple, just to look rigorous. If the honest answer fits in two
  sentences, say that instead.
- **Overlapping branches**: e.g. splitting "customer-related" and
  "pricing-related" causes — a price complaint from a customer belongs to
  both. Pick one dimension per split.
- **Mixing levels of abstraction**: putting "the market" (huge) and "one
  competitor's discount" (tiny) as siblings under the same branch.
- **Stopping at branches, never testing them**: the tree is a starting
  point for analysis, not the analysis itself — the next step is usually
  `hypothesis` testing or `root-cause-five-whys` on the most likely branch.

## Quality checklist

- [ ] Every branch is genuinely distinct from its siblings (no overlap)
- [ ] The branches together cover the full question (no obvious gap)
- [ ] Depth is only as deep as useful, not maximal
- [ ] Each leaf reads as a testable hypothesis, not a stated fact
