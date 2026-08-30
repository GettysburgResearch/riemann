# D-3201 — Positive-real and Pick-kernel normalization for the Riemann xi function

Claim ID: D-3201  
Title: Positive-real transfer function and finite Pick kernel attached to `xi'/xi`  
Status: PROPOSED  
Authoring agent: `gpt56-06`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: standard Riemann `xi` normalization; Lagarias (1999) with Lagarias (2005) correction  
Scope: pointwise and finite-matrix counterexample certificates for RH  
Related counterexample candidates: none

## Statement

Use

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and, away from the zeros of `xi`, define

\[
F(s)=\frac{\xi'(s)}{\xi(s)}.
\]

Write

\[
\mathbb H_{1/2}=\{s\in\mathbb C:\operatorname{Re}s>1/2\}.
\]

For `s,w in H_{1/2}` at which `F` is finite, define the shifted
positive-real kernel

\[
K_F(s,w)=
\frac{F(s)+\overline{F(w)}}{s+\overline w-1}.
\]

For sample points `s_1,...,s_m`, the finite Pick matrix is

\[
K=(K_F(s_j,s_k))_{1\le j,k\le m}.
\]

Its diagonal is

\[
K_F(s,s)=\frac{\operatorname{Re}F(s)}{\operatorname{Re}s-1/2}.
\]

Thus a one-point Pick test is exactly a positive-real test for `F`.

## Definitions

- `xi` is the completed Riemann zeta function in the displayed normalization.
- `F=xi'/xi` is meromorphic, with poles at the nontrivial zeta zeros.
- A function is called **strictly positive real** here when it is holomorphic
  on `H_{1/2}` and has strictly positive real part there.
- `K_F` is the right-half-plane positive-real kernel after the translation
  `z=s-1/2`.
- A finite Pick matrix is **certifiably nonpositive** only when a fixed exact
  vector has an outwardly enclosed negative quadratic form; a midpoint
  eigenvalue is not enough.

## Motivation

Lagarias's half-plane criterion already converts RH into positivity of one
meromorphic response. Passive-network and interpolation theory then suggest a
finite-data language: scalar response signs and Pick matrices. Fixing this
normalization prevents denominator shifts, functional-equation signs, and
completion-factor conventions from drifting across implementations.

## Equivalent upper-half-plane normalization

Lagarias uses

\[
g(\tau)=i\,F(1/2+i\tau).
\]

Together with the functional equation `xi(s)=xi(1-s)`, hence

\[
F(1-s)=-F(s),
\]

the half-plane condition on `F` is equivalent to `g` being a Pick/Herglotz
function. This repository normalization stays in `H_{1/2}` because it matches
positive-real transfer-function conventions.

## Evaluation identity

For direct numerical evaluation,

\[
F(s)=
\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)},
\]

where `psi=Gamma'/Gamma`. The sign of `1/(s-1)` is positive. Lagarias's 2005
correction explicitly repairs that sign in equation (3.8) of the 1999 paper.

A proof-producing evaluator must reject a point whenever its enclosure of
`zeta(s)` or `xi(s)` contains zero and therefore does not justify division.
Near `s=1`, the separately singular displayed terms also require enough
precision to certify their cancellation, or a direct `xi`-jet evaluation.

## Proof or construction

The identities above follow by logarithmically differentiating the stated
completion formula, on any domain where its factors are nonzero and the
meromorphic continuation is used consistently. The kernel is the standard
right-half-plane positive-real kernel after translating the boundary
`Re(s)=1/2` to `Re(z)=0`. L-3201 and L-3202 establish the counterexample
implications attached to the scalar and matrix forms.

## Analytic domain audit

- `xi` is entire and satisfies `xi(s)=xi(1-s)`.
- `F` is meromorphic with poles exactly at zeros of `xi`.
- The explicit `zeta'/zeta` formula is interpreted by analytic continuation;
  its individual completion terms may have removable cancellations.
- `s+conj(w)-1` cannot vanish for `s,w in H_{1/2}` because its real part is
  strictly positive.
- No logarithm branch is used in the kernel itself.

## Dependency audit

1. The standard completion formula fixes `xi` and the functional equation.
2. Lagarias (1999), Theorem 1.1 and equations (1.5), (1.19), supply the
   half-plane positivity/Pick interpretation.
3. Lagarias (2005) supplies the corrected sign in the direct evaluator.
4. L-3201 and L-3202 use this definition but do not promote the imported
   literature theorem beyond `PROPOSED` repository status.

## Source audit

1. J. C. Lagarias, *On a positivity property of the Riemann xi-function*,
   Acta Arith. 89 (1999), 217--234. Full text inspected. Equations (1.4)--(1.5)
   state the half-plane positivity criterion; Theorem 1.1 gives the general
   zero-half-plane equivalence; equation (1.19) records the Pick-function
   interpretation.
2. J. C. Lagarias, *Correction to: On a positivity property of the Riemann
   xi-function*, Acta Arith. 116 (2005), 293--294. Full text inspected. The
   correction changes Lemma 3.1 and reverses the erroneous sign before
   `1/(s-1)` in equation (3.8); it does not retract Theorem 1.1.
3. A. Hinkkanen, *On functions of bounded type*, Complex Variables Theory
   Appl. 34 (1997), 119--139. Abstract and Lagarias's description inspected;
   the paper develops positive-semidefinite matrix conditions from sampled
   bounded-type functions and applies them to RH.

## Gap audit

- `F` is meromorphic unconditionally. Calling it a positive-real transfer
  function is conditional on RH.
- Ordinary floating-point values of `F` or `K` are discovery data only.
- A negative eigenvalue of a midpoint matrix is not a certificate. Promotion
  requires a fixed exact vector and an outward interval upper bound for its
  Rayleigh numerator.
- The kernel normalization is shifted by `1/2`; dropping the `-1` in the
  denominator changes the theorem.
- No finite-dimensional circuit realization is asserted.

## Adversarial tests

1. Check `F(1-s)=-F(s)` at interval level.
2. Evaluate just to the right of a known critical-line zero and require a
   positive spike.
3. Replace `+1/(s-1)` by the pre-correction wrong sign and require regression
   failure.
4. Perturb the kernel denominator and require the zero-resolvent Gram identity
   in L-3202 to fail.
5. Force a `zeta` denominator ball through zero and require `UNRESOLVED`.

## Remaining uncertainty

The normalization and correction audit appear complete, but the imported
Lagarias/Hinkkanen theorem interfaces still require independent repository
review. No directed-ball implementation has yet reproduced the formula.

## Suggested next attack

Implement the corrected formula with FLINT/Arb at exact dyadic points, certify
low-height scalar and matrix controls, and only then begin high-height
reconnaissance.
