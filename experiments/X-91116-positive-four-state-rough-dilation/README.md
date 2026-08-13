# X-91116 — Positive four-state rough dilation

Companion exact replay for `L-91327`.

```bash
python3 experiments/X-91116-positive-four-state-rough-dilation/verify.py
```

Expected verdict:

```text
PASS_POSITIVE_FOUR_STATE_ROUGH_DILATION
```

The checker uses exact `Fraction` arithmetic for the intertwining identity,
three-factor composition, linear total-variation telescope, and SHARP/score
observations.
