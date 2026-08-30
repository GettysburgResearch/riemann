# O-108503 — Epstein/Eisenstein lattice-moduli zero-bifurcation laboratory: first events

```text
Claim ID: O-108503
Status:   OBSERVATION; arithmetic class NON_DIRECTED_HIGH_PRECISION
          (dps=40, stated truncation bounds; mpmath 1.3.0); every zero
          statement means "numerically located to the stated precision";
          NO zero theorem is claimed
Created:  2026-08-30
Programme: #764 experiments 15-19 (parent-shadow + lattice-moduli zero
          bifurcation); lab: research/exploratory/2026-08-30-two-programme-
          pass/epstein/ (lab.py, run_experiments.py, ORACLES.md,
          ZERO_ATLAS.md, PARENT_SHADOW.md, DEPARTURE_PATHS.md, JSONs)
Positioning (mandatory, from the boundary audit): the collision-and-
          departure phenomenon for Epstein zeros in one-parameter families
          is PUBLISHED (Betermin-Samaj-Travenec, arXiv:2110.09368;
          Travenec-Samaj, arXiv:1909.07112; trajectories Arenstorf-Brewer
          1993; off-line zeros for class number > 1: Davenport-Heilbronn
          1936 era, Potter-Titchmarsh; real zeros Bateman-Grosswald,
          Stark; on-line proportions Ki, Y. Lee; Hejhal's studies;
          conditionally almost-all-on-line for linear combinations:
          Bombieri-Hejhal). This lab contributes ONLY: certification
          methodology, the two-parameter moduli framing, k-indexing of
          events, and the arithmetic-endpoint reading below.
RH status: unproved; unaddressed.
```

## What was measured (all to stated precision; replayable)

- **Oracles green**: theta modular transformation to 1e-46; incomplete-
  gamma engine vs direct lattice sum to ~18 digits; the z=i factorization
  `Z_i = 4 zeta(s) beta(s)` at two points to 20 digits; FE symmetry
  `Lambda_z(s) = Lambda_z(1-s)` to 1e-25 at 10 points; reality of
  `Lambda_z(1/2+it)`; the enumerator against exact r_2 counts (a typo in
  the coordinating spec's r_2 table was caught against the brute-force
  oracle and corrected).
- **Arithmetic-point atlas** (square z=i and hexagonal): every strip zero
  in t in (0,30) located and LABELLED by its classical factor (zeta vs
  L(chi_-4) / L(chi_-3)); box winding counts integer to ~1e-14; no
  off-line zeros at low height at either arithmetic point (consistent
  with GRH numerically; nothing more).
- **Parent-shadow identities verified**: `Z_z(s) = 2 zeta(2s) E_1(z,s)`
  (gcd=1 Eisenstein) to ~23 digits and the completed-form identity to
  ~44 digits at sample points; survival-ladder reading: L6 (FE) holds at
  EVERY z, L2 (Euler product) exactly on the arithmetic factorization
  locus.
- **Path A** (x-slide at y=1.02, x in [0, 0.35]): quiet through x = 0.25;
  a departure with |disc| jump 2 bracketed in x between 0.25 and 0.35
  (candidate-pair localization incomplete near the window edge — recorded
  honestly, not resolved).
- **Path B** (rectangular lattices, y in [1,2] at x=0 — from the CM point
  z=i to the CM point z=2i, i.e. the class-number-1 form x^2+4y^2):
  departure of TWO zero pairs bracketed at y in (1.5, 1.6) with colliding
  on-line pairs localized near t ~ 22-25.3; REENTRY events bracketed at
  y in (1.6, 1.7) (t ~ 24-26) and y in (1.7, 1.8) (t ~ 10.9-16.1); by
  y = 1.8 through y = 2.0 the strip count again matches the on-line count
  (17 = 17, then 20 = 20 at y = 2).

## Reading (conjecture-generating only)

Along the rectangular family connecting two arithmetic points, the
off-line excursion is CONFINED TO THE MIDDLE of the path: zeros leave the
line after y ~ 1.5, and all measured pairs return before the second CM
point at y = 2. Together with the parent-shadow ladder reading, this is a
measured instance of "the critical-line property as a function on moduli
space, peaked at the arithmetic points" — deposited as a phenomenon
description at stated precision, with the one-parameter phenomenon itself
credited to the published literature above. The two-parameter departure-
locus grid (E4) did not run (session limits) and is first in the lab's
continuation queue, together with resolving the path-A event's pair
localization and the geometric-invariant correlation, which needs more
events than two paths provide.
```
