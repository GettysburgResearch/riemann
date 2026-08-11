# X-91008 — Gamma/Catalan safe-disc replay

This finite high-precision replay accompanies `L-91008`, `T-91003`, and `R-91003`.

It checks only exact algebra, special-function identities, and synthetic scale laws:

- the gamma-background algebra
  \((2-w-2\sqrt{1-w})/w^2=(1+\sqrt{1-w})^{-2}\);
- the exact Catalan coefficients of
  \(\Phi(w)=1/[2(1+\sqrt{1-w})^2]\);
- the beta-`(3/2,3/2)` Stieltjes integral;
- Hausdorff finite differences against exact beta cells;
- strict positivity of one finite Loewner/Pick matrix;
- the Cauchy-circle scaling at
  \(R_k=3/4-1/(k+4)\);
- the critical constant \(1/\log(4/3)\);
- synthetic coefficient crossover for one planted off-line pair.

It does **not** evaluate zeta, certify the analytic estimates, prove annular positivity, or prove RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_GAMMA_CATALAN_SAFE_DISC
```