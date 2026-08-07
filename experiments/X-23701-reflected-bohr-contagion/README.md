# X-23701 — Exact reflected Bohr-contagion regression

Status: **SYNTHETIC EXACT ALGEBRA ONLY**

This standard-library experiment checks the finite proof kernel used by the
proposal:

1. raw tuple rows with the same monomial are recombined before every norm;
2. the grouped Bohr energy is the zero-ratio coefficient of the reflected
   Laurent square;
3. direct tuple contraction and grouped contraction agree in one rational PSD
   feature Gram;
4. rowwise absolute-value energy is strictly larger in the control;
5. a bounded-rank face ledger gives the exact exponent `C_0/K`;
6. a face above the declared rank ceiling fails closed;
7. a positive scale reserve is required;
8. finitely many packet orders are not promoted to the all-order theorem.

The retained synthetic values are:

```text
raw tuple rows             6
grouped monomials          3
rowwise energy             64
grouped Bohr energy        6
rational local Gram        41/4
reflected zero ratio       6
packet order K             8
rank ceiling C0            2
C0/K                       1/4
scale reserve              1/8
conditional theta ceiling  1
mutation tests             8/8 PASS
```

The large conditional theta ceiling is deliberate: one finite order does not
prove anything asymptotic.  The proposal requires an absolute `C_0` and an
unbounded sequence `K->infinity`.

This experiment does **not** evaluate primes, Möbius values, zeta, a production
Heath–Brown packet, the contagion theorem, BTP, or RH.
