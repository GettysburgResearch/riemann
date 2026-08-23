# T104580 handoff — stationary horizontal minimum and critical-value routes

## Read order

1. `claims/lemmas/L-104537-bilateral-partition-variance-and-horizontal-modulus.md`
2. `claims/refutations/R-104519-real-axis-logconvexity-does-not-continue-to-stationary-imaginary-points.md`
3. `claims/lemmas/L-104539-positive-fourier-weighted-horizontal-modulus.md`
4. `claims/lemmas/L-104538-stationary-horizontal-minimum-proportion-transfer.md`
5. `claims/lemmas/L-104540-critical-value-total-variation-conservation.md`
6. `claims/lemmas/L-104541-critical-value-amplitude-regularity-transfer.md`
7. `claims/theorems/T-104580-stationary-horizontal-minimum-frontier.md`
8. replay and report

## Exact new results

```text
bilateral partition determinant                    PROVED EXACT
horizontal curvature = fixed-order Laguerre        PROVED EXACT
positive-Fourier weighted finite-shift defect       PROVED EXACT
real-axis continuation shortcut                    REFUTED EXACTLY
critical-only q -> alpha_2 conversion               PROVED EXACT
critical-value amplitude weighted majority         PROVED UNCONDITIONALLY
amplitude bias/variance -> count bias               PROVED EXACT
```

## Open gates

```text
SHMIN104580
  horizontally minimizing density q>1/2 at the real Xi''' zeros;

CSAMP104580
  critical sampling of the positive bulk finite-shift defect with loss <1/2;

AMPREG104580
  liminf(rho_T-v_T)>0 for |Xi''(c)| at real Xi''' zeros.
```

## Immediate attacks

### Horizontal-shift route

Use the finite quotient

```text
log |Xi''(c-ih)/Xi''(c)|^2
```

before sending `h` to zero.  Adapt Conrey's fixed-order mollifier to the
critical-point measure.  The order of limits in `L-104538` is binding.

### Sampling route

Construct a source-locked Carleson or Beurling--Selberg sampling inequality for
the real Xi''' zero set.  It must transfer the complete positive-Fourier
finite-shift identity, not merely the infinitesimal profile or an orbitwise
approximation.

### Critical-value route

Estimate the first two moments of `|Xi''(c)|` in the same short-window
normalization as Conrey's theorem.  The numerator `rho_T` already has the exact
total-variation representation of `L-104540`; only amplitude dispersion must
be controlled strongly enough that `rho_T-v_T` stays positive.

## Firewalls

- Do not use the independent `alpha_2>0.9584` theorem in a claimed descent from
  `alpha_3`.
- Do not interchange the `T -> infinity` and `h -> 0` limits without uniform
  Taylor control.
- Real-axis Laplace log-convexity does not imply imaginary critical-point
  convexity.
- Bulk positive-definite averages do not automatically sample translated
  critical windows.
- Weighted critical-value majority is not an unweighted density theorem.

## Boundary

```text
SHMIN104580       OPEN
CSAMP104580       OPEN
AMPREG104580      OPEN
alpha_2 from alpha_3 not yet proved
RH                UNPROVED
```
