# Terminal Gaussian heat-residue continuation

**Date:** 2026-08-11  
**Branch:** `research/gpt56-pro/367-terminal-heat-residue`  
**Base:** PR #367 at `2a725fb71794dfca11e76c1af2a49e6b3ea8bc9c`  
**Status:** proposed theorem package; RH remains unproved.

## Result

PR #367 reduced the corrected arithmetic kernel floor to one scalar pairing
between the completed Chebyshev discrepancy and a three-Gaussian oscillatory
kernel.  This continuation identifies that scalar with an entire Gaussian
Mellin transform of

```text
-zeta'/zeta(s) - 1/(s-1)
```

and shifts its Bromwich contour to the critical line.

The resulting exact decomposition is

```text
terminal scalar
 =
critical-line positive evaluations
- explicit smooth gamma boundary
+ right-half-plane zero residues.
```

For the parabolic kernel

```text
K_(sigma,y)(z)
 =exp(sigma^2 z^2)
  [1-cosh(2 sigma^2 y z)],
```

a target zero at displacement `y` contributes exactly `-2m`.  A nuisance zero
at displacement `d+ir` has exponential rate

```text
(d-y)(d+3y)-r^2,
```

which is precisely the terminal threat exponent proved on PR #364.  The
prime-side contour calculation and the zero-side terminal graph have therefore
become the same formula.

## Finite witness theorem

The scalar also has the explicit finite-prime form

```text
-2 A_(sigma,y) [
  sum Lambda(n)/sqrt(n) H_(sigma,y)(log n) cos(x log n)
  - integral exp(t/2) H_(sigma,y)(t) cos(x t) dt
].
```

The omitted prime tail is bounded by an elementary all-integer Gaussian
integral.  Consequently false RH, together with terminal isolation, implies a
strictly negative certificate at finite dyadic parameters and a finite
prime-power cutoff.  Conversely any such directed negative interval is a
finite negative Weil witness.

This gives a countable semidecision procedure for false RH.  No negative
Riemann-data instance was found or claimed.

## Verification

The retained checker reports

```text
PASS_TERMINAL_GAUSSIAN_HEAT_RESIDUE
```

and verifies the closed finite identities.  In the retained control:

```text
target residue contribution     -1.999999999999987
kernel identity error            1.11e-16
prime/continuum identity error   6.38e-16
```

The computation is a regression only.  It does not prove the contour theorem
or the arithmetic sign.

## Exact frontier

```text
heat/Bromwich representation             PROPOSED COMPLETE
critical-line residue decomposition      PROPOSED COMPLETE
target residue = -2m                     EXACT
threat exponent fusion                   EXACT
finite linear witness under false RH     PROPOSED COMPLETE
unconditional terminal scalar sign       OPEN / RH-EQUIVALENT
corrected-kernel floor                    OPEN / RH-EQUIVALENT
Riemann Hypothesis                        UNPROVED
```
