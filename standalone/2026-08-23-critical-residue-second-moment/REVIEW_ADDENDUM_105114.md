# Review addendum - L/T/R/M-105114 anchored collar transfer

Checkpoint base:
f8102c6648829f72a6faaad06141c25b043c3f05.

## Hostile checks

- Confirm \(f(a)\ne0\) and normalize \(f/f(a)\) before applying the bound.
- Verify \(2r_1/(r_2-r_1)\), not a dimensionful suppressed coefficient.
- Count inner-disk zeros with multiplicity using the expanded radius
  \(r_3\).
- Keep the nominal equal-disk radius convention
  \(\varepsilon r_2\).
- Add radius loads before applying the strict factor-two projection gate.
- For raw quotients, charge only \(F'\)- and \(F''\)-zero disks.
- Require a separate \(F\)-zero cover for any log-derivative rewrite.
- Keep \(\Xi_t(z)=\xi(1/2+iz)\) and fixed derivative order \(k\).
- Reject the origin as an automatic common anchor.
- Keep actual-pole manifests and selector norms as independent inputs.
- Reject any inference from generic order-one growth to cofinal absorption.
- Confirm RCMV104530 and RH remain open.

Exact replay:

    python -B experiments/X-105114-anchored-equal-disk-collar/tests/test_verify.py
    python -B -O experiments/X-105114-anchored-equal-disk-collar/tests/test_verify.py

Expected:

    PASS_T105114_ANCHORED_EQUAL_DISK_COLLAR
    16 / 16 in both modes
    15ff7ba8056a9beb5e942945c9f92dcce566f7d737bc04f8f2db6895109c3284

The replay authenticates the exact finite formula ledger, rational
projection fixture, source-normalization firewall, and open-scope flags.
It performs no Xi computation.
