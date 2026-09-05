## T-106630 — constructive shallow Cauchy transport

The T-106620 shallow canonical-correlation deficit now has an exact primal
certificate. For each mesoscopic cross-ratio, let `E_-`, `E_+` synthesize the
shallow denominator and a selected numerator confluent Cauchy block. Every
matrix `X` gives

```text
R(X)
= tr G_-^(-1)
  [G_- - C X - X* C* + X* G_+ X].
```

Exactly,

```text
canonical defect = inf_X R(X),
X_opt             = G_+^(-1) C*.
```

The gap of an approximate transport is the positive normal-equation error

```text
tr G_-^(-1) Y* G_+^(-1) Y,
Y=G_+ X-C*.
```

Thus a proof no longer has to estimate an opaque phase mean directly: it may
exhibit a concrete Cauchy-kernel transport and certify its positive residual.
A numerator subfactor is sufficient; extra favorable directions only help.

For one pole pair the cost is the squared pseudohyperbolic distance. Raw
pairwise costs cannot be summed without whitening; an exact two-column
counterexample is retained.

`MESOTRANS106630` asks for total generalized residual below `11/500 N`.
Together with the already-paid `3/40 N` deep charge and the fifth-derivative
input, it implies more than 90%. The transport estimate, 90%, and RH remain
open.
