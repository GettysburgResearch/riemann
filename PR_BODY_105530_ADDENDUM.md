## Checkpoint H — Hermitian bank and matrix companion flux (T-105530)

The scalar triangular Wick square from T-105510 does not by itself solve the
off-real Hermitian polarization.  The exact scalar expansion proves that once
its linear term is cancelled, an unavoidable `-z*zbar/4` second-chaos term
remains, independent of the scalar quadratic coefficient.

A minimal two-channel bank repairs this at the folded boundary level:

```text
w0(z)=1-z/2-z^2/4
w1(z)=z/2
```

For `r(z)=Re (1-z)^(-1)`, the unique nonzero channel eigenvalue

```text
Lambda(z)=(|w0(z)|^2+|w1(z)|^2) r(z)
```

has no Hermitian bidegrees of total degree one or two and is strictly positive
for `|z|<1`.  The error is bounded explicitly by

```text
|Lambda(z)-1|
 <= r^3(4+3r+r^2)/(16(1-r)^2),  |z|<=r<1.
```

The scalar companion Lorentz identity is also polarized to a complete matrix
identity.  Its real-line bulk is PSD; all conclusion-bearing information is
now in one signed vertical/companion matrix flux.

The new exact AND-gate is

```text
BANKREAL105530 AND MATRIXLERC105531
  -> STRIPNEG105520
  -> N0/N > 0.9.
```

Both Xi estimates remain open.  Ninety percent and RH are unproved.
