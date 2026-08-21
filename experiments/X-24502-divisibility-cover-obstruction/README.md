# X-24502 — Exact positive seed-excess band

Status: `EXACT_RATIONAL`  
Consumes: `L-24505`, `R-24501`  
Issue: #245

This verifier certifies the positive continuum band used to refute the monotone Divisibility Cover.

For each reciprocal endpoint

\[
\theta=1/N,
\qquad 32\le N\le40,
\]

it encloses the continuum seed excess and proves

\[
E(1/N)>1/10.
\]

Because every reciprocal-cell critical point is a maximum, endpoint positivity implies

\[
E(\theta)>1/10
\qquad(1/40\le\theta\le1/32).
\]

The script reuses the exact rational interval primitives of `X-24501` and adds no floating-point acceptance gate.

## Replay

```bash
python verify.py
```

Expected verdict:

```text
PASS_EXACT_POSITIVE_SEED_EXCESS_BAND
```

Expected proof-object SHA-256:

```text
428307dd3e0be7647aa660094433e2071c5e67454d534d5b0c9219defabd4cda
```

## Mutations

The verifier rejects:

1. extending the `1/10` endpoint margin down through cell `N=30`;
2. strengthening the certified margin to `1/5` at cell `N=32`.

## Boundary

This is a finite continuum sign certificate. The uniform finite-difference passage and the prime-counting contradiction are proved in `R-24501`.
