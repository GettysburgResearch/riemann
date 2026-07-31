# O-15605 — Audit of the cofinal trace-tail and visible-block frontier

Claim ID: `O-15605`  
Status: `RESEARCH AUDIT`  
Authoring agent: `gpt56-pro-09-e`  
Created: 2026-07-31  
Related counterexample candidates: none

## Repository synthesis

The newest positive-path branches now separate the localized Weil problem into
four logically distinct pieces.

1. **Exact cofinal lower-envelope implication.** PR #152 proves that rigorous
   localized lower floors with negative part tending to zero imply RH.
2. **Complete complement reduction.** PRs #155/#163/#168 turn the exact symbol
   deficit into a finite weighted packet plus a certified complement floor.
3. **Exact finite block algebra.** PR #169 closes the radical/visible/ambient
   three-block Schur factorization.
4. **Arithmetic visible block.** PR #159 proves that only the certified-zero
   near-kernel can be radicalized; PR #168 supplies exact Xi-cardinal positive
   coordinates; PR #165 isolates the phase-sensitive terminal prime window.

## New conclusion

The same-end boundary packet is no longer a blocker. `L-15612` proves a
packet-dimension-uniform local-Weyl floor

\[
 (\log R-O(1))G
\]

under one graph bound. Sharp pre-plunge and plunge-region estimates are useful
for certifying that graph condition and packet rank. Recent one-dimensional
localization results give logarithmic or near-logarithmic plunge counts rather
than bulk-size remainders; see Kulikov, arXiv:2603.07407, and Azimifard,
arXiv:2607.23016.

The opposite-boundary coupling is qualitatively different. `L-15610` shows that
it is exactly the centered terminal-prime Hankel matrix `E_a` after the zeta-pole
and polar channels cancel. `L-15611` shows that a uniform bound for a packet
containing the explicit zero-free terminal window already implies RH.

Therefore the requested cofinal weighted trace-tail theorem has not been reduced
to generic localization theory. Its last scalar/matrix estimate is an
RH-sensitive prime-error theorem.

## Why three plausible shortcuts fail

### Dimension-only saturation

A packet can have the correct dimension and miss the entire weighted-deficit
direction. Repository `R-15601` gives an exact two-dimensional counterexample.

### Fixed certified-zero frame

If an off-line zero exists, two-boundary packets amplify its quartet
exponentially while every fixed real-zero frame remains bounded. Repository
`R-16901` proves the exact obstruction.

### Phase-blind PNT error

The prime number theorem proves only

\[
 e^{-a}E_a\to0
\]

for a fixed profile. This permits an unscaled error vastly larger than the
`log R` local moat. Taking absolute prime errors before pole cancellation loses
the load-bearing phase information.

## Strongest surviving target

The exact visible margin is

\[
 \boxed{
 \beta_a
 =\sigma_a^2-\theta_a-\omega_a-\omega_a^2/h_a,}
\]

where

```text
sigma_a^2   same-end local-Weyl / certified-zero positive floor,
theta_a     centered terminal-prime Hankel operator norm,
omega_a     complete source-bound visible residual radius,
h_a         ambient complement coercivity.
```

The finite three-block theorem is complete once `beta_a>0`.

The cofinal mathematical statement still needed is

\[
 \theta_a+\omega_a+\omega_a^2/h_a
 <\log R_a-O(1)
\]

along a proof-grade unbounded support sequence, together with vanishing radical
row and assembly losses.

## Candidate computations

The following are worth parallel execution and are **not** theorem claims.

1. Build the `m=2` phase-complete endpoint packet from the universal zero-free
   window and one independent profile; compute the complete centered `E_a`.
2. Apply one, two, and five certified critical-line notch factors from PR #165;
   retain the exact matrix norm rather than a scalar FFT value.
3. Compare the directed `theta_a` with the local-Weyl moat from `L-15612`.
4. Replay the same packet through the terminal-prime and zero-side formulas as
   independent backends.
5. Use PR #168 Xi-cardinal directions as a finite positive control, but do not
   infer a growing cardinal tail bound from fixed-rank convergence.

## Literature boundary

Suzuki's arXiv:2606.09096 provides unconditional finite-interval operators and a
conjectural limiting spectral realization, not the missing cofinal lower floor.
The newest localization results, including arXiv:2603.07407 and
arXiv:2607.23016, sharply control pre-plunge eigenvalues and plunge counts, but
they do not bound the centered terminal-prime arithmetic matrix.

## Status

- Exact endpoint matrix reduction: proposed and proof-producing.
- Dimension-uniform same-end floor: proposed.
- Exact finite checker: locally tested on synthetic rational data.
- Production Suzuki terminal matrix: not yet generated.
- Cofinal terminal norm theorem: not proved.
- **RH is not claimed proved.**