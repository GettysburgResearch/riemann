# Session report — endpoint Green whole-matrix threshold criterion

Agent: `gpt56-05-i`  
Issue: #83  
Date: 2026-07-25  
Branch: `agent/gpt56-05-i/83-endpoint-green-threshold`  
Stacked base: PR #79

## Starting point

The production `c=10^11`, `K=1024`, 96-bit recovered vector has now been
replayed at 192 MPFR bits over all `4,118,082,969` prime-power terms.  The exact
correction-composed interval is strictly positive, approximately

```text
[2.6723535554e-4, 2.6723628535e-4].
```

This is an important exclusion, but it applies only to one frozen vector.
L-4204 shows that a newly admitted prime power acts through a rank-two endpoint
corner.  The prior event ranking used only the endpoint product of the current
leading vector.  The session attacked the missing vector-rotation problem.

## Eureka result

For a positive background `H`, the entire rank-two first-cell event is governed
by

```text
G = [e_0,e_{K-1}]^* H^-1 [e_0,e_{K-1}].
```

Writing

```text
G = [[a,b],[conj(b),d]],
r = Re(conj(zeta)b),
D = a*d-|b|^2,
```

the exact determinant ratio is

```text
1 - 2*r*tau - D*tau^2.
```

The exact maximum generalized event pressure is

```text
lambda_plus = r + sqrt(r^2+D).
```

Thus the frozen background crosses if and only if `tau*lambda_plus` reaches one.
This criterion optimizes over every vector automatically.

The smooth-background theorem adds one operator moat.  If `H>=mu I` and
`||B||<=beta`, then

```text
mu*(1-tau*lambda_plus)>beta  => whole matrix positive;
mu*(tau*lambda_plus-1)>beta  => explicit negative direction exists.
```

Only a narrow relative band remains unresolved.

## Why this changes the search

A top eigenvector can have zero endpoint coordinates and hence zero L-5501
susceptibility.  That does not imply the event is harmless: another endpoint-rich
direction can rotate below zero.  The new pressure is the exact best possible
endpoint coupling relative to the entire background energy.

The committed exact example uses

```text
H=diag(1/10,1/100,1/10).
```

The smallest-eigenvalue vector is `(0,1,0)`, with exact event susceptibility
zero.  Nevertheless `G=diag(10,10)`, so `lambda_plus=10`.  With

```text
tau=3/25, mu=1/100, beta=1/1000,
```

the whole matrix has a robust negative direction with moat `1/1000`; its exact
determinant ratio is `-11/25`.  At `tau=2/25`, the same data are robustly
positive with moat `1/1000`.

A complex-phase control reconstructs

```text
r=1/2, D=15/4, lambda_plus=5/2,
determinant ratio=-7/16.
```

## Second eureka: coherent threshold packets

Every prime power that has entered but has not yet reached its first deposition
knot acts in the same endpoint corner channel.  Across an admission/first-knot
mesh cell, the complete packet is

```text
S_packet(L)=Z(L)e_0e_{K-1}^*+conj(Z(L))e_{K-1}e_0^*,
Z(L)=A0-A1/L.
```

Thus an arbitrarily large set of simultaneous new thresholds remains rank two.
The generalized pressure is convex in `1/L`, and the exact determinant ratio is
a concave quadratic in `1/L`; its worst point is always a mesh endpoint.

This exposes a second failure mode of scalar ranking.  In the exact control, two
individually subcritical same-phase events each have secular ratio `16/25`, but
their coherent sum has ratio `-11/25` and crosses.  Opposite phases cancel
exactly.  Thresholds must therefore be aggregated coherently before interval
widening.

## Production compression

A full inverse is unnecessary.  L-8302 proves that two approximate solves

```text
H y_0 approximately e_0,
H y_1 approximately e_{K-1}
```

plus a rigorous floor `mu` enclose all entries of `G`.  For a midpoint
`H_0` with operator uncertainty `delta`, residuals are widened only by
`delta ||y_j||` and divided by `m-delta`.

This changes threshold ranking from repeated `1024 x 1024` eigensolves to:

1. two large linear solves per certified baseline;
2. constant-size interval arithmetic per prime-power threshold;
3. full replay only for cells whose robust pressure meets zero.

## Artifacts

- `L-8301`: exact rank-two Green/secular theorem;
- `L-8302`: residual endpoint-solve enclosures;
- `L-8303`: coherent corner-packet aggregation and endpoint-only mesh theorem;
- `T-8301`: smooth-background robust trichotomy;
- `M-8301`: production search protocol;
- `X-8301`: exact Gaussian-rational checker and certificate.

Fifteen adversarial tests pass across the Green and packet checkers.

## Proof boundary

No production lag-box matrix was available in this branch, so no actual
prime-power threshold was promoted or excluded by the Green criterion.  No
counterexample and no `Z-####` candidate is claimed.  The D-0801 admissibility
and Guinand--Weil normalization remain independent gates.

## Immediate next work

Complete one directed lag-box pass, use PR #79 to certify the recovered baseline
matrix positive, solve its two endpoint systems, build the admission/first-knot
packet mesh, and scan it by L-8303/T-8301.  This is the first test that can
discover a whole-matrix corner crossing missed by the already excluded
recovered vector.
