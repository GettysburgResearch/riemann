# L-99715 — Annulus-centered Poisson averaging has fixed gap and an exact tail-Carleson factorization

Claim ID: `L-99715`  
Status: **PROVED EXACT HARMONIC / FINITE-SUM THEOREM**  
Created: 2026-08-20  
Depends on: `L-99710`, `L-99713/L-99714`  
RH status: **not assumed**

Let a finite packet have the form

\[
F(0)=\sum_n b_n
\]

with source support

\[
N_0\le n\le RN_0,
\qquad R\ge1.
\]

Define the annulus-centered Dirichlet polynomial

\[
F_{N_0}(w)
=
\sum_n b_n\left({n\over N_0}\right)^{-w}.
\tag{L-99715.1}
\]

Since every ratio `n/N_0>=1`, this polynomial is bounded in the half-plane
`Re w>=0`.  For `tau>0`, apply the Poisson majorant from the boundary line
`Re w=-tau` to obtain

\[
|F(0)|^2
\le
\int_{\mathbb R}P_\tau(\gamma)
 |F_{N_0}(-\tau+i\gamma)|^2d\gamma.
\tag{L-99715.2}
\]

The left-boundary coefficient inflation is now only

\[
\left({n\over N_0}\right)^\tau\le R^\tau,
\tag{L-99715.3}
\]

not `x^tau`.

## 1. Exact factorization

Put `r_n=n/N_0`.  The Cauchy characteristic function gives

\[
\begin{aligned}
\mathcal P_\tau(F)
&:=
\int_{\mathbb R}P_\tau(\gamma)
 |F_{N_0}(-\tau+i\gamma)|^2d\gamma\\
&=
\sum_{m,n}b_m\overline{b_n}
 r_m^\tau r_n^\tau
 e^{-\tau|\log r_m-\log r_n|}\\
&=
\sum_{m,n}b_m\overline{b_n}
 \min(r_m,r_n)^{2\tau}.
\end{aligned}
\tag{L-99715.4}
\]

Using

\[
\min(r_m,r_n)^{2\tau}
=2\tau\int_0^{\min(r_m,r_n)}y^{2\tau-1}dy,
\]

finite Fubini gives

\[
\boxed{
\mathcal P_\tau(F)
=2\tau\int_0^R y^{2\tau-1}
 \left|\sum_{r_n\ge y}b_n\right|^2dy.
}
\tag{L-99715.5}
\]

Since every `r_n>=1`, the tail sum is `F(0)` on `0<y<=1`.  Therefore

\[
\boxed{
\mathcal P_\tau(F)
=|F(0)|^2
+2\tau\int_1^R y^{2\tau-1}
 \left|\sum_{r_n\ge y}b_n\right|^2dy.
}
\tag{L-99715.6}
\]

The Poisson square is exactly the physical scalar square plus a positive
multiplicative tail-Carleson energy.  No inequality or infinite-series
continuation enters this decomposition.

## 2. Fixed-width owner gap

For the compact base packet of `L-99713`, take `N_0=x/8`, `R=8`.  For the
growing-moment block packet of `L-99714`, take

\[
N_0=x/2^{M_L+3},
\qquad R=2^{M_L+3}=x^{o(1)}.
\]

Thus one may choose the fixed width

\[
\boxed{\tau=1.}
\tag{L-99715.7}
\]

The strip inflation is at most `R=x^(o(1))`, while `L-99710` gives the uniform
coefficient gap

\[
\boxed{
\overline V_1(n)\ge|a(n)|^2.
}
\tag{L-99715.8}
\]

This strictly improves the uncentered adaptive choice: after compactification
there is no need to send the phase width to zero.

## 3. Remaining arithmetic object

For

\[
b_n={\beta(n)\over\sqrt n}\Phi_{M_L}(x/n),
\]

the sole extra term in (L-99715.6) is

\[
\boxed{
\mathcal C_{x,L}
=2\int_1^{2^{M_L+3}}y
 \left|
 \sum_{n\ge yx/2^{M_L+3}}
 {\beta(n)\over\sqrt n}\Phi_{M_L}(x/n)
 \right|^2dy.
}
\tag{L-99715.9]
\]

(with the closing bracket in the displayed label understood as `)` in plain
text renderers).  This is a finite, source-faithful multiplicative tail square.
The logarithmic-owner Gram now has a unit spectral gap and the coefficient
diagonal is already subpower.  Only the off-diagonal packing of these nested
tails remains.

## 4. Scope

```text
endpoint centering                       exact;
fixed Poisson width                      admissible;
strip inflation                          subpower;
owner spectral gap                       uniform;
Poisson phase integral                   exact tail square;
physical scalar                          first positive term;
remaining tail packing                   explicit / open.
```

The theorem does not estimate `mathcal C_(x,L)`; it removes the analytic phase
integral and identifies the exact one-dimensional source tent that must be
controlled.