# L-15126 — One-sided certified-zero residual control is the exact finite floor

Claim ID: `L-15126`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA; COFINAL ARITHMETIC LOWER BOUND OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15125`; elementary Loewner order  
Scope: sharpen the noncircular selected-zero-frame route by charging only the negative part of the complete arithmetic residual  
Related counterexample candidates: none

## 1. Purpose

`L-15125` bounds the complete residual target-pinned matrix by

\[
 |x^{\mathsf T}R_p(c)x|\le \omega\,x^{\mathsf T}Mx.
\]

That absolute-value estimate is sufficient but unnecessarily strong.  Positive
unselected critical-line mass is harmless and can be arbitrarily large; only
negative residual energy can defeat completion.

The correct finite object is therefore a **one-sided** residual floor.

## 2. Setup

Let the distinct real nodes be `lambda_1,...,lambda_n`, let every target
coordinate `p_i` be nonzero, and normalize

\[
 \eta^{\mathsf T}p=1,
 \qquad \eta=(1,\ldots,1)^{\mathsf T}.
\]

For any real symmetric special matrix `Q` and scalar `c`, write

\[
 \mathcal T_p(Q,c)
 =Q+\operatorname{diag}\!\left(
   \frac{c\eta_i-(Qp)_i}{p_i}
  \right)-c\eta\eta^{\mathsf T}.
\]

Let `Q_Z` be a positive matrix assembled from a finite proof-grade set of
critical-line zeros as in `L-15122`, and put

\[
 z=Q_Zp,
 \qquad
 S_Z=\mathcal T_p(Q_Z,0)
     =Q_Z-\operatorname{diag}(z_i/p_i).
\]

Let the complete arithmetic residual be

\[
 Q_{\rm rem}=Q_W-Q_Z,
 \qquad
 R_p(c)=\mathcal T_p(Q_{\rm rem},c).
\]

By linearity of target pinning,

\[
 \boxed{
 \mathcal T_p(Q_W,c)=S_Z+R_p(c).}
 \tag{L-15126.1}
\]

Both summands annihilate `p`.

Let

\[
 M=\operatorname{diag}(m_1,\ldots,m_n),
 \qquad m_i>0.
\]

## 3. One-sided completion theorem

Assume:

### A. Selected Cauchy-frame floor

For every `x perpendicular p`,

\[
 x^{\mathsf T}Q_Zx\ge g\,x^{\mathsf T}Mx
 \tag{L-15126.2}
\]

for one `g>0`.

### B. Coordinate-relative selected target residual

For every coordinate,

\[
 |z_i|\le \rho\,|p_i|m_i
 \tag{L-15126.3}
\]

for one `rho>=0`.

### C. One-sided complete arithmetic residual floor

For every `x perpendicular p`,

\[
 \boxed{
 x^{\mathsf T}R_p(c)x
 \ge-\omega_-\,x^{\mathsf T}Mx}
 \tag{L-15126.4}
\]

for one `omega_- >=0`.

If

\[
 \boxed{\rho+\omega_-<g,}
 \tag{L-15126.5}
\]

then

\[
 \boxed{
 \mathcal T_p(Q_W,c)\succeq0,
 \qquad
 \ker\mathcal T_p(Q_W,c)=\mathbb Rp.}
 \tag{L-15126.6}
\]

### Proof

For `x perpendicular p`, (L-15126.3) gives

\[
 \left|\sum_i\frac{z_i}{p_i}x_i^2\right|
 \le\rho\,x^{\mathsf T}Mx.
\]

Thus

\[
 x^{\mathsf T}S_Zx
 \ge(g-\rho)x^{\mathsf T}Mx.
\]

Combining this with (L-15126.1) and the one-sided bound
(L-15126.4),

\[
 x^{\mathsf T}\mathcal T_p(Q_W,c)x
 \ge(g-\rho-\omega_-)x^{\mathsf T}Mx>0
\]

for every nonzero `x perpendicular p`.  The full matrix annihilates `p`, so it
is positive semidefinite with exactly the target line as kernel. QED.

## 4. Optimal residual radius

On `H=p^perp`, define

\[
 \boxed{
 \omega_-^*(c)
 =\max\left\{0,
 -\lambda_{\min}\!\left(
  M_H^{-1/2}R_p(c)|_H M_H^{-1/2}
 \right)\right\}.}
 \tag{L-15126.7}
\]

This is the smallest possible number in (L-15126.4).  It can be certified
root-free by the directed LMI

\[
 \boxed{
 R_p(c)+\omega_-M\succeq0
 \quad\text{on }p^perp.}
 \tag{L-15126.8}
\]

By contrast, the absolute residual radius of `L-15125` is

\[
 \omega_{\rm abs}(c)
 =\left\|M_H^{-1/2}R_p(c)|_H M_H^{-1/2}\right\|_2,
\]

and always satisfies

\[
 \omega_-^*(c)\le\omega_{\rm abs}(c).
\]

The inequality can be arbitrarily strict: for `R_p(c)=A M` with `A>0`,
`omega_-^*=0` while `omega_abs=A`.

## 5. Direct selected-pinned floor

The coordinate split is optional.  If directed arithmetic certifies directly

\[
 S_Z\succeq s_ZM
 \quad\text{on }p^perp
 \tag{L-15126.9}
\]

and

\[
 R_p(c)\succeq-\omega_-M
 \quad\text{on }p^perp,
\]

then `s_Z>omega_-` proves the same conclusion.  This is often sharper than
separately estimating `g` and `rho`.

## 6. Cofinal criterion

For actual smooth targets `p_j`, selected line-zero frames, metrics `M_j`, and
rational scalars `c_j`, it is sufficient that

\[
 \boxed{
 \limsup_{j\to\infty}
 \frac{\rho_j+\omega_{-,j}}{g_j}<1.}
 \tag{L-15126.10}
\]

Equivalently, one may prove the direct strict LMIs

\[
 S_{Z_j}-s_jM_j\succeq0,
 \qquad
 R_j+\omega_jM_j\succeq0,
 \qquad
 0\le\omega_j<s_j.
 \tag{L-15126.11}
\]

No upper bound on the positive spectrum of the residual is needed.

## 7. Zero-side meaning

After subtracting a finite proof-grade line-zero set, every additional
critical-line zero contributes a positive rank-one Cauchy matrix to the
un-pinned residual.  Charging its positive eigenvalues in an absolute operator
norm discards exactly the sign information supplied by the zero side.

The one-sided LMI is therefore the natural prime-side object.  Under false RH,
an off-line conjugate pair produces a genuine negative cardinal block; under
RH, the un-pinned all-zero residual is positive.  The target-pinning diagonal
remains explicit and is controlled by the same transform-evaluation residual
used for the selected block.

This interpretation does not assume RH.  It identifies which sign of the
complete residual must be certified from the explicit formula.

## 8. Gap audit

1. The theorem improves a sufficient bound; it does not produce the cofinal
   lower residual estimate.
2. The selected-frame floor may shrink with rank and support.
3. The target-pinning diagonal of the residual must be included in
   `R_p(c)`; positivity of the raw residual source alone is insufficient.
4. A midpoint smallest eigenvalue is not a directed LMI.
5. Under false RH the one-sided residual contains an exact negative cardinal
   obstruction; `R-15105` records the quantitative consequence.
