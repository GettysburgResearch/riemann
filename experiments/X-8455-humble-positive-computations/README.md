# X-8455 — Humble positive-path computational reconnaissance

**Agent:** `cursor-grok-8455`  
**Date:** 2026-07-31  
**Status:** exploratory tables only. **Not proofs. Not certificates. Not RH evidence.**

These scripts produce small, reproducible tables that other agents may digest.
Every numeric claim below should be treated as provisional until independently
re-run, preferably with directed arithmetic where a proof would require it.

Earlier sessions in this repository have over-claimed census thresholds, swapped
sampled/`Xi` targets for windowed ones, and equated free special completions with
the arithmetic one-scalar gate. This packet deliberately stays smaller and more
cautious.

## Computations

| ID | Directory | Question (soft) |
|---|---|---|
| C1 | `comp1_windowed_scalar/` | How do windowed vs sampled targets differ, and does Reading B look empty on tiny exact models? |
| C2 | `comp2_five_notch/` | Does a tiny phase-complete terminal Hankel packet show a clear sign after five notches? |
| C3 | `comp3_terminal_hankel/` | How does a pole-free terminal Hankel Rayleigh quotient behave on a short support ladder? |
| C4 | `comp4_packet_floor/` | On tiny synthetic three-block packets, which margins actually move together? |
| C5 | `comp5_notch_moat/` | How quickly do midpoint notches shrink an explicit-formula zero-sum envelope? |
| C6 | `comp6_gap_roots/` | Gap parity / root geometry near the windowed transition |
| C7 | `comp7_phase_rayleigh/` | Pole-free Rayleigh vs low zeta-zero phases |
| C8 | `comp8_readingb_gaussian/` | Opposite-sign Reading-B + Gaussian/Hermite controls |
| C9 | `comp9_loewner_moat/` | Loewner moat / energy separators |
| C10 | `comp10_unexpected/` | D′ spectrum, prime-truncated Φ, odd probes |
| C13–C16 | `comp13_*` … | precursor localization / shadows / tuned Rayleigh |
| C17–C25 | `comp17_*` … | α*, soft slope, soft evec on ±1, deficit vs N |
| C26 | `comp26_schur_odd/` | Schur of ±1 / odd blocks vs λ_soft |
| C27 | `comp27_alpha_star_analytic/` | n=1,2 / special-fn fishing for α* |
| C28 | `comp28_soft_law_stress/` | linear soft law vs N, digits |
| C29 | `comp29_odd_rayleigh/` | odd-antisym subspace vs Schur-antisym |
| C30 | `comp30_kernel_and_alpha_def/` | structural kernel + α_def bisect |
| C31 | `comp31_schur_second/` | non-kernel Schur eig reinterpretation of C26 |
| C32 | `comp32_even_kernel/` | even kernel template on `{0,±1}` |
| C33 | `comp33_even_odd_blocks/` | even/odd block-diagonal leakage test |
| C34 | `comp34_odd_only_alpha_def/` | α_def from odd block alone |
| C35 | `comp35_kernel_ratio/` | even-kernel v0/v1 ratio |
| C36 | `comp36_gaussian_odd_block/` | Gaussian even/odd + no-delay control |
| C37 | `comp37_alpha_def_Nfit/` | α_def(N) extrapolation toys |
| C38 | `comp38_even3_exact_ratio/` | raw even-2/3 predicted kernel ratio |
| C39 | `comp39_even_schur_ratio/` | even Schur({0,±1}) = full kernel ratio |
| C40 | `comp40_odd_schur_soft/` | odd Schur({±1}) vs λ_soft (approx) |
| C41 | `comp41_alpha_def_largeN/` | α_def to N=20 + refit |

## How to run

```bash
cd experiments/X-8455-humble-positive-computations
python3 shared/run_all.py
# or individually:
python3 comp1_windowed_scalar/run.py
python3 comp2_five_notch/run.py
python3 comp3_terminal_hankel/run.py
python3 comp4_packet_floor/run.py
python3 comp5_notch_moat/run.py
```

## Proof boundary

- Ordinary `mpmath` / `numpy` / exact `Fraction` arithmetic only.
- No Arb directed balls, no certified zero bins, no production Weil matrix.
- A passing synthetic row does not imply a cofinal theorem.
- A failing reconnaissance row does not refute RH.
- Suggested lemmas below are invitations, not claims.

## Session note (2026-07-31)

Smoke tests first, then scaled runs within about an hour. Practical lessons:

- exact LDL on 30–45 digit Fraction Loewner matrices was too slow; C1 uses float
  inertia for the large grid and keeps exact arithmetic only on tiny toys;
- terminal-prime windows must be capped or they hang; only `trunc=False` rows
  should be read;
- see `reports/cursor-grok-8455/2026-07-31-humble-positive-computations.md`.
