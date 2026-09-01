# Worked example: booking-to-departure process

### Current process
1. Inquiry received (email/platform) — who: booking staff — time:
   immediate — triggers: manual reply drafted
2. Availability checked manually against a shared calendar — who: booking
   staff — time: up to a few hours if staff is busy — triggers: quote
   sent
3. Quote sent, customer confirms — who: booking staff / customer — time:
   varies (customer-side) — triggers: deposit requested
4. Deposit received, booking manually re-entered into a second system
   (accounting) — who: booking staff — time: often delayed to end of day
   — triggers: confirmation sent
5. Trip details re-confirmed with crew closer to departure date — who:
   ops lead — time: day before — triggers: trip proceeds

### Issues found
- Step 4 is a **redundant re-entry**: the same booking is entered twice
  (booking system, then accounting) — a manual duplication that's also a
  source of data-entry errors.
- Step 4's "often delayed to end of day" is a **waiting/delay point**
  with no clear reason it needs to wait — it delays when accounting
  records actually reflect real bookings.
- Step 2's manual calendar check is a **manual step that could be
  simpler** if availability were checked directly in the booking system
  rather than cross-referenced against a separate shared calendar.

### Simplified process
1. Inquiry received — same as before
2. Availability checked directly in the booking system (no separate
   calendar cross-reference) — who: booking staff — time: immediate
3. Quote sent, customer confirms — same as before
4. Deposit received, booking auto-reflected in accounting (single entry
   point, not re-entered) — who: booking staff — time: immediate
5. Trip details re-confirmed with crew closer to departure — same as
   before (this step stays: it's a genuine safety/readiness check, not
   redundant)

### What changed and why
Removed the separate shared calendar (step 2) — safe to remove once
availability lives in the booking system as the single source of truth.
Removed the manual re-entry into accounting (step 4) — safe to remove if
the booking system and accounting can share data directly; if they can't
today, this becomes the implementation dependency to solve first, not an
immediate change.
Kept the crew reconfirmation step — this isn't redundant, it's a genuine
last check before departure and removing it would introduce real safety
risk.

### To implement this
Requires confirming whether the booking system and accounting tool can
share data directly (a real technical dependency to check first) — if
not, the calendar-consolidation change alone (removing step 2's separate
calendar) can still be done immediately as a smaller, standalone win.
