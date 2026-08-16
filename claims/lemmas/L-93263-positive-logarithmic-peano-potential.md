# L-93263 — The two-switch cubic is the logarithmic curvature of one positive compact Peano potential

Claim ID: `L-93263`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-POTENTIAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93261`  
Scope: exact kernel factorization and an unconditional positive prime potential; no critical convergence rate and no RH conclusion

## 1. Two logarithmic primitives

Let

\[
 G(x)=\int_0^x W(u)\,du.
\tag{L-93263.1}
\]

Direct integration of the two pieces in `L-93261` gives

\[
 G(x)=
 \begin{cases}
 \displaystyle {x^2\over2}(5x-1)(17x-5),&0\le x\le1/4,\\[4pt]
 \displaystyle -{x^2(1-x)^2\over6},&1/4\le x\le1,\\
 0,&x\ge1.
 \end{cases}
\tag{L-93263.2}
\]

The pieces agree at `x=1/4`, with common value `-3/512`.  The cumulative
has exactly one sign change, at `x=1/5`:

\[
 G(x)>0\quad(0<x<1/5),
 \qquad
 G(x)<0\quad(1/5<x<1).
\tag{L-93263.3}
\]

Now define the logarithmic primitive

\[
 \boxed{
 \Phi(x)=\int_0^x {G(u)\over u}\,du.
 }
\tag{L-93263.4}
\]

It has the exact compact form

\[
 \boxed{
 \Phi(x)=
 \begin{cases}
 \displaystyle {x^2(85x^2-56x+10)\over8},&0\le x\le1/4,\\[5pt]
 \displaystyle {(1-x)^3(3x+1)\over72},&1/4\le x\le1,\\
 0,&x\ge1.
 \end{cases}
 }
\tag{L-93263.5}
\]

The first quadratic has discriminant

\[
 (-56)^2-4\cdot85\cdot10=-264<0
\]

and positive leading coefficient.  The second piece is manifestly positive.
Consequently

\[
 \boxed{
 \Phi(x)\ge0\quad(x\ge0),
 \qquad
 \Phi(x)>0\quad(0<x<1).
 }
\tag{L-93263.6}
\]

Thus the signed minimal-two-switch kernel has one globally positive second
logarithmic primitive.

## 2. Exact logarithmic-curvature identity

Let

\[
 D=x{d\over dx}.
\]

Equations (L-93263.1) and (L-93263.4) give

\[
 D\Phi=G,
 \qquad
 D^2\Phi=xW.
\]

Therefore

\[
 \boxed{
 W(x)={1\over x}D^2\Phi(x)
 }
\tag{L-93263.7}
\]

on `(0,1)`, with the identity extending through the knots in the natural
piecewise/distributional sense.  No signed auxiliary kernel is present:
`Phi` itself is nonnegative and compactly supported.

## 3. Mellin transform of the positive potential

Twice integrating the Mellin action of `D`, using the vanishing endpoint data,
gives

\[
 s^2\widehat\Phi(s)=\widehat W(s+1).
\]

For `Re s>-2`, one has

\[
 \boxed{
 \widehat\Phi(s)
 =
 {1-4^{-s}\over3s(s+2)(s+3)(s+4)}.
 }
\tag{L-93263.8}
\]

The apparent singularity at `s=0` is removable, and

\[
 \boxed{
 \widehat\Phi(0)
 =\int_0^1{\Phi(x)\over x}\,dx
 ={\log4\over72}.
 }
\tag{L-93263.9}
\]

For every real `s>0`, the transform is strictly positive.  At a shifted
nontrivial zero `s=rho-1`,

\[
 \widehat\Phi(\rho-1)
 ={\widehat W(\rho)\over(\rho-1)^2}\ne0.
\tag{L-93263.10}
\]

Thus passing to the positive primitive loses no open-strip zeta pole.

## 4. A positive compact prime potential

Define, for real `X>=1`,

\[
 \boxed{
 \mathcal U_\Lambda(X)
 =\sum_{n\le X}{\Lambda(n)\over n}\Phi(n/X).
 }
\tag{L-93263.11}
\]

Every coefficient and every kernel value is nonnegative, so

\[
 \mathcal U_\Lambda(X)\ge0
\tag{L-93263.12}
\]

unconditionally.  Put

\[
 \Theta=X{d\over dX}.
\]

Since `Theta` acts as `-D` on `Phi(n/X)`, the exact curvature identity is

\[
 \boxed{
 X\Theta^2\mathcal U_\Lambda(X)
 =\sum_{n\le X}\Lambda(n)W(n/X)
 =\mathcal L_W(X).
 }
\tag{L-93263.13}
\]

The cubic Q4 prime-power discrepancy is therefore the logarithmic curvature of
one explicit positive potential.

The activation at `n=X` causes no boundary atom: `Phi(1)`, its first
logarithmic derivative, and its second logarithmic derivative vanish to the
orders encoded by (L-93263.5).  The identity is valid on every open endpoint
cell and by continuous extension at the knots.

## 5. Unconditional limit and pole audit

For `Re s>0`, absolute convergence gives

\[
 \boxed{
 \int_1^\infty
 \mathcal U_\Lambda(X)X^{-s-1}\,dX
 =\widehat\Phi(s)
   \left(-{\zeta'\over\zeta}(s+1)\right).
 }
\tag{L-93263.14}
\]

The classical prime number theorem and partial summation yield the
unconditional limit

\[
 \boxed{
 \mathcal U_\Lambda(X)\longrightarrow {\log4\over72}.
 }
\tag{L-93263.15}
\]

This uses only PNT, not an RH-scale error term.  A square-root convergence rate
for (L-93263.15) would be conclusion-producing: after subtracting
`(log4)/(72s)` in (L-93263.14), every zero with `Re rho>1/2` remains a pole at
`s=rho-1` by (L-93263.10).

Thus the new positive object changes the geometry of the producer but does not
silently make the RH-bearing rate unconditional.

## 6. Log-scale / First-Hermite interface

Put

\[
 \phi(u)=\Phi(e^{-u})\mathbf1_{u\ge0}.
\]

Then `phi>=0`, it decays like `e^{-2u}`, and

\[
 \int_0^\infty e^{-su}\phi(u)\,du=\widehat\Phi(s).
\tag{L-93263.16}
\]

Writing `X=e^y`, the potential is the causal positive convolution

\[
 \mathcal U_\Lambda(e^y)
 =\sum_n{\Lambda(n)\over n}
   \phi(y-\log n).
\tag{L-93263.17}
\]

The Q4 observable is its second `y`-derivative, multiplied by `e^y`.  This is
the exact structural interface with the First-Hermite lane: both are
prime-log convolutions followed by a second-order heat/curvature operation.
The kernels are different, and no transfer of the missing pointwise estimate
is asserted.

## 7. Boundary

```text
positive compact Peano kernel Phi          EXACT
W = x^(-1) D^2 Phi                         EXACT
positive prime potential                   UNCONDITIONAL
PNT limit log(4)/72                        UNCONDITIONAL
square-root convergence rate               OPEN / RH-BEARING
First-Hermite pointwise transfer            OPEN
RH                                          UNPROVED
```
