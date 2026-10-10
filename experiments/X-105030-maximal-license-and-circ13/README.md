# X-105030 — maximal license, CIRC-13 theorem, moving-boundary cancellation

Verification for `T-105030`, `L-105031`, `L-105032`.

* `lane_circ13/` — `circulation.py` (the O-105023 model re-run verbatim),
  `constants.py` (exact/interval constants: `X₀ = 77.930274054…`,
  `c₁ = 371342/1006005`, `c₀`, the `F₀(13)` algebra), `multileaf.py`
  (independent Edmonds–Karp on the general multi-leaf class: two-leaf
  deficits = `V(S₁)` to `1e−28`; monotonicity under added leaves; depth-3
  configuration at `X = 4·10⁵` with `deficit = V(S₁)` exactly; the
  all-heads-vs-depth-1-heads comparison).
* `lane_repair/` — `core.py`/`fast.py` (Theorem R greedy criterion),
  `lp_check.py` (full pair-variable LP cross-check, ≤ 94k variables,
  agreement `8.3e−13`), `sweep.py`/`scan.py` (all fibres to `10⁶`; the
  eight cuts), `identity.py` (the `G_j` regrouping and `W`-identity;
  score identity to `7e−15`), `witness.py` (x = 88 and `10007⁻` flow
  structure; crossing law), `hp_check.py` (increment lemma constants),
  `extras.py`, `lattice.py` (complete `2^18`-cell frozen-block balance:
  `TB_s ≥ 1.676601032` on all of `[2, P₆₁]`).
* `lane_boundary/` — `f1_regularity.py` (CORRECTED; self-contained sieve
  to `10⁶`): asserts the exact pole-coefficient cancellation (identical at
  finite truncation), the divergent drift of `F₁` with the true
  z-dependent `M_z` (`−4.34 → −7.74`, the surviving log germ), and the
  truncation-free x-space law `Ψ₁ ≈ −4√x/log x` (`−4.38 / −4.55` at
  `10⁴/10⁶`). The first deposit of this script asserted bounded `F₁`
  values produced by an `M₁`-for-`M_z` substitution — wrong, caught by
  the session's recovery pipeline; see `L-105032 §5`.

Caveats: lane scripts deposited as executed (paths may reference the
producing scratchpad); `f1_regularity.py` and `lane_circ13/constants.py`
are the replay standards for the displayed constants. Nothing here bears
on RH.
