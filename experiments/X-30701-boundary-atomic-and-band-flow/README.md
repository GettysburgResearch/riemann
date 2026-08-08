# X-30701 — Boundary atomic lower bound and outer-band flow

Run:

```bash
python experiments/X-30701-boundary-atomic-and-band-flow/verify.py
```

Expected result:

```text
PASS_EXACT_BOUNDARY_ATOMIC_LINEAR_MOAT_AND_TOP_BAND_STEP_FLOW
band rows 210089
top-band checks 7085
mutation tests 5/5
proof-object SHA-256
6443211853336997ebdea4ca94675d9d7ea1ea207ee6a66c5115f08ec188dc5b
```

`verify.py` SHA-256:

```text
7cffdb14a4aed14278516a94f1ea4631c22f22c4fc4e6d912d6146d680bd498b
```

The checker uses only integers and `fractions.Fraction`.

It verifies:

- the rational moat `c_0>1/1820`;
- the triangular no-second-multiple band;
- the `X/80` band count for `160<=X<=4096`;
- the exact nonnegative central-step realization of a decreasing outer profile;
- five fail-closed mutations.

It does not evaluate the infinite square-root series, prove all-generation
cycle optimization, prove Cycle Debt, or prove RH. The analytic monotonicity and
series arguments are in `R-30701/L-30701`.
