# Xi log-concavity, exterior-square current hierarchy and safe causal phase

This pass attacked both live T105610 gates.  It did not prove RH.  It proved
the complete source and safe-region phase statements, refuted the raw shell
energy as a natural invariant, and isolated the remaining descent/pointwise
interfaces.

## 1. Actual current and Turán numerator

For the positive even Xi Fourier source, the denominator current satisfies

```text
j_H=sum_(k>=0) H^(2k+1)/(2k+1)! Lambda_(2k+2),
Lambda_(2m)>=0,
Lambda_2=Fourier[Xi'^2-Xi Xi''].
```

Thus the actual Turán source is the first member of the complete actual current
hierarchy.  Both causal orientations are dominated coefficientwise, and every
diagonal weighted source energy—including the half derivative—contracts.

The two-trace source matrix

```text
[ exp(H xi)j_H   H Lambda_2 ]
[ H Lambda_2     exp(-H xi)j_H ]
```

is positive semidefinite at every frequency, with the higher chaoses paying
the orthogonal mode.

## 2. Standard Xi-kernel log-concavity

A direct theta-summand proof gives `(log Phi)''<0`.  With

```text
y_n=pi n^2 exp(2u),
a_n=9/2-2y_n+6/(2y_n-3),
b_n=-4y_n-24y_n/(2y_n-3)^2,
```

the exact mixture formula is

```text
(log Phi)''=E b_n+Var(a_n).
```

The variance is paid by the first-summand curvature; the complete theta tail
has a deliberately loose rational certificate ending in

```text
(9/2)(22/7)(19/1000)=1881/7000<1.
```

No external log-concavity claim and no false implication from log-concavity to
RH is consumed.

## 3. Monotone current profile

For an even log-concave source, condition the exterior-square law on its sum
frequency.  The quantile-flow velocity obeys `|v|<=1/2`, so both ordered
endpoints move right as the sum grows.  The exponential divided difference is
coordinatewise increasing.  Hence

```text
R_H(xi)=H exp(-H xi)Lambda_2(xi)/j_H(xi)
```

is nonincreasing.

At base `b` and microscope scale `h`, total height is `H=b+h` and the actual
profile is `(h/H)R_H`.  Earlier wording which conflated the two heights was
corrected before publication.

## 4. Inner causal phase at safe height

For `H>=beta_(r+1)`, the shifted derivative all-pass

```text
U_(r,H)=Xi^(r+1)(x-iH)/Xi^(r+1)(x+iH)
```

is inner.  The shifted Cartwright product supplies the zero factors; positive
Xi Laplace moments orient the exponential factor.  Under Paley--Wiener, inner
multiplication is causal.

Every decreasing source profile therefore contracts.  At the base Xi rung,
for every `b>=beta_0` and `h>0`,

```text
V_H^* M_(r_(b,h)) V_H <= M_(r_(b,h)).
```

This is an unconditional actual-source result in the complete safe region.  It
does not descend below the unknown `beta_0`.

## 5. Model bank and finite compression

The Hankel operator `H_(bar U)` is a partial isometry with initial space

```text
K_U=H^2 minus U H^2.
```

For finite Blaschke `U`, its dimension is the all-pass degree.  Every finite
source-owned compression inherits the weighted contraction exactly after the
current Gram is installed.

Trace formulas were kept at their proper scope: continuum multiplication
weights are not trace class.  Finite model-space charges are explicit, but the
cofinal trace limit retains its endpoint carrier.

## 6. Shell and pointwise firewalls

The family `p_N=z^N` has empty positive-height shells at every derivative rung,
but for `h_2=2h_1` each adjacent shell quotient has

```text
E_+=E_-=1/9.
```

Nineteen rungs pay raw negative energy `19/9>2` with zero signed winding.  Thus
raw `HSHE105602<2` is overstrong; a balanced signed/positive-energy ledger is
required.

Likewise a decreasing source profile and a perfectly inner unilateral shift
can satisfy the full weighted contraction while an off-diagonal physical
trigonometric evaluation has the wrong sign.  The source energy does not
silently imply the pointwise microscope.

## 7. Honest remaining gates

```text
POINTID105630
  identify the actual two-trace point evaluation as a positive/source-owned
  consumer of the current hierarchy;

SAFEDESC105628
  continue the safe source/phase geometry below beta_0 without a denominator
  pole or positive zero-height charge;

ENDIDX105630
  retain the finite argument-principle endpoint/common-zero ledger for the
  integrated and proportion routes.
```

The first two are RH-bearing.  None is proved here.
