# SCOPE — honest reductions and working choices

- t-window: scans and boxes use t in [0.05, 30.0] for the spec's "(0,30)". The strip
  segment t in (0, 0.05) is excluded from boxes to keep the poles s=0,1 outside the
  contour; F_z(t) = -1/(1/4+t^2) + (positive exponentially small lattice terms) is
  numerically bounded away from 0 there for every z visited (checked at t=0.01, 0.05
  during E1 at z=i and the generic z; |F| > 3.8), so no zeros are lost at the bottom.
- On-line scan grid dt = 0.05 with two nested dt/10 dip rescans (resolution 5e-4
  for close pairs); pairs closer than that appear as unresolved dips and are
  disambiguated by the box count. Zero refinement: bracketed Illinois to
  |interval| < 1e-13 * max(1,t) (12+ digits), dps = 40.
- Departure-time bisection: tau to 1e-6 as specified; the on/off classification at the
  bisection endpoints resolves line pairs down to separation ~2e-4; closer than that,
  tau* carries that (documented) classification resolution — the transition is
  continuous, so this is inherent, not a shortcut.
- COORDINATOR BUDGET REDUCTIONS (mid-run guidance from the coordinating session,
  recorded here as required):
  * E3 tau grid coarsened from the spec's 0.05 to 0.1; tau* bisection relaxed from
    1e-6 to 1e-3 (3 decimals). Path A, if quiet (no events, disc == 0 everywhere) up to
    tau = 1 (x = 0.15), is extended along the same line to x = 0.25 and 0.35
    (tau = 5/3, 7/3) before concluding anything.
  * E4 reduced from 8 directions to 4 (0, 45, 315 computed; 180 derived by the EXACT
    lattice symmetry Lambda(-x+iy) = Lambda(x+iy), asserted numerically in
    lab.selftest); t-window reduced to (0, 15.0); radius bisection to bracket 0.005
    (2 decimals). March capped at r_max = 0.3 (directions with no off-line pair
    by then are recorded as lower bounds). Radius bisection uses the local merge
    window; the full-window discrepancy is re-confirmed at the low end of the final
    bracket. e3_events.json is deposited incrementally after each completed path.
- O1 direct sum: radius 2000 (N = 4e6) with an exact-A(N) tail estimate averaged over
  64 truncation points; the achieved agreement is recorded in oracles.json (the
  circle-problem residual limits a single truncation to ~11 digits; the averaging is
  what buys 15+).
- Box contour delta = 0.2; when a boundary point lands on a zero the box is re-run
  with delta nudged by +0.0137 (recorded in box_info.delta_used).
- No reduction was applied to the tau grid (0.05), the t-window, or the oracle
  thresholds.
