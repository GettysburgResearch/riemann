# X-105107 — Blaschke–Pick jet selectors

This exact-rational verifier authenticates:

- forced target and nontarget Blaschke exponents;
- off-centre top-jet normalization, including the self derivative;
- reduction to ordinary target values;
- complete two-node Pick matrices and exact PSD thresholds;
- a singular rational-inner extremal;
- real/even multi-target symmetry;
- exact target residue preservation and nontarget annihilation;
- strict improvement over the checkpoint-7 reduced polynomial selector;
- exterior-pole, wrong-kernel, and prior-art firewalls.

Replay:

    python -B tests/test_verify.py
    python -B -O tests/test_verify.py

Expected verdict:

    PASS_T105107_BLASCHKE_PICK_JET_SELECTORS

Expected proof digest:

    82747e320365a97bf9824dd84960f00bbcb77cd738040c2c5214be844dfc738c

The replay uses only standard-library fractions and matrices of order at most
two.  It performs no Xi evaluation, conformal-map computation, zero scan,
floating-point quadrature, broad suite, or heavy computation.
