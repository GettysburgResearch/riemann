# Phase-locked high-order Hermite notch after the Bohr no-go

## Result

The uniform-center fractional heat route is false, but a hypothetical off-line zero determines a fixed center and a fixed horizontal displacement. The single most effective scalar operation is a high-order Hermite notch centered at the safe-line saddle and normalized to one at the hypothetical zero.

For `rho=1/2+delta+i gamma`, put `q=1/2-delta` and

```text
M ~ 2 q^2 T.
```

The notch multiplier on coefficients is

```text
((1-log n/T)/(2q))^M.
```

It kills the classical `log n=T` saddle and preserves the pole at `rho` exactly. The optimal absolute envelope has two saddles at

```text
log n/T = 2delta,
log n/T = 2-2delta,
```

and rate

```text
delta-delta^2.
```

A one-sided cutoff removes the second saddle. The hypothetical zero retains rate `delta^2`. Hence the exact arithmetic phase saving still required is

```text
delta(1-2delta).
```

This proves a sharp method barrier: no coefficientwise magnitude, phase-blind Gram, positive trace, or subexponential refinement can close the route.

## New source mechanism

The fractional inverse pair supplies a phase-twisted logarithmic-owner martingale. This gives a prescribed source-level mechanism for the required cancellation, rather than another common-contraction existence statement. The open theorem `PLHAC99100` is a multiplicative martingale-Carleson estimate on the single annulus

```text
log n=2delta T+O(sqrt T).
```

## Scientific boundary

```text
uniform-center heat theorem               false / PR #618
optimal phase-locked notch                proved exact
optimal coefficient envelope              proved exact
magnitude-only notch closure              refuted
phase-locked annular localization          proved exact
fractional owner martingale               proved exact
PLHAC99100                                open / RH-bearing
Riemann Hypothesis                        unproved
```
