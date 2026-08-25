# X-106120 — Bilateral Kummer tensor replay

Run:

```bash
python3 verify.py
```

The replay checks finite instances of:

- the product of the two nonzero Ramanujan identities;
- the tensor squareclass Gram and sharp principal embedding;
- the atomic source inequality `ell*rho/(c^2*d^2) <= 1/(c*d)`;
- the double full-character prime-product collision identity;
- the fixed-core two-dimensional additive large-sieve bound used in
  `L-106123`.

It does not prove `BTPP106122`, `BTPN106122`, `BTNN106122`, `BTRC106123`,
`BCI102990`, or RH.
