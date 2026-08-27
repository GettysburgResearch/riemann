## T105350 addendum — one-anchor Stieltjes boundary reduction

This checkpoint strengthens the boundary half of `T-105330` without changing
its scientific status.

### Exact theorem

For any real analytic boundary Cauchy function `H` on an interval, all-packet
Loewner positivity is equivalent to positivity of every confluent Hankel matrix
at one fixed analytic anchor:

```text
[H^((r+s+1))(x_*)/(r+s+1)!]_(r,s<k) PSD for every k
iff
[ (H(x_i)-H(x_j))/(x_i-x_j) ] PSD for every real packet.
```

The forward direction is confluent. The reverse direction reconstructs a
compact positive Hamburger measure and a global Pick extension.

### Symmetric Xi specialization

For a definite-parity Xi derivative in a symmetric window, `H` is odd and the
canonical anchor is zero. Put

```text
beta_n=(2pi i)^(-1) integral_boundary
       (F/F')(zeta) / zeta^(2n+2) dzeta.
```

Then the boundary gate is exactly

```text
[beta_(r+s)] PSD and [beta_(r+s+1)] PSD at every order.
```

Equivalently,

```text
H(iy)/(iy)
 = (2pi i)^(-1) integral_boundary (F/F')(zeta)/(zeta^2+y^2) dzeta
```

is a Stieltjes transform of a positive measure.

Define this all-order origin hierarchy as `OASH105350`. Window by window,

```text
OASH105350 <=> BCVH105330 <=> boundary-PSD part of BRP105220.
```

Therefore

```text
CRVH105330 AND OASH105350 -> RH.
```

Neither gate is proved.

### Bounded-order firewall

The exact rational odd separator in `R-105350` passes the first two confluent
orders, while the third determinant is `-1/16`. Its selected three-node
Loewner packet has every one-/two-node principal restriction positive but full
determinant `-16/2025`. No finite-order bootstrap is claimed.

### Replay

```text
PASS_X_105350_ONE_ANCHOR_LOEWNER_HAMBURGER
159 exact rational checks
50c6c26c11155fd3c35d49830f5ff6f8b32b0f0b6294bf73f04ea7aeeec9aee4
```

The replay does not evaluate Xi or prove `CRVH105330`, `OASH105350`, the
moving saddle, `PRES105220`, `BRP105220`, or RH.
