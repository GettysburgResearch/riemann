## T105646 addendum — Maxwell-equivalent current metric and universal height-owner law

**The Riemann Hypothesis remains unproved.**

### Strong source curvature

The standard Xi Fourier kernel satisfies

```text
-(log Phi)'' > kappa_0,
kappa_0=20476/2345>8.
```

### Maxwell sandwich

The exterior-square conditional law is monotone-likelihood dominated by the
Maxwell density proportional to

```text
x^2 exp(-kappa_0 x^2).
```

Its hyperbolic moment is exactly `exp(H^2/kappa_0)`. Therefore

```text
exp(-H xi-H^2/kappa_0)
 <= R_H(xi)
 <= exp(-H xi).
```

For every conclusion-facing height `H<=1/2`,

```text
(97/100) exp(-H xi) < R_H(xi) <= exp(-H xi).
```

Thus the actual current metric and the canonical exponential Paley–Wiener
metric are uniformly equivalent to within three percent.

### Exact zero-depth price

For one shifted Blaschke zero of depth `y`,

```text
tr_(K_B) M_(exp(-H xi))=2y/(H+2y),
```

and the actual current charge lies between `97/100` and `1` times this value in
the critical-height range.

### Positive height-owner law

For a zero `rho=alpha+i gamma` of `Xi'`, define

```text
Q_rho(H)
 =2(gamma-H) integral R_H(xi) exp(-2(gamma-H)xi) dxi.
```

Then

```text
Q_rho(0)=1,
Q_rho(gamma-)=0,
Q_rho is nonincreasing,
d nu_rho=-dQ_rho is a probability measure.
```

The explicit reference survival is

```text
S_gamma(H)=2(gamma-H)/(2gamma-H),
```

with density `2gamma/(2gamma-H)^2`. Uniformly for all Xi-prime zeros in the
critical strip,

```text
(97/100) S_gamma(H) < Q_rho(H) <= S_gamma(H).
```

Hence the actual and reference owner laws have Kolmogorov distance below
`3/100`. The actual mean owner height differs by less than `0.03 gamma` from

```text
2 gamma (1-log 2).
```

### Honest final transfer

```text
HOWNXFER105644

Identify the positive current-height owner law with the signed height flow of
the physical Xi-prime allpass, retaining two-trace point evaluation,
common-zero confluence and the cofinal endpoint ledger.
```

A shallow zero remains degree one even when its fixed-height weighted charge is
small; the new theorem distributes that integer as one positive unit across
all heights rather than claiming it disappears.

### Replay

```text
PASS_X_105640_STRONG_LC_DEPTH_COLLAR
checks=4223
b8d2c8770f38dbcace6a481f540d2fad1af8c01ad04fabde2ecc8167890adcf0
RH_UNPROVEN
```

### Boundary

```text
strong Xi source curvature                  PROVED / REVIEW
actual/exponential current metric 3% match   PROVED / REVIEW
one-zero positive height-owner law           PROVED EXACT
universal three-percent owner distribution   PROVED / REVIEW
HOWNXFER105644                               OPEN / RH-BEARING
BCOLLAR105643                                OPEN / RH-BEARING
POINTID105630                                OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```