# L-0340 — Li unit-circle geometry

Claim ID: L-0340  
Title: The Li zero transform detects the critical line as the unit circle  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0301  
Scope: geometric kernel for Li-coefficient searches  
Related counterexample candidates: negative Li coefficients

## Statement

For a nontrivial zero `rho=beta+i gamma` of `zeta`, define
\[
 z_\rho=1-\frac1\rho=\frac{\rho-1}{\rho}.
\]
Then
\[
 |z_\rho|^2-1
 =\frac{1-2\beta}{|\rho|^2}.
\]
Consequently,
\[
 |z_\rho|=1
 \quad\Longleftrightarrow\quad
 \operatorname{Re}\rho=\frac12.
\]
If `rho` lies left of the critical line then `|z_rho|>1`; if it lies right,
then `|z_rho|<1`.

If `rho` is on the critical line, the conjugate pair contribution to the
formal Li summand is
\[
 \left[1-z_\rho^n\right]
 +\left[1-\overline{z_\rho}^{\,n}\right]
 =2\left(1-\operatorname{Re}(z_\rho^n)\right)\ge0.
\]

## Proof

Since `z_rho=(rho-1)/rho`,
\[
 |z_\rho|^2
 =\frac{|\rho-1|^2}{|\rho|^2}.
\]
Writing `rho=beta+i gamma`,
\[
 |\rho-1|^2-|\rho|^2
 =(\beta-1)^2+\gamma^2-(\beta^2+\gamma^2)
 =1-2\beta.
\]
Division by `|rho|^2` gives the identity and all three modulus conclusions.

If `beta=1/2`, then `|z_rho|=1`.  The conjugate zero has transformed value
`\overline{z_rho}`.  Therefore the pair contribution equals
\[
 2-z_\rho^n-\overline{z_\rho^n}
 =2(1-\operatorname{Re}z_\rho^n).
\]
For a unit-modulus complex number, its real part is at most one, so the
quantity is nonnegative.  ∎

## Motivation

The Möbius transform in Li's criterion maps the critical line to the unit
circle.  A zero on the left produces a modulus greater than one and hence an
exponentially large oscillatory term at suitable indices.  This explains why
Li coefficients are sensitive to off-line zeros.

## Analytic domain audit

The transform is defined because a nontrivial zero is not `0`.  No logarithm
or contour is used.

## Dependency audit

Only elementary complex arithmetic and conjugation symmetry are used.

## Gap audit

This lemma **does not** prove Li's criterion or justify termwise reasoning in
the full zero sum.

- The Li zero sum requires a specified symmetric limiting convention.
- Individual off-line contributions can cancel with reflected/conjugate
  contributions at some indices.
- A finite truncation can have the wrong sign without a rigorous tail.
- Nonnegativity of each on-line conjugate pair does not by itself justify an
  infinite conditionally convergent sum.

## Adversarial tests

- Substitute `rho=1/2+i gamma` and check unit modulus exactly.
- Substitute reflected zeros `rho` and `1-rho`.
- Plot pair contributions only as heuristic; verify small `n` against the
  derivative definition of `lambda_n`.

## Remaining uncertainty

None in the algebraic identity.  The difficult work in Issue #14 is stable,
rigorous evaluation of the complete coefficient.

## Suggested next attack

Derive a tail bound or arithmetic recurrence independent of a zero list, then
cross-check it against the derivative definition in T-0303.
