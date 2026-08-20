# Critical descent continuation after failed analysis

This continuation resumes the T99970/T100000 critical route and records only arguments that survived hostile checks.

## New exact results

1. `L-100160`: exact critical quadratic prefix/future-tail decomposition and activation cancellation.
2. `L-100161`: every fully active critical Euler cube is explicitly positive; the prime-harmonic wall is purely a partial-activation phenomenon.
3. `L-100162`: logarithmic integration of the partial-activation correction reduces exactly to endpoint Euler weights at exponents `1`, `1/2`, and `3/2`; the half-order endpoint residue is the unique critical term.
4. `L-100163`: that residue is exactly `M_(1/2)(X)-67^(-1/2)M_(1/2)(X/67)`.

## Binding firewalls

- `R-100160`: the signed upper-ideal activation correction is not pointwise positive; collar uniqueness is insufficient.
- `R-100161`: finite Euler-squaring positivity has an alternating inverse and cannot be positively desmoothed.
- `R-100162`: the duplicate-67 square does not furnish a finite positive reconstruction of the first Harnack difference.

## Parallel branch splice

PR #679 compresses the quadratic-envelope route to `PATG100200`. Its exact cell calculus shows that an interior minimum can occur only if `S_1<0` and `S_(1/2)<0`, at

`y_*=(3 S_(1/2)/(4 S_1))^2`.

Systematic finite-cube tests on the actual rough-prime labels beginning at 67 found no double-negative cells at all through nine labels. This is diagnostic only, but it suggests a sharper theorem: prove that actual rough-prime activation ideals cannot have `S_1<0` and `S_(1/2)<0` simultaneously. If established, the entire interior-Turan half of `PATG100200` disappears, leaving only positive-parity activation endpoints.

RH remains unproved.
