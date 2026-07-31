# L-16223 — Selberg-moment local Weyl theorem for growing oscillatory phase packets

Claim ID: `L-16223`  
Status: **PROVED UNCONDITIONAL ON THE CRITICAL-LINE ZERO PARAMETERS**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Primary input: Selberg's fixed moment theorem for `S(t)`

## 1. Purpose

`R-16203` shows that the two stationary radial branches can make the total
variation of the profile density `Theta(R)`. The absolute-variation theorem
`L-16220` then gives no saving.

The Riemann--von Mangoldt remainder is not an arbitrary bounded function. Selberg
proved fixed even moments for

```text
S(t)=N(t)-M(t),                                           (L-16223.1)
```

with Gaussian order. Hölder's inequality therefore controls the oscillatory
standing-wave density in an `L^q` derivative norm. On the quadratic-log packet,
the resulting error is `o(log R)`.

This theorem treats the line-centered zero parameters. `R-16204` explains why
off-line horizontal displacements require a separate argument.

## 2. Selberg moment input

For every fixed integer `k>=1`, Selberg's theorem gives

```text
boxed:
integral_T^(2T) |S(t)|^(2k)dt
 <=C_k T(log log T)^k                                   (L-16223.2)
```

for sufficiently large `T`. The full moment asymptotic is stronger; only this
upper bound is used.

Let

```text
p=2k,
q=p/(p-1).                                                (L-16223.3)
```

For every compact interval `I subset (0,infinity)`, dyadic decomposition gives

```text
boxed:
||S(R .)||_(L^p(I))
 <=C_(I,k)(log log R)^(1/2).                              (L-16223.4)
```

## 3. Operator density and counting remainder

Let `Y_R` be a finite-dimensional Hilbert space, whose dimension may grow. Let

```text
Phi_R(x):Y_R->C,
H_R(x)=Phi_R(x)^*Phi_R(x),                                (L-16223.5)
```

with `H_R` absolutely continuous and supported in one fixed compact
`I subset (0,infinity)`. Define

```text
W_(q,R)
 :=sup_(||u||=||v||=1)
   ||d/dx <u,H_R(x)v>||_(L^q(I)).                         (L-16223.6)
```

The centered Riemann--von Mangoldt remainder in the zero-side matrix is

```text
E_R^S
 =(1/R) integral_I H_R(x)dS(Rx).                         (L-16223.7)
```

Stieltjes integration by parts gives, weakly,

```text
<u,E_R^S v>
 =-(1/R) integral_I S(Rx)
   d/dx<u,H_R(x)v>dx.                                    (L-16223.8)
```

Hence Hölder and (L-16223.4) give the dimension-free bound

```text
boxed:
||E_R^S||_op
 <=C_(I,k)(log log R)^(1/2) W_(q,R)/R.                   (L-16223.9)
```

Thus

```text
boxed:
W_(q,R)
 =o(R log R/sqrt(log log R))                             (L-16223.10)
```

is sufficient for a relative `o(log R)` local Weyl error.

## 4. Finite-branch Fourier packets

Assume that, after a finite smooth partition, the profile has the form

```text
Phi_R(x)c
 =sum_(a=1)^B
  A_a(x) exp(iR psi_a(x))
  sum_(n=0)^(m_R-1)c_n b_(a,n)(x)exp(in theta_a(x)),      (L-16223.11)
```

where:

1. `B` is fixed;
2. `A_a,psi_a,theta_a` have uniformly bounded first derivatives;
3. each `theta_a` is a diffeomorphism with derivative bounded above and below;
4. multiplication by `b_(a,n)` and its derivative is a uniformly bounded
   diagonal operator on coefficient space;
5. the coefficient metric is uniformly equivalent to ordinary `ell^2`.

These are the standard finite-branch WKB hypotheses away from a fold.

Nikolskii's inequality for a trigonometric polynomial of degree below `m_R`
gives

```text
||sum c_n exp(in theta)||_(L^(2q))
 <=C m_R^[1/2-1/(2q)]||c||_2
 =C m_R^(1/(4k))||c||_2.                                (L-16223.12)
```

Differentiating (L-16223.11), the common radial phases cost `R`, while the mode
phase costs at most `m_R`. Applying Hölder to the two factors in

```text
d/dx [conjugate(Phi_Ru)Phi_Rv]                           (L-16223.13)
```

gives

```text
boxed:
W_(q,R)
 <=C[R m_R^(1/(2k))
      +m_R^(1+1/(2k))].                                  (L-16223.14)
```

No entrywise matrix summation is used.

## 5. Quadratic-log packet

Take `k=2`, so `p=4`, `q=4/3`. If

```text
m_R=O((log R)^2),                                        (L-16223.15)
```

then (L-16223.9) and (L-16223.14) give

```text
boxed:
||E_R^S||_op
 <=C sqrt(log R log log R)+o(1)
 =o(log R).                                               (L-16223.16)
```

Thus the two-stationary-branch interference identified in `R-16203` is not a
critical-line scalarization obstruction. Its `Theta(R)` derivative is absorbed
by Selberg's fourth moment and the `L^(4/3)` packet estimate.

More generally, any fixed `k>1` closes packets satisfying

```text
m_R^(1/(2k))sqrt(log log R)=o(log R).                     (L-16223.17)
```

## 6. Fold neighborhood

A nondegenerate fold is treated separately on a window of width
`O(R^(-2/3)polylog R)`. The standard uniform Airy approximation gives profile
height `O(R^(1/6))` and product-density variation `O(R^(1/3)polylog R)`.
Using the absolute Stieltjes estimate only on that shrinking window costs

```text
O(R^(-2/3)polylog R log R)=o(1),                         (L-16223.18)
```

after the exact normalized amplitude is inserted. Hence the fold can be
spliced to the phase-packet estimate without a uniform pointwise derivative.

The numerical constants and exact Airy window are part of a production
Dunster/CCM enclosure; the asymptotic power budget is all that is used here.

## 7. Main density and bounded correction

On a compact profile-frequency interval away from zero,

```text
log(|x|/(2pi))                                            (L-16223.19)
```

is a bounded multiplier. Therefore the nonconstant main-density correction

```text
C_R=(1/(2pi)) integral H_R(x)log(|x|/(2pi))dx             (L-16223.20)
```

has operator norm bounded by the multiplier supremum times the profile Gram.
This remains dimension-free.

Combining the main density with (L-16223.16) gives

```text
boxed:
A_R=(log R)D_R+O_op(1)+o_op(log R)                       (L-16223.21)
```

for the line-centered zero parameters, provided the profile Gram has a uniform
positive floor.

## 8. Proof boundary

- The local Weyl estimate and phase-packet dimension accounting are exact.
- Selberg's moment theorem is an imported unconditional theorem.
- Dunster's radial expansion supplies the two-branch/Airy architecture, but a
  production certificate still needs directed constants.
- The theorem does not replace the off-line horizontal coordinates by their
  ordinates. `R-16204` shows that this cannot be done by a generic Taylor bound.
- No RH conclusion is claimed here.
