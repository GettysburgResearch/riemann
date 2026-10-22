# X-105108 — Exact Green–Gram selector-conditioning verification

This experiment authenticates the finite arithmetic fixtures for L/T/R/M-105108.
It uses `fractions.Fraction` and symbolic polynomial factors only.

Covered fixtures:

- the \(56/45\) off-centre Green load;
- equal- versus opposite-phase two-target data;
- the selector-compatible \(\varepsilon=1/5\) triple;
- exact product/cardinal and normalized-Gram envelopes;
- a collective three-target obstruction invisible to every pair test;
- exact disk-domain monotonicity \(4R^3\) for \(R>1/2\);
- the fixed-disk collision family \(n^m\) for integers \(n\ge2,m\ge1\);
- dependency, content-hash, mutation, and scope firewalls.

Run:

    python -B experiments/X-105108-green-gram-selector-conditioning/tests/test_verify.py
    python -B -O experiments/X-105108-green-gram-selector-conditioning/tests/test_verify.py

Expected:

    PASS_T105108_GREEN_GRAM_SELECTOR_CONDITIONING
    15/15 tests in both modes

Regenerate the committed artifact with:

    python -B experiments/X-105108-green-gram-selector-conditioning/verify.py --output experiments/X-105108-green-gram-selector-conditioning/results/verification.json

The expected proof-object digest is

    6c2484c4e63612b238f1ec6044c9b8778b725899d4be643d7e80b6a6dc345cdb

No Xi evaluation, zero scan, floating-point conformal map, contour
quadrature, broad suite, or heavy computation is performed.
