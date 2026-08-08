# X-29001 — Atomized carry, Selberg–Kummer, and endpoint-tree regression

This standard-library checker authenticates the finite algebra used by
`L-29001`--`L-29003` and the exact fixed-Abel counterexamples in `R-29001`.

Run:

```bash
python experiments/X-29001-atomized-carry-selberg-kummer/verify.py
```

The retained result is:

```text
EXACT_ATOMIZED_CARRY_SELBERG_KUMMER_AND_TREE_ALGEBRA_VERIFIED

proof-object SHA-256
8689c4233cf0c13d5eeae4db6a54a5cf48f84a5615d157d2ab36593da37bdfeb
```

Checked exactly:

```text
symmetric Nyman/carry rational rows       16,065
formal Selberg carry rows                  4,750
balanced-tree carry rows                   2,016
balanced-tree entropy rows                    63
fixed-Abel negative witnesses                  4
mutation tests                                 4
```

The formal logarithm assigns independent integer weights to primes. This checks
the complete additive and convolution algebra without floating-point logarithms.
The analytic inequality in `L-29002` is proved separately from monotonicity and
an explicit covariance decomposition.

The checker does **not** certify:

- the vector-valued atomized energy criterion's analytic continuation details;
- the cofinal energy estimate;
- `ETSR`;
- the Riemann Hypothesis.
