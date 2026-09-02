---
name: babok-requirements-elicitation
description: Elicits and documents business requirements using BABOK (Business Analysis Body of Knowledge) discipline — targeted stakeholder analysis, elicitation techniques matched to the situation, structured and traceable requirements documentation. Use when the user needs to gather or document business requirements, run a requirements elicitation process, or mentions BABOK or business analysis.
---

# BABOK Requirements Elicitation

## When to use this

A project or initiative needs its business requirements properly
gathered and documented — before design or build starts, or when
existing requirements feel too vague to build from.

## When NOT to use this

- Requirements are already clear, confirmed, and traceable — this
  skill's discipline is for the elicitation and documentation process
  itself, not for re-doing work already done well.

## Workflow

1. **Identify who actually holds the requirements knowledge** — not
   just who's most senior or available. Use `stakeholder-influence-map`
   if the stakeholder landscape is complex; the person who does the
   work daily often knows more relevant detail than their manager.
2. **Pick elicitation techniques matched to the situation, not one
   default technique for everything:**
   - **Interviews** — deep, one-on-one, good for nuance and sensitive
     topics
   - **Workshops** — good for surfacing disagreement and building shared
     understanding fast across multiple stakeholders (see
     `workshop-agenda-designer`)
   - **Document analysis** — existing process docs, systems, policies
   - **Observation** — watching the actual work happen, not just asking
     about it; often surfaces the gap between stated process and real
     process
3. **Distinguish requirement types** — conflating them produces
   documents that are either too vague to build from or too detailed
   too early:
   - **Business requirements** — the why (business objective)
   - **Stakeholder requirements** — what specific groups need
   - **Solution requirements** — functional/non-functional detail (the
     how, and only once the what is clear)
4. **Document requirements so each one is testable and traceable** back
   to a business objective — a requirement that can't be verified or
   traced isn't finished yet.
5. **Validate back with the source stakeholder** before treating a
   requirement as final — an unconfirmed requirement is a common source
   of later disputes ("that's not what I meant").

## Output format

```
## Requirements register: [project]

| ID | Requirement | Type | Source stakeholder | Traced to objective | Status |
|---|---|---|---|---|---|

### Elicitation log
| Technique | Used with | Date | Key findings |
|---|---|---|---|
```

## Common pitfalls

- Eliciting only from the most senior/available person instead of who
  actually holds the relevant knowledge.
- One elicitation technique used for everything regardless of fit
  (e.g. only interviews, missing what observation would reveal).
- Requirements written too vague to test, or too solution-prescriptive
  before the underlying need is even confirmed.
- No traceability back to a business objective, and no validation loop
  back to the source stakeholder.

## Quality checklist

- [ ] Elicitation sources include people who do the actual work, not
      just management
- [ ] Technique choice is matched to the situation, not defaulted
- [ ] Business / stakeholder / solution requirement types are kept
      distinct
- [ ] Every requirement is traceable and has been validated with its
      source
