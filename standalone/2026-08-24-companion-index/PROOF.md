# Companion partial index: a topological normal form for low-order descent

Let `p` be a real polynomial and remove `g=gcd(p,p')`.  Put `P=p/g`,
`Q=p'/g`, and `E_delta=Q+i delta P`.  The degree of `P` is the number `D` of
distinct roots of `p`.  Since `P,Q` are coprime, `E_delta` has no real zero.
On the upper semicircle its leading term contributes `D pi` of argument.  On
the real line, `Q/P=p'/p` after reduction has one positive Cauchy-index jump at
each distinct real root, contributing `R pi`.  Therefore

```text
2 pi N_plus = pi(D+R),
N_plus=(D+R)/2,
N_minus=(D-R)/2.
```

The compactified Cayley ratio

```text
U_delta=(Q+i delta P)/(Q-i delta P)
```

is unimodular and has winding `R`.  For a reduced Blaschke quotient
`u=B_plus/B_minus`, this becomes

```text
deg u = deg B_plus-deg B_minus;
rank H_u = deg B_minus;
rank H_conj(u) = deg B_plus;
deg u = ||H_conj(u)||_HS^2-||H_u||_HS^2.
```

Energy controls the bad rank only after separation.  If the normalized kernels
at the denominator zeros have Gram spectrum in `[kappa,K]` and
`|B_plus(b_j)|>=epsilon`, then every nonzero Hankel singular value is at least
`epsilon sqrt(kappa/K)`, and

```text
deg B_minus <= K ||H_u||_HS^2/(kappa epsilon^2).
```

This condition is necessary in kind.  For `u=B_a/B_b`, the bad rank is one and

```text
||H_u||_HS^2=((a-b)/(1-ab))^2 -> 0
```

as `b->a`.

For Xi, the exact remaining ninety-percent statement is that the reduced bad
companion count in a regular dyadic window is below `(1/20-o(1))N`.  The
current source-energy estimates do not prove this without a direct winding or
near-axis separation theorem.
