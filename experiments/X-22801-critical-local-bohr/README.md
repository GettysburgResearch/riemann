# X-22801 — Exact finite local/Bohr regression

This experiment uses only Python integers and `fractions.Fraction`.

It verifies, for every `1<=D<=16`:

1. the reduced-Farey divisor-coordinate identities behind `L-22801`;
2. the exact Jordan/Bohr energy;
3. the exact physical integral
   \[
   \int_D^{2D}|S_D(x)|^2dx
   \]
   by piecewise-quadratic integration;
4. the finite inequality
   \[
   \int_D^{2D}|S_D|^2
   \le\frac94D\mathcal B_D.
   \]

The largest retained ratio occurs at `D=10`:

```text
32421033 / 18019750
= 1.7991943839...
```

The proof-object digest is

```text
0c606242167ca7b7ab213a0a2c9ac97fb8488591c43af1cdb78a2a2fb0e12c9c
```

## Run

```bash
python verify.py certificates/exact-D16.json \
  --output results/exact-D16-verification.json
python -m unittest discover -s tests -v
```

## Proof boundary

This is a finite regression for the **truncated centered packet**. It does not verify:

- the completed endpoint/tail channel;
- the uniform Farey determinant bound;
- the divisor-Hilbert estimate;
- the all-`D` theorem;
- RH.

Its purpose is to catch algebraic factors and provide adversarial data for reviewing `T-22801`, not to support extrapolation from sixteen finite levels.