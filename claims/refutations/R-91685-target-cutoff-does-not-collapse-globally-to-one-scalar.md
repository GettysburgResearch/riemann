# R-91685 — The causal target cutoff does not globally collapse to one scalar

Claim ID: `R-91685`  
Status: **EXACT SCOPE CORRECTION / ALGEBRAIC COUNTEREXAMPLE**  
Created: 2026-08-14  
Depends on: the causal target atom of `L-91348/L-91682`  
RH status: **unproved**

## 1. The tempting but false collapse

Write

\[
 p=s^2,
 \qquad
 y=u^2,
 \qquad
 A=su=\sqrt{py}.
\]

Inside the child-active regime `d<=y`, the causal target atom is

\[
 K_T(d)
 =(1-s^{-1})
 \left[
  \frac{4u(s+1)}d-\frac3{\sqrt d}
 \right].
\tag{R-91685.1}
\]

Because the prefactor is common, it is tempting to conclude that all target
cutoffs depend only on

\[
 \sigma=u(s+1).
\]

That conclusion is false globally. For `d>y` the child term is inactive and

\[
 K_T(d)=\frac{4A}{d}-\frac3{\sqrt d},
\tag{R-91685.2}
\]

so crossing `d=y` changes the formula.

## 2. Exact same-`sigma` counterexample

Let `a=sqrt(67)` and compare

\[
 (p_1,y_1)=(67,4)
\]

with

\[
 (p_2,y_2)=((2a+1)^2,1).
\]

Both have the same proposed scalar:

\[
 \sqrt{y_1}(\sqrt{p_1}+1)
 =2(a+1)
 =\sqrt{y_2}(\sqrt{p_2}+1).
\tag{R-91685.3}
\]

At `d=2`, however, the first packet is child-active and the second is
child-inactive. Direct simplification gives

\[
\boxed{
 K_T(2;p_2,y_2)-K_T(2;p_1,y_1)
 =2+\frac4{\sqrt{67}}-\frac3{\sqrt{134}}>0.
}
\tag{R-91685.4}
\]

The sign is exact: `2>3/sqrt(134)` because `4*134>9`, and
`4/sqrt(67)>0`.

Thus equal `sigma` does not imply equal target atoms or equal Target-Lorenz
cutoffs.

## 3. Correct two-variable cell form

The globally valid formula is

\[
\boxed{
 K_T(d)
 =\frac{4A}{d}-\frac3{\sqrt d}
 -\mathbf1_{d\le u^2}\frac{u}{A}
  \left(\frac{4u}{d}-\frac3{\sqrt d}\right).
}
\tag{R-91685.5}
\]

Multiplying by the positive `A` gives

\[
\boxed{
 A K_T(d)
 =\frac{4A^2}{d}-\frac{3A}{\sqrt d}
 -\mathbf1_{d\le u^2}
  \left(\frac{4u^2}{d}-\frac{3u}{\sqrt d}\right).
}
\tag{R-91685.6}
\]

On a fixed child-activation cell the indicator set is fixed. Every cumulative
target inequality defining a cutoff is then a quadratic expression in `A`,
with algebraic-affine dependence on `u`. This is the correct finite
semi-algebraic reduction.

For component rows, after also fixing the parent and child quotient activation
cells,

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N}
\]

makes every Lorenz margin an explicit algebraic-logarithmic cell function in
`A` and `u`. A directed proof may partition these cells, but it may not replace
them globally by one `sigma` variable.

## 4. Boundary

```text
inner-regime scalar factorization             EXACT
one global scalar cutoff parameter            FALSE
same-sigma counterexample                     EXACT
correct (A,u) semi-algebraic target cells      EXACT
all arithmetic row-cell signs                 OPEN
Riemann Hypothesis                            UNPROVEN
```
