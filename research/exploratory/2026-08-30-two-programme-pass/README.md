# 2026-08-30 two-programme pass — Riemann Structures (#763) × Generalized L-Objects (#764)

```text
Status:  EXPLORATION + PROVED components (per-claim labels govern; see
         claims/methodology/M-108000-two-programme-pass-contract.md)
Scope:   finite and exact throughout, except numerics labeled
         NON_DIRECTED_HIGH_PRECISION / FLOATING_RECONNAISSANCE which are
         conjecture-generating only; no global/unbounded conclusion is drawn
         from any finite computation; RH and GRH are unproved and unaddressed
Exact sources or dependencies: main @ the pass base commit; pinned imports
         from origin/codex/l-function-detector-atlas recorded in
         integration/2026-08-30/ source locks; sympy 1.14.0 and mpmath 1.3.0
         for symbolic/numeric layers (versions locked in provenance files);
         all conclusion-bearing finite computations are stdlib-exact
What was actually run: see integration/2026-08-30/ source locks and each
         experiments/X-1080xx / X-1085xx replay
Smallest remaining gap: per-claim; the ranked continuation queues live in
         reports/claude/2026-08-30-*.md
```

## Layout

- `core/` — exact stdlib algebra (Fraction polynomials, Berlekamp-Massey,
  Newton identities, symmetric-power calculus, Sturm certificates), the
  world schema contract, the trace-to-object structure detector, and the
  sympy symbolic defect extractor.
- `worlds/` — the cross-world corpus: one build script + one validated JSON
  record per world (zeta, Dirichlet mod 5, elliptic 11a, function-field
  elliptic/F5, Ihara Ramanujan + non-Ramanujan, Beurling, Davenport-
  Heilbronn, Epstein pair, three engineered counterfeits, pinned repo-native
  imports). Every cell of every record carries status + rigor + witness.
- `matrix/` — the assembled survival/mechanism matrix (the #764 ladder view
  and the #763 mechanism view of the same corpus) and the transform-defect
  runs.
- `epstein/` — the lattice-moduli zero-bifurcation laboratory
  (#764 experiments 15-19; NON_DIRECTED_HIGH_PRECISION).
- `BOUNDARY_AUDIT_CONSOLIDATED.md` — the literature collision audit gating
  every novelty statement of the pass.

## Reading order

1. `BOUNDARY_AUDIT_CONSOLIDATED.md`
2. `matrix/MATRIX.md` (the two-view matrix with witness index)
3. claims bands `T/L/R/O-1080xx` (#763) and `T/L/R/O-1085xx` (#764)
4. `reports/claude/2026-08-30-*.md` (per-programme checkpoints + bridge)

## Pass 3 additions (2026-08-31; campaigns C1-C8)

- `matrix/ap_table_11a1.json` — exact a_p for 11a1, 9591 good primes
  <= 1e5 (Hasse-checked); shared input for C2/C4.
- `matrix/c1_defect_atlas.py|json` — the defect atlas: spectrum
  polynomials M_m (m <= 9), tower discriminants factored, the (m,d)
  codimension grid, transform defects, 192-point splitting census.
- `matrix/m10_m11_spectrum.json`, `matrix/m12_m13_spectrum.json`,
  `matrix/spectrum_collision_loci.json` — the torsion-resonance data
  (O-108512): collision loci with two held-out confirmations.
- `matrix/c2_phase_diagram.py|json` — the trace-scaling line: exact
  strata identities, |t| = 1 phase transition (L-108511).
- `matrix/c4_boundary_telescope.py|json` — zero constellation of the
  bridge product on Re s = 3/2, root-angle dichotomy, honest controls.
- `graphs/` — the C5-C7 graph telescope: `telescope.py|json` (atlas +
  certified rewiring walks), `spectroscopy.py|json` (breach sides +
  minimal polynomials), `census14.py|json` (n = 14 extension). Claims:
  O-108006.
- `epstein/c8_run.py`, `epstein/c8_campaign.json` — the 12-direction
  departure-radius campaign with geometric invariants per event.
- Theorems grown from these campaigns: T-108509 (deformation
  spectrum, standalone/2026-08-31-deformation-spectrum/) and T-108510
  (codimension law, standalone/2026-08-31-defect-codimension-law/),
  with stdlib replays X-108509 / X-108510.
- Pass report: `reports/claude/2026-08-31-two-programme-pass3.md`.
