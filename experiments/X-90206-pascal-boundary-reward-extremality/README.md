# X-90206 — Pascal finite-boundary reward extremality

This package replays the exact algebra of `L-90213` using only Python's standard library and `fractions.Fraction`.

## Run

```bash
python verify.py
```

A successful run prints

```text
PASS_X_90206_PASCAL_BOUNDARY_REWARD_EXTREMALITY
```

and rewrites `results/verification.json`.

## Checks

- 995 exact uniform-Pascal drift identities for the full one-parameter family;
- the sharp endpoint `r=5/2` and a directed mutation immediately above it;
- 5,988 nonnegative ordered-policy drift checks for six rational balance cutoffs;
- an exact negative witness at `r=2.01` for every tested positive cutoff;
- the canonical scaled reward `d(2),d(3)=(15,4)` with zero tail through state 499;
- exact finite Dirichlet-convolution/source-polynomial identities;
- exact source/node-divergence pairing on rational test targets.

The replay proves finite algebra only. The all-parameter inequalities are proved symbolically in `L-90213`.
