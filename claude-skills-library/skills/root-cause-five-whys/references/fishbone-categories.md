# Fishbone categories for multi-cause problems

When a symptom likely has more than one contributing cause, check across
these categories before committing to a single 5-Whys chain. Adapt
category names to the actual business context.

- **People** — skills, staffing levels, training, turnover, workload
- **Process** — how work is actually done, handoffs, response-time
  standards, approval steps
- **Tools/Systems** — booking system, communication tools, scheduling
  software, their reliability and ease of use
- **External** — seasonality, weather, competitor actions, currency,
  regulation, market-wide demand shifts

## Worked example: "Response time to booking inquiries got slower"

Quick fishbone pass across categories:
- People: a team member who handled inquiries left last month (likely
  contributor — fact, checkable via staffing records)
- Process: no formal backup/coverage plan for inquiry handling when
  someone is out (likely contributor)
- Tools: booking inquiry inbox is shared with general email, easy for
  messages to get buried (possible contributor — check inbox structure)
- External: inquiry volume itself increased due to seasonal demand
  (possible contributor — check volume data before assuming)

Two categories (People, Process) look like the strongest candidates based
on what's known; Tools and External are worth a quick data check before
ruling in or out. From here, run 5-Whys on the strongest candidate:

1. Why did response time get slower? → Fewer people available to answer
   inquiries (fact: one team member left).
2. Why weren't inquiries redistributed? → No documented backup process for
   who covers inquiries when someone is out (fact: confirmed no such
   document exists).
3. Why was there no backup process? → Inquiry handling was informally
   owned by one person, never formally cross-trained (root cause:
   process/staffing structure, not a one-off event).

Root cause: inquiry handling lacked a documented, cross-trained backup —
not simply "we lost a team member," which is the surface-level symptom
explanation. Fix aimed at root cause: document the inquiry process and
cross-train a second person. Symptom-level mitigation in the meantime:
temporarily reassign inquiry handling to another available team member.
