# X-102890 — Lattice-normalized centered dispersion replay

Standard-library replay for `R-102868`, `L-102880--L-102884`, and `T-102890`.

It checks:

```text
exact zero square-lattice moment of K_L;
negative sign of the original R_L lattice moment;
Y^(-1/6) unrestricted derivative Type-I exponent;
one- and two-modulus centered nonzero-phase identities;
coherent weighted modulus-family identity;
boundary squarefree-kernel typing.
```

It does not prove `SLCD102890` or RH.

Run:

```bash
python3 verify.py --output /tmp/x102890.json
cmp /tmp/x102890.json results/verification.json
```
