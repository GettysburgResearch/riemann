# Green–Gram conditioning of the optimal residue selector

Date: 2026-08-23

Checkpoint base: `cf07de0ba009e8b288eb98b6b4a0ed1d8f12e251`

## Outcome

L-105107 solved the minimum selector norm by a finite Pick matrix but left
its geometric content implicit.  L-105108 makes that content explicit.
With the positive convention \(g=-\log\rho\), every forced target value has
magnitude

\[
|y_c|=|\gamma_c|r_\Omega(c)^{d_c-1}
e^{\sum_{a\ne c}n_ag_\Omega(c,a)}.
\]

The multipoint interaction is exactly

\[
\tau=\|G^{-1/2}D_yG^{1/2}\|_2,
\]

where \(G\) is the normalized Szegő Gram matrix.  Consequently

\[
\max|y_c|\le\tau\le\max|y_c|\sqrt{\kappa_2(G)}.
\]

Finite Blaschke cardinals yield a second, purely potential upper envelope
whose other-event exponents are all the full orders \(d_a\).  The inverse
Gram diagonal is exactly the reciprocal square of target product separation.
Exact pair thresholds, a diagonal-dominance criterion, domain monotonicity,
and conformal-map-free Euclidean collision bounds complete the finite
ledger.

## New obstructions

Three tempting shortcuts fail exactly.

1. At nodes \(\pm1/2\), values \((2,2)\) and \((-2,2)\) have identical
   geometry and magnitudes but optimal norms two and four.
2. For nodes \((-1/2,0,1/2)\), values \((-1,1,-1)\), every pair problem
   is feasible by \(2+\sqrt3\), while the full problem requires
   \(4+\sqrt{15}\).
3. In the fixed unit disk, for integers \(n\ge2,m\ge1\), a nontarget of
   order \(m\) at \(1/n\) forces norm \(n^m\).  Smooth fixed boundary and
   total order do not replace separation.

The equal-data residue-compatible triple with targets \(\pm1/5\) and a
simple nontarget at zero is especially diagnostic: local Green load five,
Gram factor five, exact norm twenty-five, cardinal envelope twenty-six.

## Prior-art audit

No `L/T/R/M/X-105108` collision exists in main, the fetched refs, or the
shared worktrees.  Main's accepted actual-Xi Pick claims concern a different
kernel and stop at low order.  Draft PR #720 explicitly warns that diagonal
or different-kernel positivity does not prove the required Pick condition.
Historical annular Green material is unintegrated and uses the normalization
\(-2\log|b|\), not the present \(-\log|b|\).  Historical L-91014 is
ID-colliding/unintegrated, and L-92302 remains quarantined without a
growing-order estimate.  None is a dependency.

## Exact authentication

    PASS_T105108_GREEN_GRAM_SELECTOR_CONDITIONING
    15/15 focused tests in normal and optimized Python
    6c2484c4e63612b238f1ec6044c9b8778b725899d4be643d7e80b6a6dc345cdb

The verifier uses standard-library rational arithmetic and exact determinant
polynomials.  It performs no Xi evaluation, conformal numerics, zero scan,
quadrature, broad suite, or heavy campaign.

## Remaining gate

For a cofinal Xi application one must authenticate the full event manifest,
the changing rectangle maps or map-free substitutes, all Green loads and
target products, the complex phases and joint Gram operator, and finally
decay of the unweighted boundary quotient strong enough to absorb the
selector norm.  Multiplicity defect, strict jet coherence, RCMV104530, and
RH remain open.
