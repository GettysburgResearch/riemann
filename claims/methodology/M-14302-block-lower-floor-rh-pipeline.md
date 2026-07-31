# M-14302 — Proof pipeline for a cofinal block lower floor

Claim ID: `M-14302`  
Title: Replace prolate-ground convergence by a finite low-block, complement-coercivity, and squared-residual program  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Dependencies: `L-14308`, `L-14309`, `T-14302`; CCM localized Weil operator and prolate target  
Scope: positive RH research program  
Related counterexample candidates: none

## Objective

For an unbounded support schedule `lambda_j→infinity`, produce exact lower floors

\[
 \mu_{\lambda_j}\ge F_j,
 \qquad
 \liminf_j F_j\ge0.
\]

By `T-14302`, this proves RH.  The workflow never needs to identify or follow a
single ground eigenvector.

## Stage 1 — capture the complete near-radical packet

Do not begin with only the first prolate target.  At each support, form a finite
space

\[
 S_\lambda
 =\operatorname{span}\{P_\lambda E(h_{m,\lambda}):
      m\le m(\lambda)\},
\]

containing every prolate mode whose concentration defect is below a declared
threshold.  Numerical CCM data show several tiny localized Weil eigenvalues;
leaving one of them in the complement destroys any useful scalar Temple gap.

The packet must preserve:

- exact parity decomposition;
- exact source normalization and the two codimension conditions on `h`;
- the complete finite-prime manifest for the chosen support;
- a rational Gram matrix and an exact basis transformation.

The size `m(lambda)` should be chosen from a proved prolate eigenvalue threshold,
not a visually selected list.

## Stage 2 — compute the low block and cross map

With `P` the orthogonal projector onto `S_lambda`, define

\[
 B=P A_\lambda P,
 \qquad
 R=(I-P)A_\lambda P.
\]

Two independent representations should be retained:

1. direct contraction of the localized Weil matrix;
2. the radical-tail identity of `L-14309`, transporting the cross functional to
   `(I-P_lambda)E(h)` outside the support.

The two enclosures must overlap.  The second representation is expected to be
better conditioned because the ideal global `E`-vector is in the radical.

## Stage 3 — certify the entire complement

Split the complement into

\[
 S_\lambda^\perp=E_{\rm mid}\oplus E_{\rm hi}.
\]

### Finite middle block

Choose a deterministic Fourier or finite-element cutoff and certify the finite
middle block by exact rational or ball `LDL*`.  Include every low or ambiguous
mode in `S_lambda`; the middle block should have a clear positive moat.

### Infinite high-frequency block

Prove a symbolic lower bound of the form

\[
 C_{\rm hi}\succeq
 \gamma_\lambda I+h_\lambda M_\lambda.
\]

The most direct candidate is:

- extract the logarithmically growing archimedean symbol;
- bound the finite prime-power kernel in operator norm;
- charge finite-rank pole terms exactly;
- choose a Sobolev/Fourier weight `M_lambda` that makes the remainder coercive.

This is the load-bearing distinction between a lower certificate and ordinary
Ritz data.  The high-frequency argument must cover every omitted mode.

## Stage 4 — exact Schur correction

Compute

\[
 K_\lambda
 =B_\lambda-h_\lambda^{-1}
 R_\lambda^*M_\lambda^{-1}R_\lambda.
\]

Certify a rational `f_lambda` with

\[
 K_\lambda\succeq f_\lambda I.
\]

The ambient lower floor is

\[
 F_\lambda
 =\min\{\gamma_\lambda,f_\lambda\}
  -\delta_\lambda,
\]

where `delta_lambda` is the complete directed operator/form assembly radius.
`X-14304` checks the finite rational Schur packet.

## Stage 5 — prove one symbolic vanishing envelope

Finite levels are reconnaissance.  The proof requires an explicit function

\[
 \varepsilon(\lambda)\downarrow0
\]

and an analytic theorem showing

\[
 F_\lambda\ge-\varepsilon(\lambda)
\]

for every sufficiently large member of an unbounded schedule.

The prolate evidence suggests the following division of labor:

\[
 \|t_\lambda\|_X
 \le D_\lambda(1-\chi(\lambda))^{1/2},
\]

\[
 \|R_\lambda\|_{M^{-1}}
 \le C_\lambda\|t_\lambda\|_X,
\]

\[
 \frac{C_\lambda^2D_\lambda^2
 (1-\chi(\lambda))}{h_\lambda}
 \longrightarrow0.
\]

Because the prolate concentration defect is superexponentially small, polynomial
or ordinary exponential losses in `C_lambda`, `D_lambda`, and `1/h_lambda` may
still be admissible.  Every growth rate must be proved.

## Immediate finite experiments

These experiments do not prove RH, but they identify which analytic inequality
is worth proving.

1. **Scalar versus packet floor.**  Recompute the CCM supports with one, two,
   four, and all detected prolate low modes in `S_lambda`.  Record how the
   complement moat changes.
2. **Residual/gap scaling.**  Measure separately
   `||R||`, `h`, `||R||/h`, and `||R||^2/h`.  A constant linear ratio but vanishing
   squared ratio is precisely the regime opened by `L-14308`.
3. **Direct versus tail residual.**  Evaluate `R` from the full localized matrix
   and from `L-14309`; discrepancy is a normalization or tail-domain bug.
4. **High-mode coercivity.**  On increasing Fourier cutoffs, compare the exact
   complement minimum with the proposed archimedean-minus-prime lower symbol.
5. **FEM lower-bound repair.**  Apply the same block/Schur calculation to the
   newest Suzuki finite-element matrices.  Positive FEM eigenvalues are upper
   bounds; the new target is a full complement lower floor.
6. **Support onset cells.**  Use `L-14201` to sample immediately after each
   prime-power threshold, where the localized matrix changes most sharply.

## Recommended parallel work packets

### P-14302-A — radical-tail continuity

Prove a weighted Sobolev bound

\[
 |QW(f,g)|\le C_\lambda\|f\|_{X_\lambda}
 \|g\|_{M_\lambda}
\]

for an `X_lambda` norm controlled by prolate leakage.

### P-14302-B — high-frequency complement

Derive a rigorous lower symbol for the archimedean operator and a complete
operator-norm bound for all prime and pole perturbations.

### P-14302-C — multi-prolate block

Build the exact low packet, preserve the full block rather than diagonalizing it
numerically, and export `B`, `R`, and Gram data as rationals/balls.

### P-14302-D — independent Suzuki adapter

Translate the P1 finite-element operator into the same lower-floor schema and
identify the missing nonconforming/high-mode residual estimator.

### P-14302-E — asymptotic closure

Once A–D expose observed growth rates, prove one explicit cofinal envelope.
Do not fit a superexponential curve and call it a theorem.

## Stop conditions

- Stop scalar eigenvector fitting if `||R||/h` stabilizes but `||R||^2/h`
  decays; switch to the energy-floor theorem.
- Stop increasing finite dimension when the omitted-complement lower bound is
  absent.
- Stop optimizing one low vector if another tiny mode remains outside the packet.
- Stop a numerical branch immediately if its claimed lower bound is only a Ritz
  upper bound.
- Promote RH only after a symbolic cofinal envelope and independent analytic
  review, never from a long finite run.

## Current proof boundary

The finite block theorem and exact checker are available.  The unresolved
mathematics is concentrated in two statements:

1. a Weil-form continuity estimate strong enough to convert prolate tail decay
   into a squared residual bound;
2. a complete high-frequency complement coercivity theorem.

Those are genuinely weaker and more operator-local than convergence of a chosen
ground eigenvector to `k_lambda`.
