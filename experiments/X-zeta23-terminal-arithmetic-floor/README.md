# X-zeta23-terminal-arithmetic-floor

Finite regression for `TERMINAL_GAUSSIAN_ARITHMETIC_FLOOR.md`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

The script checks:

- exact target values `F(z)=1`, `F(conj z)=-1`;
- the closed real-axis square of the Gaussian cardinal;
- the exact autocorrelation shell by numerical Fourier inversion;
- the completed-Chebyshev Stieltjes normal form against a finite von Mangoldt sieve;
- decay of the real-axis spectral mass;
- the `r lambda < 2` single-pair trace-moment resource barrier.

It does not prove the cofinal one-sided Chebyshev gate, the corrected-kernel floor, or RH.
