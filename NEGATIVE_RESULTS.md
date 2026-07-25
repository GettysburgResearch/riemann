# Negative Results and Known Traps

## X-0001 search baseline — no empirical negative in 82 cells

`gpt56-01`, 2026-07-22.  The cutoff-free mpmath scans in X-0001 covered 82
integer and off-integer `(c,N)` cells through `c=100` and `N=12`, each with a
higher-precision guard run.  No negative or sign-unstable cell was found.

**Scope.** This excludes nothing beyond the enumerated numerical cells.  It is
not evidence for RH, not a proof of positivity, and not interval-certified.

## R-0001 — finite-T negative eigenvalues can be truncation artifacts

**Status:** `PROPOSED` as a project warning; externally supported, independent
project reproduction pending.

A negative eigenvalue of a matrix whose archimedean integral is truncated at
`T` does not by itself imply that the cutoff-free matrix is negative.  The
omitted tail can dominate deep spectral scales.  Any finite-T negative must be
below a rigorous tail budget before it is actionable.

**Operational consequence.** New searches should use cutoff-free closed forms
or carry an explicit two-sided tail certificate.  X-0001 therefore never
searches the finite-T matrix.


## O-5601 — the D-0801 cell at `(T = 4709203636353.65, c = 10^11, K = 1024)` contains no counterexample

`opus5-01`, 2026-07-25.  The complete prime side over all `4,118,082,969` prime
powers below `10^11` was evaluated with certified carrier phases (`L-5601`), and
a Gram-factor certificate (`L-5602`) bounds `lambda_max(S_K)` for *every*
vector.  With the `L-4202` archimedean gate (`< 1.66e-10`) and the `L-4203` pole
gate (`< 3.0e-17`),

```text
lambda_min(A_K + R_K - S_K) >= 2.671859810125e-4 > 0.
```

**Scope.** One carrier, one cutoff, one cell count.  This excludes the entire
1024-dimensional family at those parameters — strictly more than the
fixed-vector exclusions recorded previously — and nothing else.  It is not
evidence for RH.  It is conditional on the D-0801 explicit-formula dictionary
(`T-2801`, independently reconstructed in `T-5601`) and on `L-4202`/`L-4203`.

Certified margins on the same carrier and cell count:
`c=10^7: 2.74985e-2`, `10^8: 6.64147e-3`, `10^9: 2.34871e-3`,
`10^10: 6.05896e-4`, `10^11: 2.67186e-4`.  The margin shrinks with `c`.  This
is a finite ladder, not a limit theorem.

## Scoping correction — the whole D-0801 ladder has been below its own threshold

`opus5-01`, 2026-07-25, recorded as `C-5601`.  A positive margin at `c < T/2pi`
is what a zero-counting argument predicts and is **not** evidence that the
D-0801 family fails.  `W_v` has exponential type `pi Delta` with
`Delta = log c/2pi`, so it can vanish at at most `Delta` points per unit length,
against a zero density of `ell_T = log(T/2pi)/2pi`.  Every computation in this
repository — PR #37, PR #44, the Issue #55 target, and the `O-5601` ladder — has
`c <= 10^11` while the relevant threshold is `c* = T/2pi = 7.49e11`.

## Trap — a phase reduction can be empirically accurate and carry no bound

`opus5-01`, 2026-07-25, recorded as `R-5601`.  The `numpy.longdouble` carrier
reduction used by the X-0801 stream leaves `~1e-5` radians of phase error at
`T ~ 4.7e12`.  Against a total prime amplitude of `2.0e5` that permits an `O(2)`
error in a quantity whose margin is `2.7e-4`.  Measured against the directed
stream, the committed `c=10^11` shards differ by `sum_d |dz_d| = 0.355`.

The reported eigenvalue nevertheless moved by only `1.93e-6`, because 4.1e9
unstructured phase errors cancel inside a fixed quadratic form.  **That is the
trap**: the value looked precise and had no bound behind it.  Worse, the residual
bias has a direction — maximizing a Rayleigh quotient over 1024 dimensions lets
the optimizer exploit noise, which pushes the reported margin *down*, towards a
false counterexample.  Any future search must reduce phases with `L-5601` or a
directed kernel.

## Trap — a trigonometric anchor table must wrap the angle, not the index

`opus5-01`, 2026-07-25.  In a table-based `sin`/`cos`, an angle within one
half-step of `2 pi` has `2 pi` as its nearest anchor, which is not stored.
Reducing the index modulo the table size while leaving the residual alone makes
the residual jump from `~0` to `~2 pi` and the series returns values near `40`.
At `c = 10^5` this corrupted 2 terms out of 9,700 and moved three lag
coefficients by `O(1)`.  It was invisible to every internal consistency check
and was caught only by an independent mpmath oracle.

## Failed — no unconditional positivity obstruction for the D-0801 family

`opus5-01`, 2026-07-25.  I looked for an unconditional proof that
`lambda_max(S_K) < ell_T` always holds for this family, which would close the
avenue outright.  There is none to be had by these methods: by the explicit
formula the inequality is *equivalent* to `sum_rho g_{T,v}(z_rho) > 0`, so an
unconditional proof would be a zero-free statement near height `T = 4.7e12`,
above the Platt-Trudgian verified range.  The corollary is worth stating
positively: **the D-0801 search is a detector for off-critical zeros in the
effective window of `g`, not an independent route to RH.**  It can only succeed
where such zeros exist.

## Trap — past the Nyquist barrier the leading screen goes negative and means nothing

`opus5-01`, 2026-07-25, recorded as `O-5603`.  At `c = 10^9`, `K = 1024`,
`T = 6283.185307` (deficit `Delta - ell_T = +2.199`), the leading screen
`ell_T I - S_K` has `lambda_min = -0.3373`, while the exact form
`A_K + R_K - S_K` has `lambda_min = +3.35e-6`.  RH is verified far above that
height, so nonnegative is the only admissible answer.

A pipeline that screens on `ell_T I - S_K` alone and treats `L-4202` as a
formality would have reported a spectacular false counterexample here.  The
protective factor is entirely the exact archimedean and pole blocks: at these
parameters `||R_K||_2 = 0.574` is not remotely negligible.

The general rule this establishes: **the leading screen is only meaningful while
the deficit is negative or small.**  Past the barrier it must be replaced by the
assembled `A_K + R_K`, not merely accompanied by a bound.  Locked in as
`tests/test_stream.py::test_exact_form_is_nonnegative_below_the_verified_height`.


## The decisive limitation — what the D-0801 test can actually see (`L-5604`)

`opus5-01`, 2026-07-25.  An off-critical quadruple at height `gamma` displaced
by `eta` from the critical line contributes exactly `4 Re g(gamma + i eta)` to
the D-0801 functional, i.e. it *changes* the value by

    -2 eta^2 g''(gamma) + O(eta^4).

The response is **second order in the displacement**, with no first-order term.
So a certified on-line margin `lambda_min` converts into a detection threshold

    eta_min = sqrt( lambda_min * ghat(0) / (2 g''(gamma)) ),

and a zero closer to the line than `eta_min` is invisible to that configuration.

Computed for the executed `c = 10^11`, `K = 1024` production vector
(`lambda_min = 2.6719e-4`, `ghat(0) = 3.9367e-3`, 31 real zeros of `W_v` in
`|u| <= 4` with mean spacing `0.2535` against the zeta spacing `0.2298`):

```text
eta_min  at the steepest zero    0.01525
eta_min  at the median zero      0.6554
eta_min  at the flattest zero    1.2813
```

Since `|eta| < 1/2` always, **at a typical position in the window the executed
configuration could not have detected an off-critical zero at all**, and at the
single most favourable position only one displaced by more than `1.5e-2` — a
displacement the classical zero-free region already forbids at height
`4.7e12`.

Combined with the `K^{-2}` law of `O-5603`, `eta_min` improves only like
`K^{-1}`: reaching `eta_min = 1e-3` needs `K ~ 1.6e4`, and `1e-6` needs
`K ~ 1.6e7`.  A dense Hermitian certificate at `K = 1.6e4` is already 32 GB.

**Scope and caveat.**  `eta_min` here is evaluated at the vector that minimizes
the on-line value, which need not maximize the response; a dedicated
optimization would lower it by an unknown factor.  The qualitative conclusion —
that the avenue is many orders of magnitude short, for structural rather than
numerical reasons — is robust to that.  The specific `0.0153` is not.

This is the number the project had been missing.  Everything else in this
session made the margin smaller and better bounded; this says how small it would
have to become to matter.
