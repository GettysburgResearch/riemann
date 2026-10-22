# X-105110 — Exact principal-part edge-cancellation verification

This experiment authenticates L/T/R/M-105110 with standard-library exact
rational and polynomial algebra.  Transcendental identities are verified by
their algebraic derivatives, endpoint data, and rational lower certificates;
no floating-point quadrature is used.

Covered checks:

- the oriented and absolute straight-edge Cauchy-kernel ledgers;
- the endpoint/corner logarithmic firewall;
- the weighted first/second exterior residue formulas;
- the simultaneous \(F_\delta\) quotient identities and partial fraction;
- exact coefficient bounds behind both absolute-edge divergences;
- the \(F_N\) fixed global manifest, residue, and selector data;
- the rational lower chain proving a right edge exceeds \(N^2/30\);
- the full-contour versus individual-edge scope firewall;
- dependency, content-hash, mutation, and open-scope checks.

Run:

    python -B experiments/X-105110-principal-part-edge-cancellation/tests/test_verify.py
    python -B -O experiments/X-105110-principal-part-edge-cancellation/tests/test_verify.py

Expected:

    PASS_T105110_PRINCIPAL_PART_EDGE_CANCELLATION
    18/18 tests in both modes

Regenerate:

    python -B experiments/X-105110-principal-part-edge-cancellation/verify.py --output experiments/X-105110-principal-part-edge-cancellation/results/verification.json

Expected proof-object digest:

    3f0286c2d574e8252fe9903f4f62d86e510275bdf4a1a085e3f232873aec9532

No Xi evaluation, zero scan, floating-point root finding, contour quadrature,
broad suite, or heavy campaign is performed.
