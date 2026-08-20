# L-100311 — Exact Vaughan decomposition leaves one compact balanced trilinear

Claim ID: `L-100311`  
Status: **PROVED EXACT DECOMPOSITION; ONE ARITHMETIC FORM OPEN**  
Created: 2026-08-20  
Depends on: `L-100310`  
RH status: **not assumed**

Fix \(U\ge1\) and put

\[
\mu_U(n)=\mu(n)\mathbf1_{n\le U},\qquad
a_U=\varepsilon-\mu_U*\mathbf1.
\]

At the Dirichlet-series level \(A_U=1-\zeta M_U\). Hence

\[
2M_U-\zeta M_U^2+\frac{A_U^2}{\zeta}=\frac1\zeta,
\]

and coefficient comparison gives the exact identity

\[
\boxed{\mu=2\mu_U-\mu_U*\mu_U*\mathbf1+a_U*a_U*\mu.}
\tag{L-100311.1}
\]

Moreover,

\[
a_U(n)=0\qquad(1\le n\le U).
\tag{L-100311.2}
\]

Apply (L-100311.1) to \(\mathcal W_1(X)\). If \(U<X/16\), the
\(2\mu_U\) term is absent by compact support, and

\[
\boxed{\mathcal W_1(X)=\mathcal T_U(X)+\mathcal B_U(X),}
\tag{L-100311.3}
\]

where

\[
\mathcal T_U(X)
=-\sum_{a,b\le U}\frac{\mu(a)\mu(b)}{\sqrt{ab}}
\sum_{m\ge1}\frac1{\sqrt m}K_1\!\left(\frac{X}{abm}\right),
\tag{L-100311.4}
\]

and

\[
\boxed{
\mathcal B_U(X)
=\sum_{\substack{r,s>U\\m\ge1}}
\frac{a_U(r)a_U(s)\mu(m)}{\sqrt{rsm}}
K_1\!\left(\frac{X}{rsm}\right).
}
\tag{L-100311.5}
\]

Using `L-100310` at \(Y=X/(ab)\),

\[
|\mathcal T_U(X)|
\le\frac{V_1}{12}X^{-3/2}\left(\sum_{a\le U}a\right)^2.
\]

With \(U=\lfloor X^{1/3}\rfloor\),

\[
\boxed{\mathcal T_U(X)=O_{K_1}(X^{-1/6}).}
\tag{L-100311.6}
\]

This error has finite logarithmic integral.

The compact support gives the exact remaining ranges

\[
\frac X{16}\le rsm\le X,\qquad r,s>U,\qquad
m\le\frac X{U^2}\ll X^{1/3}.
\tag{L-100311.7}
\]

Thus every linear and classical Type-I contribution has been paid. The only
remaining term is the signed compact near-hyperbola form
\(\mathcal B_{\lfloor X^{1/3}\rfloor}(X)\), with two truncated-divisor
coefficients and one literal Möbius coefficient.
