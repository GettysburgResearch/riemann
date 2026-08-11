# Macroscopic first-Hermite positivity — 2026-08-11

**Branch:** `research/gpt56-pro/379-macroscopic-heat-positivity`  
**Base:** PR #379 at `589f1c05ccaf248cf08c87fefa7d5ab6d2380708`  
**RH:** unproved

## Result

The first-Hermite scalar from PR #379 is unconditionally positive in two large regions:

```text
q sufficiently small, uniformly for every real centre x;
fixed q, all sufficiently large |x|.
```

The proof uses only:

- the coarse effective lower bound `mu(t)>=c log(2+|t|)-C` from Stirling;
- the paired inequality
  `log(2+|x+u|)+log(2+|x-u|)>=log(2+u)`;
- an annulus at `u~q^-1/2`, which creates a uniform
  `q^-3/2 log(1/q)` gamma reserve;
- `Lambda(n)<=log n`, making the small-`q` prime channel superexponentially small;
- absolute convergence of the fixed-`q` prime series.

## Meaning

A negative witness cannot occur at fixed Gaussian resolution and arbitrarily high ordinate. Any hypothetical terminal-pair witness at growing height requires `q->infinity` as well.

Thus the unresolved region is the joint diagonal

```text
x -> infinity,
q -> infinity.
```

At every integer `q=n`, an effective compact interval `[-X(n),X(n)]` contains every possible negative centre. This turns PR #379's countable criterion into a compact search at each resolution, though the resolution index remains unbounded.

## Boundary

```text
broad-kernel positivity                 proposed complete unconditional
fixed-resolution exterior positivity    proposed complete unconditional
compact search interval at each q        proposed complete
joint growing x,q sign                   open / RH-equivalent
Riemann Hypothesis                       unproved
```
