# L-98921 — Logarithmic-owner martingale gives an exact prefix Volterra equation

Claim ID: `L-98921`  
Status: **PROVED EXACT FINITE IDENTITY**  
Created: 2026-08-19  
Depends on: `L-97101/L-97102`, `L-98920`  
RH status: **not assumed**

Put

\[
 c(n)=\frac{b_\diamond(n)}{\sqrt n},
 \qquad
 \mathcal B(x)=\sum_{n\le x}c(n).
\]

The logarithmic-derivative identity from `L-97101` is

\[
 b_\diamond(n)\log n
 =-\sum_{\substack{d\mid n\\d>1}}
   \Lambda_\diamond(d)b_\diamond(n/d).
\]

Dividing by `sqrt(n)` and summing over `n<=x` gives, by finite divisor switching,

\[
\sum_{n\le x}c(n)\log n
 =-\sum_{2\le d\le x}\frac{\Lambda_\diamond(d)}{\sqrt d}
  \mathcal B(x/d).
\tag{L-98921.1}
\]

Abel summation gives exactly

\[
\sum_{n\le x}c(n)\log n
 =\mathcal B(x)\log x-\int_1^x\mathcal B(t)\frac{dt}{t}.
\tag{L-98921.2}
\]

Therefore

\[
\boxed{
\mathcal B(x)\log x
 =\int_1^x\mathcal B(t)\frac{dt}{t}
 -\sum_{2\le d\le x}\frac{\Lambda_\diamond(d)}{\sqrt d}
  \mathcal B(x/d).
}
\tag{L-98921.3}
\]

The second term is the prefix form of the exact alternating divisor martingale.
Its source-level owner weights are probability weights only before the prefix
sum is collapsed. Hence any successful energy argument must retain the source
index (or an equivalent conditional expectation) until after the martingale
quadratic variation is estimated.

This identity explains why a source-blind positive renewal norm diverges at RH
scale while the source-level martingale still has logarithmic energy.
