# L-15125 — Certified-zero frame plus complete arithmetic residual implies target completion

Claim ID: `L-15125`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA; COFINAL FRAME/RESIDUAL ESTIMATES OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15110`, `L-15119`, `L-15122`; elementary Loewner order  
Scope: direct noncircular positivity of the fixed arithmetic target-pinned matrix, without target-root or canonical-inertia assumptions  
Related counterexample candidates: none

## 1. Purpose and scope correction

The root-explicit residue formula of `L-15122` is exact and valuable, but using it
requires the finite target polynomial to be simple and real-rooted.  Cofinal
simple real-rootedness together with convergence to `Xi` already implies RH by
Hurwitz, before the arithmetic scalar line is inspected.

The genuinely noncircular finite route must therefore prove positivity of the
fixed arithmetic target-pinned matrix **without first proving the target roots
real**.

This lemma does so.  A finite set of already certified critical-line zeros
builds an unconditional positive Cauchy frame.  The actual smooth target is
nearly in its kernel because its transform is small at those zeros.  Every
unselected contribution is retained in one complete prime-side residual
matrix.  If the positive frame moat dominates both errors, the full arithmetic
completion is positive and real-rootedness follows only at the end.

## 2. Target-pinning map and linearity

Let the distinct real nodes be

\[
 \lambda_1,\ldots,\lambda_n,
\]

let every target coordinate `p_i` be nonzero, and normalize

\[
 \eta^{\mathsf T}p=1,
 \qquad
 \eta=(1,\ldots,1)^{\mathsf T}.
 \tag{L-15125.1}
\]

For any real symmetric special matrix `Q` and scalar `c`, define

\[
 \mathcal T_p(Q,c)
 =Q+
 \operatorname{diag}\!\left(
  \frac{c\eta_i-(Qp)_i}{p_i}
 \right)
 -c\eta\eta^{\mathsf T}.
 \tag{L-15125.2}
\]

Then

\[
 \mathcal T_p(Q,c)p=0.
 \tag{L-15125.3}
\]

The map is linear:

\[
 \boxed{
 \mathcal T_p(Q_1+Q_2,c_1+c_2)
 =\mathcal T_p(Q_1,c_1)
  +\mathcal T_p(Q_2,c_2).}
 \tag{L-15125.4}
\]

## 3. Positive selected-zero frame

Let `Z` be a finite proof-grade multiset of nonresonant real centered zeta
zeros.  Use `L-15122` to form the positive matrix

\[
 Q_Z
 =\sum_{\gamma\in Z}
  A_{\gamma,L}\,
  \ell_\gamma\ell_\gamma^{\mathsf T},
 \qquad
 (\ell_\gamma)_i
 =\frac1{r_{\gamma,L}-\lambda_i},
 \tag{L-15125.5}
\]

where

\[
 A_{\gamma,L}
 =m_\gamma\frac{L}{\pi^2}
  \sin^2(\pi r_{\gamma,L})>0.
\]

Thus

\[
 Q_Z\succeq0.
\]

Let the selected target residual be

\[
 z=Q_Zp.
 \tag{L-15125.6}
\]

The selected target-pinned matrix at zero boundary scalar is

\[
 S_Z
 :=\mathcal T_p(Q_Z,0)
 =Q_Z-\operatorname{diag}\!\left(\frac{z_i}{p_i}\right).
 \tag{L-15125.7}
\]

It satisfies `S_Z p=0` exactly.

## 4. Complete arithmetic residual

Let `Q_W` be the actual finite Weil special matrix, represented by the complete
polar, archimedean, and all-prime-power source of `L-15119`.  Subtract the
selected-zero source/matrix:

\[
 Q_{\rm rem}=Q_W-Q_Z.
 \tag{L-15125.8}
\]

No sign is assigned to `Q_rem`; it contains every unselected zero orbit
implicitly through the explicit formula.

For one real boundary scalar `c`, put

\[
 R_p(c)
 :=\mathcal T_p(Q_{\rm rem},c).
 \tag{L-15125.9}
\]

By linearity,

\[
 \boxed{
 \mathcal T_p(Q_W,c)
 =S_Z+R_p(c).}
 \tag{L-15125.10}
\]

Both summands annihilate `p`.

## 5. Direct frame/residual theorem

Let

\[
 M=\operatorname{diag}(m_1,\ldots,m_n),
 \qquad m_i>0,
 \tag{L-15125.11}
\]

be a positive diagonal metric.  Suppose:

### A. Selected-frame coercivity

For every `x perpendicular p`,

\[
 \boxed{
 x^{\mathsf T}Q_Zx
 \ge g\,x^{\mathsf T}Mx}
 \tag{L-15125.12}
\]

for one `g>0`.

### B. Coordinate-relative selected residual

For every coordinate,

\[
 \boxed{
 |z_i|\le\rho\,|p_i|m_i}
 \tag{L-15125.13}
\]

for one `rho>=0`.

### C. Complete residual-form bound

For every `x perpendicular p`,

\[
 \boxed{
 |x^{\mathsf T}R_p(c)x|
 \le\omega\,x^{\mathsf T}Mx}
 \tag{L-15125.14}
\]

for one `omega>=0`.

If

\[
 \boxed{\rho+\omega<g,}
 \tag{L-15125.15}
\]

then

\[
 \boxed{
 \mathcal T_p(Q_W,c)\succeq0,
 \qquad
 \ker\mathcal T_p(Q_W,c)=\mathbb Rp.}
 \tag{L-15125.16}
\]

### Proof

For every `x perpendicular p`, (L-15125.13) gives

\[
 \left|
  \sum_i\frac{z_i}{p_i}x_i^2
 \right|
 \le\rho\sum_i m_ix_i^2
 =\rho x^{\mathsf T}Mx.
\]

Therefore

\[
 x^{\mathsf T}S_Zx
 \ge(g-\rho)x^{\mathsf T}Mx.
\]

Using (L-15125.10) and (L-15125.14),

\[
 x^{\mathsf T}\mathcal T_p(Q_W,c)x
 \ge(g-\rho-\omega)x^{\mathsf T}Mx>0
\]

for every nonzero `x perpendicular p`.  The full matrix annihilates `p`, so it
is positive semidefinite with exactly the target line as kernel. QED.

No target polynomial, target root, canonical Loewner matrix, or RH-positive
all-zero representation occurs in this proof.

## 6. Exact transform-evaluation form of the selected residual

For the integer CCM nodes `-N,...,N`, `L-15122` gives

\[
 \widehat V_n(\gamma)
 =\frac{\sqrt L}{\pi}
  \frac{\sin(\pi r_{\gamma,L})}
       {r_{\gamma,L}-n}.
 \tag{L-15125.17}
\]

Let `F_p` be the compact finite transform of the coefficient vector `p` in the
same normalization.  Then

\[
 F_p(\gamma)
 =\frac{\sqrt L}{\pi}
  \sin(\pi r_{\gamma,L})
  \sum_n\frac{p_n}{r_{\gamma,L}-n}.
 \tag{L-15125.18}
\]

Consequently

\[
 \boxed{
 (Q_Zp)_i
 =\sum_{\gamma\in Z}
  m_\gamma\frac{\sqrt L}{\pi}
  \sin(\pi r_{\gamma,L})
  \frac{F_p(\gamma)}
       {r_{\gamma,L}-\lambda_i}.}
 \tag{L-15125.19}
\]

At a certified zeta zero,

\[
 \Xi(\gamma)=0,
\]

so a directed smooth-target transform error immediately bounds
`|F_p(gamma)|`.  Equation (L-15125.19) turns those pointwise errors into the
coordinate-relative residual `rho` without root isolation.

This is the direct payoff of the selected-zero frame.

## 7. Frame coercivity without target roots

The matrix `Q_Z` is an explicit positive weighted Cauchy Gram.  Its coercivity
on `p^perp` can be certified by:

1. direct interval `LDL^T` on a rational complement basis;
2. a smallest generalized eigenvalue against the diagonal metric `M`;
3. a Cauchy-determinant lower bound for the selected evaluation frame,
   followed by the angle between its one-dimensional kernel and `p^perp`.

When `|Z|=n-1` and the selected ordinates are distinct and nonresonant, the
Cauchy evaluation vectors are linearly independent.  Hence `Q_Z` has corank one.
Its restriction to `p^perp` is positive definite exactly when its kernel vector
is not orthogonal to `p`.  This is a finite directed condition, not an RH
assumption.

## 8. Complete residual-form production

The residual matrix `R_p(c)` is built from

\[
 \beta^{\rm rem}=\beta^W-\beta^Z
\]

using the same target-pinning formula (L-15125.2).  A production proof may bound
(L-15125.14) by:

- direct interval generalized `LDL^T` of
  
  \[
  \omega M\pm R_p(c)
  \quad\text{on }p^perp;
  \]
- a weighted row-sum bound;
- an exact small scalar optimization in `c`;
- a Schur or source-line bound exploiting parity.

Unlike an all-zero positive expansion, this residual is computed entirely from
the complete prime-side explicit formula and the finite certified-zero
subtraction.

## 9. Cofinal criterion

For a sequence of actual smooth targets `p_j`, finite certified-zero sets `Z_j`,
diagonal metrics `M_j`, and rational scalars `c_j`, suppose directed proof
objects establish

\[
 Q_{Z_j}\succeq g_jM_j
 \quad\text{on }p_j^perp,
 \tag{L-15125.20}
\]

\[
 |(Q_{Z_j}p_j)_i|
 \le\rho_j|(p_j)_i|(M_j)_{ii},
 \tag{L-15125.21}
\]

and

\[
 |x^{\mathsf T}R_{p_j}(c_j)x|
 \le\omega_jx^{\mathsf T}M_jx
 \quad(x\perp p_j).
 \tag{L-15125.22}
\]

Then the arithmetic scalar line passes cofinally whenever

\[
 \boxed{
 \limsup_{j\to\infty}
 \frac{\rho_j+\omega_j}{g_j}<1.}
 \tag{L-15125.23}
\]

The stronger ratio tending to zero is sufficient.

This is the corrected, noncircular final cofinal statement.  It requires no
prior finite real-rootedness theorem; real-rootedness is the conclusion of the
positive arithmetic matrix.

## 10. Gap audit

1. A selected positive zero frame is unconditional, but its frame floor on
   `p^perp` must be directed and may shrink with dimension.
2. Pointwise transform errors must be converted to coordinate-relative bounds;
   tiny target coefficients remain a conditioning hazard.
3. The complete residual matrix includes all unselected arithmetic content and
   is load bearing.
4. Choosing `|Z|=n-1` is natural but not mandatory; a lower-rank frame cannot be
   coercive on all of `p^perp` without another positive block.
5. The theorem is sufficient, not necessary.
6. No cofinal Riemann sequence satisfying (L-15125.23) is proved here.