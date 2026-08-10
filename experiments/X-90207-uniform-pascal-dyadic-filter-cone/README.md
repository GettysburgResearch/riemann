# X-90207 — Uniform-Pascal dyadic filter cone

This package replays `L-90216` with exact rational arithmetic and a minimal exact implementation of `Q(sqrt(2))`.

## Run

```bash
python verify.py
```

A successful run prints

```text
PASS_X_90207_UNIFORM_PASCAL_DYADIC_FILTER_CONE
```

and rewrites `results/verification.json`.

## Checks

- direct Markov drifts against the block-cone inequalities;
- the Haar and canonical filters;
- a genuine feasible degree-three filter;
- a mutation immediately beyond the canonical first-coefficient bound;
- the improved factor-64 polynomial in exact `Q(sqrt(2))` arithmetic;
- its exact negative witness
  `d(15)=(1-sqrt(2))/42`.

The script uses only the Python standard library.
