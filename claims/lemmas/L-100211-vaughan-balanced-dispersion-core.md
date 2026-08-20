# L-100211 — Exact Vaughan decomposition leaves one balanced near-hyperbola dispersion term

Claim ID: `L-100211`  
Status: **PROVED EXACT DECOMPOSITION; BALANCED DISPERSION OPEN**  
Created: 2026-08-20  
Depends on: `L-100210`  
RH status: **not assumed**

Fix an integer \(U\ge1\). Put

\[
\mu_U(n)=\mu(n)\mathbf1_{n\le U},
\qquad
a_U=\varepsilon-\mu_U*\mathbf1.
\tag{L-100211.1}
\]

At the Dirichlet-series level, if \(M_U\) is the series of \(\mu_U\), then
\(A_U=1-\zeta M_U\). The identity

\[
2M_U-\zeta M_U^2+\frac{A_U^2}{\zeta}
=
\frac1\zeta
\]

gives the exact coefficient formula

\[
\boxed{
\mu
=
2\mu_U-\mu_U*\mu_U*\mathbf1+a_U*a_U*\mu.
}
\tag{L-100211.2}
\]

Moreover

\[
a_U(n)=0\qquad(1\le n\le U).
\tag{L-100211.3}
\]

Apply (L-100211.2) to the scalar \(\mathcal W_1(X)\) of `L-100210`. If
\(U<X/16\), the first term vanishes because \(K_1\) is supported on
\([1,16]\). Hence

\[
\boxed{
\mathcal W_1(X)=\mathcal T_U(X)+\mathcal B_U(X),
}
\tag{L-100211.4}
\]

where

\[
\mathcal T_U(X)
=
-\sum_{a,b\le U}
\frac{\mu(a)\mu(b)}{\sqrt{ab}}
\sum_{m\ge1}\frac1{\sqrt m}
K_1\!\left(\frac{X}{abm}\right)
\tag{L-100211.5}
\]

and

\[
\boxed{
\mathcal B_U(X)
=
\sum_{\substack{r,s>U\\m\ge1}}
\frac{a_U(r)a_U(s)\mu(m)}{\sqrt{rsm}}
K_1\!\left(\frac{X}{rsm}\right).
}
\tag{L-100211.6}
\]

By `L-100210.8`,

\[
|\mathcal T_U(X)|
\le
\frac{V_1}{12}X^{-3/2}
\left(\sum_{a\le U}a\right)^2.
\tag{L-100211.7}
\]

Choose \(U=\lfloor X^{1/3}\rfloor\). Then

\[
\boxed{\mathcal T_U(X)=O_{K_1}(X^{-1/6}).}
\tag{L-100211.8}
\]

This error has finite logarithmic integral at infinity.

The support of \(K_1\) gives the exact localization

\[
\frac X{16}\le rsm\le X,
\qquad
r,s>U,
\qquad
m\le\frac X{U^2}\ll X^{1/3}.
\tag{L-100211.9}
\]

Thus all Type-I ranges have been removed. The conclusion-facing arithmetic
problem is one balanced, compact-product, near-hyperbola trilinear form.

Define `BVD100210` by

\[
\boxed{
\int_2^Y
\bigl(\mathcal B_{\lfloor X^{1/3}\rfloor}(X)\bigr)_-
\frac{dX}{X}
=
Y^{o(1)}.
}
\tag{BVD100210}
\]

Equations (L-100211.4) and (L-100211.8) imply

\[
\boxed{\mathrm{BVD100210}\Longrightarrow RH.}
\tag{L-100211.10}
\]

`BVD100210` remains open. Unlike `MWOC99910`, it is an explicit arithmetic
decomposition: the linear and unbalanced ranges are already proved harmless,
and only the signed balanced core remains.
