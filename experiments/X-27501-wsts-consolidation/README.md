# X-27501 — Exact finite regression for the WSTS consolidation

This experiment authenticates finite algebra used by the final weighted
shell-tail review packet.

Run:

```bash
python experiments/X-27501-wsts-consolidation/verify.py
```

The checker uses only Python's standard library and exact `Fraction`/integer
arithmetic.  It verifies:

```text
the normalized-tail derivative factorization;
the prime-tail queue equals the maximum positive suffix;
weighted Abel summation by upper tails;
the least Skorokhod boundary charge;
exact dyadic shell telescoping;
a finite Stieltjes integration-by-parts orientation;
zero-cost logarithmically weighted prime transfer;
the cubic/quartic logarithmic error budget;
the finite dyadic ratio lies in [1/3,1/2].
```

The retained result class is

```text
EXACT_FINITE_ALGEBRA_ONLY
```

It does **not** prove:

```text
WSTS;
RH;
the classical Chebyshev error bound;
any cofinal prime-sampling estimate.
```

The analytic estimates and the conditional equivalence are stated in
`L-27501/T-27501` and require independent human review.