# Sources, proof scope, attempted closure, and execution record

## Analytic inputs and reading scope

1. Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
   arXiv:2610.04045v1, Theorem 1.1, definitions (1.2) and Sections 2.1--2.5.
   https://arxiv.org/html/2610.04045v1
   The primary HTML was freshly obtained. The theorem's four monomials and
   BOTH n-th-power-free index conventions were readable explicitly. The fixed
   field and admissible generator/ray choices are part of the theorem, not
   uniform parameters. The deep proof and all its dependencies were not rebuilt.
   Corollary 1.5 is not an input to this new residual theorem.

2. Blomer--Goldmakher--Louvel, *L-functions with n-th order twists*,
   arXiv:1112.1650, Section 5 and the preceding Hecke setup.
   https://arxiv.org/pdf/1112.1650
   The primary PDF was obtained; printed pages 18--19 were rendered and read
   for the common-column Mellin separation and the Mobius detector context.
   The exact flat-cutoff functional equation used here is a reconstruction,
   not a claim that BGL prints this new bound. Their zero-detector inequality,
   multiple-series theorems and zero-density exponents are NOT premises here.

3. #984, b6a29037a2be358294401d71d7305b0f402c2eea,
   standalone/2026-10-18-reciprocal-moment-law/MOLLIFIED_APPROXIMATION.md
   and RECIPROCAL_MOMENTS.md.
   Both were freshly read through GitHub. The first supplies the prior
   signed-residual idea, exact flat-cutoff cancellation, small-conductor
   warning and old pointwise-dual estimate. We reconstruct its needed
   functional-equation interface and replace its final dual-product estimate.
   The second's Euler asymptotic, common zero-selected good set and cap remain
   unchanged and are NOT newly certified or silently removed.

4. #980, 392223625496b6674795fa8e1c0eb9768688f1ef,
   the prior finite-translation work and its still-open prime/continuum
   estimate. Its live published state was verified. Its archive was not
   rerun in this pass and it is not a premise of the new residual theorem.

5. #983, e9ce2d171fba2bcca4cb4d8c6e78dc97f69613e9, inspected at live PR
   description scope only: fixed-principal moment versus growing-family
   distinctions and the remaining weighted vertical adapter. No new
   mathematical or formal statement from it is adopted as an input here.

No CT or quasi-RH theorem, no assumed inverse-L moment, no theta-to-native
projection, and no density hypothesis is used. One CT-v2 landing-page fetch
failed; its body was not needed or imported. Classical Holder, Dirichlet
polynomial powering, ideal counting, functional equations and subharmonic
mean inequalities are credited. No worldwide priority or optimality claim
is made for the new specialization or for these methods.

## What was attempted and what was actually gained

The requested goal was the full prescribed-member critical estimate, not a
new fraction near 0.9. We examined whether the latest full-family signed
approximate inverse could remove its exceptional/cap restriction.

The new mixed-moment argument improves the complete residual itself. At 3/4
it gives U^(11/15+epsilon) rather than the prior displayed U^(7/8+epsilon),
and supports a length U^(3/5) mollifier rather than U^(1/4). An explicit
high-order argument triples the near-critical sextic saving on every fixed
line in the displayed neighborhood of 1/2. These are full-family estimates,
not just reformulations or subset definitions.

The closure does not follow: E_A equals -1 at a zero, so an error bound with
a positive power of U can still accommodate one persistent exceptional row.
The common compact-segment relative approximation is asserted only after
accounting for the bad count. Higher fixed residual moments keep a growing
power cost; no varying-order uniform estimate is inferred. This is a real
remaining arithmetic gap, not unfinished exponent bookkeeping or a merely
pending numerical test. No new global zero-free boundary or RH proof is claimed.

## Executed finite checks

`python replay.py` freshly passed. Normal and optimized runs reproduce
CHECKS.json byte-for-byte. There are 10,540 explicit finite predicates,
INCLUDING repeated setup and grid guards, with group counts in that report.
Ten separately executed corrupted optimized processes fail at their intended
gates and reproduce MUTATIONS.json.

Coverage includes the exact 3/4 exponent identities; 400 rational near-line
parameter choices in five fixed character orders; actual-conductor exponents
on declared grids, including subunit dual lengths; 420 finite mixed Holder
arrays; full flat-cutoff convolutions at the listed integer cutoffs; and
error powers through degree three, with every produced product retained.

Character checks use exact arithmetic in Q(omega) for FOUR declared profiles
of actual residue characters modulo 7 and 13, including imprimitive principal
characters and original nonunit zeros. They include 2,500 mixed ratio identities
and 900 sixth-power-removal cases with shared primes. This is NOT a complete
number-field Hecke-family, actual L-value, theta-row or zeta-zero computation.
The test cutoff is rational and piecewise flat/linear; it verifies algebra,
not the analytic smooth-weight decay premise.

A principal-row audit found that the primitive polar term cannot be inserted
into the U^(1/2) dual fourth-moment bound. The proof excludes principal rows
from THAT auxiliary bound and adds their final residual contribution separately.
The published Theorem A covers them. A negative control rejects the false
extension. Noninteger powering of Dirichlet polynomials is also explicitly
rejected; every fractional moment use is by valid interpolation.

The exploratory floating-point LP under /mnt/data was used only to suggest
parameters. It is not part of this packet or an acceptance premise. All
published parameters and certificates are exact rational calculations, and
the general interval theorem has a written algebraic proof rather than a
sampled-grid inference.

Proof and checker have the same author. No independent AI/human referee,
Lean build, whole-repository validator, upstream theorem rebuild, or remote
CI execution is claimed. A byte manifest authenticates files, not mathematics.
