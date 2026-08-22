# X-105040 — proof artifacts for T-105040 (the smooth half closes)

Three-lane proof packet plus the orchestrator's cross-check standard.

* `lane1_rigor/` — the two proved lemmas. `lemma1_verify.py`: H-expansion
  `H(Y) = 4√Y + ζ(1/2)log Y + ζ'(1/2) + E(Y)` with the two-sided bound
  `|E| ≤ (log Y + 11)/(8⌊Y⌋^{3/2})` (Y ≥ 15) — constants derived from the
  ζ integral representation, bound verified by true-sup cell analysis on
  [2, 10⁵] (20× headroom). `lattice_sat.py`/`greedy_sat.py`: the sliver
  lock (e* = 1110, θ*_∞ = 0.419882602681071 exact rational, strict prefix
  inequalities by integer comparison) and the saturated closed forms with
  certified floors M₂ ≥ 1316.5009, M₃ ≥ 482.1523, M_sc > 13.903914 for
  all x ≥ 5P₆₁. `envsup.py`: |Ẽ_j| ≤ 1.081e−12 uniform envelope.
  `NOTES.md`: full derivations.
* `lane2_certify/` — the certified middle ranges. `common.py` (evaluator
  with explicit float64 error budgets), `certify.py` (grid + Lipschitz
  certificate; run twice: [10⁶, 5P₆₁] and — via CERT_X0/CERT_X1 env —
  [67, 10⁶]; 400+400 intervals, 0 failures; worst floors 98.54/36.67 and
  4.06/1.45), `validate.py` (brute-force cross-checks, envelope and
  derivative validation), `anchor_hp.py` (40-dps anchors), `sweep.py`
  (117,356-point dense sweep; minima 106.1986/39.3933 at 10⁶, inf M_sc =
  10.744179 at 1000587⁻). Structural results in `NOTES.md`: the
  F-identity, the M_sc ODE law (Corollary C), the jump law (Lemma A).
* `lane3_audit/` — assembly audit: contract re-derivation from L-99020,
  the jump-law measurements, edge cases ([2, 2000] sweep incl. left-limits;
  exact endpoint zeros), independent cancellation-free saturation
  verification (`saturation.py`; the M_j = ΔR_j − 4C_j·M_sc identity to
  0.0), and the recorded float64 incident (≥ 40 dps at x ≥ 10²⁶).
* `orchestrator_standard.md` — the pre-lane cross-check standard
  (H-constant = ζ'(1/2); slopes α_j = κ_j·B^s_θ matched to 7 digits by
  three independent derivations).

Arithmetic models, stated plainly: Segment 3 (tail) and the sliver lock
are exact/high-precision mathematics; Segments 1–2 are budgeted-float64
certificates with slack 70×–1800×, not interval-library arithmetic.
Nothing here bears on RH.
