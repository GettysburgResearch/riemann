# Reviewer C4: mathematical coverage and source-faithful repair handoff

**Status: completed targeted paper-level review and repair packet; the exhaustive Reviewer-C allotment and public-release clearance remain incomplete.**

Repository: `GettysburgResearch/riemann`.
C review PR: **#798**, branch `review/C/2026-09-05-post-release-audit`.
Publication parent and inherited coverage: `e0d1cb976030048275b5c2cda4275341650a350c`.
Scientific/policy baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Scientific boundary: August 22 integration, research through PR #707.

This successor is the former Reviewer A, reassigned by the user to C. The role
change supplies neither a second independent endorsement of A's report nor a
non-author verdict on #793 or A-authored Architecture-E work. C's previous author
of #792 is not the author of this successor review; the limited #792 assessment
below comes from new derivations of the two specified proof files. Earlier A
reading is disclosed, and this is not counted as a second independent vote.
No unpublished reviewer result is a dependency.

The deliverable is additive under `reviews/C/pass4-math-completion/`. Earlier C
reports and the 566-row census are preserved, not silently relabeled current or
complete. No original research, main, canonical registry, formal source, workflow,
repository permission, or release setting is changed. Publication identity, if
any, belongs in the separate publication receipt, not a self-referential seal.

## 1. What this pass adds

The strongest addition is a complete **conditional mathematical replacement for
the actual-Xi source-to-order-three Pick argument**, including the previously
unexplained prefix assembly and the positive-node domain across the half-node.
It does not inhabit the old contradictory input type. It describes a new,
source-faithful type and proves the required consequences from explicit spectral
and entire-function assumptions.

The second addition is a complete reconstruction of the two analytic propositions
still supplied as formal consumer inputs: tail-Mellin Landau boundary singularity
and holomorphy from subpower logarithmic negative mass. Two further adapters,
initial-agreement extension and affine pole multiplicity, receive proofs. These
are classical analytic tools, not a new Möbius estimate or an RH proof.

The third addition is a fresh proof-level audit of #792's full-source
finite-window coercivity and energy-completed Schur reduction. The precise
normalization, infinite prime tail, one integrable kernel derivative, energy-space
completion, Galerkin direction, and residual lower bound are reconstructed. The
actual effective-matrix sign remains unproved.

Inventory: **22 source-file inspection records, 38 component dispositions,
24 conjunctive implication records, and 16 explicit hypothesis/conclusion nodes**.
These are not counts of accepted theorems, transitive imports, or independently
rebuilt Lean declarations. Some files were inspected previously; this inventory
records this pass's actual reading scope. The catalog read is explicitly partial.

## 2. The source and publication baseline

The current C PR and main ref were read before substantive work. They matched the
requested C head and the baseline above. AGENTS.md, docs/REVIEWING.md and the
previous canonical manifest were reread at that exact baseline. The manifest
itself freezes main `677203992eb0168920365ee45ae9db76bfa97dcf` for the historical
August 22 science; present main is not substituted for that frozen research.

`SOURCES.tsv` binds each inspected file to repository, exact commit, Git blob,
returned range and limitation. `CENSUS_DELTA.tsv` names only this pass's review
objects. It is not a newly acquired census of 340 historical or 79 postcut PRs.
No fresh semantic inference is drawn from a historical `updated_at` value.
`SOURCE_VERSION_DIFFS.tsv` records that #792 matches its inherited pin, whereas
A's #795 has advanced from the census's `f184ca...` to `b50bb781...`. This
review-version drift is flagged for reconciliation, not inherited acceptance.

The large historical `FORMAL_CATALOG_AUDIT.tsv` response was truncated. Its
leading returned rows were used for routing, but the record is not represented
as a fresh complete 37-row read. In contrast the shared Xi definitions, six
selected Mellin modules, Xi reserve/curvature/Pick modules, and the two #792 proof
files were read in complete or explicitly overlapping ranges. The source table
makes the distinction auditable.

## 3. Mellin analytic gaps: paper proofs now supplied

Read [the complete Mellin proof](proofs/MELLIN_ANALYTIC_GAPS.md).

### 3.1 Preserve the actual transform and singularity predicate

The convention is exactly

\[
 \mathcal M f(s)=\int_1^\infty f(x)x^{-s-1}\,dx.
\]

The formal `NonremovableAt` means `not AnalyticAt` for a *total function*. It
is weaker than no analytic extension of a punctured germ. A function supported
only at one point demonstrates the difference. Existing holomorphic-defect and
nonvanishing-multiplier transfers remain correct for their actual total-function
equalities. The review supplies the corresponding genuine punctured-germ theorem
and requires a new identity if that stronger language is used.

### 3.2 Tail Landau, with the actual quantifiers

For a locally integrable tail, eventual nonnegativity, and finite real abscissa c,
subtract the compact initial portion and change variables x=exp(y). One obtains
a nonnegative Laplace density. Absolute convergence strictly to the right gives
all analytic derivatives there. If an analytic extension existed around c, take
a nearby Taylor center to its right. The alternating derivatives are nonnegative
moments. Tonelli sums the positive Taylor series at a point to the left of c,
forcing convergence there and contradicting the definition of c.

The proof specifies the disk and displacement, handles the compact head, and
uses absolute convergence rather than assuming a pointwise bound on the density.
It proves the exact mathematical content of `MellinLandauBoundarySingularity`.
It is **not a compiled Lean implementation** of that proposition.

### 3.3 Negative-mass holomorphy

Let A(X)=integral from 1 to X of f_-(x)/x. A bound A(X)<=C_epsilon X^epsilon
for every positive epsilon implies convergence of the negative-part transform
and all its differentiated integrals on every compact in Re(s)>0. The proof
uses dyadic shells and retains the epsilon, constant, threshold and compact
minimum real part. It also gives a quantitative far-tail bound. It does not
supply a bound uniform up to Re(s)=0.

### 3.4 Two adapters and the whole criterion

The identity theorem proves the `hContinuationExtension` adapter from the
existing core's half-plane analyticity, convergence and initial agreement. Local
factorization proves `ShiftedReciprocalPoleOrder` under the exact multiplicity
interpretation, with every finite multiplicity and any nonzero affine slope.
Neither argument constructs the complete native core or a native sign estimate.

The paper-level consumer is reassembled, including the case where the positive
part has abscissa minus infinity. The all-zero and compact-support cases cannot
be excluded merely because a formal API packages only a real finite abscissa.
The first open arithmetic burden is still the literal every-epsilon negative-mass
estimate for the fixed detector, with its source identity and fixed noncancelling
factors. Reflection/zero-location infrastructure remains explicitly named.

There is also a separate total-value normalization obligation at zeta's pole:
its reciprocal should have the analytic value zero. The report gives a correctly
extended reciprocal using entire xi and the gamma factor, but does not assert
an unevaluated value of Mathlib's total zeta(1), or a second universal contradiction
in the fixed-detector API.

## 4. Actual Xi: a complete conditional repair, not a proof from empty inputs

Read [the complete Xi repair](proofs/XI_SOURCE_REPAIR.md).

### 4.1 Correct function, not an arbitrary patched node

The pinned Mathlib declaration states

\[
 \Lambda(s)=\Lambda_0(s)-1/s-1/(1-s),
\]

with entire Lambda_0. Thus the required normalization is

\[
 \boxed{\xi_{\mathrm{ent}}(s)=\frac12+\frac12s(s-1)\Lambda_0(s).}
\]

It is entire, satisfies the functional equation, equals the raw product away
from 0 and 1, and has value 1/2 at both removable points. Its centered version
is even. The pinned Mathlib overview has a sign inconsistency with its actual
declaration; the repair is bound to the declaration body, not that overview.

The old formal raw product is exactly zero at s=1. Its centered Pick node at
x=1/2 is therefore zero, contradicting the required `diagonalPositive` field.
This confirms the prior C source-level nonvacuity defect. It is not kernel
inconsistency and does not refute the intended informal theorem.

### 4.2 Complete countable spectra must permit no off-line zeros

An injective Nat-to-off-line-orbit map requires infinitely many off-line orbits.
Replacing the xi value does not cure that issue. The new contract uses arbitrary
countable index types and finite exhaustions, or optional padding. Every actual
location is represented exactly once with analytic multiplicity; the selected
critical reserve is explicitly disjoint from the other-critical list.

Three individual omissions in the old list fields are identified. They are not
claimed to yield a countermodel to the entire old input, which is already empty
and whose additional convergence fields may impose other restrictions.

### 4.3 The finite and infinite steps are both supplied

For a threshold H>=1024, a selected critical ordinate gamma0<=H/2, and off-line
representatives 0<a<1/2, b>H, retain the literal blocks

\[
 R(t)=2/(t+\gamma_0^2),\qquad
 q(t)=4m(t+b^2-a^2)/((t+b^2-a^2)^2+4a^2b^2).
\]

The complete mathematical argument proves:

* a reciprocal-square count bound controls total shares, with unused reserve
  at least **215/512** under the displayed coarse hypotheses;
* the source's one-orbit payment works on **every t>=0**, not only t>1/4;
* paid prefixes equal the original spectral partial sums, with selected
  multiplicity and all cross terms retained;
* derivative majorants yield C2 convergence across t=1/4 and on the full positive
  domain; Hadamard factorization identifies the limit with the correctly entire
  source, conditional on exact complete zero data and order<2;
* positivity, the two scalar monotonicities, companion concavity and reciprocal
  concavity follow on that same domain;
* the exact determinant factorization and a strict two-node pivot imply PSD
  through size three; repeated evaluation nodes are handled by exact congruence.

This is a replacement for unexplained analytic fields, not permission to erase
the external source contract. The verified-height theorem, existence of the
selected reserve, all-height zero-count input, actual entire growth/zero
identification, and compiler-level implementation still need their own acceptance.
A normalized metadata string proves none of them.

The proof provides empty, finite and infinite synthetic off-line examples for
nonvacuity testing. One finite example has genuine nonreal centered zeros while
still satisfying the low-order positivity contract. These are not actual-zeta
counterexamples; they demonstrate that the repaired hypotheses do not hide RH.

### 4.4 Formal delivery boundary

`lean/EntireXiRepair.lean` is a complete candidate for the function-level repair
and elementary regressions, with no placeholder proof bodies. **It was not
compiled**: Lean and Lake are absent in the active environment. Candidate source
is not reported as a kernel-checked theorem. It lies outside trusted imports.
All shared definitions, consumers, Challenge/Solution pairs, hashes and registry
rows must be updated coherently in an authorized repair, followed by an exact-tree
build. This packet deliberately makes no trusted-source edit.

## 5. #792: the previously author-excluded operator components

Read [the fresh operator reconstruction](proofs/OPERATOR_AUDIT.md).
Source: `465cb28ed8cbfa1bb071d9a85eeda9890decfe6b`, precisely the two proof files
listed in `SOURCES.tsv`. This is not an independent blanket acceptance of #792
or a replay of its numerical reconnaissance.

The reconstruction pays the full prime-power tail on a fixed window as a signed
rank-two form, derives the Fourier multiplier on the constrained subspace, and
checks the 2pi normalization. The exponentially growing kernel is not assigned
an unrestricted integrable Fourier transform. The archimedean lower barrier
holds for every frequency, not merely sampled frequencies.

The positive subspace has finite codimension, with a primitive-norm lower bound
compatible with compactness. At L=1 the exact sufficient choices K=101 and X=3
are reconstructed, including the sharpened primitive coefficient 6/5 and the
corresponding residual coefficient 15/8. These statements do not prove that the
full 104-dimensional effective form is positive.

Only one integrable kernel derivative is needed for the source-specific coupling.
The gamma derivative's logarithmic singularity and prime-power cusps remain in
the proof. Completing the positive subspace in its **energy norm**, rather than
inverting a compact L2 block, gives the legitimate finite Schur form S_L. The
positivity and negative-index identities survive; an unrestricted nullity
identity would be false.

Galerkin effective matrices converge to S_L from above. Positive upper sections
are not lower sign certificates. For arbitrary exact trial corrections, the
matrix bound

\[
 U-3R\preceq S_L\preceq U
\]

is valid, with 15/8 in place of 3 for the specified L=1 subspace. R is the full
complex residual Gram. Approximate constraints, integration, matrix entries and
rounding require separately certified error bounds. No actual continuum lower
certificate is generated here. A fixed-window certificate would still not prove
the unbounded family of signs needed by the RH-facing route.

## 6. Evidence and trust separation

The independent checker does not import any upstream research producer. It
reconstructs **17 symbolic identities and 1,075 other bounded fixtures**, totaling
**1,092 controls**. They include rational orbit geometry, all principal minors
of finite synthetic Pick packets (including repeats), reserve-prefix identities,
countable-contract finite controls, exact Schur examples and rational constants.
Normal and optimized Python runs return identical mathematical payloads.

These are finite controls, not machine proofs of Landau, dominated convergence,
Hadamard factorization, the actual zeta spectrum, Plancherel, or the complete
operator inequalities. The associated paper proofs and their assumptions are
the evidence for those analytic statements. The package validator checks content,
identity joins, declared scope and graph consistency; it does not verify the
proof text. See `VALIDATION.md` for replay commands and rejection tests.

No large zero/prime/interval campaign, remote CI, Lean build, Comparator,
independent-kernel replay, all-history scan, or original-paper PDF audit was run.
The old A independent seven-point certificate is not counted as new C evidence.
The formal actual-Xi source finding remains a source-level argument, not a new
compiler transcript.

## 7. Corrected route map and first open theorem

| Route | What the new packet supplies | First remaining burden |
|---|---|---|
| Fixed Mellin detector | Landau and negative-mass holomorphy, initial extension and affine pole-order proofs, complete conditional criterion | Literal fixed-source every-epsilon negative-mass estimate, plus compiled/source-bound analytic adapters |
| Actual-Xi Pick through three | Normalization/index repair and conditional source-to-prefix-to-curvature-to-PSD argument on all positive nodes | Actual source bindings and compiled inhabited repaired API; then genuinely higher-order positivity, not extrapolation from order three |
| #792 finite-window operator | Full-tail constrained coercivity, W1,1 energy coupling, effective Schur/index equivalence and residual lower enclosure | Rigorous actual lower matrix, then an unbounded prescribed family of effective signs; global xi/coefficient adapter remains separately scoped |
| Native arithmetic, other heat/theta/Weil, geometry and imports | Earlier scoped review records retained, not newly upgraded here | Their literal signed estimate, full-source sign, external theorem or specialist source-binding gate as recorded by primary reviewers |

There is no reviewed-only route to RH. The small implication ledger keeps native
negative mass and all-length effective signs as distinct open nodes. It also
retains the actual-Xi implementation/source-binding gate and has no order-three
positivity-to-RH arrow.

## 8. Unchecked material and integrator handoff

The requested targeted mathematical work is delivered; **most of C's broad
census/security/build allotment is not claimed completed**. The unclosed classes
remain enumerated in `COVERAGE.tsv` and `RELEASE_BLOCKERS.md`:

- exhaustive claim splitting and transitive/branch/attachment coverage of the
  inherited 79 postcut PRs; fresh 340-head acquisition;
- all uncataloged formal modules and the full pinned Mathlib/Zeta23 import
  closure; exact compiler, comparator and independent-kernel executions;
- actual primitive continuum/physical-integral certificates and complete
  producer-to-correction campaigns;
- external paper/version and license/NOTICE rights checks, all-history
  secrets/PII scans, complete ACL/bypass audit and effective launch controls;
- independent acceptance of former-A-authored work and specialist B review.

B remains the appropriate cross-review for automorphic, Segre/Chow, partial
Frobenius and full #765 transport modules. Integrators must reconcile source
versions and scientific dispositions rather than treat a routing label as
acceptance. No external source premise is discharged by the absence of a local
counterexample. Review the new repair proofs under new identities; preserve
old source SHAs, failed definitions and scope-qualified counterexamples.
