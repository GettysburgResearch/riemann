# L-96102 — Real endpoints and the full Möbius specialization

Claim ID: `L-96102`  
Status: **EXACT COMPOSITION LEMMA CONDITIONAL ONLY ON L-96101**  
Created: 2026-08-16

## 1. Real endpoints

For fixed \(r,j\), every knot of the initial-prime row is an integer product
\(dm\).  Between consecutive knots,

\[
 \mathfrak S_{r,j}(Y)=a\log Y+b.
\]

The global packet decomposition in `L-96101` is endpoint-independent and its
stop-loss evaluation is valid on the whole open cell.  No integer-to-real
interpolation error occurs.

## 2. Full row

Fix \(X\) and \(j\), and let \(R\) contain every prime at most \(X/j\).  Every
squarefree \(k\le X/j\) is a divisor of \(P_R\); every other divisor contributes
zero by triangular support.  Therefore

\[
\boxed{
 c_X(j)=
 \sum_{d\mid P_R}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
}
\tag{L-96102.1}
\]

`L-96101` gives

\[
 \boxed{c_X(j)\ge0.}
\tag{L-96102.2}
\]

No infinite Euler product is exchanged.

## 3. Partial initial segments

If an initial segment stops before all active primes, the omitted Euler factors
can be inverted on triangular support by finite positive geometric series.
Thus full-active positivity and the positive finite inverse recover every
shorter initial segment.  Equivalently, `L-96101` already supplies those
segments directly.
