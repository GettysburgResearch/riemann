# Moving-carrier reciprocal source and actual-Turán phase bridge

The T105600 packet left two source-facing physical routes:

```text
pointwise differential microscope / phase variance;
height-shell H^(1/2) winding energy.
```

A review of the latest one-sided-Hardy work and PR #731's actual-Xi
exterior-square Hankel source shows that two apparent transfer layers are
artifacts of coordinates.

## Exact denominator resolution

For `q=(L-A)^-1`, use

```text
q = integral_0^infinity exp(-uL) exp(uA) du.
```

The Dirichlet-convolution exponential `exp_*(u a)` has nonnegative
coefficients. Differentiation gives exactly

```text
q-hq'
 = integral exp(-uL)
   sum_n c_u(n)(1+h log n+h u L')n^-s du.
```

The complete moving carrier phase is common at fixed `u`, so the phase-uniform
one-sided Hardy gap applies without freezing. After integration, the only
adverse carrier term is the scalar

```text
h |L'|/(Re L-A(sigma))^2.
```

On every far right safe line, the prime-two reserve is of order `(Re L)^-2`,
whereas the drift is `O(|t|^-1(Re L)^-2)`. The actual moving carrier therefore
has a strict one-sided reserve unconditionally.

## Exact numerator resolution

For `m=F/F'`, put

```text
T_F=F'^2-FF'',
J_F=Im(F conjugate(F')).
```

Then

```text
h m'/Im m
 = h T_F/J_F * conjugate(F')/F'.
```

For Xi, `T_Xi` has the positive exterior-square Fourier density

```text
(1/4pi) integral (2u-xi)^2 Phi(u)Phi(xi-u) du.
```

This is the same actual theta-Hankel numerator used on PR #731. The pointwise
phase-variance route and the averaged robust-frame route therefore differ in
norm, not in source.

## Revised gate

The remaining theorem is `MCTPHYS105610`: retain the exact moving-carrier
reserve and actual Turán source through pole/seam transport, horizontal
endpoints, taper, truncation, denominator whitening and physical two-trace
identification.

The following former items are removed:

```text
carrier freezing;
carrier-phase freezing;
reciprocal reconstruction after freezing;
operator-valued archimedean drift;
frozen-numerator transfer.
```

A positive source alone still does not sign the physical scalar. The explicit
countermodel `1+(1/2)cos z` has a positive exterior-square source but a positive
microscope at `pi+i log 2`; the denominator all-pass orientation remains load
bearing.

RH is unproved.
