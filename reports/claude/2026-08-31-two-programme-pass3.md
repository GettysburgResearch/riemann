# Pass 3 report — computational campaigns C1–C8 and the theorems they produced

```text
Date: 2026-08-31
Programmes: #763 (Riemann Structures), #764 (Generalized L-Objects)
Branch/PR: claude/riemann-repo-review-m7dk1x / PR #781
Design: computation-first (campaigns C1-C8 producing machine-readable
        atlases for others to mine), with the standing conversion rule:
        any pattern surviving a held-out test gets a same-pass proof
        attempt. Five conversions succeeded (T-108509, T-108510,
        T-108513, T-108514 — the infinite expansion-side family — and
        T-108515, the Segre bridge identifying the defect with the
        K-polynomial of the Segre embedding of (P^1)^m), and multiple
        same-pass conjectures were refuted by
        their own tests and corrected before commit (the Hadamard
        min-law, the D_m positivity guess, the girth-profile swap,
        the unconditional even-factor simplicity; see the honesty
        trail).
RH status: RH and GRH are unproved; nothing in this pass addresses
        them. Every artifact carries rh_established: false.
```

## New claims of this pass

| Claim | Kind | One line |
|---|---|---|
| T-108509 | THEOREM | Deformation spectrum: every d=2 power defect = product of floor((m-1)/2) self-dual rank-2 L-data; spectrum polynomial M_m; tower invariants D_m = disc_z M_m |
| T-108510 | THEOREM | Codimension law: defect numerator degree deficit = backward vanishing order; all-d top-coefficient sign law; product/shift/section laws |
| L-108511 | LEMMA | Trace-scaling line crosses the survival trichotomy: Z_0 = zeta(4s-2)/zeta(2s-1), Z_{-1} = L(Sym^2,2s)/(zeta(2s-1)L(f,s)), exact |
| O-108006 | OBSERVATION | Graph purity telescope: 605-graph certified corpus, negative-end breach law (37/37 through n=14), certified walk bifurcations |
| O-108512 | OBSERVATION (half-converted) | Torsion resonance entry law m = 2 ord(alpha^2)+1: ten points, ten exact matches, six held-out |
| T-108513 | THEOREM | Resonance threshold: class crowding forces collisions from m = 2R+1 (all m), collision at z = a; converse proved for all torsion points, m <= 17 |
| T-108514 | THEOREM | GP(n,2) positive-end-only for ALL n >= 24 (exact threshold; infinite expansion-side family; three pieces, all adversarially verified sound) |
| T-108515 | THEOREM | Segre bridge: N_m = equivariant K-polynomial cofactor of the Segre embedding of (P^1)^m; m=3 Betti table exact; defect FE = Gorenstein duality of the cube; N_m(2,1) = Eulerian polynomial |

Pass-2 claims T-108507 and T-108508 received addenda: the spectrum
theorem closes T-108507's tower question; the codimension law proves
T-108508's top-coefficient conjecture for all d.

## Campaign outcomes (the data others can mine)

**C1+C3 — defect atlas** (matrix/c1_defect_atlas.py + json, 21s):
symbolic numerators and spectrum polynomials m = 2..9 (extended to 11),
tower discriminants factored, 192-point splitting census (m=5: splits
iff D_5 square, 12/12), the (m,d) grid (10 cells, codimension law
everywhere, denominators full), transform defects (Rankin control
confirmed symbolically; mixed cube codim 2; shift codim 1; section
codim 1), scaled self-duality confirmed at d=2 and refuted for d>=3.

**C2 — deformation phase diagram** (matrix/c2_phase_diagram.py + json):
exact a_p table for 11a1 to 1e5 (9591 good primes, Hasse-checked);
temperedness phase transition exactly at |t| = 1 with the Sato-Tate
closed form D(t) = (2 th* - sin 2 th*)/pi matching empirically
(0.3888 vs 0.3910 at t=2); the two strata identities verified exactly
on all good-support n <= 20000; rigidity: integral+tempered locus of
the line = {0, +-1}.

**C4 — boundary telescope** (matrix/c4_boundary_telescope.py + json):
zero constellation of the bridge product D(s): tempered primes place
local zeros EXACTLY on Re s = 3/2, untempered band shrinks like
1/log p (max 1.6404 beyond p = 1e4) — correcting an earlier working
note (5/2 is the absolute-convergence edge, not the predicted
accumulation line); root-angle dichotomy (deformed-ST match L1 = 0.04
over 20 bins) deposited as the Estermann/Kurokawa criterion input,
with the honest control that dense local zeros alone prove nothing
(the t=0 quotient has them and is meromorphic).

**C5 — graph telescope** (graphs/telescope.py + json): 134-graph exact
atlas (Hamiltonian cubic exhaustive n <= 10 with brute isomorphism;
n = 12 spectral+invariant dedup — class counts 1,2,5,17,80 match the
published census, CITATION-NEEDED on the reference); unbiased 2-swap
walks with one Sturm certificate per step: 6 + 2 certified
departure/reentry events from GP(12,1)/GP(12,5).

**C6 — spectroscopy** (graphs/spectroscopy.py + json): every
non-Ramanujan graph breaches at the NEGATIVE spectral end; breach
minimal polynomials extracted (GP(9,1): x^3+3x^2-1 — the shifted
cyclotomic cubic of 2cos(2pi/9)).

**C7 — census extension** (graphs/census14.py + json): n = 14: 471
classes, 31 non-Ramanujan, all negative-end. Law: 37/37 through n=14.

**C8 — Epstein direction campaign** (epstein/c8_run.py +
c8_campaign.json; 12 runs, ~2h at dps 40): a departure ISLAND at
theta = 75 deg (radius (0.481, 0.500], point ~ (0.129, 1.483)) with
clean corridors at 60 and 82.5-88 deg — the low-height locus is lobed,
not star-shaped; the high window (18, 32) flips the ordering (the
x-slide departs at (0.444, 0.463] there while clean below); a measured
grid caveat (theta = 90 coarse-clean while E4's fine bisection is
dirty at (0.569, 0.575] — narrow dirty intervals can be straddled);
and the first invariant correlation: BOTH first-departure points lie
hyperbolically close to a CM point other than the base (0.101 from
i sqrt 2; 0.149 from rho) — two events, deposited as a question with
data, not a law. Full details in the O-108503 C8 addendum.

**Torsion resonance follow-up** (matrix/spectrum_collision_loci.json,
m10_m11_spectrum.json, m12_m13_spectrum.json, m14_m15_spectrum.json,
torsion_field_probe.py + json): the collision loci of the deformation
spectrum on the self-dual slice acquire the minimal polynomial of the
torsion point with R = ord(alpha^2) at EXACTLY m = 2R + 1. Definitive
exact table via the number-field engine (the whole defect computation
run in Q[a]/(C) at b = 1; each cell seconds): ten torsion points
(R = 3, 4, 5, 5, 6, 9, 9, 10, 11, 13), ten exact matches with 2R + 1
(entries 7, 9, 11, 11, 13, 19, 19, 21, 23, 27), complete absence
certified at every earlier m, monotone persistence after entry; six of
the ten entries were held-out predictions recorded before their runs.
All torsion factors carry even multiplicity; the {0, +-1}-slice
collapse lemma (proved) explains the a and (a -+ 1) dominance. The
threshold mechanism was then FOUND AND PROVED (T-108513, standalone/
2026-08-31-torsion-resonance-threshold/): class crowding of the Sym^m
weight monomials mod the torsion order forces repeated defect roots
from m = 2R on; at m = 2R the triple lands on the boundary class
(z = 2 — no collision, deriving the universal m = 2R non-entry) and
at m = 2R+1 on c = +-1, forcing two spectrum points to collide AT THE
ORIGINAL TRACE z = a ((z-a)^2 | M_{2R+1}, machine-confirmed 10/10);
the a = 0 m = 6 gap and its m = 8 return are derived by the same
counting. The CONVERSE was then ALSO PROVED for all m <= 15 for every
torsion point of every order (monic sieve: torsion minimal polynomials
are monic-integral, and the exact factorizations of disc_z M_m(a,1)
show the non-torsion factor has non-unit leading coefficient at every
m in range — disc_slice_factor_lcs.json), making the entry law a
complete two-sided theorem in that range; the m >= 16 converse is
reduced to a checkable normal form per m.

**Segre bridge (Lane 1 of the six-hour continuation; T-108515,
standalone/2026-08-31-segre-defect-bridge/)**: the powered-coefficient
series sum h_r^m T^r is recognized as the equivariant Hilbert series
of the Segre ring of (P^1)^m, and the defect numerator N_m is PROVED
(all m) to be the Segre variety's equivariant K-polynomial divided by
explicit ballot-multiplicity excess factors
det(1 - Sym^{m-2k}(A) b^k T)^{C(m,k)-C(m,k-1)}. At m = 3 the full
equivariant Betti table of the 2x2x2 Segre was computed exactly
(stdlib Fraction Koszul homology, matrix/segre3_betti.py): C;
3 det^2 Sym^2 @ 2; 2 det^3 Sym^3 + 4 det^4 Sym^1 @ 3; 3 det^5 Sym^2
@ 4; det^9 @ 6 — det^9-self-dual, reassembling to
K_3 = N_3 (1 - abT + b^3 T^2)^2. The defect functional equation
T-108500(3) received a second, geometric proof: R_m is the normal
toric ring of the unit m-cube (explicit saturation), [-1,1]^m is
reflexive with omega = b^m R(-2), and Stanley reciprocity (imported,
labelled) forces the FE — the self-duality of the obstruction IS
Gorenstein duality of the cube. Two corollaries: N_m(2,1) = the
Eulerian polynomial A_m (the defect is a GL_2-equivariant Eulerian
deformation, its FE deforms Eulerian palindromy), and the held-out
rank-3 test K_{2,3} = G_3 det(1 - Lambda^2 A T) — predicted by the
bridge, then machine-verified against T-108508 — depositing the
Lascoux-strand route to the general-rank square-defect law. Replay:
experiments/X-108515-segre-bridge (integer-exact through actual
Kronecker/symmetric-power matrices and integral Faddeev-LeVerrier,
m = 2..6, all green incl. -O). This realizes Priority 1 of the
external programme review, proved independently of its sketch.

**Two-parameter deformation plane (Lane 2; L-108516)**: L-108511's
trace-scaling line extends to the full plane
Z_{t,u} = prod (1 - t a_p p^{-s} + u p^{1-2s})^{-1}. Proved
unconditionally: every coefficient b_n(t,u) is weighted-homogeneous
of degree Omega(n) (wt t = 1, wt u = 2) — so the upper half-plane
FIBERS over the line by root-scaling, t -> -t is the Liouville twist,
and the parabola u = t^2 is the Omega-graded flow through L(f); the
t = 0 axis is Dahlquist's family with
Z_{0,u} = zeta_{u^2}(4s-2)/zeta_u(2s-1) (and the collapse
Z_{0,-1} = zeta(2s-1) exactly); the purity wedge is
{u >= t^2} union {t = 0} (inside: Hasse, unconditional; outside:
p = 2 witnesses); the integrality locus is exactly Z^2. RIGIDITY
THEOREM (unconditional): the integral + weight-1-pure points of the
whole plane are EXACTLY four classical points — (1,1) = L(f),
(-1,1) = the Liouville-twist quotient, (0,1) = zeta(4s-2)/zeta(2s-1),
(0,-1) = zeta(2s-1). Two parameters buy no new arithmetic points; and
by weighted homogeneity the (a,b)-resonance atlas is universal for
the plane. Machine: matrix/tu_atlas.py + tu_atlas.json (stdlib-exact,
n <= 20000 coefficientwise in Z[t,u], 9591-prime wedge scan, ALL OK).

**Two-invariant phase diagram (Lane 3; O-108517)**: over a 45-graph
exact corpus (capped-ladder families k = 2..6, all GP(n,k) n <= 11,
Moebius ladders; exhaustive-subset Cheeger constants h, exhaustive
max-cut frustration indices f, Sturm verdicts with adaptive cuts),
the two structural invariants organize the breach sides exactly:
positive-end breach <=> h <= 1/4 (16/16 vs 0/29, empty gap
(1/4, 1/3)); among all non-Ramanujan rows the FIRST breach side is
predicted by f = 2 (negative entry, all five NEG-only rows) vs f = 4
(positive entry, all eight POS rows); the positive families go
both-end at CONSTANT f = 4 as the corridor dilutes frustration
density (f/m: 2/15 -> 2/33). Honest calibration: the Cheeger
inequality would prove a breach only below h ~ 0.0858, three times
smaller than the observed threshold — the dichotomy is a corpus
pattern beyond current inequalities, and "does positive-end-only
force f >= 3?" is deposited as the sharpest open question.

**Certified Epstein wall point (Lane 4; T-108518)**: the lab's first
PROVED off-critical-line zero — Z(s, 10i) has a real zero in
(81/100, 41/50) (FE partner in (9/50, 19/100)). Method: self-dual
theta -> incomplete-gamma representation (derived inline; verified
against the independent Chowla-Selberg formula to ~1e-40 at two
points), then directed-rounding interval evaluation (mpmath.iv,
dps 120) at rational sigma with three proved truncation bounds
(Gamma(a,x) <= x^{a-1}e^{-x} for the term bound; a theta-geometric
lattice-tail bound; a ratio-1/2 series truncation) and
reflection-identity checks on the gamma enclosures. Certified margins
of order 1 against interval widths ~5e-18. Honesty: the phenomenon is
classical (Bateman-Grosswald real zeros; CITATION-NEEDED), Epstein
zetas are not zeta, and nothing here bears on RH — the contribution
is the proof-grade anchor for the lab's rectangular bifurcation story
and the certification template; the complex archipelago point is
deposited as the next target with its missing ingredients listed.

**Lane 3 completions (O-108517 addendum + L-108520)**: (i) exhaustive
n = 16 rescan: the three minimal positive-end-only spectra have
UNIQUE graph realizations (3 graphs in 65,346 canonicals; cospectral
caveat closed), all with f = 4 — the f >= 3 necessity holds
exhaustively at minimal order; (ii) the 6-head x 6-cap atlas (50
exact rows) answers the deposited non-diamond-head question: windows
occur for exactly the window-type x window-type block pairs, the
crossing block kills them, the f-dichotomy extends (f = 4 / 2 / 0),
and the three witnesses re-decompose as 6/6 ladders with a common
s709 block; (iii) WINDOW FINITENESS IS PROVED (L-108520): an induced
2x15 ladder forces lambda_2 > 2 sqrt 2 AND lambda_min < -2 sqrt 2
(Dirichlet ladder modes + Courant-Fischer; threshold settled by
50 > 49), so every capped-ladder family leaves positive-only by
corridor length 15 — the transient-window vs permanent-regime
dichotomy of O-108006/T-108514 is now proved at both poles.

**The alternant closed form (Lane 6; T-108522)**: the divided-
difference/partial-fraction identity sum_r h_r^m T^r = (m-1)-fold
alternant of geometric products yields EXPLICIT closed forms for
every defect numerator N_{m,d} — in particular the general-rank
square defect

N_{2,d} = sum_j x_j^{d-1} prod_{a!=j}(1-x_a^2 T)
prod_{a<b!=j}(1-x_a x_b T)/prod_{a!=j}(x_j-x_a),

CLOSING T-108508's open general-d problem (symbolically equal to the
proved d = 3, 4 forms; verified at exact points for d = 5, 6, 7 —
ranks with no previously known closed form), and re-deriving
T-108510's top-coefficient sign law in three lines. The proof is
three elementary lemmas (bialternant expansion; partial fractions;
multiplication bookkeeping); boundary check: the literature itself
states no general closed Hadamard-numerator form is known (Kar,
RHUMJ 23 (2023)), so the alternant is claimed new-in-context with
classical technique. STABLE LAYER THEOREMS followed the same day:
each T^j-correction is a weight-2j symmetric function determined at
d = 2j, so single symbolic computations prove for ALL ranks that
corr_3 = 2 sum_{i>=4}(-1)^i e_i h_{6-i} (T-108508's guess),
corr_4 = 2 sum_{i>=5}(-1)^i e_i h_{8-i} (new), and the
eleven-monomial corr_5 — where the linear law TERMINATES (first
layer empty at j = 5; purely second-stratum, collapsing at d = 5 to
T-108508's quadratic coefficient). MULTILINEAR EXTENSION (Theorem
C): closed-form defect numerators for naive TRIPLE products
sum a_n b_n c_n n^{-s} against the automorphic triple-product
denominator, at every rank tuple, with the degree law deg N_{ABC} =
dA dB dC - max(d) — the naive n - dA guess was refuted by the
machine at shape (2,2,3) and the corrected law's mechanism (the
bialternant at negative index) came from that failure; the pair case
re-derives Rankin-Selberg exactness in one line. Ground truth added: the exact equivariant Betti table of
P^2 x P^2 ((1,9,16,9,1) at twists 0,2,3,4,6, per-weight characters;
matrix/segre_d3m2_betti.py). Replays: matrix/alternant_defect.py
(sympy+exact) and X-108522 (stdlib), all green.

**Frustration bound (L-108521)**: lambda_min <= -3 + 4f/n for every
cubic graph (one-paragraph Rayleigh proof via the bipartition vector
of a frustration-optimal spanning subgraph). Corollaries: f <
n(3-2sqrt2)/4 forces a negative-end breach (f = 2 suffices at every
n >= 47), and positive-end-only families need LINEARLY growing
frustration. With L-108520 (corridor forcing), both poles of the
O-108517 two-invariant diagram now have proved mechanisms; the open
middle is the h <= 1/4 expansion dichotomy.

**Certified COMPLEX wall point (Lane 4 stage 2; T-108519)**: rigorous
winding number 1 (interval [0.97335, 1.02666], 3696 adaptive contour
steps, every step passing the exact-step lemma's conditions) proves
Z_Q has exactly one zero in [83/100, 99/100] x [1221/100, 1238/100]
at the exact-rationalized theta80 dirty probe of the C8 archipelago
— the repo's first proof-grade COMPLEX Epstein zero (Re rho >= 0.83;
a certified off-line quadruple with conjugate/FE partners). New
machinery: complex-rectangle intervals over mpmath.iv, Spouge Gamma
with explicit error, two-branch incomplete gamma, and the
rotated-contour K-Bessel bound |K_{a+i mu}(x)| <= e^{-mu theta}
K_a(x cos theta) that makes the Lipschitz sup bound realistic at
t ~ 12. Honesty: a first run walked all its steps soundly but left
the winding unpinned (per-sample tail boxes accumulated over ~3750
angle increments); the bound-budgeting lesson — size enclosure
widths against the SUM, not the step — is recorded in the standalone
status block, and the fixed run (tail 5.1e-14) pinned the integer.

## Process notes (honesty trail)

- The X-108510 replay's mixed-triple test was written expecting the
  Hadamard min-law and REFUTED it (nu = 4 = max, not 2 = min); the
  proof document was corrected before commit and both files record the
  history. The corrected max-law is what the reciprocity argument
  proves.
- The C4 telescope's angle-histogram CDF had a direction bug caught by
  its own L1 = 2.0 sanity signal; fixed (L1 = 0.04).
- The C5 brute-isomorphism route at n = 12 was infeasible (12! loops);
  replaced by spectral+invariant dedup with the cospectral-merge caveat
  stated in every artifact; the external count match validates n = 12.
- A positivity conjecture for D_m on the tempered slice was tested and
  REFUTED within minutes (D_m vanishes at torsion points — which
  became O-108512's discovery). Failed guesses are recorded, not
  hidden.

## Where a reader should start

1. standalone/2026-08-31-deformation-spectrum/PROOF.md — the pass's
   central theorem; then matrix/spectrum_collision_loci.json for what
   it opens up.
2. standalone/2026-08-31-defect-codimension-law/PROOF.md — one
   mechanism explaining every defect degree in both programmes.
3. claims/lemmas/L-108511-trace-scaling-strata.md — one line through
   deformation space crossing the whole survival trichotomy with exact
   identities.
4. graphs/spectroscopy.json + claims/observations/O-108006 — the
   discrete moduli laboratory and the negative-end law.
5. standalone/2026-08-31-segre-defect-bridge/PROOF.md — the defect's
   second life as geometry: Segre K-polynomial, cube Gorenstein
   duality, Eulerian deformation.
```
