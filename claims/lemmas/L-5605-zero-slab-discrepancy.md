# L-5605 — Exact zero-slab discrepancy criterion

Claim ID: `L-5605`  
Title: RH fails exactly when a finite ordinate slab contains more total zeros than critical-line zeros, both counted with multiplicity  
Status: PROPOSED  
Authoring agent: `gpt56-02-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: functional-equation and conjugation symmetry; the argument principle for the total count  
Scope: finite zero-counting certificates  
Related counterexample candidates: none

## Statement

Let `a<b` be real numbers that are not ordinates of nontrivial zeros. Define

\[
 N(a,b)=\sum_{\substack{\rho:\ a<\Im\rho<b}}m(\rho),
\]

where every nontrivial zero in the critical strip is counted with its
multiplicity, and

\[
 N_0(a,b)=\sum_{\substack{\rho:\ \Re\rho=1/2\\a<\Im\rho<b}}m(\rho).
\]

Then

\[
 \boxed{D(a,b):=N(a,b)-N_0(a,b)\ge0}
\]

is exactly the number of off-critical zeros in the slab, counted with
multiplicity. In a positive-ordinate slab it is even:

\[
 \boxed{D(a,b)\in2\mathbb Z_{\ge0}.}
\]

Consequently,

\[
 \boxed{D(a,b)>0\Longrightarrow \text{RH is false}.}
\]

Conversely, if RH is false, there exist rational zero-free endpoints `a<b` for
which `D(a,b)>=2`. Thus one exact finite slab discrepancy is an unconditional
RH counterexample certificate.

## Empty-line-gap corollary

Suppose a rigorous interval computation proves

\[
 Z(t)\ne0\qquad(a<t<b),
\]

so that `N_0(a,b)=0`. Then

\[
 \boxed{N(a,b)>0\Longrightarrow \text{RH is false}.}
\]

This is the correct proof target suggested by the large empirical PR #71 gap:
certify an open line-zero-free interval and independently count every zeta zero
in its full critical-strip slab.

If instead `N(a,b)=0`, the certificate proves only that this finite slab is
empty of all zeros. It does not imply RH elsewhere and does not by itself fix
the sign of a global Pick or Weil functional.

## Sign-change warning

Let `V(a,b)` be the number of sign changes of Hardy's real function `Z(t)` on
`(a,b)`. Then

\[
 V(a,b)\le N_0(a,b),
\]

but equality requires additional multiplicity information. Therefore

\[
 N(a,b)>V(a,b)
\]

is not a counterexample certificate. A double zero on the critical line has
`N=N0=2` and `V=0`.

A proof-producing line count may use sign-changing isolating intervals for
simple zeros together with separate interval derivative or argument-variation
certificates for every remaining root. It must count multiplicities.

## Proof

Every zero counted by `N_0` is also counted by `N`, so their difference is the
sum of the multiplicities of exactly those zeros with real part different from
`1/2`. This proves nonnegativity and the first assertion.

For a zero `beta+i gamma` with `gamma>0` and `beta!=1/2`, the functional equation
and conjugation give the distinct zero

\[
 1-\overline{\rho}=1-\beta+i\gamma
\]

at the same positive ordinate and with the same multiplicity. Off-line zeros in
a positive-ordinate slab therefore occur in pairs, proving evenness.

If the difference is positive, at least one off-line zero exists and RH is
false.

Conversely, take any off-line zero `beta+i gamma` with `gamma>0`. The zero set is
discrete, so choose real `a<gamma<b` avoiding all zero ordinates and containing
no other ordinate outside a sufficiently small neighbourhood of `gamma`.
Approximate the endpoints by rationals while preserving these properties.
The slab contains the off-line reflected pair and hence `D(a,b)>=2`. This proves
the converse. The empty-line-gap corollary is immediate. ∎

## Finite certificate contract

A certificate should contain:

1. exact rational endpoints `a<b`;
2. directed nonvanishing on both horizontal boundaries used by the total-count
   contour;
3. an exact integer `N(a,b)` from an argument-principle or Turing certificate;
4. a complete list of disjoint critical-line root intervals in `(a,b)`;
5. a multiplicity certificate for each listed root;
6. a proof that no other critical-line root occurs in the slab;
7. exact integer arithmetic establishing `N-N0>0`.

For an empty-line-gap certificate, items 4--6 are replaced by one directed proof
that `Z` is nonzero on the whole interval.

## Implementation note

FLINT already exposes rigorous Platt/Turing routines including
`acb_dirichlet_platt_zeta_zeros` and Hardy-Z isolation. A proof-grade
continuation should use those directed routines rather than infer a total count
from the smooth term `(theta(b)-theta(a))/pi` or from convergence of sampled
sign changes.

## Analytic and domain audit

- Boundaries containing a zero are forbidden unless a half-weight convention is
  explicitly reconstructed.
- Multiplicity is part of both counts.
- The evenness conclusion is stated for positive ordinates; slabs meeting zero
  need separate symmetry bookkeeping.
- The criterion is local and finite but not a claim that any particular slab
  has a discrepancy.

## Adversarial tests

1. A slab containing two simple line zeros: `N=N0=2`, no discrepancy.
2. A slab containing one double line zero: `N=N0=2` but `V=0`.
3. A slab containing one reflected off-line pair: `N=2`, `N0=0`.
4. A slab containing one line zero and one off-line pair: `N=3`, `N0=1`.
5. Move a zero to a boundary and require rejection.
6. Delete one line-root interval and require the multiplicity ledger to fail.

## Remaining uncertainty

No total or line count near the PR #71 ordinate is certified by this lemma. It
only gives the exact target and the proof boundary.

## Suggested next attack

Use FLINT's rigorous Platt/Turing implementation to isolate a block of
consecutive zeta zeros around the exact PR #71 rational ordinate. If two
consecutive **total** zero balls bracket the ordinate, the intervening slab is
certified empty. Search neighbouring empirically large line gaps the same way;
a total zero inside a rigorously line-empty slab would be an unconditional
counterexample.
