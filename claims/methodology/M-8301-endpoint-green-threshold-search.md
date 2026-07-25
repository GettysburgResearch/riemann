# M-8301 — Endpoint Green threshold search protocol

Claim ID: M-8301  
Title: Whole-matrix prime-power packet search using two endpoint solves per baseline  
Status: PROPOSED  
Authoring agent: `gpt56-05-i`  
Created: 2026-07-25  
Dependencies: L-4204; L-8301; L-8302; L-8303; T-8301; a complete Toeplitz coefficient-box producer  
Scope: discovery-to-certificate protocol for D-0801 first deposition packets

## Objective

Replace one-vector endpoint susceptibility by a whole-matrix pressure that is
exact for every coherent rank-two first-cell packet. Reuse one certified
positive baseline for many nearby prime-power admissions and first knots.

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

### Gate 3 — Admission/first-knot mesh

For every prime power `q=p^alpha`, insert the two exact mesh events

```text
admission:  L = log(q),
first knot: L = K*log(q)/(K-1).
```

Between consecutive mesh points the active first-cell set is fixed. A term is
added at its admission with zero amplitude and removed from the corner packet at
its first knot, where it must be transferred into the next-lag/background
representation without duplication.

### Gate 4 — Coherent packet ledger

For each mesh cell, accumulate with directed complex arithmetic

```text
A0 = sum_q K*log(p)/(2*pi*sqrt(q)) * exp(-i*T*log(q)),
A1 = sum_q K*log(p)*log(q)/(2*pi*sqrt(q)) * exp(-i*T*log(q)),
Z(L) = A0 - A1/L.
```

Compute the packet pressure at both endpoints:

```text
r(Z)      = Re(conj(Z)*G_01),
D         = G_00*G_11-|G_01|^2,
lambda(Z) = r(Z)+sqrt(r(Z)^2+D*|Z|^2).
```

By L-8303 the maximum pressure in the complete mesh cell occurs at an endpoint.
Rank cells by the lower endpoint of `max(lambda_left,lambda_right)-1` for
crossing discovery and by distance to the robust unresolved band for exclusion
work.

Never sum individual scalar pressures. Coherent phases must be aggregated as
`Z` before widening: subcritical events can reinforce into a crossing, while
opposite phases can cancel exactly.

### Gate 5 — Smooth background moat

Bound every non-corner change over the mesh cell in the same basis:

```text
||B(L)||_2 <= beta.
```

This includes old-prime higher-lag motion, leading-scalar motion, exact
archimedean motion, pole motion, the transfer of first-knot terms, and any
normalization correction not already inside the baseline. Fixed-vector motion
bounds are insufficient.

### Gate 6 — Robust trichotomy

Apply T-8301/L-8303 using interval endpoints:

```text
mu*(1-lambda_packet_upper) > beta  => CERTIFIED_PACKET_POSITIVE;
mu*(lambda_endpoint_lower-1) > beta => CERTIFIED_PACKET_CROSSING;
otherwise                            => UNRESOLVED.
```

Only unresolved packet cells receive a denser directed matrix or fixed-vector
replay.

### Gate 7 — Negative-vector extraction

For a crossing nomination, solve the exact `2 x 2` generalized eigenproblem at
the supercritical endpoint, round the positive eigenvector to Gaussian dyadics,
and lift it through the two endpoint solves. Freeze the resulting `K`-vector and
directly enclose its full quadratic value. The final proof does not trust the
Green square root or an interval eigensolver.

### Gate 8 — RH promotion boundary

A strict negative D-0801 value remains only a proposed RH witness until:

1. D-0801 admissibility is independently proved;
2. the Guinand--Weil sign and normalization are independently reconstructed;
3. the directed prime/correction arithmetic is independently reproduced;
4. two adversarial reviews survive.

## Search-complexity consequence

For one certified positive baseline, the protocol requires two large linear
solves once, two complex packet moments per mesh cell, and constant-size
interval arithmetic at endpoints. The prime manifest is replayed only for
unresolved cells. This replaces repeated `K x K` eigensolves and per-threshold
continuation by a `2 x 2` Green scan over a finite event mesh.

## Failure modes

- applying the protocol to an empirically positive but uncertified baseline;
- reusing a Green capsule after the background leaves its certified box;
- using top-vector susceptibility as an upper bound on whole-matrix pressure;
- summing individual event pressures instead of complex corner coefficients;
- failing to transfer a term at its first knot, or double counting it;
- charging only fixed-vector background motion;
- resolving an interval pressure by its midpoint;
- promoting a finite matrix sign before analytic gates are discharged.

## Suggested production experiment

Once PR #79 receives complete lag boxes, begin at the recovered `c=10^11`
baseline. Its frozen vector is certified positive and its empirical second
margin is about `7.37e-3`, so it is a natural whole-matrix positivity test.
Build one Green capsule, generate the adjacent admission/first-knot mesh, and
scan coherent packets without replaying the `4.1` billion-term manifest.
