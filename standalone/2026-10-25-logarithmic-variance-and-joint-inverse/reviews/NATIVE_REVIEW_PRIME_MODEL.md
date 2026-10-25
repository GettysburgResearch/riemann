# Independent review: actual spectral floor from prime discrepancy

Date: 25 October 2026. Reviewer: `native_bootstrap`, independent of the author.

## Exact object and verdict

Reviewed file: `third-pass/spectral/PRIME_MODEL_SPECTRAL_FLOOR.md`.

Reviewed SHA256:
`642acd096866d14193e6554b8273819f94e11423177886270e622ef78135412b`.

**Verdict: PASS at the stated scope.** The discrepancy-integral inequality
is an unconditional finite-matrix bound for the complete source. The
explicit prime-number-theorem specialization is a valid consequence of
the stated imported theorem. The estimate does not give an improved
fixed zero-free half-plane.

The initial file hash was
`c93e5830b3d971b5df6eb60767714840daba66cf831a756690e66f32d6aed699`.
During review the author distinguished digamma notation `psi_Gamma` from
the Chebyshev function `psi`. I reread the complete final file before
binding this verdict to its final hash.

## Source authentication

I checked the complete additive Weil form against PR 1017 at
`450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, resident
`standalone/2026-10-23-weil-resolvent-publication/browse/PROOF.md`,
and opened [Connes--Consani--Moscovici, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1).

I freshly verified [Johnston--Yang, arXiv:2204.01980v2](https://arxiv.org/html/2204.01980v2),
Theorem 1.4, equation (1.7): it states the `psi` error bound with the
constants `0.026`, `1.801`, `0.1853`, and threshold `x>=23` used here.
The authors' underlying numerical verifications were not replayed.

## Independent derivation

The continuous prime model has exactly the negative kernel
`-exp(|u|/2)`. The full pole contribution has kernel `2cosh(u/2)`.
Their sum is therefore `exp(-|u|/2)`, with Fourier multiplier
`1/(t^2+1/4)` under the stated convention. This retains both pole terms;
there is no positivity assumption on the arithmetic remainder.

The digamma recurrence verifies

\[
 \Re\psi_\Gamma(1/4+it/2)+\frac1{t^2+1/4}
       =\Re\psi_\Gamma(5/4+it/2).
\]

The lower constant is consequently
`psi_Gamma(5/4)-log pi = 4-gamma-pi/2-3log2-log pi`, as displayed.
The digamma series gives its pointwise lower-bound direction.

For a zero-extended trigonometric polynomial the autocorrelation
derivative contains the boundary term
`-conjugate(f(a-u))f(a)`. Combining this with the `L2` derivative and
point-evaluation bounds yields exactly

\[
 |C_f'(u)|\le
 [\pi N+(2N+1)/2]a^{-1}\|f\|_2^2.
\]

The endpoint term cannot be dropped. The file retains it.

With `E(x)=psi(x)-x+1`, the lower endpoint in Stieltjes integration by
parts is zero. The upper endpoint is zero because `C_f(2a)=0`, even
when the endpoint happens to coincide with a prime power. The sign of
the remainder is therefore the positive integral

\[
 \int_0^{2a}E(e^u)e^{-u/2}
        [S_f'(u)-S_f(u)/2]du.
\]

The absolute-value estimate gives
`2(D_(a,N)+1/2)I(a)||f||_2^2`, with exactly the factor in Theorem 1.
The finite variational principle applies on the full space and on its
even subspace. This proves the stated finite floor, including `N=0`
and every `a>0`.

For the power bound `|psi(x)-x|<=C_beta x^beta`, `beta>1/2`, integrating
the factor `exp((beta-1/2)u)` gives `exp((2beta-1)a)`. The polynomial
Fourier dimension can be absorbed into an arbitrarily small exponential
loss. Thus a spectral consumer returns the same `beta`, not a smaller
one.

For the Johnston--Yang specialization, I checked the initial-interval
majorant, the extra bounded contribution from the `+1` in `E`, and the
split of the remaining integral at `u=a`. On its second half the
Vinogradov--Korobov exponent is increasing for all sufficiently large
`a`; a fixed reduction of its positive constant absorbs the polynomial
factor. This gives the actual-source lower bound (23), with leading
exponential rate one and the stated subexponential saving.

## Scope and remaining gap

No load-bearing correction is required at the reviewed hash. The first
unproved strengthening is exactly the last section's proposed use of
signed autocorrelation structure before the absolute value in (17).
The PNT majorant itself cannot reduce its supplied power exponent.

This review approves an explicit lower estimate, not a positivity
certificate, a variance-selector construction, or a new fixed strip.
The final claim that the baseline improves by more than every inverse
power of `a` is correct along a fixed polynomial mode schedule.

## What ran

Fresh primary-source lookup, full proof reading, independent symbolic
derivation of the pole/model cancellation and Stieltjes signs, and
SHA256 computation. No approximate matrix diagonalization, fitted
asymptotic, or finite-data extrapolation is involved in the verdict.
