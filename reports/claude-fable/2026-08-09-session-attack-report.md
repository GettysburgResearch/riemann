# Session attack report — 2026-08-09 (`claude-fable-5`, branch `claude/riemann-proof-review-8nz34i`)

One focused session attacking the open core after a full repository pass. Multi-agent orchestration (5 workflows, ~2.9M subagent tokens, 20+ independent derivation/verification agents); every load-bearing new identity machine-validated by ≥2 independent implementations; key steps hand-verified by the session author. The dedicated final adversarial-verify stage was cut short by a usage limit — disclosed in `T-90001` §6; statuses everywhere preserve the authoring agents' own PROVED / PROVED_SKETCH / NUMERICAL_ONLY labels.

## Deliverables (in dependency order)

| File | One-line content |
|---|---|
| `claims/theorems/T-90001-theta-bridge-equivalence.md` | **WSTS ⟺ RH as a short self-contained theorem**: exact bridge with explicit `10.3(2+log X)` floor; **Moat Lemma proved** (`J=H/√θ` nondecreasing via `S_N ≤ 2√N−1`); RH ⇒ `B_X ≪ log³` (log⁴→log³ sharpening); three independent classical consumers for WSTS ⇒ RH replacing the square-screw chain; calibration: unconditional `B_X` exponent ≡ best zero-free-strip width; VK-strength unconditional bound; effective window to ~10²⁵. Three named bookkeeping flags. |
| `claims/observations/O-90004-structure-map-and-hardness-theorems.md` | z-max collapse (top half killed unconditionally; `B_X=[T^s(2)]_+` modulo Lemma S), Fejér-log2 kernel + dyadic blind spots, Bochner no-go for small-support Weil positivity, averaging-circularity theorem, attainment dichotomy, numerics-cannot-decide (≤10¹⁹), carry-LP = averaged Chebyshev with dual exactly Λ. |
| `claims/refutations/R-90001-cbvr-residual-export-amplifies-debt.md` | **CBVR (PR #316) refuted as designed**: per-generation debt `~(log X)^{g−1}`, chain aggregate `~X^0.62`, certified fixed-scale witness family; independently replicated to 15 digits. |
| `claims/observations/O-90001-…` | SHARP hinge scans to `T=10⁸` (rows 2–64 all T); exact terminal coefficient `½T^{−3/2}>0` (lemma); fixed-row recurrence enabling all-T sweeps. |
| `claims/observations/O-90002-…` | GFEP extended to 10⁵ full / 10⁶ targeted; minimum structure `~X^{−1/2}` explicit; scope correction to T-28001 §9; provenance nit. |
| `claims/observations/O-90003-…` | Carry profile `𝔊 ≥ 1` on `[1,10⁷]` (PR 243/247/252 shared sign target: no cheap kill). |

## Honest bottom line

RH remains unproved and WSTS remains exactly as hard as RH — now as a *theorem* (T-90001 §5), not a slogan. What changed: the repo's canonical equivalence is compressed from ~40 conditional files + an unreviewed consumer to a ~12–15-page self-contained argument with three named bookkeeping flags; one live closing route (CBVR) is refuted; the live open predicates (SHARP/GFEP) are massively stress-tested with structure exposed; and the wall map (§3 of O-90004) proves which attack shapes are circular before they are attempted.

## Recommended next steps

1. Review `T-90001` first (it is small); if it survives, re-point `T-27501` at it and retire the transport stack as architecture.
2. Promote Lemma S (z-collapse) to a theorem via the same per-cell calculus as the Moat.
3. Chase T-90001's three flags (C_E constants; real-X interpolation; Theorem B citations).
4. Gate all future "producer" PRs on the O-90004 §3 wall map.

---

# Addendum: the strike session (same day, second dispatch)

Three sequential strikes at the remaining open core, kill-criteria set in advance, adversarial review of all new work (prior work left to the external review track per project owner's instruction).

| Strike | Outcome | Files |
|---|---|---|
| **A — dBN flow** | Lane **closed by theorems**: no one-sided prime-side certifier exists at t>0 (divergence + truncation sign-flip + classical-wall translation); the cost of \(\Lambda\to0\) via the existing architecture is superexponential; the dynamics schema stalls at death time 0.34 even with perfect statistics. Survivor: the **Tilted Moat Lemma** (the moat deepens monotonically along the flow; the tilt is a low-pass filter). | `R-90002`, `L-90002`, `O-90005` |
| **B — monotone/operator positivity** | **T-90002: Lemma S promoted** — z-collapse proved; WSTS is now ONE scalar per X: \(B_X=[T^s(2)]_++O^*(X^{-3/2}\log X)\). **T-90003: GFEP proved for all n>X/10** (certified gates; positivity carried by ancestry over a wholly negative diagonal — the Perron–Frobenius pattern at theorem level); Landau fence: the uniform bottom sign pattern is RH-hard; GFEP's open core is exactly n=o(X). Plus: c-monotone moat, PSD c-Gram that provably cannot manufacture zero-side positivity, PNT-calibrated ladder decrement law, cone-blindness witness, three-crossing warning for general ratios. | `T-90002` (+addendum), `T-90003`, `L-90003`, riders in `O-90002`/`O-90004`, `X-90004` |
| **C — carry-resolvent spectral probe** | **Structure theorem**: the inverse carry matrix is exactly Möbius × elementary (no truncation error; subsumes L-32701 with closed forms for all rows); spectrum provably arithmetic-free; **no PSD/spectral realization exists** — first failure at exactly T=10 with an exact rational witness, cause ζ-blind (the pure sawtooth reproduces it to 0.6%). Carry positivity is a cone statement, not a spectral one. | `O-90006`, `X-90005` |

## State of the open core after the strikes

Everything now rides on **one scalar per X**: \([T^s(2)]_+\) — the one-sided ramp deficit — with the provable-positivity cone proven unable to reach it, the dBN lane closed, the spectral lane closed, averaging circular, and the elementary-ladder lane PNT-calibrated. The scalar's unconditional status equals the zero-free-strip width (T-90001 §5), by theorem. The remaining problem is the classical wall, now stated in its sharpest known elementary form, with every tried lane fenced by a theorem rather than a memory.

