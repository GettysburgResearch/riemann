# T-108000 — The witnessed axiom-separation table for zeta worlds

```text
Claim ID: T-108000
Status:   PROVED at the stated finite scope: a theorem-of-the-instances
          aggregating exact certificates of the 12-world corpus; imported
          dependence theorems cited for the provably-empty cells; nothing
          global about zeta is claimed
Created:  2026-08-30
Programme: #763 (Riemann Structures), experiment 1 (cross-world matrix)
          + mode C (synthetic worlds); table artifact:
          research/exploratory/2026-08-30-two-programme-pass/matrix/MATRIX.md
Depends on: the world records worlds/*.json (each with per-cell witnesses
          and build scripts), core/worlds.py validation (12/12 clean)
RH status: RH and GRH are unproved; this table proves nothing about them.
```

## Statement

Over the built corpus (zeta, Dirichlet mod 5, elliptic 11a, function-field
elliptic/F5, Ihara Ramanujan + non-Ramanujan, Beurling, Davenport-
Heilbronn, the Epstein pair, and three engineered counterfeits), the
mechanism axes {EULER_PRODUCT, DUALITY_FE, TRACE_FORMULA,
POSITIVITY_PURITY, TENSOR_OPS, FAMILY} versus the critical-line conclusion
separate as follows, with three cell types per the boundary audit:

**WITNESSED separations (exact certificates in the corpus):**

1. `{Euler product, FE, trace formula}` does NOT force the critical line:
   the non-Ramanujan cubic graphs (prism family), with the Euler product
   exact over primitive geodesics, the functional equation proved as
   coefficient identities, the Bass determinant identity proved IN FULL
   from exact non-backtracking traces — and the line FALSE by exact Sturm
   certificates (lambda^2 in (8,9)); refined witness: self-adjointness
   supplies spectrum REALNESS but not the purity gap — two distinct
   mechanisms.
2. `{Euler product}` does not force `{FE}`: the 2-deleted zeta, fully
   proved (exact zero s0 = 2 pi i / log 2 whose reflection is excluded by
   the classical nonvanishing of zeta on Re s = 1); Beurling rows imported
   alongside.
3. `{FE}` does not force `{Euler product}` (nor the line): Davenport-
   Heilbronn, with the self-duality derivation done exactly in Q(zeta_20)
   and the non-multiplicativity witness 1 + kappa^2 of norm 6400; off-line
   zeros imported (density-zero caveat recorded: off-line zeros are rare —
   Bombieri-Hejhal).
4. Archimedean data is not free: the wrong-gamma completion is proved
   non-entire (pole transport: the mismatched gamma's poles at odd
   negative integers survive because the even character's trivial zeros
   sit at the even ones) and admits no reflection functional equation.
5. Local purity does not supply global structure: the seeded completely
   multiplicative counterfeit has weight-0 pure degree-1 local factors and
   an exhaustive exact certificate that it is no real character of
   conductor <= 50; everything global is honestly OPEN.
6. In this corpus the co-occurrence `critical line THEOREM <=>
   POSITIVITY_PURITY HOLDS` is EXACT and machine-derived
   (matrix/MATRIX.md cross-tabulation): the THEOREM worlds are precisely
   the two with an identified purity mechanism (Frobenius eigenvalue
   purity; Ramanujan spectral gap), and the purity-FAILS world has line
   FALSE. This is the organizing observation of #763's first pass — a
   property of the corpus, not evidence about zeta.

**PROVABLY-EMPTY separations (imported dependence theorems; cited, not
reproved):** Hamburger's uniqueness theorem (degree 1 with zeta's FE and
growth: no separating world exists); the Kaczorowski-Perelli degree
classification (no exotic low-degree Selberg-class worlds); Weil's
converse theorem (FE for sufficiently many twists at GL(2) forces
automorphy — L6+L7-all-twists cannot be separated from L8 at that scope).
Attributions per the boundary audit file.

**OPEN cells (the discovery frontier):** a number-field-ontology world
with the full package minus purity; a Beurling system with a genuine
functional equation (Hilberdink-Lapidus anchor); measure-valued cells
(O-108506). These are questions, not claims.

## Novelty position

Every individual separation is folklore or classical and is cited as such
(Terras's zeta dictionary is the direct ancestor of the comparative view;
Stark-Terras for the graph formulation; Davenport-Heilbronn 1936; the
audit file carries the full list). The pass's artifact is the TABLE:
one machine-validated schema, an exact witness attached to every populated
cell, dependence theorems attached to every empty cell, and build scripts
that regenerate every certificate. Deposited as instances and witnesses,
not as a general mechanism theorem — the mechanism theorem ("purity =>
line" in a defined class containing the corpus) is the ranked next target.

## Caveats

- native_imports was completed in the 2026-08-31 continuation pass
  (corpus 13/13; see O-108004 for the runs and their pinned provenance);
  this caveat is retained as the record of the pass-1 gap.
- The Epstein pair's generic member and the DH world import their
  known-zero locations; only the finite algebraic layers are proved here.
```
