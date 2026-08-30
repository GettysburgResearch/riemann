# Stationary q-adic coarea and the high-primitive beta frontier

## Summary

The T-107100 moving-grid annular detector can be replaced, at quantitative
zero-abscissa scope, by a stationary shifted-band square function. Averaging
one multiplicative partition parameter gives the fixed compact kernel

\[
\Lambda_{67}(v)=\left(1-{|v|\over\log67}\right)_+.
\]

The resulting maximal square has exact power exponent `2 Theta-1`, for both
the 67-free Möbius source and the literal beta source.

The fixed kernel permits a clean common-core decomposition. An absolute
argument removes every pair with a primitive factor at most
`(log Y)^A`; this simultaneously removes the full diagonal and every common
core larger than `Y/(log Y)^A`. The sole surviving arithmetic object is one
signed scalar with

```text
two large coprime primitive factors;
ratio between 1/67 and 67;
pairwise coprimality with the common core;
no separately squared core channels.
```

The route is now

```text
stationary triangular detector
  -> high-primitive assembled interference H_A
  -> RH.
```

The first arrow is exact and the discarded ranges are polylogarithmic. The
estimate for `H_A` remains open and RH-equivalent.

## New files

- `L-107110` stationary coarea and triangular kernel;
- `L-107111` exact zero-abscissa exponent;
- `L-107112` shallow/terminal range closure;
- `T-107110` revised conclusion-facing frontier;
- `X-107110` exact finite replay;
- `M-107110` hostile review contract.

## Replay

```text
PASS_T107110_STATIONARY_QADIC_COAREA
checks=4026
f5e71155375fc5bbb78993e1e5f3b4995c666accd9935c3401df0bc4d55324d9
```

## Boundary

```text
stationary coarea identity          proved exact
zero-abscissa exponent              proved
shallow primitive rays              proved polylog
terminal common cores               proved polylog
high-primitive interference         open / RH-equivalent
RH                                  unproved
```