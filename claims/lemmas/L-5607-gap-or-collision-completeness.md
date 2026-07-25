# L-5607 — Gap-or-collision completeness for finite RH counterexamples

Claim ID: `L-5607`  
Title: Every off-critical zero is exposed either by a positive count in a critical-line-empty gap or by an excess-multiplicity collision at a critical-line ordinate  
Status: PROPOSED  
Authoring agent: `gpt56-02-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `L-5605`; discreteness of the nontrivial zero set; functional-equation and conjugation symmetry  
Scope: exhaustive zero-counting architecture  
Related counterexample candidates: none

## Statement

Let

\[
 \Gamma_0=\{\gamma>0:\zeta(1/2+i\gamma)=0\}
\]

be the set of positive critical-line zero ordinates, ignoring multiplicity for
its topology. Suppose RH is false and let

\[
 \rho=\beta+i\gamma,
 \qquad
 \beta\ne\frac12,
 \qquad
 \gamma>0
\]

be an off-critical zero. Exactly one of the following alternatives holds.

### Gap case

If `gamma` is not in `Gamma_0`, there are rational zero-free endpoints `a<b`
with

\[
 a<\gamma<b,
 \qquad
 N_0(a,b)=0,
 \qquad
 N(a,b)\ge2.
\]

Thus `L-5605` gives a finite unconditional RH-disproof certificate entirely
inside one critical-line-empty gap.

### Collision case

If `gamma` belongs to `Gamma_0`, there are rational zero-free endpoints `a<b`
containing no zero ordinate other than `gamma` such that

\[
 N(a,b)>N_0(a,b).
\]

The excess is an even positive integer and gives a finite unconditional
RH-disproof certificate. Operationally, the proof object is a certified total
multiplicity at the ordinate cluster minus a certified Hardy-Z multiplicity.

Consequently, a proof-producing enumeration of

1. every open gap between consecutive positive critical-line zero ordinates, and
2. every critical-line ordinate cluster with its multiplicity,

is existentially complete for detecting RH failure.

## Proof

The set of nontrivial zeros is discrete. Its intersection with the critical line
is therefore discrete as well.

If `gamma` is not a critical-line ordinate, choose an open interval around
`gamma` disjoint from `Gamma_0`. Shrink it, if necessary, so that its endpoints
are not ordinates of any nontrivial zero, and replace the endpoints by rationals
without changing these properties. The reflected zero

\[
 1-\overline\rho=1-\beta+i\gamma
\]

has the same positive ordinate and multiplicity, so the slab contains at least
two total zeros but no line zero. This is the gap case.

If `gamma` is a critical-line ordinate, discreteness permits an open interval
containing no other zero ordinate. Choose rational zero-free endpoints inside
that isolating interval. The total multiplicity in the slab equals the
critical-line multiplicity at `gamma` plus the multiplicities of the off-line
reflected pair or pairs at the same ordinate. Therefore it is strictly larger
than the line multiplicity, and the excess is even by symmetry. This is the
collision case.

The two cases are mutually exclusive and exhaust all possibilities for
`gamma`, proving completeness. ∎

## Why a large-gap sieve is useful but not complete by itself

A large empirical Hardy-Z gap is an efficient nomination target because it
makes the line count `N0=0` in the proposed interior and leaves a comparatively
wide numerical moat for directed nonvanishing. But an off-line zero can lie in
a small gap, and it can share an ordinate with a line zero. Therefore:

- ranking large gaps is a discovery optimization;
- certifying **all** gaps and all collision clusters is the completeness layer;
- no gap-size threshold may enter the theorem.

## Finite certificate schemas

### Gap certificate

```text
exact rational a<b
consecutive certified Hardy-Z zero balls outside (a,b)
N0(a,b)=0
exact Turing integers N(a), N(b)
D=N(b)-N(a)>0
```

### Collision certificate

```text
exact rational a<gamma<b
one certified critical-line root cluster in (a,b)
exact critical-line multiplicity m0
exact total-zero count m
m-m0>0
```

Both terminate in the same exact `L-5605` discrepancy checker.

## Search protocol

1. Use an inexpensive ordinary Riemann--Siegel scan only to rank gaps and
   suspicious clusters.
2. Replace every nominated ordinate and endpoint by exact rationals or dyadics.
3. Isolate consecutive Hardy-Z zeros with directed Platt/Turing arithmetic.
4. In gap cells, choose exact endpoints strictly between the isolating balls and
   compute total zero counts.
5. In collision cells, evaluate Hardy-Z derivatives or a small argument contour
   to certify line multiplicity, then compute the total count.
6. Promote only a strict positive integer discrepancy reproduced by an
   independent implementation.
7. For completeness over a bounded height range, maintain a contiguous,
   gap-free manifest of every certified gap and every line-root cluster.

## Analytic and domain audit

- The theorem is existential and does not assert that a bounded scan settles RH.
- A critical-line zero of even multiplicity belongs to the collision ledger even
  though it produces no sign change.
- Exact ordinate equality is handled by the collision case; it is never dismissed
  as probability zero in the proof.
- Endpoints are chosen away from all zero ordinates, so no half-weight convention
  is needed.

## Adversarial tests

1. One off-line reflected pair in an otherwise empty line gap.
2. One off-line pair sharing an ordinate with a simple line zero.
3. One off-line pair sharing an ordinate with a double line zero.
4. Several off-line pairs at one ordinate; verify an even excess.
5. A line-only double zero; verify zero discrepancy despite no sign change.
6. Delete one gap or collision cluster from a bounded manifest and require the
   completeness checker to reject the height range.

## Remaining uncertainty

No bounded range above the established verification height is certified by this
lemma. The computational bottleneck is the directed Platt/Turing production and
an independent multiplicity backend.

## Suggested next attack

Use the PR #71 gap as the first exact gap-cell control. Then run the same
`N-N0` producer over a batch of the largest empirically nominated gaps in a
contiguous high-height window. A single positive integer discrepancy is the
requested unconditional counterexample; all zero discrepancies become a
proof-carrying local RH verification ledger.
