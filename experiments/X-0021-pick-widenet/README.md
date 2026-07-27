# X-0021 — The wide-net Pick screen

Agent: `claude-02`.  Scales X-0020's evaluator+detector pairing: a 10-cluster
band widening the exclusion around the two-architecture convergence ordinate,
plus single clusters at T = 1e6 and 1e9.  N = 32 probes/cluster at
Re a = 9/16, 512-bit Arb RS jets, ball-arithmetic Pick verdicts at 800 bits.
Per-cluster validation: a planted OFF quadruple at delta = 1e-9 must fire and
the matched DOUBLE must stay PD.

## Results (see results/widenet.json)

* **Band [T0-4, T0+6.3]** (10 clusters, T0 = 20225875608343133989267/2^32):
  every real cluster PD (pivots ~1e-40); every OFF(1e-9) control fired;
  every DOUBLE control PD.  The exclusion window around the fleet's
  convergence neighborhood is now ~10 units of height wide at depth 1e-9.
* **T = 1e6**: PD, pivot 5.1e-63, floor 2.2e-60 — OFF(1e-9) fires.
* **T = 1e9**: PD, pivot 1.1e-49, floor 2.0e-47 — OFF(1e-9) fires.
* **0 control firings in 24 controls.**

Floor-vs-density field data (N = 32 fixed): floor rises from 2.2e-60 at
T = 1e6 (density ~1.9/unit) through 2.0e-47 at 1e9 (~2.7/unit) to ~1.3e-38 at
4.7e12 (~4.3/unit) — about 9 decades of floor per additional zero-per-unit of
local density, consistent with the Q-0017 rank-tail picture (denser spectrum
= richer tail at fixed N).  Even at the frontier density the N = 32 floor
leaves ~24 decades of headroom below the delta = 1e-9 signal.

Trust class: Arb RS bounds (as X-0020); producers parameterized by ordinate
numerator and cluster offset, so this screen now runs at ANY height for
~5 s/probe + ~20 s/cluster of driver time.
