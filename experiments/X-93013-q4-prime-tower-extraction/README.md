# X-93013 — Q4 prime-tower extraction replay

Arithmetic class: `EXACT_INTEGER_FORMAL_VON_MANGOLDT`  
Claim exercised: `L-93013`

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The checker represents every von-Mangoldt prime power as a formal variable. It
verifies the five-channel expansion for both weighted Q4 kernels, partitions
all monomials by underlying prime base, checks the tower-count envelope, and
runs coefficient and equality-only-diagonal mutations.

The replay does not authenticate the analytic Chebyshev bound, estimate the
remaining distinct-prime correlations, prove endpoint PIG, or prove RH.
