# X-90004 — GFEP certificate artifacts (T-90003, Strike B prong B1)

- `cells.py`, `exactR.py` — cell calculus for R_X (Lemma 1; verified to 1e-27/1e-32).
- `certify.py` — 88 interval enclosures for the C_N sign structure (Lemma 2, dead zone N=5..40).
- `certified_band2_fixed.py` — the MAIN certified occupancy-minorant gate for Theorem 5, WITH the
  reviewer's epsilon repair (Q(2m'+1) >= 1/4 - 5/(4 X0), valid uniformly for p > X/10); worst band
  margin 0.8326. The unfixed `certified_band2.py` (scratchpad only) used 1/4 - 5/(8 X0), unsound
  for band children p just above X/10 - do not reuse it.
- `smallX.py` — exact finite gate X < 2000 (199,597 pairs, min sqrt(X)*Sigma = 2.790140).
- `sigma_struct.py` — top-determinism identity Sigma = pR(p) for 2n >= X (Theorem 4).
- `adv_b_review.py` — the adversarial reviewer's independent implementations (decomposition to 8e-17,
  Mellin fence checks, three-crossing confirmation).
- `b2_cfamily.py` — c-monotone moat / c-Gram numerics for L-90003 (note: check-(4) printout has an
  inverted comment; see L-90003 artifacts note).

Environment: python3 + numpy + mpmath. SHA256SUMS covers all scripts.
