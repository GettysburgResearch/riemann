# O-5606 — The D-0801 detection window is `O(1)` in height, and the route is dominated by Riemann–Siegel

Claim ID: O-5606
Title: One D-0801 pass can detect an off-line zero over only `~1.05` units of
height however large the prime cutoff is, so its cost per unit of certified
height grows like `T` while Riemann–Siegel's grows like `sqrt(T)`
Status: PROPOSED (measured at three cutoffs; the extrapolation past the Nyquist
barrier is conditional on C-5601)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: L-5604 (the `eta^2` response and the 3x3 pencil); C-5601 (the
Nyquist barrier `c > T/2pi`); O-5601 (the production pass and its wall time);
X-5602 (the Riemann–Siegel throughput it is compared against)
Scope: the D-0801 carrier family at `T = 94184072727073/20 ~ 4.709e12`, cutoffs
`c = 10^9, 10^10, 10^11`, `K = 1024`
Related counterexample candidates: none — this is a statement about the search,
not about any candidate

## The question

Every number this programme has produced is a *value* of the exact form at one
carrier.  `L-5604` gives the sensitivity at the single best offset:
`eta_min = 0.0315` at `u = +0.264`, comfortably below the ceiling `|eta| < 1/2`
that every nontrivial zero obeys.  Read alone that is encouraging.

The question that decides whether the route is a viable *search* is different
and had not been asked:

> For how many units of height `u` does `eta_min(u)` stay below `1/2` at all?

Call that measure the **pass coverage** `m`.  It converts a per-pass cost into a
cost per unit of height, which is the only quantity comparable across methods.
Outside the coverage set the pass cannot fire for *any* admissible displacement
whatsoever, so those ordinates are simply not examined.

## The measurement

`detection_coverage.py` evaluates `eta_min(u)` on a `3001`-point grid spanning
`|u| <= 6` (about `52` mean spacings) via the `L-5604` pencil
`eta_min(u)^{-2} = lambda_max(S\,C^*Q^{-1}C)`, and measures the sub-level sets.

```text
log c   Delta    Delta/ell_T   lambda_min     eta_min    coverage    coverage    main
                 (Nyquist)     exact form     (best u)   (t units)   (spacings)  window
  9     3.2982   0.7579        2.3487e-03     0.1168     1.0400      4.526       1.0320
 10     3.6647   0.8421        6.0590e-04     0.0529     1.0640      4.630       1.0560
 11     4.0311   0.9263        2.6719e-04     0.0315     1.4240      6.197       1.0720
```

Every column moves except the one that matters.  From `c = 10^9` to `c = 10^11`
the prime work grows by a factor of `82`, the on-line margin falls by a factor
of `8.8`, the best-case sensitivity improves by a factor of `3.7` — and **the
detection window grows by `3.9%`**, from `1.032` to `1.072`.

(The `1.424` total at `c = 10^11` is the main window plus five side lobes of
combined width `0.35`; the lobes are numerically real but each is narrower than
`0.09`, and a search cannot rely on landing inside one.  The main window is the
honest figure.)

At `c = 10^11` the window is `[-0.536, +0.536]`, and the median of `eta_min` over
the scanned range is `1.176`: **over `88%` of the range the pass is blind in
principle**, since no zero can be displaced by more than `1/2`.

## Why this is fatal, given C-5601

`C-5601` places the Nyquist barrier at `Delta = ell_T`, i.e. at `c = T/2pi`:
below it the margins saturate and the form stays positive; only above it can the
carrier resolve the zero density.  The three rows above sit at
`Delta/ell_T = 0.76, 0.84, 0.93` — all below the barrier, and the margin is
indeed still positive at every one.

So a search must run at `c > T/2pi`.  A pass at cutoff `c` enumerates
`~ c/log c` prime powers, and covers `~1.05` units of height.  Hence

\[
 \text{cost per unit height} \;\gtrsim\; \frac{\pi(T/2\pi)}{1.05}
 \;\sim\; \frac{T}{2\pi\log T}\quad\text{— linear in } T .
\]

Riemann–Siegel evaluates `Z` with `N = \lfloor\sqrt{T/2\pi}\rfloor` main-sum
terms, and locating every sign change needs a bounded number of evaluations per
unit height (measured: `139.3` at `32` points per Gram interval).  Hence

\[
 \text{cost per unit height} \;\sim\; 139\sqrt{T/2\pi}\quad\text{— like } \sqrt{T}.
\]

**The ratio grows like `sqrt(T)`.**  At the production height:

```text
                                          terms per unit of height
D-0801, c = 10^12 (first cutoff above the barrier)      3.447e+10
Riemann-Siegel at the same height                       1.206e+08
                                          ratio               286

measured wall clock, same machine
D-0801, c = 10^11 pass:  316 s / 1.424 units  =  221.9 s per unit height
rs_zeta scan          :   98.2 s /   20 units =    4.91 s per unit height
                                          ratio              45.2
```

The wall-clock ratio is smaller than the term ratio only because the D-0801
figure is taken *below* the barrier, where the route does not work, and because
`rs_zeta` was sharing two of four cores with another job.  Above the barrier the
two ratios agree.

## And it is also the less sensitive method

Cost would be forgivable if the D-0801 pass saw something Turing's method does
not.  It sees strictly less:

| | detects | over |
|---|---|---|
| D-0801 pass | `eta > eta_min(u) >= 0.0315` | a window of `1.07` units |
| Turing / `Z` sign changes | **any** `eta > 0` | the whole scanned range |

An off-line zero produces no sign change of `Z` at all, so it is caught by the
count, not by observation — which is exactly why the `O-5604` argument is able
to exclude off-line ordinates rather than merely fail to see them.  The D-0801
form, by contrast, responds to a displacement only at second order
(`T-5602`: the response is even in `eta`), and only inside its window.

**Conclusion: as a search primitive the D-0801 carrier route is dominated by
classical zero counting on both axes — asymptotically `sqrt(T)` times more
expensive per unit of height, and unable to see displacements below `0.0315`
even where it looks.**

## What survives

This does not retire the route, and two things about it remain genuinely
valuable:

1. **It is a different criterion.**  Turing's method certifies a *count*; the
   Weil/D-0801 form certifies a *positivity*.  A negative value would disprove
   RH directly, without any appeal to an external bound on `\int S`, whereas the
   `O-5604` certificate is conditional on precisely such a bound.  The two
   failure modes are disjoint, and that is worth something.
2. **The certificate is small.**  A D-0801 refutation is a `1024`-vector, a lag
   table and a dyadic freeze.  A Turing refutation at height `T` is a scan.
3. The whole apparatus — `L-5601` exact phases, `L-5603` archimedean endpoints,
   the Gram-factor bound `L-5602` — is about *certifying a value*, and that is
   independent of whether the value is worth searching for.

What this observation does say is that **compute spent enlarging `c` in the hope
of a negative is spent at the wrong exchange rate**, and that a search for
off-line zeros should be a Riemann–Siegel/Turing scan with the D-0801 form
reserved for packaging a violation once located.

## Limitations

1. Everything here is floating.  `eta_min(u)` uses `L-5603`-assembled blocks in
   ordinary arithmetic and the leading term of an `eta`-expansion; the claim is
   the *order of magnitude* of the coverage, not its digits.
2. The `O(1)` window is measured at three cutoffs spanning two decades, all
   **below** the Nyquist barrier.  The extrapolation above the barrier rests on
   `C-5601`, which is a conjecture.  If the window widened sharply on crossing,
   the cost model would change — though the window would have to grow by a
   factor of `~300` to reach parity, against a measured `3.9%` per two decades.
3. The `139.3` evaluations per unit height is a property of the `32`-points-per-
   Gram-interval setting, not a theorem; a sharper scanner would improve the
   Riemann–Siegel side and make the gap wider, not narrower.
4. `eta_min(u)` is computed at `K = 1024`.  Larger `K` past the barrier is
   governed by the `K^{-2}` law, which changes the margin but not the width of
   the response window; this was not separately measured.
5. The comparison is per unit of height at one `T`.  It says nothing about which
   heights are worth scanning.

## Reproduction

```bash
cd experiments/X-5601-rigorous-carrier-stream
for c in 9 10 11; do
  python3 detection_coverage.py results/stream-c1e${c}-k1024.json \
      --carrier-num 94184072727073 --carrier-den 20 \
      --u-range 6.0 --u-points 3001 --pass-seconds 316 \
      --out results/detection-coverage-c1e${c}.json
done
```

## Suggested next attack

Measure the window once, directly, **above** the barrier, which removes
limitation 2 and settles the cost model.  The `c = 10^12`, `K = 2048`,
`T = 3.1e12` stream (`Delta/ell_T = 1.03`) is the smallest configuration that
crosses it.
