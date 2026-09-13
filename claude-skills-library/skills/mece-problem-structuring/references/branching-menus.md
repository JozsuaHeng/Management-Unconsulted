# Branching menus and worked examples

## Common top-level branching logics

| Logic | Use when | Example split |
|---|---|---|
| By driver type | Diagnosing a metric change | Demand vs. Supply vs. Price |
| By P&L line | Financial performance question | Revenue vs. Cost vs. Margin |
| By stakeholder | Something touches multiple parties | Customer vs. Internal team vs. Partner/supplier |
| By process step | A workflow or funnel is underperforming | Awareness → Inquiry → Booking → Fulfillment → Repeat |
| Internal vs. external | Unclear if the cause is controllable | Internal (controllable) vs. External (market/macro) |
| By customer segment | Performance varies by who's buying | Segment A vs. Segment B vs. Segment C |

Pick **one** logic per split. Don't blend two (e.g. "Revenue vs. Customer
complaints" mixes a P&L line with a stakeholder — they can overlap).

## Worked example: Golden Island Cruises booking drop

Question: "What is driving the drop in Q3 bookings, and what should we do?"

```
Q3 booking drop
├── Demand-side (fewer people wanting to book)
│   ├── Fewer inquiries reaching us
│   │   ├── Lower marketing/ad spend or reach this quarter
│   │   └── Seasonal dip (low season in Lombok)
│   └── Lower conversion from inquiry to booking
│       ├── Slower response time to inquiries
│       └── Quote perceived as too expensive vs. alternatives
├── Supply-side (fewer trips we could actually sell)
│   ├── Fewer available boat/date slots
│   └── Cancellations or maintenance downtime
└── Price/positioning
    ├── Priced above what the market will currently bear
    └── Losing share to a specific named competitor
```

Next step after structuring: pick the most plausible branch(es), state them
as hypotheses, and test each against actual data (inquiry volume, response
times, competitor pricing) — that's where this skill hands off to
`root-cause-five-whys` or direct data analysis, not further structuring.

## Worked example: "What should we do about rising fuel costs?"

Question reframed as a decision question: "Given rising fuel costs, what
should GIC do to protect margin?"

```
Response to rising fuel costs
├── Absorb the cost
│   └── Accept lower margin per trip
├── Pass the cost through
│   ├── Raise prices across the board
│   └── Add a fuel surcharge line item
├── Reduce fuel consumption
│   ├── Optimize routes/itineraries
│   └── Adjust boat speed/scheduling
└── Change the cost base
    ├── Renegotiate fuel supplier terms
    └── Explore fuel-efficient boat upgrades (longer-term)
```

Notice these four branches are genuinely different levers (not
overlapping) and together cover the realistic option space (exhaustive) —
that's what makes it MECE rather than just a list of ideas.
