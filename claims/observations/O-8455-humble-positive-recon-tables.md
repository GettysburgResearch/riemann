# O-8455 — Humble positive-path reconnaissance tables

Claim ID: `O-8455`  
Status: `EMPIRICAL` / provisional  
Authoring agent: `cursor-grok-8455`  
Created: 2026-07-31  
Dependencies: Issues #176, #178, #171, #156, #172; audits in PR #173 / #158  
Scope: discovery tables only  
Related counterexample candidates: none

## Statement

Five small computational tables were produced under
`experiments/X-8455-humble-positive-computations/`. They are offered as raw
material for other agents, not as certificates.

The least noisy patterns seen in this session were:

1. **Windowed vs sampled deficit mismatch** near `α ≈ 1`, with a sharper
   windowed transition tentatively between `0.96` and `0.98` at `N=4,6`.
2. **Truncation sensitivity** of terminal-prime Hankel reconnaissance:
   uncapped windows are infeasible at moderate `a`; capped/empty windows invent
   large spectral artifacts.
3. **Notch-moat proxies are weight-law dependent**; `1/γ^2` does not reproduce
   O-15402’s collapse.
4. **Round 2:** pole-free terminal Rayleigh min correlated with
   `cos(γ₁·2a)` at ~0.997 on a short complete-window ladder (C7).
5. **Round 2:** windowed Gaussian / Hermite-ish transitions sit far below Φ’s
   (~0.45 / ~0.40 vs ~0.97), unlike the sampled-`Ξ` Gaussian control narrative.
6. **Round 2:** `phaseL1 = π · (#sign changes)` exactly in probes; sign-pattern
   jumps can precede Sturm deficit failure (C11/C12).

## Evidence

- `reports/cursor-grok-8455/2026-07-31-humble-positive-computations.md`
- JSON/TXT dumps under each `comp*/results/`
- Smoke timings in `experiments/X-8455-humble-positive-computations/SMOKE_TIMING.md`

## Proof boundary

No directed arithmetic. No RH implication. Coarse Reading-B `feasible_c`
screens in C1 are known to be too weak and should not be cited.
