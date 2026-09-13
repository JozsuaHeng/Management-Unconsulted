---
name: meeting-notes-to-actions
description: Turns raw meeting notes or a transcript into a clean record of decisions made and action items with owners and dates. Use when the user has meeting notes/transcript to process, asks what was decided, or wants action items pulled out of a conversation.
---

# Meeting Notes to Actions

## When to use this

There's raw, messy meeting content (notes or a transcript) and the user
needs it turned into something usable afterward: what was decided, and
what needs to happen next.

## When NOT to use this

- The user wants a full narrative summary of the discussion, not action
  extraction — this skill optimizes for decisions/actions, not a
  blow-by-blow account (though a short context section is included).
- There's no actual content yet (the meeting hasn't happened) — this
  processes existing notes, it doesn't generate an agenda (that's a
  simpler, separate task).

## Workflow

1. **Read through fully before extracting anything** — decisions and
   action items are often stated informally or revisited later in the
   conversation, so pulling from the first mention alone can miss a later
   correction or change of plan.
2. **Separate three distinct things**, since they get conflated easily:
   - **Decisions made** — something was actually settled, not just
     discussed
   - **Action items** — someone needs to do something specific
   - **Open questions** — raised but not resolved, still needs follow-up
3. **Every action item needs an owner and, if stated or inferable, a
   date.** If a task was mentioned with no clear owner, flag it as
   "owner not assigned" rather than guessing who's responsible.
4. **Write action items as concrete tasks, not topics** — "follow up with
   the Gili dock contact by Friday" not "Gili route logistics."
5. **Don't invent a decision that wasn't actually made.** If something was
   discussed but left open, it belongs in Open Questions, not Decisions —
   conflating "discussed" with "decided" causes real confusion later.
6. **Keep a brief context line** (1-2 sentences) so the output makes sense
   without needing the original notes, but don't reproduce the whole
   conversation.

## Output format

```
## Meeting summary: [topic/date]

**Context**: [1-2 sentence summary of what the meeting was about]

### Decisions made
- [Decision, stated as settled fact]

### Action items
- [ ] [Task] — Owner: [name or "not assigned"] — Due: [date or "not set"]

### Open questions
- [Question still unresolved, needs follow-up]
```

## Common pitfalls

- Treating something discussed-but-unresolved as a decision.
- Action items with no owner, left unassigned instead of flagged.
- Vague action items that can't actually be checked off as done.
- Missing a decision or task mentioned only once, mid-conversation,
  because extraction stopped after a first pass.

## Quality checklist

- [ ] Decisions, actions, and open questions are kept clearly separate
- [ ] Every action item has an owner (or is flagged as unassigned) and a
      due date (or flagged as not set)
- [ ] Action items are concrete, checkable tasks, not topic labels
- [ ] Nothing is stated as decided that was actually left open
