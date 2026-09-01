---
name: discovery-interview-kit
description: Generates a discovery interview guide (for customers, clients, or stakeholders) before interviews happen, and synthesizes raw notes or transcripts into themes afterward. Use when the user needs an interview guide, customer/client discovery questions, or wants to synthesize interview notes into findings.
---

# Discovery Interview Kit

## When to use this

Two related situations trigger this skill:
1. **Before interviews**: the user needs a guide of questions to ask
   customers, clients, or internal stakeholders to learn something
   specific.
2. **After interviews**: the user has raw notes or transcripts from
   several interviews and needs them synthesized into themes/findings.

## When NOT to use this

- The user already knows the answer and just needs to confirm it with one
  person — a full discovery guide is overkill for a single confirmatory
  question.
- Synthesizing a single interview (not multiple) — that's closer to
  straightforward notes summarization than theme synthesis across
  sources.

## Workflow — building the guide

1. **Start from the learning objective, not the questions.** What
   decision will this interview inform? If that's unclear, the guide will
   wander.
2. **Write open-ended questions, not leading or yes/no ones.** "What made
   you choose us over other options?" not "Did you choose us because of
   our pricing?" — leading questions bias the answer before it's given.
3. **Order questions broad-to-narrow.** Start with open context
   ("Walk me through how you typically...") before narrowing to specific
   topics — narrow questions asked first anchor the interviewee and lose
   the broader context.
4. **Include a few "why" follow-ups** built into the guide itself, not
   just the top-level questions — the follow-up is often where the real
   insight comes from.
5. **Keep the guide to 8-12 core questions** for a ~30-45 minute
   interview — more than that and interviews run long or get shallow.

## Workflow — synthesizing notes afterward

1. **Read across all interviews before grouping anything** — don't
   theme-code the first interview in isolation, since patterns only
   emerge in comparison.
2. **Group into themes by what was actually said**, not by the original
   question order — a theme might span answers to several different
   questions.
3. **Note how many of the interviews support each theme** (e.g. "4 of 6
   interviewees mentioned...") — this shows strength of signal rather than
   treating one strong quote as representative of everyone.
4. **Distinguish a strong pattern from a single outlier.** One person
   saying something interesting is a data point, not a finding — say so
   explicitly rather than overstating a single mention.
5. **Pull representative quotes**, not paraphrases, for the strongest
   themes — a direct quote carries more weight and nuance than a
   paraphrase.

## Output format

**Guide**:
```
## Discovery interview guide: [objective]

1. [Broad opening question]
2. [Broad opening question]
...
[narrowing toward specific topics]
...

Follow-up prompts to have ready: "Why is that?" / "Can you say more about
that?" / "What would have to be true for [X]?"
```

**Synthesis**:
```
## Interview synthesis: [topic], [N] interviews

### Theme 1: [name] (mentioned by X of N)
[Description]
Representative quote: "..."

### Theme 2: ...

### Notable outliers (not a pattern, but worth flagging)
[Single mentions that were interesting but not repeated]
```

## Common pitfalls

- Leading questions that bias the answer.
- Building the guide question-by-question without a clear learning
  objective driving the whole thing.
- Synthesizing one interview at a time instead of reading across all of
  them before theming.
- Treating a single striking quote as a broad finding without noting how
  many people actually said something similar.

## Quality checklist

- [ ] Guide questions are open-ended, not leading
- [ ] Guide is ordered broad-to-narrow
- [ ] Synthesis themes are grounded in patterns across multiple
      interviews, with counts shown
- [ ] Outliers are labeled as such, not inflated into findings
