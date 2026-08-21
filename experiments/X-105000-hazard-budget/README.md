# X-105000 — machine verification of the hazard-budget packet

Run: `python3 verify.py` (deps: sympy, mpmath; ~2 min). Expected final line:
`ALL CHECKS PASSED`. Results land in `results/results.json`.

What is verified (fixture list mirrored in `M-105000 §3`):

* S1 symbolic derivative `d/dw [T(w)/T(pw)] = 6(√p−1)/(√w · T(pw)²)` —
  the monotone-ratio engine behind the coupling cap (`L-105001 §1`) and
  branch submultiplicativity (`L-105002`).
* S2 exact deficit identity `product − block = r_p r_q R_p (R_q − R_{pq|p})`.
* S3 corpse reproduction: 70-digit directed enclosure of
  `δ₆₇ = r(1−2r)` matching `R-97600`'s deposited interval; the
  `R-99440.5` leading coefficient `4C_j(1−r)/p·√Y`; exactness of the causal
  identity (`s+λ=1`, `−λr+α=0`).
* S4 thresholds: loss fraction `1−2r > 3/4` iff `p > 64`; deficit positive
  iff `p ≥ 5`; small-prime overshoot constant `5/3 − 2^{−1/2} − 3^{−1/2}`.
* S5 exchange-rate universality: `q_T` closed form `≥ √p`; √-growth of the
  rows; numeric `q_T, q_2, q_3 ≈ √p` bands.
* S6 normalization invariance of the price under the `R-99820` cocycle.
* S7 budget inequality (`T-105000` A.1) on 200 random admissible block
  families (never violated).
* S8 directed bracket of the `Π_T` unit crossing: `Π_T(578906) < 1 <
  Π_T(584375)`.
* S9 weight-bound identity `√(Z/Y)·T(Y) − T(Z) = 3(1 − √(Z/Y))`;
  `Π_G ≤ Σ 1/p`; monotone growth of `Π_G`.
* S10 knot identifiability (Lemma 0 of `M-105000`): exact 5×5 symbolic solve.

What is NOT verified here: any statement about zeta zeros; anything about
the truth of RH; anything beyond the admissible class of `T-105000 §2`.
