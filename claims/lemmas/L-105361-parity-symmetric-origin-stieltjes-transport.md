# L-105361 — Symmetric annuli add positive Stieltjes atoms at the Xi origin

Claim ID: `L-105361`  
Status: **PROVED EXACT PARITY-SYMMETRIC TRANSPORT THEOREM**  
Created: 2026-08-23  
Depends on: `L-105351`, `L-105360`  
RH status: **not assumed**

## 1. Symmetric setup

Assume the hypotheses of `L-105360`, with anchor `x_*=0`. Assume in addition
that `F` has definite parity and both windows are invariant under
`z\mapsto-z`. Then the annular critical points occur in pairs `\{c,-c\}`, and

\[
\rho_{-c}=\rho_c.
\tag{L-105361.1}
\]

Write

\[
H_{\rm in}(z)=\sum_{n\ge0}\beta_n^{\rm in}z^{2n+1},
\qquad
H_{\rm out}(z)=\sum_{n\ge0}\beta_n^{\rm out}z^{2n+1}.
\tag{L-105361.2}
\]

The origin coefficients are the contour moments of `L-105351`.

## 2. Exact paired-pole expansion

For one positive annular critical point `c>0`, pair its pole with the pole at
`-c`:

\[
{\rho_c\over z-c}+{\rho_c\over z+c}
={2\rho_c z\over z^2-c^2}
={-2\rho_c\over c^2}
{z\over1-z^2/c^2}.
\tag{L-105361.3}
\]

Therefore

\[
\boxed{
\beta_n^{\rm in}
=
\beta_n^{\rm out}
+
\sum_{\substack{c>0\\c\text{ annular critical}}}
{-2\rho_c\over c^{2n+2}},
\qquad n\ge0.
}
\tag{L-105361.4}
\]

Put

\[
\boxed{
s_c={1\over c^2},
\qquad
W_c={-2\rho_c\over c^2}.
}
\tag{L-105361.5}
\]

Then

\[
\beta_n^{\rm in}
=eta_n^{\rm out}+\sum_cW_cs_c^n.
\tag{L-105361.6}
\]

If `\rho_c\le0`, then `s_c\ge0` and `W_c\ge0`: each symmetric critical pair
adds one positive Stieltjes atom.

## 3. The two Stieltjes Hankel updates

For `k\ge1`, define

\[
\mathsf S_k^{(0)}(\Omega)
=[\beta_{r+s}(\Omega)]_{r,s=0}^{k-1},
\qquad
\mathsf S_k^{(1)}(\Omega)
=[\beta_{r+s+1}(\Omega)]_{r,s=0}^{k-1}.
\]

With `v_k(s)=(1,s,\ldots,s^{k-1})^T`, equation (L-105361.6) gives

\[
\boxed{
\mathsf S_k^{(0)}(\Omega_{\rm in})
=
\mathsf S_k^{(0)}(\Omega_{\rm out})
+
\sum_cW_c v_k(s_c)v_k(s_c)^T,
}
\tag{L-105361.7}
\]

and

\[
\boxed{
\mathsf S_k^{(1)}(\Omega_{\rm in})
=
\mathsf S_k^{(1)}(\Omega_{\rm out})
+
\sum_cW_cs_c v_k(s_c)v_k(s_c)^T.
}
\tag{L-105361.8}
\]

Under nonpositive annular residues, both increments are positive semidefinite.
Hence

\[
\boxed{
\mathsf S_k^{(a)}(\Omega_{\rm in})
\succeq
\mathsf S_k^{(a)}(\Omega_{\rm out}),
\qquad a\in\{0,1\}.
}
\tag{L-105361.9}
\]

## 4. Exact Stieltjes-measure update

If the outer origin sequence has a positive Stieltjes representing measure
`\nu_out`, then

\[
\boxed{
\nu_{\rm in}
=
\nu_{\rm out}
+
\sum_cW_c\delta_{s_c}
}
\tag{L-105361.10}
\]

represents the inner sequence. Thus the two-matrix Stieltjes criterion is
preserved inward without any determinant expansion.

## 5. Safe-axis transport

For real safe-axis `y`, divide (L-105361.3) by `z` and set `z=iy`. This gives

\[
\boxed{
{H_{\rm in}(iy)\over iy}
=
{H_{\rm out}(iy)\over iy}
+
\sum_{c>0}{-2\rho_c\over c^2+y^2}.
}
\tag{L-105361.11}
\]

Every summand is nonnegative when `\rho_c\le0`, and it is exactly

\[
{W_c\over1+s_cy^2}.
\]

Thus the inward window transport adds elementary positive Stieltjes resolvents
on the actual Xi safe axis.

## 6. Cofinal fixed-order reduction

Let `\Omega_N` be a nested parity-symmetric exhaustion and suppose every
annular critical pair is real with nonpositive residue. If there is one
cofinal sequence `N_j\to\infty` such that, for every fixed `k` and
`a\in\{0,1\}`,

\[
\boxed{
\liminf_{j\to\infty}
\lambda_{\min}
\bigl(\mathsf S_k^{(a)}(\Omega_{N_j})\bigr)
\ge0,
}
\tag{L-105361.12}
\]

then the complete origin Stieltjes hierarchy is positive in every finite inner
window. It is enough to prove vanishing terminal negative part order by order;
exact terminal positivity and uniformity in `k` are unnecessary.

## 7. Affine terminal calibration

A particularly concrete sufficient terminal asymptotic is

\[
\boxed{
\beta_0(\Omega_{N_j})\longrightarrow a\ge0,
\qquad
\beta_n(\Omega_{N_j})\longrightarrow0
\quad(n\ge1).
}
\tag{L-105361.13}
\]

For each fixed `k`, both terminal matrices then converge to positive
semidefinite matrices: `\mathsf S_k^{(0)}` converges to a matrix with only the
`(0,0)` entry `a`, and `\mathsf S_k^{(1)}` converges to zero. Hence
(L-105361.12) follows.

This is the infinite-function analogue of the exact polynomial outer-window
calibration `H(z)=z/n`.

## 8. Scope

No terminal Xi asymptotic is proved here. The safe-axis scalar inequality in
(L-105361.11), even at every single `y`, should not be confused with the full
Stieltjes moment hierarchy unless complete monotonicity or the two Hankel
families are established. Nonreal critical pairs and positive residues remain
binding obstructions. RH is unproved.
