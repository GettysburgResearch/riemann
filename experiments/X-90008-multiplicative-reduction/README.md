# X-90008 — Multiplicative reduction artifacts (T-90008, Stage 1 of the bootstrap dispatch)

Exact exhaustive minimization of the transported GFEP/Form-A functionals over the class
H = {completely multiplicative ±1 sources}, via the disjoint-fiber core+fold WHT
decomposition (exact for the full class; sizes 2^25..2^669 covered).

- `m1_mult.py` — per-exit search at (2000,20),(2000,40),(3000,25),(3000,100),(4000,15),
  (6000,15),(10000,20); validations: V1 full brute force (2^10/2^15), V2 direct re-eval,
  V3 independent mpmath first-entrance flow path. Result: class min = value at λ (= true μ)
  at EVERY exit, all positive; single-flip spectrum δ(q) ≥ 0 throughout.
- `m1_ramp.py` — one-scalar Ramp_f(X) = Σ_{d sf} f(d) T_X(d); exact Λ-identity check
  (Ramp_λ = Σ Λ(q) w_X(q), ≤1.4e-12); class min = λ-value at X = 600..10000.
- `m1_minimality.py` — multiplicative head + free tail block: freeing (K/2,K] re-breaks
  the functional at every tested point; H admits no tail relaxation.
- `m1_*.log` — canonical runs of the above (python3 + numpy + mpmath, float64 search,
  dps30 recheck).

Depends on `experiments/X-90004-gfep-certificates/g3_adv.py` (kernels + flow path), unchanged.
Consumer claim file: `claims/theorems/T-90008-multiplicative-reduction.md`.
