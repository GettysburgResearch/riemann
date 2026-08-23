# L-105380 — Odd Xi derivatives have explicit origin source-moment matrices

Claim ID: `L-105380`  
Status: **PROVED EXACT SOURCE COORDINATE — HIGHER SIGN INEQUALITIES OPEN**  
Created: 2026-08-23  
Depends on: the positive Xi Fourier kernel; `L-105370`  
RH status: **not assumed**

## 1. Positive tilted Fourier law

Use a one-sided positive Fourier representation

\[
\Xi(t)=\int_0^\infty\Phi(u)\cos(tu)\,du,
\qquad
\Phi(u)>0.
\]

Fix an odd derivative order

\[
r=2\ell+1
\]

and put

\[
F(t)=\Xi^{(r)}(t).
\]

Up to a common nonzero real scalar, which cancels in `F/F'`,

\[
F(z)=\int_0^\infty u^{r}\Phi(u)\sin(zu)\,du,
\]

\[
F'(z)=\int_0^\infty u^{r+1}\Phi(u)\cos(zu)\,du.
\]

Define the probability law

\[
\boxed{
 d\mathbb P_r(u)
={u^{r+1}\Phi(u)\,du
 \over
 \int_0^\infty u^{r+1}\Phi(u)\,du}.
}
\tag{L-105380.1}
\]

Let `U` have this law, set `X=U^2`, and define

\[
\boxed{
\mu_j=\mathbb E_r[X^j],
\qquad j\ge0,
\qquad \mu_0=1.
}
\tag{L-105380.2}
\]

Then

\[
\boxed{
{F(z)\over F'(z)}
=
{\mathbb E_r[\sin(zU)/U]
 \over
 \mathbb E_r[\cos(zU)]}.
}
\tag{L-105380.3}
\]

## 2. Exact source-coefficient recurrence

Write the odd source germ

\[
\boxed{
{F(z)\over F'(z)}
=z\sum_{n\ge0}a_n^{(r)}z^{2n}.
}
\tag{L-105380.4}
\]

The numerator and denominator in (L-105380.3) are

\[
{\mathbb E[\sin(zU)/U]\over z}
=
\sum_{j\ge0}{(-1)^j\mu_jz^{2j}\over(2j+1)!},
\]

\[
\mathbb E[\cos(zU)]
=
\sum_{j\ge0}{(-1)^j\mu_jz^{2j}\over(2j)!}.
\]

Coefficient comparison gives

\[
\boxed{
a_0^{(r)}=1,}
\tag{L-105380.5}
\]

and, for `n>=1`,

\[
\boxed{
 a_n^{(r)}
={(-1)^n\mu_n\over(2n+1)!}
-
\sum_{j=1}^{n}
{(-1)^j\mu_j\over(2j)!}
 a_{n-j}^{(r)}.
}
\tag{L-105380.6}
\]

This recursion computes every source matrix of `L-105370` directly from the
positive tilted Xi moments.

## 3. First four coefficients

Put

\[
x=\mu_1,
\qquad
y=\mu_2,
\qquad z_3=\mu_3.
\]

Then

\[
\boxed{a_0=1,}
\tag{L-105380.7}
\]

\[
\boxed{a_1={x\over3},}
\tag{L-105380.8}
\]

\[
\boxed{a_2={x^2\over6}-{y\over30}
={5x^2-y\over30},}
\tag{L-105380.9}
\]

and

\[
\boxed{
 a_3
={x^3\over12}-{11xy\over360}+{z_3\over840}
={210x^3-77xy+3z_3\over2520}.
}
\tag{L-105380.10}
\]

The first shifted source pivot is therefore unconditionally positive:

\[
\boxed{\mathsf A_1^{(1)}=[x/3]\succ0.}
\tag{L-105380.11}
\]

Together with `A_1^(0)=[1]`, the complete source side of the order-one capacity
problem is strictly positive for every odd Xi derivative.

## 4. First nontrivial source determinants

The order-two unshifted source determinant is

\[
\boxed{
\det\mathsf A_2^{(0)}
=a_2-a_1^2
={5x^2-3y\over90}.
}
\tag{L-105380.12}
\]

Hence

\[
\mathsf A_2^{(0)}\succeq0
\iff
{y\over x^2}\le{5\over3}.
\tag{L-105380.13}
\]

Equivalently, for the positive variable `X`,

\[
\operatorname{Var}(X)\le{2\over3}\mathbb E[X]^2.
\]

The order-two shifted determinant is

\[
\boxed{
\det\mathsf A_2^{(1)}
=a_1a_3-a_2^2
={35x^2y+15xz_3-42y^2\over37800}.
}
\tag{L-105380.14}
\]

Thus its exact source condition is

\[
\boxed{
35x^2y+15xz_3\ge42y^2.
}
\tag{L-105380.15}
\]

These are literal moment-shape inequalities for the tilted positive Xi kernel,
not zero-location statements.

## 5. Exact order-one critical capacities

Assume the nonzero critical points in a symmetric window are real with
nonpositive residues, and put

\[
s_c=c^{-2},
\qquad
W_c=-2F(c)/(c^2F''(c))\ge0.
\]

From `L-105370`, the two order-one boundary pivots are

\[
\boxed{
\beta_0(F;\Omega)
=1-\sum_cW_c,
}
\tag{L-105380.16}
\]

and

\[
\boxed{
\beta_1(F;\Omega)
={x\over3}-\sum_cW_cs_c.
}
\tag{L-105380.17}
\]

Therefore the complete order-one origin Stieltjes gate is exactly

\[
\boxed{
\sum_cW_c\le1,
\qquad
\sum_cW_cs_c\le{x\over3}.
}
\tag{L-105380.18}
\]

No source-matrix conditioning or Christoffel inversion is required at this
order.

## 6. Point-mass and high-saddle calibration

If the tilted law collapses to one point with `X=x`, then

\[
\mu_j=x^j
\]

and

\[
{F(z)\over zF'(z)}
={\tan(\sqrt{x}z)\over\sqrt{x}z}.
\]

The coefficients become

\[
1,\quad{x\over3},\quad{2x^2\over15},
\quad{17x^3\over315},\ldots
\]

and the determinant margins in (L-105380.12) and (L-105380.14) are strictly
positive. The moving-saddle programme predicts that the tilted Xi law becomes
asymptotically concentrated, so these source determinants should enter the
positive cone with room in the high derivative tail. That analytic assertion
remains subject to the hostile review of `L-105321`.

## 7. Scope

Positivity of `Phi` proves the probability representation and `a_1>0`, but it
does not by itself prove the kurtosis and third-moment inequalities
(L-105380.13) and (L-105380.15). Mixtures with sufficiently broad support can
violate them. No claim is made here for even derivative levels, all matrix
orders, the critical capacities, or RH.
