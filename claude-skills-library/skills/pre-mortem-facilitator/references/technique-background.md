# Background: prospective hindsight

The pre-mortem technique comes from psychologist Gary Klein. The core
mechanism: asking "what could go wrong?" invites hedged, generic answers,
because predicting failure feels like betting against the plan (socially
uncomfortable, especially in a group). Asking people to imagine failure
has *already happened* and explain *why* removes that social friction —
it becomes a storytelling/explaining exercise rather than a prediction,
and people are much more willing (and specific) when explaining an
assumed fact than when speculating about a possibility.

## Worked example: launching the new Gili multi-day route

**The scenario**: It's six months from now. The Gili route launch has
failed — bookings never took off and it's being quietly discontinued.

### Reasons it failed
1. The scouting trip revealed mooring/logistics issues that weren't
   resolved before the route was publicly marketed. — Foreseeable now:
   Yes
2. Pricing was set without checking unit economics, and margin was too
   thin to sustain marketing spend. — Foreseeable now: Yes
3. A well-funded competitor launched a similar route first and captured
   early demand. — Foreseeable now: Partially (competitor timing itself
   isn't controllable, but being slow to market after knowing a
   competitor might move is)
4. A major regional event (e.g. unusual weather pattern) disrupted the
   whole first season. — Foreseeable now: No — genuinely low-probability
   and not specifically foreseeable

### Safeguards to put in place now
- Don't begin public marketing until the scouting trip is complete and
  any logistics issues are resolved (sequencing safeguard, directly
  prevents reason 1).
- Run `unit-economics-breakdown` on proposed pricing before it's finalized,
  not after (directly prevents reason 2).
- Set an internal target date for going to market and treat schedule
  slippage past it as a flag to reassess, given competitive timing risk
  (partial mitigation for reason 3).

### Accepted risks
- Regional weather/event disruption (reason 4) is accepted as a general
  business risk, not specifically addressed by this launch's safeguards —
  it's the kind of risk better handled by overall business resilience
  (e.g. not over-relying on any single route) than a launch-specific fix.

Notice the pattern: two of the four reasons turned into concrete,
immediate actions; one turned into a partial timing safeguard; one was
consciously accepted rather than forced into an unnecessary mitigation.
