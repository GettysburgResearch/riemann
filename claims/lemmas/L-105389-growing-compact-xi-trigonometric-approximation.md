# L-105389 — Real-saddle concentration controls a growing Xi trigonometric window

Claim ID: `L-105389`  
Status: **PROVED QUANTITATIVE REAL-LINE CONSEQUENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105385`, `L-105387`  
RH status: **not assumed**

## 1. Relative concentration rate

Use the scales `omega_r` and normalized functions `G_r` from `L-105387`. The
proof of `L-105385` gives

\[
\mathbb E|U-w_s|=O(\sqrt{w_s/s})
\]

and `omega_r=w_s+O(sqrt(w_s/s))` in the relevant parity tilt. Hence, with

\[
V_r={U\over\omega_r},
\]

one has

\[
\boxed{
\mathbb E|V_r-1|
=O\left({1\over\sqrt{r\omega_r}}\right).
}
\tag{L-105389.1}
\]

The Gaussian real-saddle tails also give, for every fixed `H>0` and fixed
integer `m>=0`,

\[
\boxed{
\mathbb E
\left[
(1+V_r)^m e^{HV_r}|V_r-1|
\right]
=O_{H,m}\left({1\over\sqrt{r\omega_r}}\right).
}
\tag{L-105389.2}
\]

The even normalization uses the exponent-`r` law for the function and the
exponent-`r+2` law for `omega_r`; their saddle locations differ by `O(1/r)`,
which is absorbed in (L-105389.1).

## 2. Growing complex-strip approximation

Let `Y_r>=1` satisfy

\[
\boxed{
{Y_r\over\sqrt{r\omega_r}}\longrightarrow0.
}
\tag{L-105389.3}
\]

Fix `H>0`. For odd derivatives, compare

\[
V_r^{-1}\sin(yV_r)
\quad\text{with}\quad
\sin y,
\]

and for even derivatives compare `cos(yV_r)` with `cos y`. On
`|Im y|<=H`, the mean-value theorem in `V` gives a bound by

\[
C_{H,m}(1+|y|)(1+V_r)^m e^{HV_r}|V_r-1|
\]

for each of the first two `y` derivatives. Using (L-105389.2),

\[
\boxed{
\max_{0\le m\le2}
\sup_{\substack{|\operatorname{Re}y|\le Y_r\\
|\operatorname{Im}y|\le H}}
\left|
G_r^{(m)}(y)-T_p^{(m)}(y)
\right|
=
O_H\left({1+Y_r\over\sqrt{r\omega_r}}\right),
}
\tag{L-105389.4}
\]

where

\[
T_{\rm odd}(y)=\sin y,
\qquad
T_{\rm even}(y)=\cos y.
\]

Thus the trigonometric approximation is uniform on a genuinely growing real
window with any fixed complex height.

## 3. A growing family of real critical cells

Let `J_r` satisfy

\[
J_r=O(Y_r)
\]

and keep the corresponding trigonometric critical centers a fixed distance
from the endpoints of the strip. Put

\[
\varepsilon_r={1+Y_r\over\sqrt{r\omega_r}}.
\tag{L-105389.5}
\]

On circles of one fixed small radius about every sine/cosine critical center,
the limiting derivative has a uniform positive lower bound independent of the
cell index. Rouché's theorem and (L-105389.4) therefore give, simultaneously
for all `j<=J_r`, unique real simple critical points with

\[
\boxed{
\omega_rc_{r,j}=y_j^p+O(\varepsilon_r).
}
\tag{L-105389.6}
\]

The reality follows from conjugation symmetry and uniqueness in each symmetric
critical disk.

The second-derivative approximation gives uniformly

\[
\boxed{
\omega_r^2\rho_{r,j}=-1+O(\varepsilon_r).
}
\tag{L-105389.7}
\]

Hence every one of these `J_r` residues is strictly negative for large `r`.

## 4. Uniform critical-atom approximation

Put

\[
\widehat s_{r,j}={1\over\omega_r^2c_{r,j}^2},
\qquad
W_{r,j}=-{2\rho_{r,j}\over c_{r,j}^2}.
\]

For all cells in the growing prefix,

\[
\boxed{
\widehat s_{r,j}
={1\over(y_j^p)^2}
\left(1+O(\varepsilon_r)\right),
}
\tag{L-105389.8}
\]

\[
\boxed{
W_{r,j}
={2\over(y_j^p)^2}
\left(1+O(\varepsilon_r)\right).
}
\tag{L-105389.9}
\]

For every fixed moment order `n`, summability of
`(y_j^p)^(-2n-2)` gives

\[
\boxed{
\sum_{j\le J_r}
\left|
W_{r,j}\widehat s_{r,j}^{\,n}
-
W_j^p(s_j^p)^n
\right|
=O_n(\varepsilon_r),
}
\tag{L-105389.10}
\]

where `(W_j^p,s_j^p)` are the unit-scale tangent or cotangent atoms.

## 5. Available growth scale

Since `omega_r` is asymptotic to a constant multiple of `log r`, every choice

\[
Y_r=r^\gamma
\qquad(0<\gamma<1/2)
\]

satisfies (L-105389.3). The capacity application will choose a much smaller
`gamma` depending on the matrix order in order to beat the shrinking
trigonometric tail eigenvalue.

## 6. Scope

This theorem still does not reach the moving-saddle scale, where the rescaled
window is of order `r`. It supplies no information about critical points beyond
`J_r`, and no sum over the complete critical tail. The error constants depend
on the fixed complex height and derivative order of the normalized function.
No RH conclusion is claimed.
