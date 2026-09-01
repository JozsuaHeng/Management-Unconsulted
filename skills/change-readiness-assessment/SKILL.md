---
name: change-readiness-assessment
description: Assesses an organisation's or team's readiness for an upcoming change — capability gaps, sentiment, and support needs — based on real evidence rather than assumption, so the change plan addresses actual gaps. Use when the user wants to check readiness before a go-live, needs a training needs analysis, or wants to gauge how prepared people are for a change.
---

# Change Readiness Assessment

## When to use this

A change is approaching (go-live, rollout, reorg taking effect) and the
user wants to know, before it happens, whether the affected group is
actually ready — not assume readiness because no one has complained.

## When NOT to use this

- Too early — before the change is concretely defined, there's nothing
  specific to assess readiness against.
- As a one-time check with no plan to re-check closer to go-live —
  readiness can change (for better or worse) as the date approaches.

## Workflow

1. **Define readiness dimensions relevant to this change:**
   - **Capability** — do people have the skills/knowledge needed, or is
     there a training gap?
   - **Sentiment/attitude** — are people supportive, neutral, resistant?
     (Silence isn't the same as support.)
   - **Communication reach** — has the message actually reached everyone
     who needs it, in a form they've absorbed (not just "was sent")?
   - **Leadership/sponsorship support** — do people see their own
     manager visibly backing the change, not just a general
     announcement from elsewhere?
2. **Gather real evidence**, not assumption — a short survey, a few
   direct conversations, or manager input. "No one's complained" is not
   evidence of readiness.
3. **Score readiness per group/dimension**, and be specific about what's
   driving a low score — a low capability score means training is
   needed; a low sentiment score means the Desire stage (see
   `change-management-roadmap`) needs more work, not more training.
4. **Turn gaps into specific actions with owners and a deadline before
   go-live** — an assessment that doesn't lead to action is just a
   report.
5. **Re-check closer to the go-live date** if there's meaningful time
   between the assessment and launch — readiness isn't static.

## Output format

```
## Readiness assessment: [change], as of [date]

| Group | Capability | Sentiment | Communication reach | Leadership support | Overall |
|---|---|---|---|---|---|
| ... | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High | ... |

### Gaps requiring action before go-live
| Gap | Action | Owner | Deadline |
|---|---|---|---|
| ... | ... | ... | ... |

### Evidence basis
[Survey / conversations / manager input — and where this is still
assumption]
```

## Common pitfalls

- Treating absence of complaints as evidence of readiness.
- Vague "medium readiness" scores with no explanation of what's actually
  missing, making the score useless for planning action.
- Assessing once, early, and never re-checking as go-live approaches.
- Skipping sentiment/leadership-support dimensions and only checking
  capability — a technically-trained but unsupported team still
  under-adopts.

## Quality checklist

- [ ] Scores are based on real evidence (survey/conversations), not
      assumption — and that basis is stated
- [ ] Each low score has a specific driver, not just a rating
- [ ] Gaps convert into owned, dated actions
- [ ] There's a plan to re-check readiness closer to go-live if time
      allows
