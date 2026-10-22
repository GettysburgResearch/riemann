# X-90016 — Optimized radix-five annular regression

Companion checker for `L-90016` and `T-90012`.

```bash
python experiments/X-90016-radix5-annular/verify.py --max-x 5000000
```

Expected line:

```text
PASS_RADIX5_FACTOR125_ANNULAR_REGRESSION
```

It imports the exact radical-switching endpoint implementation from `X-90015`, verifies the radix-five RH-side margin, and checks every aligned endpoint `X=125N` through the retained maximum. The first aligned endpoint `X=125` is the sole retained nonnegative exception; every tested aligned endpoint from `X=250` through five million is negative. The scan is reconnaissance only and is not a cofinal sign proof.
