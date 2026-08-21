# X-93015 — Q4 prime-major-arc replay

Arithmetic class: `EXACT_RATIONAL_WITH_FORMAL_PRIME_LOG_SYMBOLS`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93015_Q4_PRIME_MAJOR_ARC_LOCALIZATION
```

The replay checks the complete prime-base source and row partitions, exact Gram splitting, sum-before-square diagonal inequalities, prime-power orbit support, generic orthogonal-projection cross identities, and hostile gauge/contracted-channel mutations.

It does not certify the analytic Chebyshev bound, the Fourier square-root minor-arc estimate, the remaining distinct-prime major-arc estimate, or RH.
