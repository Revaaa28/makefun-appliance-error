# Candidates — The Funniest Honest Appliance Error

Competition: u-xvader-the-funniest-honest-appliance-error-adec4450 ($2, winner-takes-all).
Judge brief, in order: (1) honest error message an appliance could show, ≤200 chars;
(2) the laugh — a real joke, surprise or twist, not a cute phrasing that only smiles;
(3) the honesty — names a fault the appliance could plausibly report, humour from the truth;
(4) the machine's voice — flat, put-upon, the appliance itself speaking;
(5) the economy — every word earns its place, no padding, no explaining the joke.

Ranking is MANUAL against the brief in order, plus pairwise checks against the
strongest rival shapes. No Gemini judge, no NVIDIA judge, no judge API/proxy
tournament (standing rule, Rev 2026-11-24).

## Candidates

1. **Vacuum cleaner — dustbin full.** "Error: dustbin full. I have swallowed a sock, three coins and your earring. I am keeping the earring." (101 chars)
   Rationale: a flat inventory that turns into a confession of theft; the machine
   keeps the one valuable thing. Fault is real (bin-full sensors exist, vacuums
   do swallow small objects).

2. **Washing machine — missing sock.** "Error: one sock missing. I did not take it. Check the dryer. We do not speak anymore." (85 chars)
   Rationale: denial plus an inter-appliance feud; the missing sock is the classic
   washer complaint. Weak spot: a washer cannot actually count socks, so the
   fault is less literally reportable than the others.

3. **Dishwasher — filter blocked.** "Error: filter blocked. I found rice, a toothpick and what I can only describe as regret." (88 chars)
   Rationale: a deadpan inventory where the last item is not an object at all;
   the machine judges the household. Fault is real (blocked filters are a standard
   dishwasher error).

4. **Fridge — door ajar.** "Error: door ajar for 12 minutes. I have been cooling your kitchen. The kitchen does not appreciate it." (102 chars)
   Rationale: the fridge reports doing its job on the wrong room; flat, put-upon,
   and the fault (door ajar, timed) is exactly what fridges report.

5. **Kettle — boiled dry.** "Error: boiled dry. I had no water and kept going anyway. That is the job. That was the job." (91 chars)
   Rationale: the machine worked itself to death out of duty; the tense shift
   ("is" → "was") is the twist. Fault is real (boil-dry cut-outs exist).

6. **Microwave — turntable jammed.** "Error: turntable jammed. Your plate has not moved in 3 minutes. Neither have I. We are both stuck here." (103 chars)
   Rationale: shared stuckness; the machine and the plate in the same predicament.
   Fault is real (jammed turntables are reported).

7. **Toaster — bread ejected early.** "Error: bread ejected before browning. It asked to leave early. I respected its wishes." (86 chars)
   Rationale: the toast quits; the machine grants it an exit. Fault is plausible
   (early ejection / pop-up fault) but "asked to leave" leans cute rather than a
   sharp twist.

8. **Coffee machine — descale overdue.** "Error: descale required. I have been brewing through limescale for a year. The coffee tastes of effort now." (107 chars)
   Rationale: "tastes of effort" is deadpan understatement; the fault (descale
   overdue) is a standard coffee-machine error.

9. **Fridge — water filter expired.** "Error: water filter expired 214 days ago. I have been filtering nothing. The water is just water now." (101 chars)
   Rationale: the machine admits months of pretending; "just water now" lands
   flat. Fault is real (filter-life counters exist).

10. **Oven — self-clean refused.** "Error: self-cleaning cancelled. I refuse to burn off your mistakes at 500 degrees again." (88 chars)
    Rationale: the oven goes on strike against the owner's mess; "your mistakes"
    is the barb. Fault is plausible (self-clean abort) but the refusal is more
    attitude than a reportable fault.

11. **Washing machine — unbalanced load.** "Error: unbalanced load. Your duvet has balled up and is beating me from the inside. Please open the door and negotiate." (119 chars)
    Rationale: the duvet as an attacker inside the drum; "negotiate" asks the
    owner to parley with laundry. Fault is real (unbalanced-load errors are
    standard). "Negotiate" is the weakest word — slightly cute.

12. **Dryer — lint filter blocked.** "Error: lint filter blocked. I am choking on your clothes. Clean me or I stop breathing." (87 chars)
    Rationale: the dryer reports suffocation in the owner's laundry; "stop
    breathing" is a sharp threat. Fault is real. The second half explains the
    first a little too much, costing economy.

## Manual ranking (brief criteria in order)

| Rank | # | Line (short) | Why here |
|------|---|--------------|----------|
| 1 | 1 | Vacuum keeps the earring | Best twist (confession of theft after a flat inventory), fault fully real, voice flat throughout, 101 chars with no wasted word. |
| 2 | 3 | Dishwasher finds "regret" | Single-word twist is very sharp and the fault is textbook; loses to #1 only on criterion 2 — "regret" is one beat where #1 has two (inventory → theft). |
| 3 | 4 | Fridge cools the kitchen | Fault is the most literally reportable of all; the twist (cooling the wrong room) is strong but the third sentence softens the landing slightly. |
| 4 | 9 | Filter expired, "just water" | Honest admission over 214 days, flat voice, good economy; the laugh is quieter than #1–#3 — a smile more than a twist. |
| 5 | 5 | Kettle boiled dry | Real fault, good tense-shift twist; "That is the job. That was the job." is slightly self-pitying and explains itself a touch. |
| 6 | 6 | Microwave, both stuck | Good shared-predicament joke, real fault; the last sentence restates the second, costing economy. |
| 7 | 2 | Washer, missing sock | Strong joke (feud with the dryer) but criterion 3 is its weak leg: a washer cannot count socks, so the fault is the least literally reportable. |
| 8 | 8 | Coffee tastes of effort | Nice deadpan line, real fault; the laugh is a wry smile, not a surprise or twist. |
| 9 | 11 | Duvet beating me | Real fault and a vivid image, but "negotiate" tips into cute and the line is the longest. |
| 10 | 12 | Dryer choking | Real fault, sharp threat, but the second sentence explains the first — fails criterion 5. |
| 11 | 10 | Oven refuses self-clean | Attitude over report; the fault is thin (a refusal, not a reported failure). |
| 12 | 7 | Toaster, toast asked to leave | Cute phrasing that only smiles; no real twist, and the fault is the softest. |

## Pairwise checks (winner vs strongest rival shapes)

- **#1 vacuum vs #3 dishwasher:** both are flat inventories with a twist at the end.
  #3's twist is one word ("regret"); #1's twist is an action (keeping the
  earring) that reframes the whole inventory as a crime report. #1 wins on
  criterion 2 — a bigger surprise, and the joke keeps working after the first read.
- **#1 vacuum vs #4 fridge:** #4's fault is more literally reportable (door-ajar
  timers are standard), so #4 edges #1 on criterion 3 by a hair. But criterion 2
  decides first where they differ most: #1's theft confession is a real joke with
  a twist; #4's "the kitchen does not appreciate it" is a wry observation. #1 wins.
- **#1 vacuum vs #2 washer:** #2's feud ("We do not speak anymore") is the
  funniest single beat in the set, but #2 fails criterion 3 — no washer can report
  a missing sock. #1's fault is real and its twist is nearly as strong. #1 wins.
- **#1 vacuum vs #9 fridge filter:** #9 is the flattest voice in the set, but its
  laugh is a quiet admission, not a surprise. #1 wins on criterion 2 by a clear margin.

## Winner

**#1 — Vacuum cleaner, dustbin full:**

> Error: dustbin full. I have swallowed a sock, three coins and your earring. I am keeping the earring.

101 characters, 101 bytes. One line, UTF-8, no trailing newline in the entry file
(the program writes the line without a trailing newline; the gate counts characters,
and a bare line is the cleanest form).
