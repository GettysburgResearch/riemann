# O-15401 — The universal one-window prime statistic resolves into the first critical zeros

Claim ID: `O-15401`  
Title: Prime-power reconnaissance through `10^7` matches the explicit zero sum at `10^-8` scale  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15405`, `T-15403`, `X-15404`  
Scope: numerical validation and scheduling only  
Related counterexample candidates: none

## Experiment

The script `X-15404-single-window-prime-recon/recon.py` constructs the universal
convolution-square window by Fourier inversion, enumerates every prime power
through

\[
 10^7,
\]

and evaluates

\[
 D_*(a)=
 \sum {\Lambda(n)\over\sqrt n}F_*(2a-\log n)-c_*e^a.
\]

The manifest contains

```text
ordinary primes       664,579
all prime powers      665,134
FFT samples           131,072
scan points            10,000
first zeros compared       50.
```

All arithmetic is ordinary NumPy/mpmath double or high-precision discovery
arithmetic. It is not directed.

## Observed range

Over

\[
 6\le x=2a\le\log(10^7)+2,
\]

the dense scan found

```text
maximum  +0.006113779573986733 at x=10.332652460463645
minimum  -0.006020674487444921 at x=17.664833547402125.
```

Thus subtracting two terms individually of size about `exp(a)` leaves an
order-`10^-3` to order-`10^-2` oscillatory signal.

## Explicit-formula agreement

The comparison used

\[
 -2\sum_{0<\gamma\le\gamma_{50}}
 |M(i\gamma)|^2\cos(\gamma(x-3))
\]

plus the first twenty trivial-zero terms. Representative discrepancies were

```text
x=6.0                 3.92e-11
x=10.0                1.40e-9
x=10.33265246046      -5.44e-10
x=14.0                 5.75e-9
x=16.0                 1.69e-8
x=17.66483354740        2.81e-8.
```

The residual growth is consistent with ordinary interpolation and summation
error at the largest prime manifest, not with an extra large spectral term.

## Spectral interpretation

On the critical line the transform has the exact phase form

\[
 \widehat F_{*,L}(i\gamma)
 =e^{-3i\gamma}|M(i\gamma)|^2.
\]

The coefficients are nonnegative and decay rapidly. Numerically,

```text
|M(i gamma_1)|^2  approximately 2.52824e-3
|M(i gamma_2)|^2  approximately 4.14337e-4.
```

The first zero pair can therefore contribute about `5.06e-3`, explaining most
of the observed envelope. The statistic is not suffering uncontrolled pole
cancellation after the exact subtraction; it is directly displaying the low
zeta-zero spectrum.

## Why this matters

1. `L-15404`'s pole cancellation is numerically visible over six orders of
   magnitude in the prime cutoff.
2. The one-window criterion has a practical scale: its RH-valid zero-sum moat is
   plausibly around `10^-2`, not an astronomically large cancellation radius.
3. Certified notches from `L-15406` can suppress the first few dominant on-line
   terms and shrink that moat further.
4. The same statistic is exponentially sensitive to any shifted pole in the
   open right half-plane.

## Proof boundary

- The prime sieve is exact as integer discovery code, but the weights, window,
  FFT inversion, accumulation, and zero evaluation are not directed.
- The first fifty zeros are mpmath values, not independently certified balls.
- Agreement with an explicit-formula prediction is a regression, not a proof of
  `T-15403`.
- No counterexample or positive proof is claimed.
