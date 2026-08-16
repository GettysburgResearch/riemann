# L-94201 — The full native Möbius component row is coefficientwise nonnegative

Claim ID: `L-94201`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94200`; the exact native row definition  
RH status: **not assumed**

## 1. Full row

For real \(X\ge1\) and integer \(j\ge2\), define
\[
 c_X(j)
 =\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
 \tag{L-94201.1}
\]

Let
\[
 z=\frac Xj
\]
and let \(P(z)\) be the product of the primes at most \(z\), with the empty
product interpreted as one.

Every \(k\) with \(\mu(k)\ne0\) and \(k\le z\) is a squarefree divisor of
\(P(z)\). Conversely, if \(d\mid P(z)\) but \(d>z\), then
\[
 Q_{X/d}(j)=0
\]
by triangular support. Hence
\[
 \boxed{
 c_X(j)
 =\sum_{d\mid P(z)}
   \frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
 }
 \tag{L-94201.2}
\]

## 2. Positivity

Apply `L-94200` to the initial prime segment \(p\le z\). It gives
\[
 \sum_{d\mid P(z)}
 \frac{\mu(d)}{\sqrt d}Q_{X/d}(j)\ge0.
\]
Therefore
\[
 \boxed{c_X(j)\ge0}
 \qquad(X\ge1,\ j\ge2).
 \tag{L-94201.3}
\]

The support is triangular:
\[
 c_X(j)=0\qquad(j\ge X),
\]
and `L-94200` gives strict positivity for \(2\le j<X\).

Thus the full native row
\[
 c_X=(c_X(j))_{j\ge2}
\]
is a finite nonnegative physical row at every real endpoint.

## 3. Why no limiting Euler product is hidden

Equation (L-94201.2) is a finite identity. The apparent full Möbius sum already
terminates at \(X/j\); adjoining all primes up to \(X/j\) adds only divisor
terms whose component row is zero beyond triangular support.

There is no exchange of an infinite Euler product, no analytic continuation,
and no use of a zero-free region.

## 4. Exact source formula

The canonical seed can also be written
\[
 d_X^\star(t)
 =\sum_{k\le X/t}\frac{\mu(k)}{\sqrt{kt}}
   \log\frac{X}{kt},
\]
\[
 b_X^\star(n)=\sum_{t=n}^{\lfloor X\rfloor}d_X^\star(t),
\]
\[
 c_X(j)
 =(j+1)\left[
 \frac{b_X^\star(j)}{j-1}
 -\frac{2b_X^\star(j+1)}j
 +\frac{b_X^\star(j+2)}{j+1}
 \right].
 \tag{L-94201.4}
\]

The theorem proves positivity of the row after the complete Möbius cancellation.
It does not assert positivity of each oriented Möbius child or of the seed
\(d_X^\star(t)\) separately.

## 5. Boundary

```text
full Möbius sum = finite initial-prime Euler sum      exact
componentwise sign c_X(j)>=0                          proposed complete
strict interior sign                                 proposed complete
branchwise oriented-child positivity                 not claimed
Target-Lorenz leaf transport                          not used
Riemann Hypothesis                                    not assumed
```
