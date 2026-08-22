# L-105303 — Entire-window Hermite–Pick compression for low-order descent

Claim ID: `L-105303`
Status: **PROVED EXACT AT REGULAR FINITE-WINDOW SCOPE**
Created: 2026-08-23
Depends on: residue theorem; exact reverse–Rolle interval identity
RH status: not assumed

## 1. Regular window and critical trace form

Let `F` be a real entire function,

\[
F(\bar z)=\overline{F(z)},
\]

and let `Omega` be a bounded conjugation-invariant rectangle whose boundary
contains no zero of `F'`. Assume every zero of `F'` in `Omega` is simple and
is not a zero of `F`. Let

\[
M=N_{F'}(\Omega)
\]

be the number of those critical points, counting conjugate points separately.
For `0<=i,j<M`, define

\[
\boxed{
B_{ij}(F;\Omega)
=-\frac1{2\pi i}\int_{\partial\Omega}
 \frac{F(z)}{F'(z)}z^{i+j}\,dz.
}
\tag{L-105303.1}
\]

The residue theorem gives

\[
\boxed{
B_{ij}(F;\Omega)
=-\sum_{\substack{F'(c)=0\\c\in\Omega}}
 \frac{F(c)}{F''(c)}c^{i+j}.
}
\tag{L-105303.2}
\]

The matrix is real and symmetric.

Let `G` and `E` be the numbers of real critical points in `Omega` with
`F(c)/F''(c)<0` and `>0`, and let `C` be the number of nonreal conjugate
critical-point pairs. Then `M=G+E+2C`.

## 2. Exact inertia

Evaluation at the `M` distinct critical points is a real-linear isomorphism

\[
\mathbb R[z]_{<M}
\longrightarrow
\mathbb R^G\times\mathbb R^E\times\mathbb C^C.
\tag{L-105303.3}
\]

Indeed, a polynomial of degree below `M` vanishing at all critical points is
zero, and the real dimensions agree. Under this map the bilinear form of
`B(F;Omega)` becomes

\[
-\sum_{c\in\mathbb R}\rho_c u(c)v(c)
-2\operatorname{Re}
 \sum_{\operatorname{Im}c>0}\rho_c u(c)v(c),
\qquad
\rho_c=\frac{F(c)}{F''(c)}.
\tag{L-105303.4}
\]

Every real critical point contributes its literal sign `-rho_c`; every
nonreal pair contributes one positive and one negative direction. Therefore

\[
\boxed{
\operatorname{inertia}B(F;\Omega)=(G+C,E+C),
\qquad
\operatorname{sig}B(F;\Omega)=G-E.
}
\tag{L-105303.5}
\]

This is a direct entire-function localization. No canonical-product
exhaustion and no separate estimate of the nonreal algebraic-square correction
is required: each nonreal pair is hyperbolic and cancels from the signature.

## 3. Exact interval descent with endpoint ledger

Let the horizontal part of `Omega` contain the regular real interval
`I=(a,b)`, and suppose it contains every real zero of `F'` in that interval.
The exact real reverse–Rolle identity gives endpoint bits
`epsilon_a,epsilon_b in {0,1}` such that

\[
\boxed{
N_{\mathbb R}(F;I)
=1+\operatorname{sig}B(F;\Omega)
 -\epsilon_a-\epsilon_b.
}
\tag{L-105303.6}
\]

The endpoint terms are not averaged or discarded. Complex critical points in
the rectangle make zero net contribution to the signature.

## 4. Source-owned analytic compression

Let `phi_1,...,phi_d` be holomorphic in a neighbourhood of `Omega`, satisfy
`phi_j(\bar z)=\overline{phi_j(z)}`, and be fixed before the critical signs are
observed. Define the compressed matrix

\[
\boxed{
C_{ij}
=-\frac1{2\pi i}\int_{\partial\Omega}
 \frac{F(z)}{F'(z)}\phi_i(z)\phi_j(z)\,dz.
}
\tag{L-105303.7}
\]

It is the restriction of the full critical trace form to the span of the
evaluation vectors of the `phi_j`. Hence

\[
\nu_+(C)\le \nu_+\bigl(B(F;\Omega)\bigr).
\tag{L-105303.8}
\]

For every real symmetric `C`,

\[
(\operatorname{tr}C)_+^2
\le \nu_+(C)\operatorname{tr}(C^2).
\tag{L-105303.9}
\]

Combining (L-105303.5)--(L-105303.9),

\[
\boxed{
N_{\mathbb R}(F;I)
\ge
2\frac{(\operatorname{tr}C)_+^2}{\operatorname{tr}(C^2)}
-M+1-\epsilon_a-\epsilon_b.
}
\tag{L-105303.10}
\]

The integer version replaces the quotient by its ceiling.

This is the conclusion-facing low-order Levinson inequality. It has the same
two-trace shape as a zero-side matrix method, but its matrix is weighted by the
literal critical-value/curvature sign `-F/F''` through the contour `F/F'`.

## 5. Exact two-trace contour representation

Put

\[
\mathcal K_d(z,w)=\sum_{j=1}^d\phi_j(z)\phi_j(w).
\tag{L-105303.11}
\]

The two statistics in (L-105303.10) have the exact contour forms

\[
\boxed{
\operatorname{tr}C
=-\frac1{2\pi i}\int_{\partial\Omega}
 \frac{F(z)}{F'(z)}\mathcal K_d(z,z)\,dz,
}
\tag{L-105303.12}
\]

and

\[
\boxed{
\operatorname{tr}(C^2)
=\frac1{(2\pi i)^2}
 \int_{\partial\Omega}\int_{\partial\Omega}
 \frac{F(z)F(w)}{F'(z)F'(w)}
 \mathcal K_d(z,w)^2\,dz\,dw.
}
\tag{L-105303.13}
\]

No root factorization appears. Entry `(0,0)` with `phi_1=1` is the negative
of the first boundary charge in `L-105102`; the full matrix retains all mixed
critical moments before the sign count is compressed. Equations
(L-105303.12)--(L-105303.13) are the direct interface to a two-trace explicit
formula or mollified safe-line calculation.

## 6. Polynomial and taper preconditioning

If `w` is holomorphic, real-symmetric, and nonzero at every critical point in
`Omega`, replacing `phi_j` by `w phi_j` is an injective congruence on the full
critical algebra and a source-owned preconditioning on a compression. It may
be chosen from a fixed low-dimensional family, but it must not be selected
from the unknown signs.

Arbitrary sign-adaptive interpolation would make the finite problem
tautological and is forbidden. The analytic programme must freeze the test
family from the explicit formula or another source-side construction.

## 7. Xi record threshold

Take `F=Xi`, `I=(T,2T)`, and a regular symmetric rectangle. Let `M(T)` be the
complete `Xi'` zero count in that rectangle. If a fixed source-owned family of
compressions satisfies

\[
\liminf_{T\to\infty}
\frac{(\operatorname{tr}C_T)_+^2}
{M(T)\operatorname{tr}(C_T^2)}
>\frac{1+0.67250}{2}=0.83625,
\tag{L-105303.14}
\]

and the endpoint terms are `o(M(T))`, then (L-105303.10) gives a critical-line
proportion strictly above `0.67250` after the standard adjacent zero-count
comparison.

## 8. Scope

The matrix identity, inertia, compression inequality, and endpoint-aware count
are exact. This theorem does not estimate the Xi contour matrices, prove the
required simplicity/common-zero hypotheses, or beat the record. Those are the
open analytic tasks of `T-105300`.
