# X-zeta23-linear-resolution-rigidity

Finite diagnostics for the continuation of PR #390 from sublinear heat resolution to a fixed positive fraction of `log T`.

The script checks:

1. the adaptive Gaussian cutoff exponent
   \[
   u/2-u^2/(4q)=q/4-(u-q)^2/(4q);
   \]
2. a coarse continuum tail bound after truncation at `exp(a q)`, `a>2`;
3. the fixed-moment union scale `L^(1-K)` for integer resolutions
   `q <= L/(4 a K)`;
4. the refined growing-moment exponent proxy;
5. the finite Cauchy--Schwarz resonance certificate;
6. conversion from prime-power count to a distinct-prime count.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_LINEAR_RESOLUTION_FIRST_HERMITE_RIGIDITY
```

The replay proves finite identities and scale checks only. It does not prove the analytic large-value theorem, pointwise first-Hermite positivity, the corrected-kernel floor, or RH.
