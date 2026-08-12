# R-91003 — Positive Jordan coefficients and unweighted Cauchy mass do not close RH

Claim ID: `R-91003`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-11  
Depends on: `L-91009`, `L-91011`  
RH status: **unproved**

Two attractive shortcuts are invalid.

## 1. Positive Euler coefficients live in the wrong half-plane

The shift ratio

\[
 \frac{\zeta(s-a)}{\zeta(s+a)}
 =
 \sum_{n\ge1}
 \frac{J_{2a}(n)}{n^{a+s}}
\]

has strictly positive coefficients, but the series is directly valid only for

\[
 \Re s>1+a.
\]

The completed Clark boundary is \(\Re s=1/2\). Positivity of the coefficients
does not transfer Schur, Pick, or radial-monotonicity structure across that
analytic-continuation gap. Any such transfer would already exclude the
reciprocal-zeta poles and is RH-bearing.

## 2. The unweighted centre mass counts off-line pairs positively

For the soft count, a line zero contributes total mass

\[
 \frac{\pi a}{2},
\]

while one reflected pair of depth \(d<a\) contributes

\[
 \pi a.
\]

Thus the unweighted centre integral counts the two zeros of an off-line pair
with exactly the same total mass as two line zeros. It cannot distinguish RH
from false RH.

The conclusion-producing information lies in:

```text
pointwise monotonicity in a;
signed or frequency-resolved centre localisation;
the exact depth-square moment defect;
or a nonlinear Pick/signature statistic.
```

Neither coefficientwise positivity nor unweighted averaging supplies the
missing theorem.
