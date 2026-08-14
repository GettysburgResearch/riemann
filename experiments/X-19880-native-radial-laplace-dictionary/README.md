# X-19880 — Exact native-to-radial dictionary analogue

This experiment checks a discrete geometric-Laplace analogue of `L-19880` using
Python integers and `fractions.Fraction` only.

For the lattice ramp

```text
R_u(n)=(n-u)_+
```

and `0<z<1`, the exact identity is

```text
((1-z)^2/z) sum_(n>=0) z^n R_u(n)=z^u.
```

It is the discrete counterpart of

```text
lambda^2 int exp(-lambda x)(x-u)_+ dx=exp(-lambda u).
```

The checker verifies:

1. the transformed ramp coefficient for each mode;
2. nonnegative source-owner fractions summing to at most one;
3. exact interval refinement;
4. one common feature column for full, used, and slack matrices;
5. `full-used=slack` exactly;
6. positive semidefiniteness of the slack Gram by exact LDL;
7. an optional claimed matrix;
8. exact radix-four ancestor visibility and the `Y_4=0` radial null gauge;
9. fail-closed parsing and dimensions.

Reproduction:

```bash
python3 verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python3 -m unittest discover -s tests -v
```

The regression does not evaluate zeta, prove the continuous integral theorem,
construct `SONTR` or `NRMA`, or prove RH.
