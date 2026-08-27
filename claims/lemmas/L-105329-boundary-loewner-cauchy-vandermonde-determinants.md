# L-105329 — Boundary Loewner positivity has an exact Cauchy–Vandermonde determinant hierarchy

Claim ID: `L-105329`  
Status: **PROVED EXACT AT FINITE REGULAR-WINDOW SCOPE; BOUNDARY SIGN OPEN**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105217`, `L-105218`  
RH status: **not assumed**

## 1. Boundary remainder

Let `F`, `Omega` and a real interval `I subset Omega` satisfy the hypotheses of
`L-105214`. Write

\[
H_{F,\Omega}(z)
={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta.
\tag{L-105329.1}
\]

The complete boundary part of the Bezoutian is

\[
\mathscr R_{F,\Omega}(x,y)
=F'(x)F'(y){H_{F,\Omega}(x)-H_{F,\Omega}(y)\over x-y}
\tag{L-105329.2}
\]

and also

\[
\mathscr R_{F,\Omega}(x,y)
={F'(x)F'(y)\over2\pi i}
\int_{\partial\Omega}
 {F(\zeta)/F'(\zeta)\over(\zeta-x)(\zeta-y)}\,d\zeta.
\tag{L-105329.3}
\]

## 2. Every quadratic form is one contour square

For a finite packet of distinct noncritical real nodes

\[
X=(x_1,\ldots,x_k)\subset I
\]

and a real vector `v`, put

\[
G_{X,v}(\zeta)
=\sum_{j=1}^{k}{v_jF'(x_j)\over\zeta-x_j}.
\tag{L-105329.4}
\]

Then

\[
\boxed{
v^T\mathscr R_Xv
={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)\over F'(\zeta)}G_{X,v}(\zeta)^2\,d\zeta.
}
\tag{L-105329.5}
\]

Thus `BRP105220` is not an unspecified matrix event: every candidate negative
square is one explicit rationally weighted boundary contour.

## 3. Exact packet determinant

Andreief's identity gives

\[
\boxed{
\begin{aligned}
\det\mathscr R_X
={1\over k!(2\pi i)^k}
\int_{(\partial\Omega)^k}
&\det\!\left[
 {F'(x_i)\over\zeta_a-x_i}
\right]_{i,a=1}^{k}{}^2\\
&\times\prod_{a=1}^{k}{F(\zeta_a)\over F'(\zeta_a)}\,d\zeta_a.
\end{aligned}
}
\tag{L-105329.6}
\]

The Cauchy determinant evaluates explicitly. After squaring,

\[
\boxed{
\det\!\left[
 {F'(x_i)\over\zeta_a-x_i}
\right]^2
=
{\displaystyle
 \left(\prod_iF'(x_i)^2\right)
 \Delta(X)^2\Delta(\zeta)^2
 \over\displaystyle
 \prod_{i,a}(\zeta_a-x_i)^2}.
}
\tag{L-105329.7}
\]

Consequently,

\[
\boxed{
\begin{aligned}
\det\mathscr R_X
={\left(\prod_iF'(x_i)^2\right)\Delta(X)^2
 \over k!(2\pi i)^k}
\int_{(\partial\Omega)^k}
 {\Delta(\zeta)^2
  \prod_a F(\zeta_a)/F'(\zeta_a)
 \over
  \prod_{i,a}(\zeta_a-x_i)^2}
\prod_a d\zeta_a.
\end{aligned}
}
\tag{L-105329.8}
\]

This is the boundary analogue of the critical-residue Vandermonde hierarchy
in `L-105328`.

## 4. Exact equivalence to the all-packet gate

A real symmetric matrix is positive semidefinite exactly when all its
principal minors are nonnegative. Every principal submatrix of
`mathscr R_X` is the matrix of a subpacket. Therefore

\[
\boxed{
\mathscr R_{F,\Omega}\succeq0
\text{ on every finite real packet}
\quad\Longleftrightarrow\quad
\det\mathscr R_X\ge0
\text{ for every finite packet }X.
}
\tag{L-105329.9}
\]

Define

```text
BCVH105330:
  every determinant in (L-105329.8) is nonnegative for every real packet in
  every window of the exact Xi exhaustion.
```

At the finite-window level, `BCVH105330` is exactly the all-packet
positive-semidefiniteness component of `BRP105220`. The separate clause
excluding a nonreal critical correction is supplied by `CRVH105330` in
`L-105328`. No packet-size bootstrap is being assumed.

## 5. Confluent one-centre hierarchy

Let all packet nodes coalesce at a real noncritical point `x`. With normalized
derivative evaluation, the confluent Loewner matrix is

\[
\boxed{
\mathsf L_k(x)
=\left[
 {H_{F,\Omega}^{(r+s+1)}(x)\over(r+s+1)!}
\right]_{r,s=0}^{k-1}.
}
\tag{L-105329.10}
\]

Its entries are the exact contour moments

\[
{H^{(r+s+1)}(x)\over(r+s+1)!}
={1\over2\pi i}\int_{\partial\Omega}
 {F(\zeta)/F'(\zeta)\over(\zeta-x)^{r+s+2}}\,d\zeta.
\tag{L-105329.11}
\]

A second Andreief calculation yields

\[
\boxed{
\det\mathsf L_k(x)
={1\over k!(2\pi i)^k}
\int_{(\partial\Omega)^k}
 {\Delta(\zeta)^2
  \prod_aF(\zeta_a)/F'(\zeta_a)
 \over
  \prod_a(\zeta_a-x)^{2k}}
\prod_a d\zeta_a.
}
\tag{L-105329.12}
\]

These one-centre determinants are necessary confluent consequences of BRP and
are natural scalar targets for local analysis. This lemma does **not** promote
them alone to the complete separated-packet theorem.

## 6. Polynomial calibration and nested-window transport

For a polynomial in an outer window containing every critical point,

\[
H_{p,\Omega}(z)=z/n+b,
\]

so the boundary remainder is the rank-one positive kernel

\[
\mathscr R_{p,\Omega}(x,y)=p'(x)p'(y)/n.
\]

All determinants of size at least two vanish. Thus the hierarchy has the
correct finite-polynomial boundary calibration.

Under enlargement across real nonpositive critical residues, `L-105217`
transports the boundary remainder by positive rank-one increments. Hence one
positive outer-window boundary hierarchy descends through every such annulus.
The missing Xi input is a positive terminal boundary window and control of any
nonreal annular critical packet.

## 7. Scope

The determinant identities are exact but provide no sign for their contour
integrals. The contour variable lives on the literal finite boundary; replacing
it by a safe-axis coordinate requires an exact normalization and exhaustion
map. `BCVH105330`, the complete `BRP105220` gate, and RH remain open.
