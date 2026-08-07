# Positive RH frontier — source audit through 2026-07-31

Agent: `gpt56-04-f`  
Scope: primary-source audit for the positive spectral/Weil program  
Status: literature synthesis; no theorem promotion by citation alone

## Sources inspected

1. Alain Connes and Walter D. van Suijlekom,
   *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*,
   arXiv:2511.23257.
2. Alain Connes, Caterina Consani, and Henri Moscovici,
   *Zeta Spectral Triples*, arXiv:2511.22755.
3. Masatoshi Suzuki,
   *Weil's quadratic form via the screw function*, arXiv:2606.09096.
4. Akiva Groskin,
   *A finite Guinand--Weil dictionary and archimedean tail order for the
   truncated Weil quadratic form*, arXiv:2607.02828.
5. Taebong Kim et al.,
   *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator*,
   arXiv:2607.24830.
6. Marvin B. Freedman,
   *Finite-core Volterra reductions for a Weyl-positive Riemann phase kernel*,
   arXiv:2606.29555.
7. Paul Finsler,
   *Über das Vorkommen definiter und semidefiniter Formen in Scharen
   quadratischer Formen* (classical strict quadratic-pencil theorem).
8. L. L. Dines,
   classical convexity theorem for the joint range of two homogeneous quadratic
   forms.

## What is genuinely available

### 1. Finite real-zero transfer

Connes--van Suijlekom prove that a real symmetric positive matrix of the special
divided-difference form, with one-dimensional even kernel, forces the associated
interpolation polynomial and finite Fourier transform to have only real zeros.
They also prove a continuous analogue for a simple isolated extremal
eigenfunction.

This is the correct finite real-zero engine used by `T-15103` and `T-15104`.

### 2. Exact finite arithmetic dictionary

The July 2026 Guinand--Weil dictionary identifies every finite Galerkin quadratic
value with an exact band-limited zero sum and gives a one-sided totally-positive
archimedean tail order. It makes finite signs meaningful; it does not turn
cofinally many unproved signs into a theorem.

### 3. Operator formulations of Weil positivity

Suzuki gives an unconditional screw-function realization and a localized
self-adjoint operator framework. The proposed limit operator with zeta-zero
spectrum remains conjectural.

The July numerical realization finds the expected Archimedean law and positive
finite lowest eigenvalues, but explicitly separates those observations from an
arithmetic proof of RH.

### 4. Spectral-triple convergence program

Connes--Consani--Moscovici obtain finite selfadjoint rank-one perturbations whose
spectra approximate low zeta zeros with remarkable accuracy. Their paper
explicitly identifies rigorous convergence of the operators or regularized
determinants to the zeta object as the missing implication.

### 5. Weyl/KLM--de Branges program

Freedman develops a positive Weyl-kernel and Volterra/Schur certificate stack.
The manuscript explicitly leaves the quotient-to-original Weyl lift,
uniform-parameter coverage, and final de Branges/RH bridge outside the completed
certificate.

## Repo synthesis

The current positive repo work has solved or sharply formalized four finite
interfaces:

1. exact finite Weil matrices and explicit-formula normalization;
2. finite real-zero transfer from positive special matrices;
3. exact Hermite global-radical targets and local-uniform target approximation;
4. proof-producing finite rational/directed certificates.

The remaining obstruction is not another finite precision problem. It is a
**cofinal structural positivity theorem**.

The target-pinned diagonal completion of `T-15103` is one possible bridge. Before
this audit it had only an edgewise nonnegative-weight sufficient test.
`L-15107` now gives its complete finite decision:

\[
 A_p+cB_p\succ0\text{ on }p^\perp
 \iff
 A_p>0\text{ on the }B_p\text{-isotropic cone}
\]

when the slope is indefinite.

Thus the positive program can be stated without hidden eigengap assumptions:

> Prove the Finsler isotropic-cone inequality cofinally for the exact
> Hermite-radical targets, and prove their locally-uniform convergence to `Xi`.

The first statement yields finite real-rooted approximants through the
Connes--van Suijlekom theorem; the second lets Hurwitz conclude RH.

## Important non-shortcuts

1. Huge finite positivity tables do not imply cofinal positivity.
2. A graph-separator failure does not refute the scalar completion; `R-15101`
   gives an exact counterexample.
3. Allowing an arbitrary positive special completion is not a free proof:
   `L-15108` shows it is equivalent to real-diagonalizability of the target
   rank-one quotient, hence essentially to the finite real-zero property itself.
4. Numerical agreement of finite spectra with zeta zeros does not supply the
   required operator/determinant convergence.
5. The Weyl/KLM certificate does not yet identify the de Branges evaluation
   kernel required for RH.

## Highest-value experiments

1. Export exact small-level Hermite targets and run:
   - direct Sturm real-root certification;
   - exact `L-15107` scalar-pencil certification;
   - arbitrary special-metric construction when the first succeeds but the
     second fails.
2. Track the Finsler feasible interval versus localization level and band.
3. Search for a closed analytic representation of the isotropic-cone form using
   the exact radical leakage identity `L-15102`.
4. Compare the target-pinned quotient metric with the boundary-resolvent metric
   of `L-15105`.
5. Treat the Freedman Hardy/Volterra pullback as a separate bridge theorem; do
   not combine two incomplete implications into one claimed proof.

## Verdict

The latest literature and repository work identify a coherent proof program but
do not presently prove RH. The strongest new reduction in this branch is the
exact cofinal Finsler criterion `T-15104`. It converts the finite positive step
from a heuristic graph search into a necessary-and-sufficient scalar-pencil
problem, with exact positive and negative certificates.
