# X-0601 — Prime-power edge and tiny-support search

Status: **EMPIRICAL, NOT CERTIFIED**  
Agent: `gpt56-01-a`  
Issues: #8 and #1

## Research question

Does the cutoff-free finite Weil matrix develop a negative direction in a narrow
one-sided neighborhood of a prime-power threshold, or in the tiny-support
regime `c=exp(L)` close to `1`, that the X-0001 grid missed?

## Exact components

- `L-0601`: the newly admitted `q=p^a` term has derivative jump
  `-(2/(a*sqrt(q))) 11^T`.
- `L-0602`: moment constraints delay the first new-prime signal from order one
  to orders 5, 9, 13, and so on.
- `L-0603`: exact frozen rank-one susceptibility threshold.
- `L-0604`: exact Lerch resummation of four slowly convergent correction sums.

The full matrix signs produced by the scripts are ordinary mpmath observations.

## Files

- `run.py`: independent cutoff-free even-matrix assembly, exact event kernel,
  moment diagnostics, and shardable edge scanner.
- `lerch_resum.py`: tiny-`L` Lerch formulas.
- `test_run.py`, `test_lerch_resum.py`: regression and identity tests.
- `results/scan-summary.json`: compact parameters, hashes, and strongest near
  misses. Raw scan JSON is regenerated rather than committed.

## Reproduce tests

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Expected at this commit: `9 passed`.

## Reproduce a small edge scan

```bash
python run.py \
  --limit 30 \
  --bands 4 8 12 \
  --fractions 0 0.02 0.05 0.1 0.2 0.35 0.5 0.65 0.8 0.92 0.98 \
  --dps 85 \
  --output results/local-small.json
```

## Main session scans

1. `N=12`, 72 consecutive prime-power intervals from `q=2` through `q=263`,
   11 log-fractions per interval, 85 digits: 792 cells.
2. Selected deepest cells repeated at 130--220 digits.
3. Exact thresholds through `q=97`, `N=20`, 170 digits: 35 cells.
4. `97 -> 101` refined near its interior dip and checked for every
   `1 <= N <= 30`, up to 260 digits.
5. Representative odd-sector checks.
6. Lerch-resummed `L=1e-1` through `1e-12`, `N<=6`.

No empirical negative or retained precision sign flip was found.

## Strongest near miss

At `q=97`, `next=101`, `N=12`, the refined minimum was near log-fraction
`0.0962`:

```text
lambda_min ~= 5.18080693547815707234989428698e-44
```

It remained positive at 220 decimal digits. This is not a certificate.

## Numerical semantics

- Backend: mpmath 1.3.0.
- Working precision is explicitly set for matrix construction and eigensolving.
- The archimedean matrix is cutoff-free; no finite integration `T` is used.
- Direct correction sums stop against analytic tail envelopes, but their
  floating evaluation is not outward-rounded.
- Lerch output is not an interval ball.

## Counterexample promotion rule

A negative screen is not a candidate until a fixed dyadic vector and exact
`(c,N)` receive independently generated entry balls and the X-0001 exact checker
proves a Rayleigh upper endpoint below zero. The finite dictionary must also
pass its independent normalization audit.
