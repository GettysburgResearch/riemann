# T-0309 — de Bruijn--Newman threshold

Claim ID: T-0309  
Title: de Bruijn--Newman real-zero threshold and RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorems of de Bruijn, Newman, Rodgers--Tao  
Scope: imported equivalence and positive-time witness route  
Related counterexample candidates: Issue #18

## Statement

For real `t`, define the entire function
\[
 H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)\,du,
\]
where
\[
 \Phi(u)=\sum_{n=1}^{\infty}
 \left(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\right)
 e^{-\pi n^2e^{4u}}.
\]

There exists a finite real constant `Lambda` such that
\[
 H_t\text{ has only real zeros}
 \quad\Longleftrightarrow\quad
 t\ge\Lambda.
\]
RH is equivalent to `Lambda<=0`.  Rodgers and Tao proved `Lambda>=0`.
Consequently,
\[
 \mathrm{RH}\quad\Longleftrightarrow\quad\Lambda=0.
\]

In particular, L-0360 shows that a certified nonreal zero of `H_t` for one
explicit `t>0` disproves RH.

## Sources

- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17
  (1950), 197--226, DOI 10.1215/S0012-7094-50-01720-0.
- Charles M. Newman, *Fourier transforms with only real zeros*, Proc. Amer.
  Math. Soc. 61 (1976), 245--251.
- Brad Rodgers and Terence Tao, *The de Bruijn--Newman constant is
  non-negative*, Forum Math. Pi 8 (2020), e6,
  DOI 10.1017/fmp.2020.6, arXiv:1801.05914.

Inspection level: Rodgers--Tao's primary abstract/arXiv statement was inspected
and supplies the exact normalization and historical threshold wording.  The
older original proofs were located bibliographically but not reconstructed.

## Motivation

This creates an entire-function zero search distinct from zeta itself.  The
logical certificate is local even though the threshold theorem is global.

## Proof status

Imported theorem; proof not reproduced.  L-0360 proves the finite-witness
contrapositive.

## Analytic/domain audit

- `t` is real and `z` complex.
- The kernel is super-exponentially decaying, but a certificate must still
  prove uniform tails for complex `z`.
- The direction is "only real iff `t>=Lambda`".
- At `t=0`, the zero condition corresponds to RH under the source
  normalization.

## Gap audit

- Different authors rescale `t`, `z`, or `Phi`; a positive-time witness must
  use this exact fingerprint.
- Numerical quadrature over real `u` must control `cos(zu)` for complex `z`.
- A nonreal zero for negative `t` is expected and is not a disproof.
- `Lambda>=0` is a theorem but does not decide RH without `Lambda<=0`.

## Remaining uncertainty

No statement uncertainty in Rodgers--Tao's normalization.  Independent proof
review is pending.

## Suggested next attack

Claim Issue #18 and first prove reusable uniform tail bounds before doing any
large reconnaissance scan.
