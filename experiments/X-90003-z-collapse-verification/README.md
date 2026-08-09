# X-90003 — Verification artifacts for T-90002 (Lemma S promotion + z-collapse)

Claim ID: `X-90003` (provisional; allocate at registry)
Session: `riemann-proof-review-8nz34i`, Strike B prong B3 (2026-08-09)
Backs: `claims/theorems/T-90002-z-collapse-lemma-s.md`

## Scripts

- `profile_cells.py` — all load-bearing finite inequalities of T-90002 §1 (Theorem P):
  P1 cell-formula cross-check vs raw \(E\); cells 2–6 suprema < 0; cell 7 strict decrease,
  endpoint signs, slope ≥ 1.7305, \(c^*\) to 20 digits; cells 8–17 endpoint minima > 0.0329;
  \(\Xi(N)\)-scan N=18..400 with the provable \(D(N)\) plus N>400 envelope; \(|\delta_N|\le D(N)\)
  spot checks; P4 c-Lipschitz ≤ 1.28; certified driver bracket for \((1+\zeta(1/2))\log 2\)
  from P2's own σ-inequality at N=10^6. Exits nonzero on any failure. Runtime ~2 min.
- `discrete_check.py` — exact \(s_X(q)\) for all \(2\le q\le Y\) at \(X\in\{100001,199999,200000\}\)
  (even + odd): exactly one sign flip, at \(\lfloor c^*X\rfloor\); no exceptions outside the ±52
  window (in fact none outside ±1); Theorem Q lower bound slack > 0 on \(q\le X/110\); the exact
  two-scale identity of T-90002 §2 to ~1e-11 (float accumulation), including the \(q\mid Y\)
  correction \(\beta_Y\); floor-bound ratio ≤ 0.072 of the T-90001 §1 majorant.

## Status of runs (this session)

`profile_cells.py`: ALL PASS. `discrete_check.py`: all checks pass at the three X values above;
earlier exploratory runs also passed at X=6000 (identity, incl. q|Y cases q=2,3,5,12) and the
fleet's X grid to 5·10^5 (O-90004 §1).

## Reproduce

python3 profile_cells.py && python3 discrete_check.py
