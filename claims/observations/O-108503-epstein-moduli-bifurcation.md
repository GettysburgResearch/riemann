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
  a departure with |disc| jump 2 bracketed in x between 0.25 and 0.35.
  RESOLVED in the 2026-08-31 continuation run: with the window widened to
  t in (0.05, 35) the discrepancy PERSISTS (n_box - n_line = 2) and is
  localized to the subwindow t in (24, 30) — a genuine off-line pair, not
  a window-boundary artifact (epstein/e4_locus.json, path_A_resolution).
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
credited to the published literature above.

## E4 departure-locus sketch (2026-08-31 continuation run; e4_locus.json)

Four directions from z = i, coarse radii to 0.8 with bisection on the
first discrepant direction, t-window (0.05, 20):

- **rectangular direction (0,1): first off-line discrepancy at radius in
  (0.569, 0.575]** — refining path B's (1.5, 1.6) bracket to y* ~ 1.57;
- directions (1,0), (1,1)/sqrt2, (2,1)/sqrt5: NO discrepancy through
  r = 0.8 in this t-window (no claim beyond that window and radius).

Together with the path-A resolution (the (1,0) direction DOES depart by
r <= 0.35 once the window reaches t = 35): the measured departure locus
around the CM point is ANISOTROPIC AND HEIGHT-STRATIFIED — which zero
pair breaks first, and at what moduli distance, depends on both the
deformation direction and the height window: the rectangular direction
breaks first at low height (t ~ 11-16 pairs), the x-slide first at
t ~ 24-30. The geometric-invariant correlation still needs more events
than four directions provide and remains the lab's continuation target.

## C8 twelve-direction campaign (2026-08-31 pass 3; c8_run.py, c8_campaign.json)

Ten angles (0..90 deg) at window (0.05, 20), radii 0.2..0.8 with
bisection to 0.02 on the first dirty COARSE radius, plus two
height-stratified runs at (18, 32); every event NON_DIRECTED_HIGH_
PRECISION at dps 40, geometric invariants recorded per first-dirty
point. Findings, stated with the campaign's grid caveat below:

- **A departure ISLAND off the symmetry axes**: theta = 75 deg departs
  at radius (0.481, 0.500] (first-dirty point z ~ (0.129, 1.483)),
  while BOTH neighbors sampled at 60 and 82.5-88 deg are clean through
  r = 0.8 at the coarse radii — the low-height departure locus is
  lobed, with clean corridors between lobes, not star-shaped around
  the CM point.
- **Height stratification sharpened**: at window (18, 32) the x-slide
  ray theta = 0 (through y = 1.0 exactly) departs at radius
  (0.444, 0.463], while it is clean through 0.8 in the low window —
  the direction that is quiet at low height is the FIRST to break in
  the high window; theta = 45 stays clean in both.
- **GRID CAVEAT (a measured instance, not hypothetical)**: theta = 90
  reads "clean through r = 0.8" on the COARSE radii, yet E4's fine
  bisection certified a discrepancy at radius (0.569, 0.575] and path
  B's reentry brackets put the pair back on-line by y ~ 1.6-1.7: the
  dirty interval is NARROWER than the 0.15 coarse step and was
  straddled. Every C8 "clean" verdict therefore means "clean at the
  five coarse radii", nothing stronger; the two dirty verdicts are
  positive certificates at stated precision.
- **The island is an ARCHIPELAGO (island_probe.json, five follow-up
  calls)**: at radius 0.5 the dirty set is {75 deg, 80 deg} with a
  CLEAN angle 77.5 deg BETWEEN the two dirty ones (and clean 70,
  72.5, 82.5); radially the 75-deg spot is thin (dirty at r = 0.500,
  clean at 0.481 and 0.55). The off-line locus at this height is a
  fragmented, speckled shell confined to y ~ 1.47-1.50 — consistent
  with a single zero pair's off-line excursion sweeping a thin
  angularly-intermittent band, and a direct demonstration that ANY
  coarse grid systematically under-detects this locus (the grid
  caveat above, now measured twice).
- **Invariant correlation (2 events; suggestive only)**: both
  first-departure points lie hyperbolically CLOSE TO A CM POINT OTHER
  THAN the base point i — the 75-deg point at distance 0.101 from
  z = i sqrt 2 (systole 0.674, cusp height 1.483), the high-window
  theta-0 point at distance 0.149 from the hexagonal point rho
  (systole 1.0, cusp height 1.0); and the earlier x = 0 departure
  height y ~ 1.57 is itself at distance ~0.11 from i sqrt 2. Whether
  departures preferentially occur near OTHER arithmetic points of the
  moduli curve — "zeros leave the line where a different CM basin
  begins" — is deposited as the campaign's question, with these
  measurements as its first data and NO claim beyond them.

## Certification anchor (2026-08-31 continuation; T-108518)

The lab's first PROVED zero: `Z(s, 10i)` has a real zero in
`(81/100, 41/50)` off the critical line, certified by
directed-rounding interval arithmetic on the incomplete-gamma
representation with explicit tail bounds
(standalone/2026-08-31-epstein-wall-certificate/,
epstein/wall_certificate.py + .json). Phenomenon classical
(Bateman-Grosswald; CITATION-NEEDED); every other zero statement in
this claim remains NON_DIRECTED_HIGH_PRECISION. The complex
archipelago-point certification is deposited there as the next
target, with the template's missing ingredients listed.
```
