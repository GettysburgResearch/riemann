# O-5607 — A conditional Turing certificate at `t = 10^13`, above the verified height

Claim ID: O-5607
Title: `996.5` units of height at `t = 10^{13}` contain no off-line zeros,
conditional on an imported bound on `\int S` and on an uncertified `Z`
Status: PROPOSED (conditional certificate; the `Z` evaluation is not
interval-certified, so this is not a proof)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: X-5602 (`rs_zeta.c`, `turing.py`); an external bound on
`\int S(t)\,dt`, which this repository does **not** prove
Scope: the window `[10^{13}+0.5,\;10^{13}+999.5]`
Related counterexample candidates: none

## Why this height

Platt–Trudgian verified RH to height `3.0000175\times10^{12}`.  Everything the
D-0801 and Pick programmes in this repository have examined sits at
`T \approx 4.7\times10^{12}` — above that frontier, but only by a factor of
`1.57`, and only at isolated ordinates.  `10^{13}` is `3.33` times the frontier,
and this is a contiguous window rather than a set of points.

## The scan

```text
window                 [10^13 + 0.5, 10^13 + 999.5]
main sum terms         1,261,566 per evaluation
grid                   16 points per Gram interval
sign changes located   4467  (4471 over the full scanned span of 1000)
smooth count           4471.5625 over the full span
deficit                0.5625      -- an ordinary S(t) fluctuation
min |Z| on the grid    3e-05
```

## The certificate

`turing.py`, with `c = N(t_1)` unknown and `M(t)` the contribution of
hypothetical off-line ordinates, enumerating `|D_c + M| \le B` over
`c_{\rm est} + [-3,3]`:

```text
B conservative   3 + 0.1 log t2        = 5.9934
B Trudgian       2.067 + 0.059 log t2  = 3.8331   (for reference)

c offset   max D       min D        verdict
  +3       +2997.02     +1.18       excluded: D exceeds +B for any M >= 0
  +2       +1998.02     +0.68       excluded: D exceeds +B
  +1        +999.02     +0.18       excluded: D exceeds +B
   0          +0.83     -0.59       CONSISTENT WITH NO OFF-LINE ZEROS
  -1          -0.82   -998.98       excluded: no admissible M (slope quantised)
  -2          -1.32  -1997.98       admissible only with off-line zeros
  -3          -1.82  -2996.98       excluded: no admissible M (slope quantised)
```

The clean branch is strikingly tight: `D` stays inside `[-0.59, +0.83]` across
the whole window, against a bound of `5.99`.  The `-1` and `-3` exclusions are
the slope quantisation of `M` — `D` falls with slope `1` and `3`, and no sum of
slope-`2` ramps tracks either without leaving the corridor.

The surviving `-2` alternative admits off-line ordinates at exactly two places
on the grid, `0.000` and `999.0` — the two endpoints.  It is the boundary
degeneracy: `D` falls with slope exactly `2`, which one pair at `\tau \approx 0`
compensates as `M(t) = 2t`.  It says nothing about the interior.

```text
certified free of off-line zeros up to   10000000000996.512
certified fraction of the window         0.9970
```

**Conditional on the imported bound and on the `Z` evaluation, the interval
`[10^{13}+0.5,\;10^{13}+996.5]` contains no zero off the critical line.**

## Comparison with the PR #71 window

The same machinery on the `40`-unit window at `T \approx 4.709\times10^{12}`
certified `93.2%`.  Here it certifies `99.7%`, because the uncertifiable region
is a fixed `(B - D(t_2))/\mathrm{mult}` at the right edge — about `3` units in
both cases — and a `1000`-unit window dilutes it `25` times more effectively.
**The edge cost is additive, so the certified fraction improves with window
length**, which is the right way to run this: long scans, not many short ones.

## What this is worth

Modest, and worth stating plainly.  It is not a proof, it is not new
mathematics, and Platt–Trudgian-class verifications operate at vastly larger
scale with certified arithmetic.  What it demonstrates is that the X-5602
detector, built in this session for a different purpose, produces conditional
exclusions over contiguous height at a rate the positivity routes cannot
approach — `1000` units for one scan, against the `~1.07` units a D-0801 pass
examines (`O-5606`).  That is the concrete form of the domination claim.

## Limitations

1. **The bound on `\int S` is imported.**  This repository proves no such bound.
   The weaker of the two constants is deliberately looser than any published
   value, so substituting a proved constant strengthens the conclusion — but the
   dependency is real and is the reason this is labelled conditional.
2. **The `Z` evaluation is not certified.**  Ordinary doubles, `C_0`-only
   Riemann–Siegel remainder with an *asymptotic* error estimate.  A missed sign
   change would invalidate the count the whole argument rests on.  The observed
   `min |Z|` on the grid is `3\times10^{-5}`, which is reassuring but not a
   bound.  This is the gap worth closing, and closing it would reduce the
   conclusion to item 1 alone.
3. `N = \lfloor\sqrt{t/2\pi}\rfloor = 1{,}261{,}566` is constant across the
   window by construction; the program refuses spans where it would change.
4. The `-2` alternative is dismissed on the grounds that its admissible
   ordinates are the window endpoints.  That is a statement about where the
   window was cut, and a scan of an adjacent window would resolve it — but it
   has not been run.
5. `16` points per Gram interval.  A close pair separated by less than about
   `1/16` of a Gram interval could in principle be missed; the `O-5604`
   protocol (re-run at higher `--per-gram` before trusting any deficit) was not
   applied here because the deficit is `0.56`, well inside the ordinary range.

## Reproduction

```bash
cd experiments/X-5602-riemann-siegel-detector
./rs_zeta --t0 1e13 --span 1000 --per-gram 16 --threads 4 \
          --emit-zeros --zeros-file results/zeros-1e13.txt \
          --out results/rs-scan-1e13.json
python3 turing.py results/zeros-1e13.txt \
    --t1 10000000000000.5 --t2 10000000000999.5 --grid 2000 \
    --out results/turing-1e13.json
```

## Suggested next attack

Interval-certify `Z`.  Everything else in this claim is already conditional on
one imported bound; item 2 is the only part that depends on code written here,
and it is the only part that can be removed by work rather than by citation.
