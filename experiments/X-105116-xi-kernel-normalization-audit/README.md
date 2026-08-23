# X-105116 Xi kernel normalization audit

This lightweight exact audit locks the factor-two repair between PR #720's
L-104528 and L-104531 conventions.  It checks the completed-xi prefactor,
the kernel differential operator, the standard-kernel multiplier, the
gamma-integral coefficient, and the even/odd anchor phases.

Run:

    python -B tests/test_verify.py
    python -B -O tests/test_verify.py

The audit imports no unmerged source blob and makes no Xi, RCMV104530, or RH
claim.  It runs no floating-point or heavy computation.

Expected verdict:

    PASS_X105116_XI_KERNEL_NORMALIZATION_AUDIT
    4efde5c2dadf2c52b9b7200c062fbef31e0e1ff451804f5b18d864026fcd2cc8

The digest covers the canonical payload before its `audit_sha256` field.
The checked-in result also fail-closes the scope flags for source import,
the Xi growth proof object, actual manifests, RCMV104530, and RH.
The source OIDs are exact metadata locks, not live imports: the verifier
checks their shape and relationships but deliberately does not invoke Git.
