# X-21704 — Brownian Green-defect exact replay

Run:

```bash
python experiments/X-21704-brownian-green-defect/verify.py
```

The checker uses only Python integers and `fractions.Fraction`. It validates the finite algebra behind `L-21707`:

```text
three positive cutoff families: raw, logarithmic, central-binomial;
G_lambda(0)=1;
complete coefficient collapse into G_lambda and G_lambda';
finite-product ordering behind A_lambda(y)>=0;
elementary central-binomial Wallis bound;
four deliberate mutations.
```

Retained verdict:

```text
PASS_EXACT_BROWNIAN_GREEN_DEFECT_ALGEBRA
```

Proof-object SHA-256:

```text
65442b5fb1ff09e06c7f237102cc289bb9c28f6d33f1b12cea7f54d0670277d7
```

The checker does **not** certify the contour deformation, the zeta functional-equation normalization, the all-real-zero theorem, BLNRZ, or RH. Those remain analytic review obligations.
