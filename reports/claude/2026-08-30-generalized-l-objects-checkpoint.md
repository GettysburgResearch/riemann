# Programme #764 checkpoint — first pass (2026-08-30)

```text
Status:  first Gate-0 pass, claims band 1085xx (+ shared substrate)
Scope:   see M-108000; RH and GRH are unproved and unaddressed
Sibling: #763 checkpoint report (same date); bridge report ties the two
```

## What was proved (complete proofs, exact replays green)

1. **T-108500 — the pointwise-transform defect law** (standalone proof +
   `X-108500`, 7 exact check families): for generic degree-2 local data,
   `sum h_k^m T^k = N_m / det(1 - Sym^m T)` with exact minimal denominator,
   `deg N_m = m-1`, closed coefficient formula, the linear-coefficient law
   `c_1 = a^m - h_m`, and — the pass's favourite single result — the
   **self-duality functional equation of the defect**
   `N_m(T) = b^{m(m-1)/2} T^{m-1} N_m(1/(b^m T))`: the obstruction to
   functoriality is itself self-dual. The m=3 defect is irreducible over
   `Q(a,b)` — odd powers >= 3 exit the character ring entirely, while m=2
   is the classical Rankin-Selberg case (imported, used as oracle). Exact
   degeneration on the trace-zero locus recorded. Complete machine table
   for m = 2..6 (`matrix/defects.json`), each row formula-constructed,
   series-verified, self-duality-verified, and instantiation-checked.
2. **T-108501 — commutative collapse** (+ associative one-variable
   corollary; `X-108501`): every finite-dimensional commutative (and, for
   a single algebra variable, every associative) hypercomplex extension of
   zeta carries exactly jets of zeta on the spectrum — no new zero
   geometry. Delivers the collapse half of the issue's named
   quaternionic/multicomplex theorem target for series/functional-calculus
   definitions. Bicomplex instance credited to Rochon (2004).
3. **Lemma (L3 is cheap)**: every polynomial pointwise transform of every
   bounded-degree local system passes ladder level L3 with a p-uniform
   degree bound (Kronecker-criterion argument) — the ladder discriminates
   polynomial transforms only from L4/L6 upward.

## What was discovered exactly and deposited with witnesses

4. **O-108505 — rank structure of the square defect**: denominator
   `Sym^2` and numerator degree `C(d,2)` at ranks 2-4 (exact); the
   Gauss-sign exterior-square closed form
   `N = sum_j (-1)^{j(j-1)/2} e_j(Ext^2) T^j` proved at rank 2, exact at
   rank 3, **refuted at rank 4** with recorded witnesses; defect
   self-duality is a rank-2/self-dual phenomenon (exact rank-3
   counterexample). The corrected rank-4 law is an open exact target.
5. **O-108506 — angle-stratified purity** (bridge with #763): the m=3
   defect is integral and self-dual at every good prime but pure of
   weight 3 exactly when `a_p^2 < p`; witnesses from 11a1 (impure at p=2,
   pure at p=3; full stratification to p=97). Ladder cell L4 for this
   object is a DENSITY, not a bit — motivating measure-valued cells in a
   schema revision.

## Corrected under audit (deposited as firewalls, not hidden)

- The conjectured "effective defect iff global survival" is FALSE at the
  meromorphy level (`zeta(s)/zeta(2s)`); the honest object is the
  S1/S2/S3 trichotomy on top of Estermann/Dahlquist/Kurokawa theory
  (T-108500 failure ledger F-108500-1).
- Naive coefficientwise instantiation checking breaks on degeneration
  loci; cross-multiplied rational equality is the honest check
  (F-108500-2).

## Epstein-Eisenstein lattice-moduli laboratory (NON_DIRECTED_HIGH_PRECISION)

Oracle suite green to the stated precisions (theta transform 1e-46;
engine cross-check 1e-37; factorization at z=i against zeta*beta; FE
symmetry; line reality); zero atlas at the square and hexagonal points
labels every strip zero by its classical factor and finds no off-line
zeros at low height (consistent with GRH numerically, nothing more);
parent-shadow identities `Lambda_z = 2 zeta(2s) E_1(z,s)`-normalized
verified to 23-44 digits. Departure paths (O-108503; positioned strictly
under the published one-parameter literature — Betermin-Samaj-Travenec,
Travenec-Samaj, Arenstorf-Brewer): path A (x-slide, y=1.02) quiet through
x=0.25 with one bracketed departure in (0.25, 0.35); path B (rectangular
lattices from the CM point z=i to the CM point z=2i) shows the full
bifurcation story — two zero pairs depart at y in (1.5,1.6) with colliding
pairs localized near t ~ 22-25, reentries at y in (1.6,1.7) and (1.7,1.8),
and the line full again by y=1.8: the off-line excursion is confined to
the middle of the CM-to-CM path. The E4 departure-locus grid did not run
(session limits); it heads the lab's continuation queue.

## Survival matrix

As built (matrix/MATRIX.md; 12 of 13 world records, zero validation
problems; native_imports lost to session limits and deferred): the ladder
view separates cleanly — the counterfeits hold L1-L3 cheaply and fail or
open at L4-L6 exactly as designed, Davenport-Heilbronn holds L6 with a
fully exact Q(zeta_20) derivation while failing L1/L2 by exact witness,
the 2-deleted zeta does the converse, and the two theorem-worlds
(function-field elliptic, Ramanujan graphs) hold the entire ladder with
exact instance certificates.

## Ranked continuation queue (#764)

1. Corrected rank-4 square-defect law (witnesses deposited in O-108505);
   suggested mechanism: the `Ext^2 x Ext^2 -> det` self-pairing special to
   rank 4.
2. S1/S2/S3 stratum classification of the defect Euler products
   `prod_p N_m(p^{-s})` for m <= 5 over a fixed GL(2) source, by applying
   Estermann/Dahlquist/Kurokawa to the exact defect tables; natural-
   boundary question for m = 3 as the sharpest case.
3. Epstein departure-locus refinement: denser direction grid, second and
   third zero pairs, and the geometric-invariant correlation test with
   enough events to be meaningful.
4. Schema revision: measure-valued ladder cells (angle-stratified purity
   as the model phenomenon).
5. General-m, general-rank defect law: the coefficient formula holds at
   all ranks (same proof); find the rank-d closed forms and their
   representation-theoretic meaning.
6. Escape routes from T-108501: genuinely several-noncommuting-variable
   zeta objects or free functional calculi; construct one with provably
   non-jet zero geometry or extend the collapse.
7. Beurling system with a genuine functional equation: existence/
   impossibility (shared with #763; Hilberdink-Lapidus anchor).

## Continuation pass (2026-08-31)

The three ambitious targets of the second pass landed as theorems:

1. **T-108507 — the cube-defect bridge** (proved + `X-108507`, 5 exact
   checks): `N_3(T) = det(1 + b A_2 T)` where `A_2` is the TRACE-DOUBLED
   deformation (trace `2a`, determinant kept) — the obstruction to cubing
   is the local L-datum of another point of the deformation space. The
   splitting field of the defect is `A_2`'s Satake field (explaining the
   character-ring exit), the purity stratification is `A_2`'s
   temperedness stratification (Ramanujan violated exactly on
   `{a_p^2 > p}`, Sato-Tate density `2/3 - sqrt3/(2pi) = 0.391`), and
   globally `sum' a_n^3 = L(Sym^3) x D(A_2-twisted)` — verified exactly
   on all good-support `n <= 300` for 11a1. Natural-boundary corollary
   stated CONDITIONAL on the pinned Estermann/Dahlquist/Kurokawa criteria
   (Kurokawa, Proc. LMS 1986 I-II). Structural reading: **deformations
   obstruct each other** — three previously separate exact facts
   (self-duality, exit, stratified purity) are one fact seen three ways.
2. **T-108508 — square-defect closed forms proved for ranks <= 5**
   (symbolic-expansion proofs): rank 4 is the Gauss-sign polynomial plus
   `2 e4 h2 T^3 - 2 e4^2 e2 T^5` (the perfect-matching/`det`-pairing
   layer); the full rank-5 correction list is proved, with the
   `h`-polynomial layer pattern (`corr_3 = 2(e4 h2 - e5 h1)`,
   `corr_4 = -2 e5 h3`) and the top-sign law
   `(-1)^{(d-1)(d-2)/2} det^{d-1}` for `d <= 5`. General rank OPEN with
   proved data points — O-108505's open problem resolved at the ranks it
   posed.
3. **Epstein lab completion**: the pending path-A event RESOLVED as a
   genuine off-line pair (persists with window headroom to t=35,
   localized to t in (24,30) at x=0.35, y=1.02); E4 four-direction
   departure-locus grid run (see epstein/e4_locus.json). All seven
   ledgered adversarial minors applied (ledger updated in place).
