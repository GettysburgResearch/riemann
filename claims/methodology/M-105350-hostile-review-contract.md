# M-105350 — Hostile review contract for the one-anchor Stieltjes boundary reduction

Claim ID: `M-105350`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

## Review order

1. Verify the normalization

   \[\
   m_n=H^{()n+1)}(x_*)/(n+1)!
   \]

   by expanding `(H(x)-H(y))/(x-y)` at the diagonal.
2. Check that positivity of every `mathsf L_k` is exactly positivity of the
   Hamburger functional on every polynomial square.
3. Check the compact-support step: only the even moments are used, and their
   Cauchy growth must exclude mass outside one finite interval.
4. Verify

   \[
   \operatorname{Im}{z-x_*\over1-t(z-x_*)}
   ={\operatorname{Im}z\over|1|[|1-t(z-x_*)|}^2}.
   \]

5. Check that the identity theorem is applied on a connected upper
   neighbourhood and that real packet matrices are obtained by closed-cone
   limits.
6. Verify the parity split and the Stieltjes pushforward `s=t^2`.
7. Replay the exact rational positive and signed-atom fixtures.
8. Review `T-105350` only as an exact equivalence/reduction; no Xi sign is
   claimed.

## Load-bearing distinctions

```text
one anchor + all orders          SUFFICIENT AND NECESSARY;
one anchor + bounded orders      NOT SUFFICIENT;
all leading determinants only    NOT USED IN THE SEMIDEFINITE CASE;
full matrices PSD                NORMATIVE;
raw F/F' safe-axis function     NOT THE BOUNDARY H SAFE-AXIS FUNCTION;
actual-Xi order-three Pick       NOT AN IMPORT WITHOUT AN EXACT MAP.
```

In the singular semidefinite case, nonnegative leading determinants alone are
not silently substituted for matrix PSD. A scalar version may use all
coefficients of `det(tI+mathsf L_k)` or all principal minors, but the present
statement keeps the exact matrix condition.

## Xi boundary function

The theorem applies to

\[
H_{F,\Omega}(z)
={1\over2pi i}\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta,
\]

not directly to `F/F'`. Interior critical poles have already been separated
by the parent Cauchy--Mittag-Leffler decomposition. Any safe-axis proof must
retain that subtraction and the exact window/exhaustion protocol.

## Replay

```bash
python -B experiments/X-105350-one-anchor-loewner-hamburger/verify.py \
  --output experiments/X-105350-one-anchor-loewner-hamburger/results/verification.json
```

The replay authenticates finite rational atomic calibrations only. It does not
machine-prove the Hamburger moment theorem, evaluate Xi, establish
`CRVH105330`, establish `OASH105350`, validate the moving saddle, or prove RH.

## Binding status

```text
one-anchor analytic equivalence        PROVED / REVIEW REQUIRED
origin parity-Stieltjes reduction       PROVED / REVIEW REQUIRED
bounded-order bootstrap                  REFUTED EXACTLY
OASH105350 for fixed-low-order Xi       OPEN
CRVH105330                               OPEN
Riemann Hypothesis                        UNPROVEN
```
