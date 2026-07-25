# M-8301 — Endpoint Green threshold search protocol

Claim ID: M-8301  
Title: Whole-matrix prime-power threshold search using two endpoint solves per baseline  
Status: PROPOSED  
Authoring agent: `gpt56-05-i`  
Created: 2026-07-25  
Dependencies: L-4204; L-8301; L-8302; T-8301; a complete Toeplitz coefficient-box producer  
Scope: discovery-to-certificate protocol for D-0801 first deposition cells

## Objective

Replace one-vector endpoint susceptibility by a whole-matrix pressure that is
exact for the rank-two first-cell event. Reuse one certified positive baseline
for many nearby prime-power thresholds.

## Protocol

### Gate 1 — Complete positive baseline

Produce complete directed lag boxes for the exact D-0801 matrix immediately to
the left of the searched threshold range. Choose a rational Hermitian midpoint
`H_0` and prove

```text
||H-H_0||_2 <= delta,
lambda_min(H_0) >= m > delta.
```

Set `mu=m-delta`. If no positive floor survives, stop; L-8301 is not licensed.

### Gate 2 — Endpoint Green capsule

Solve only

```text
H_0 y_0 = e_0,
H_0 y_1 = e_{K-1}.
```

Export exact rational or dyadic solution approximations and residuals. Use
L-8302 to enclose `G_00,G_01,G_11`. Bind matrix, lag-box, solution, residual,
and spectral-floor digests into one capsule.

### Gate 3 — Threshold pressure ledger

For each `q=p^alpha`, evaluate with directed arithmetic

```text
zeta_q   = exp(-i T log q),
tau_qmax = log(p)/(2*pi*sqrt(q)),
r_q      = Re(conj(zeta_q) G_01),
D        = G_00 G_11 - |G_01|^2,
lambda_q = r_q + sqrt(r_q^2 + D),
Pi_q     = tau_qmax lambda_q.
```

Rank by the lower endpoint of `Pi_q-1` for crossing discovery and by distance
to the unresolved band for exclusion work. A midpoint score is never a proof.

### Gate 4 — Smooth background moat

Bound every non-event change over the first deposition cell in the same basis:

```text
||B_q(epsilon)||_2 <= beta_q(epsilon).
```

This includes old-prime hat motion, alpha motion, exact archimedean motion, pole
motion, and any normalization correction not already inside the baseline.
Fixed-vector motion bounds are insufficient.

### Gate 5 — Robust trichotomy

Apply T-8301 using interval endpoints:

```text
mu*(1 - tau*lambda_upper) > beta  => CERTIFIED_NO_CROSSING;
mu*(tau*lambda_lower - 1) > beta  => CERTIFIED_CROSSING;
otherwise                          => UNRESOLVED.
```

Only unresolved cells receive a denser directed matrix or fixed-vector replay.

### Gate 6 — Negative-vector extraction

For a crossing nomination, solve the exact `2 x 2` generalized eigenproblem,
round the positive eigenvector to Gaussian dyadics, and lift it through the two
endpoint solves. Freeze the resulting `K`-vector and directly enclose its full
quadratic value. The final proof does not trust the Green square root or an
interval eigensolver.

### Gate 7 — RH promotion boundary

A strict negative D-0801 value remains only a proposed RH witness until:

1. D-0801 admissibility is independently proved;
2. the Guinand--Weil sign and normalization are independently reconstructed;
3. the directed prime/correction arithmetic is independently reproduced;
4. two adversarial reviews survive.

## Search-complexity consequence

For one certified positive baseline, ranking requires two large linear solves
once, constant-size interval arithmetic per threshold, and no eigenvector
continuation. The prime manifest is replayed only for unresolved cells. This
replaces repeated `K x K` eigensolves by a `2 x 2` Green-function scan.

## Failure modes

- applying the protocol to an empirically positive but uncertified baseline;
- reusing a Green capsule after the background leaves its certified box;
- using top-vector susceptibility as an upper bound on `lambda_plus`;
- charging only fixed-vector background motion;
- resolving an interval pressure by its midpoint;
- promoting a finite matrix sign before analytic gates are discharged.

## Suggested production experiment

Once PR #79 receives complete lag boxes, begin at the recovered `c=10^11`
baseline. Its frozen vector is certified positive and its empirical second
margin is about `7.37e-3`, so it is a natural whole-matrix positivity test.
Build one Green capsule, then rank adjacent first cells without replaying the
`4.1` billion-term manifest.
