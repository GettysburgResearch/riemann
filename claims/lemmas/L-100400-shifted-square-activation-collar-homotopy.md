# L-100400 — Exact shifted-square activation-collar homotopy

Claim ID: `L-100400`  
Status: **PROVED EXACT IDENTITY**  
Created: 2026-08-20  
RH status: **not assumed**

Put

\[
\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67),
\qquad
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1}.
\]

For `-1<=c<=0`, define

\[
S_c(y)=(4\sqrt y-3+c)\mathbf 1_{y\ge1},
\qquad
\lambda_c={(3-c)^2\over9},
\]

\[
Q_c(Y)=\sum_{n\le Y}{\beta(n)\over\sqrt n}S_c(Y/n)^2,
\qquad
H_2(X)=\sum_{n\le X}{\beta(n)\over\sqrt n}T(X/n)^2.
\]

## 1. Scaling identity

Whenever `lambda_c y>=1`,

\[
\boxed{
{1\over\lambda_c}S_c(\lambda_c y)^2=(4\sqrt y-3)^2.
}
\tag{L-100400.1}
\]

Indeed, `sqrt(lambda_c)=(3-c)/3`, so

\[
S_c(\lambda_c y)
=(3-c)\left({4\over3}\sqrt y-1\right).
\]

Split the sum for `Q_c(lambda_c X)` at `n=X`.  Formula (L-100400.1)
gives

\[
\boxed{
{1\over\lambda_c}Q_c(\lambda_c X)
=H_2(X)+P_c(X),
}
\tag{L-100400.2}
\]

where the complete pre-activation collar is

\[
\boxed{
P_c(X)=
\sum_{X<n\le\lambda_cX}
{\beta(n)\over\sqrt n}
\left(4\sqrt{X/n}-3\right)^2.
}
\tag{L-100400.3}
\]

No term is absorbed into an error estimate.

## 2. Distributional derivative

Write

\[
G_c(u)=e^{-u}Q_c(e^u),
\qquad
L_c(X)=\sum_{n\le X}{\beta(n)\over\sqrt n}S_c(X/n).
\]

At `u=log n`, the term indexed by `n` activates with jump

\[
(1+c)^2\beta(n)n^{-3/2}.
\]

On every open activation cell, direct differentiation gives

\[
{d\over du}
\left[e^{-u}{\beta(n)\over\sqrt n}S_c(e^u/n)^2\right]
=(3-c)e^{-u}{\beta(n)\over\sqrt n}S_c(e^u/n).
\]

Hence, as measures,

\[
\boxed{
dG_c(u)
=(1+c)^2\sum_{n\ge1}{\beta(n)\over n^{3/2}}
\delta_{\log n}(du)
+(3-c)e^{-u}L_c(e^u)\,du.
}
\tag{L-100400.4}
\]

## 3. Exact future formula

Let

\[
C_2=16\sum_{n\ge1}{\beta(n)\over n^{3/2}}
=16{1-67^{-3/2}\over\zeta(3/2)},
\qquad
\mathcal E_2(X)=C_2X-H_2(X).
\]

Since `G_c(u)->C_2`, integrate (L-100400.4) from
`log(lambda_c X)` to infinity and use (L-100400.2).  One obtains

\[
\boxed{
\begin{aligned}
\mathcal E_2(X)={}&
X(1+c)^2\sum_{n>\lambda_cX}{\beta(n)\over n^{3/2}}\\
&+(3-c)X\int_{\lambda_cX}^{\infty}L_c(t){dt\over t^2}
+P_c(X).
\end{aligned}
}
\tag{L-100400.5}
\]

This identity is exact for every `X>=1` and every `-1<=c<=0`.
