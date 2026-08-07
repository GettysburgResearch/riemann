# Agent report — exact target-pinned completion audit

Agent: `gpt56-04-f`  
Issue: #151, parallel continuation  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Date: 2026-07-31

## Objective switch

The user requested a positive RH attack. I audited the newest positive branches
and primary literature rather than extending counterexample searches.

The strongest repo route uses exact Hermite global-radical targets, finite
special matrices, and Hurwitz. Its finite target-pinning theorem had a
transparent graph-weight sufficient condition, but not a complete finite
decision procedure.

## Main results

### L-15107 — complete scalar-pencil criterion

For a prescribed finite target `p`, the diagonal completion is the exact pencil

\[
 T_p(c)=A_p+cB_p.
\]

The slope has an explicit inertia determined only by the signs of `eta_i p_i`.
When it is indefinite, strict Finsler gives

\[
 \exists c:T_p(c)\succeq0,\ \ker T_p(c)=Rp
\]

if and only if

\[
 x^TA_px>0
\]

for every nonzero `x perp p` satisfying

\[
 x^TB_px=0.
\]

This removes graph weights, finite natural-ground assumptions, eigengaps, and
floating eigenvector tracking from the finite gate.

### T-15104 — cofinal RH criterion

If the exact Hermite target transforms converge locally uniformly to `Xi` and
the Finsler completion passes cofinally, the finite special-matrix theorem makes
every approximant real-rooted and Hurwitz proves RH.

This is a conditional theorem, not a completed proof.

### L-15108 — arbitrary-completion boundary

An arbitrary positive special completion exists exactly when the target
rank-one quotient is real-diagonalizable. Hence allowing every special metric is
essentially a reformulation of the finite real-zero problem, not a shortcut.

The one-scalar Weil completion remains meaningful because it is a much smaller
structured family whose Finsler condition might be attacked arithmetically.

### R-15101 — graph separator is incomplete

A four-dimensional integer Gram matrix has a strict target-pinned completion
with exact complement LDL pivots

```text
26, 6075/104, 48
```

even though its graph interval is empty:

```text
c >= 66
c <= 15.
```

No previous graph-positive certificate is invalidated. The correction is that
graph failure cannot retire a target level.

## Exact software

`X-15103` adds a standard-library checker for:

1. strict rational completions;
2. rational isotropic-cone obstructions;
3. rational conflicting-threshold obstructions.

Ten adversarial tests pass. No floating-point operation appears in the checker.

## Literature synthesis

The latest sources agree on the frontier:

- Connes--van Suijlekom solve the finite special-matrix to real-zero transfer;
- Connes--Consani--Moscovici identify rigorous convergence as the missing
  spectral-triple step;
- Suzuki supplies an unconditional localized Weil/screw operator but leaves the
  limiting spectral realization conjectural;
- Groskin makes finite Weil values exact and controls the Archimedean tail;
- the July numerical Suzuki realization is positive evidence, explicitly not an
  arithmetic proof;
- Freedman's Weyl/Volterra stack still leaves the final de Branges pullback
  outside its certificate.

The common blocker is a cofinal structural positivity/convergence theorem, not
more finite precision.

## Candidate computations proposed

1. Exact small-level Hermite `Q,p` exports.
2. Numerical scalar-pencil search followed by exact rational LDL.
3. Direct Sturm certification of the target interpolation polynomial.
4. Rational Finsler obstruction extraction on failed levels.
5. Comparison of the scalar completion metric with the boundary-resolvent metric.
6. Analytic use of the exact radical leakage identity to prove positivity on the
   `B_p`-isotropic cone.

## Counterexample and proof status

No RH proof is claimed. No counterexample candidate is involved.

The exact remaining positive statement is now:

\[
 x^TA_{p_j}x>0
 \quad
 (x\perp p_j,\ x\ne0,\ x^TB_{p_j}x=0)
\]

cofinally, together with locally-uniform convergence of the finite target
transforms to `Xi`.

That is a sharper global blocker than the earlier graph or finite-eigenvalue
conditions.
