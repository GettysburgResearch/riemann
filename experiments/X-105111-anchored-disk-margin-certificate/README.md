# X-105111 — Exact anchored/disk quotient-margin verification

This experiment authenticates L/T/R/M-105111 using standard-library exact
rational and polynomial arithmetic.  Logarithms and exponentials remain
symbolic labels backed by exact ratios and coefficient inequalities.

Covered checks:

- both normalized denominator derivative identities through \(F'''/F\);
- both log-density identities by exact cross multiplication;
- the anchored-drop and total-variation ledgers;
- exact rational first/product margins and drop ratios;
- the two-disk cover geometry, center values, derivative suprema, and slacks;
- sharp anchor-only and first-versus-product margin firewalls;
- the stable global first manifest, target residue, selector, and fixed
  anchor data of the \(Q_S\) family;
- the exact rational collapsing nonsample value;
- dependency, content-hash, mutation, and open-scope checks.

Run:

    python -B experiments/X-105111-anchored-disk-margin-certificate/tests/test_verify.py
    python -B -O experiments/X-105111-anchored-disk-margin-certificate/tests/test_verify.py

Expected:

    PASS_T105111_ANCHORED_DISK_MARGIN_CERTIFICATE
    19 tests in both modes

Regenerate:

    python -B experiments/X-105111-anchored-disk-margin-certificate/verify.py --output experiments/X-105111-anchored-disk-margin-certificate/results/verification.json

Expected proof-object digest:

    7bafdd3d8fb379e8d8de2cd30df8b96331378d7e4f244bb801439493a2e132cd

No Xi evaluation, zero scan, floating-point root finding, quadrature, broad
suite, or heavy campaign is performed.
