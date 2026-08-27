# Dual Vandermonde contour hierarchies for the sharp Xi last defect

Date: 2026-08-23  
Dedicated PR: #729  
Scientific status: **RH unproved**

## Main exact advance

The complete critical-residue sign problem in one regular window is the
positive-definiteness of the Hankel matrix

\[
\mathsf P_{rs}
=-{1\over2\pi i}\int_{\partial\Omega}
 {F(z)\over F'(z)}z^{r+s}\,dz.
\]

If `c_j` are the critical points and `rho_j=F(c_j)/F''(c_j)`, then

\[
\mathsf P=V^T\operatorname{diag}(-\rho_j)V.
\]

Thus all critical points are real with negative residues exactly when every
leading determinant is positive. The generalized pencil with the unweighted
critical count matrix has characteristic polynomial

\[
{\det(\mathsf P+t\mathsf G)\over\det\mathsf G}
=\prod_j(t-\rho_j),
\]

and in the polynomial case it is the quotient-algebra resultant already
present on this PR.

Each leading determinant is one exact Vandermonde multiple-contour integral.
This replaces an overstrong global coherence average by a sharp finite scalar
hierarchy.

## Boundary dual

For every real packet `X`, the determinant of the parent Cauchy-Loewner
remainder is

\[
\det\mathscr R_X
={\left(\prod_iF'(x_i)^2\right)\Delta(X)^2
 \over k!(2\pi i)^k}
\int
 {\Delta(\zeta)^2\prod_aF(\zeta_a)/F'(\zeta_a)
 \over\prod_{i,a}(\zeta_a-x_i)^2}
\prod_a d\zeta_a.
\]

Nonnegativity for every packet is exactly the parent all-packet boundary-PSD component. The critical hierarchy separately excludes nonreal critical corrections.
The residue and boundary hierarchies are the two scalar determinant faces of
the exact Bezoutian Schur split.

## Binding separator

For

\[
p=x^4-2x^2-1,
\]

the residues are `(-1/4,1/4,-1/4)`. The first two leading critical
determinants are `1/4` and `1/8`, but the complete determinant is `-1/16`.
Therefore neither the first moment nor the first exterior-square channel
certifies the pointwise sign gate.

## Correct conclusion graph

```text
CRVH105330 complete critical determinant hierarchy
AND
BCVH105330 complete boundary determinant hierarchy
-> PRES105220 AND BRP105220
-> RH.
```

Both Xi determinant hierarchies remain open.

## Moving-saddle audit

The proposed moving-saddle theorem remains plausible but not authenticated.
The correct shifted contour is `(u_(m,z)-w_m)+[0,infinity)`. A uniform global
relative-dominance inequality away from the moving saddle and explicit
connector ratios are still required. Fixed derivative estimates should use
relative approximation on `z`-disks of radius comparable to `1/(1+w_m)`.

## Replay

```text
PASS_X_105330_DUAL_VANDERMONDE_CONTOUR_HIERARCHIES
222 exact rational checks
93f59673fad499278a27b6a93f801d96156907759642bf6b8fc9fb0626a66c5e
```

The replay certifies finite algebra only and records both sharp Xi gates and RH
as unproved.
