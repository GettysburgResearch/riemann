## T105640 addendum — uniform Xi curvature and the critical-depth collar

**The Riemann Hypothesis remains unproved.**

### Uniform source theorem

The standard Xi Fourier kernel satisfies

```text
-(log Phi)'' > 20476/2345 > 8
```

on the complete real line. The proof is a self-contained theta-mixture bound:
the first orbit has weight `>200/201` and the complete score variance consumes
less than `1881/7000` of its elementary curvature floor.

This is strong log-concavity only; no `TP_infinity` or RH implication is
asserted.

### Exponential current/Turan envelope

At total height `H`,

```text
R_H(xi)
 = exp(-H xi) / E[sinh(2H X)/(2H X)]
 <= exp(-H xi).
```

For a base `b`, physical scale `h`, and `H=b+h`,

```text
r_(b,h)(xi) <= (h/H) exp(-H xi).
```

Combined with T105630, the actual source profile is monotone and exponentially
enveloped.

### Exact anti-inner depth price

For every finite upper-half-plane inner function,

```text
tr_(K_B) M_(exp(-H xi))
 = 1/(2 pi H) integral_R (1-|B(x+iH/2)|^2) dx.
```

One shifted zero at depth `y` costs exactly

```text
2y/(H+2y).
```

Hence the Xi-prime anti-inner packet above total height `H` obeys

```text
tr_(K_B) M_(r_(H,h))
 <= (2h/H^2) integral_H^beta1 N_1(T;t) dt.
```

At `H=beta1-delta`, `delta<=beta1/2`, this is at most

```text
(4 delta/beta1) N_1(T;H).
```

Thus every fixed-depth packet is paid. Only a vanishing boundary collar can be
source-cheap.

### Binding firewall

A one-zero Blaschke factor has degree one while its weighted charge
`2y/(H+2y)` tends to zero. Therefore the source-charge estimate does not remove
the zero. The live target is the signed/pointwise conversion of the microscopic
collar:

```text
BCOLLAR105643.
```

### Replay

```text
PASS_X_105640_STRONG_LC_DEPTH_COLLAR
checks=4219
769c7f5f517949d0591e8cc33032a6f081abbf5ea43ad53556daeac2499b4a69
RH_UNPROVEN
```

### Updated frontier

```text
strong Xi source curvature                    PROVED / REVIEW
profile exponential envelope                  PROVED EXACT
model-space exponential trace                 PROVED EXACT
anti-inner soft-depth collar                  PROVED EXACT
weighted charge -> degree                     REFUTED
BCOLLAR105643                                  OPEN / RH-BEARING
POINTID105630                                  OPEN / RH-BEARING
ENDIDX105630                                   OPEN
Riemann Hypothesis                            UNPROVEN
```