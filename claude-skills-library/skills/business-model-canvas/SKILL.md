---
name: business-model-canvas
description: Maps or redesigns a business's value proposition, customer segments, channels, relationships, revenue streams, key resources, activities, partners, and cost structure on one page. Use when the user wants to understand how a business makes money, evaluate a new business model, or redesign an existing offering.
---

# Business Model Canvas

## When to use this

The user wants a whole-business (or whole-offering) view of how value is
created, delivered, and captured — e.g. "how does this business actually
make money," "help me design a new offering," "what would change if we
added a subscription model."

## When NOT to use this

- The question is only about pricing — use `pricing`-adjacent reasoning
  directly or `unit-economics-breakdown` for the numbers.
- The question is about competitive position, not the business's own
  model — use `swot-strategic-review` or `porters-five-forces`.

## Workflow

1. **Confirm the subject**: the whole company, or one specific offering
   (e.g. "GIC's day-trip product" vs. "GIC as a whole"). Different
   offerings within one business can have different canvases.
2. **Fill the nine building blocks**, in this order (each depends on the
   ones before it, so this order avoids circular reasoning):
   1. **Customer Segments** — who is this for, specifically (not "tourists"
      but "honeymooning couples booking 3+ day trips" if that's the real
      segment).
   2. **Value Proposition** — what problem is solved or need met, for each
      segment, and why choose this over alternatives.
   3. **Channels** — how customers find out about, evaluate, buy, and
      receive the offering (marketing, booking platform, referral, direct).
   4. **Customer Relationships** — how the relationship is built and kept
      (personal service, self-service, community, automated).
   5. **Revenue Streams** — how money actually comes in (one-time booking
      fee, tiered pricing, add-ons, deposits) and from which segments.
   6. **Key Resources** — what's essential to deliver the value prop
      (boats, crew, dock access, brand/reputation, booking system).
   7. **Key Activities** — what the business must actively do well
      (route planning, guest experience delivery, maintenance, marketing).
   8. **Key Partners** — who's relied on externally (fuel suppliers, dock
      operators, booking platforms, tour agents).
   9. **Cost Structure** — what actually drives cost (fixed: boat
      maintenance, crew salaries; variable: fuel, provisioning per trip).
3. **Check for internal consistency.** The Value Proposition should
   plausibly justify the Revenue Streams; Key Resources/Activities should
   plausibly be able to deliver the Value Proposition; Cost Structure
   should reflect the Key Resources/Activities actually listed.
4. **If redesigning (not just mapping)**, isolate which block(s) are
   changing and trace the consequence through the other eight — a new
   Revenue Stream (e.g. adding subscriptions) usually forces changes to
   Customer Relationships and Channels too.

## Output format

```
## Business Model Canvas: [subject]

**Customer Segments**: ...
**Value Proposition**: ...
**Channels**: ...
**Customer Relationships**: ...
**Revenue Streams**: ...
**Key Resources**: ...
**Key Activities**: ...
**Key Partners**: ...
**Cost Structure**: ...

### Consistency check
[Any block that doesn't line up with the others, flagged explicitly]
```

A 3x3 grid layout (the traditional canvas visual) can be offered instead if
working in a context that renders diagrams well — see
`references/canvas-layout.md`.

## Common pitfalls

- Vague customer segments ("everyone," "tourists") that make every other
  block impossible to make specific.
- Filling blocks independently without checking they're mutually
  consistent (a "premium personalized service" value prop paired with a
  "self-service, lowest cost" cost structure is a contradiction worth
  flagging).
- Treating this as a one-time exercise rather than something to revisit
  when a business changes what it sells or who it sells to.

## Quality checklist

- [ ] Customer segments are specific, not generic
- [ ] Value proposition explains why this segment chooses this over
      alternatives
- [ ] All nine blocks are filled and internally consistent
- [ ] Any contradiction between blocks is explicitly flagged, not
      smoothed over
