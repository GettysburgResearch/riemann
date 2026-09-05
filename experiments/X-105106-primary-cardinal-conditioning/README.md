# X-105106 — Primary-cardinal conditioning ledger

This exact-rational verifier authenticates the finite-window consequences of
L-105106:

- the closed top-primary cardinal formula;
- all local target and nontarget congruences;
- degree, leading coefficient, weighted coefficient norm, and separation
  envelopes;
- real/even symmetry and its possible one-degree cancellation;
- the exact partial-fraction identity for \(W/M\);
- real-even clustered first- and second-selector obstructions;
- Blaschke lower bounds excluding a higher-degree holomorphic escape;
- the independent holomorphic-remainder edge firewall.

Replay:

    python -B tests/test_verify.py
    python -B -O tests/test_verify.py

Expected verdict:

    PASS_T105106_PRIMARY_CARDINAL_CONDITIONING

Expected proof digest:

    7dc8a3075e983d48032d74e14af2d3fed5611adb9735623e32a9dfa8623ace33

The replay uses only Python standard-library fractions on degree-at-most-nine
polynomials.  It performs no Xi evaluation, zero scan, floating-point
quadrature, broad suite, or heavy computation.
