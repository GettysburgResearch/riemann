# Peano–Hermite continuation: actual large-prime rows and covariance spectrum

## Executive result

The live independent base is PR #546 at `f920202e...`; no later direct
successor exists. This pass attacks both open producers without importing the
factor-67/parity line.

The retained PR #546 scan is shown not to test `LPTRP_23`: it scans ordinary
Möbius rows, while the theorem consumes rows with the Euler factors at two and
three removed. The new checker evaluates the actual filtered coefficients and
certifies their prefix derivatives through `10^8` using exact integer
square-root brackets. The activation identity then proves both rows positive
for every real endpoint below `100000001`.

Every fixed finite large-prime sieve is also proved eventually positive. Thus
any obstruction must lie in the genuinely diagonal regime with unbounded sieve
depth.

On the carrier side, the cubic multiplier cancels completely from the exact
phase-locked covariance. The covariance is invariant under invertible safe-line
preconditioning and has a positive atomic autocorrelation spectrum with mean
energy `O_m(q)`. This proves a corrected carrier-average theorem but also shows
that additional Peano/kernel redesign cannot by itself solve the pointwise
sign.

## Scientific boundary

```text
actual filtered rows through 10^8, all real X     proved
fixed finite sieve eventual positivity             proved
growing-prime diagonal tail                        open / RH-bearing
phase-locked positive autocorrelation               proved
pointwise SCID_PL                                   open / RH-bearing
Riemann Hypothesis                                 unproved
```
