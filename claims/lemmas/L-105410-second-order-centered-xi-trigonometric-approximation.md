# L-105410 — Second-moment centering upgrades the real-saddle Xi approximation to second order

Claim ID: `L-105410`  
Status: **PROVED UNCONDITIONALLY FROM THE POSITIVE REAL-SADDLE LAW — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-24  
Depends on: `L-105385`, `L-105387`, `L-105389`  
RH status: **not assumed**

## 1. The load-bearing centering

Let `r` tend to infinity through one parity. Use the positive Mellin-tilted law that represents the normalized derivative itself:

- for odd `r`, use `P_(r+1)`;
- for even `r`, use `P_r`.

Put

\[
\omega_r^2=\mathbb E[U^2],
\qquad
V_r={U\over\omega_r},
\qquad
\mathcal R_r=r\omega_r.
\tag{L-105410.1}
\]

Changing `r` to `r+1` in `mathcal R_r` is immaterial. By construction,

\[
\boxed{\mathbb E[V_r^2]=1.}
\tag{L-105410.2}
\]

The real-saddle curvature theorem gives, for every fixed `A,H>=0`,

\[
\boxed{
\mathbb E\!\left[
(V_r-1)^2(1+V_r)^A e^{HV_r}
\right]
=O_{A,H}(\mathcal R_r^{-1}).
}
\tag{L-105410.3}
\]

Indeed `Var(U)=O(omega_r/r)` and `omega_r` is asymptotic to the real saddle. The exponentially small off-saddle tails pay all fixed positive and negative powers needed below.

The normalization (L-105410.2) also gives the exact cancellation

\[
\boxed{
\mathbb E[V_r-1]
=-{1\over2}\mathbb E[(V_r-1)^2].
}
\tag{L-105410.4}
\]

Thus the linear Taylor error is already second order. This cancellation was not used in the first-order estimate of `L-105389`.

## 2. Second-order trigonometric approximation

Use the parity-normalized functions

\[
G_r^{\rm odd}(y)
=\mathbb E\!\left[{\sin(yV_r)\over V_r}\right],
\qquad
G_r^{\rm even}(y)
=\mathbb E[\cos(yV_r)].
\tag{L-105410.5}
\]

The odd expression is interpreted continuously at `V=0`. Let

\[
T_{\rm odd}(y)=\sin y,
\qquad
T_{\rm even}(y)=\cos y.
\]

Fix `H>0`. Taylor expansion in `V` at one, followed by (L-105410.3) and (L-105410.4), gives, for every `Y>=1` and `m=0,1,2`,

\[
\boxed{
\sup_{\substack{|\Re y|\le Y\\|\Im y|\le H}}
\left|
G_r^{(m)}(y)-T_p^{(m)}(y)
\right|
\ll_{H,m}
{(1+Y)^2\over\mathcal R_r},
}
\tag{L-105410.6}
\]

uniformly whenever `Y=o(sqrt(mathcal R_r))`.

For the odd law, split first into `|V-1|<=1/2` and its complement. On the central event the first two `V` derivatives of every displayed `y` derivative are bounded by `C_H(1+Y)^2(1+V)^A e^(HV)`. The complement is absorbed by the tilted off-saddle estimate. The even case is immediate. This proves (L-105410.6) without a complex moving saddle.

## 3. The source germ has the same second-order rate

For every fixed integer `j>=0`,

\[
\boxed{
\mathbb E[V_r^{2j}]
=1+O_j(\mathcal R_r^{-1}).
}
\tag{L-105410.7}
\]

To see this, expand `x^j` at `x=1` with `x=V_r^2`; its linear expectation vanishes exactly and the quadratic remainder is paid by (L-105410.3).

For odd derivatives, these are precisely the normalized moments entering `L-105380`.

For even derivatives, the regularized source law is the two-power tilt of the function law. Therefore

\[
\mathbb E_{r+2}[V_r^{2j}]
={\mathbb E_r[V_r^{2j+2}]\over\mathbb E_r[V_r^2]}
=\mathbb E_r[V_r^{2j+2}]
=1+O_j(\mathcal R_r^{-1}),
\tag{L-105410.8}
\]

and

\[
\mathbb E_{r+2}[V_r^{-2}]=1.
\tag{L-105410.9}
\]

The exact source recurrences are polynomial/rational in finitely many of these moments. Hence, for every fixed matrix order `k` and `a in {0,1}`,

\[
\boxed{
\left\|
\widehat{\mathsf A}_{k,r}^{(a)}
-\mathsf T_{k,p}^{(a)}
\right\|_{\max}
=O_k(\mathcal R_r^{-1}).
}
\tag{L-105410.10}
\]

Here the hat denotes the positive diagonal scaling by `omega_r`.

## 4. Cellwise critical-atom error

Let `y_j^p` be the sine/cosine critical centers of `L-105382`. Let `J_r=o(sqrt(mathcal R_r))`. Applying (L-105410.6) on one fixed disk about each center gives, simultaneously for every `j<=J_r`,

\[
\boxed{
\omega_r c_{r,j}
=y_j^p+O\!\left({(1+j)^2\over\mathcal R_r}\right),
}
\tag{L-105410.11}
\]

\[
\boxed{
\omega_r^2\rho_{r,j}
=-1+O\!\left({(1+j)^2\over\mathcal R_r}\right).
}
\tag{L-105410.12}
\]

The approximation of the first derivative away from the disjoint critical disks also excludes additional critical points in the complete controlled strip. Conjugation symmetry makes the unique critical point in each symmetric disk real.

Put

\[
\widehat s_{r,j}={1\over\omega_r^2c_{r,j}^2},
\qquad
W_{r,j}=-{2\rho_{r,j}\over c_{r,j}^2},
\]

and let `(s_j^p,W_j^p)` be the unit trigonometric atom. For every fixed `n>=0`,

\[
\boxed{
\left|
W_{r,j}\widehat s_{r,j}^{\,n}
-W_j^p(s_j^p)^n
\right|
\ll_n
{(1+j)^{-2n}\over\mathcal R_r}.
}
\tag{L-105410.13}
\]

Consequently,

\[
\boxed{
\sum_{j\le J_r}
\left|
W_{r,j}\widehat s_{r,j}^{\,n}
-W_j^p(s_j^p)^n
\right|
\ll_n
\begin{cases}
J_r/\mathcal R_r,&n=0,\\
1/\mathcal R_r,&n\ge1.
\end{cases}
}
\tag{L-105410.14}
\]

This is the critical improvement: higher Stieltjes moments do not pay the number of controlled cells.

## 5. Scope

The theorem is entirely real-saddle and source-positive. It does not control critical points outside `o(sqrt(mathcal R_r))`, prove the complete critical tail real, establish any low-order derivative descent, or prove RH. The analytic constants and parity normalizations require independent review.
