# Canvas layout for diagram output

When producing this as a visual (e.g. inside an Artifact or a slide), use
the traditional 3x3+1 grid layout:

```
+----------------+----------------+----------------+----------------+
| Key Partners   | Key Activities | Value          | Customer       |
|                |                | Proposition    | Relationships  |
|                +----------------+                +----------------+
|                | Key Resources  |                | Channels       |
+----------------+----------------+----------------+----------------+
| Cost Structure                  | Revenue Streams                 |
+----------------------------------+----------------------------------+
                    | Customer Segments (spans full width, right side) |
```

Simplified reading order for a text/markdown rendering (used in the main
SKILL.md output format): Customer Segments → Value Proposition → Channels
→ Relationships → Revenue → Resources → Activities → Partners → Cost. This
follows the dependency order described in the workflow, which is easier to
reason through than the traditional visual grid order.

## Worked example: Golden Island Cruises, day-trip product

- **Customer Segments**: International tourists in Lombok/Gili area
  booking 1-day boat trips, typically booking 1-2 weeks ahead via
  online research.
- **Value Proposition**: A scenic, well-run day trip with an experienced
  local crew, without the commitment or cost of a multi-day charter.
- **Channels**: Direct website booking, travel agent partnerships,
  review-platform visibility (TripAdvisor/Google).
- **Customer Relationships**: Mostly one-time, service-quality-driven;
  some repeat/referral relationship via word of mouth.
- **Revenue Streams**: Per-person day-trip fee; upsells (private charter
  upgrade, add-on activities).
- **Key Resources**: Day-trip-capable boats, trained crew, dock access,
  online booking presence/reputation.
- **Key Activities**: Trip scheduling and crewing, guest experience
  delivery, safety/maintenance, marketing and review management.
- **Key Partners**: Fuel suppliers, dock operators, travel agents,
  booking platforms.
- **Cost Structure**: Fixed (crew salaries, boat maintenance, insurance),
  variable (fuel, per-trip provisioning).

Consistency check example: if Revenue Streams shifts toward heavy discount
promotions to compete on price, that puts pressure on the "scenic,
well-run, experienced crew" Value Proposition — worth flagging as a
tension rather than assuming the two coexist fine.
