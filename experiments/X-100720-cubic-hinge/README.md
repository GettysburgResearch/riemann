# X-100720 — Exact cubic hinge / rough-prefix algebra replay

This standard-library checker verifies the finite algebraic interfaces of the
T100720 packet.

```bash
python3 experiments/X-100720-cubic-hinge/verify.py \
  --output /tmp/t100720.json
cmp /tmp/t100720.json \
  experiments/X-100720-cubic-hinge/results/verification.json
```

Expected:

```text
PASS_T100720_CUBIC_HINGE_ROUGH_PREFIX_ALGEBRA

a05a9ed1c455a87115424ec8d4bfb0ec1fc8acc94ce0f36f012c4c35be88f0ba
```

The replay checks:

- the hinge and carrier/collar identities;
- a rational compensated-prefix derivative fixture;
- exact third-variation and first-moment factorizations;
- four finite two-sided Taylor inequalities;
- the regularity-countermodel scaling constant.

It does not replay Tao's published semigroup theorem or Mertens' asymptotic.
It predates the later adaptive partition and exponent-`e` theorem, whose proofs
are analytic. It does not prove `APCC100723`, `DPCC100723`, or RH.
