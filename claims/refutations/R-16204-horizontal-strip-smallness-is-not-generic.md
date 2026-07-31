# R-16204 — Off-line horizontal displacement is not a generic small profile error

Claim ID: `R-16204`  
Status: **REFUTED AS A GENERAL LOCAL-WEYL INFERENCE**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Targets: generic horizontal-strip closure in `L-16209/L-16210/T-16204`

## 1. Purpose

A zeta zero has centered parameter

```text
s_rho=gamma+i delta,
|delta|<1/2.                                               (R-16204.1)
```

After scaling by the radial frequency `R`, the imaginary displacement is only
`delta/R`. If the profile derivative is uniformly bounded, this is a small
error. Radial profiles oscillate at frequency `R`, however, so a displacement
of size `1/R` can change the two-branch interference by order one.

This is not repaired by pairing the reflected zeros. The exact example below
shows that a generic horizontal-strip estimate cannot be obtained from the
Riemann--von Mangoldt count and the strip bound alone.

## 2. Exact two-branch profile

Take the entire real profile

```text
Phi_R(z)=exp(iRz)+exp(-iRz)=2cos(Rz).                     (R-16204.2)
```

For a centered zero displacement `y`, the scalar zero-side kernel is

```text
K_R(x,y)
 =conjugate(Phi_R(x-iy))Phi_R(x+iy).                     (R-16204.3)
```

Since `Phi_R` has real Taylor coefficients,

```text
K_R(x,y)=4cos^2(Rx+iRy).                                 (R-16204.4)
```

Pair the functional-equation reflected displacements `y` and `-y`. For

```text
y=delta/R,                                               (R-16204.5)
```

one obtains exactly

```text
boxed:
K_R(x,delta/R)+K_R(x,-delta/R)
 =4[1+cos(2Rx)cosh(2delta)].                              (R-16204.6)
```

On the critical line the corresponding pair is

```text
K_R(x,0)+K_R(x,0)=4[1+cos(2Rx)].                         (R-16204.7)
```

Therefore

```text
boxed:
Delta K_R(x,delta)
 =4cos(2Rx)[cosh(2delta)-1].                             (R-16204.8)
```

For every fixed nonzero `delta`, this is order one. The first-order Taylor term
cancels under reflection, but the second-order term is not small because
`partial_y^2K_R=Theta(R^2)`.

## 3. The common center phase does cancel

For a profile written as

```text
widehat T(s)
 =R^(-1/2)exp(-isx_0)Phi_R(s/R),                          (R-16204.9)
```

the common factor `exp(-isx_0)` cancels exactly in the zero-side product.
Thus (R-16204.8) is not an artifact of the tail center. It is the intrinsic
interference between the incoming and outgoing radial branches.

A single branch `exp(iRz)` has `K_R(x,y)=1` and is independent of `y`; the
obstruction is precisely the cross-branch term.

## 4. Riemann--von Mangoldt counting does not control the cross phase

The unconditional counting formula determines the number of ordinates in a
long interval up to an error `O(log T)`. It does not control the exponential sum

```text
sum_gamma cos(2gamma) w_gamma,                            (R-16204.10)
```

where

```text
w_gamma=cosh(2delta_gamma)-1>=0.                          (R-16204.11)
```

An abstract counting sequence can obey the same main counting law and
`O(log T)` discrepancy while placing `Theta(log T)` ordinates in narrow
neighborhoods of successive maxima of `cos(2gamma)`. Its weighted cross sum is
then of the same order as the total count. Hence no theorem based only on the
Riemann--von Mangoldt remainder and `|delta|<=1/2` can turn (R-16204.8) into
`o(log R)` after normalization.

This does not assert that the actual zeta zeros have such a distribution. It
shows that the proposed universal local-Weyl proof does not contain enough
information to exclude it.

## 5. Relation to `L-16223`

On the critical line, `delta=0`, and Selberg's moments of the actual counting
remainder control the two-branch oscillation. `L-16223` proves the resulting
`o(log R)` operator error for the quadratic-log packet.

For off-line zeros, the unknown weights (R-16204.11) are correlated with the
zero ordinates. Selberg's theorem for the unweighted argument function does not
bound this weighted exponential sum.

## 6. Correct alternatives

A positive proof must supply genuinely additional input. Possible interfaces
are:

1. an arithmetic/prime-side analysis of the localized Weil form that never
   replaces the complex zero parameters by real ordinates;
2. a theorem controlling the weighted off-line exponential sum
   (R-16204.10);
3. a one-branch or endpoint-jet source construction that removes the radial
   cross term;
4. a positivity/floor theorem obtained by the deficit-augmentation or harmonic
   Schur machinery without zero-side scalarization;
5. RH itself, in which case every `delta_gamma` is zero—but using this to prove
   the positive theorem would be circular.

## 7. Corrected status

```text
exact radial amplitude normalization:               PROVED
critical-line two-branch local Weyl error:           PROVED
Riemann--von Mangoldt main scalar term:              PROVED
generic off-line horizontal replacement:            REFUTED
complete unconditional growing-frame scalarization: OPEN / RH-BEARING
```

The four-gate transfer theorem remains a valid sufficient criterion. This
refutation identifies why its last source-specific hypothesis cannot be proved
from Dunster asymptotics and zero counting alone. No RH conclusion is claimed.
