# L-95504 — The classical zero-free region gives a genuine subexponential SACF improvement

Claim ID: `L-95504`  
Status: **PROVED FROM ONE CLASSICAL IMPORT — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400/L-95401`; the classical zero-free-region bound for the Mertens function  
Scope: unconditional subexponential gain; no fixed power saving and no RH conclusion

## 1. Imported classical estimate

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\]

A classical consequence of the de la Vallée Poussin zero-free region and
Perron contour displacement is that there are absolute constants `c,C>0`
such that

\[
\boxed{
|M(x)|\le Cx\exp\!\bigl(-c\sqrt{\log x}\bigr)
}
\tag{L-95504.1}
\]

for all sufficiently large `x`.  The modern Vinogradov--Korobov region gives a
stronger logarithmic exponent; the weaker form (L-95504.1) is sufficient here.

No zero-density theorem, RH hypothesis or unproved cancellation statement is
imported.

## 2. Odd Mertens state

Put

\[
M_o(x)=\sum_{\substack{n\le x\\n\ \mathrm{odd}}}\mu(n).
\]

Since every nonzero even Möbius coefficient is `mu(2m)=-mu(m)` with `m` odd,

\[
\boxed{M(x)=M_o(x)-M_o(x/2).}
\tag{L-95504.2}
\]

Iteration gives the finite identity

\[
\boxed{M_o(x)=\sum_{j\ge0}M(x/2^j).}
\tag{L-95504.3}
\]

Splitting the sum at `2^j=sqrt(x)` and applying (L-95504.1) to the first part
shows, after changing the constants, that

\[
\boxed{
|M_o(x)|\ll x\exp\!\bigl(-c_1\sqrt{\log x}\bigr)
}
\tag{L-95504.4}
\]

for some absolute `c_1>0`.

## 3. Partial summation through the exact ten bands

Retain PR #580's annular weight

\[
G_X(t)=
\frac{(\log t)J_0(t/X)+(\log2)J_1(t/X)}{\sqrt t},
\qquad X/1024<t\le X.
\tag{L-95504.5}
\]

On each of the ten exact activation bands, `J_0,J_1` are fixed cubics over
`Q(sqrt(2))`.  Hence there are absolute constants `C_0,C_1` such that on every
open band

\[
|G_X(t)|\le C_0\frac{\log(2X)}{\sqrt X},
\qquad
|G_X'(t)|\le C_1\frac{\log(2X)}{X^{3/2}}.
\tag{L-95504.6}
\]

The kernels are continuous at the activation knots.  Applying Stieltjes
partial summation separately on the ten bands, and using (L-95504.4) uniformly
for `X/1024<=t<=X`, gives

\[
\begin{aligned}
|\mathcal A(X)|
&=
\left|\sum_{X/1024<m\le X\atop m\ \mathrm{odd}}
\mu(m)G_X(m)\right|\\
&\ll
\sqrt X\,\log(2X)
\exp\!\bigl(-c_2\sqrt{\log X}\bigr)
\end{aligned}
\tag{L-95504.7}
\]

for some absolute `c_2>0`.

This estimate visibly uses the actual odd Möbius coefficients.  It is not a
source-blind kernel or diagonal bound.

## 4. Consequence for SACF

For `H=log^B(2X)`, PR #580 gives

\[
|\mathcal A(X)|^2
=
\mathcal S_H(X)+O_B(\log^{B+2}(2X)).
\]

Therefore

\[
\boxed{
|\mathcal S_H(X)|
\ll_B
X\log^2(2X)
\exp\!\bigl(-2c_2\sqrt{\log X}\bigr)
+
\log^{B+2}(2X).
}
\tag{L-95504.8}
\]

This is a genuine subexponential improvement over the source-blind
`O(X polylog X)` scale.

It is not a fixed power saving: for every fixed `delta>0`,

\[
\exp(-c\sqrt{\log X})>X^{-\delta}
\]

for all sufficiently large `X`.  Thus (L-95504.8) does not enter the fixed
zero-free-strip regime of `L-95502` and does not imply RH.

## 5. Stronger classical option

Replacing (L-95504.1) by a Vinogradov--Korobov Mertens estimate strengthens
(L-95504.7)--(L-95504.8) by the corresponding

\[
\exp\!\left[-c(\log X)^{3/5}(\log\log X)^{-1/5}\right]
\]

factor.  No part of the Q4 argument changes.

## 6. Boundary

```text
odd-Mertens reduction                         EXACT
partial summation through all ten Q4 bands   COMPLETE
unconditional subexponential SACF gain        PROVED ON CLASSICAL IMPORT
fixed SACF power saving                       NOT PROVED
polylog SACF                                  OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```
