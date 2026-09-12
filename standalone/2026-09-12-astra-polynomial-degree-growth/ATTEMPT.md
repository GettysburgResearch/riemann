# Full-problem attempt and the latest research context

Status: PROPOSED; full completion NOT obtained.

## 1. What changed since the previous response

A live 25-PR census covers #838--#862. A second repository-wide updated-PR
search since 2026-09-10T19:25:56Z returned nine items, all inside that census.
This is not a proof review of 25 branches or the complete historical repository.
Each exact head and reading depth appears in LATEST_WORK.tsv. Main was frozen
at f99d9e3908dde4865377c75d9ca051c1f545bf4f.

The latest PR845 head is 59384bcdea88bdedb86c503479c6c26c681daf5e, not the
b9ccd03 checkpoint in the last conversation answer. It adds AC29's explicit
origin cutoffs and simultaneous graph approximation. Its complete PROOF.md
was read; the live discussion was empty. The previous four-file locally
unpublished derivative-obstruction packet has landed separately as PR861;
its NOTE.md Git blob matches the old supplied ZIP. These are distinct packets.

PR848 now has 37 changed paths and live head 2f0056d542603cb8118b9ac9da45b397162778e4.
Its PR body still opens with the original a1b4625 head. Reading only that body
would miss the innovations, cubic-residual and collision-energy continuations.
The complete collision-energy proof was read here. Its all-scale diagonal is
polylogarithmic, but its actual distinct-product covariance is unbounded in
scope and still unestimated. It is all-integer, not our odd-source norm.

Other latest work was assessed at metadata/description level, NOT independently
verified. It importantly rules out some apparent cross-program shortcuts:

* #842's connected 73-spin ten-moment realization and higher fixed-order local
  submersion do not provide all-order target reachability.
* #856 refutes the actual full Brownian companion phase condition; the older
  proposals cannot still consume it as a theorem.
* #858 certifies a nonreal zero of the centered N=5 approximant, NOT xi. Its
  finite exceptional-index theorem is not disappearance of the limiting defect.
* #859 and #860 give alternative fixed-depth high-height theorems under the
  SAME path and claim ID, with different proofs and evidence. They must be
  reconciled rather than counted as independent reviews or merged blindly.
* Faster complete gamma/branching approximation does not exchange a fixed-depth
  high-height theorem with an unbounded-depth/global-height limit.

None of those unresolved arrows is imported as a hypothesis silently satisfied.

## 2. Why pursue degree growth rather than another uniform inequality

The original goal was a degree-uniform C_eta in the compensated polynomial
inequality. The native zero modes make its boundary constants delicate, and
necessity for RH was not shown. We removed that potentially excessive demand:
allow the best eta=0 finite-dimensional cost to grow, but control its exponent.
The exact inverse-coordinate map then produces the positive scalar S_N with
NO optimization over coefficients. Every term is a full squared norm, not a
chosen diagonal from a different arithmetic source.

The new global theorem is that even liminf log(1+S_N)/log N=0 gives RH. This
requires the degree-controlled construction in PROOF.md Section 4; qualitative
polynomial density alone does not let one compare the witness to a supplied
unbounded sequence of degree caps. An off-line zero would force a positive
power lower bound at every large degree, so it cannot hide between certificates.

## 3. Actual upper-bound attack and its stopping point

In the odd Legendre coordinates, the output-side covariance adds positive
rank-one operators. This makes the positive block energy

    d_N = sum_(j=N)^(2N-1)||Kphi_j||^2

an exact target. A polylogarithmic bound on d_N on all late dyadic degrees
would close the whole argument. The new boundary decomposition controls
S_N<=800(2N-1) unconditionally and proves the desired subpower upper bound
ONLY when the RH-strength Mobius estimate is assumed. No argument making
d_N polylogarithmic or subpower was found.

The finite trace estimates are below four through N=32, but the new logarithmic
lower theorem proves that four is NOT a global ceiling. Thus fitting or extending
that plateau would be a false completion. The code does not fit an asymptotic
law or label finite matrices all-degree evidence.

PR848's true coalesced collision diagonal cannot be substituted for d_N. Its
cross-product covariance remains signed and open, and the projections/weights
are different. The derivative-based comparison is ruled out by the exact
native family in PR861. We do not claim either result solves this new bound.

## 4. What would constitute completion

Prove a source-specific bound for S_N at an unbounded sequence N_j with
log(1+S_(N_j))/log N_j tending to zero. The degrees can be sparse and the
constants need not remain bounded. Sections 4--5 then exclude every off-critical
zero and reflection gives RH. No separate cycle, positivity, or domain premise
is needed AFTER that exact bound; the bound itself is still OPEN.

All new component results require independent review. No full proposed RH proof
with that estimate hidden as a lemma is being submitted.
