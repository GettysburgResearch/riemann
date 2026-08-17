# T-93290 — The actual `LPTRP_23` rows are positive through one hundred million

Claim ID: `T-93290`  
Status: **PROVED FINITE UNCONDITIONAL THEOREM / EXACT DIRECTED CERTIFICATE**  
Created: 2026-08-18  
Depends on: `L-93290`; `X-93290`  
RH status: **unproved**

Let `a_2,a_3^sharp` be the actual large-prime-filtered coefficient sequences
of (R-93290.4)--(R-93290.5). Then for every integer

\[
 2\le N\le10^8,
\]

\[
\boxed{
 A_2(N)>2.12132034355964257,
}
\tag{T-93290.1}
\]

and for every

\[
 3\le N\le10^8,
\]

\[
\boxed{
 \frac13A_3^\sharp(N)>0.82136720504591819.
}
\tag{T-93290.2}
\]

The certified minima occur at `N=2` and `N=4`, respectively. Therefore, by
`L-93290`,

\[
\boxed{
 c_X^{>3}(2)>0\quad(X>2),
\qquad
 c_X^{>3}(3)>0\quad(X>3)
}
\tag{T-93290.3}
\]

for every real

\[
 1\le X<100000001.
\tag{T-93290.4}
\]

The triangular boundary values are zero.

## Exact certificate arithmetic

Set

\[
 Q=10^{18},
\qquad
 L_Q(n)=\left\lfloor\frac Q{\sqrt n}\right\rfloor.
\tag{T-93290.5}
\]

The verifier computes `L_Q(n)` from a floating seed but then adjusts it until
the two exact unsigned-128-bit inequalities

\[
 L_Q(n)^2n\le Q^2<(L_Q(n)+1)^2n
\tag{T-93290.6}
\]

hold. No correctness property of `sqrt`, the hardware rounding mode, or the C
library is used after that adjustment.

For an integer coefficient `b`, the certified lower contribution is

\[
 \frac{bL_Q(n)}Q\quad(b\ge0),
\qquad
 \frac{b(L_Q(n)+1)}Q\quad(b<0).
\tag{T-93290.7}
\]

All cumulative sums are exact signed 128-bit integers. The retained minimum
scaled integers are

```text
row 2:
2121320343559642572

three times row 3:
2464101615137754582
```

and the checker tests `200,000,000` exact coefficient coordinates.

This is a finite theorem, not an asymptotic proof. It advances the actual
producer by a factor greater than `333` beyond PR #546's surrogate scan and,
more importantly, covers the correct Euler-filtered rows and every real
activation cell. It does not establish eventual positivity or RH.
