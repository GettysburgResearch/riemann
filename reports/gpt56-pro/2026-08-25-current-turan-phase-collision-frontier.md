# Current–Turán exterior-square hierarchy and the physical phase-collision frontier

The live T105610 programme had reduced the Xi differential microscope to the
actual pair

```text
numerator:   T_Xi = Xi'^2-Xi Xi'';
current:     J_Xi = Im(Xi conjugate(Xi'));
phase:       conjugate(Xi')/Xi'.
```

The apparent remaining denominator-whitening problem is now resolved at the
source level.

## Exact hierarchy

For the positive even Xi Fourier kernel, define

```text
Lambda_(2m)(xi)
 = (1/2) integral (2u-xi)^(2m) Phi(u)Phi(xi-u) du.
```

Every member is nonnegative, `Lambda_2=Fourier[T_Xi]`, and exactly

```text
Fourier[J_h]
 = sum_(k>=0) h^(2k+1)/(2k+1)! Lambda_(2k+2).
```

Thus the denominator current is the complete odd exterior-square chaos
generating function and the actual Turan source is its first coefficient.
In particular

```text
Fourier[J_h] >= h Lambda_2 + h^3 Lambda_4/6.
```

On the decaying upper and reflected frequency orientations,

```text
h exp(-h|xi|) Lambda_2(xi) <= Fourier[J_h](xi).
```

This implies contraction at every diagonal weighted source energy, including
the `H^(1/2)`/Hankel weight.

## Two-trace common mother

The matrix

```text
[ exp(h xi) j_h      h Lambda_2 ]
[ h Lambda_2         exp(-h xi)j_h ]
```

is positive semidefinite at every frequency. Its determinant is
`j_h^2-h^2 Lambda_2^2`; the higher chaoses pay the orthogonal two-trace mode.
The statement remains true after an arbitrary phase which is diagonal in the
frequency coordinate.

Therefore the upper trace, lower reflected trace, numerator tail, denominator
current and all source-diagonal phases are one positive matrix source.

## The sole noncommuting object

The actual physical phase is multiplication by

```text
U_h(a)=conjugate(Xi'(a+ih))/Xi'(a+ih).
```

In the frequency source coordinate it is convolution. Let

```text
r_h(xi)=h exp(-h xi)Lambda_2(xi)/j_h(xi),  0<=r_h<=1.
```

For an abstract positive contraction `R` and unitary `V`,

```text
I-Re(VR)
 =(I-R)+R^(1/2)(I-Re V)R^(1/2)
   -Re([V,R^(1/2)]R^(1/2)).
```

The first two terms are positive. Hence every physical negative direction is
carried by one weighted phase commutator. In Fourier coordinates its exact
Hilbert--Schmidt kernel is

```text
Uhat(xi-eta) [sqrt(r(eta))-sqrt(r(xi))].
```

This is the common object behind the pointwise microscope, the robust-frame
trace route, and the topology-sensitive shell energy.

## Raw shell gate correction

For `p_N(z)=z^N`, every derivative is real-rooted and every positive-height
shell is empty. Yet for `h2=2h1`, every adjacent shell quotient has

```text
E_-=E_+=1/9.
```

Across nineteen rungs the raw negative energy is `19/9>2`, although the exact
signed degree is zero. Thus raw `HSHE105602<2` is an overstrong sufficient
condition, not a natural real-rootedness invariant. A viable integrated proof
must retain the positive Hardy compensation instead of discarding it before
summing.

## Revised gates

```text
APCX105620:
  transfer the diagonal current/Turan contraction through the physical
  Xi-prime all-pass map and finite-window interfaces;

PCC105623:
  absorb the positive part of the weighted phase commutator by the higher-
  chaos reserve plus the positive all-pass phase term;

BSHE105620:
  retain that same positive compensation in the integrated shell/winding
  ledger.
```

These gates are different norms of one physical commutator. None is proved.
RH remains unproved.
