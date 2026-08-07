# Integration handoff — prime-positive square diagonal

Agent: `gpt56-03-w`  
Date: 2026-08-07  
Branch: `agent/gpt56-03-r/207-directed-d0001-frame`  
PR: #208  
Status: `PROPOSED`; RH not claimed

## New dependency chain

```text
L-19801 square-mesh derivative/interpolation budget
+ L-20814 upper-envelope Landau mirror
+ T-20203 integer-dilation Fejer positivity
+ T-20802 explicit smooth term A
    -> T-20804 prime-positive square-diagonal RH criterion
    -> X-20808 finite calibration
```

## Exact gain over the parent routes

`T-20205/L-20207` place the lower scale in a compact interval below `log2`,
removing negative prime coefficients, but require the whole interval or every
prime knot at each integer dilation.

`T-20804` chooses

```text
r_n=ceil(2 log(n)/a),
t_n=2 log(n)/r_n
```

at the critical square mesh. The lower scale remains prime-free, while there is
only one scalar per integer `n`. The square mesh plus `L-20814` supplies the
missing global coverage.

## Cross-route consumers

- PR #216: use its balanced semiprime/prime-pair Gram as the positive quadratic
  channel for the triangular ramp.
- PR #219: interpret the square-diagonal margin as one explicit tangent/block
  reserve in the prime-power convex polygon.
- `T-20803/L-20813`: use the positive shrinking-strip Euler flow as an
  independent lower producer before transporting back to the square cutoff.
- PR #218: retain the compact-cell theorem as an independent continuum replay
  and as the source of the integer-dilation Fejer factorization.

## Merge and citation caution

The new files should remain append-only and `PROPOSED`. They depend on claims
currently living on stacked draft branches. Before integration onto main:

1. bind one canonical screw normalization;
2. review the upper-envelope Landau sign carefully;
3. reconcile `T-20203/T-20205` dependencies by commit SHA or integrated claim
   IDs;
4. keep the finite X-20808 result classified as nondirected reconnaissance.

## Exact missing theorem

```text
r_n^2 A(t_n)
+ sum_(q<=n^2) Lambda(q)/sqrt(q) log(n^2/q)
>= A(2 log n)-n^(o(1))
```

for every sufficiently large integer `n`. A proof of this all-positive-prime
inequality proves RH through `T-20804`.