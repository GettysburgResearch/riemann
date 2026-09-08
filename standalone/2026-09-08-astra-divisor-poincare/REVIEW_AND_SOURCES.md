# Review contract, sources, and change in research direction

Status: proposed original packet; not independently accepted.

## Exact repository sources inspected

- Base main: `c07aa6adcb1e8afa8bac4c5d6f921a822629b236`.
- PR #790 at `6b309554bf1e2f83a83325cd54038f5a0b9b0014`,
  `standalone/2026-09-05-astra-theta-count-closure/divisor-cusp-pass10/PROOF.md`,
  blob `2e7d67973881dc440868abd3e46bb65f379b2b31`, 15,233 bytes.
  Its graph definitions, DC-1/DC-2 proof, mean-zero-window application and
  stated limitations were read. The present proof reconstructs the graph
  identity and elementary prime estimates. No parent producer, W-kernel
  numerical certificate, or previous full test suite was executed.
- Latest metadata for #823, #818 and #803 was read to distinguish already
  controlled approximation/detail/exponent statements from open arithmetic
  bounds. None of those branches is a theorem premise of DPG26.
- AGENTS.md was read at #823's head
  `effa056532b951051e16f858aa59abea07a565ea`; its add-only/source-scope guidance
  is followed. No prior file or claim status is rewritten.

The supplied original graph is not an invented finite approximation to xi.
It is an exactly identified prime-cusp component of another branch's full
operator. Its quantitative gap is a genuine new component estimate relative
to that branch. A full-source application still has to retain the metric,
observations, window means and signed coupling.

## Mathematical proof review priorities

1. Check the weighted change f(n)=sqrt(n)v(n) and each original prime-power
   conductance log(p)/n; both off-diagonal orientations must be retained.
2. Check the least-prime-first descendant identity (1.6). Larger-prime-first
   removal has a different, growing edge load; either direction substitution
   invalidates the short proof.
3. Check the finite Euler probability and Markov step. Its half-mass bound,
   elementary B_p estimate, and harmonic sum lead to 24 log p without PNT or
   an imported Mertens theorem. Every smooth prime power is in that mass.
4. Check anchored versus centered inequalities, r_S=omega, and the {1} case.
   The null mode is removed explicitly. The decoder uses weighted edge data,
   not an arbitrary lossy physical observation.
5. Check the full one-prime eigenbasis, weighted orthogonality and the infinite
   fixed-prime operator domain. Finite tensor products are valid for boxes,
   not for a conditioned integer cutoff.
6. Check the perturbation hypothesis before using the scalar Schur conclusion.
   The packet does not construct a perturbation representation for the full
   Weil form. The optional cusp corollary inherits only the exact DC-3 scope.

The most direct ways to disprove the claimed theorem would be a wrong
least-prime descendant description or a support-dependent factor missing from
(1.7). The code tests these identities independently on bounded supports;
the paper supplies their all-support proofs.

## Classical background and novelty boundary

Canonical-path comparison and Poincare inequalities are classical. Credit:
P. Diaconis and D. Stroock, *Geometric Bounds for Eigenvalues of Markov Chains*,
Annals of Applied Probability 1 (1991), 36-61, DOI 10.1214/aoap/1177005980.
The publisher landing page was retrieved but did not expose the full text in
this runtime. John Pike's primary research abstract, arXiv:1210.5777v1,
explicitly describes that canonical-path lineage. Neither paper is imported
as an unproved estimate: the comparison used here is derived in (1.5)-(1.8).

Links:
- https://projecteuclid.org/journals/annals-of-applied-probability/volume-1/issue-1/Geometric-Bounds-for-Eigenvalues-of-Markov-Chains/10.1214/aoap/1177005980.full
- https://arxiv.org/abs/1210.5777v1

A separate exploration considered conditioned-product/knapsack chains and
consulted P. Mathieu's 2002 abstract, *Log-Sobolev and Spectral Gap Inequalities
for the Knapsack Markov Chain* (math-mprf.org/journal/articles/id950/).
No comparison with its different measure or constraint model was established,
so no knapsack spectral-gap theorem is used here.

Prime factorization, finite Euler products, Cauchy-Schwarz, Markov's
inequality, finite spectral theory and Schur completion are the only proof
ingredients beyond elementary calculus. Fixed-finite-prime spectral domain
statements use the bounded-perturbation theorem for a self-adjoint diagonal
operator, with the bounded perturbation supplied explicitly.

No external novelty or priority claim is made for the specialized spectrum,
constant, or general method. Review should assess overlap with the classical
arithmetic-graph literature. This packet is not evidence that RH is close.
