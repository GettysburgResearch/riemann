# L-16224 — The two radial stationary branches have exactly equal leading weight

Claim ID: `L-16224`  
Status: **PROVED LEADING STATIONARY-PHASE GEOMETRY**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: `L-16222`; standard one-dimensional stationary phase

## 1. Purpose

The normalized radial Bessel template has a fold at scaled Mellin frequency
`omega=2`. Above the fold there are two stationary points. This lemma computes
their weights exactly and shows that neither branch is lower order.

The result explains both:

- why the Airy fold merges into a genuine standing wave;
- why endpoint or zero-side cancellation, rather than one-branch dominance, is
  required to control horizontal displacement.

## 2. Leading normalized radial tail

For `sigma=0`, `L-16222` gives the normalized additive leakage template

```text
rho_gamma(z)
 =sqrt(2gamma) z^(-1/2)
  J_0(gamma sqrt(z^2-1))+O_L2(gamma^-1),                 (L-16224.1)
```

on `z>1`. Put

```text
phi(z)=sqrt(z^2-1).                                       (L-16224.2)
```

The first-alias multiplicative tail Mellin integral contains

```text
rho_gamma(z) z^(-1/2+i gamma omega) dz.                  (L-16224.3)
```

Using

```text
J_0(y)
 =(2/(pi y))^(1/2)
  cos(y-pi/4)+O(y^(-3/2))                                (L-16224.4)
```

away from the fold endpoint, each exponential branch has amplitude

```text
a(z)=1/[sqrt(pi) z sqrt(phi(z))]                         (L-16224.5)
```

and phase

```text
Psi_omega(z)=phi(z)-omega log z.                         (L-16224.6)
```

The opposite exponential gives the reflected frequency.

## 3. Stationary-frequency map

The stationary equation is

```text
Psi_omega'(z)=0
 <=>
boxed:
omega=z^2/sqrt(z^2-1).                                  (L-16224.7)
```

The right side decreases from infinity to `2` on `(1,sqrt(2))` and increases
from `2` to infinity on `(sqrt(2),infinity)`.

Thus:

```text
omega<2: no real stationary point;
omega=2: one nondegenerate fold at z=sqrt(2);
omega>2: two stationary points z_-<sqrt(2)<z_+.          (L-16224.8)
```

Writing `y=z^2`, the stationary equation is

```text
y^2-omega^2 y+omega^2=0.                                (L-16224.9)
```

The two roots satisfy

```text
y_+=y_-/(y_--1).                                         (L-16224.10)
```

## 4. Exact stationary weights

At a stationary point,

```text
Psi_omega''(z)
 =(z^2-2)/(z^2-1)^(3/2).                                 (L-16224.11)
```

Therefore the squared stationary-phase weight, apart from the common universal
factor, is

```text
w(z)
 =a(z)^2/|Psi_omega''(z)|
 =(z^2-1)/[pi z^2 |z^2-2|].                              (L-16224.12)
```

Using (L-16224.10), direct substitution gives

```text
boxed:
w(z_-)=w(z_+).                                           (L-16224.13)
```

Thus the incoming and outgoing branches have exactly equal leading magnitude.
No uniform estimate can discard one of them as a lower-order tail.

## 5. Mode-dependent phases

For the fixed/prolylogarithmic mode window, Dunster's phase expansion is

```text
gamma xi_n(z)
 =gamma phi(z)
  -(2n+1)/2 theta(z)
  +O((n+1)^2/gamma),                                     (L-16224.14)

 theta(z)=arccos(1/z).                                   (L-16224.15)
```

At the paired stationary points, (L-16224.10) gives

```text
boxed:
theta(z_+)=pi/2-theta(z_-).                              (L-16224.16)
```

For the positive Fourier modes `n=4j`, the relative mode phases on the two
branches are therefore conjugate up to one common harmless phase:

```text
exp(-4ij theta(z_-)),
exp(+4ij theta(z_-)).                                    (L-16224.17)
```

The growing radial packet is consequently a finite standing-wave Fourier
packet. This is exactly the architecture treated by the Selberg-moment theorem
`L-16223` on the critical line.

## 6. Fold matching

As `omega` decreases to `2`, the two equal-weight stationary points coalesce at
`z=sqrt(2)`. Standard Chester--Friedman--Ursell reduction converts their sum into
one Airy profile. The equal-weight identity fixes the symmetric Airy matching
and rules out an asymmetric one-branch limit.

## 7. Consequences

1. The radial two-branch interference is structural, not an artifact of a loose
   Bessel bound.
2. `R-16203` cannot be repaired by proving that the far stationary point is
   smaller.
3. Selberg moments control the critical-line standing wave through
   `L-16223`.
4. The off-line horizontal weights change the cross term at order one, as shown
   in `R-16204`; an additional arithmetic or prime-side theorem is indispensable.

## 8. Proof boundary

The leading stationary geometry and equal-weight identity are exact. A
production profile requires directed Dunster/Bessel remainders and a uniform
Airy transition, supplied as finite obligations by `L-16222` and `L-16221`.
No RH conclusion is claimed.
