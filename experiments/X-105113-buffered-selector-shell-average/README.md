# X-105113 — Exact buffered-selector shell-average verification

This lightweight experiment authenticates L/T/R/M-105113 with standard
library `Fraction` and polynomial arithmetic.

It checks:

- the signed vertical and horizontal shell orientations against exact
  parameter-averaged polynomial edge integrals;
- the triangular-weight Tonelli mean and the coordinate-correct inverse
  widths;
- sharp indicator fixtures for both measurable width constants;
- the prescribed-weight quantifier and the absence of a universal good
  rectangle;
- the cubic derivatives, actual manifests, residues, charge jumps, selector
  congruences, and canceled carriers;
- the dependency, mutation, scope, content-hash, and control-character
  firewalls.

Run:

    python -B experiments/X-105113-buffered-selector-shell-average/tests/test_verify.py
    python -B -O experiments/X-105113-buffered-selector-shell-average/tests/test_verify.py

Expected:

    PASS_T105113_BUFFERED_SELECTOR_SHELL_AVERAGE
    18 tests in both modes

Expected proof-object digest:

    44e0cffca9d4d680555287e8290cfa645d979dc76b064f0ab6914ace88c7d560

The verifier hashes exactly the packet metadata, four claim files, verifier,
and test file.  It performs no floating point, root finding, Xi evaluation,
broad suite, or heavy computation.
