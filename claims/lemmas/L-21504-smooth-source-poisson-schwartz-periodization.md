# L-21504 — Smooth two-cancellation sources have Schwartz arithmetic images and exact periodizations

Claim ID: `L-21504`  
Title: Poisson summation closes the fold-convergence half of the smooth source/CCM bridge  
Status: **PROPOSED — COMPLETE POISSON/SCHWARTZ/PERIODIZATION THEOREM; WEIL-FORM DOMAIN AND PRODUCTION NORMALIZATION SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: classical Poisson summation for `C_c^infinity`; the arithmetic map used in `L-16205/L-15631`  
Scope: smooth differential Mellin-cardinal sources of `L-15631/L-19819` and the corrected-tail identity of `L-19820`

## 1. Source class and arithmetic image

Let

\[
 f\in C_c^\infty(\mathbb R)
\]

be even, vanish on a neighborhood of zero, and satisfy

\[
 \int_{\mathbb R}f(x)\,dx=0.
 \tag{L-21504.1}
\]

For `u>0`, define

\[
 \boxed{
 E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu).
 }
 \tag{L-21504.2}
\]

The sum is finite at every fixed `u`.  Use the additive Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(x)e^{-i\xi x}\,dx.
 \tag{L-21504.3}
\]

## 2. Exact Poisson representation

Since `f` is even and `f(0)=0`,

\[
 2\sum_{n\ge1}f(nu)=\sum_{n\in\mathbb Z}f(nu).
 \tag{L-21504.4}
\]

Poisson summation gives

\[
 \sum_{n\in\mathbb Z}f(nu)
 ={1\over u}\sum_{m\in\mathbb Z}
 \widehat f\!\left({2\pi m\over u}\right).
 \tag{L-21504.5}
\]

The zero-frequency term is absent by (L-21504.1).  Therefore

\[
 \boxed{
 E(f)(u)
 ={1\over2\sqrt u}
 \sum_{m\ne0}
 \widehat f\!\left({2\pi m\over u}\right).
 }
 \tag{L-21504.6}
\]

This identity is exact and exposes every arithmetic Poisson alias at once.

## 3. Arbitrary-order decay at the small multiplicative endpoint

Let

\[
 \mathcal D=u\partial_u.
\]

Applying `mathcal D` repeatedly to (L-21504.6) produces a finite linear
combination of terms

\[
 u^{-1/2-j}
 \left({2\pi m\over u}\right)^k
 \widehat f^{(k)}\!\left({2\pi m\over u}\right)
\]

with fixed `j,k` depending only on the derivative order.  Because every
Fourier derivative of `f` is Schwartz, for every pair of integers `r,M>=0`
there is a constant `C_(r,M,f)` such that

\[
 \boxed{
 |\mathcal D^rE(f)(u)|
 \le C_{r,M,f}u^M,
 \qquad 0<u\le1.
 }
 \tag{L-21504.7}
\]

Indeed choose a Schwartz power larger than `M+r+3`; the remaining sum is
bounded by a convergent `sum_(m!=0)|m|^-2` after harmless powers are absorbed.

At the opposite endpoint, if the support of `f` is contained in `[-B,B]`, then

\[
 E(f)(u)=0
 \qquad(u>B).
 \tag{L-21504.8}
\]

Thus the logarithmic arithmetic image

\[
 h_f(t)=E(f)(e^t)
 \tag{L-21504.9}
\]

satisfies

\[
 \boxed{h_f\in\mathcal S(\mathbb R).}
 \tag{L-21504.10}
\]

The same conclusion holds for every finite derivative with respect to an
external source parameter, provided the corresponding source derivatives are
bounded in finitely many `C_c^infinity` seminorms.

## 4. Exact smooth periodization

For a period length `L>0`, define

\[
 \Sigma_Lh(x)=\sum_{m\in\mathbb Z}h(x+mL).
 \tag{L-21504.11}
\]

For `h=h_f`, (L-21504.10) implies absolute and locally uniform convergence of
(L-21504.11), together with every `x` derivative.  Hence

\[
 \boxed{
 \Sigma_Lh_f\in C^\infty(\mathbb R/L\mathbb Z).
 }
 \tag{L-21504.12}
\]

Its exact Fourier coefficients are

\[
 \boxed{
 {1\over L}\int_{-L/2}^{L/2}
 \Sigma_Lh_f(x)e^{-2\pi ikx/L}\,dx
 ={1\over L}\widehat h_f\!\left({2\pi k\over L}\right).
 }
 \tag{L-21504.13}
\]

The interchange of sum, derivatives, and integral is justified by absolute
Schwartz convergence; no formal fold or distributional endpoint convention is
needed.

## 5. Exterior fold and projection tails

Let `P_L` be restriction to the fundamental interval and let

\[
 t=(I-P_L)h_f.
\]

The exterior fold

\[
 (\mathfrak F_Lt)(x)
 =\sum_{m\ne0}t(x+mL),
 \qquad |x|\le L/2,
 \tag{L-21504.14}
\]

converges absolutely in every `C^r` norm and obeys

\[
 \Sigma_Lh_f=P_Lh_f+\mathfrak F_Lt.
 \tag{L-21504.15}
\]

Let `Pi_N` be the ordinary Fourier projection on the circle.  Since
`Sigma_Lh_f` is smooth, for every `r,M` one has

\[
 \boxed{
 \|(I-\Pi_N)\Sigma_Lh_f\|_{C^r}
 \le C_{r,M,L,f}(1+N)^{-M}.
 }
 \tag{L-21504.16}
\]

Consequently all three terms in the corrected tail

\[
 W_{L,N}f
 =(I-P_L)h_f
 -\iota_L\mathfrak F_L(I-P_L)h_f
 +\iota_L(I-\Pi_N)\Sigma_Lh_f
 \tag{L-21504.17}
\]

are genuine functions with convergent `L2`, Sobolev, and distributional
pairings.  The exact identity

\[
 \boxed{
 \iota_L\Pi_N\Sigma_Lh_f=h_f-W_{L,N}f
 }
 \tag{L-21504.18}
\]

holds in `L2` and in distributions, not merely formally.

## 6. Application to the smooth differential cardinal frame

The multiplicative sources in `L-15631/L-19819` are smooth, compactly
supported away from zero after even extension, and satisfy both

\[
 f(0)=0,
 \qquad \int f=0.
\]

Therefore every source column satisfies the theorem.  In particular:

1. its arithmetic image is logarithmically Schwartz;
2. every periodization fold is absolutely `C^infinity` convergent;
3. the discarded Fourier tail is superalgebraically small at fixed source;
4. the algebraic corrected-tail identity of `L-19820` is valid on ordinary
   function spaces without an unproved fold-convergence assumption.

This closes the convergence half of Interface A in the whole-matrix/prolate
source programme.

## 7. Form-level consequence and remaining gate

Suppose the repository's Weil form `Q_W` is continuously defined on a common
space containing the global Schwartz image `h_f`, the finite sharp extension
`iota_L Pi_N Sigma_L h_f`, and the corrected tail (L-21504.17).  If `h_f` is in
the exact radical on that domain, then (L-21504.18) gives

\[
 \boxed{
 Q_W(\iota_L\Pi_N\Sigma_Lh_f,
     \iota_L\Pi_N\Sigma_Lh_g)
 =Q_W(W_{L,N}f,W_{L,N}g).
 }
 \tag{L-21504.19}
\]

The algebra is immediate by expanding `h_f-W_f` and using radicality.

What remains is not convergence of the fold.  It is the exact production
normalization and form-domain theorem asserting that the sharp finite CCM
vectors and the corrected tails inhabit this common domain and that their
matrix agrees with the declared finite CCM/Suzuki matrix.

## 8. Proof boundary

- The Poisson representation, arbitrary-order endpoint decay, Schwartz
  periodization, Fourier coefficients, and projection-tail estimates are
  unconditional classical analysis.
- The theorem applies directly to the smooth differential cardinal sources.
- It does not identify the repository's exact finite CCM normalization or prove
  continuity of the Weil form on sharp zero extensions.
- It does not provide the quantitative complete profile Gram or local-Weyl LMI.
- It is a new proposed bridge and does not by itself prove RH.
