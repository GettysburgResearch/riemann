# Sources, overlap and reading boundary

## Pinned repository context

1. PR #953, `a93d382951f8fac7b0c28783061a7ddb99fcf0a4`,
   `standalone/2026-10-16-divisibility-covariance/THEOREMS.md`.
   Live PR metadata checked; the complete user-provided proof file was
   inspected. Its ideal-divisibility and prime-ideal-quotient estimates are
   not rebranded as the present rational-prime exchange theorem.
   https://github.com/GettysburgResearch/riemann/pull/953

2. PR #952, `3b7d2948840446c752bbf284f6f90f6592395a29`,
   `standalone/2026-10-16-critical-gaussian-energy/ENERGY_THEOREM.md`.
   Exact Gaussian pair kernel and finite-D absolute Fubini. Its content is
   available in the conversation and the attached archive. Formula (3) of
   THEOREMS.md is inherited, with the square completion rechecked.
   https://github.com/GettysburgResearch/riemann/pull/952

3. PR #954, `3241178607671c4dd979cefdad0670fd426194da`,
   `standalone/2026-10-16-norm-collision-energy/THEOREMS.md`.
   Live metadata and the fetched main statements and Sections 2--3 were read.
   The result already includes the full norm-collision block, its leading
   logarithm, and a long Mellin-average bound. Its tensor-square explanation
   of the exponent is credited. This packet reconstructs the quadratic
   complex continuation and moving-prime estimates directly; it does not
   claim a full audit of #954's remaining proofs or numerical checker.
   https://github.com/GettysburgResearch/riemann/pull/954

4. The repository AGENTS.md supplied in context has blob
   `c2181ad9ebf037614f3daa8957df640159f8d968`. The standalone-proposed scope and
   exact-source/review distinctions are retained. No integrated file changes.

A repository PR search for "prime-exchange" also found older #658, #653 and
#403. Their descriptions were inspected; these use different SHARP/network
and scattering objects. The term "prime exchange" itself is not claimed as
new, and their complete proofs were not reviewed or imported.

## Classical external inputs

- Terence Tao, *The prime number theorem in arithmetic progressions, and
  dueling conspiracies*, 24 September 2009. The explicit FIXED-modulus PNT
  statement was freshly checked. Only its specialization to 1 mod 3 is
  used; none of the heuristic arguments later in that article is a premise.
  https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/

- Terence Tao, *254A, Notes 4: Some sieve theory*, 21 January 2015.
  Classical Selberg upper-sieve and interval prime-counting background.
  THEOREMS.md supplies the actual weak O(H/log H) proof via its exact
  quadratic form; it does not import an unproved prime-pair assertion.
  https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/

- Classical ideal unique factorization, the splitting of rational primes in
  Q(omega), and zeta_K=zeta L(chi_-3). The elementary continuation formulas
  needed are written in THEOREMS.md (18). Only the positive residue at one
  and polynomial bounds on positive vertical strips are used. No zero-free
  region is required.

- Gaussian Mellin inversion, residue calculus, positive Euler comparison,
  partial summation, finite Mobius inversion, and Cauchy--Schwarz are
  classical. Their use is not a global novelty claim.

## What was NOT imported or assumed

No Dedekind quasi-RH theorem, theta moment theorem, GRH, short-interval PNT,
Hardy--Littlewood prime-pair conjecture, Mammen restoration estimate, native
critical energy bound, or inverse-zeta continuation through unknown poles.
No PDF or Lean source was needed or rebuilt in this pass. No claim is made
about the mathematical status of an uninspected revised external manuscript.

The contribution here is the source-specific moving rational-ratio
calculation, the full polynomial/power error at fixed m, the sharp thin-band
exchange law, and the uniform physical-phase absolute upper estimate, relative
to the inspected repository work. A global priority search has not been completed.
