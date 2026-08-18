# L-97903 — The complete cube through `(log X)^2 log log X` is positive

Claim ID: `L-97903`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: the sharp `P_61` annular asymptotic; classical PNT and Mertens theorems  
RH status: **not assumed**

Let

\[
 Z_X=(\log X)^2\log\log X
 \tag{L-97903.1}
\]

and let

\[
 Q_Z=\prod_{67\le p\le Z_X}p.
\]

Define

\[
 \mathcal B_Z(X)=
 \sum_{d\mid Q_Z}\frac{\mu(d)}{\sqrt d}b(X/d),
 \qquad
 U_Z(X)=\frac{\mathcal B_Z(X)}{\sqrt X},
 \tag{L-97903.2}
\]

with zero extension below activation. Then

\[
 \boxed{
 U_Z(X)=a_*\prod_{67\le p\le Z_X}\left(1-\frac1p\right)
 +o\!\left(\frac1{\log Z_X}\right)>0
 }
 \tag{L-97903.3}
\]

for every sufficiently large `X`. Consequently

\[
 U_Z(X)\asymp\frac1{\log\log X}.
 \tag{L-97903.4}
\]

This extends `L-97900`: the full primorial is now much larger than `X`, so the
proof must control the activated divisor tail rather than demand uniform
activation of every divisor.

## Proof

Choose

\[
 L_X=(\log X)^{10},
 \qquad
 D_X=X/L_X.
 \tag{L-97903.5}
\]

For `d<=D_X`, the child endpoint is at least `L_X`, and the sharp annular
asymptotic gives

\[
 b(X/d)=a_*\sqrt{X/d}+c_*+O((X/d)^{-3/2}).
 \tag{L-97903.6}
\]

The complete normalized sum differs from the full square-root Euler product by
four errors.

### 1. Activated main-term tail

For `d>D_X`,

\[
 d^{-1}\le D_X^{-1/2}d^{-1/2}.
\]

Hence

\[
 \sum_{d\mid Q_Z\atop d>D_X}\frac1d
 \le D_X^{-1/2}
 \prod_{67\le p\le Z_X}(1+p^{-1/2}).
 \tag{L-97903.7}
\]

The PNT and partial summation give

\[
 \log\prod_{p\le Z_X}(1+p^{-1/2})
 \le(2+o(1))\frac{\sqrt{Z_X}}{\log Z_X}
 =o(\log X).
 \tag{L-97903.8}
\]

Indeed the right side is asymptotic to
`log(X)/sqrt(log log X)`. Thus (L-97903.7) is `X^{-1/2+o(1)}`.
The actual normalized contribution of every `d>D_X` is bounded by the same
quantity, because `0<=b(Y)<=C sqrt(Y)`.

### 2. Constant term

The complete unsigned constant contribution is at most

\[
 \frac{|c_*|}{\sqrt X}
 \prod_{67\le p\le Z_X}(1+p^{-1/2})
 =X^{-1/2+o(1)}.
 \tag{L-97903.9}
\]

No sign of the constant Euler product is used.

### 3. Asymptotic remainder on `d<=D_X`

After normalization by `sqrt(X)`, the remainder in (L-97903.6) contributes

\[
 O\!\left(X^{-2}\sum_{d\le D_X}d\right)
 =O(L_X^{-2}),
 \tag{L-97903.10}
\]

because the divisors form a subset of the positive integers.

### 4. The positive main product

Mertens' theorem gives

\[
 \prod_{67\le p\le Z_X}(1-p^{-1})
 \asymp\frac1{\log Z_X}.
 \tag{L-97903.11}
\]

Every error above is `o(1/log Z_X)`. Substituting
(L-97903.6) in the activated range and comparing the truncated main sum with
the full product therefore proves (L-97903.3).

## Sharp scope of the elementary argument

The estimate uses the half-weight product

\[
 \prod_{p\le Z}(1+p^{-1/2}).
\]

It remains negligible after division by `sqrt(X)` throughout the stated range.
Pushing `Z` to approximately `(log X)^2(log log X)^2` makes this elementary
unsigned control critical. A further extension must cancel the constant/tail
source structurally rather than enlarge the same absolute bound.