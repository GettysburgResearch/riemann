# X-95500 — Q4 SACF critical-resonance replay

Run:

```bash
python3 verify.py --scan-limit 100000 --output results/verification.json
sha256sum -c SHA256SUMS
```

The exact replay checks the gcd/source bijection, local Euler completion,
formal logarithmic derivatives, dual-frequency factorization, Q4 kernel root
lines, zero-frequency mass, autocorrelation Gram identity, and exponent
mapping. The endpoint scan is floating reconnaissance only.

It does not prove SACF, FOCC, OCHD, or RH.

The replay also checks the exact odd-Mertens dyadic reconstruction and the
discrete partial-summation identity used by the unconditional classical
zero-free-region gain.  It does not numerically certify the imported analytic
zero-free-region theorem.
