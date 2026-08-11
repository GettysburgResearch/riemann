# X-zeta23-first-hermite-large-values

Finite diagnostics for the proposed large-value theorem in

```text
research/external/anthropic-zeta23/proofs/FIRST_HERMITE_LARGE_VALUES.md
```

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

The checker rebuilds von Mangoldt coefficients and tests:

- the coefficient-energy scale \(V(q)\sim q\);
- uniform one-prime block bounds;
- finite root-of-unity torus moments against a Bernstein-type envelope;
- a long-interval mean square against the coefficient energy;
- the \(B=8\) Gaussian tail completion-of-square bound;
- the growing-moment/exceptional-set parameter optimization.

Retained verdict:

```text
PASS_FIRST_HERMITE_LARGE_VALUES
```

The experiment is a finite diagnostic. It does not prove the analytic large-value theorem, the first-Hermite sign, the corrected-kernel floor, or RH.
