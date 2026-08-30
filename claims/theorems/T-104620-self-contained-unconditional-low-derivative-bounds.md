# T-104620 — Self-contained unconditional low-derivative line bounds

Claim ID: `T-104620`  
Status: **UNCONDITIONAL RECONSTRUCTION WITH EXACT FINITE CERTIFICATES**  
Created: 2026-08-26  
Depends on: `L-104602`, `L-104603`, `X-104620`  
RH status: **unproved**

The reconstructed Conrey functional and the four exact rational certificates
give

\[
\boxed{
\alpha_0>\frac3{10},
\qquad
\alpha_1>\frac45,
\qquad
\alpha_2>\frac{37}{40},
\qquad
\alpha_3>\frac{24}{25}.
}
\tag{T-104620.1}
\]

These are unconditional critical-line lower bounds for the first four fixed
derivative orders.

## 1. What is genuinely reconstructed

```text
admissibility conditions                  RECONSTRUCTED
two weighted polynomial quadratic forms   RECONSTRUCTED
Euler--Lagrange mollifier minimization     RECONSTRUCTED
finite variational functional              RECONSTRUCTED
four explicit certificates                 PROVED EXACT
transcendental comparisons                  PROVED BY RATIONAL INTERVALS
```

## 2. What this theorem does not claim

- It does not reproduce Conrey's optimized published table.
- It does not improve the known numerical records.
- It does not derive the second-derivative bound from the third-derivative
  proportion.
- It does not validate the previously advertised `98.73% -> 92.18%`
  adjacent-companion argument.
- It does not prove RH.

## 3. Next unconditional optimization problem

Use the admissible rational family

\[
\phi(x)=1-x+\sum_{j=1}^{d}a_jx(1-x)(1-2x)^{2j-1}
\]

and rational `R`. For each fixed degree the functional is an explicitly
certifiable finite-dimensional problem.

The next target is to reproduce the published values

\[
0.3658,\quad0.8137,\quad0.9584,\quad0.9873
\]

from frozen rational coefficients, and then test higher degree without changing
the analytic theorem. Any claimed improvement must be accompanied by a complete
`Fraction` certificate and a source lock to the exact primary theorem.
