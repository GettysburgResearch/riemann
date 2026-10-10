# Validation, review scope, and source boundaries

**Status:** proposed standalone component proofs. This packet has scoped independent agent reviews and exact finite checks. It has not been merged, formally verified, or accepted as a proof of a full moment or RH.

## 1. Analytic dependency levels

The exact support argument uses the classical cubic theta transformation in the normalization of the imported October 5 source, its finite cusp family, and the kernel calculation proved here. It does not use the imported canonical induction, a pointwise Möbius saving, or a large sieve. The arbitrary-row addendum also uses the source's explicit fixed-family statement for bad-prime, unit, and reciprocity factors. Its conclusion is exact vanishing for a complete reunited component, not an averaged estimate.

The all-cusp quantitative theorem and cube-inverse theorem with scalar exponent beta=1 use elementary ideal counting and the named classical quadratic and cubic upper large sieves in addition to those theta inputs. The cusp coefficient identification is checked directly against Dunn–Radziwiłł, arXiv:2109.07463v3, equations (5.7), (5.13), (5.14), and (5.16). That paper's GRH-conditional main results, dispersion theorem, and sieve lower-bound claims are not used. ARBITRARY_ROW_MOMENTS.md then proves the additional mixed-scalar, row-power, and auxiliary-allocation adapters; the all-row mean squares are not inferred from the support theorem alone.

The improved scalar exponent beta=11/12 has an additional dependency: the fixed-angular extension of the imported canonical/two-Poisson theorem. The new note proves the derivative, gamma, iteration interface, extraction, and conductor-uniform reciprocal adapters. It does not independently reconstruct the entire underlying October 5 canonical proof. Thus the improved ranges are source-conditional deductions. A defect in that imported analytic input would invalidate the improved ranges without invalidating the separately proved finite identities.

The general-order incidence estimates use the native second moment with uniform moving exclusions, pinned to PR #913. Optional finite-order pointwise exponents are separate premises. This beta is not the angular family's beta unless a theorem explicitly identifies the inputs; no such substitution is made here.

The exact centered-sign witness is finite and unconditional within the stated native coefficient conventions. It disproves universal positivity of that centered form. It supplies no asymptotic lower bound or counterexample to the desired moment.

## 2. Frozen proofs and independent reviews

The final source hashes are recorded in PROVENANCE.json. Reviews bind the exact source hashes printed inside them. Their PASS verdicts apply only to their stated source-qualified scope.

| Source | Review coverage |
|---|---|
| ANGULAR_THETA.md | angular_initial_review.md audits the derivative and first canonical checkpoint; root_review.md binds the final source and verifies the required canonical-domain repair. angular_component_review.md independently audits the final scalar and component sections. |
| DOUBLE_REFLECTION.md | support_cutoff_review.md and root_review.md check the literal completion, second twist, normalization, pole-free composition, and standard-face cutoff. |
| REUNITED_SUPPORT_CUTOFF.md | support_cutoff_review.md and root_review.md check the generic finite-cusp transform, raw kernel constants, reunited period, and order of exact cutoff insertion. |
| ARBITRARY_ROW_SUPPORT.md | arbitrary_row_support_review.md and root_review.md check active/inactive zero masks, the fixed bad/unit family, branch scalar independence, and the exact all-row extension. |
| ARBITRARY_ROW_MOMENTS.md | row_quantitative_review.md and root_review.md check every active scalar exponent, the exact residual row factors, uniform scalar and sieve interfaces, disjoint row-sector Euler sums, moving auxiliary bounds, and sharp/Schwartz row profiles. |
| ALL_CUSP_GAUSS_FACTORIZATION.md | all_cusp_review.md and root_review.md check the primary cusp formulas, conjugation, additive normalization, purely cubic bad part, all valuation tails, and quantitative composition. |
| CUBE_INVERSE.md | cube_inverse_review.md, cube_inverse_second_review.md, and root_review.md check the exact inverse, both scalar families, all three coprimality corrections, smoothness, norm factors, and final range. The second review also independently inspects and replays its exact checker. |
| HERMITIAN_INCIDENCE.md | incidence_review.md audits the mathematical snapshot. root_review.md verifies the exact two-replacement typesetting erratum and closes the final-source binding. |
| CENTERED_NATIVE_SIGN.md | root_review.md checks the finite-field Gauss calculation, genuine source coefficients, all six unit rows, full finite completion, and correct product-diagonal subtraction. |

The first angular review requested Sigma=XF in the canonical theorem. The final source uses that exact equality and the required short-row domain; a looser transfer envelope is not substituted. The incidence source received exactly two control-byte-to-TeX repairs. Reversing precisely the two replacements recorded in reviews/incidence_typesetting_erratum.json recovers the independently reviewed mathematical snapshot. No mathematical alteration is hidden under that erratum.

The cube-inverse review separately reads the final finite shared-divisor proof, rather than inheriting approval from its earlier Euler-correction version. Its smooth terminal cutoff is inserted before applying a smooth scalar estimate. A shared correction label is explicitly allowed to overlap the remaining positive variable; imposing an extra exclusion would change the identity.

The reviews are independent checks by collaborating agents in this research pass. They are not a claim of external mathematical peer review or formal verification.

The earlier notes and their frozen reviews retain their original narrower row and auxiliary boundaries. ARBITRARY_ROW_MOMENTS.md and its own final review are the additional source for removing those restrictions from the specified positive norms. No earlier review is represented as having approved that later composition. The full signed covariance boundary remains unchanged.

## 3. Exact finite computations

The checkers use integer and rational arithmetic and explicit exception-based acceptance tests. None relies on Python assert statements that disappear under optimization.

| Checker | Predicates | Coverage |
|---|---:|---|
| checks/check_incidence_adapters.py | 36,190 | Forward mixed-sign Euler correction; all local phases and nonunit zeros; genuine sextic characters at split primes; full finite Hermitian gcd identities at orders four and six; native odd-incidence eligibility through order twelve; rational cutoffs. |
| checks/check_centered_native_sign.py | 8,230 | Native inert-prime cubic Gauss fibers; the specified actual coefficients and sextic values; full finite completed polynomial; exact opposite centered signs. |
| checks/check_support_algebra.py | 11,134 | All 648 matrices in SL_2(O/(3)); fixed-unit cusp reduction; 8,262 standard-frequency projection cases; all 81 selected local Ramanujan profiles; exact rational maxima for the completed range. |
| checks/check_cube_inverse_algebra.py | 46,080 principal finite cases, plus rational certificates | 9,216 shared-divisor identities with sixth roots and zero masks; 4,096 full allocation configurations; 32,768 row/cubic mask factorizations; exact vertex maxima and nonnegative gap certificates at five rational scalar exponents. |
| checks/check_arbitrary_row_algebra.py | 872 local cases, 24 parity cases, and valuation progressions | 432 active-scalar phase cases; 336 cross/reciprocity cases including positive valuations divisible by six; 104 exponent-four Ramanujan cases; the six powerful-row and six moving-auxiliary geometric progressions; unchanged quadratic parity. |

The first three reports contain 55,554 exact predicates. The additional cube-inverse report covers the separately enumerated 46,080 cases and rational certificates. Each checker was run normally and with Python optimization enabled; the corresponding JSON outputs agree byte for byte. Separate reviewers reproduced the checks specified in their reports. This is finite coverage of the described algebra, not of an unbounded arithmetic family.

The cube-inverse checker uses formal prime supports and exact sixth roots in Z[omega]; its norm labels are not represented as an independent evaluation of Eisenstein residue symbols. It deliberately detects two incorrect transformations: adding the forbidden exclusion between the positive residual variable and the shared label fails in 91 configurations, and replacing an extracted row zero by one fails a separate forced-prime test. Its report includes both regressions.

The arbitrary-row checker leaves Gauss factors as formal fixed monomials, checks all six character phases and their literal zeros, and records the scope of its original amplitude-based auxiliary tests. The later refined auxiliary allocation is additionally checked in the analytic review: its three pairs of squared-prefactor and length exponents are (-1,2), (0,1), and (-1,-1), giving energy maxima 0,1,2/3. The original physical-valuation tails at auxiliary primes have maxima -1,0,0. The full proof retains the required prime exclusions and source coefficient reindexing; exponent bookkeeping alone would not authenticate that analytic step.

Run each checker from the repository root, for example:

```bash
python standalone/2026-10-10-sextic-centered-covariance/checks/check_incidence_adapters.py
python -O standalone/2026-10-10-sextic-centered-covariance/checks/check_incidence_adapters.py
python standalone/2026-10-10-sextic-centered-covariance/checks/check_centered_native_sign.py
python -O standalone/2026-10-10-sextic-centered-covariance/checks/check_centered_native_sign.py
python standalone/2026-10-10-sextic-centered-covariance/checks/check_support_algebra.py
python -O standalone/2026-10-10-sextic-centered-covariance/checks/check_support_algebra.py
python standalone/2026-10-10-sextic-centered-covariance/checks/check_cube_inverse_algebra.py
python -O standalone/2026-10-10-sextic-centered-covariance/checks/check_cube_inverse_algebra.py
python standalone/2026-10-10-sextic-centered-covariance/checks/check_arbitrary_row_algebra.py
python -O standalone/2026-10-10-sextic-centered-covariance/checks/check_arbitrary_row_algebra.py
```

Compare each output with its corresponding file under results/. The checkers do not prove theta automorphy, a contour shift, conductor-uniform Möbius cancellation, an infinite moment estimate, or RH. No Lean build was run, and ordinary numerical precision is not presented as a directed certificate.

## 4. Working filenames in frozen notes

The mathematical sources and reviews were copied byte for byte into this packet. Some refer to their development filenames. The following mapping resolves those names without editing a frozen review:

| Working filename | Packet file |
|---|---|
| centered_a2_attack.md | ANGULAR_THETA.md |
| singleton_cancellation_attack.md | HERMITIAN_INCIDENCE.md |
| replica_bootstrap_attack.md | CENTERED_NATIVE_SIGN.md |
| double_reflection_attack.md | DOUBLE_REFLECTION.md |
| reunited_cusp_cutoff.md | REUNITED_SUPPORT_CUTOFF.md |
| all_cusp_gauss_factorization.md | ALL_CUSP_GAUSS_FACTORIZATION.md |
| cube_inverse_attack.md | CUBE_INVERSE.md |
| ARBITRARY_ROW_SUPPORT.md | ARBITRARY_ROW_SUPPORT.md |
| ARBITRARY_ROW_MOMENTS.md | ARBITRARY_ROW_MOMENTS.md |

The adjacent PR #915 is a pinned unmerged dependency, not part of this branch's ancestry. Its [coupled theta note](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/COUPLED_THETA_COMPLETION.md), [scalar audit](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/REFLECTION_SCALAR_AUDIT.md), and [reunited Ramanujan note](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/REUNITED_RAMANUJAN_EULER_PRODUCT.md) are read at the exact commit above. The manifest records their authenticated Git blob and SHA-256 identities, not hashes of locally newline-modified copies.

## 5. Assembly and acceptance boundary

Only this standalone packet and the root README navigation paragraph change. The packet has been checked for control bytes, paired mathematical delimiters, and local Markdown targets. Source and review hashes are checked against the exact final files. The staged Git tree is compared with the GitHub-created tree before publication. The draft PR is stacked on PR #914, exact parent 0cc0428fedbbfc340044c7451b3d392c1da9a103.

The staged whitespace check reports one trailing space in ANGULAR_THETA.md and six extra final blank lines in frozen source or review files. Those cosmetic bytes are retained deliberately to preserve the exact reviewed snapshots. No other whitespace issue was reported; the separate control-byte, delimiter, local-link, and content-hash checks passed.

No PASS verdict here establishes the strict signed off-diagonal bound in the parent A2_COMPLETION.md, equation (6.9). The quantitative all-cusp and cube-free bounds now include every nonzero row and the expressly defined moving fourth-power auxiliary twist. They do not control the signed auxiliary average or the centered sesquilinear form with independently corrected columns. The original balanced first-Poisson scale is of order D^(3-theta), beyond the proved ranges. Every-order balanced singleton cancellation, the full fourth moment, the cofinal generalized moment hierarchy, and RH remain open.
