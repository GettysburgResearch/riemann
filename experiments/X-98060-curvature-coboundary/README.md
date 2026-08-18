# X-98060 — Multiplicative curvature and cutoff-coboundary replay

This experiment authenticates the finite algebra and directed fixtures used by
`L/T/R-98060--98063`.

Run:

```bash
python3 experiments/X-98060-curvature-coboundary/verify.py
```

Expected verdict:

```text
PASS_T98060_MULTIPLICATIVE_CURVATURE_CUTOFF_COBOUNDARY
```

The verifier checks:

1. the prime-adjoining cross-ratio identity with exact rational arithmetic;
2. the truncated cutoff-coboundary identity with exact rational Stieltjes jump
   measures;
3. the literal `P_61` coefficient dictionary with every future Euler prime
   `q>=71` through the directed fixture range;
4. outward interval signs of the `p=67` ratio Wronskian at
   `Y=869/2,871/2,875/2`;
5. strict positivity of the fixture denominator and `Q(871/2)<67`;
6. the signs and numerical values of the fixed asymptotic constants `a_*` and
   `c_*`;
7. the exponent separation used in the fully activated logarithmic-prime
   switch theorem.

Arithmetic classes:

```text
cross-ratio/coboundary fixtures     EXACT_RATIONAL
ratio sign fixture                  OUTWARD_INTERVAL_80_DPS
asymptotic constants                HIGH_PRECISION_DIAGNOSTIC + ANALYTIC SIGN
log-prime switch theorem            ANALYTIC_PNT_ASYMPTOTIC
```

The replay does not prove the post-logarithmic product-boundary sign, `GPC67`,
or RH.  Those fields are fail-closed in the retained result.