# Integration handoff — normalized first-difference notches

Stack on PR #184.

Add:

```text
L-17802  optimal proof-safe first-difference line notch
T-17801  RH equivalence and phase-band inheritance
O-17802  hybrid/all-difference discovery ladder
M-17801  sensitivity-aware notch scheduler
X-17802  exact finite algebra and frontier-gain checker
```

Immediate production order:

1. close the corrected five-box normalization cell;
2. run the one-difference/four-box hybrids at zeros 4 and 3;
3. run the all-difference filter with selected phases retained explicitly;
4. repeat on the exact triangular base from `L-15409`.

No RH claim. A filter gain is not a zero; only a strict directed `T-15604` band
violation is decisive.
