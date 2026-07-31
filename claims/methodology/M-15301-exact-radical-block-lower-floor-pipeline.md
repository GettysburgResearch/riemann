# M-15301 — Zero-evaluation-split lower-floor pipeline

Claim ID: `M-15301`  
Title: Split the complete low packet into a radical-like near-kernel and a directly certified visible block  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: `T-14302`, `L-14308`, `L-14311`--`L-14313`, `L-15301`, `L-15303`, `L-15304`

## Updated objective

The newest base stack already closes the fixed Gaussian radical-tail numerator,
the complete finite-packet complement denominator, and their cofinal ratio. The
remaining positive barrier is the growing finite low block.

A first version of this methodology proposed approximating the whole complete
low-symbol packet by exact radical truncations. `L-15304` proves that this can
be impossible: exact radicals vanish at every zeta zero, whereas a generic
packet direction is evaluation-visible.

The corrected pipeline approximates only the certified zero-evaluation
near-kernel.

## Finite block decomposition

At support level `lambda`, let `U_lambda` be the complete low packet selected by
the multiband symbol theorem. Choose proof-grade centered zeta zeros

\[
 Z_\lambda=\{z_1,\ldots,z_m\}
\]

and form the evaluation map

\[
 \mathcal V_\lambda u=
 (\widehat u(z_1),\ldots,\widehat u(z_m)).     \tag{1}
\]

In one declared Hardy/form metric, split

\[
 U_\lambda=R_\lambda\oplus V_\lambda,        \tag{2}
\]

where:

- `R_lambda` is a directed rational near-kernel of (1);
- `V_lambda` is a rational complement with a certified positive generalized
  singular-value floor.

Only `R_lambda` is submitted to exact radical repair. `V_lambda` remains in the
finite Schur block and must be directly lower-bounded.

## Radical-like block

Construct exact source-domain radical targets for `R_lambda` using either:

1. the explicit Gaussian/Hermite family in the base stack;
2. the general compact smooth repair of `L-15301`;
3. the growing self-dual Hermite packets of `L-15303`.

For every frozen basis vector, retain:

```text
source constraints and normalization
tail Hardy/form norm
localized approximation error
low-block form interval
cross residual into V_lambda
cross residual into the ambient complement.
```

`L-15304` is used as a consistency gate: a vector declared radical-like must
indeed have small evaluations at every bound certified zero.

## Evaluation-visible block

For `V_lambda`, certify a direct finite lower bound on the complete form block.
Possible proof objects include:

- exact rational LDL after a directed assembly radius;
- a block Schur factorization against the radical-like block;
- certified critical-line-zero PSD contributions plus a separately bounded
  remainder;
- a symbol-derived matrix lower bound preserving prime cancellation.

The visible block may not be discarded merely because its distance from radical
truncations is positive.

## Ambient complement

Write the final operator in the three-block decomposition

\[
 \mathcal H_\lambda=
 \begin{pmatrix}
 B_R & X^* & Y^*\\
 X   & B_V & Z^*\\
 Y   & Z   & C
 \end{pmatrix}.                              \tag{3}
\]

The base `L-14313` packet theorem supplies a positive complement floor for `C`.
First eliminate `C` with the exact Temple--Schur correction. Then eliminate the
visible block `B_V` if it has a certified positive moat. What remains is a small
radical-like corrected block.

The production floor is the minimum eigenvalue of the completely corrected
finite matrix minus one assembly radius. Every elimination is recomputed with
exact rational or directed arithmetic.

## Cofinal target

The proof goal is a symbolic estimate

\[
 F_\lambda\ge-\varepsilon(\lambda),
 \qquad \varepsilon(\lambda)\to0             \tag{4}
\]

on an unbounded support sequence. `T-14302` then proves RH.

A useful sufficient decomposition is

\[
 \varepsilon_\lambda
 \le E_{R,\lambda}
 +\frac{\|X_\lambda\|^2}{\beta_{V,\lambda}}
 +\frac{\|(Y_\lambda,Z_\lambda)\|^2}{h_\lambda}
 +\delta_{\rm assembly,\lambda},             \tag{5}
\]

where `E_R` is the repaired radical-block error, `beta_V` is the visible-block
lower floor, and `h` is the ambient complement floor. Formula (5) is a
scheduling template; final constants must be derived in the exact packet
metric.

## First production experiment

1. Build the smallest complete multiband packet at a modest support.
2. Evaluate its basis at 8, 16, 32, and 64 certified critical-line zeros.
3. Freeze rational near-kernel bases at several directed singular thresholds.
4. Measure whether the near-kernel dimension stabilizes.
5. Fit repaired Gaussian/Hermite targets only to the near-kernel.
6. Factor the visible block directly.
7. Compose all three blocks through the exact Schur checker.
8. Repeat at several supports before proposing an asymptotic rate.

## Fail-closed rules

1. A floating SVD is reconnaissance only.
2. Packet, tail, and evaluation bounds must use one metric.
3. Every zero evaluation must be source-bound to an actual certified zero.
4. The complete low packet must still contain every direction removed from the
   ambient complement theorem.
5. Small radical tails do not imply the visible block is harmless.
6. Finite positive floors do not replace (4).
7. Duplicate claim IDs or conflicting normalizations stop integration.

## Status boundary

This methodology corrects an overstrong approximation target and may reduce the
truly radical-like block dramatically. It does not provide the direct visible-
block lower bound or the cofinal envelope. RH is not claimed.