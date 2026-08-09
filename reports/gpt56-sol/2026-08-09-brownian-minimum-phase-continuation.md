# Brownian raw stability continuation — 2026-08-09

Status: **multiple new exact finite/all-N reductions; cofinal quarter-plane stability open; RH unproved**

## New results in this continuation

### 1. Exact finite stability now reaches N=4

`L-34005` proves `M_3(z)!=0` on `Re z>=0`.

`L-34006` proves `M_4(z)!=0` on `Re z>=0` despite the first negative linear shift `alpha_(4,1)=-1/20`.

These are analytic two-region sector/Rouche proofs, not zero scans.

The stronger conjecture `M_N` zero-free on the entire right half-plane for all N is false in floating reconnaissance: the first finite zero branch crosses `Re z=0` around N~19 and approaches the true boundary `Re z=1/4` from the left.  This reconnaissance is not used as proof.

### 2. The all-N numerator is now a sine-tail canonical object

`L-34007` proves

```text
C_N(x)
 =4 prod_(k>N)(1-x^2/k^2)^2
 =4[sin(pi x)/(pi x prod_(k<=N)(1-x^2/k^2))]^2.
```

Thus the all-N numerator is a sampled derivative of the squared tail remaining after deleting the first N zero pairs from Euler's sine product.

### 3. Exact N-recursion

`L-34008` resolves each Gamma(2) variable into two exponentials and proves

```text
(1-N^-2 E^-1)^2 D_N(2z)=D_(N-1)(2z).
```

The stage `N-1 -> N` introduces exactly the two new forced Hermite zeros

```text
z=-(2N-2), -(2N-1)
```

and the new homogeneous frequency `N^(-2z)(Az+B)`.

### 4. Exact adverse-packet boundary

`L-34009` proves the sharp all-parameter theorem

```text
alpha_(N,i)<0  iff  N>=4 i^2.
```

Therefore the complete delicate packet is exactly

```text
1<=i<=floor(sqrt(N)/2).
```

The sqrt(N) scale is intrinsic, not an artifact of numerics or asymptotic truncation.

### 5. Order-statistic probability representation

`L-34010` defines independent Beta-prime(1,2) variables `Y_k` and

```text
U_k=log k + (1/2)log Y_k,
M_N=min_(k<=N) U_k.
```

Then

```text
P(M_N>u)
 =prod_(k<=N)(1+e^(2u)/k^2)^-2
```

and its hazard is strictly increasing:

```text
h_N(u)=4 sum_(k<=N) e^(2u)/(k^2+e^(2u)),
h_N'(u)>0.
```

Most importantly, in the genuine moment strip,

```text
D_N(2z)
 =sin(pi z)/(pi z) E[e^(-2z M_N)].
```

Hence the RH-facing finite theorem `1/4<Re z<1/2` is an honest bilateral-Laplace minimum-phase problem, not a meromorphic-continuation artifact.

After the critical Esscher tilt, it is exactly zero-freeness of

```text
E_nuN[e^(-2w M_N)],  0<Re w<1/4.
```

## External-theorem checks

Several tempting generic shortcuts were checked and rejected at their proper scope:

- GGC closure under powers does not imply multiplicative infinite divisibility or Mellin zero-freeness.
- IFR/increasing hazard does not have a generic minimum-phase theorem strong enough for the required bilateral transform.
- finite-order total positivity gives horizontal zero-free strips, but cannot distinguish the desired right/left half-plane geometry and would also exclude the legitimate approximating critical zeros.

## Current preferred Brownian attacks

1. **Growing packet theorem.**  Control the exact `i<=sqrt(N)/2` adverse packet collectively; every remaining shift is positive.
2. **Difference-equation stability.**  Use `L-34008` to prove the pair-addition boundary-value problem preserves `Re z<=1/4` for non-forced zeros.
3. **Canonical-product/Herglotz route.**  Use the positive tail Stieltjes score in `L-34007` to build a genuine side-sensitive canonical system.
4. **Minimum/order-statistic route.**  Exploit the explicit hazard/product structure of `L-34010`, but only with a theorem strong enough to control complex Laplace zeros after the critical tilt.

## Exact boundary

```text
Dirichlet-average factorization              complete exact
explicit all-N numerator                     complete exact
reciprocal Hermite identity                  complete exact
N=2,3,4 closed-right-half-plane stability    complete exact
squared sine-tail canonical weight           complete exact
serial-exponential N-recursion                complete exact
adverse packet i<=sqrt(N)/2                   complete exact
beta-prime minimum representation             complete exact
cofinal Re z>1/4 stability                    OPEN / RH-bearing
Riemann Hypothesis                            UNPROVED
```
