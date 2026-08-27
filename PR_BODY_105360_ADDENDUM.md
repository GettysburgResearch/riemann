## T105360 addendum — terminal affine boundary remainder

This checkpoint removes the remaining window-by-window repetition from the
boundary Stieltjes hierarchy.

### Exact nested-window transport

For symmetric regular windows `Omega_1 subset Omega_2`, every crossed real
critical pair `+-c` contributes the atom

```text
support s_c = 1/c^2,
weight  w_c = -2 rho_c/c^2.
```

The boundary Cauchy functions satisfy

```text
H_1(z)=H_2(z)+z sum_c w_c/(1-s_c z^2),
```

and the origin moments satisfy

```text
beta_n(Omega_1)=beta_n(Omega_2)+sum_c w_c s_c^n.
```

Under `rho_c<=0`, every weight is nonnegative. Thus one outer positive
Stieltjes measure transports inward by adding positive atoms.

### Terminal affine remainder gate

Define `TAIR105360` by

```text
H_N(z) -> a z locally uniformly near zero,
a >= 0,
```

along the exact regular symmetric exhaustion. Equivalently,

```text
beta_0(Omega_N) -> a,
beta_n(Omega_N) -> 0 for every n>=1,
```

with one fixed-disk analytic bound.

Assuming `CRVH105330`, every crossed residue is nonpositive and every fixed
inner boundary function has the positive measure

```text
nu_m
 = a delta_0
   + sum_(c>0 outside Omega_m)
       (-2 rho_c/c^2) delta_(1/c^2).
```

Therefore

```text
CRVH105330 AND TAIR105360 -> OASH105350 -> RH.
```

Neither `CRVH105330` nor `TAIR105360` is proved for the last defective
low-order Xi derivative. RH remains unproved.

### Binding firewall

A positive terminal slope alone is insufficient. The odd entire function

```text
H(z)=z-z^3
```

has `H'(0)=1`, but its second confluent moment matrix is

```text
[[1,0],[0,-1]],
```

with determinant `-1`. The full affine-germ limit, not merely the first
coefficient, is load bearing.

### Replay

```text
PASS_X_105360_TERMINAL_STIELTJES_TRANSPORT
43 exact rational checks
```

The replay authenticates finite rational atomic transport only. It does not
evaluate Xi or prove either source-specific gate.
