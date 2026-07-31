# L-16213 — A quadratic-log Fourier cutoff suffices for the exact Xi source in the moving Hardy norm

Claim ID: `L-16213`  
Status: **PROVED FROM STANDARD XI STRIP DECAY**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `T-15101`; Stirling bounds for the completed zeta function

## 1. Purpose

The complete-frame theorem `T-16204` becomes substantially more plausible if
the finite dimension grows much more slowly than the radial scale

```text
R_lambda=2pi lambda^2.
```

The exact global Hermite radical has Fourier--Mellin transform `Xi`. Gamma-factor
decay implies that only

```text
N_lambda=O((log lambda)^2)
```

centered Fourier modes are needed to approximate this target in a Hardy norm
whose strip width tends to `1/2`.

Thus the growing profile packet may have polylogarithmic, rather than prolate
bandwidth-sized, dimension.

## 2. Exact source and coordinates

Let

```text
K(t)=k(exp t),
t in R,                                                    (L-16213.1)
```

where `k` is the exact global Hermite radical of `T-15101`. In the declared
normalization,

```text
Fourier(K)(z)=Xi(z).                                      (L-16213.2)
```

Put

```text
L=log lambda,
phi_(n,L)(t)=(2L)^(-1/2)exp(i pi n t/L),
|t|<=L,                                                    (L-16213.3)
```

and let `P_(L,N)` be the ordinary Fourier projection onto `|n|<=N`.

For `0<=tau<1/2`, write

```text
||f||_(L,tau)^2
 =integral_(-L)^L |f(t)|^2 2cosh(2tau t)dt.               (L-16213.4)
```

## 3. Standard Xi strip bound

For every fixed `tau_0<1/2`, Stirling's formula for the gamma factor and a
standard polynomial vertical-strip bound for zeta give constants `A,C` such
that

```text
boxed:
|Xi(x+iy)|
 <=C(1+|x|)^A exp(-pi|x|/4),
|y|<=tau_0.                                               (L-16213.5)
```

Only the real-axis case is needed for the coefficient estimate below. Directed
production may replace (L-16213.5) by an explicit Stirling remainder and an
explicit convexity bound.

The logarithmic source `K` and all its fixed exponential weights below
`1/2` are rapidly decreasing. In particular, for every `B>0`,

```text
integral_(|t|>L)|K(t)|^2 exp(2tau_0|t|)dt
 =O_B(exp(-BL)).                                         (L-16213.6)
```

For the Hermite arithmetic source the actual support-tail decay is much faster.

## 4. Fourier coefficients

Let

```text
c_n(L)=<K,phi_(n,L)>_(L2(-L,L)),
omega_n=pi n/L.                                          (L-16213.7)
```

Using (L-16213.2),

```text
c_n(L)
 =(2L)^(-1/2)Xi(omega_n)+epsilon_n(L),                    (L-16213.8)
```

where Cauchy--Schwarz and (L-16213.6) give, uniformly in `n`,

```text
|epsilon_n(L)|<=O_B(exp(-BL))/sqrt(L).                   (L-16213.9)
```

The uniform error cannot be summed over infinitely many `n` as written; instead
apply integration by parts to the support-tail difference. For every `m`,

```text
|epsilon_n(L)|
 <=C_(B,m) exp(-BL)
   sqrt(L)(1+|n|)^(-m).                                  (L-16213.10)
```

Thus its square tail is superexponentially negligible for the schedules below.

## 5. Ordinary projection tail

Parseval and (L-16213.5) imply

```text
||(I-P_(L,N))K||_(L2(-L,L))^2
 <=C L^C
   exp[-pi^2 N/(2L)]
 +O_B(exp(-BL)).                                         (L-16213.11)
```

Indeed

```text
|Xi(pi n/L)|^2
 <=C(1+n/L)^(2A) exp[-pi^2|n|/(2L)],                    (L-16213.12)
```

and the remaining geometric-polynomial series is bounded by its first term
times a power of `L+N`.

## 6. Moving Hardy tail

On `[-L,L]`,

```text
2cosh(2tau t)<=2exp(2tau L).                              (L-16213.13)
```

Therefore

```text
boxed:
||(I-P_(L,N))K||_(L,tau)^2
 <=C L^C
  exp[2tau L-pi^2N/(2L)]
 +O_B(exp[-(B-2tau)L]).                                  (L-16213.14)
```

Let

```text
tau_L->1/2,
N_L=ceil(cL^2),                                           (L-16213.15)
```

with one fixed

```text
boxed:
c>2/pi^2.                                                (L-16213.16)
```

Since `2tau_L<=1+o(1)`,

```text
2tau_LL-pi^2N_L/(2L)
 <=-[pi^2c/2-1+o(1)]L.                                  (L-16213.17)
```

The bracket is positive, so

```text
boxed:
||(I-P_(L,N_L))K||_(L,tau_L)->0.                         (L-16213.18)
```

The simple deterministic choice

```text
N_L=ceil(L^2)                                             (L-16213.19)
```

is more than sufficient.

## 7. Full target error

Combining (L-16213.18) with the global support tail gives

```text
boxed:
||K-P_(L,N_L)(1_[-L,L]K)||_(tau_L)->0.                   (L-16213.20)
```

The same conclusion holds for the repaired moving prolate target once its
source-specific Hardy difference from `K` tends to zero as in `L-16208`.

## 8. Dimension versus radial scale

With `L=log lambda`,

```text
m_lambda=2N_L+1=O((log lambda)^2),                        (L-16213.21)
```

while

```text
R_lambda=2pi lambda^2.                                   (L-16213.22)
```

Hence, for every fixed power `q`,

```text
boxed:
m_lambda^q/R_lambda->0.                                 (L-16213.23)
```

This gives ample room for dimension factors in an operator-valued local Weyl
error or fold-variation estimate.

## 9. Consequence for the growing frame

A complete exact-radical source frame for the finite diagonal criterion need
only span a Fourier space of polylogarithmic dimension. The source-profile
problem is therefore not a simultaneous asymptotic for `O(lambda^2)` modes.
It is enough to construct and control

```text
O((log lambda)^2)                                        (L-16213.24)
```

source directions at radial frequency scale `O(lambda^2)`.

This does not prove the uniformly conditioned frame of `T-16204`, but it removes
a potentially fatal dimension mismatch.

## 10. Proof boundary

The theorem uses the exact Xi transform normalization and standard completed-zeta
strip decay. A production artifact should retain explicit constants and
normalization. It does not construct the growing exact-radical source frame or
prove its tail scalarization. It does not prove RH.
