# R-100610 — Either owner marginal alone permits square-root physical collapse

Claim ID: `R-100610`  
Status: **PROVED EXACT FINITE MATRIX FIREWALL**  
Created: 2026-08-20  
Depends on: `T-100610`  
RH status: **not assumed**

The two estimates in the Schur AND-gate cannot be replaced by either one-sided
estimate alone.

For `N>=1`, let `A_N` be the `N by N` matrix with

\[
(A_N)_{i1}=1
\qquad(1\le i\le N)
\]

and every other entry zero. Every row has absolute sum one, but

\[
\|A_N\|_{2\to2}=\sqrt N
\]

because `A_N e_1` is the all-ones vector. Thus a uniform row Schur bound does
not control the collapse norm.

The transpose matrix has every column absolute sum one while its operator norm
is again `sqrt(N)`. Thus a uniform column Schur bound alone also fails.

These are the matrix versions of the two asymmetric arithmetic no-go modes:

```text
first-owner only:
  many least-owner rows may collapse into one greatest-owner column;

largest-owner only:
  many greatest-owner columns may collapse into one least-owner row.
```

The two-sided Schur estimate removes both multiplicities simultaneously:

\[
\|A\|_{2\to2}
\le
\sqrt{
 \left(\sup_i\sum_j|A_{ij}|\right)
 \left(\sup_j\sum_i|A_{ij}|\right)
}.
\]

Consequently, replacing `FOCR100610 AND LOCR100610` by either marginal alone
would repeat the source-blind square-root loss already exhibited by the
prime-interval collapse fixtures. This refutation is mechanism-specific; it
does not assert that either arithmetic marginal is false.