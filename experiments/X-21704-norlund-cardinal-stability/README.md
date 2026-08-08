# X-21704 — Exact Nörlund cardinal derivative-sampling replay

Run:

```bash
python experiments/X-21704-norlund-cardinal-stability/verify.py
```

Retained verdict:

```text
PASS_EXACT_NORLUND_CARDINAL_DERIVATIVE_SAMPLING
```

Proof-object SHA-256:

```text
e36d9ce0ce8ee3ea9f4127aa08e52dc028876a8d7ff3826f1dcee8b9f29454e8
```

The verifier uses only integers and `fractions.Fraction`. It checks:

```text
binomial-cardinal identity C_(K,n)=4 R_K(n)^2;
raw coefficient identity alpha=-(x beta(x))' at x=n;
logarithmic Nörlund preservation of the derivative identity;
Mellin derivative-sampling normal form at five integer exponents;
four source/weight/exponent mutations.
```

It does **not** prove:

```text
Nörlund Half-plane Stability;
Reciprocal Complete Monotonicity;
any zero location;
RH.
```
