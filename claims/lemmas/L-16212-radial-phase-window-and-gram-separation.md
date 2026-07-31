# L-16212 — A single-alias radial window separates the repaired mode-4 and mode-8 profiles

Claim ID: `L-16212`  
Status: **PROVED PHASE GEOMETRY; NORMALIZATION AND UNIFORM ERROR INSERTION OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Primary dependency: Dunster, *Asymptotics of Prolate Spheroidal Wave Functions*, radial fixed-mode formulas

## 1. Purpose

After `R-16202`, the tail-profile Gram must be proved for two exact-radical
combinations. Their leading leakage components are respectively mode 4 and mode
8. This lemma identifies a frequency interval in which:

1. only the first arithmetic Poisson alias can contribute by stationary phase;
2. the fixed-mode radial phases of modes 4 and 8 have a nonconstant relative
   phase;
3. the limiting two-profile Gram is therefore strictly positive.

The remaining analytic task is to insert the exact Dunster/Fuchs normalization
constants and uniform remainder bounds into this geometry.

## 2. Radial phase

Use the order-zero fixed-index radial PSWF normalization. Dunster introduces

```text
xi_n(z)
 =integral_1^z sqrt((t^2-sigma_n^2)/(t^2-1)) dt,
 z>1.                                                     (L-16212.1)
```

For fixed `n` and `gamma->infinity`, the separation parameter gives

```text
sigma_n^2=(2n+1)/gamma+O(gamma^-2).                       (L-16212.2)
```

On every compact interval

```text
1+epsilon<=z<=Z,
```

Taylor expansion under the integral is uniform and yields

```text
boxed:
gamma xi_n(z)
 =gamma sqrt(z^2-1)
  -(2n+1)/2 arccos(1/z)
  +O_(n,epsilon,Z)(gamma^-1).                            (L-16212.3)
```

Indeed

```text
sqrt((t^2-sigma^2)/(t^2-1))
 =t/sqrt(t^2-1)
  -sigma^2/[2t sqrt(t^2-1)]
  +O(sigma^4),                                           (L-16212.4)
```

and

```text
integral_1^z t/sqrt(t^2-1)dt=sqrt(z^2-1),

integral_1^z dt/[t sqrt(t^2-1)]=arccos(1/z).              (L-16212.5)
```

## 3. Logarithmic frequency map

Put

```text
z=exp(t),
t>=0,                                                     (L-16212.6)
```

and define the leading normalized phase

```text
phi(t)=sqrt(exp(2t)-1).                                   (L-16212.7)
```

Its logarithmic frequency is

```text
omega(z)=d/dt phi(t)
        =z^2/sqrt(z^2-1).                                (L-16212.8)
```

A direct derivative gives

```text
omega'(z)
 =z(z^2-2)/(z^2-1)^(3/2).                               (L-16212.9)
```

Therefore `omega` has its unique minimum at

```text
z=sqrt(2),
omega_min=2.                                             (L-16212.10)
```

This is the unique nondegenerate fold of the first radial alias.

## 4. Arithmetic aliases

For the `k`-th Poisson sample, the radial argument is

```text
z=k exp(t).                                               (L-16212.11)
```

Its leading logarithmic frequency is `omega(z)`. For every integer `k>=2`,
`z>=k>sqrt(2)`, so its smallest possible frequency is

```text
omega_k,min=k^2/sqrt(k^2-1).                             (L-16212.12)
```

The first competing alias is `k=2`, with threshold

```text
omega_2,min=4/sqrt(3).                                   (L-16212.13)
```

Hence every compact interval

```text
boxed:
J subset (2,4/sqrt(3))                                   (L-16212.14)
```

is a **single-alias window**: no `k>=2` term has a stationary point there.
Repeated integration by parts makes all higher-alias contributions
`O_J(gamma^-M)` for any fixed `M`, provided the radial amplitudes have the
standard finite symbol bounds.

## 5. Fixed-mode phase separation

Let

```text
theta(z)=arccos(1/z).                                    (L-16212.15)
```

From (L-16212.3), the relative radial phase of modes 8 and 4 is

```text
boxed:
gamma xi_8(z)-gamma xi_4(z)
 =-4 theta(z)+O(gamma^-1).                               (L-16212.16)
```

The function `theta` is strictly increasing for `z>1`. Therefore the relative
phase is not constant on either stationary branch over any nontrivial interval
`J` in (L-16212.14).

## 6. Local profile Gram

Assume the normalized radial leakage asymptotics take the standard WKB form on
the first alias,

```text
r_n(lambda z)/sqrt(d_n)
 =A(z) cos(gamma phi(log z)-(2n+1)theta(z)/2+vartheta)
  +epsilon_(n,gamma)(z),                                 (L-16212.17)
```

where on the stationary preimage of one compact `J`:

```text
0<a<=|A(z)|<=A_0,
||epsilon_(n,gamma)||_(symbol)<=O(gamma^-1).              (L-16212.18)
```

The common amplitude may be replaced by uniformly comparable mode-dependent
amplitudes without changing the conclusion.

Stationary phase on the two nondegenerate branches gives normalized spectral
profiles `Phi_4,Phi_8`. After discarding oscillatory cross-branch terms, their
limiting Gram on `J` is a finite positive weighted sum of matrices of the form

```text
[ 1                 exp(-4i theta(z)) ]
[ exp(4i theta(z))   1                  ].                (L-16212.19)
```

For a vector `(a,b)`, vanishing of its limiting quadratic form would require

```text
a+b exp(-4i theta(z))=0                                  (L-16212.20)
```

for almost every `z` in a nontrivial interval. Since `theta` is nonconstant,
this forces `a=b=0`.

By compactness of the unit sphere in `C^2`, the limiting local Gram has a
strictly positive minimum eigenvalue. Uniform stationary-phase errors then give

```text
boxed:
Gram_J(Phi_4,Phi_8)>=c_J I                               (L-16212.21)
```

for all sufficiently large `gamma`.

## 7. Exact-radical packet

The repaired target of `T-16201`, normalized by its tail scale, approaches the
mode-4 leakage profile because its mode-8 repair coefficient is
`O(d_4/d_8)`. The independent repaired complement approaches the mode-8
profile. Therefore (L-16212.21) transfers by a uniformly invertible `2 x 2`
change of basis to the exact-radical tail packet:

```text
boxed:
Gram_J(Phi_rad,1,Phi_rad,2)>=c'_J I.                     (L-16212.22)
```

Since the full profile Gram dominates its restriction to `J`, this proves the
nondegeneracy gate in corrected `T-16202` once the normalization/error hypothesis
(L-16212.17)--(L-16212.18) is supplied.

## 8. Fold and variation

The lower endpoint `omega=2` is a nondegenerate fold because

```text
omega'(sqrt(2))=0,
omega''(sqrt(2))!=0.                                      (L-16212.23)
```

A uniform Airy normal form at that fold gives product-density variation
`O(gamma^(1/3) polylog gamma)`, which is `o(gamma)` and therefore satisfies
`L-16210`. Away from the fold ordinary stationary phase gives `O(1)` variation
on compact frequency intervals.

This identifies the exact radial estimate needed for the complete profile
budget; it is not used to prove (L-16212.21), which works on a compact interval
strictly above the fold.

## 9. CCM scale

In the CCM normalization

```text
gamma=2pi lambda^2.                                      (L-16212.24)
```

Thus the normalized Mellin frequency scale is

```text
boxed:
R_lambda=2pi lambda^2.                                   (L-16212.25)
```

## 10. What remains

The phase geometry, single-alias window, and conditional Gram argument are
complete. The remaining source-level proof obligations are:

1. identify the CCM normalized Fourier leakage with Dunster's radial solution;
2. prove the amplitude normalization (L-16212.17) relative to `sqrt(d_n)`;
3. propagate Dunster's explicit error through the arithmetic Poisson sum;
4. prove the fold variation and horizontal-strip budgets globally.

These are scalar fixed-mode asymptotic estimates. No matrix-level
superexponential comparison remains.

## 11. Proof boundary

This lemma does not assert that (L-16212.17)--(L-16212.18) have been verified in
the CCM normalization. It proves that, once they are, the repaired profile Gram
cannot degenerate. It does not prove RH.
