# Validation and review boundary

Status: locally tested proposed mathematics; NOT PUSHED. The proof and checker
have the same author. No independent human referee, separately commissioned
agent, Lean build, comparator, transitive axiom audit, repository-wide validator
or remote CI result is claimed. The finite tests below do not certify the
imported sieve, AFE or infinite analytic conclusions.

## New execution

`python verify.py` and `python -O verify.py` produce byte-identical CHECKS.json.
The report contains **1,507 explicit predicates**, including setup and repeated
exponent guards, not 1,507 independent analytic cases.

- 96 COMPLETE local residue-sum cases. At residue norm 13, all declared
  (t,k,J) cases with t+k<=4 are enumerated (50 cases). At norm 37 the cap
  is 2 (16 cases). At norm 25 it is 3 (30 cases), in the unramified ring
  Z_5[sqrt(2)]. Every residue allowed by each specified modulus/congruence
  is included. These are local rings, not a complete global field census.
- Exact arithmetic in Z[zeta_6,zeta_(p^n)] is represented by two integer
  coefficients in the omega basis and reduction by Phi_(p^n). No floating
  roots, approximate equality or OCR is used. Full Gauss products at all
  five nontrivial character powers and the unit/nonunit distinction pass.
- 468 rational formal-series coefficient comparisons through v^12 check
  the original supported shell sum against all five new rational factors
  and the old unramified expression. The rational Gauss-symbol parameters
  are ALGEBRA fixtures, not alleged values of Gauss sums. The separate
  direct residue sums check the primitive C_(t,k) identities.
- 252 actual-conductor dyad monomials check that the dual AFE factor
  uses Q0^(2-4lambda), including Q0 much shorter than U. All fixed detector
  exponents, both endpoints of both second-type monomials and the exact
  1/920 improvement are checked rationally.
- 380 weighted correction-moment exponent guards and explicit new-domain
  points are checked. These rational fixtures do not substitute for the
  real-parameter inequalities proved in RAMIFIED_FACTORS Section 4.

`run_mutations.py` writes eight separate corrupted copies of the actual
checker source in temporary directories and executes each with `python -O`.
All fail at their intended predicates. The changes erase a nonunit zero,
omit the j=5 boundary, discard valuation support, erase the ramified unit
phase, retain the old B exponent, retain the old mollifier weights, omit the
dual conductor factor, or change the exceptional-count Holder exponent.
MUTATIONS.json records the actual errors and exit codes.

## Parent replay and source identities

The delivered #966 packet was expanded locally. Its original manifest passed,
and its COMPLETE verifier was rerun under normal and optimized Python.
Both outputs agree with the archived CHECKS.json byte-for-byte. The original
PROOF.md, CONTOURS.md and verify.py Git blob identities match the frozen
source IDs in SOURCES.md. Its old mutations and any historical numerical
reports were NOT regenerated. The short-support predecessor is not a logical
input to the two new components and is not said to have received a new audit.

## Adversarial mathematical reading

The local calculation was rederived from C_(t,k)(J), rather than extending
CT's majorant by an unsupported analytic-continuation slogan. We checked the
negative j=5 boundary, both j=3 channels, the raw theta=chi(u/p^j) versus
masked chi(u) distinction, and normal convergence away from ramified primes.
The global sharpness example enlarges S ONCE and does not infer a lower
bound for the signed Poisson sum from a local coefficient.

For the detector, the inducing conductor is dyadized before applying a
negative dual exponent. Both AFE pieces and full columns c*d^6 are present.
The line shift changes the B exponent as well as the mollifier mass.
The cardinality is retained inside Holder until elimination. The Gamma
contour crosses only a zero residue, and the one-zero-per-index norm-prefix
and height maxima are explicitly paid. Small nearby-line losses are absorbed
before choosing the fixed polynomial height rho. These are same-author proof
checks, not an independent referee verdict.

## Packaging checks and limits

Syntax compilation, the payload manifest, fresh ZIP-extraction replays of
both checker modes and all eight mutations, and an add-only Git patch
application in a fresh LOCAL FIXTURE passed. The fixture was not a cloned
full repository; no claim of a full repository worktree or CI pass is made.
The exact receipt and hashes are in the outer PUBLICATION_RECEIPT.json.

The active GitHub tools exposed read/search but no commit/branch/push action.
A plugin search found only the installed hybrid GitHub connector. Direct
`git ls-remote` failed with `Could not resolve host: github.com`; no gh CLI
or authenticated publishing session was available. No new remote branch,
commit, comment or PR was created. Existing #966 remains the verified base.

A first combined packaging command exceeded its 20-second execution limit
after producing the patch and initial ZIP. That run is NOT counted as a
successful fresh-extraction replay. The subsequent bounded synchronous
replay completed all normal/optimized, mutation and packaging checks.
