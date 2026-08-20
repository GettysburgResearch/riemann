# L-99812 — Native first ownership is contractive in the exact Poisson–Hardy target

Claim ID: `L-99812`  
Status: **PROVED EXACT HILBERT-SPACE COMPOSITION THEOREM**  
Created: 2026-08-20  
Depends on: `L-99810`; native first-owner identity of PR #660  
RH status: **not assumed**

For fixed `tau>0`, let `A_tau` map a finitely supported coefficient sequence
`c` into

\[
 A_\tau c=
 \left(
  \sum_nc_n,
  \sqrt{2\tau}\,t^{\tau-1/2}
  \sum_{n\ge t}c_n
 \right)
 \in\mathbb C\oplus L^2([1,\infty),dt).
\tag{L-99812.1}
\]

By `L-99810`,

\[
 \boxed{\|A_\tau c\|^2=Q_\tau(c).}
\tag{L-99812.2}
\]

Let the coefficient-exact native first-owner identity be

\[
 Ff=s_kf+\sum_{i=1}^k\lambda_i\Delta_i^{\rm fut}f,
\tag{L-99812.3}
\]

where

\[
 s_k\ge0,\qquad \lambda_i\ge0,
 \qquad s_k+\sum_i\lambda_i=1,
\]

and

\[
 \Delta_i^{\rm fut}
 =(I-U_i)\prod_{h>i}(I-r_hU_h).
\]

Apply the linear map `A_tau` to (L-99812.3). Convexity of the squared Hilbert
norm gives

\[
\boxed{
 Q_\tau(Ff)
 \le s_kQ_\tau(f)
 +\sum_{i=1}^k\lambda_i
  Q_\tau(\Delta_i^{\rm fut}f).
}
\tag{L-99812.4}
\]

This is a direct physical-target inequality. It does not push a free labelled
`l^2` vector through an uncontrolled collapse map; the first-owner identity is
observed only after entering the exact Hardy space whose norm is the canonical
Poisson quadratic form.

## Free labelled audit

In the free subset-source space, PR #660 gives

\[
 \|\Delta_i^{\rm fut}f\|^2
 =2\prod_{h>i}(1+r_h^2).
\]

Since `sum lambda_i<=1`,

\[
 s_k\|f\|^2+
 \sum_i\lambda_i\|\Delta_i^{\rm fut}f\|^2
 \le1+2\prod_h(1+r_h^2),
\tag{L-99812.5}
\]

which is polylogarithmic for rough-prime activities `r_h^2=1/p_h`.
Equation (L-99812.5) authenticates the labelled source budget, while
(L-99812.4) identifies the exact additional arithmetic obligation: control the
Hardy norms of the future-completed currents, not an arbitrary collapse norm.

## Scope

The theorem fuses the `GPMOC99800` phase packet with the literal native Euler
source. It removes the generic `sqrt(number of labels)` step, but it does not
prove that the right side of (L-99812.4) is subpower after physical endpoint
observation. That remaining owner-tail packing is stated in `T-99810`.