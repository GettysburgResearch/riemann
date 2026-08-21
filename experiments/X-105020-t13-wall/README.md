# X-105020 — the t = 13 wall: three-lane computation packet

Verification for `L-105021`, `L-105022`, `O-105023`, `R-105024`,
`L-105025`, `M-105026`.

## Driver (run this first)

`python3 verify_pivotal.py` → `ALL PIVOTAL CHECKS PASSED` (~2 s).
Re-derives from scratch and asserts: the complete `2^{18}`-lattice
quarantine enumeration (negative set = 19 points ≤ 61, min `−2323/30030`
at 13); the cap crossings `C(7/20) = 67.4938767…`, `C* = (45045|B₁₃|/4646)²
= 87.3589317…` with `H₁₃(67) > 7/20 > H₁₃(71)` and `H₁₃(87) > 0 > H₁₃(88)`;
the circulation law constants `c₁ = 4(1/67 − A₁₃) = 371342/1006005` and
`4|A₁₃| = 9292/30030`; the depth-split identity's closed-form value at `z = 1.5` (the sieve side
of the identity is re-derived in `lane_primezeta/`); and the
`B₂` log²-blow-up at `z → 1⁺` (`1.808 / 19.602` at `10⁻² / 10⁻⁴`).

## Lane subdirectories (full computations, as produced)

* `lane_hall/` — `moat.py` (exact-rational + 250-bit interval crossings,
  full `t < 500` table), `hall_lp.py` (per-fibre Hall LP / max-flow,
  duals; prefix⟺LP equivalence verified to `1.4e−13`); output table in
  `results/moat_out.txt`.
* `lane_circulation/` — `task1_reproduce.py` (239 atoms,
  `E_T − O_T = 17.00508653821905…` interval-certified),
  `circulation.py` (two-leaf Hoffman model, cut family, Edmonds–Karp
  cross-validation, witness ladder), `verify.py`, `final_aux.py`
  (lattice `A_t` scan, closed-form checks).
* `lane_primezeta/` — `lane_p_main.py` (μ/rough-depth sieve to `10⁷`,
  Dirichlet-identity verification, transform quadrature, `h^{(≤2)}` scan
  on `[1,10⁶]`), `lane_p_aux.py`, `lane_p_check2.py` (tail-corrected and
  non-circular cross-checks; germ/blow-up measurements).

Caveats: lane scripts are deposited as executed (paths may reference the
producing scratchpad); the driver is self-contained and is the replay
standard for the claims. Nothing here bears on RH.
