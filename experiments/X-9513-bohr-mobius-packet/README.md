# X-9513 — Exact Bohr covariance and Jordan-square replay

The verifier checks `L-9513` using Python integers and `fractions.Fraction` only.

It performs:

1. 144 independent pair checks for all `1<=d,e<=12`, comparing direct
   piecewise-polynomial integration over `lcm(d,e)` with
   \[
   \frac{(d,e)^2}{12de}+
   \frac{(d,e)^4}{180d^2e^2};
   \]
2. twelve complete packet checks comparing the pairwise Möbius quadratic form
   with the positive Jordan-totient factorization;
3. exact nonnegativity of every retained packet energy.

Expected verdict:

```text
PASS_EXACT_L9513_BOHR_JORDAN_FACTORIZATION
```

Proof-object SHA-256:

```text
aaa036169a156e0519543328d7ed4fe307b84708856323e12f499620e29a75f2
```

## Proof boundary

This validates finite covariance and factorization algebra only. It does not
prove a local-to-Bohr transference estimate, the all-moments ladder, the
critical energy bound, or RH.
