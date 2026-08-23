# X-105115 common safe rectangle

This exact verifier checks the finite supporting-line projection theorem,
the sharp non-strict counterexample, restricted Tonelli normalization, raw
quotient envelopes, and the selector-domain firewall.

Run:

    python -B tests/test_verify.py
    python -B -O tests/test_verify.py

No floating-point arithmetic, Xi evaluation, root search, or heavy
computation is used.
