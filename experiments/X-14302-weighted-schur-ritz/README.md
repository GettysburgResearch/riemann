# X-14302 — exact weighted Schur–Ritz verifier

This directory implements the finite rational adapter in the audited
`L-14302`. It does not construct a Riemann--Weil matrix, a prolate target, or a
Hardy Gram. It verifies a certificate after those objects have been enclosed by
external analytic/provenance code.

## Checked gates

For a rational midpoint matrix `A0`, operator-radius bound `delta`, exact parity,
nonzero even projection vector `p`, complete rational bases of the even
complement and odd sector, and rational Loewner bounds

```text
0 < G_lower <= G_exact <= G_upper,
```

the checker verifies:

1. midpoint symmetry and parity;
2. completeness, parity, rank, and orthogonality of both bases;
3. `G_lower >= m S` and `G_upper >= G_lower`;
4. `U >= Rayleigh_A0(p) + delta`;
5. the robust weighted even-complement LMI;
6. the robust odd-sector gap LMI;
7. the dual residual Schur certificate;
8. the operator-radius contribution to the dual residual.

It then emits exact rational bounds for the global spectral gap, the total dual
residual, and the projectively optimized Hardy target-line distance.

## Synthetic certificate

The five-dimensional example uses parity

```text
(+,+,+,-,-),
```

an unnormalized target projection `p=(2,0,0,0,0)`, and

```text
M_even = diag(4,10000)
```

in standard even-complement coordinates. The retained even- and odd-sector
bases are deliberately nonorthogonal, so the coordinate Gram identities are
exercised rather than hidden by a standard basis. The second even mode has a
very large Hardy weight but zero midpoint coupling to the target. This realizes
the geometry for which the dual-residual certificate is much sharper than a
worst-case embedding factor. A nonzero operator radius `delta=1/100` is retained.

The exact output is

```text
simple-even global ground state: certified
global spectral gap >= 49/25
dual residual <= 21/100
Hardy target-line distance <= 37/70
```

No floating eigenvalue or eigenvector is supplied to the checker.

## Reproduction

From the repository root:

```bash
python3 -m py_compile \
  experiments/X-14302-weighted-schur-ritz/verify.py \
  experiments/X-14302-weighted-schur-ritz/tests/test_verify.py

python3 -m unittest discover \
  -s experiments/X-14302-weighted-schur-ritz/tests -v

python3 experiments/X-14302-weighted-schur-ritz/verify.py \
  experiments/X-14302-weighted-schur-ritz/certificates/synthetic-interval.json \
  --output experiments/X-14302-weighted-schur-ritz/results/synthetic-interval-verification.json

sha256sum -c experiments/X-14302-weighted-schur-ritz/SHA256SUMS
```

## Proof boundary

The verifier assumes external proofs that:

- the exact matrix lies in the declared operator ball;
- the exact matrix commutes with parity;
- the exact Hardy Gram lies between the supplied rational Loewner bounds;
- the weighted projection-tail bound represents the norm in `T-14301`.

An entrywise interval table is not automatically a Loewner enclosure, and a ball
around a parity-commuting midpoint does not prove exact parity.
