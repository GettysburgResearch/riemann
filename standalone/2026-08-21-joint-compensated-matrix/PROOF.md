# Joint compensation and two-orientation gluing for the quadratic-wavelet RH frontier

## Status

This is a fail-closed implication packet. It proves exact algebraic and analytic interfaces and isolates two open arithmetic estimates. It does not prove the Riemann Hypothesis.

## 1. Base detector

PR #697 supplies a fixed compact reciprocal-zeta detector with an exact decomposition

```text
G_beta=C+Q+A.
```

The calibration `C` has fixed compact support. The coordinates `Q` and `A` arise from the quadratic-error and activation/largest-prime parts of one distributional bridge.

## 2. Why componentwise one-sided bounds are unsafe

PR #694 proves an exact carrier audit for a natural short/long split: the two pieces have opposite leading `sqrt(X)/log X` carriers. Their physical sum cancels, but negative parts or absolute energies taken before summation need not. Thus the bridge must retain a shared signed compensation.

## 3. Matched transfer

For every real `f,g,tau`,

```text
(f+g)_- <= (f+tau)_-+(g-tau)_-,
```

and the infimum over `tau` is exactly `(f+g)_-`. Applying this pointwise with `f=Q` and `g=A` proves

```text
QMT101500 AND AMT101500 -> negative-mass bound for G_beta -> RH.
```

The transfer may depend on the horizon and on `X`; it cancels before the fixed detector is passed to Mellin-Landau.

## 4. Adaptive finite completion

For `C_Z=I+R_Z`, positivity of `C_ZF` gives

```text
F_- <= (R_ZF)_+.
```

This is safe even for `Z=Z(X)` because it bounds the fixed detector `F`. The remaining task is to estimate the positive correction residual.

## 5. Opposite owner forms

For

```text
E=product_i(I-r_iU_i),
C=product_i(I+r_iU_i),
```

one has two exact telescopes for `(C-I)E`:

```text
native past + one owner + squared future,
```

or

```text
squared past + one owner + native future.
```

These orientations are complementary. A region where the least-owner estimate is efficient need not be a region where the greatest-owner estimate is efficient.

## 6. Full-tail firewall

The complete correction multiplier is

```text
(C_Z(z)-1)(1-67^(-z))/zeta(z).
```

Every finite `C_Z` preserves the zero at `z=1`. A square-root carrier produced by first deleting the unsquared native tail is therefore not a valid full-source obstruction.

## 7. Regional AND-gate

Let `L` and `R_opp` be nonnegative majorants furnished by the two triangular forms. For any measurable `Omega_Y`,

```text
int_1^Y F_- dX/X
 <= int_(Omega_Y) L dX/X
  + int_([1,Y]\Omega_Y) R_opp dX/X.
```

Thus

```text
LCOR101510 AND RCOR101510 -> RH.
```

Both terminal estimates are open. The exact contribution of this packet is the source-faithful composition and the removal of the false componentwise and truncated-tail shortcuts.
