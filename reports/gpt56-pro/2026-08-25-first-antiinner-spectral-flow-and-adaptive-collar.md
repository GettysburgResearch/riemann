# First anti-inner spectral flow and the adaptive source/index collar

The T105630 safe causal theorem is naturally indexed by total analytic height
`H=b+h`.  It therefore remains valid whenever `H>beta_1`, not merely when the
base itself exceeds `beta_0`.

The first failure below that domain is completely explicit.  If one simple
Xi-prime zero enters the shifted upper half-plane at depth `delta`, the boundary
phase changes from an inner function `A` to

```text
U = conjugate(B_b) A.
```

Its adverse Hankel operator is rank one:

```text
H_U^* H_U = |A(b)|^2 P_(phi_b),
phi_b(xi)=sqrt(2 delta) exp(-delta xi-i alpha xi).
```

For a source-frequency bank `[0,L]`, the full charge splits exactly as

```text
visible source charge = |A(b)|^2(1-exp(-2 delta L));
signed endpoint charge = |A(b)|^2 exp(-2 delta L).
```

Thus a first crossing is invisible to every fixed band, but no topological
charge is lost: it escapes to frequencies of order `1/delta` and reappears in
the signed endpoint complement.

The actual current weight obeys

```text
r_(b,h)(xi) <= (h/H) exp(-H xi),
```

so the current-weighted charge of a depth-`delta` factor is at most

```text
2 h delta / (H(H+2 delta)).
```

It vanishes linearly at contact.  The transverse spectral-flow derivative,
not the static energy, is the nonzero object at the boundary.

The correct cofinal architecture is therefore hybrid:

```text
delta L >= c:  source contraction sees at least 1-exp(-2c) of the charge;
delta L < c:   retain the exact signed endpoint/index term in a collar c/L.
```

This replaces the false fixed-band source-only descent target.  The remaining
work is to control the Xi-prime divisor in the microscopic collar, couple its
signed spectral flow to the parent Xi Clark/zero-height atom, and retain the
actual two-trace point evaluation.  RH remains unproved.
