# T-99810 — Active-pair positivity and ratio-67 Möbius-window frontier

Claim ID: `T-99810`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; FINAL WINDOW ESTIMATE OPEN**  
Created: 2026-08-20  
Base: PR #659 canonical scalar spine at `83c17b32a99ac9e1aa5aec3168535550eb286636`  
RH status: **unproved**

This packet attacks the remaining physical-collapse/owner-Carleson frontier without promoting a source-blind energy estimate.

## Proven results

1. `L-99810`: the live min-cut problem admits an exact potential-weighted Cheeger reduction; uniform unweighted Cheeger is false near activation.
2. `L-99811`: every fully deep two-prime cube of the zero-free box potential has fixed favorable mixed sign; every formal failure is activation-local.
3. `L-99813/L-99815`: the **actual weighted two-prime Euler block**

\[
\Phi(y)-p^{-1/2}\Phi(y/p)-q^{-1/2}\Phi(y/q)+(pq)^{-1/2}\Phi(y/(pq))
\]

is strictly positive for every active rough pair `67<=p<q`, `y>=pq`.
4. `L-99814`: on any common deep/collar formula `a+(b+c\log y)y^{-1/2}`, a weighted two-prime block annihilates all nonconstant half-order modes and retains only the positive constant mode.
5. `L-99816`: every fully active top-collar `k`-prime Euler cube is positive for all `k>=1`.
6. `L-99817`: inactive rough primes are exactly silent, so the source is triangular in the endpoint.
7. `L-99818`: one-prime SHARP box Harnack positivity holds globally and the collar action is finite-dimensional/triangular.
8. `L-99819`: after arbitrary prime completion, the sole `u e^{-u/2}` collar coefficient is exactly

\[
-3\sum_{e^u/67<n<=e^u}\mu(n)
\]

on the active squarefree rough source: a plain ratio-67 Möbius-window discrepancy.

## What failed and was repaired

- source-blind physical collapse still costs `sqrt(N)`;
- endpoint moment cancellation does not automatically suppress Poisson off-diagonal correlations;
- uniform unweighted Cheeger fails at thin boundary corners;
- raw parent-only Kraft charging fails by harmonic divergence;
- box potential is not globally unweighted submodular across inactive formal cubes;
- a draft `(2,2,1,0)` regime argument was corrected before being used: that pattern is only a pre-activation left limit, not an active native cube.

## Exact remaining theorem

All new pair/collar identities show that the many-prime activation complexity is carried by the ratio-67 Möbius-window term. The remaining conclusion-producing estimate is a one-sided/subpower logarithmic bound for that window at the exact decorated source scope. Any proof strong enough to give

\[
\int_1^X [\text{window-induced box deficit}]_-\,\frac{dt}{t}=X^{o(1)}
\]

feeds PR #653's zero-free-box/nonnegative-Landau consumer and yields RH.

That final window estimate is **not proved here**. In particular, no source-blind `L^2` or Mertens bound is imported, since such a bound at the required strength would itself carry RH-scale information.

```text
active weighted two-prime positivity       PROVED GLOBALLY
full-deep all-order positivity             PROVED
fully-active top-collar all-order positivity PROVED
inactive-prime triangular reduction        PROVED
one-prime box Harnack                       PROVED
many-prime collar slope = ratio-67 Mertens window PROVED EXACT
remaining one-sided window negative mass   OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
