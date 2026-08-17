# T-93291 — Corrected Peano–Hermite/two-row producer frontier after the 93290 pass

Claim ID: `T-93291`  
Status: **UNCONDITIONAL ADVANCE AND FAIL-CLOSED CLOSURE CONTRACT**  
Created: 2026-08-18  
Frozen base: PR #546 at `f920202ea15c577bf05fa58370bdc3d8313868cd`  
RH status: **unproved**

The successor establishes:

```text
actual p>3 coefficient dictionaries                 exact
real-X activation/prefix reduction                  exact
actual LPTRP prefixes through 10^8                  proved directed
actual LPTRP rows for all real X<100000001          proved
fixed finite large-prime sieve eventual positivity  proved
naive conjugated monotone cone                       refuted at p=5
cubic-free phase-locked covariance                   exact
safe-line preconditioner gauge invariance            exact
positive covariance spectral representation          proved
phase-locked covariance mean energy O_m(q)           proved
```

## Static branch

The fixed two-row Mellin–Landau consumer of PR #546 remains valid at its
conditional scope. `T-93290` proves a large finite segment of its actual
producer, while `L-93291` proves every fixed finite sieve depth eventually.
The remaining static theorem is now localized to the diagonal regime in which
the number of active primes grows with `X`:

\[
\boxed{
 \mathrm{LPTRP}_{23}^{\infty}:
 \quad A_2(N),A_3^\sharp(N)\ge0
 \quad(N\ge10^8).
}
\tag{T-93291.1}
\]

This is equivalent to the unproved tail of the stronger prefix producer, not a
new name for a proved result.

## Carrier branch

`L-93292` removes the centered-cubic representation from the signed covariance:

\[
 \mathfrak C_{q,m}(t)
 =\frac1{2\pi}\int K_{q,m}(\xi)Z(\xi-t)d\xi.
\tag{T-93291.2}
\]

`L-93293` supplies its exact positive autocorrelation and `O_m(q)` carrier mean
energy. `R-93292` proves that these facts cannot yield the one-carrier sign by
themselves. The surviving carrier producer is still the explicit pointwise
inequality `SCID_PL`, now known to be invariant under every invertible fixed
safe-line preconditioner.

## Exact conclusion boundary

Either of the following would complete the existing consumer:

1. prove the growing-prime tail (T-93291.1);
2. prove `SCID_PL` by arithmetic information not erased by safe-line gauge
   invariance;
3. replace the pointwise carrier consumer by a legitimate conclusion mechanism
   that uses the positive spectral measure of `L-93293`.

None is proved here. No factor-67 Hall theorem, annular `1/42` repair, parity
producer, Mertens square-root estimate, or RH-strength prime error is imported.

```text
meaningful unconditional quantitative advance  yes
complete unconditional RH proof                 no
Riemann Hypothesis                              unproved
```
