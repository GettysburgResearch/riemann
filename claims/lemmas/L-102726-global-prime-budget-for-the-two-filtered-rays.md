# L-102726 — The two filtered rays have a globally subcritical native prime budget

Claim ID: `L-102726`  
Status: **PROVED DIRECTED FINITE/ANALYTIC THEOREM**  
Created: 2026-08-22  
Depends on: `L-102725`  
RH status: **not assumed**

Retain the two kernels

\[
K_1=K_{-1},\qquad K_2=K_{-1/2}.
\]

For `K_j(y)>0`, define the labelled native child budget

\[
\mathfrak b_j(y)
=
\sum_{p\le y}p^{-1/2}\frac{K_j(y/p)}{K_j(y)}
+
\mathbf1_{67\le y}67^{-1/2}\frac{K_j(y/67)}{K_j(y)}.
\tag{L-102726.1}
\]

The last term is the second labelled copy of `67`.

Then

\[
\boxed{
\sup_{y>1}\mathfrak b_1(y)<0.874777,
\qquad
\sup_{y\ge1}\mathfrak b_2(y)<0.941359.
}
\tag{L-102726.2}
\]

In particular both budgets are strictly below one.

## 1. Analytic tail

Put

\[
P_*=
\sum_p p^{-3/2}+67^{-3/2}.
\]

Directed summation through `10^5`, followed by the all-integer integral tail,
gives

\[
\boxed{P_*<0.858.}
\tag{L-102726.3}
\]

For `y>=8`, `K_j(y)=c_infty y`.  By `L-102725`,

\[
\mathfrak b_j(y)
\le
P_*+(C_j-1)
\sum_{p>y/8}p^{-3/2},
\]

where

\[
C_1=\frac53,
\qquad C_2=2.
\]

Using

\[
\sum_{n>N}n^{-3/2}<\frac2{\sqrt N}
\]

gives

\[
\mathfrak b_1(y)<0.976
\qquad(y\ge1024),
\]

and

\[
\mathfrak b_2(y)<0.983
\qquad(y\ge2048).
\tag{L-102726.4}
\]

## 2. Finite cells

Below those analytic thresholds the only breakpoints are

\[
1,2,4,8
\quad\text{and}\quad
p,2p,4p,8p.
\]

On each open cell, writing `x=sqrt(y)`, both the numerator and denominator in
(L-102726.1) are quadratic polynomials in `x`.  The derivative numerator is
therefore quadratic, so every cell maximum occurs at an endpoint or at one of
at most two explicitly computable stationary points.

The retained directed replay checks:

```text
z=-1:
  355 cells through 1024;
  3 interior stationary points;
  maximum < 0.874776599;
  maximizing cell 7<y<8.

z=-1/2:
  633 cells through 2048;
  3 interior stationary points;
  maximum < 0.941358299;
  maximizing boundary y=6.
```

No grid inference is used.

## 3. Adjacent-level consequence

Let `E` be the labelled native Euler source, with the two `67` labels kept
distinct.  For fixed `X`, assign to a labelled subset `S`

\[
w_j(S)
=
p_S^{-1/2}K_j(X/p_S).
\]

Pair every odd subset with the even parent obtained by deleting its greatest
label.  For every even parent `B`, (L-102726.2) gives

\[
\sum_{q>\max B}w_j(B\cup\{q\})
< w_j(B).
\]

Hence

\[
\boxed{
\sum_S(-1)^{|S|}w_j(S)\ge0.
}
\tag{L-102726.5}
\]

Passing through the finite active source at each scale gives

\[
\boxed{
\sum_n\frac{\beta(n)}{\sqrt n}K_j(X/n)\ge0
\qquad(X>0,\ j=1,2).
}
\tag{L-102726.6}
\]

This is an exact native-source theorem, not positivity of the kernel alone.