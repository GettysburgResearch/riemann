# X-26201 — Exact critical Euler-fiber regression

This standard-library-only checker verifies the finite algebra used by
`L-26201/L-26202`.

Run:

```bash
python experiments/X-26201-critical-euler-fiber/verify.py
```

Retained verdict:

```text
PASS_EXACT_CRITICAL_EULER_FIBER_ALGEBRA
```

The checker uses exact arithmetic in

\[
\mathbb Q(\sqrt2).
\]

It verifies:

- the filter polynomial
  \((1-2z)(1-\sqrt2z)^2\);
- the complete local two-adic polynomial
  \((1-z)(1-2z)(1-\sqrt2z)^2\);
- the pole and double half-pole roots;
- positivity of the first 65 exact inverse coefficients;
- the exact generalized-prime coefficients through order 64;
- the finite four-scale source identity through 512;
- the odd Möbius firewall;
- complete five-tap fibers over every squarefree odd core in range;
- three mandatory factor-deletion mutations.

Retained proof-object digest:

```text
eae4763448cea4d19301e5f18eae6dbd5eb29c69a05d535ade49211ec6e3483e
```

## Scope boundary

The checker proves finite/filter/source algebra only.  It does **not** verify:

- the analytic block-Laplace equivalence;
- the two-frequency reflected physical identity;
- a production Schur reserve;
- the `EFRC` recurrence;
- RH.
