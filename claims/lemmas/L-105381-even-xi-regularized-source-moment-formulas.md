# L-105381 — Even Xi derivatives have explicit regularized origin source moments

Claim ID: `L-105381`  
Status: **PROVED EXACT SOURCE COORDINATE — SIGN INEQUALITIES OPEN**  
Created: 2026-08-23  
Depends on: the positive Xi Fourier kernel; `L-105370`  
RH status: **not assumed**

## 1. Positive tilted law and the central residue

Fix an even derivative order

\[
r=2\ell
\]

and put

\[
F(t)=\Xi^{(r)}(t).
\]

Define the probability law

\[
\boxed{
 d\mathbb P_r^{\rm ev}(u)
={u^{r+2}\Phi(u)\,du
 \over
 \int_0^\infty u^{r+2}\Phi(u)\,du}.
}
\tag{L-105381.1}
\]

Let `U` have this law, put `X=U^2`, and define

\[
h=\mathbb E[X^{-1}],
\qquad
x=\mathbb E[X],
\qquad
y=\mathbb E[X^2],
\qquad
z_3=\mathbb E[X^3].
\tag{L-105381.2}
\]

The ratio has the exact probability form

\[
\boxed{
{F(z)\over F'(z)}
=-
{\mathbb E[\cos(zU)/U^2]
 \over
 \mathbb E[\sin(zU)/U]}.
}
\tag{L-105381.3}
\]

At the origin it has the central critical pole

\[
\boxed{
\rho_0={F(0)\over F''(0)}=-h<0.
}
\tag{L-105381.4}
\]

Define the regularized odd source germ

\[
\boxed{
\widehat m_F(z)
={F(z)\over F'(z)}-{\rho_0\over z}
=z\sum_{n\ge0}a_n^{(r),\rm ev}z^{2n}.
}
\tag{L-105381.5}
\]

## 2. Exact quotient series

With `t=z^2`, write

\[
R(t)
=-
{h-t/2+xt^2/24-yt^3/720+z_3t^4/40320-\cdots
 \over
 1-xt/6+yt^2/120-z_3t^3/5040+\cdots}.
\tag{L-105381.6}
\]

Then

\[
{F(z)\over F'(z)}={R(z^2)\over z},
\qquad
R(0)=-h,
\]

and `a_n` is the coefficient of `t^(n+1)` in `R(t)`.

## 3. First three regularized coefficients

Direct division gives

\[
\boxed{
 a_0^{\rm ev}
={1\over2}-{hx\over6}
={3-hx\over6}.
}
\tag{L-105381.7}
\]

The first shifted coefficient is

\[
\boxed{
 a_1^{\rm ev}
={x\over24}-{hx^2\over36}+{hy\over120}
={15x-10hx^2+3hy\over360}.
}
\tag{L-105381.8}
\]

The next coefficient is

\[
\boxed{
\begin{aligned}
 a_2^{\rm ev}
={}&{x^2\over144}-{y\over360}
-{hx^3\over216}+{hxy\over360}-{hz_3\over5040}\\
={}&{105x^2-42y-70hx^3+42hxy-3hz_3\over15120}.
\end{aligned}
}
\tag{L-105381.9}
\]

These formulas are exact for every even Xi derivative satisfying the simple
central-pole hypothesis.

## 4. Exact order-one source conditions

The two source matrices at order one are

\[
\mathsf A_1^{(0)}=[a_0^{\rm ev}],
\qquad
\mathsf A_1^{(1)}=[a_1^{\rm ev}].
\]

Therefore

\[
\boxed{
\mathsf A_1^{(0)}\succeq0
\iff
hx\le3,
}
\tag{L-105381.10}
\]

and

\[
\boxed{
\mathsf A_1^{(1)}\succeq0
\iff
15x+3hy\ge10hx^2.
}
\tag{L-105381.11}
\]

The elementary Cauchy inequality gives only `hx>=1`; it does not supply the
required upper bound. These are genuine concentration inequalities for the
even tilted Xi law.

## 5. Exact order-one critical capacities

Assume every nonzero critical point in a symmetric window is real with
nonpositive residue, and put

\[
s_c=c^{-2},
\qquad
W_c=-2F(c)/(c^2F''(c))\ge0.
\]

Then

\[
\boxed{
\beta_0(F;\Omega)
=a_0^{\rm ev}-\sum_cW_c,
}
\tag{L-105381.12}
\]

and

\[
\boxed{
\beta_1(F;\Omega)
=a_1^{\rm ev}-\sum_cW_cs_c.
}
\tag{L-105381.13}
\]

Thus the complete order-one boundary gate is

\[
\boxed{
\sum_cW_c\le{3-hx\over6},
\qquad
\sum_cW_cs_c
\le{15x-10hx^2+3hy\over360}.
}
\tag{L-105381.14}
\]

A negative source reserve on either right-hand side rules out boundary
positivity before any critical atom is inserted.

## 6. Point-mass calibration

If the tilted law collapses to `X=x`, then

\[
h=x^{-1},
\qquad y=x^2,
\qquad z_3=x^3.
\]

The regularized ratio becomes the cotangent model

\[
-{\cot(\sqrt{x}z)\over\sqrt{x}}
+{1\over xz}
={z\over3}+{xz^3\over45}+{2x^2z^5\over945}+\cdots.
\]

Accordingly,

\[
a_0^{\rm ev}={1\over3},
\qquad
a_1^{\rm ev}={x\over45},
\qquad
a_2^{\rm ev}={2x^2\over945},
\]

which checks (L-105381.7)--(L-105381.9) and gives strict positive source
reserve in the concentrated high-saddle model.

## 7. Scope

The positive Xi Fourier kernel proves the probability representation and the
central residue sign `rho_0<0`. It does not by itself prove (L-105381.10) or
(L-105381.11). No all-order source positivity, critical capacity inequality,
terminal theorem, or RH conclusion is claimed.
