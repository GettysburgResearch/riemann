# X-93250 — Exact replay for the centered-Q4 Bernoulli/cubic packet

Arithmetic class:

```text
EXACT_RATIONAL
```

The checker authenticates the new finite algebra only:

1. the Bernoulli weight has mean zero and norm \(1/180\);
2. its primitive is the cubic kernel \(K(x)=x(1-x)(2x-1)/3\);
3. the cell-field projection equals the finite cubic Riesz sum for arbitrary rational sources;
4. the centered Cauchy bridge has the stated factor \(N/180\);
5. the Mellin numerator is exactly \(s-1\);
6. formal Q4 prime-base components reconstruct the complete source, row, centered row, and cubic scalar;
7. the scalar block diagonal obeys the exact \(1/972\) kernel bound on the tested rational fixtures;
8. the abstract block-count and rank-one cross bounds are sharp;
9. hostile endpoint, kernel, mean, source-partition, and cardinality mutations are detected.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93250_CENTERED_Q4_CUBIC
```

The replay does **not** prove the zeta explicit formula, the Mellin pole exclusion, the imported First-Hermite estimates, the analytic prime-tower bound of `L-93015`, CPBD, or RH.
