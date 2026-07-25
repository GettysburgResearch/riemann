# O-5602 — The D-0801 margin varies by a factor of 46 across nearby carriers

Claim ID: O-5602
Title: A 256-point certified carrier scan shows the leading margin is a strongly
structured function of `T`, and that the Issue #42/#44 carrier sits at a deep
local minimum
Status: PROPOSED (per-carrier values EMPIRICAL; the extremum is certified)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-0801; L-0801; L-5601; L-5602; O-5601
Scope: `c = 10^8`, `K = 1024`, 256 carriers
Related counterexample candidates: none

## The scan

`experiments/X-5601-rigorous-carrier-stream/carrier_scan.py` ran one complete
directed stream per carrier — all `5,762,859` prime powers below `10^8`, phases
by L-5601 — for

\[
 T_m=\frac{94184072727073+4m}{20},\qquad m=0,\ldots,255,
\]

i.e. `T` from `4709203636353.65` to `4709203636404.65` in steps of `0.2`.  The
local zero spacing at this height is `2\pi/\log(T/2\pi) = 0.2298`, so the scan
covers about 222 mean spacings at slightly under one sample per spacing.

```text
margin_min   0.0066414741170204294     at m = 0   (the Issue #42/#44 carrier)
margin_max   0.3082187205143594        at m = 255
margin_mean  0.10910971851677806
margin_std   0.09081927185943253
```

The extremum was re-run through the full L-5602 certificate:

```text
certified universal margin at T = 94184072727073/20:  >= 0.006641472902948355 > 0
```

## What it says

1. **The margin is not noise.**  Its standard deviation is `0.091` against a
   mean of `0.109`; it ranges over a factor of `46`.  `ell_T` is essentially
   constant over the scan (`d ell_T/dT = 1/(2\pi T) \approx 3.4\times10^{-14}`),
   so all of the variation is in `lambda_max(S_K(T,c))`.
2. **The carrier used throughout Issues #42/#44/#55 is a deep local minimum** —
   about `16x` below the scan mean.  The "optimized carrier continuation" of
   PR #42 evidently did find something real.  Every number in O-5601 should be
   read as *the best carrier known in this neighbourhood*, not as a typical one.
3. **Carrier search is the productive direction.**  A complete certified stream
   costs `0.72 s` at `c = 10^8` and `3.5 s` at `c = 10^9`, so thousands of
   carriers are affordable.  If a `46x` spread exists over 51 units of `T`, the
   natural question is how deep the minima get over a much wider range, and
   whether any carrier reaches the `10^{-8}` scale where the L-4202 correction
   gate becomes load-bearing.
4. **The scan as run was one-sided and should be redone.**  It starts *at* the
   minimum and walks upward, so it maps one wall of one basin.  A two-sided,
   wider, adaptively refined scan is the obvious successor.

## Limitations

- One cutoff, one cell count, one 51-unit carrier window, one direction.
- Per-carrier margins come from `numpy.linalg.eigvalsh` on the assembled matrix
  and are **nominations**, not certified: only the minimum was re-certified.
  The stream feeding them is directed, so the *matrix* is bounded (L-5601); it
  is the eigenvalue step that is floating.
- A small margin at one cutoff does not imply a small margin at another; the
  minimizing carrier can move with `c`.
- Nothing here approaches zero.  The smallest certified value in the scan is
  `6.6e-3`, which is `4\times10^{7}` times the correction gate.

## Suggested next attack

Two-sided adaptive scan at `c = 10^9`: coarse pass at step `2` over `\pm10^4`
units of `T`, then bisect into every basin whose floating margin is below the
running minimum, then certify the best few with L-5602.  Budget: a coarse pass
of `10^4` carriers is about ten hours of four-core time, and each refinement
level is cheap.  Cross-reference `C-5601`: the search should be run at a carrier
*and* cutoff pair with `c \ge T/2\pi`, which for `c = 10^9` means `T \le 6.3e9`.
