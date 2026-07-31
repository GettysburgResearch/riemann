# L-16222 — Integrated Dunster normalization and directed radial remainder

Claim ID: `L-16222`  
Status: **PROVED FROM DUNSTER'S DECLARED ENVELOPE BOUND AND STANDARD BESSEL INEQUALITIES**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: `L-16217`; Dunster equation (6.5); standard Bessel-envelope bounds

## 1. Purpose

`L-16217` fixes the radial amplitude exactly by unitarity. This lemma completes
the analytic translation of Dunster's pointwise radial approximation into the
`L2` leakage normalization used by the arithmetic tail.

The key observation is that the Bessel-template norm can be compared to an
exact modified-Bessel product without approximating the inverse Liouville map.

## 2. Radial Bessel template

For order `m=0`, put

```text
B_(sigma,gamma)(z)
 ={(z^2-1)(z^2-sigma^2)}^(-1/4)
  xi_sigma(z)^(1/2) J_0(gamma xi_sigma(z)),               (L-16222.1)
```

where

```text
xi_sigma(z)
 =integral_1^z sqrt((t^2-sigma^2)/(t^2-1))dt,
1<z<infinity.                                             (L-16222.2)
```

Let `z_sigma(xi)` be the inverse map. Since

```text
sqrt(1-sigma^2) t/sqrt(t^2-1)
 <=sqrt((t^2-sigma^2)/(t^2-1))
 <=t/sqrt(t^2-1),                                        (L-16222.3)
```

integration gives

```text
sqrt(1-sigma^2)sqrt(z^2-1)
 <=xi_sigma(z)
 <=sqrt(z^2-1).                                           (L-16222.4)
```

Put `a=1-sigma^2`. Inverting (L-16222.4) yields

```text
sqrt(1+xi^2)
 <=z_sigma(xi)
 <=sqrt(1+xi^2/a).                                        (L-16222.5)
```

Consequently

```text
a/(1+xi^2)
 <=1/(z_sigma(xi)^2-sigma^2)
 <=a^(-1)/(1+xi^2).                                      (L-16222.6)
```

## 3. Exact transformed norm

Since

```text
dxi/dz=sqrt((z^2-sigma^2)/(z^2-1)),                      (L-16222.7)
```

a direct change of variables gives

```text
boxed:
||B_(sigma,gamma)||_2^2
 =integral_0^infinity
  xi J_0(gamma xi)^2
  /(z_sigma(xi)^2-sigma^2)d xi.                          (L-16222.8)
```

At `sigma=0`, `z_0(xi)^2=1+xi^2`. The classical Hankel resolvent identity gives

```text
integral_0^infinity
 xi J_0(gamma xi)^2/(1+xi^2)d xi
 =I_0(gamma)K_0(gamma).                                  (L-16222.9)
```

Combining (L-16222.6)--(L-16222.9),

```text
boxed:
a I_0(gamma)K_0(gamma)
 <=||B_(sigma,gamma)||_2^2
 <=a^(-1) I_0(gamma)K_0(gamma).                          (L-16222.10)
```

The standard large-argument expansions imply

```text
I_0(gamma)K_0(gamma)
 =(2gamma)^(-1)[1+O(gamma^-2)].                           (L-16222.11)
```

Hence, uniformly for `sigma^2<=1/2`,

```text
boxed:
||B_(sigma,gamma)||_2^2
 =(2gamma)^(-1)[1+O(sigma^2+gamma^-2)].                  (L-16222.12)
```

## 4. Integrated Dunster envelope

Dunster's equation (6.5) gives an error of the form

```text
|E_(sigma,gamma)(z)|
 <=C gamma^-1
 {(z^2-1)(z^2-sigma^2)}^(-1/4)
 xi^(1/2) env J_0(gamma xi),                              (L-16222.13)
```

with `C` uniform in his declared parameter range.

Use the elementary envelope bounds

```text
env J_0(y)^2<=C(1+|log y|^2),   0<y<=1,                 (L-16222.14)

env J_0(y)^2<=C/y,              y>=1.                   (L-16222.15)
```

Transforming as in (L-16222.8), the interval `0<xi<=gamma^-1` contributes
`O(gamma^-2)` to the squared envelope norm, and the remaining interval
contributes `O(gamma^-1)` by (L-16222.6). Therefore

```text
||envelope template||_2^2<=C/gamma,                      (L-16222.16)
```

and

```text
boxed:
||E_(sigma,gamma)||_2<=C gamma^(-3/2).                   (L-16222.17)
```

Since `||B||_2=Theta(gamma^-1/2)`, the relative `L2` radial error is

```text
boxed:
||E||_2/||B||_2=O(gamma^-1).                             (L-16222.18)
```

## 5. Canonical normalized profile

With the notation of `L-16217`, Dunster's actual radial function is

```text
Psi_n=A_n[B_n+E_n].                                      (L-16222.19)
```

The exact leakage normalization (L-16217.23) gives

```text
A_n=(s_n/chi_n)/||B_n+E_n||_2.                           (L-16222.20)
```

Thus the canonical unit radial leakage profile satisfies the exact identity

```text
boxed:
rho_(n,lambda)
 =(B_n+E_n)/||B_n+E_n||_2.                               (L-16222.21)
```

In particular, the Dunster constants `p_n^0,q_n^0` cancel completely from the
normalized profile.

Dunster's quantization and `L-16219` give, uniformly for
`n=O((log lambda)^2)`,

```text
sigma_n^2=O((n+1)/gamma).                                (L-16222.22)
```

Equations (L-16222.12), (L-16222.17) and (L-16222.22) therefore imply

```text
boxed:
||rho_(n,lambda)-sqrt(2gamma)B_(sigma_n,gamma)||_2
 <=C(n+1)/gamma.                                         (L-16222.23)
```

The harmless `gamma^-1` contribution has been absorbed into `n+1`.

## 6. Directed version

Every step has a finite outward-rounded interface:

```text
sigma interval;
Dunster envelope constant C;
directed I_0(gamma),K_0(gamma);
rational bounds in (L-16222.6);
small/large Bessel-envelope constants;
exact chi_n and d_n intervals.                            (L-16222.24)
```

The checker first proves the two-sided template norm, then charges the integrated
envelope, and finally normalizes through the exact identity (L-16222.21). No
superexponentially small absolute quantity is subtracted.

## 7. Consequence for the requested amplitude gate

The first requested item is now closed in the correct relative form:

```text
boxed:
radial leakage amplitude
 =sqrt(d_n(1+chi_n)/2),                                  (L-16222.25)

normalized radial profile
 =sqrt(2gamma) times Dunster's Bessel template
  +O_L2((n+1)/gamma).                                    (L-16222.26)
```

For the quadratic-log packet and `gamma=2pi lambda^2`, the relative error is

```text
O((log lambda)^2/lambda^2)->0.                           (L-16222.27)
```

## 8. Proof boundary

This lemma controls the additive Fourier leakage. The multiplicative arithmetic
Poisson sum can still contain endpoint aliases and two-stationary-branch
interference. Those are treated by `L-16221` and the scope correction
`R-16203`; they do not affect the exact amplitude theorem.
