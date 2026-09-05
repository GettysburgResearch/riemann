# X-105109 — Exact log-derivative edge-obstruction verification

This experiment authenticates L/T/R/M-105109 using standard-library rational
arithmetic and exact polynomial root/sign certificates.

Covered checks:

- the identities \(F/F'=1/\mathscr L\) and
  \(F^2/(F'F'')=1/(\mathscr L(\mathscr L^2+\mathscr L'))\);
- finite-jet exponential-gauge derivative data at a boundary point;
- the exact \(F_s\) derivative polynomials and complete disk manifests;
- the fixed first/second target principal coefficients;
- the optimal selector formulas and bounded golden-ratio limit;
- exact \(s=101/100\) root intervals and boundary quotient values;
- the boundary-sup versus contour-integral scope firewall;
- dependency, content-hash, mutation, and open-scope checks.

Run:

    python -B experiments/X-105109-log-derivative-edge-obstruction/tests/test_verify.py
    python -B -O experiments/X-105109-log-derivative-edge-obstruction/tests/test_verify.py

Expected:

    PASS_T105109_LOG_DERIVATIVE_EDGE_OBSTRUCTION
    17/17 tests in both modes

Regenerate:

    python -B experiments/X-105109-log-derivative-edge-obstruction/verify.py --output experiments/X-105109-log-derivative-edge-obstruction/results/verification.json

Expected proof-object digest:

    54829e77cb2aa90192aabdd61f86ff045a04ba3549f82c75384bc9a4e08f2890

No Xi evaluation, zero scan, floating-point root finding, contour quadrature,
broad suite, or heavy campaign is performed.
