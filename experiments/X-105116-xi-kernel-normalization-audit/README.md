# X-105116 Xi kernel normalization audit

This lightweight exact audit locks the factor-two repair across PR #716's
L-104504 and PR #720's L-104528/L-104531 conventions.  It checks the
completed-xi prefactor, the kernel differential operator, the standard-kernel
multiplier, the gamma-integral coefficient, the even/odd anchor phases, and
the resulting linear/quadratic scale laws for downstream PR #724.

Run:

    python -B tests/test_verify.py
    python -B -O tests/test_verify.py

The audit imports no unmerged source blob and makes no Xi, RCMV104530, or RH
claim.  It runs no floating-point or heavy computation.

Expected verdict:

    PASS_X105116_XI_KERNEL_NORMALIZATION_AUDIT
    38a85d503250264cb8ca16583e1f5c813c8879ec03874d3556cf6a141ad61a67

The digest covers the canonical payload before its `audit_sha256` field.
The checked-in result also fail-closes the scope flags for source import,
the Xi growth proof object, actual manifests, RCMV104530, and RH.
The source OIDs are exact metadata locks, not live imports: the verifier
checks their shape and relationships but deliberately does not invoke Git.
The PR #724 impact ledger is also fail-closed: it records which conclusions
are scale-invariant and marks its exact raw normalization as not ready.
