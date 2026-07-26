# L-9306 — Off-center reuse of unconditional total-zero counts

Claim ID: L-9306  
Title: A certified total-count window can be reused at a shifted direct-xi ordinate  
Status: PROPOSED  
Authoring agent: `gpt56-07-b`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: L-9303  
Scope: exact finite total-count deflation  
Related counterexample candidates: none

## Statement

Let `C,T` be real numbers, let

```text
0 < R_1 < ... < R_K,
```

and suppose an unconditional zero-count certificate proves that the slab

```text
C-R_k < Im rho < C+R_k
```

contains at least `M_k` nontrivial zeta zeros, counted with multiplicity, where

```text
0 = M_0 <= M_1 <= ... <= M_K.
```

Define

```text
Delta = |T-C|,
R'_k  = R_k + Delta,
d_k   = M_k-M_(k-1).
```

Then the same certificate proves that at least `M_k` zeros satisfy

```text
|T-Im rho| < R'_k.
```

Consequently, under RH, L-9303 applies at the shifted direct-xi ordinate `T`
with the exact deflation

```text
sum_k d_k log(u + (R'_k)^2).
```

Every L-9303 monotonicity, positive-Gram, and cross-Loewner consequence remains
valid with these widened radii. A strict directed reversal still contradicts
RH.

## Definitions

- The source count center is `C`.
- The direct completed-xi ordinate is `T`.
- Every endpoint, radius, shift, and widened radius is represented exactly as
  a rational number.
- Counts refer to all nontrivial zeta zeros in the full critical strip, with
  multiplicity.

## Motivation

An unconditional total-count table is expensive to produce, while direct-xi
rectangles at nearby ordinates are comparatively cheap. This lemma permits a
rigorous nearby-ordinate search without repeating the count computation. The
cost is explicit and conservative: every source radius is widened by the
absolute ordinate shift.

## Proof

Take any zero counted in the source slab of radius `R_k`. Its ordinate
`gamma=Im rho` satisfies

```text
|gamma-C| < R_k.
```

The triangle inequality gives

```text
|gamma-T|
 <= |gamma-C| + |C-T|
 <  R_k + Delta
 =  R'_k.
```

Thus every zero counted in the source slab lies in the widened slab centered at
`T`; multiplicities are unchanged. Hence the widened slab contains at least
`M_k` zeros.

The common addition of `Delta` preserves strict radius ordering:

```text
R'_1 < ... < R'_K.
```

Assume RH. Every counted zero is then on the critical line, so the widened
radii are valid order-statistic upper bounds on the distances from `T`.
Applying L-9303 with `R'_k` proves the claimed complete-monotonicity and
Loewner consequences.

## Analytic domain audit

The lemma changes no analytic function and introduces no contour, branch, or
singularity. Each subtraction term `log(u+(R'_k)^2)` is real analytic for
`u>0`. The completed-xi normalization is exactly the one required by L-9303.

## Dependency audit

- The triangle-inequality count transfer is elementary and unconditional.
- Only the conversion of counted zeros into critical-line mass uses the RH
  hypothesis, exactly as in L-9303.
- All direct-xi positivity conclusions are inherited from L-9303.

## Gap audit

- Source endpoints must be checked against `C`, not silently relabeled as
  centered at `T`.
- The widened radius must be `R_k+|T-C|`; using `R_k` after shifting is
  unsound.
- Counts must include multiplicity and remain nested.
- This lemma supplies lower counts only. It does not identify individual zeros
  or assert that any zero is on the line unconditionally.
- A negative numerical midpoint is not a witness; the complete directed
  interval must be strictly negative.

## Adversarial tests

The X-9302 adapter tests:

- exact zero shift, recovering L-9303 unchanged;
- a half-unit shift, requiring radius `R+1/2`;
- endpoint drift around the original count center;
- Boolean and malformed count data;
- decreasing cumulative counts.

## Remaining uncertainty

The lemma itself is elementary. The inherited uncertainties are the
independent correctness of the total-count and direct-xi primitives and review
of L-9303's completed-xi normalization.

## Suggested next attack

Reuse one dual-precision count table over a rational mesh of nearby ordinates,
rank total-count-deflated cross-Loewner minors, and independently escalate only
strict negative nominees.
