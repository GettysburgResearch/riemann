# L-97702 - The annular 5:3 scalar is an exact four-band critical Möbius boundary

Claim ID: `L-97702`  
Status: **PROVED EXACT FINITE-SUM / STIELTJES IDENTITY**  
Created: 2026-08-18  
Depends on: the sparse 5:3 scalar dictionary from PR #557 and the annular consumer of PR #547  
RH status: **not assumed**

For `Y>0` and `n>=1`, define the scale-four hinge

\[
H_Y(n)=\min\!\left(\log4,\log\frac Yn\right)_+.
\tag{L-97702.1}
\]

The unique scalar

\[
R_X=5c_X(2)+3c_X(3)
\]

has the exact coefficient dictionary

\[
a_*(n)=6\mathbf1_{n=1}-6\mu(n)
+9\mathbf1_{2\mid n}\mu(n/2)
-3\mathbf1_{4\mid n}\mu(n/4).
\tag{L-97702.2}
\]

Its annular difference is

\[
\mathcal A_X=R_X-R_{X/4}
=\sum_{n\ge1}\frac{a_*(n)}{\sqrt n}H_X(n).
\tag{L-97702.3}
\]

Define

\[
\kappa_X(n)=
-6H_X(n)+\frac9{\sqrt2}H_{X/2}(n)-\frac32H_{X/4}(n).
\tag{L-97702.4}
\]

Then

\[
\boxed{
\mathcal A_X=6H_X(1)+\mathfrak C_X,
\qquad
\mathfrak C_X=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}\kappa_X(n).
}
\tag{L-97702.5}
\]

## Proof of the sparse identity

Since `H_(X/2)(m)=H_X(2m)` and `H_(X/4)(m)=H_X(4m)`, the three terms in
`mathfrak C_X` contribute respectively

```text
-6 mu(m)     to H_X(m)/sqrt(m),
+9 mu(m)     to H_X(2m)/sqrt(2m),
-3 mu(m)     to H_X(4m)/sqrt(4m).
```

Together with the boundary atom `6 H_X(1)`, this is exactly (L-97702.2).
All sums are finite because the hinges vanish beyond their endpoints.

## Four-band form

Put

\[
B_{1/2}(t)=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\tag{L-97702.6}
\]

For every `Y>0`, finite Fubini gives

\[
\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}H_Y(n)
=
\int_{Y/4}^{Y}B_{1/2}(t)\,\frac{dt}{t}.
\tag{L-97702.7}
\]

Indeed,

\[
H_Y(n)=\int_{Y/4}^{Y}\mathbf1_{n\le t}\frac{dt}{t}.
\]

Substituting (L-97702.7) into (L-97702.5) and splitting at
`X/16,X/8,X/4,X/2,X` yields

\[
\boxed{
\begin{aligned}
\mathfrak C_X={}&
-\frac32\int_{X/16}^{X/8}B_{1/2}(t)\frac{dt}{t}\\
&+\frac{9\sqrt2-3}{2}
 \int_{X/8}^{X/4}B_{1/2}(t)\frac{dt}{t}\\
&+\frac{9\sqrt2-12}{2}
 \int_{X/4}^{X/2}B_{1/2}(t)\frac{dt}{t}\\
&-6\int_{X/2}^{X}B_{1/2}(t)\frac{dt}{t}.
\end{aligned}}
\tag{L-97702.8}
\]

No estimate has entered: (L-97702.8) is an exact identity for every real `X>0`.

## The exact sign target

Define `C4MBI67(X)` by

\[
\boxed{
\mathfrak C_X\ge-6H_X(1).
}
\tag{L-97702.9}
\]

Then, pointwise in `X`,

\[
\boxed{
\mathrm{C4MBI67}(X)
\iff \mathcal A_X\ge0.
}
\tag{L-97702.10}
\]

For `X>=4`, `H_X(1)=log 4`, so the threshold is `-6 log 4`.  The theorem does
not prove (L-97702.9); it identifies the exact critical four-band inequality.
