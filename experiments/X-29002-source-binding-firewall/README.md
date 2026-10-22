# X-29002 — Source-binding firewall

This exact standard-library regression supports `R-29002` and `L-29006`.

It verifies:

- the compact filtered endpoint identity
  \[
  W_n=D_n-\frac32D_{2n}+\frac12D_{4n}=\frac12E_{2n}-E_n;
  \]
- all corresponding carry columns through `n=64`;
- exact formal Kummer and Selberg coordinates;
- the equality between an endpoint-difference packet and a nonnegative sum of
  complete `W_m` fibers on fifteen rational source blocks;
- the aggregate endpoint reserve;
- the exact symbolic counterexample
  \[
  P_{\omega,6}(2)^2-S_{\omega,6}(2)
  =\log3\log(25/32)<0;
  \]
- the exact ordinary row-scaling firewall at `(n,j,alpha)=(4,2,1/2)`.

Run:

```bash
python experiments/X-29002-source-binding-firewall/verify.py
```

The checker uses only Python's standard library, integers, and
`fractions.Fraction`.  The logarithmic counterexamples are certified by their
exact symbolic reductions and the integer inequalities `25<32` and `3>2`.

## Proof boundary

The regression certifies finite algebra only.  It does not certify a coupled
interior source matrix, a cofinal recurrence, an atomized energy bound, or RH.
