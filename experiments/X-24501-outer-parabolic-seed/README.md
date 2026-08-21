# X-24501 — Exact outer parabolic-seed margin

Status: `EXACT_RATIONAL`  
Consumes: `L-24505`, `L-24507`  
Issue: #245

This verifier certifies the finite continuum margin used in the outer-feasibility theorem.

For every reciprocal cell `2<=N<=27`, it encloses

\[
M_N=
2(H_N+1)
\exp\left(\frac{A_N+2H_N-2}{2(H_N+1)}\right)-4N
\]

and proves

\[
M_N<-1/50.
\]

The checker uses only Python integers and `fractions.Fraction`:

- square roots are enclosed by exact dyadic integer-square-root intervals;
- logarithms use the positive atanh series with an exact geometric tail;
- exponentials use a positive Taylor series with an exact ratio tail;
- interval arithmetic is outward by construction.

It also verifies the exact integer inequalities

```text
28^3 < 149^2
28*149*50 < 2*104301
```

which feed the uniform finite-difference remainder in `L-24507`.

## Replay

```bash
python verify.py
```

Expected verdict:

```text
PASS_EXACT_OUTER_PARABOLIC_SEED_MARGIN
```

Expected proof-object SHA-256:

```text
c849273361e1c868fe24d814a078c74181bb11d5ffa1160154a29dd6e1e95521
```

## Mutations

The checker requires both adversarial controls to fail:

1. extending the `1/50` margin through cell `N=28`;
2. strengthening the margin to `1/40` through cell `N=27`.

## Boundary

The decimal endpoints in the output are display-only. Every acceptance decision is made with exact rational intervals. This experiment certifies the finite continuum margin; the analytic averaging argument remains in `L-24507`.
