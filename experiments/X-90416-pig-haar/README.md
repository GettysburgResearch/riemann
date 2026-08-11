# X-90416 — Exact PIG bridge/Haar localization replay

This standard-library regression supports `L-90416` and `L-90417`.

Run:

```bash
cd experiments/X-90416-pig-haar
python3 -m py_compile verify.py
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Expected classification:

```text
PASS_X_90416_PIG_HAAR_LOCALIZATION
```

The checker uses only integer and `fractions.Fraction` arithmetic. It verifies:

1. the bridge cell, reflection, and first-difference identities;
2. exact discrete Haar Parseval;
3. every reflected triangular-window formula on the declared finite packet;
4. the fine-scale energy inequality;
5. the radix-four triangular/Haar scaling identity;
6. the finite four-adic atom bound.

The retained packet covers:

```text
3,570 bridge cells
3,514 first-difference rows
3,514 Haar coefficients
56 fine-scale inequalities
119 radix-four scaling rows
496 atom rows
```

It does **not** prove the coarse-Haar square-function bound, deterministic PIG, the repaired global PIG-to-pole adapter, or RH.
