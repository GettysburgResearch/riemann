# L-106135 — Reflection-even reserve and reflection-odd defect are exact complements

Claim ID: `L-106135`  
Programme aliases: `LFAM1.REFLECTION_COMPLEMENTARITY`, `LFAM2.ONE_SIGNATURE_GATE`, `STRESS.EVEN_ODD_ENERGY_IDENTITY`  
Status: **PROVED EXACT HILBERT-SPACE AND DIFFERENTIAL IDENTITY**  
Created: 2026-08-25  
Depends on: corrected `L-106134`; elementary reflection projections  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The reflection-even and reflection-odd energies introduced in the first
`T-106150` draft are not independent source measurements. They are
orthogonal complementary energies of one fixed half-field.

## 1. Complementary projections

For a real logarithmic half-field `f` and a physical coordinate `x`, let

\[
(R_xf)(u)=f(x-u).
\]

Then `R_x` is a self-adjoint unitary involution. Hence

\[
E_x=\frac12(I+R_x),
\qquad
O_x=\frac12(I-R_x)
\]

are orthogonal projections with

\[
E_x+O_x=I,
\qquad
E_xO_x=0.
\]

Therefore

\[
\boxed{
\|E_xf\|_2^2+\|O_xf\|_2^2=\|f\|_2^2,
}
\tag{L-106135.1}
\]

and

\[
\boxed{
\langle f,R_xf\rangle
=\|E_xf\|_2^2-\|O_xf\|_2^2.
}
\tag{L-106135.2}
\]

## 2. The theta-averaged identity

For the ordinary half-source completion of `L-106134`, put

\[
\begin{aligned}
\mathcal E_U(x)
&=\int_0^1(1-\theta)
  \|E_xf_{U,\theta}\|_2^2d\theta,\\
\mathcal O_U(x)
&=\int_0^1(1-\theta)
  \|O_xf_{U,\theta}\|_2^2d\theta,\\
\mathcal N_U
&=\int_0^1(1-\theta)
  \|f_{U,\theta}\|_2^2d\theta.
\end{aligned}
\]

The quantity `mathcal N_U` is independent of `x`. Equations
(L-106135.1)--(L-106135.2) give

\[
\boxed{
\mathcal E_U(x)+\mathcal O_U(x)=\mathcal N_U,
}
\tag{L-106135.3}
\]

and

\[
\boxed{
\mathcal J_U(e^x)
=\mathcal E_U(x)-\mathcal O_U(x)
=2\mathcal E_U(x)-\mathcal N_U
=\mathcal N_U-2\mathcal O_U(x).
}
\tag{L-106135.4}
\]

## 3. Exact differential equivalence

Let

\[
\mathcal D_{\rm out}
=\frac12D(D-1)(5D+3/2)(2D-1).
\]

Because `mathcal D_out` contains the factor `D`, it annihilates the constant
`mathcal N_U`. Thus

\[
\boxed{
\mathcal D_{\rm out}\mathcal J_U
=2\mathcal D_{\rm out}\mathcal E_U
=-2\mathcal D_{\rm out}\mathcal O_U.
}
\tag{L-106135.5}
\]

Consequently, pointwise,

\[
\boxed{
(\mathcal D_{\rm out}\mathcal J_U)_-
=2(\mathcal D_{\rm out}\mathcal E_U)_-
=2(\mathcal D_{\rm out}\mathcal O_U)_+.
}
\tag{L-106135.6}
\]

The first `REFEV106150 AND REFOD106150` conjunction was therefore redundant:
either statement is exactly equivalent to the ordinary self-convolution gate.

## 4. Reflection-mismatch form

Since

\[
O_xf=\frac12(f-R_xf),
\]

\[
\boxed{
\mathcal O_U(x)
=\frac14\int_0^1(1-\theta)
\int_{\mathbb R}
|f_{U,\theta}(u)-f_{U,\theta}(x-u)|^2
\,du\,d\theta.
}
\tag{L-106135.7}
\]

Thus the final ordinary reflection problem is the positive differential
variation of one explicit reflection-mismatch energy.

## Scope

This lemma removes a duplicate implication gate. It does not estimate
`(mathcal D_out mathcal O_U)_+`. The single corrected gate is
`REFSIG106150` in `T-106150`.
