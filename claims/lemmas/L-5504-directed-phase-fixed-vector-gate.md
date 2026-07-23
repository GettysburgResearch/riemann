# L-5504 — Directed phase replay and fixed-vector correction gate

Claim ID: L-5504  
Title: A complete directed prime manifest and one exact dyadic vector give a finite carrier sign certificate  
Status: PROPOSED  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; L-4202; L-4203  
Scope: exact-vector certification of piecewise-carrier Rayleigh values  
Related counterexample candidates: none

## Statement

Let `v in (Z[1/2]+i Z[1/2])^K` be nonzero, with exact squared norm `N`. Fix an
exact rational carrier `T` and an exact integer cutoff `c`. Suppose:

1. an exact manifest contains every prime and every higher prime power `q<=c`
   exactly once, with `Lambda(p^a)=log p`;
2. directed arithmetic produces an interval `[P_-,P_+]` containing the complete
   normalized prime Rayleigh value `v^*S_K(T,c)v`;
3. directed arithmetic produces `[A_-,A_+]` containing
   `alpha_T N`, where
   \[
   \alpha_T=\frac{\log(T/(2\pi))}{2\pi};
   \]
4. a rigorous operator bound `B` contains the exact archimedean deviation and
   pole block:
   \[
   \|(A_K-\alpha_T I)+R_K\|_2\le B.
   \]

Then the exact full Rayleigh value lies in

\[
 \boxed{
 [A_- -P_+-BN,\; A_+-P_-+BN].
 }
\]

In particular:

- if `A_+-P_-+BN<0`, the exact D-0801 form is negative on `v`;
- if `A_--P_+-BN>0`, the exact form is positive on `v`.

No interval eigenvector or interval eigensolver is required.

### Directed phase anchor

If a phase is enclosed by `phi in [phi_-,phi_+]` and
`w=phi_+-phi_-`, then

\[
 \cos\phi\in[\cos\phi_- -w,\cos\phi_-+w],
\]

\[
 -\sin\phi\in[-\sin\phi_- -w,-\sin\phi_-+w].
\]

Therefore one correctly rounded evaluation at the lower phase anchor, expanded
by the directed phase width, is a valid unit-circle enclosure even for enormous
unreduced phases.

### Uniform gate used by X-5501

For

\[
 10^8\le c\le1.02\times10^8,
 \qquad K=1024,
 \qquad T=\frac{94184072727073}{20},
\]

L-4202/L-4203 and elementary rational inequalities give

\[
 \boxed{B<\frac1{4,000,000,000}=2.5\times10^{-10}.}
\]

One admissible exact reconstruction is

\[
 B_A=\frac1{3T}
 \left(32(5+2H_{1022})+2046+\frac14\right),
\]

\[
 B_R=\frac{2\cdot5050\cdot4}
 {\left(\frac{3\cdot16}{2K}\right)
  \left(\frac{16}{2K}\right)T^2},
\]

for which `B_A+B_R<1/(4*10^9)` by exact rational comparison.

## Proof

For the phase anchor, the derivatives of sine and cosine have absolute value at
most one. The mean-value theorem gives the two width expansions. Directed
rounding of the anchor and each endpoint operation preserves containment.

By assumptions 2 and 3, the leading scalar-minus-prime value lies in
`[A_- -P_+, A_+-P_-]`. Assumption 4 and Cauchy--Schwarz give

\[
 |v^*((A_K-\alpha_T I)+R_K)v|\le BN.
\]

Adding the symmetric error interval proves the full enclosure and both sign
rules.

For the uniform gate, `c>=10^8` and `e^2<10` imply `L=log c>16`; hence
`b=2L/K>32/K` and `1/b<32`. Also `pi>3`. Substitution into L-4202 gives `B_A`.
For `c<=102000000`, `sqrt(c)/2<5050`; the displayed elementary lower bounds on
`pi^2h` and `sinh(pi h)` give `B_R` through L-4203. The committed exact checker
performs the final rational comparison. ∎

## Motivation

This is the terminal proof interface for the requested six-stage pipeline. All
heuristic work—eigenvectors, threshold ranking, phase models, and local
optimization—ends before this lemma. The proof object is a finite manifest, an
exact vector, directed intervals, and one rational sign comparison.

## Analytic domain audit

All phase and logarithm evaluations are at positive real arguments. The prime
sum is finite. D-0801 admissibility and the Guinand--Weil identity remain
separate dependencies and are not proved here.

## Dependency audit

L-0801 supplies the exact prime Toeplitz expression. L-4202 and L-4203 supply
the archimedean and pole operator bounds. The interval argument is independent
of the discovery implementation.

## Gap audit

- The manifest must be complete and bind to the exact cutoff.
- Every phase, hat position, amplitude, correlation, and accumulation operation
  must be outward rounded.
- A midpoint vector is not the exact dyadic vector.
- The compact gate scales by `N`; it is not simply added when the vector is not
  normalized.
- A negative leading interval smaller than the gate is unresolved.
- The explicit-formula normalization and test admissibility remain blocking
  dependencies for an RH conclusion.

## Adversarial tests

1. Mutate one manifest count or digest and reject.
2. Widen a phase until the final sign interval touches zero and reject.
3. Mutate one dyadic coordinate and reject the vector digest.
4. Relabel a positive control as negative and reject.
5. Compare a small-cutoff replay with an independent high-precision backend.
6. Rerun at higher precision and require nested intervals when the same producer
   environment is used.

## Remaining uncertainty

The executed X-5501 producer uses MPFR directed functions and passes a small
independent control, but it has not been independently reimplemented for the
full `10^8` manifest. The theorem itself has no known gap.

## Suggested next attack

Export the PR #44 `c=10^11` leading vector and shard manifest, then run a
segmented MPFR producer using this exact fixed-vector interface. The target
phase error budget is orders of magnitude looser than arbitrary full-matrix
entry certification.
