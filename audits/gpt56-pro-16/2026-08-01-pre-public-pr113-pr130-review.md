# Pre-public review — PRs #113–#130 assigned set

Reviewer: `gpt56-pro-16`  
Date: 2026-08-01  
Published on: PR #164 / `agent/gpt56-pro-12/151-mode8-trace-form`  
Scope: PRs #113, #114, #115, #116, #117, #118, #119, #120, #124, #125, #127, #128, #129, #130

## Review protocol

Each PR was frozen at its current head SHA before substantive review. The verdict below applies only to that frozen commit. I inspected the load-bearing theorem and lemma files, exact checkers, committed test/control artifacts, workflow-only patches, dependency statements, and finite/global scope. I did not rerun any expensive special-function or zero-count computation.

Verdict meanings:

```text
VERIFIED
    The claims made at the frozen commit are correctly scoped and the
    load-bearing finite proof/checker architecture passes review.

VERIFIED WITH FIXES
    The principal mathematics passes, but a specified source-binding,
    wording, notation, artifact, or integration repair is required before
    public promotion.

GAP/BLOCKED
    The PR does not yet establish its advertised production result, or an
    integration defect prevents publication at the frozen commit.

REJECTED
    A load-bearing mathematical conclusion is false as stated.
```

A repair proposed after this review does not retroactively change the frozen-commit verdict.

## Frozen heads and verdict matrix

| PR | Frozen head SHA | Verdict | Short reason |
|---:|---|---|---|
| #113 | `73f69f12e8da3f30df6d01cb9033566897d5cfaa` | **GAP/BLOCKED** | Workflow/RUN trigger only; no retained run or mathematical result at this head. |
| #114 | `3364022e2a8d642fb129d786a2dd7e33a27ffaa3` | **VERIFIED WITH FIXES** | `L-9309` finite algebra is correct; production checker does not require immutable external source/count bindings. |
| #115 | `5780d133785cc20873b5743f4066c64219ef6aba` | **GAP/BLOCKED** | `RUN_BASIS.md` trigger only; no attached status or result at the frozen head. |
| #116 | `d7a5c3462bdee73827414448ef9144a908869359` | **VERIFIED WITH FIXES** | `L-9310` and exact LDL/radius proof pass; source provenance is echoed rather than independently checked and the full verification object is not committed. |
| #117 | `833dbd7b5ab6c51a6a4e561c589d845eb9254901` | **VERIFIED WITH FIXES** | Zero-anchor algebra/checkers pass; one existential singularity sentence is too broad and no production zero-anchor verdict is retained. |
| #118 | `208b66fa75f013ea9ce4c87c6e4d1b60c4025f4b` | **GAP/BLOCKED** | Run marker only; no result. |
| #119 | `18453b7a8953524a84d367bd3a21c6697b269e8d` | **GAP/BLOCKED** | Trigger-pattern/RUN change only; the claimed provenance repair is inherited from the base, not proved by this diff; no result. |
| #120 | `0738690fa93c8001347c9771b35439ae113b8879` | **GAP/BLOCKED** | Dual-replay marker only; no retained result. |
| #124 | `3671eef74a773e9b5867a29ba5272068c2a229d9` | **VERIFIED** | Moving-anchor one-moment, two-Schur, width, and reduced-contraction algebra all pass with correctly finite scope. |
| #125 | `016ed393cd267bef8bbb4a4bf281179d95e8d7cb` | **VERIFIED WITH FIXES** | Polynomial/slab Pick identities pass; production logical gates are evidence strings rather than digest-bound source objects. |
| #127 | `f1399457298004f0e69a60013ba6583e63f38772` | **GAP/BLOCKED** | Core Padé theorem passes, but claim ID `L-9312` collides with PR #117 and the zero-endpoint integrability hypothesis needs to be explicit. |
| #128 | `418a99c56e22002c2e8bb407fab77091fc787a4e` | **VERIFIED WITH FIXES** | Positive-anchor/Geronimus algebra passes; final candidate input is not source-authenticated and the theorem duplicates PR #124’s canonical interface. |
| #129 | `d44c80537c61dfc7961a1303fc6cb53f3e01efff` | **VERIFIED WITH FIXES** | Cross-height product and critical-point theorems/checkers pass conditionally; source digests are not checked against actual primitive files and parent product normalization must be frozen. |
| #130 | `0282a6fb051a412be1a9991ba3afb09d79c3a525` | **GAP/BLOCKED** | Checker design is sound, but the PR contains no completed moment/result artifact or status at the frozen head. |

Verdict totals:

```text
VERIFIED                 1
VERIFIED WITH FIXES      6
GAP/BLOCKED              7
REJECTED                 0
```

## Detailed findings

### PR #113 — workflow trigger

Changed files:

```text
.github/workflows/x9306-real-log-portfolio.yml
experiments/X-9306-real-log-portfolio-search/RUN.md
```

The patch adds a branch-push trigger, grants `contents: write`, and commits generated result files back to the run branch. The RUN marker explicitly asserts no sign. The mechanics are coherent, but no status or retained output is attached to the frozen head. It cannot be cited as evidence for a cone verdict.

**Required before publication:** retain the exact result and SHA ledger on a result-bearing branch, or close this trigger PR as superseded. Do not merge it as a mathematical contribution.

### PR #114 — simplicial monomial-positive cone

Files reviewed:

```text
claims/lemmas/L-9309-simplicial-resolvent-portfolio-cone.md
experiments/X-9307-simplicial-portfolio-basis/verify.py
results/tests.txt and synthetic controls
```

Verified finite algebra:

1. On distinct nodes, the zero-sum response map
   
   ```text
   beta -> -sum_i beta_i product_(j!=i)(y+u_j)
   ```
   
   is an isomorphism onto degree-at-most-`n-2` polynomials.
2. The inverse evaluation formula at `-u_i` is correct.
3. The monomial-positive cone is the image of the nonnegative coefficient orthant and is simplicial.
4. Normalization by `P(1)=1` gives a unique convex combination.
5. The minimum of a linear functional is attained on one monomial basis ray.
6. Zero-extension of a subset portfolio multiplies its response by positive-coefficient factors and embeds it into the full cone.

The exact checker recomputes the zero-sum and polynomial identities and contracts rational intervals correctly. The seven committed synthetic tests cover the central finite kernel.

**Fix required:** in `RIEMANN_XI_DIRECTED` mode, `feature_table_sha256` is optional and authenticates only the user-supplied table itself. The checker does not require the primitive, count, normalization, ordinate, or source-certificate files whose semantics make the intervals Riemann data. Production mode must require immutable external bindings and closed parent-gate identifiers. The RH interpretation remains conditional on `L-9308` and the selected count/deflation theorem.

### PR #115 — exact-basis trigger

The sole change is `RUN_BASIS.md`. Its base branch contains a workflow for the exact basis computation, but the frozen PR has no attached run/status/result. It is not mathematical evidence.

**Integration:** supersede by the retained `basis.json` result branch; do not merge the marker as a proof PR.

### PR #116 — full half-line SOS moment cone

Files reviewed:

```text
claims/lemmas/L-9310-halfline-sos-moment-closure.md
experiments/X-9308-halfline-sos-moment-closure/verify.py
results/pr103-full-cone-summary.json
tests/test_verify.py
```

Verified mathematics:

1. The univariate half-line decomposition
   
   ```text
   P(y)=sum a_r(y)^2 + y sum b_s(y)^2
   ```
   
   with the stated even/odd degree bounds is correct.
2. Positivity on the entire degree-bounded cone is equivalent to PSD of the two Hankel matrices.
3. A negative `H0` direction gives `q^2`; a negative `H1` direction gives `y q^2`.
4. The midpoint-minus-`delta I` exact LDL certificate plus a row-sum operator-radius bound is a valid robust interval proof.
5. The committed test reconstructs the reported proof digest from the inherited basis table.

**Fixes required:**

- Commit the complete generated verification object, not only a compact summary and digest.
- The checker hashes the basis file but only copies `basis_source_git_blob_sha1`, `source_certificate_sha256`, `primitive_sha256`, and `total_count_sha256` from its metadata. It does not fetch or verify those source objects. Add a typed provenance manifest and reject stale/mismatched source files.
- Preserve the exact finite scope: degree at most 14, sixteen fixed nodes, one ordinate, one atomized count profile. This is not evidence for higher degree or another table.

### PR #117 — zero-anchor extension

Files reviewed:

```text
L-9311-zero-anchor-one-moment-extension.md
L-9312-zero-anchor-conditioning-budget.md
L-9313-reduced-zero-anchor-contraction.md
X-9309 verify_zero_anchor.py and overlap checker
```

Verified mathematics:

- Zero-extension gives `b_(k+1)=a_k`.
- The degree-15 moment matrices and lower Schur threshold are indexed correctly.
- The exact square witness has value `b0-theta`.
- The reduced contraction reconstructs the same scalar from one point difference and the old moments; its closed polynomial formula and signs are correct.
- Direct/reduced interval overlap is a deterministic algebraic consistency gate.

The main checker is substantially stronger than the earlier moment checkers: it checks two nested zero primitives, normalization, scale, ordinate, functional-equation residual, nonvanishing at the zero anchor, count-window semantics, primitive identity, directed logs, and exact interval witnesses/LDL.

**Fixes required:**

- Narrow the sentence claiming that every off-critical zero creates a positive-axis singularity in the zero-anchored logarithm. A zero `beta+i gamma` produces the positive real singularity `u=(beta-1/2)^2` only when the chosen height is `T=gamma`; for an arbitrary frozen height the singularity is generally complex in `u`.
- Call the direct/reduced comparison an independent *assembly* or algebraic cross-check, not independent analytic evidence.
- No production zero-anchor verdict is retained at this frozen head; keep `O-9311` explicitly unverified.

### PRs #118, #119, #120 — zero-anchor triggers

These PRs contain only RUN markers or trigger-pattern edits. At the queried frozen heads, no status/result was attached.

Specific note on #119: the diff broadens the branch pattern and adds `RUN.md`; it does not itself contain the provenance repair described in its title/body. That repair is inherited from its base and must be reviewed and retained on the result-bearing branch.

**Disposition:** close/supersede these trigger PRs after one immutable production result is retained. They should not enter the mathematical merge order.

### PR #124 — general moving-anchor theorem

Files reviewed:

```text
L-12201-moving-anchor-one-moment.md
T-12202-moving-anchor-two-schur-completeness.md
L-12203-admissible-width-old-cone.md
L-12204-moving-anchor-reduced-contraction.md
X-12201 exact synthetic checker/tests
```

Verified mathematics:

- In the shifted coordinate `z=y+t`, zero-extension yields `c_(k+1)=L_old(z^k)` and introduces exactly one new scalar.
- Both Schur matrices, thresholds, signs, and explicit lower/upper witnesses are correct.
- The admissible-width identity is an inherited nonnegative old-cone response; strict old-cone positivity forces positive width.
- The reduced point-difference formula and its response polynomial are correct.

The claims consistently limit themselves to finite moment algebra and mark midpoint reconnaissance as empirical. No production Riemann sign is asserted.

**Integration:** merge only after #117 and the verified old-cone source. Treat this PR as the canonical general one-node extension. PR #128 should become an adapted-basis corollary/implementation rather than a parallel primary theorem.

### PR #125 — slab-complement and polynomial Pick localizers

Files reviewed:

```text
L-12101-quadratic-zero-sum-pick-contraction.md
L-12102-certified-slab-complement-pick.md
L-12103-polynomial-multislab-pick.md
L-12104-rational-sos-support-filters.md
verify_slab_complement.py and multislab controls
```

Verified mathematics:

1. The quadratic partial-fraction identity is exact.
2. Exact zero-sum cancellation removes the polynomial term and improves the resolvent packet to `O(gamma^-2)`, giving absolute convergence after the quadratic weight.
3. Exact slab counts plus saturated disjoint critical-line bins account for every in-slab zero unconditionally.
4. Under RH, subtracting the complete negative-weight slab contribution leaves a nonnegative outside-slab sum.
5. The general polynomial/moment-cancellation contraction and disjoint multi-slab sign pattern are correct.
6. The rational SOS support-filter cone is a valid sufficient cone; it does not claim completeness.

The exact checker correctly enforces exact zero sum, disjoint bins, exact multiplicity saturation, interval contraction, and the `r r*` orientation.

**Fixes required:** production `logical_gates` accept a state and any nonempty evidence string. They do not bind the `F` rectangles, slab count, endpoint-zero proof, or zero bins to immutable source objects. Require digest-bound typed evidence and exact parent claim/commit identifiers. Keep the RH consequence explicitly conditional on the reviewed `D-3201/L-3201/L-3202` normalization.

### PR #127 — support-aware Padé gate

The finite truncated-Stieltjes theorem is mathematically sound:

```text
a_k=b_(k+1)+w b_k,
H0(t)=C0+t zz^T,
HA(t)=CA-(w+A)t zz^T,
```

and the PSD intersection is the complete one-scalar interval under the stated positive-measure/support hypothesis. The variational endpoints and square/support-localized witnesses are correct.

**Frozen-commit blockers:**

1. The claim ID `L-9312` is already used in PR #117 by `L-9312-zero-anchor-conditioning-budget.md`. Merging both produces two incompatible registry entries with the same ID.
2. In the abstract `w=0,A=0` endpoint case, explicitly require that the Stieltjes integral exists and that the measure has no unremoved mass at `y=0`; otherwise `1/(y+w)` need not be integrable.
3. The PR overlaps the more general moving-anchor framework in #124 and should be rebased as a support-aware corollary after renumbering.

The mathematical core is not rejected, but the frozen PR is not mergeable as a theorem contribution.

### PR #128 — adapted positive-anchor/Geronimus interface

Files reviewed:

```text
L-9314-positive-anchor-one-moment-extension.md
L-9315-reduced-positive-anchor-contraction.md
positive_anchor.py
verify_b0_interval.py
```

Verified mathematics:

- The recurrence `a_k=b_(k+1)+w b_k` is correct.
- The adapted basis gives the displayed `C0/C1` blocks.
- Strict positivity of the old cone proves both inherited blocks positive definite.
- The lower and upper Schur thresholds and the `q0^2`, `y q1^2` witness contractions are correct.
- The reduced contraction and width budget are correct.
- The discovery code labels midpoint gates as discovery-only; the negative checker contracts fixed exact rational directions against the complete boxes.

**Fixes required:**

- The candidate `b0_interval` is accepted from a standalone JSON object and is not cryptographically bound to a new-point primitive, normalization, count profile, or precision ladder. A production negative needs a typed source manifest.
- Replace “independent overlap check” with “alternative assembly cross-check” unless a genuinely independent special-function backend is used.
- Consolidate with #124: retain #124 as the canonical shifted-coordinate theorem and present #128 as its adapted-basis/Geronimus implementation.

### PR #129 — cross-height direct-`xi` portfolios

Files reviewed:

```text
L-9801-cross-height-algebraic-direct-xi-portfolios.md
L-9802-critical-point-certificates-for-rational-cross-height-portfolios.md
X-9801 verify.py
X-9802 verify.py
```

Verified mathematics:

- Per-height zero-sum exponents cancel each height-dependent canonical-product constant and the `1/gamma` asymptotic term.
- Global nonnegativity of the one-zero quadratic-factor response implies the direct product/logarithmic inequality under RH.
- The rational critical-point criterion is complete: the response tends to zero at both infinities, and all minima occur at exhaustive derivative roots or infinity.
- The exact Sturm root counts, rational logarithm enclosures, polynomial reconstruction, and directed product/log contractions are internally sound.
- The retained Riemann-data midpoints are positive controls, not counterexample claims.

**Fixes required:**

- In production mode, the checker verifies that each `source_sha256` is syntactically a digest but does not bind it to an actual source file or its normalization/point table. Add external file-digest verification.
- Bind `L-7501` and the completed-`xi` genus-zero product normalization to an exact reviewed commit. This is the load-bearing RH implication.
- Narrow the sentence that the one-height specialization “preserves existential completeness” unless the exact two-point completeness theorem and its quantifiers are imported explicitly.

### PR #130 — degree-18 distinct-gap experiment

The checker architecture is sound:

- exact moments define the two complete Hankel tests;
- positive closure uses exact LDL of midpoint minus the complete box radius;
- NumPy is used only to nominate a direction;
- a negative is promoted only through a frozen rational vector and exact interval quadratic contraction.

However, the frozen PR contains the workflow, builders, tests, configuration, and RUN marker but no immutable moment table or verification result. No status check was attached when queried.

**Required before publication:** commit the complete directed moments, exact result, source/certificate/count digests, and precision nesting. Until then the advertised degree-18 decision has not occurred.

## Merge and integration order

### Direct-`xi` moment stack

Recommended order:

```text
parent L-9308/PR #111
-> PR #114 finite simplicial theorem
-> one authenticated basis-result branch (not trigger-only PRs)
-> PR #116 full degree-14 moment closure
-> PR #117 zero-anchor extension
-> PR #124 canonical moving-anchor theorem
-> PR #128 adapted-basis corollary/implementation
-> PR #127 only after renumbering and rebasing as support-aware corollary
```

PRs #113, #115, #118, #119, and #120 are workflow triggers and should not appear as mathematical dependencies.

### Slab/Pick stack

```text
reviewed D-3201/L-3201/L-3202 and exact zero-table dependencies
-> PR #125
```

The production checker must be source-bound before any Riemann negative can be promoted.

### Cross-height direct-`xi` stack

```text
reviewed L-7501 and PR #105 primitive normalization
-> PR #129
-> PR #130 only after its actual degree-18 result exists
```

## Connections missed by the individual PRs

The following are new observations from this review and are **PROPOSED**, not retroactive verification.

1. **One canonical truncated-Stieltjes extension theorem.** PRs #117, #124, #127, and #128 are congruent forms of the same one-node Geronimus/Markov–Padé extension. A single source theorem can own the recurrence and two affine PSD pencils; zero-anchor, moving-anchor, support-aware, and adapted-basis statements should be corollaries. This removes duplicated proofs and the `L-9312` collision.
2. **Additive/multiplicative dual candidate validation.** PR #125’s polynomial Pick localizers and PR #129’s cross-height direct-product portfolios integrate different transforms of the same hypothetical zero measure. A future candidate should be replayed through both interfaces when possible: agreement is a strong normalization and source-consistency test, though not statistical independence.
3. **Finite-to-global firewall.** PRs #116, #117, #124, #127, #128, and #130 close or test finite degree/node cones. No collection of such positive finite results proves RH without a separately proved exhaustion/compactness theorem. This gate should be explicit in every integration summary.

The proposed unification is recorded separately as `M-16301`; it does not change any frozen verdict above.

## SERIOUS RESOLUTION PATH

**No complete resolution path is established by these fourteen PRs at their frozen heads.**

They provide serious finite falsification engines and rigorous finite cone closures, but none proves that its increasing finite families exhaust an RH-equivalent global cone. The closest high-value disproof architecture is the combination of PR #125 and PR #129 over shared cross-height primitives and certified slabs.

Exact missing steps for a serious full-resolution claim are:

1. source-bind and independently review the parent RH implications:
   `L-7501`, `L-9308`, and `D-3201/L-3201/L-3202`;
2. prove an exhaustion theorem showing that any off-line zero forces a strict finite witness in an increasing declared family, **or** prove that positive finite cones converge to a known RH-equivalent global positivity criterion;
3. produce either a strict directed negative with independent primitive reproduction or a global limiting positivity theorem;
4. preserve exact finite/global quantifiers and immutable source provenance throughout.

Until an exhaustion theorem or strict negative exists, the reviewed positive closures are local exclusions, not evidence that RH is globally true.
