# L-105360 — Nested-window anchor moments transport by explicit residue atoms

Claim ID: `L-105360`  
Status: **PROVED EXACT ENTIRE-FUNCTION TRANSPORT THEOREM**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105217`, `L-105350`  
RH status: **not assumed**

## 1. Setup

Let `F` be entire and real on the real axis. Let

\[
\Omega_{\rm in}\Subset\Omega_{\rm out}
\]

be bounded conjugation-symmetric Jordan domains, both regular for `F'`. Fix a
real anchor

\[
x_*\in\Omega_{\rm in}\cap\mathbb R.
\]

Assume that every zero of `F'` in the closed annulus
`\Omega_{\rm out}\setminus\Omega_{\rm in}` is simple and does not equal
`x_*`. Write

\[
\rho_c={F(c)\over F''(c)}
\]

and let `H_in,H_out` be the boundary Cauchy functions of `F/F'` associated with
the two windows.

By `L-105217`, for `z\in\Omega_in`,

\[
\boxed{
H_{\rm in}(z)
=H_{\rm out}(z)
+
\sum_{\substack{F'(c)=0\\
c\in\Omega_{\rm out}\setminus\Omega_{\rm in}}}
{\rho_c\over z-c}.
}
\tag{L-105360.1}
\]

## 2. Exact one-anchor moment transport

Define the Hamburger anchor moments

\[
m_n^{\rm in}
={H_{\rm in}^{(n+1)}(x_*)\over(n+1)!},
\qquad
m_n^{\rm out}
={H_{\rm out}^{(n+1)}(x_*)\over(n+1)!}.
\tag{L-105360.2}
\]

For each annular critical point put

\[
\boxed{
t_c={1\over c-x_*},
\qquad
w_c={-\rho_c\over(c-x_*)^2}.
}
\tag{L-105360.3}
\]

Differentiating one pole gives

\[
{1\over(n+1)!}
\left({d\over dz}\right)^{n+1}
{\rho_c\over z-c}\Bigg|_{z=x_*}
={-\rho_c\over(c-x_*)^{n+2}}
=w_ct_c^n.
\]

Therefore

\[
\boxed{
m_n^{\rm in}
=m_n^{\rm out}
+
\sum_c w_ct_c^n,
\qquad n\ge0.
}
\tag{L-105360.4}
\]

This is an exact finite atomic update, not an asymptotic expansion.

## 3. Exact Hankel rank-one update

For `k\ge1`, let

\[
\mathsf L_k^{\rm in}
=[m_{r+s}^{\rm in}]_{r,s=0}^{k-1},
\qquad
\mathsf L_k^{\rm out}
=[m_{r+s}^{\rm out}]_{r,s=0}^{k-1}
\]

and

\[
v_k(t)=(1,t,\ldots,t^{k-1})^T.
\]

Equation (L-105360.4) is equivalent to

\[
\boxed{
\mathsf L_k^{\rm in}
=
\mathsf L_k^{\rm out}
+
\sum_c w_c\,v_k(t_c)v_k(t_c)^T.
}
\tag{L-105360.5}
\]

If every annular critical point is real and

\[
\rho_c\le0,
\tag{L-105360.6}
\]

then `t_c` is real and `w_c\ge0`. Hence

\[
\boxed{
\mathsf L_k^{\rm in}\succeq\mathsf L_k^{\rm out}
\qquad(k\ge1).
}
\tag{L-105360.7}
\]

The same statement follows directly at separated nodes because

\[
{\rho_c/(x-c)-\rho_c/(y-c)\over x-y}
={-\rho_c\over(x-c)(y-c)}
\]

is a positive rank-one Loewner kernel when `\rho_c\le0`.

## 4. Positive-measure transport

Suppose `H_out` has the one-anchor representation

\[
H_{\rm out}(z)
=H_{\rm out}(x_*)+(z-x_*)
\int_{\mathbb R}{d\mu_{\rm out}(t)\over1-t(z-x_*)}
\]

with `\mu_out\ge0`. Under (L-105360.6), define

\[
\boxed{
\mu_{\rm in}
=
\mu_{\rm out}+\sum_cw_c\delta_{t_c}.
}
\tag{L-105360.8}
\]

Then `\mu_in\ge0`, and it represents the nonconstant part of `H_in`; the
constant difference is fixed by evaluating at `x_*`. Thus all-packet Loewner
positivity descends from the outer window to the inner window.

## 5. Approximate terminal reserve is enough

Let

\[
\Omega_1\Subset\Omega_2\Subset\cdots
\]

be a nested regular exhaustion, and assume every critical point crossed by the
exhaustion is real with nonpositive residue. Fix an inner index `N` and an
order `k`. Iterating (L-105360.5) gives, for every `M>N`,

\[
\mathsf L_k(\Omega_N)
=
\mathsf L_k(\Omega_M)+\mathsf P_{k;N,M},
\qquad
\mathsf P_{k;N,M}\succeq0.
\tag{L-105360.9}
\]

Consequently,

\[
\lambda_{\min}\bigl(\mathsf L_k(\Omega_N)\bigr)
\ge
\lambda_{\min}\bigl(\mathsf L_k(\Omega_M)\bigr).
\tag{L-105360.10}
\]

Therefore it is enough that along one cofinal sequence `M_j\to\infty`, for
every fixed `k`,

\[
\boxed{
\liminf_{j\to\infty}
\lambda_{\min}
\bigl(\mathsf L_k(\Omega_{M_j})\bigr)
\ge0.
}
\tag{L-105360.11}
\]

Then every finite-order inner anchor matrix is exactly positive semidefinite.
Equivalently, one may require only

\[
\|\mathsf L_k(\Omega_{M_j})_-\|\longrightarrow0
\tag{L-105360.12}
\]

for each fixed `k`. No estimate uniform in `k` is needed for this logical
transport: each finite order is frozen before the terminal limit is taken.

## 6. Meaning

The boundary hierarchy has a monotone direction once the sharp residue sign is
known:

```text
outer boundary moment matrix
        + positive annular residue atoms
        = inner boundary moment matrix.
```

Thus the all-window boundary gate can be replaced by one cofinal terminal
asymptotic reserve together with the pointwise annular residue gate.

## 7. Scope

The theorem does not prove that annular critical points are real, does not prove
`rho_c<=0`, and does not produce the terminal estimate (L-105360.11). Nonreal
critical conjugate pairs give real rank-two updates with no automatic sign.
Positive residues give negative atomic weights. The theorem is an exact
transport mechanism, not an RH proof.
