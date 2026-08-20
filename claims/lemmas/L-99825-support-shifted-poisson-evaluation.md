# L-99825 — Support-shifted Poisson evaluation removes the absolute-scale cost

Claim ID: `L-99825`  
Status: **PROVED EXACT HARDY/POISSON THEOREM**  
Created: 2026-08-20  
Depends on: `L-99822`, `L-99824`  
RH status: **not assumed**

Let `(c_n)` be a finite complex packet supported on

\[
N\le n\le RN,
\qquad N\ge1,\ R\ge1,
\]

and fix `tau>0`. Put

\[
E(z)=\sum_nc_n n^{\tau-z}.
\]

The usual right-half-plane Poisson inequality applied to `E` gives a point
cost of order `N^{-2\tau}` only after the support origin is used. Define

\[
F(z)=N^zE(z)
    =\sum_nc_n n^\tau\exp[-z\log(n/N)].
\tag{L-99825.1}
\]

Every frequency `log(n/N)` is nonnegative, so `F` is bounded on the closed
right half-plane. On the boundary `|N^{i\gamma}|=1`, while

\[
F(\tau)=N^\tau\sum_nc_n.
\]

Therefore, with

\[
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)}
\]

and

\[
Q_\tau=\int_{\mathbb R}
 \left|\sum_nc_n n^{\tau-i\gamma}\right|^2
 P_\tau(\gamma)\,d\gamma,
\]

Poisson point evaluation gives

\[
\boxed{
\left|\sum_nc_n\right|^2
\le N^{-2\tau}Q_\tau.
}
\tag{L-99825.2}
\]

This is strictly sharper than dropping the factor `N^{-2tau}`.

## 1. Shifted Hardy identity

Using `L-99822` and anchoring the Brownian covariance at `N` gives

\[
\boxed{
N^{-2\tau}Q_\tau
=
\left|\sum_nc_n\right|^2
+
2\tau\int_N^\infty
 \left|\sum_{n\ge v}c_n\right|^2
 \left(\frac vN\right)^{2\tau}\frac{dv}{v}.
}
\tag{L-99825.3}
\]

If `N=n_1<...<n_J` is the ordered support and
`S_j=\sum_{\ell\ge j}c_{n_\ell}`, then equivalently

\[
\boxed{
N^{-2\tau}Q_\tau
=
|S_1|^2+
\sum_{j=2}^J
\left[
 \left(\frac{n_j}{N}\right)^{2\tau}
-\left(\frac{n_{j-1}}{N}\right)^{2\tau}
\right]|S_j|^2.
}
\tag{L-99825.4}
\]

## 2. Application to the fixed compact box

For the packet `d_X(n)` of `L-99824`, either the packet is empty or its least
support point `N_X` satisfies

\[
N_X\ge X/536,
\qquad
n/N_X\le536.
\tag{L-99825.5}
\]

At fixed `tau=1`, the normalized diagonal obeys

\[
\begin{aligned}
N_X^{-2}\sum_n|d_X(n)|^2n^2
&\le536^2\sum_n|d_X(n)|^2\\
&=O(1)
\end{aligned}
\tag{L-99825.6}
\]

by `L-99824`. Thus neither point evaluation nor the coefficient diagonal has a
power-sized dependence on `X`.

The exact remaining theorem is the source-specific suffix estimate

\[
\boxed{
\int_1^X N_t^{-1}Q_t^{1/2}\frac{dt}{t}=X^{o(1)}.
}
\tag{L-99825.7}
\]

By (L-99825.3), its integrand is exactly

\[
\left[
 \left|\sum_nd_t(n)\right|^2
 +\frac{2}{N_t^2}\int_{N_t}^{\infty}
   \left|\sum_{n\ge v}d_t(n)\right|^2v\,dv
\right]^{1/2}.
\]

In the usual blockwise/subpower sense, (L-99825.7) gives subpower logarithmic
negative mass for `G`, hence RH.

The theorem removes the artificial absolute-scale loss. It does not claim the
nested arithmetic suffix sums are already controlled.
