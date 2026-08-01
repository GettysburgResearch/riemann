# L-16230 — Adaptive angular cutoffs close the normalized radial and frequency-derivative tails

Claim ID: `L-16230`  
Status: **PROVED FOR COEFFICIENT-TAIL FIELDS; ENDPOINT CLAIM SUPERSEDED BY R-16205**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: exact leakage normalization `L-16217`

## Statement

Let `gamma_j -> infinity`. At each level take the exact two-constraint repaired
source packet in modes `0,4,8,12`. Let `s_(n,j)>0` be the exact positive-ray
leakage amplitudes and let `a_(n,j,k)` be the directed angular Legendre
coefficients.

For every prescribed `epsilon_j>0`, finite angular cutoffs may be chosen so that
the normalized coefficient-tail synthesis errors satisfy

```text
sum_source epsilon_rad,j <= epsilon_j/gamma_j,
```

and consequently

```text
sum_source epsilon_drad,j <= epsilon_j.
```

The horizontal-strip coefficient-tail error is `O(epsilon_j/gamma_j)`.
Choosing, for example, `epsilon_j=2^-j` proves cofinal decay of these three
source-derived fields.

## Proof

For one fixed block, the directed Legendre coefficient sequence is square
summable. Since `s_(n,j)>0`, its coefficient tail divided by the exact leakage
norm tends to zero as the finite cutoff tends to infinity. Increase the cutoff
until the displayed repaired-packet bound is met.

Differentiating the finite Fourier kernel with respect to scaled radial
frequency multiplies the omitted angular source by at most `gamma_j`, because
`|t|<=1` on the angular support. Evaluation in the horizontal strip of
half-width `1/(2gamma_j)` costs only a fixed exponential factor. QED.

## Scope correction

This theorem does **not** prove decay of a normalized Poisson endpoint remainder
from an absolute bound on `||f_j^(4)||_1`. For a unit tail profile that remainder
contains

```text
||f_j^(4)||_1 / sqrt(delta_j),
```

where `delta_j` is the first-alias energy. Since `delta_j` is
superexponentially small, fixed Sobolev convergence of the compact sources does
not close the relative endpoint gate. See `R-16205`.

The remaining production emitter must derive the endpoint channels and their
remainder from the normalized radial ODE/Bessel profile itself, then combine
that result with the complete Poisson cross-alias operator bound.
