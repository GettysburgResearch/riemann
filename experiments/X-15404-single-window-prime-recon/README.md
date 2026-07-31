# X-15404 — Universal one-window terminal-prime reconnaissance

Status: empirical, non-directed  
Agent: `gpt56-05-l`  
Issue: #154  
Claims: `O-15401`; theorem targets `L-15405`, `T-15403`

## Purpose

Test the explicit single-window RH criterion on a complete finite prime-power
manifest and compare the pole-subtracted prime statistic with the corresponding
critical-zero expansion.

The window is the convolution square of the shifted dyadic infinite-convolution
density. Its transform is

```text
exp(-2z) product_(j>=1)
[(1-exp(-2^-j z))/(2^-j z)]^2.
```

## Retained run

```bash
python recon.py \
  --cutoff 10000000 \
  --fft-size 131072 \
  --grid-points 10000 \
  --zero-count 50 \
  --output results/recon-1e7.json
```

The finite manifest contains

```text
664,579 ordinary primes
665,134 total prime powers.
```

The dense scan over `6 <= x=2a <= log(10^7)+2` found

```text
maximum +0.006113779573986733
minimum -0.006020674487444921.
```

At retained checkpoints, the prime statistic minus the first-fifty-zero and
trivial-zero prediction stayed between approximately `4e-11` and `3e-8`.

## Numerical architecture

- NumPy Boolean sieve for exact finite prime-power enumeration;
- FFT inversion of the exact infinite-product transform at binary64 precision;
- linear interpolation of the smooth window;
- binary64 prime accumulation;
- mpmath evaluation of the first fifty critical zeros;
- direct finite zero-sum prediction.

## What the run shows

The order-`exp(a)` pole and polar terms cancel in practice, leaving a small
oscillatory signal whose envelope is dominated by the first few zeta zeros.
This supports the normalization and candidate scale of `T-15403`.

## What it does not show

- no interval arithmetic;
- no independent prime or zero backend;
- no certified infinite-product tail;
- no rigorous RH-valid bound `B_*`;
- no positive or negative RH conclusion.

The next production version should use exact spline/tail intervals, a complete
prime-power manifest, certified zero-count shell bounds, and dual-precision
outward accumulation.
