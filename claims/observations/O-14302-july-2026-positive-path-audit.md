# O-14302 — July 2026 audit of the positive RH frontier

Claim ID: `O-14302`  
Title: The strongest current positive routes all lack a lower spectral floor, not another finite upper approximation  
Status: `RESEARCH NOTE — PROPOSED INTERPRETATION`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Scope: repository-wide and literature-wide strategy audit  
Related counterexample candidates: none

## Sources reviewed

Primary sources and identifiers:

- Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755,
  especially Corollary 3.8 and Section 8.
- Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the
  Spectral Action*, arXiv:2511.23257 / CMP 406 (2026), 312.
- Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096.
- Kim–Hong–Kim–Choi–Jang–Shin–Kim, *A Numerical Realization of Suzuki's
  Weil-Quadratic-Form Operator*, arXiv:2607.24830v2, 29 July 2026.
- Michałowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors
  of the Riemann xi coefficients*, arXiv:2607.16795.
- Connes–Consani, *Spectral triples and zeta-cycles*, Enseign. Math. 69 (2023).
- Current repository PRs #140, #141, #144, and #150, plus the finite direct-xi,
  screw, Pick, and moment-cone closures.

## What the literature now establishes

### 1. Localized Weil ground values are the shortest positive criterion

CCM define the localized lower spectral value `mu_lambda`, prove it is
nonincreasing with support, and state that `lim mu_lambda=0` implies RH.  Their
Section 8 instead pursues a stronger program: prove the ground is simple-even
and converges to an explicit prolate target so that its Fourier transform tends
to `Xi`.

The simple-even theorem of Connes–van Suijlekom is exact and powerful, but it is
a theorem about zeros **after** a simple isolated extremal eigenfunction is
available.  It does not provide the missing lower bound for the Weil operator.

### 2. The newest Suzuki computation is upper-bound evidence

arXiv:2607.24830 numerically realizes Suzuki's nonlocal operator, observes a
strictly positive, superexponentially decaying lowest FEM value in the tested
range, and explicitly states that it does not prove RH.  A conforming finite
element eigenvalue is naturally a Rayleigh–Ritz upper bound for the ambient
lowest eigenvalue.  Positivity of that number cannot exclude a smaller negative
ambient direction without an independent residual/complement estimator.

The paper's operator-residual criterion is useful evidence for the same missing
object: a rigorous lower floor or a complete residual-growth bound.

### 3. Suzuki's real-rooted characteristic functions still need convergence

arXiv:2606.09096 constructs finite-interval self-adjoint operators and associated
real-rooted characteristic functions unconditionally.  The RH implication
requires a locally uniform limiting statement.  This is structurally parallel
to the CCM determinant route: every finite approximant has the right zero
geometry, but convergence to the arithmetic target is the global theorem.

### 4. The Toeplitz-minor wedge closes a tail, not the critical cone

arXiv:2607.16795 proves

\[
 D_{r,k}>0\qquad(k\ge10^{18}r^3),
\]

with proof-grade Arb and exact-rational certificates.  The author explicitly
identifies the complementary region, especially bounded `k/r`, as RH-critical.
The result is an important global positivity region but does not combine with
finite zero verification to cover all orders.

### 5. The repository has closed many finite cones correctly

The repository now contains proof-grade positive closures for:

- the full recovered `4.1`-billion-prime-power carrier vector;
- several complete fixed direct-xi polynomial and Loewner cones;
- a full degree-14 half-line polynomial response cone at the PR103 table;
- complex Pick boxes that had appeared negative at inadequate precision;
- extensive selected-factor and support-gap finite screens.

These results eliminate numerical ghosts and sharpen candidate design.  None is
cofinal in support or degree, so none alone proves RH.

## New synthesis

The common missing statement is not “find another positive finite eigenvalue.”
It is:

\[
 \boxed{
 \text{produce an ambient lower spectral envelope whose negative part tends to zero}.}
\]

`L-14308` and `T-14302` show that this can be strictly easier than the currently
advertised ground-state convergence programs.

A finite packet of all prolate near-radical modes may rotate internally or have
multiplicity.  Only its corrected Schur floor matters.  The residual enters
quadratically, so the scaling

\[
 \|R\|\asymp h\asymp\varepsilon
\]

is fatal for eigenvector convergence but successful for a lower floor.

The 2023 near-radical construction adds a second key point: the ideal global
`E(h)` vector is in the Weil radical.  `L-14309` proves that every residual of its
support truncation is exactly the residual of the discarded tail.  This gives a
concrete route for importing the superexponential prolate concentration defect.

## Highest-value conjectural estimates

The following are **not proved** and are recorded for parallel attack:

1. **Graph-norm leakage transfer.**  For the CCM target,
   \[
   \|(I-P_\lambda)E(h_\lambda)\|_{X_\lambda}
   \le \operatorname{poly}(\lambda)
   (1-\chi(\lambda))^{1/2}
   \]
   in a norm `X_lambda` on which the Weil form is continuous.
2. **Packet complement coercivity.**  After placing every prolate mode with
   concentration eigenvalue above a fixed threshold into `S_lambda`, the
   remaining localized Weil complement admits a lower bound whose negative part
   is polynomially controlled.
3. **Archimedean high-mode domination.**  Beyond an explicit Fourier index, the
   logarithmic archimedean symbol dominates the complete finite-prime and pole
   perturbation in operator norm.
4. **Squared residual closure.**  The ratio
   \[
   \|R_\lambda\|_{M^{-1}}^2/h_\lambda
   \]
   decays even when `||R_lambda||/h_lambda` does not.
5. **Suzuki lower-bound adapter.**  A Lehmann–Goerisch, complement-Schur, or
   nonconforming-residual estimate can convert the positive P1 FEM data into a
   genuine ambient floor.

Each statement must be proved with exact normalization and domain control before
entering an RH chain.

## Candidate computations worth running

1. Reprocess the CCM numerical tables and plot both `R/h` and `R^2/h` for the
   full low prolate packet.
2. Apply `X-14304` to the finite Fourier matrices while increasing the packet
   dimension until the complement moat stabilizes.
3. Reuse the exact prime manifests from the counterexample program to bound the
   high-frequency prime perturbation, rather than re-enumerating it.
4. Run a lower-bound estimator on the new Suzuki P1 matrices and report the
   difference between Ritz upper values and certified lower floors.
5. Search immediately right of prime-power support thresholds, where `L-14201`
   shows the localized ground path is most susceptible.
6. Preserve failures: if complement coercivity collapses because of another
   prolate mode, add that mode to the packet and record the rank transition.

## Verdict

No complete RH proof has been obtained in this audit.

The concrete advance is a reduction of the positive frontier from two strong
spectral-convergence assertions to one weaker cofinal inequality:

\[
 \liminf_{j\to\infty}
 \left[
 \min\{\gamma_j,
 \lambda_{\min}(B_j-h_j^{-1}R_j^*M_j^{-1}R_j)\}
 -\delta_j
 \right]\ge0.
\]

Proving this inequality is enough for RH even if no individual ground vector
converges to the prolate target.
