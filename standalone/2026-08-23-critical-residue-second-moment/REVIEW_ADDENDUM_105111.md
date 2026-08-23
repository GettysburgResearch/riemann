# Review addendum — L/T/R/M-105111 quantitative margins

Checkpoint base:
b52e4b4dceefb0b6c56b0ffe303d4ca01ffe9c56.

## What changed

Both logarithmic denominator margins now have an exact anchored-drop ledger
and a noncircular finite-disk certificate.  The derivative inputs are
expressed through \(F'/F,F''/F,F'''/F\).

Exact rational fixtures bind the margin/drop equalities and disk slacks.  A
stable-global-first-manifest family proves that finite anchor values do not
control the edge between anchors.

## Hostile checks

- Verify the signed subarc definition of the exact downward log drop.
- Verify nonvanishing is assumed for log variation but proved by positive
  disk slack.
- Verify both normalized-derivative and log-density identities.
- Verify the selector equality uses constant boundary modulus.
- Verify margins \(3/4,15/64\) and ratios \(4/3,16/5\).
- Verify both disk covers, derivative suprema, and four slacks exactly.
- Verify the first-margin versus product-margin firewall.
- Verify the \(Q_S\) family has only the globally fixed first target zero.
- Keep the edge away from target zero and do not claim a stable second
  manifest.
- Verify Xi/cofinal/RH scope remains open.

Exact replay:

    python -B experiments/X-105111-anchored-disk-margin-certificate/tests/test_verify.py
    python -B -O experiments/X-105111-anchored-disk-margin-certificate/tests/test_verify.py

Expected:

    PASS_T105111_ANCHORED_DISK_MARGIN_CERTIFICATE
    19 / 19
    7bafdd3d8fb379e8d8de2cd30df8b96331378d7e4f244bb801439493a2e132cd

Xi anchors, disk enclosures, cofinal variation, selector absorption,
cancellation debts, strict coherence, RCMV104530, and RH remain open.
