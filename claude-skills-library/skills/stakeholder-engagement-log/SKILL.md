---
name: stakeholder-engagement-log
description: Maintains an ongoing, chronological log of stakeholder engagement — who was contacted, when, why, what was discussed, and what follow-up resulted — as a project runs. Use when the user needs to track engagement history over a project's life, log meeting outcomes with stakeholders, or wants a record of who's been engaged and about what, distinct from a one-time influence/interest map.
---

# Stakeholder Engagement Log

## When to use this

A project is underway with ongoing stakeholder contact, and the user
needs a running record of that contact history — not a one-time
prioritization exercise (`stakeholder-influence-map` covers that
separately, and both commonly exist side by side on a real project).

## When NOT to use this

- A one-off engagement with no ongoing relationship to track — a simple
  note is enough.
- What's actually needed is the influence/interest prioritization, not a
  history log — use `stakeholder-influence-map`.

## Workflow

1. **Log each interaction as it happens**, or as close to it as
   practical — reconstructing engagement history from memory weeks later
   loses accuracy and detail fast.
2. **Capture consistently for every entry**: who was involved (both
   sides), the date, the purpose of the contact, the actual discussion
   points (not just "had a meeting"), and the outcome or follow-up
   needed.
3. **Use it operationally, not just as a record** — before a new
   meeting with a stakeholder, check the log for prior context so the
   conversation doesn't repeat ground already covered.
4. **Review periodically for engagement gaps** — a stakeholder who
   hasn't appeared in the log for a while, especially one who's
   high-influence, is a risk worth noticing before it becomes a problem.
5. **Use it to brief new team members quickly** — a well-kept log lets
   someone joining the project understand engagement history without a
   long verbal handover.

## Output format

```
## Stakeholder engagement log: [project]

| # | Stakeholder(s) | Date | Purpose | Discussion points | Outcome / follow-up |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |
```

## Common pitfalls

- Logging in bulk after the fact instead of as engagement happens —
  detail and accuracy degrade quickly from memory.
- Vague entries ("had a catch-up") that give a future reader no useful
  context.
- Never reviewing the log for gaps — a stakeholder who's gone quiet is
  a signal, not a non-event.
- Confusing this with `stakeholder-influence-map` — the two serve
  different purposes (ongoing record vs. one-time prioritization) and a
  real project benefits from both existing together.

## Quality checklist

- [ ] Entries are logged close to when the interaction happened, not
      reconstructed later
- [ ] Every entry has specific discussion points, not a generic summary
- [ ] Outcomes/follow-ups are captured, not just that a meeting occurred
- [ ] The log is periodically reviewed for stakeholders who've gone
      quiet
