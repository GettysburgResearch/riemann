# R-20804 — The fixed-band archimedean Weil form is not a bounded operator

Claim ID: `R-20804`  
Title: Translation inside a fixed Paley–Wiener band makes the logarithmic gamma weight unbounded  
Status: `PROVED SCOPE CORRECTION`  
Authoring agent: `gpt56-03-review`  
Created: 2026-08-01  
Scope: the bounded-operator and Ritz-convergence paragraph of PR #91, `L-3602`

## Statement

Let `PW_Delta` be the real Paley–Wiener space whose Fourier transforms are supported in

\[
[-\Delta/2,\Delta/2].
\]

Put

\[
w(x)=\operatorname{Re}\psi\!\left(\frac14+\frac{ix}{2}\right)-\log\pi.
\]

The quadratic form

\[
\mathfrak a(F)=\int_{\mathbb R}w(x)|F(x)|^2\,dx
\]

is **not** bounded on the `L2` unit sphere of `PW_Delta`.

Consequently the sentence in `L-3602` asserting that the compact archimedean block defines a bounded self-adjoint operator on the complete fixed-support carrier-envelope Hilbert space is false. The finite matrices in `L-3601/L-3602` are unaffected, but the stated bounded-operator proof of continuum Ritz convergence does not follow.

## Proof

Let

\[
b_\Delta(x)=\sqrt\Delta\,\frac{\sin(\pi\Delta x)}{\pi\Delta x}
\]

and define the real translates

\[
F_A(x)=b_\Delta(x-A).
\]

Every `F_A` belongs to the same fixed-band Paley–Wiener space and

\[
\|F_A\|_2=1.
\]

The standard digamma asymptotic on the vertical line gives

\[
w(x)=\log|x|+O(1)
\qquad(|x|\to\infty).
\]

The continuous function `w` is bounded below on the real axis. Fix `R>0` so that

\[
\int_{-R}^{R}|b_\Delta(u)|^2du>\frac12.
\]

For `A>2R`, write `x=A+u`. Uniformly for `|u|<=R`,

\[
w(A+u)\ge\log A-C_R.
\]

Using the global lower bound for `w` outside this interval gives

\[
\begin{aligned}
\mathfrak a(F_A)
&=\int_{\mathbb R}w(A+u)|b_\Delta(u)|^2du\\
&\ge\frac12(\log A-C_R)-C,
\end{aligned}
\]

which tends to `+infinity`. Hence no constant `C0` can satisfy

\[
|\mathfrak a(F)|\le C_0\|F\|_2^2
\]

throughout `PW_Delta`.

For the even test function used in `L-3602`,

\[
g_F(x)=\frac12(F(x)^2+F(-x)^2),
\]

the density `w` is even, so the archimedean integral is the same translated quadratic value. The obstruction therefore applies to the exact Weil packet, not merely to an auxiliary complex space. QED.

## What remains valid

The following parts of PR #91 are not affected:

1. the finite sinc Gram and product-transform identities of `L-3601`;
2. the finite Legendre–Bessel orthonormalization;
3. the exact overlap kernel and recurrence;
4. every finite prime, pole, and compact archimedean matrix entry;
5. monotonicity of finite Ritz minima under nested compression, whenever the finite matrices are interpreted as form compressions.

## Required repair

A valid global theorem must replace bounded-operator density by a quadratic-form argument:

1. define the semibounded closed archimedean/Weil form and its form domain;
2. prove that the finite Legendre–Bessel union lies in that domain;
3. prove that this union is a **form core**, not merely `L2`-dense;
4. only then invoke the variational convergence of nested form compressions.

No such form-core proof is present at the frozen PR #91 head. This scope correction therefore blocks only the continuum-completeness/Ritz conclusion; it does not reject the finite witness formulas.
