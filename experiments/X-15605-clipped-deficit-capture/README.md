# X-15605 — Exact clipped-deficit capture regression

This standard-library-only verifier replays the finite separation in
`L-15618`.

The retained diagonal model has

```text
G = 2, alpha = 0, Gamma = 1,
D = diag(2,2,3/5,3/5),
L = span(e1,e2).
```

The true complement floor is `7/5`, but the un-clipped trace condition fails:

```text
Tr D - 2(G-alpha) = 6/5 > 1 = G-Gamma.
```

Clipping at the exact danger threshold gives

```text
theta = G-Gamma = 1,
Tr(D-theta I)_+ = 2 = 2(Gamma-alpha),
```

so the sharp gate passes exactly.

Run:

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
```

The checker uses only Python integers, `fractions.Fraction`, JSON, and SHA-256.

Retained proof-object SHA-256:

```text
d246fe0a776f5baa01d21b3befb91dab4fbf1d21d528553c2a5a9e9eb1c43202
```
