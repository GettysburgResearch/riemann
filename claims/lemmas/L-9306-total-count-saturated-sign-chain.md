# L-9306 — Total-count-saturated Hardy-​Z sign chains isolate every zero

Claim ID: L-9306  
Title: An exact total count equal to a certified alternating Hardy-​Z sign chain yields pairwise-disjoint one-zero bins and arbitrary dyadic refinement  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: continuity of Hardy's `Z`; exact total zero count in a critical-strip slab  
Scope: proof-grade critical-line zero bins for direct-`xi` and Pick deflation  
Related counterexample candidates: none

## Statement

Let `a<b` be exact real ordinates that are not ordinates of nontrivial zeros of
`zeta`. Let

\[
 a<s_0<s_1<\cdots<s_m<b
\]

be exact real sample points. Suppose all of the following have been certified.

1. A proof-grade argument-principle or Turing computation gives the exact total
   number of nontrivial zeros in the open slab
   \[
      a<\operatorname{Im}\rho<b,
   \]
   counted with multiplicity, as
   \[
      N(a,b)=m.
   \]
2. For every `j`, a directed enclosure of Hardy's real function
   \[
      Z(t)=e^{i\theta(t)}\zeta(1/2+it)
   \]
   at `s_j` excludes zero.
3. The certified signs alternate:
   \[
      \operatorname{sgn}Z(s_{j-1})
      =-\operatorname{sgn}Z(s_j),
      \qquad 1\le j\le m.
   \]

Then:

### A. Exact one-zero bins

Every interval

\[
 I_j=(s_{j-1},s_j),\qquad 1\le j\le m,
\]

contains exactly one nontrivial zero of `zeta`, counted with multiplicity. That
zero lies on the critical line and is simple. There are no other nontrivial
zeros in the slab `(a,b)`.

Thus the intervals `I_j` are unconditional, pairwise-disjoint, exact
critical-line zero bins with lower count and exact count both equal to one.

### B. Sign-preserving refinement

Fix one bin `(l,r)` whose endpoint signs are certified and opposite. Let `x`
be any exact point with `l<x<r` for which a directed enclosure of `Z(x)` excludes
zero. Then exactly one of

\[
 (l,x),\qquad(x,r)
\]

has opposite certified endpoint signs, and that subinterval remains an exact
one-zero bin.

Consequently, repeated exact-dyadic bisection, with fail-closed precision
escalation whenever a midpoint sign is unresolved, produces arbitrarily narrow
pairwise-disjoint certified zero bins without evaluating a zero-locating or
Newton primitive.

### C. Direct-`xi` deflation interface

For any exact target ordinate `T`, a refined bin `[l_j,r_j]` supplies the valid
squared-distance upper bound

\[
 B_j=\max\{(T-l_j)^2,(T-r_j)^2\}.
\]

Therefore the bins may be inserted directly into `L-9301` as independently
certified critical-line zero lower-count-one gates. Under RH, subtracting

\[
 \sum_j\log(u+B_j)
\]

from the horizontal completed-`xi` logarithmic modulus preserves all declared
complete-monotonicity and cross-Loewner inequalities.

## Definitions

The completed zeta function is

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Hardy's function is the real-valued continuous function on the real line

\[
 Z(t)=e^{i\theta(t)}\zeta(1/2+it),
\]

with the standard continuous Riemann--Siegel phase. Its real zeros are exactly
the critical-line nontrivial zeros of `zeta`, with the same multiplicities.

A **certified sign** means an outward-rounded real interval for `Z(t)` lies
strictly inside `(0,infinity)` or `(-infinity,0)`. A ball containing zero has no
certified sign.

An **exact total count** means the zero-count output is itself enclosed in a
ball containing one and only one integer and all analytic hypotheses of the
counting routine, especially endpoint nonvanishing, are discharged.

## Motivation

At very large ordinate, locating one indexed zero with a general-purpose
Platt/Newton routine can be much more expensive than evaluating `Z` at one
specified point. A sign-change census already proves one line zero per
alternation, while a total count proves that no unobserved multiplicity remains.
When the two counts agree, root location is unnecessary: the sign intervals are
already exact isolating bins.

This is especially useful at the PR #71 ordinate. `O-5608` records an exact
40-unit total count of `172` and a chain of `173` exact samples with `172`
certified alternations and no undecided signs. The theorem converts that one
computation into `172` independently refinable zero bins, suitable for the
zero-deflated direct-`xi` route.

## Proof

For each `j`, continuity of `Z` and opposite endpoint signs imply by the
intermediate value theorem that `Z` has a zero in `I_j`. Such a zero is a
nontrivial zero of `zeta` on the critical line. The intervals are pairwise
disjoint, so these give at least `m` distinct critical-line zeros and therefore
at least `m` nontrivial zeros in the slab, counted with multiplicity.

The exact total count is `m`. Hence every lower bound just obtained is sharp:

- every `I_j` contains total multiplicity exactly one;
- no zero lies in `(a,s_0)`, `(s_m,b)`, at a sample point, or elsewhere in the
  slab;
- the unique zero in each `I_j` is on the critical line;
- its multiplicity is one.

This proves part A.

For part B, the certified nonzero sign at `x` equals one of the two opposite
endpoint signs. It therefore agrees with exactly one endpoint and disagrees
with the other. The subinterval with disagreeing endpoint signs contains a
line zero. Since the original interval contains exactly one zero with total
multiplicity one, that subinterval contains the same unique zero and the other
subinterval contains none. Repetition proves the refinement claim. Choosing
the dyadic midpoint halves the width whenever its sign is certified.

For part C, the unique ordinate `gamma_j` lies in `[l_j,r_j]`, so

\[
 (T-\gamma_j)^2\le
 \max\{(T-l_j)^2,(T-r_j)^2\}=B_j.
\]

This is precisely the upper squared-distance input required by `L-9301`; its
positive-kernel subtraction argument then applies. QED.

## Certificate schema

A minimal sign-chain certificate contains

```text
slab endpoints a,b                 exact rationals or dyadics
total-count ball                   directed, unique integer m
sample ordinates s_0,...,s_m       exact dyadics
Z intervals at every sample        directed, each excluding zero
sample signs                        recomputed from the intervals
claimed alternation count           m
count/source digests                immutable
```

A refinement certificate additionally contains, per bin, the sequence of exact
trial points and directed `Z` intervals. The checker reconstructs which half
was retained after every step; it does not trust a declared final interval.

## Analytic domain audit

- `Z` is evaluated only at real ordinates.
- Every sample must lie strictly inside the open count slab.
- The count endpoints must be proved zero-free according to the semantics of
  the count primitive.
- No logarithm of `zeta`, contour deformation, zero simplicity assumption, or
  division by `xi` occurs in the sign-chain proof.
- Simplicity is concluded from equality with the multiplicity-aware total
  count; it is not inferred merely from a sign change.

## Dependency audit

- Continuity and the real-zero correspondence for Hardy's `Z` give one line
  zero per sign alternation.
- The exact total count gives the global multiplicity ceiling.
- `L-9301` is used only for the optional direct-`xi` deflation consequence.
- `O-5608` is an application artifact, not a logical dependency of the general
  theorem.

## Gap audit

- Alternating floating signs are not enough; every sign must be a directed ball
  excluding zero.
- A smooth Riemann--von Mangoldt estimate is not an exact total count.
- Equality of the number of guide zeros with the count is irrelevant unless
  the actual sample signs alternate.
- An unresolved midpoint may not be assigned a sign from its floating midpoint.
- A sign change alone proves an odd-multiplicity line zero, not simplicity;
  simplicity here uses the exact multiplicity-aware count equality.
- Bins that touch at a sample point are disjoint as open intervals because the
  sample is certified nonzero. Closed transport intervals may share a
  zero-free endpoint, which a checker must handle explicitly rather than call
  overlapping zero mass.
- Refining one bin may not alter or reorder neighboring sample endpoints.
- The theorem certifies only the declared finite slab.

## Adversarial tests

1. Supply three alternating signs but total count four; require the checker to
   reject exact-isolation status while retaining a lower count of three.
2. Supply total count three but only two alternations; require rejection.
3. Insert an unresolved sample interval containing zero; require fail-closed
   behavior.
4. Reverse one midpoint sign during bisection; require reconstruction to detect
   that the retained half no longer has opposite signs.
5. Use a synthetic polynomial with two roots inside one initial interval and a
   compensating empty interval; total-count equality must fail.
6. Use one double root: no sign alternation occurs across it, and the method
   must not certify it through a sign chain.
7. Verify that the farthest-endpoint formula for `B_j` remains valid when `T`
   lies inside, to the left of, or to the right of the bin.

## Remaining uncertainty

The theorem is elementary and complete-looking, but its first production use
still depends on obtaining the exact `O-5608` sample table and replaying the
Hardy-`Z` balls in an independently reviewed backend. The numerical sharpness
of the resulting direct-`xi` deflation depends on how cheaply the 172 bins can
be narrowed.

## Suggested next attack

Serialize the 173 exact `O-5608` sample points and their directed Hardy-`Z`
intervals, verify the saturated chain with a standard-library checker, and run
parallel sign-preserving bisection only on bins ranked by sensitivity of the
smallest PR #71 zero-deflated cross-Loewner row. Stop refinement as soon as a
strict directed sign is obtained or every bin's uncertainty contribution is
below the remaining positive moat.
