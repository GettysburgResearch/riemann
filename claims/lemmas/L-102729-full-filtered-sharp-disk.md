# L-102729 — The signed dyadic filter preserves one full SHARP disk

Claim ID: `L-102729`  
Status: **PROVED EXACT CARRIER THEOREM + DIRECTED PRIME-BUDGET CERTIFICATE**  
Created: 2026-08-23  
Depends on: `L-102725--L-102728`; PR #690 active SHARP positivity  
RH status: **not assumed**

Put

\[
 S_-(y)=4(\sqrt y-1)\mathbf1_{y\ge1},
 \qquad
 P_2=(I-\sqrt2S_2)(I-S_2)^2.
\]

Write

\[
 z=-1+w,
 \qquad |w|\le\frac12,
\]

and define the filtered carrier

\[
 \boxed{
 K_w(y)=P_2\,|S_-(y)+w|^2.
 }
 \tag{L-102729.1}
\]

The three rays of `L-102728` are the real points

\[
 w=-\frac12,\quad0,\quad\frac12.
\]

This theorem proves the whole closed disk, including complex shifts.

## 1. Exact carrier geometry

Let `x=sqrt(y)` and write

\[
 K_w(y)=C(x)+2B(x)\Re w+A(x)|w|^2.
\]

On the four activation cells the coefficients are:

### Cell `1<=y<2`

\[
 A=1,
 \qquad B=4(x-1),
 \qquad C=16(x-1)^2=B^2.
 \tag{L-102729.2}
\]

Thus

\[
 K_w(y)=|4(x-1)+w|^2\ge0.
\]

### Cell `2<=y<4`

\[
 A=-(1+\sqrt2),
\]

\[
 B=-4(\sqrt2x-\sqrt2-1),
\]

\[
 C=-8(\sqrt2x^2-4\sqrt2x+2+2\sqrt2).
 \tag{L-102729.3}
\]

Here `A<0`, so the minimum over the disk occurs on its boundary. Since `B` is
real, the boundary minimizer is one of the two real endpoints
`w=+-1/2`. Those are exactly the already-certified filtered rays
`z=-3/2` and `z=-1/2`.

### Cell `4<=y<8`

\[
 A=\sqrt2,
 \qquad B=2(x-2\sqrt2),
\]

\[
 C=4(x^2-4x+4\sqrt2).
 \tag{L-102729.4}
\]

If the unconstrained minimizer `w=-B/A` lies inside the disk, then

\[
 \boxed{
 C-\frac{B^2}{A}
 =2(2-\sqrt2)x^2>0.
 }
 \tag{L-102729.5}
\]

Otherwise the disk minimum is again attained at one of the two real boundary
rays.

### Cell `y>=8`

All four dilates are active and the constant and square-root modes cancel:

\[
 \boxed{
 A=B=0,
 \qquad
 C=2(2-\sqrt2)y>0.
 }
 \tag{L-102729.6}
\]

Consequently

\[
 \boxed{
 K_w(y)\ge0
 \qquad(y>0,\ |w|\le1/2).
 }
 \tag{L-102729.7}
\]

## 2. Uniform prime-removal budget

For a complete labelled native source, including the second labelled copy of
`67`, define

\[
 \mathfrak b_w(y)
 =
 \sum_{p\le y}p^{-1/2}\frac{K_w(y/p)}{K_w(y)}
 +\mathbf1_{67\le y}67^{-1/2}\frac{K_w(y/67)}{K_w(y)}.
 \tag{L-102729.8}
\]

At a zero of the denominator the ratio is interpreted by the continuous
adjacent-level limit.

The retained directed cell certificate proves simultaneously for the entire
disk

\[
 \boxed{
 \mathfrak b_w(y)\le0.942<1
 \qquad(1\le y\le2048).
 }
 \tag{L-102729.9}
\]

It checks `633` activation cells and all boundary/interior stationary points of
the disk minimum.

For the analytic tail, put

\[
 c=2(2-\sqrt2).
\]

Equation (L-102729.6) gives `K_w(y)=cy` for `y>=8`, while the exact cell
calculation gives

\[
 0\le K_w(t)\le2ct
 \qquad(1\le t\le8,\ |w|\le1/2).
 \tag{L-102729.10}
\]

The directed prime ledger gives

\[
 \sum_p p^{-3/2}+67^{-3/2}<0.858.
\]

For `y>=2048`, only primes `p>y/8` can pay the factor-two boundary excess, so

\[
 \mathfrak b_w(y)
 <0.858+
 \sum_{p>y/8}p^{-3/2}
 <0.858+\frac2{\sqrt{256}}
 <0.983.
 \tag{L-102729.11}
\]

Thus

\[
 \boxed{
 \sup_{y>0,\ |w|\le1/2}\mathfrak b_w(y)<1.
 }
 \tag{L-102729.12}
\]

## 3. Native and tangent consequences

Adjacent-level pairing now gives, for the literal duplicate-`67` native source,

\[
 \boxed{
 P_2Q_{\rm native,-1+w}(X)\ge0
 \qquad(|w|\le1/2).
 }
 \tag{L-102729.13}
\]

The completion tangent is a nonnegative linear combination of multiplicative
shifts of the same native source. Therefore, for every completion time `tau`,

\[
 \boxed{
 P_2Q_{\tau,-1+w}(X)\ge0,
 \qquad
 JP_2Q_{\tau,-1+w}(X)\ge0
 }
 \tag{L-102729.14}
\]

for all `X>0` and every complex `w` with `|w|<=1/2`.

This is the first exact transport of a full Hermitian test-vector disk through
the signed compact filter. It does not by itself orient the final Lorentz
functional; that scope is fixed in `R-102722`.