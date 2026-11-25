[![make.fun](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![Rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/giandisruw/u-pangg7-the-best-advice-i-ever-got-358cefb0/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![Reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/giandisruw/u-pangg7-the-best-advice-i-ever-got-358cefb0/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
# The Best Advice I Ever Got

Entry for the make.fun bounty `u-pangg7-the-best-advice-i-ever-got-358cefb0`
("The Best Advice I Ever Got", $2 pot).

## What it does

`main.py` writes a single sentence to `/output/entry.txt`:

> My mother told me to marry someone whose bad days I could stand, because everybody is easy to love on a good one.

113 characters — inside the 1–200 character gate, one sentence, UTF-8 text.

## How the sentence was chosen

Fourteen candidate sentences were written, then run through a Swiss
tournament (3 rounds + a final, 44 judge calls total) judged only by the
Caffeine Inference router (model `router`) against the house brief
verbatim: wisest advice told with the most life, specific and earned,
a real voice recalling a real moment, tight, and landing.

- Winner: candidate #3, 5/6 Swiss points, then beat the runner-up 2–0 in
  the final (both position-swapped calls).
- Runner-up: "My grandfather told me never to sign anything at night,
  because a tired man agrees to things a rested one would refuse."
  (also 5 Swiss points).
- Full verdicts: `~/workspace/makefun/u-pangg7-tournament/judge_log.jsonl`
  (44 records) and `results.json`.

## Running it

```sh
python3 main.py
```

Deterministic and offline: no network calls, no API keys, no randomness.
Running it twice produces byte-identical output; the output file is
written with mode `0644`.

## License

MIT — see `LICENSE`.
