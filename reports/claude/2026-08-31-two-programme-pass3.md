# Pass 3 report — computational campaigns C1–C8 and the theorems they produced

```text
Date: 2026-08-31
Programmes: #763 (Riemann Structures), #764 (Generalized L-Objects)
Branch/PR: claude/riemann-repo-review-m7dk1x / PR #781
Design: computation-first (campaigns C1-C8 producing machine-readable
        atlases for others to mine), with the standing conversion rule:
        any pattern surviving a held-out test gets a same-pass proof
        attempt. Two conversions succeeded (T-108509, T-108510), one
        prediction was confirmed held-out (O-108512), one conjecture of
        this pass was refuted by its own test and corrected before
        commit (the Hadamard min-law; see T-108510).
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
| O-108512 | OBSERVATION | Torsion resonance: order-N collision loci of the spectrum enter at m = N+1; order-10 confirmed held-out at m=11 |

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

**C8 — Epstein direction campaign** (epstein/c8_run.py, RUNNING at
report time; c8_campaign.json incremental): 12 directions from z = i
with bisection and geometric invariants (hyperbolic CM distance,
systole, cusp height) at each first departure; first four directions
(0-45 deg) clean through r = 0.8 in the (0.05, 20) window, consistent
with E4's anisotropy. Final harvest lands in this pass's last commit.

**Torsion resonance follow-up** (matrix/spectrum_collision_loci.json,
m10_m11_spectrum.json): the collision loci of the deformation spectrum
on the self-dual slice contain the order-N torsion minimal polynomials
from m = N+1 (orders 4, 6, 8 observed; order 10 PREDICTED then
confirmed at m = 11 by fresh computation; order 12 at m = 13 is the
posed next test); all torsion factors have even multiplicity.

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
```
