# X-92203 — Reciprocal Loewner–Hankel exact replay

Run:

```bash
python3 verify.py
```

Retained verdict:

```text
PASS_RECIPROCAL_LOEWNER_HANKEL
```

The checker uses only exact rational arithmetic.  Through orders one to four
it verifies:

```text
M_n(1/p)=D T H_n(p) T^T D;
det M_n(1/p)=p^(-2n) det H_n(p);
the finite squared-pole Cauchy–Binet/Vandermonde formula.
```

The replay proves finite algebra only.  It does not certify the infinite Xi
pole expansion, any zeta-specific Hankel sign, finite-order matrix
monotonicity of the actual Xi impedance, complete Bernstein passivity, or RH.
