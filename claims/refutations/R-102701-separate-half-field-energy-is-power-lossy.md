# R-102701 — Separate half-field energies are power-lossy before carrier recombination

Claim ID: `R-102701`  
Status: **PROVED UNCONDITIONAL NO-GO THEOREM**  
Created: 2026-08-22  
Depends on: PR #719 `L-102700--L-102701`; the quantitative PNT  
RH status: **not assumed**

Let `A` and `A_-` be the ratio-four kernels in `L-102701`.  Put

\[
c_A=2\log2\,(1-2^{-1/2})>0.
\]

Their Mellin multipliers satisfy

\[
\widehat A(1/2)=c_A,
\]

\[
\widehat {A_-}(1/2)=0,
\qquad
\widehat {A_-}'(1/2)=c_A.
\]

For a fixed compact kernel `K`, partial summation against the prime number
theorem gives

\[
\sum_p\frac1{\sqrt p}K(X/p)
=
\sqrt X
\left[
\frac{\widehat K(1/2)}{\log X}
-
\frac{\widehat K'(1/2)}{\log^2X}
+O_K(\log^{-3}X)
\right].
\]

For every ordinary prime,

\[
\lambda_-(p)=\lambda_+(p)=-\frac12.
\]

The extra labelled `67` changes only a finite term.  Hence the singleton-prime
parts of the two fields satisfy

\[
\boxed{
F_+^{[1]}(X)
=-\frac{c_A}{2}\frac{\sqrt X}{\log X}
+O(\sqrt X/\log^2X),
}
\tag{R-102701.1}
\]

and

\[
\boxed{
F_-^{[1]}(X)
=+\frac{c_A}{2}\frac{\sqrt X}{\log^2X}
+O(\sqrt X/\log^3X).
}
\tag{R-102701.2}
\]

Consequently, on every large dyadic block,

\[
\int_X^{2X}|F_+^{[1]}(Y)|^2\frac{dY}{Y}
\asymp \frac{X}{\log^2X},
\]

\[
\int_X^{2X}|F_-^{[1]}(Y)|^2\frac{dY}{Y}
\asymp \frac{X}{\log^4X}.
\]

Thus a Cauchy estimate which takes the two half-fields in absolute value before
all deterministic chaos carriers are recombined is power-sized.  Root-freeness
of `F_-` removes the unit coordinate; it does not remove its prime carrier.

The exact factorization

\[
H_{\rm def}=2F_-*_MF_+
\]

must therefore be used as a polarized current.  Neither separate field energy
is a valid substitute for the conclusion-facing signed scalar.

This no-go is consistent with `L-102706--L-102708`: their polylogarithmic
statements concern labelled source energy, same-product collapse and the
subcritical gauge transfer—not the physical `L2` norm of either half-field.