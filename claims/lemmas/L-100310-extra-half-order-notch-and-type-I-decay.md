# L-100310 — One extra safe half-order notch closes the complete Type-I channel

Claim ID: `L-100310`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: PRs #674--#675  
RH status: **not assumed**

Let \(K_0\) be the minimal ratio-eight ordinary-Möbius wavelet of PR #674:

\[
\widehat K_0(s)
=(1-\sqrt2\,2^{-s})(1-2^{-s})^2
\frac{s+\frac32}{s^2(s-\frac12)}.
\]

Apply one further boundary-safe half-order notch,

\[
\boxed{K_1=(I-\sqrt2 S_2)K_0.}
\tag{L-100310.1}
\]

Then

\[
\operatorname{supp}K_1\subset[1,16],\qquad
\widehat K_1(s)=(1-\sqrt2\,2^{-s})\widehat K_0(s),
\]

and

\[
\boxed{\widehat K_1(1/2)=0.}
\tag{L-100310.2}
\]

All new zeros lie on \(\Re s=1/2\); no pole associated with an off-line zeta
zero is cancelled.

Define

\[
k(x)=x^{-1/2}K_1(1/x),\qquad \operatorname{supp}k\subset[1/16,1].
\]

Then

\[
\int_{\mathbb R}k(x)\,dx
=\int_1^{16}K_1(y)y^{-3/2}\,dy=0.
\tag{L-100310.3}
\]

The explicit compact formulas imply that \(k'\) has finite distributional
variation. Write \(V_1=\operatorname{Var}(k')\). The composite trapezoid
formula with periodic Bernoulli remainder gives, for every \(Y\ge1\),

\[
\left|\frac1Y\sum_{m\in\mathbb Z}k(m/Y)-\int k\right|
\le\frac{V_1}{12Y^2}.
\]

After the substitution \(x=m/Y\),

\[
\boxed{
\left|\sum_{m\ge1}\frac1{\sqrt m}K_1(Y/m)\right|
\le\frac{V_1}{12}Y^{-3/2}.
}
\tag{L-100310.4}
\]

This is a genuine power-decaying Type-I estimate. The extra notch is essential:
the first half-order zero in \(K_0\) is spent removing the original carrier
pole; the second creates the vanishing continuous main moment.

Finally put

\[
\mathcal W_1(X)=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}K_1(X/n).
\]

Its Mellin transform is \(\widehat K_1(s)/\zeta(s+1/2)\), so subpower
logarithmic negative mass of \(\mathcal W_1\) implies RH.
