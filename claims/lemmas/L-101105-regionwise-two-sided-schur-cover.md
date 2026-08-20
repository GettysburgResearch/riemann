# L-101105 — Regionwise two-sided Schur cover turns different producer lanes into one lossless matrix estimate

Claim ID: `L-101105`  
Status: **PROVED EXACT CONJUNCTIVE MATRIX THEOREM**  
Created: 2026-08-20  
Depends on: PR #691 `T-100610--T-100611`, `L-100614`  
RH status: **not assumed**

Let the centered long-interval matrix of PR #691 be

\[
\widetilde A(X)=\bigl(\widetilde A_{ij}(X)\bigr)_{i<j},
\]

with endpoint survival vectors `a,b` satisfying

\[
\|a\|_2\le1,
\qquad
\|b\|_2\le1.
\]

The complete centered-cubic negative part is bounded by

\[
(F(X))_-\le |a^*\widetilde A(X)b|.
\tag{L-101105.1}
\]

Let

\[
\widetilde A=\sum_{\nu\in\mathfrak P}\widetilde A^{(\nu)}
\tag{L-101105.2}
\]

be any **source-owned disjoint partition of its entries**.  A region may be a
prime-ratio band, an activation side, a smooth/rough class, a finite-squaring
class, or a divisor-renewal class, but every matrix entry must occur exactly
once.

For each region define

\[
R_\nu(X)=\sup_i\sum_j|\widetilde A_{ij}^{(\nu)}(X)|,
\qquad
C_\nu(X)=\sup_j\sum_i|\widetilde A_{ij}^{(\nu)}(X)|.
\tag{L-101105.3}
\]

The two-sided Schur test and the triangle inequality give the pointwise bound

\[
\boxed{
(F(X))_-
\le
\sum_{\nu\in\mathfrak P}
\sqrt{R_\nu(X)C_\nu(X)}.
}
\tag{L-101105.4}
\]

Consequently, with logarithmic measure `dX/X`,

\[
\boxed{
\int_1^Y(F(X))_-\frac{dX}{X}
\le
\sum_{\nu\in\mathfrak P}
\left(\int_1^YR_\nu(X)\frac{dX}{X}\right)^{1/2}
\left(\int_1^YC_\nu(X)\frac{dX}{X}\right)^{1/2}.
}
\tag{L-101105.5}
\]

This is stronger as an implication-matrix interface than requiring one global
first-owner estimate and one global largest-owner estimate.  Different regions
may use different theorem pairs:

```text
short intervals:       signed unconditionally by L-100613;
smooth/deep regions:   removed by the proved smooth/deep estimates;
finite-squared region: row side from adaptive squaring;
divisor-exposed region: column side from positive renewal;
endpoint collar:       activation/coarea or phase/wavelet estimate.
```

For a finite or subpower-sized partition, the regional product conditions

\[
\left(\int_1^YR_\nu\frac{dX}{X}\right)
\left(\int_1^YC_\nu\frac{dX}{X}\right)
=Y^{o(1)}
\tag{L-101105.6}
\]

for every surviving region imply subpower negative mass and hence RH through
the centered-cubic detector.

Neither marginal is dispensable in a surviving region: one-column and one-row
matrices show that one-sided Schur control alone permits a square-root collapse
loss.  The theorem therefore gives genuine AND-hyperedges, not aliases for a
single scalar conjecture.
