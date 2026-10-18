# A complete low-product amplitude bound

Status: **proposed unconditional component mathematics.** The complete proof
is in [PROOF.md](PROOF.md). It leaves the high-product native amplitude and
the RH-strength coarse-energy recurrence open.

The result controls a specified part of the actual Newton amplitude. On every
output annulus `X <= k < 2X` in the strict step
`Y+1 <= k < (Y+1)^2`, subtract the harmonic kernel's exact logarithmic part
and retain its two finite balance coordinates. The complete input-product
range `d <= X^rho` can then be removed with a power-small squared amplitude
error for every fixed `1/2 < rho < 2/3`.

For example, at `rho = 5/8`, the sum of squared errors over the **entire**
Newton step is

    O(Y^(-1/8) (1+log Y)^8).

The elementary estimate taking absolute values term by term only gives
`O(D^2 log^2 D / X)` on one annulus, with a power gain when `D < X^(1/2-epsilon)`.
The proof here retains every coefficient cross term, groups equal rational
frequencies and controls their complete covariance. It extends that
power-small range to `D < X^(2/3-epsilon)`.

The Fourier estimate is valid for arbitrary complex coefficients bounded
by `d_2(d)`. Its gain is periodic cancellation of the harmonic kernel;
it is not a new bound exploiting the signs of the Möbius function. The exact
native Dirichlet-inverse identity identifies the output to which it applies.

## What remains in the amplitude

Writing `M_Y = sum_(n<=Y) mu(n)/n`, the second finite coordinate is

    B_Y = 1 + sum_(n<=Y) mu(n)log(n)/n - (log Y + gamma/2) M_Y.

The retained expression on each annulus is exactly

    2 M_Y B_Y + M_Y^2 log(Y^2/k)
       - sum_(X^rho<d<=Y^2) (g_Y*g_Y)(d) R(k/d)/d,

with the integer cutoff understood and
`R(t) = H_floor(t) - log(t) - gamma`. Products `d > k` remain in this finite
sum. Their renormalized remainder cancels part of the displayed balance,
even though their original harmonic value is zero.

The removed range is complete as a range of products. It is an asymptotically
small fraction of all ordered input pairs. At the final annulus and `rho=5/8`,
it includes every interaction with one index up to a constant times `Y^(1/4)`.
No conclusion follows for the remaining products from their count alone.

The proof transfers to the block means retained in #974 by contractivity of
orthogonal projection. It compares the **square roots** of the two energies;
the mixed energy term is paid explicitly. No new subquadratic bound on the
remaining amplitude in terms of the preceding energy is asserted.

## Review and replay

- [PROOF.md](PROOF.md): exact statements, complete analytic proof, balances,
  step coverage and projection consequence.
- [SOURCES.md](SOURCES.md): exact inherited commits and scope of nearby work.
- [check_amplitude.py](check_amplitude.py): exact finite algebra and coverage
  checker, with explicit predicates that remain active in optimized Python.
- [CHECKS.json](CHECKS.json) and [CHECKS_OPTIMIZED.json](CHECKS_OPTIMIZED.json):
  ordinary and optimized replays.
- [VALIDATION.md](VALIDATION.md): primitive construction, arithmetic contract,
  coverage, failure controls and the distinction between replay and proof.

The proof contains no imported zero-free strip, short-interval theorem or
improved large-sieve estimate. The finite Fourier and spacing arguments are
classical and are proved here for the required normalization; no general
priority claim is made for those methods.
