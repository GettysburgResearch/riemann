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
7. **Round 3:** Loewner `n_neg` jumps with the deficit, not the sign precursor;
   precursor localized to `p_{±2}` zero at α≈0.99755 (C13/C16). Naive γ₁
   cos/sin tuning destroyed the terminal Rayleigh lock (C15).

## Evidence

- `reports/cursor-grok-8455/2026-07-31-humble-positive-computations.md`
- JSON/TXT dumps under each `comp*/results/`
- Smoke timings in `experiments/X-8455-humble-positive-computations/SMOKE_TIMING.md`

## Proof boundary

No directed arithmetic. No RH implication. Coarse Reading-B `feasible_c`
screens in C1 are known to be too weak and should not be cited.
8. **Round 4:** α*(p2=0)≈0.9975450892474784; after it a Loewner soft
   mode declines to 0 then emits a negative pair at the deficit (~0.975).
   Gaussian has p2-flip but no delayed deficit; Hermite-ish differs (C17–C19).
9. **Round 5:** α* is fixed by the first two Φ terms; after α*, Loewner
   min_pos falls nearly linearly (r²≈0.99996) and hits 0 at the deficit jump
   ≈0.97505 (C20–C21). Reading-B cones stayed one-sided in coarse probes (C22).
10. **Round 6:** soft Loewner eigenvector mass is on `j=±1` (~99%), not on
    `j=±2`; α_def≈0.975 for N≥5 on a coarse grid (C23–C24).
11. **Round 7:** soft mode = odd-antisym Loewner ground state (ratio 1±1e-12);
    Schur({±1}) works once a structural ~0 even kernel is quotiented (C26/C29/C31).
    α* fixed by Φ n=1+2 (Δ~1e-10); α_def(N) bisect≈0.9734…0.9756 for N=4…10 (C27–C30).
    Even/odd Loewner leakage ≤8e-17; kernel ≈ even 3-point mode on `{0,±1}` (C32–C33).
    Odd-only α_def(N=4…12) rises to ~0.97568; tiny-N fit suggests a_inf≈0.9758 (C34/C37).
    Gaussian control: even/odd still splits, but p2-zero and odd_min-zero coincide (~0.47) — no delay (C36).
    Even-kernel ratio recovered by Schur({0,±1})_even to ~1e-13 (C39).
    Odd Schur({±1}) only ≈λ_soft (ratio~1.004); full odd subspace is exact (C40).
    α_def(N=20)≈0.975758; refit a_inf≈0.97577 via a+b/N³ (C41).
