# Worked example: sizing a new multi-day Gili route

This uses invented illustrative figures to show the *method* — any real
use of this skill should replace every number with sourced or clearly
labeled current data, not reuse these.

### TAM (top-down)
"Annual international tourist arrivals to Lombok" — **Fact** (if pulled
from a cited tourism board / BPS statistics figure, cite it here).
→ Multiply by "% who take any boat/marine tour during their visit" —
**Estimate**, based on a stated source or comparable-market benchmark, or
**Assumption** if no source exists — label whichever it actually is.

### SAM (narrowing from TAM)
Filter TAM down by:
- Only tourists whose trip length and budget fit a multi-day charter
  (narrows by trip type) — **Assumption** unless backed by booking-platform
  or survey data.
- Only tourists reachable through GIC's actual channels (website,
  existing agent partners, review platforms) — **Assumption**, since
  channel reach isn't precisely measurable without ad platform data.

### SOM (bottom-up, grounded in real capacity)
Build from GIC's actual operating constraints, not a percentage guess:
- Number of boats that could realistically be allocated to the new route
  — **Fact** (known internally).
- Trips per month each boat could run on this route, given crew and
  maintenance schedules — **Fact/Estimate** (known internally, or a
  reasonable estimate if the route is new).
- Guests per trip × price → monthly revenue capacity — **Estimate**
  (calculation from the above facts).
- Realistic booking/fill rate in year one, given it's a new route with no
  track record — **Assumption**, and probably the single most uncertain
  number in the whole build.

### Sensitivity note
In a build like this, SOM is almost always most sensitive to the **fill
rate assumption** in year one, not to TAM or SAM — because SOM is
capacity-constrained, not demand-constrained, in a new small route. That's
worth stating explicitly: "even if SAM is off by 2x, SOM barely changes,
because the real constraint is boats and crew, not addressable demand."
This is the kind of insight a mechanical percentage-narrowing exercise
would miss, but naming it is exactly what makes the sizing useful for a
real decision.
