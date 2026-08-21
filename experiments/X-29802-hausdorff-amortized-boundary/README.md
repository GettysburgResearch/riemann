# X-29802 — Hausdorff/Pascal amortized boundary regression

Run:

```bash
python experiments/X-29802-hausdorff-amortized-boundary/verify.py
```

Expected classification:

```text
EXACT_HAUSDORFF_PASCAL_AMORTIZED_BUDGET_VERIFIED
```

Finite checks:

```text
paired shifted pure-power jets   24,576
Euler source partitions               32
reversed-order mutation                 1
```

Result digest:

```text
23f5fd5b6b1e89d413489e6630b232412baac6ad3c56a7b291f2bbeafd1a26e2
```

The checker uses only `fractions.Fraction`. It verifies finite rational instances, not the complete common-tail/collar source manifest, Cycle Debt, the prime-ramp theorem, or RH.
