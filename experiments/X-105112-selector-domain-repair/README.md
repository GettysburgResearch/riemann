# X-105112 — Exact selector-domain repair verification

This lightweight experiment authenticates L/T/R/M-105112 with standard
library Fraction and polynomial arithmetic.

It checks:

- both same-selector-domain weighted-sup equalities;
- the general actual-weight-norm product inequality;
- the maximum-modulus tau envelope on the selector-domain closure;
- \(F'/F=z^3\) and \(F''/F=z^2(z^4+3)\) exactly;
- the order-three target and optimal selector \(W_*=z^2\);
- the radius-\(1/2\) counterexample values two and eight;
- recovery of equality on the unit semicircle;
- the frozen-file, dependency, mutation, content-hash, and control-character
  firewalls.

Run:

    python -B experiments/X-105112-selector-domain-repair/tests/test_verify.py
    python -B -O experiments/X-105112-selector-domain-repair/tests/test_verify.py

Expected:

    PASS_T105112_SELECTOR_DOMAIN_REPAIR
    15 tests in both modes

Expected proof-object digest:

    3748777ede886502e57c6ad77777807b11b98104a8ecba04b60f162b10e2b19c

No floating point, root finding, Xi evaluation, broad suite, or heavy
computation is performed.
