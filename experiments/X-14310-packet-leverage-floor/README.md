# X-14310 — Exact packet-leverage symbol floor

This experiment implements the finite arithmetic layer of `L-14317`.

For a certified packet subspace `K`, the normalized Fourier density of every
`w in K-perp` satisfies

```text
p_w(xi) <= c_K(xi)
         = ||P_(K-perp) exp(-i xi x)||^2/(2 pi).
```

Given cellwise directed bounds

```text
s(xi)>=L_j,
c_K(xi)<=C_j,
```

and a tail floor `s>=G`, the checker proves

```text
q_s(w)/||w||^2
>= G-sum_j C_j |I_j| (G-L_j)_+.
```

Every breakpoint level is checked exactly with `fractions.Fraction`; no
optimizer, eigensolver, or floating-point arithmetic enters the replay.

## Strict constant-packet control

On `[-1,1]`, use the synthetic packet `K=span{1}`. Its complement density cap is

```text
c_0(xi)=(1/pi)(1-(sin xi/xi)^2).
```

For `|xi|<=1/2`, `L-14317` proves the rational upper bound

```text
c_0(xi)<=53/1998.
```

The synthetic symbol has lower value `-10` on `[-1/2,1/2]` and tail floor `+1`.
The uniform-density theorem `L-14316` gives only the negative floor
`-833/333`. The exact packet-leverage replay instead gives

```text
1-11*(53/1998)=1415/1998>0.
```

This is an abstract `L2` packet separation. It does not assert that the
constant function is a Suzuki/CCM radical or belongs to the localized form
domain.

## Production contract

A production certificate must bind:

1. an exact packet subspace and digest;
2. membership of its vectors in the relevant Hilbert/form domain;
3. the complete Suzuki symbol normalization;
4. disjoint rational frequency cells;
5. directed symbol lower bounds;
6. directed leverage-deficit upper bounds;
7. an analytic symbol tail floor;
8. complete breakpoint levels and the claimed optimum.

For a nonorthonormal exact packet basis `k`, use

```text
c_K(xi)=(L-b(xi)^* M^(-1)b(xi))/(2 pi),
M_ij=<k_i,k_j>, b_i=<k_i,exp(-i xi x)>.
```

Approximate prolate vectors require an explicit subspace-error moat before use.

## Verification

```text
8 exact adversarial tests pass
strict synthetic packet-complement floor = 1415/1998
floating-point operations in checker = 0
```

No production Suzuki packet-leverage certificate has yet been run.
