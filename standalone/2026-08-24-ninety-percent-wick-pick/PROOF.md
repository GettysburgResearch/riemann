# A confluent full-signature descent and a 91.77% Wick–Pick criterion

## Status

This note proves a new exact finite-window descent theorem and an unconditional
source-owned frozen model whose one-percent Xi transfer would imply that at
least

\[
\frac{1563433}{1703567}=0.917740834\ldots
\]

of zeta zeros lie on the critical line.  The one-percent actual-Xi transfer is
not proved.  Therefore neither the 91.77% conclusion nor the Riemann
Hypothesis is established here.

## 1. Why the previous robust inequality could not reach 90%

The prior positive-index descent was

\[
\frac{N_0}{N}\ge2\eta-1-\frac{821}{5000}.
\]

Since `eta<=1`, its absolute ceiling is `0.8358`.  This is not a numerical
shortcoming of the Wick model; it is a structural loss from replacing full
signature by positive index and then charging every nonreal or confluent
block as a nuisance.

## 2. Reduced quotient and local residue form

Let `F` be real analytic on a regular finite interval `(a,b)` and holomorphic
on a surrounding conjugation-invariant rectangle.  Put

\[
R=F/F'.
\]

At a zero of `F` of multiplicity `mu`, common factors cancel and
`R(z)=(z-c)/mu+O((z-c)^2)`.  The poles of `R` are precisely non-root critical
points.

At a real pole of order `m`, with leading Laurent coefficient `a_m`, the
complete Hermite residue block is congruent to `-a_m J_m`.  Hence its
signature is `-sgn(a_m)` when `m` is odd and zero when `m` is even.  A
nonreal conjugate pair is an invertible hyperbolic block and has zero
signature.  With the convention that `1/(x-c)` has Cauchy index `+1`,

\[
\operatorname{sig}H=-\operatorname{Ind}(F/F').
\]

## 3. Reciprocal Cauchy-index descent

Let `V_x(F,F')` be one when `F(x)` and `F'(x)` have opposite signs and zero
otherwise.  Tracking this sign variation through each zero gives

\[
\operatorname{Ind}(F'/F)+\operatorname{Ind}(F/F')=V_a-V_b.
\]

Every distinct real zero of `F`, of any multiplicity, contributes exactly one
to `Ind(F'/F)`.  Therefore

\[
Z_{\rm dist}(F;(a,b))=\operatorname{sig}H+V_a-V_b.
\]

If `C` is any source-fixed analytic compression of the full residue form, then

\[
\nu_+(H)\ge\nu_+(C)
\ge\frac{(\operatorname{tr}C)_+^2}{\|C\|_{HS}^2}.
\]

Writing `M` for the reduced total pole order and using
`sig H=2 nu_+(H)-M` yields

\[
Z_{\rm dist}
\ge
2\frac{(\operatorname{tr}C)_+^2}{\|C\|_{HS}^2}
-M+V_a-V_b.
\]

For `F=Xi`, `M<=N_1`, the endpoint term is bounded, and `N_1/N->1`.  Thus

\[
\liminf\frac{N_0}{N}\ge2\liminf\eta_T-1,
\qquad
\eta_T=\frac{(\operatorname{tr}C_T)_+^2}
{N_1\|C_T\|_{HS}^2}.
\]

There is no multiplicity, common-zero, or nonreal density subtraction.

## 4. Cancelling two Euler chaoses

Let

\[
x=A_X/L,
\qquad
W_2=\exp(-x/2-x^2/4).
\]

Then

\[
\frac{LW_2^2}{L-A_X}
=
\exp\left(\sum_{j\ge3}\frac{x^j}{j}\right)
=
\sum_{m\ge0}d_mx^m.
\]

The coefficients satisfy

\[
d_0=1,
\quad d_1=d_2=0,
\quad md_m=\sum_{j=3}^m d_{m-j},
\quad 0\le d_m\le1.
\]

The normalized arithmetic coefficients are

\[
a_{2,L}(n)=
\sum_{m=3}^{\Omega(n)}d_mL^{-m}\Lambda^{*m}(n).
\]

The prime-simplex calculation gives

\[
\lim_{L\to\infty}
\sum_{n\le e^L}\frac{a_{2,L}(n)^2}{n}
=
\sum_{m\ge3}d_m^2\frac{m!}{(2m)!}.
\]

Using the first three exact terms and a geometric factorial tail,

\[
\sum_{m\ge3}d_m^2\frac{m!}{(2m)!}
\le
\frac1{1080}+\frac1{26880}+\frac1{756000}
+\frac{13}{8316000}
=
\frac{9181}{9504000}
<\frac1{1000}.
\]

The Hermitian two-sided symbol therefore has mean square below `501/500` and
normalized effective rank above `500/501`.

## 5. The 91.77% conditional theorem

If the actual Xi matrix has at least 99% of the frozen model trace and at most
101% of its Hilbert--Schmidt norm, then

\[
\eta_T
\ge
\frac{500}{501}\left(\frac{99}{101}\right)^2
=
\frac{1633500}{1703567}.
\]

The full-signature descent gives

\[
\liminf\frac{N_0}{N}
\ge
2\frac{1633500}{1703567}-1
=
\frac{1563433}{1703567}
=0.917740834\ldots.
\]

The exact margin above `0.9` is

\[
\frac{302227}{17035670}.
\]

## 6. Remaining analytic theorem

The open conjunction `W2XFER105500` must pass the degree-two Wick factor
through the complete one-copy and two-copy safe-line Gram formula and show
that horizontal, pole, archimedean-freezing, taper, canonical-product,
omitted-prime, and endpoint errors retain the 99/101 comparison.  The
`A_X^2` term makes its boundary price stronger than for the first-chaos
factor, so the earlier `K=1` transfer cannot be cited unchanged.
