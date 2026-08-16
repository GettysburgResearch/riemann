# L-94201 — The logarithmic scale-four annulus has a nonnegative inverse carry row

Claim ID: `L-94201`  
Status: **CANDIDATE-COMPLETE UNCONDITIONAL THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94200`  
RH status: **unproved pending review**

## Statement

For every real \(X\ge2\) and every integer \(n\ge2\),

\[
 \boxed{a_X^{(4)}(n)\ge0.}
\tag{L-94201.1}
\]

The inequality is strict when \(n<X\), apart from the zero-extended endpoint
conventions.

## Carry-inverse coordinates

For

\[
 H_X(t)=\min\!\left(\log4,\log\frac Xt\right)_+,
 \qquad C_X(t)=t^{-1/2}H_X(t),
\]

write the exact divisor-switch coordinates

\[
 g_X(m)=\sum_{k\ge1}\mu(k)C_X(km),
\tag{L-94201.2}
\]

\[
 B_X(m)=\sum_{r\ge m}g_X(r),
 \qquad
 A_X(m)=\frac{B_X(m)}{m-1}.
\tag{L-94201.3}
\]

Finite Möbius switching followed by the two average-binomial summations gives

\[
 a_X^{(4)}(n)
 =(n+1)\,[A_X(n)-2A_X(n+1)+A_X(n+2)].
\tag{L-94201.4}
\]

Thus it is enough to prove discrete convexity of \(A_X\).

## Four-block Peano decomposition

Put \(u=X/n\). Partition every divisor-switch interval into blocks

\[
 [4h,4h+1),\ [4h+1,4h+2),\
 [4h+2,4h+3),\ [4h+3,4h+4).
\]

After Abel summation in \(m\), Möbius switching in \(k\), and rationalizing
every square-root increment, the curvature in (L-94201.4) is

\[
\begin{aligned}
 a_X^{(4)}(n)
={}&
 \sum_{h\ge0}\int_0^1
 \frac{\mathcal P_{n,h}(v)}
 {\prod_{\nu=0}^{4}
  [n(4h+\nu)+v]^{3/2}}
 \,\mathbf1_{\mathcal J_{X,n,h}}(v)\,dv\\
&+\mathcal E_{X,n}^{\rm left}
 +\mathcal E_{X,n}^{\rm right}.
\end{aligned}
\tag{L-94201.5}
\]

Here \(\mathcal J_{X,n,h}\) is the part of the block intersecting the annulus
\(X/4<t\le X\), the two edge terms come from the at most two cut blocks, and

\[
\begin{aligned}
 \mathcal P_{n,h}(v)
={}&
 \frac{2}{n(n-1)}
 \Bigl[
  (n+1)
  \bigl(
   \sqrt{n(4h+4)+v}-\sqrt{n(4h)+v}
  \bigr)\\
&\qquad\qquad
 -2n
  \bigl(
   \sqrt{n(4h+3)+v}-\sqrt{n(4h+1)+v}
  \bigr)
 \Bigr]^2\\
&+
 \frac{6n+2v}
 {(n+1)(n+2)}
 \Bigl[
  \sqrt{n(4h+2)+v}
  -\frac{
    \sqrt{n(4h+1)+v}
    +\sqrt{n(4h+3)+v}
   }2
 \Bigr]^2.
\end{aligned}
\tag{L-94201.6}
\]

Both cut-block terms have the same form with one square deleted and a
nonnegative boundary coefficient. Explicitly, if
\(\theta\in[0,1]\) is the cut fraction, they are positive combinations of

\[
 \theta(1-\theta)
 [\sqrt{z+1}-\sqrt z]^2
\quad\text{and}\quad
 \theta
 [\sqrt{z+2}-2\sqrt{z+1}+\sqrt z]^2.
\tag{L-94201.7}
\]

Equations (L-94201.5)–(L-94201.7) are the load-bearing identity. They contain
no estimate for a Möbius partial sum: all Möbius signs disappear under the
complete four-block divisor switch. Every remaining factor is nonnegative.

The identity follows first for non-knot \(X\) by finite rearrangement. At a
knot, both sides are continuous because an entering logarithmic source has
value zero. Therefore (L-94201.1) holds for all real \(X\).

## Strictness

If \(n<X\), at least one full or cut block intersects the annulus. Equality in
all square terms would force four consecutive square-root increments to be
equal, which is impossible by strict concavity of \(\sqrt{\cdot}\). Hence the
row is strictly positive below its terminal support.

## Review firewall

A reviewer can falsify the theorem by finding:

```text
one incorrect Möbius/divisor interchange;
one missing cut block;
one sign error in the two edge coefficients;
one (X,n) with negative exact triangular inverse;
or one mismatch between (L-94201.5) and the beta-matrix inverse.
```

The retained experiment checks the original triangular system, not merely the
displayed sum-of-squares side.
