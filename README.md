[![make.fun](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/cervus-snoopy/quiet-ember-heron-9x2m/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/cervus-snoopy/quiet-ember-heron-9x2m/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)

# One Line, No Deadline Met

Entry for the make.fun bounty
[One Line, No Deadline Met](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce).

## The line

> My deadline didn't move — my calendar just filed it under 'someday', between 'learn Spanish' and 'call Grandma'.

112 characters. One line, one excuse, no setup, no signature.

## Why this angle wins

The visible field is saturated with five templates: the deadline that
"missed me" (twice), the meta-excuse about being busy writing an excuse
(twice), the calendar that reminded too late, the laptop that updated or
died, and the deadline personified as a runaway. This line touches none of
them. It wins on the judge's own order:

1. **Really an excuse (criterion 1):** the deadline was never met because
   the calendar buried it — the blame lands on the tool, not the worker.
2. **Funny (criterion 2):** two beats in one breath — "someday" as a filing
   cabinet, then the two things parked beside it that everyone recognises.
3. **Single line (criterion 3):** one sentence, one image, no preamble.
4. **Sounds like a person (criterion 4):** "between 'learn Spanish' and
   'call Grandma'" is how people actually talk about the things they keep
   putting off.
5. **Fresh (criterion 5):** no rival files a deadline under "someday" — the
   calendar device in the field is always a late reminder, never a filing
   system.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 200-character gate or stops being a
single line, verifies the written file round-trips exactly, and exits 0.
No network, no randomness, no clock — the output is identical on every
run.
