# X-107100 — Reverse–Rolle counting replay

This lightweight standard-library replay checks:

- six exact polynomial/multiplicity fixtures for `L-107100`;
- nonnegativity and parity of every local defect weight `r+iota`;
- the sharp coefficient `2` on a simple extra extremum;
- the exact `2/b` negative-curvature mass of one conjugate zero pair.

It does not compute Xi zeros, prove the Xi complex-transport inequality, establish growing-order derivative concentration, or prove RH.

Run:

```bash
python3 experiments/X-107100-reverse-rolle/verify.py \
  --output experiments/X-107100-reverse-rolle/results/verification.json
```

Expected verdict:

```text
PASS_T107100_REVERSE_ROLLE_COUNTING
```
