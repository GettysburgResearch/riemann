# X-98500 — Signed Dickman/VK transfer replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay checks:

- Dickman positivity and the delay equation numerically;
- the exact finite-part sign change between cutoffs \(11\) and \(13\);
- a synthetic signed-boundary convolution;
- the \(5/8,3/4\) exponent algebra.

It does not replace the multidimensional Stieltjes comparison, the classical
Vinogradov–Korobov PNT, the imported P61 proof object, the critical-core
transport, or RH.
