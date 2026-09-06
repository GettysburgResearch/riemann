# Reviewer D — final two-pass review of integrated main

**Status: final independent reconstruction handoff for the integrator, with
explicit partial mathematical coverage.** This is neither blanket acceptance
of main nor a claim to have re-proved every canonical statement. RH and GRH
remain unproved in the inspected work.

**Audit date:** 2026-09-06 (Asia/Jerusalem). **Repository:**
`GettysburgResearch/riemann`. **Controlling baseline:**
`main@8d16f8d9c475db290bc85e53d775b93b9bcdb336`, tree
`91742c176e5f7e5df8669e9a55f258c4889a1c12`.
**Scientific release under audit:** integration/2026-08-22, through PR #707.
**First-pass D head:** `55a7371432760ff44d396f6e63d95d65e64ad2a5` (PR #799).
**Review branch:** `review/D/20260905-integrated-main-reaudit`.

This closeout adds only `reviews/D-final/`. The original sixteen-file
`reviews/D/` packet, including its exact-coverage validator, remains unchanged.
This sibling layout preserves both the scientific and executable history.
The final publication SHA is recorded in the PR and downloadable receipt; it
is not guessed or embedded circularly in this commit.

## 1. Bottom line and recommended integration decision

The first pass found seven definite defects or missing hypotheses. The second
pass confirms their dispositions and adds four findings: a wrong Farkas dual
sign, an unsupported rational-certificate guarantee for real data, a missing
real part and operator-domain distinction in a jump-generator identity, and
a Fourier-normalization error in the leading Fredholm coefficient.

**Recommended action: targeted repairs under new identities, not wholesale
rollback.** The worst new defect is the Farkas sign: as printed, it permits
an 'infeasibility certificate' for a feasible system. The operator corrections
change exact formulas and proof contracts, but do not destroy the surviving
safe-line Poisson construction or fixed-degree high-carrier obstruction.

This pass also finishes several important previously unread adapters. It
reads the complete Vaughan two-field coefficient factorization, reconstructs
the actual safe-scale Julia mass bounds, inspects the discrete Dickman
comparison and signed profile argument, reviews the native Y4/Volterra
interfaces, and supplies a detailed reciprocal-zeta/Hardy argument for the
wavelet upper abscissa. No critical signed estimate is proved by those steps.

The combined handoff has **114 component review dispositions** (74 first-pass,
40 second-pass), **123 recorded edges** (62+61), and **106 inspection records**
(67+39). These are counts of records and components, not distinct canonical
claims or accepted theorems. Some second-pass records revisit an earlier
source. The complete 24-family/139-row canonical denominator remains visible
in `COVERAGE.tsv`; it is not a claim that all 139 rows received full proof
review. Legacy Robin/Xi/correction surfaces are additional to that denominator.

## 2. Consolidated findings and extraction actions

All detailed first-pass counterexamples remain in `../D/REPAIRS.md`.
New repairs R11–R18 are in this directory's `REPAIRS.md`. Source IDs resolve
to full commit/path/blob locators, not moving branches.

| Finding | Scope and verdict | Required integrator action |
|---|---|---|
| D-F01, L-95601 | Varying-order extension is false even with orders 2 and 4; fixed filter theorem survives. | Separate fixed Toeplitz inversion from the actual varying-row inverse; remove unsupported extension. |
| D-F02, L-91900.6 | Spectrum does not imply an eigenvector at the feedback threshold. | Replace full spectrum by point spectrum or add appropriate compactness/isolation. |
| D-F03, resident Hermite packet | 'Negative principal minor not necessary' is false for finite Hermitian non-PSD. | Correct to all-principal-minor criterion; distinguish leading minors. |
| D-F04, L-100130 versus original wavelet | Endpoint energy normalization differs by `((X/8)^2-1)|G_mu(X)|^2`. | Correct the identity; attach first-pass suffix-field repair and new R15 analytic adapter. Neither critical energy bound is proved. |
| D-F05, resident matched-pole packet | Integration omitted `n>=2`. | Restore the original hypothesis; one-node construction is zero. |
| D-F06, resident Robin envelope | Cap variables and feasibility contract were omitted. | Restore `n_r`, certified caps and minimum-tail feasibility, or use the explicitly weaker cap-free envelope. |
| D-F07, L-101103 | Initial negative excursion is uncharged. | Charge both boundary components or require nonnegative initial value; retain the triviality of subpower log-length at that normalization. |
| **D-F08, S01 L-94023** | **Printed Farkas obstruction sign is false.** | For `Az=b,Gz>=0,z>=0`, use `A^Tu-G^Tv>=0,v>=0,b^Tu<0`. Check copied certificate implementations. |
| **D-F09, S02 L-91671** | Real duality does not guarantee rational certificates. | Add rational-data or effective algebraic/symbolic witness contract; weak/equality rows cannot be proved by merely small residuals. |
| **D-F10, S03 L-91029.9** | Unsymmetrized generator identity is generally complex and mixes vector/matrix actions. | Insert `Re`; specify vector multiplication or matrix conjugation and correct norm. Do not infer self-adjointness. |
| **D-F11, S04 HC.14** | Inherited Fourier normalization requires `2pi mu(T)B`, not `mu(T)B`. | Normalize the entire zero/gamma/prime form consistently; retain the corrected fixed-degree no-go. |

These are not eleven refuted programmes. D-F05/D-F06 were extraction omissions;
D-F09 is an assurance contract; D-F11 is an exact normalization defect with a
surviving asymptotic sign consequence. No actual off-line zeta zero or negative
actual-Xi kernel value is claimed.

### D-F08 is an immediate proof-level counterexample

With `A=G=b=1`, `z=1` is feasible, while `u=-1,v=1` meets every condition of
the source's printed plus-sign 'dual'. Therefore the alternatives can both
hold. R11 derives the correct minus-sign version by a nonnegative slack.
The other native Farkas source, S02, uses `Gx<=c`; its plus-sign dual is
correct and must not receive the same edit. The source convention, not the
name 'Farkas', determines the sign.

### D-F10 and D-F11 must not be dismissed as unexplained notation

The one-jump vector example `D=-i,f=1` has negative generator inner product
`1+i` and squared-increment half-energy `1`. R13 gives the exact real-part
identity, plus the separate Hilbert–Schmidt conjugation version. The safe
Euler compound-Poisson law itself survives.

The Fredholm source's own evaluation-vector norm fixes the unnormalized
Fourier transform. Plancherel then supplies the missing `2pi`. The discrepancy
multiplies a nonzero positive trace-class `B` by a quantity growing like
`log T`, so it cannot be hidden in the claimed bounded remainder. R14 pays the
corrected uniform remainder and proves that fixed exterior/Hankel degree
blindness survives. The full exceptional-zero index still imports a
cardinal-source capture theorem not completely re-audited here.

## 3. Important second-pass survivals and proof completions

### Native sources and exact finite alternatives

S02's atomwise sum really does prevent source overdraw when every local
identity uses the same coordinate vector. S01's common-template primal is
also legitimate as a *finite reduction*. Neither proves live feasibility.
S09/S29 preserve every finite shift coefficient, including future-prime
completion and parity. The coefficient budget below one eighth is not a
physical mass theorem until a common typed source identifies those quantities.

S11/S12's radix-four inverse and score-null ancestor support are exact on
indices at least two. The triangular lower tail can still create negative
rows. Nullity in the radial dictionary is not free feasibility. S10's
Volterra formula correctly has both `sqrt(x)` and `x` boundary modes and
all derivative-jump atoms; use `a>0` and the stated regularity. S13's real
finite cubature is conditional on a genuinely positive finite endpoint
measure and integrable typed coordinates. Its already excluded literal-score
assignment remains excluded.

### Supercritical Taylor and critical consumer

S06/S07 give real mathematics: an activation-zero positive-source theorem at
all real powers `m>=2`, and positive Taylor remainders up to the stated
level. Their source is not silently identified with the ordinary SHARP
kernel. The critical multiplier in S08 is exact; every artificial real pole
is removed by the lower-interval correction or the zeta-pole zero. The
Landau conclusion still requires a signed producer.

R17 separates eventual sign (sufficient), subpower logarithmic negative mass
(equivalent, with a supplied RH-to-Mertens converse), and the quadratic
identity. A combined '.7–.9' label cannot treat these as one assertion.
The critical contraction does not follow from the supercritical signs.

### Vaughan, Dickman and Bellman

S15/S16 close the previously unread finite coefficient factorizations:
`a_U=b_U*1` and `a_U*a_U*mu=b_U*b_U*1=b_U*a_U=h_U*h_U`.
The two ratio-four kernels multiply in Mellin space, and the squarefree gcd
constraints are necessary. Step endpoint conventions are harmless in
integrals, not in arbitrary literal finite point sums. Keep the first-pass
Hardy truncation repair; the whole two-field energy estimate is still open.

S17's Dickman comparison retains both the CDF-discrepancy term and the
repeated-prime correction. S18's signed full-base profile is a valid adapter
under a finite exponentially weighted variation bound and positive total
mass. The actual P61 base expansion/variation is still an explicitly
unreconstructed primitive input. Classical VK and de Bruijn estimates remain
named imports with their ranges, not new numerical certificates.

The claimed Bellman inequality is exactly equivalent to same-state positivity
by S19's source recurrence. It is not an additional independently stronger
sign theorem. Heredity means applying the established state theorem again
at descendants which still satisfy its hypotheses; it does not pass through
the deep fixed-small-prime region.

### Safe operator mathematics

The positive divisor cocycle and its Hilbert-space isometry (S21) and the
second anchor-jet orthogonal decomposition (S22) survive. A three-dimensional
source jet does not construct its metric-preserving physical-port adapter.
The completed source/curvature sign is still a separate problem.

S27's actual prime mass `m4<85/196` and S28's algebraic six-term bound
`n4<1/4` have been freshly reconstructed. The old corrected reserve is
`21587/38416`; this is a replay of an existing repair, not a new discovery.
Nakamura's quasi-Lévy density and its normalization are explicit imported
source inputs. Safe tail-Hankel domination does not identify the critical
completed Gram.

The Brownian selected-prime argument in S20 survives at the precise producer
class and top-half-mass hypotheses in the inspected review extract. This
pass does not reject every possible positive mixture or Brownian construction.
Its primary-source fixed-height expansion and all original computational
packages are not independently replayed.

### Wavelet analytic adapter and finite controls

R15 supplies the reciprocal-zeta growth and half-plane Hardy bound previously
left as an imported adapter. It uses an analytic logarithm in a zero-free
half-plane, Borel–Carathéodory, a Gaussian-damped three-lines argument, then
uniform Hardy norms and causal Laplace uniqueness. It does **not** infer a
causal source from one finite meromorphic line integral. The upper energy
abscissa is therefore supported under the explicitly stated standard analytic
imports. Boundary attainment is not asserted. The two distinct energies
remain distinct, with the earlier repair for the original criterion.

The resident finite Pick-box packet is correctly conditional on its supplied
primitive rectangles. Only its generic exact midpoint/radius implication is
newly reconstructed; the actual high-ordinate xi evaluations are not replayed.
The previous finite Robin reconstruction and low-order actual-Xi proof audit
remain in the first packet with their original dependencies.

## 4. Concrete extraction destinations and priorities

These are proposed destinations for NEW correction objects; no edit to these
paths is made by this PR.

| Priority | Destination | Required content / review gate |
|---|---|---|
| P0 | `research/integrated/native_assets/FARKAS_CORRECTIONS_2026-09-06.md` | R11/R12, convention-specific dual signs, exact one-variable counterexample, certificate arithmetic class; update `ARITH.LIVE_MARGINAL_FARKAS` and `ARITH.FINITE_FARKAS`. |
| P1 | `research/integrated/direct_main/cauchy_jordan/JUMP_GENERATOR_CORRECTION_2026-09-06.md` | R13, vector versus matrix domain, real part and symmetry requirements; do not delete the valid Euler/Poisson construction. |
| P1 | `research/integrated/operator_no_go/FREDHOLM_NORMALIZATION_2026-09-06.md` | R14 with both Fourier conventions, corrected `c_Tilde`, full-source scaling and conditional capture boundary. |
| P1 | `research/integrated/wavelet_xd/ENERGY_AND_HARDY_REPAIR_2026-09-06.md` | First-pass R4 plus R15, separate energy definitions, causal H2 argument, no attainment at the abscissa. |
| P1 | `research/integrated/q4/VARYING_FILTER_FIREWALL_2026-09-06.md` | First-pass R1 counterexample; retain fixed filters and require actual varying-row inverse. |
| P2 | `research/integrated/corrections/D_REAUDIT_ERRATA_2026-09-06.md` | Spectrum/point-spectrum, all versus leading principal minors, matched-pole n>=2, Robin caps, initial excursions. |
| P2 | `research/integrated/dickman_bellman/BELLMAN_SCOPE_2026-09-06.md` | R16; state exact equivalence with same-state positivity and preserve P61/VK/de Bruijn dependencies. |
| P2 | `research/integrated/direct_main/taylor/CRITICAL_SCOPE_2026-09-06.md` | R17; split eventual sign, negative-mass equivalence and quadratic identity. |
| P2 | `research/integrated/direct_main/p79/EXACT_SPLIT_SCOPE_2026-09-06.md` | Replace inclusive .2–.8 locator by enumerated algebraic equations; retain existing false positive-splice dispositions. |

After independent checking of the new repairs, the integrator should propagate
scope and dependency changes to the canonical release claims, edges, root
RESULTS/PROOF_GRAPH/OPEN_CUTS and formal statement trackers where relevant.
Do not edit the frozen source proof or pretend that a repaired statement
validates its original version. No large certificate is invalidated here
merely because its producer was not replayed; conversely no unreplayed
certificate is re-certified by this report.

## 5. Coverage, omissions and narrowly targeted outstanding review

`COVERAGE.tsv` supplies a final row for every canonical family and the four
additional first-pass surfaces. Unlisted claims keep their previous status
but receive **no new D acceptance**. Important residual checks are:

1. **P61 primitive closure:** derive the repaired annular base, its differentiated
   expansion and weighted variation from the actual finite source; verify
   constants/ranges of the imported VK/de Bruijn statements if an effective
   numerical endpoint is to be claimed. No `J_*` interval replay here.
2. **Full cardinal capture:** check the PR #365 Xi-cardinal construction, its
   decay and differentiability, and membership in every required Gaussian
   range. S05 was read only through line 215. This controls the complete
   exceptional-zero index, not the repaired high-carrier bulk calculation.
3. **Uncovered producer families:** full C4MBI, native endpoint, factor-67/Lorenz,
   Q4 annular/Goldbach/finite-filter critical-zero proof closure, carrier/staircase
   and remaining safe-line/Green-port inputs were not exhaustively re-audited.
   The gate map is metadata, not a replacement proof.
4. **Primitive computational evidence:** no original high-ordinate Pick boxes,
   large Robin streams, full factor64 reward producer, P79 certificates,
   Brownian fixed-height package or external zero verification was regenerated.
   The finite suites below have strictly smaller, declared scopes.
5. **Formal and provenance closure:** no Lean/Comparator/Nanoda build or remote
   CI run, no all-139-row source-tree closure, no new complete PR/issue archaeology.
   The partial canonical TSV fetch in this pass is not represented as full
   inspection; the known denominator comes from the first-pass family ledger.
6. **Source collisions:** S30 is the different PR #403 L-91307, inspected to
   disambiguate S27's Julia mass source. It gets no whole-theorem acceptance.
   There is no claim of external reviewer independence or complete absence
   of historical authorship overlap; independence here means fresh derivation
   and a checker importing no original producer.

These are final handoff questions, not dependencies on unpublished A/B/C work
and not assertions that those reviewers failed. Cross-review reconciliation
and any targeted additional audit belong to the integrator. Reviewer D's
requested two-pass report is closed at this explicit boundary.

## 6. Validation and preservation

The new checker runs **35 named bounded checks / 26,407 fixtures** in each of
normal Python and Python `-O`, with byte-identical reconstructed outputs.
Most fixtures are elementary finite parabolic-support checks; the count is
not a measure of theorem coverage. It uses exact rationals, Gaussian rationals,
algebraic numbers and symbolic identities. It evaluates no zeta values, no
large prime sum, and no zero census. Its analytic Gaussian integrals are
symbolic controls, not directed numerical quadratures.

The entire original first-pass checker was also replayed in both modes:
**45 named checks / 9,380 fixtures** per mode, plus its package validator.
The original rejection records remain authenticated; they are not relabeled
as newly executed original rejection CLI runs. New corruption checks and
package hashes are recorded in `VALIDATION.md`.

Finite tests do not machine-prove the infinite analytic arguments, classical
imports or source identifications. All new acceptance recommendations refer
to the proof reasoning above and in `REPAIRS.md`, with those boundaries.
