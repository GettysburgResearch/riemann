# L-16215 — A uniform polylogarithmic Fuchs window closes the growing radical-frame conditioning

Claim ID: `L-16215`  
Status: **PROVED ASYMPTOTIC TRANSFER; UNIFORM PROLATE INPUT OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-16213`, `L-16214`; the fixed-index Fuchs defect law and Hermite point values

## 1. Purpose

`L-16214` reduces the conditioning of the consecutive-triple exact-radical
frame to two scalar quantities:

```text
M_lambda r_*(lambda),
q_max(lambda)/q_min(lambda).                             (L-16215.1)
```

This lemma proves that both are polynomially controlled on the quadratic-log
cutoff as soon as the familiar fixed-index prolate asymptotics hold uniformly
through that polylogarithmic mode window.

No new PSWF asymptotic is claimed. The point is to isolate exactly how much
uniformity the positive route needs.

## 2. Defect model

Put

```text
c=2pi lambda^2.                                          (L-16215.2)
```

For a positive Fourier-prolate mode of index `n`, define the Fuchs model

```text
F_n(c)
 =2^(3n+1) sqrt(pi) c^(n+1/2) exp(-2c)/n!.              (L-16215.3)
```

The fixed-index theorem is

```text
d_n(lambda)=F_n(c)(1+o(1)).                              (L-16215.4)
```

Let

```text
M=M_lambda,
I_M={0,4,8,...,4(M+1)}.                                  (L-16215.5)
```

Assume the following **uniform Fuchs window**: for one fixed
`0<theta<1`, eventually

```text
boxed:
|d_n/F_n(c)-1|<=theta,
 n in I_M.                                                (L-16215.6)
```

It is enough below to take `theta<=1/3`.

## 3. Adjacent defect ratios

The model ratios are exact:

```text
F_(n+4)(c)/F_(n+8)(c)
 =[(n+5)(n+6)(n+7)(n+8)]/[4096 c^4].                    (L-16215.7)
```

Under (L-16215.6) with `theta<=1/3`,

```text
d_(n+4)/d_(n+8)
 <=2 F_(n+4)/F_(n+8).                                   (L-16215.8)
```

For sufficiently large `lambda`, the right side is below `1/2` uniformly on
`I_M`. Since the defects are increasing,

```text
r_j
 =(d_(n+4)-d_n)/(d_(n+8)-d_n)
 <=d_(n+4)/(d_(n+8)-d_(n+4))                            (L-16215.9)
```

with `n=4j`. Therefore

```text
boxed:
r_j
 <=4 F_(n+4)/F_(n+8)
 =[(n+5)(n+6)(n+7)(n+8)]/[1024 c^4].                    (L-16215.10)
```

Consequently

```text
boxed:
M r_*
 <= M(4M+8)^4/(1024 c^4)
 =O(M^5/c^4).                                            (L-16215.11)
```

For the schedule `M=O((log lambda)^2)` from `L-16213`,

```text
boxed:
M r_*
 =O((log lambda)^10/lambda^8)->0.                        (L-16215.12)
```

Thus the banded frame is a vanishing perturbation of the first-difference
frame by a very large margin.

## 4. Hermite point-value window

Let `Q_n` be the limiting normalized Hermite point value at zero in the CCM
Fourier convention. Up to one fixed normalization constant, for an even index
`n=2m`,

```text
|Q_(2m)|^2
 =binomial(2m,m)/4^m.                                    (L-16215.13)
```

Wallis bounds give constants `0<c_0<C_0` such that

```text
c_0(m+1)^(-1/2)
 <=|Q_(2m)|^2
 <=C_0(m+1)^(-1/2).                                     (L-16215.14)
```

Hence, on `n=0,4,...,4(M+1)`,

```text
boxed:
max|Q_n|/min|Q_n|<=C(M+1)^(1/4).                         (L-16215.15)
```

Assume the uniform growing-mode point-value approximation

```text
boxed:
|q_n/Q_n-1|<=theta_q<1,
 n in I_M.                                                (L-16215.16)
```

Then

```text
boxed:
q_max/q_min
 <=[(1+theta_q)/(1-theta_q)]C(M+1)^(1/4).                (L-16215.17)
```

## 5. Frame condition number

Insert (L-16215.12) and (L-16215.17) into `L-16214`. For sufficiently large
`lambda`,

```text
s_min(B)>=c/M,
s_max(B)<=3,                                              (L-16215.18)
```

and therefore the original coefficient frame satisfies

```text
boxed:
kappa(U_lambda)=O(M^(5/4)).                              (L-16215.19)
```

On the quadratic-log schedule,

```text
boxed:
kappa(U_lambda)
 =O((log lambda)^(5/2)).                                 (L-16215.20)
```

Thus the exact-radical source repair introduces only polylogarithmic
conditioning. In particular, every fixed power of the frame condition number
is `o(lambda^epsilon)` for every `epsilon>0`.

## 6. Dimension budget against the radial scale

Since

```text
M=O((log lambda)^2),
R_lambda=2pi lambda^2,                                   (L-16215.21)
```

one has, for every fixed `A,B`,

```text
boxed:
M^A kappa(U_lambda)^B/R_lambda->0.                       (L-16215.22)
```

This absorbs any fixed polynomial dimension or frame-conditioning loss in the
fold-admissible local-Weyl error.

## 7. Exact remaining prolate input

The growing frame algebra no longer requires a new matrix theorem. It requires
only the two scalar uniform windows:

```text
A. d_n=F_n(c)(1+O(theta))
   uniformly for n<=4M+4,

B. q_n=Q_n(1+O(theta_q))
   uniformly for n<=4M+4,                               (L-16215.23)
```

where

```text
M=O((log lambda)^2),
c=2pi lambda^2.                                          (L-16215.24)
```

Because `M=o(c^epsilon)` for every `epsilon>0`, this is a very small uniform
window compared with the full Shannon transition region `n=Theta(c)`.
Dunster's angular and radial expansions are the natural primary source for
proving it with directed constants.

## 8. Proof boundary

Equations (L-16215.7)--(L-16215.22) are elementary consequences of the declared
uniform windows. The windows themselves have not been reconstructed with
explicit uniform errors in the CCM normalization. This lemma does not prove the
growing arithmetic tail-frame inequality or RH.
