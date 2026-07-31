# O-15402 — Low critical-zero notches collapse the universal prime-window background

Claim ID: `O-15402`  
Title: One, two, and five midpoint notches reduce the pole-free prime signal by five to seven orders of magnitude  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15406`, `M-15403`, `X-15404`  
Scope: scheduling evidence for a directed notched-window certificate  
Related counterexample candidates: none

## Run

The complete finite prime-power manifest through `10^7` was replayed with the
pole-free universal window and with box factors designed at the first one, two,
and five mpmath critical-zero midpoints.

Every profile retained the dyadic infinite-convolution tail. The notched window
was assembled by ordinary FFT inversion. The scan used

```text
262,144 FFT samples
3,000 support samples per rung
664,579 ordinary primes
665,134 total prime powers.
```

Only values with `x>=14` are summarized, so the trivial-zero transient is
negligible.

## Results

| notches | support cost | minimum | maximum | empirical RMS |
|---:|---:|---:|---:|---:|
| 0 | `0` | `-1.00832e-2` | `+9.53306e-3` | `5.45277e-3` |
| 1 | `0.444521` | `-1.09468e-4` | `+1.07503e-4` | `7.38165e-5` |
| 2 | `0.743407` | `-2.23055e-7` | `+2.22687e-7` | `1.16327e-7` |
| 5 | `1.391915` | `-3.11585e-9` | `+4.18403e-9` | `1.59040e-9` |

The first notch suppresses the dominant first-zero oscillation. The second
removes the next large mode. By five midpoint notches, the remaining theoretical
first-fifty-zero signal is below the numerical accuracy of the FFT/prime
accumulation, and the observed `10^-9` scale is best interpreted as a numerical
floor.

## Support economy

The notch cost is

\[
 2\pi\sum_{j\le m}{1\over\gamma_j}.
\]

Five low-zero notches add only about `1.39` to the one-sided profile support.
Higher-height notches would cost progressively less.

## Meaning

1. The zero-notch attenuation in `L-15406` is visible in the prime data itself.
2. A directed low-zero notch packet could reduce the RH-valid pointwise moat
   from about `10^-2` to far below `10^-6` with modest support growth.
3. The same notch remains nonzero at every strict horizontal displacement, so
   this background suppression does not trade away counterexample sensitivity.
4. Numerical precision, not residual critical-line background, becomes the
   limiting factor after a few notches.

## Proof boundary

- Design ordinates are ordinary mpmath midpoint zeros, not directed balls.
- The transform zeros are therefore approximate in this run.
- Window inversion, prime weights, and accumulation are binary64.
- The apparent five-notch floor is not a mathematical residual estimate.
- No RH-valid moat or counterexample is certified.
