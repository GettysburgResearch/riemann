## Purpose

Continue PR #561 at exact head `db9bdc63c855c6ddf664b763d748f8155a6a2c67` and attack its open global parity-Hall producer.

**RH remains unproved.** This successor reduces the producer to one `5:3` scalar and one globally owned activation-boundary functional.

## Advances

1. Exact `5:3` reciprocal-state factorization and zero-safe Mellin numerator.
2. Adaptive even-depth Bonferroni theorem for the homogeneous rough product.
3. Positivity of every smooth-interior rough finite difference.
4. Exact parity-covariant positive Julia lift.
5. Exact localization of the remaining sign to `GABPT`, the Global Activation-Boundary Parity Transport theorem.
6. Exact firewall showing the positive Julia trace retains the real zeta pole and cannot by itself feed Landau.

## Paper and replay

```text
standalone/2026-08-17-global-parity-hall/main.tex
standalone/2026-08-17-global-parity-hall/global-parity-hall-scalar-julia-97240.pdf
```

```bash
python3 experiments/X-97240-global-parity-hall/verify.py \
  --output experiments/X-97240-global-parity-hall/results/verification.json
sha256sum -c T97240_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T97240_GLOBAL_PARITY_HALL_SCALAR_JULIA_REDUCTION
```

## Scientific boundary

```text
adaptive homogeneous parity depth      PROVED
smooth-interior positivity             PROVED
parity-covariant Julia lift            PROVED
activation-boundary localization       PROVED
GABPT                                  OPEN / RH-BEARING
GABPT -> RH                            PROVED CONDITIONAL
Riemann Hypothesis                     UNPROVEN
```
