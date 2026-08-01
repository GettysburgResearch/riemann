# Pre-public independent review — PRs #80, #82, #85–#92, #94, #96–#98

Reviewer: `gpt56-03-review`  
Date: 2026-08-01  
Review branch: `agent/gpt56-03-r/207-directed-d0001-frame`  
Frozen-head ledger: `reports/gpt56-03-review/2026-08-01-pre-public-pr80-98-freeze.md`

## Review method and status boundary

Each verdict below applies only to the frozen head SHA recorded in the first table. I inspected the load-bearing claims, finite/global quantifiers, dependencies, proof boundaries, checkers, source bindings, and retained artifacts. I did not rerun any expensive computation. Small exact algebra checks and static code audits were used where necessary. GitHub Actions was queried for the four trigger-only heads; none had a workflow run associated with the frozen commit.

`VERIFIED` means the reviewed contribution is correct within its explicitly stated finite or conditional scope. `VERIFIED WITH FIXES` means the core mathematics passes but an identified pre-public repair is required. `GAP/BLOCKED` means at least one load-bearing theorem, production hypothesis, or result artifact is absent or unsupported. No proposed repair below retroactively changes the frozen verdict.

## Frozen heads

| PR | Frozen head SHA |
|---:|---|
| #80 | `724ba6621bcf864ffbf2f25680074198be618ea5` |
| #82 | `293b4491ec3b59a4e75cd80c811ae69f6625c899` |
| #85 | `655a3656a7265f36c6845bd00c02058e369037be` |
| #86 | `25eae2dc8dec99d74e5a7bdea577367dd6ad02d8` |
| #87 | `a374379b7adcac44f16462b9f75238c81a45b11d` |
| #88 | `20b73402aef153ca543c285d3df8d5c07ffb58eb` |
| #89 | `9119a43e308a2593b0c66efab0e69102e0bbac08` |
| #90 | `d00b50b4c199facf49062f0d8b7635a3e2768ae4` |
| #91 | `7d69b64186d672a5fbe71f956fb1a0471eebb6e9` |
| #92 | `eece42cf8aef93c82c3e8f63e09b048c7bca2abf` |
| #94 | `64a122219dea18e14564502cabc4b566dbb3c4f1` |
| #96 | `9f385eca9aaf2bacfca3c09a5acd53a3f68ef6ce` |
| #97 | `55d9333954f86c3d35af8a38fe9f5bc79d099c6b` |
| #98 | `2f012ebd4bd782f0ba93a6ecc4f98f62b262be20` |

## Verdict matrix

| PR | Classification | Short reason |
|---:|---|---|
| #80 | **VERIFIED WITH FIXES** | Exact full-complex Pick contraction and equal-cost refinement theorem pass; the finite checker does not bind the primitive Arb artifact and common point metadata strongly enough. |
| #82 | **GAP/BLOCKED** | Several finite algebra and normalization claims pass, but the global binary80/binary128 moat is a hand-audited operation ledger rather than a source-derived or independently directed proof, and no production `K=1024` result exists. |
| #85 | **GAP/BLOCKED** | `L-8501`–`L-8504` pass; the fast source still inherits the unclosed floating ledger, and the complete coefficient, complement, residual, and circulant artifacts are absent. |
| #86 | **GAP/BLOCKED** | Trigger-only PR; no workflow run or proof-bearing artifact at the frozen head. |
| #87 | **VERIFIED WITH FIXES** | The zero-slab discrepancy theorem and producer architecture pass, but endpoint semantics must be corrected or independently certified. |
| #88 | **VERIFIED WITH FIXES** | Log-modulus Cauchy-Gram total positivity and the four-point existential witness pass; the production checker must bind one common ordinate and primitive direct-`xi` artifact. |
| #89 | **VERIFIED WITH FIXES** | Rank-two Green algebra and robust first-cell theorem pass; D-0801 normalization/admissibility and the actual complete background moat remain external and must be stated as such everywhere. |
| #90 | **VERIFIED WITH FIXES** | Scalar, fixed-vector, and matrix zero-bin deflation lemmas pass; checker trusts a declared external gate/hash instead of replaying the zero-count and primitive evidence. |
| #91 | **GAP/BLOCKED** | Finite off-lattice and Legendre–Bessel formulas pass, but `L-3602` incorrectly treats the fixed-band archimedean form as a bounded operator; its global Ritz/completeness proof requires a missing form-core theorem. |
| #92 | **GAP/BLOCKED** | Trigger-only PR; no workflow run or result at the frozen head. |
| #94 | **GAP/BLOCKED** | Trigger-only PR; no workflow run or result at the frozen head. |
| #96 | **VERIFIED WITH FIXES** | Zero-deflated direct-`xi` modulus theorem and exact finite checker pass; zero evidence and common direct-`xi` primitive provenance are not independently replayed. |
| #97 | **GAP/BLOCKED** | Trigger-only PR; no workflow run or result at the frozen head. |
| #98 | **VERIFIED** | Suzuki screw normalization, prime-knot convexity, finite negative-type/Gaussian/FIR/deflation theorems, and the positive directed Toeplitz control pass within their stated scope. No negative Riemann witness is claimed. |

No assigned PR is classified `REJECTED`. PR #91 contains a rejected global argument, but its substantial finite formulas remain valid; the appropriate whole-PR verdict is therefore `GAP/BLOCKED` rather than rejection.

---

## PR-by-PR findings

### PR #80 — full-complex Pick audit

**Verified claims.**

- `claims/lemmas/L-6602-full-complex-pick-fixed-vector-contraction.md`: for
  \[
  K_{ij}=\frac{F_i+\overline{F_j}}{z_i+\overline z_j},
  \qquad
  h_i=\sum_j\frac{v_j}{z_i+\overline z_j},
  \qquad
  c_i=2\overline v_i h_i,
  \]
  the identity
  \[
  v^*Kv=\operatorname{Re}\sum_i c_iF_i
  \]
  has the correct conjugations and sign.
- `L-6603`: selecting the largest pointwise uncertainty contributions is optimal under the theorem's actual hypotheses—one fixed vector, equal refinement costs, and predetermined pointwise shrink factors.
- `verify_full_pick_vector.py`: signed-int64 decoding, exact denominator reconstruction, rectangle intersection, and rational contraction are sound.

**Required fixes.** The checker verifies the vector and final interval hashes but does not cryptographically bind the supplied primitive point table to the named Arb artifact, producer source, backend version, or exact common grid metadata. Add a primitive-table canonical digest, exact point/ordinate manifest, and source/backend bindings. Preserve the finite conclusion: one exact vector is positive; the full matrix is not certified PSD.

### PR #82 — fast midpoint carrier producer

**Verified subclaims.**

- `L-2815` and `L-2816`: segment-centered logarithm and reciprocal-square-root truncation identities and remainders.
- `L-2817`: phase-grid assignment/fallback logic as a finite theorem.
- `L-2820`, `L-2821`, and `L-2822`: exact interval composition, autocorrelation-manifest algebra, and the independent directed-producer comparison interface.
- `T-2819`: the transform, admissibility, signs, pole term, prime coefficient, and absolute zero-sum convergence of the D-0801 Guinand–Weil dictionary are internally consistent with the located finite Guinand–Weil source.

**Blocking point.** `L-2818`'s target-wide moat ultimately depends on a hand count of the binary80/binary128 straight-line operations. `verify_fast_budget.py` proves exact arithmetic after accepting that per-term allowance; it does not establish that `fast_prime_shard.cpp`, a compiled binary, or the target host follows the ledger. The PR itself correctly says the production `K=1024` run is pending. Before integration, require either a mechanically source-derived floating-error certificate or an independent fully directed containment run over every operation class, together with source/binary/compiler/ABI hashes.

### PR #85 — whole-matrix closure and hybrid coefficient source

**Verified subclaims.**

- `L-8501`: Hermitian circulant completion and principal-submatrix interlacing.
- `L-8502`: one-direction Schur repair. The coarse targets have exact surplus
  \[
  \frac1{4000}\left(\frac7{1000}-\frac1{1000}\right)
  -\left(\frac1{5000}+\frac1{1000}\right)^2
  =\frac3{50{,}000{,}000}>0.
  \]
- `L-8503`: the Hermitian Toeplitz coefficient-to-operator estimate has no hidden factor `K`.
- `L-8504`: the rational inverse-Cholesky/congruence row-sum criterion is valid.
- `merge_hybrid_source_strict.py`: the strict layer usefully binds the budget self-hash, producer Git blob, parameter fingerprint, normalization fingerprint, coverage, and source counts. The apparent `cells+1` autocorrelation issue is benign because the retained terminal autocorrelation is exactly zero and the matrix has 1,024 actual lag coefficients.

**Blocking point.** `L-8505` inherits PR #82's unclosed floating ledger. The source plan explicitly is not a completed coefficient artifact, and there is no completed hybrid source, repaired-complement certificate, residual certificate, or circulant completion. Even successful finite closure would settle only the declared finite D-0801 matrix.

### PR #86 — circulant workflow trigger

The only changed file is `experiments/X-8201-circulant-completion/RUN_TRIGGER.md`. It explicitly makes no sign claim. No workflow run is associated with frozen head `25eae2d…`; therefore there is no result to review or merge as evidence.

### PR #87 — exact zero-slab discrepancy

**Verified claims.**

- `L-5605`: `N(a,b)-N_0(a,b)` exactly counts off-critical zeros with multiplicity; in a positive-ordinate slab it is even.
- Sign changes alone do not count even-multiplicity line zeros.
- The finite converse from any off-line zero to rational zero-free slab endpoints is valid.
- `flint_line_gap_discrepancy.c` correctly freezes the target, obtains consecutive Hardy-Z balls, constructs exact dyadics between them, calls rigorous total-zero counts, and rejects negative or odd positive discrepancies.

**Required endpoint repair.** FLINT's documented `acb_dirichlet_zeta_nzeros` convention counts zeros with multiplicity in `0 < Im(s) <= T`. Isolation of a unique integer does not itself prove that `T` is not a zero ordinate. The frozen producer's comment claiming otherwise is unsupported. Either:

1. independently certify both exact endpoints zero-free and retain the open-slab theorem; or
2. rewrite the certificate and discrepancy theorem with the exact half-open `(a,b]` convention and allocate endpoint line multiplicity consistently.

Also bind the precise FLINT version and the documented semantics of the Platt consecutive-zero routine. This is a pre-public fix, not a refutation of `L-5605`.

### PR #88 — logarithmic direct-`xi` modulus total positivity

**Verified claims.** Under RH, the genus-zero product

\[
H_T(u)=C_Tu^{m_0}\prod_a(1+u/a)^{m_a}
\]

gives

\[
\frac{\log(u+a)-\log(v+a)}{u-v}
=\int_0^\infty\frac{dt}{(u+a+t)(v+a+t)}.
\]

This is a Cauchy Gram kernel. Andreief's identity and the Cauchy determinant establish nonnegative cross minors for two increasing positive node lists. The interlaced four-point pattern near an off-line zero has determinant

\[
-\frac{(2m\log2)^2}{h^2}+O(h^{-1})<0,
\]

so the family is existentially complete for a finite directed disproof.

`verify_log_loewner.py` uses sound rational logarithm and determinant enclosures.

**Required fixes.** A Riemann certificate must bind every point to one exact real ordinate `T`; the checker currently sees only `u` and modulus intervals. It must also bind the direct-`xi` primitive table, producer source, backend, and normalization artifact. Synthetic controls remain exact; no actual negative Riemann row exists.

### PR #89 — endpoint Green first-cell theorem

**Verified claims.** `L-8301`'s two-dimensional generalized endpoint operator has the stated determinant and eigenvalues; `L-8302`'s residual-enclosed endpoint solves are sound; `T-8301`'s positive and negative operator-moat inequalities have the correct directions; `L-8303`'s coherent corner aggregation and concavity/endpoint reduction are valid.

**Required fixes / scope.** Every theorem statement and future artifact must preserve that the D-0801 first-cell formula, Guinand–Weil normalization, left matrix floor, and complete background operator norm are external hypotheses. There is no actual directed threshold-cell certificate in the frozen PR. The finite theorem is verified; any RH consequence remains conditional on the full D-0801 analytic stack.

### PR #90 — certified critical-line zero deflation

**Verified claims.** `L-8401`'s Poisson lower subtraction, `L-8402`'s fixed-vector Pick subtraction, `L-8403`'s matrix repair

\[
g(\gamma)g(\gamma)^*\succeq g(c)g(c)^*-(2G+\eta)\eta I,
\]

and `L-8404`'s Hardy-Z sign-change lower count are correct. The `Fraction` checker correctly handles finite complex intervals and deflated contractions.

**Required fixes.** The checker accepts a JSON gate state and copied evidence hash; it does not replay or bind the actual zero-count proof or primitive `F` artifact. Replace this with an immutable endpoint-safe zero-measure ledger and primitive-table digest. The strict synthetic examples are valid but are not Riemann data.

### PR #91 — off-lattice sinc and confluent Legendre carriers

**Verified finite content.** `L-3601`'s sinc Gram, product transform, finite prime block, pole block, and cancellation-safe compact archimedean entries pass. The Legendre–Bessel formula, identity coefficient Gram, overlap kernel, parity, recurrence, and finite projections in `L-3602`–`L-3604` also pass.

**Load-bearing global gap.** `L-3602` claims the compact archimedean form defines a bounded self-adjoint operator on the complete fixed-band Paley–Wiener space and uses ordinary `L2` density for continuum Ritz convergence. This is false. For unit-norm fixed-band sinc translates `F_A(x)=b_\Delta(x-A)`,

\[
\int\left(\operatorname{Re}\psi(1/4+ix/2)-\log\pi\right)|F_A(x)|^2dx
\sim\log A\to\infty.
\]

The correction is preserved separately as `R-20804`. A valid global theorem needs a semibounded closed quadratic form, a declared form domain, and proof that the finite Legendre–Bessel union is a form core. Until then, finite negative witnesses remain valid, but the stated continuum completeness/Ritz conclusion is blocked.

### PR #92 and PR #94 — gap workflow triggers

Each frozen PR contains only a marker file intended to trigger the base workflow. Neither frozen head has an associated workflow run. The marker language is honest; there is simply no total-count, Hardy-Z, discrepancy, or cross-precision artifact to review.

### PR #96 — zero-deflated direct-`xi` modulus

**Verified claims.** With a certified line-zero bin and

\[
B_r=\max((T-a_r)^2,(T-b_r)^2),
\]

the residual kernel identity

\[
K_y(u,v)-K_B(u,v)=\int_y^B\frac{ds}{(u+s)(v+s)}
\]

is positive. Complete monotonicity, cross-minor total positivity, the division-free two-point inequality, and survival of the off-line logarithmic singularity are correct. The finite checker arithmetic is sound.

**Required fixes.** As in PRs #88 and #90, the checker must replay or cryptographically bind the zero evidence, common ordinate, direct-`xi` primitive table, source, backend, and normalization. The synthetic strict separation is exact; no Riemann negative exists.

### PR #97 — zero-deflated direct-`xi` trigger

The sole file is a workflow marker. No run is associated with frozen head `55d9333…`; hence no gap-count or direct-`xi` artifact was produced at this commit.

### PR #98 — Suzuki screw prime-knot route

**Verified claims.** The located Suzuki source supports the normalization `Psi=-g_zeta` and the RH implications used by the branch. Independently checked finite results include:

- `D-9501`'s explicit prime-power formula and screw sign convention;
- `L-9503`'s smooth series, derivatives,
  \[
  A''(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}},
  \]
  plastic-constant threshold, exact lower bound
  \[
  A''(\log2)=\frac5{3\sqrt2},
  \]
  strict cell convexity, stationary-point classification, and cancellation-resistant recurrence;
- `L-9501`'s anchored PSD, conditional negative type, Hilbert metric, and three-value determinants;
- `L-9502`'s Schoenberg Gaussian transfer and explicit Taylor moat;
- `L-9504`'s complete zero-sum FIR cone, increment Toeplitz parameterization, zero-spectrum Gram, and exact prime-resonance derivative jump;
- `L-9505`'s zero-bin Loewner repair, fixed-vector subtraction, and two-sided tail box;
- `X-9502`'s exact FIR/autocorrelation contraction and manifest recount.

The retained directed Toeplitz row is strictly positive and therefore excludes one finite vector only. The branch repeatedly states that no finite positive scan proves RH and no counterexample is claimed. I found no pre-public mathematical blocker in this frozen PR.

---

## Integration and merge-order concerns

GitHub mergeability is not mathematical readiness. The recommended dependency order is:

1. **Endpoint-safe zero ledger first.** Repair PR #87's endpoint semantics and export a counted zero-measure primitive. The proposed common interface is `O-20804`.
2. **Zero consumers afterward.** PR #90 may consume that ledger for Pick/scalar deflation; PR #96 should stack on the reviewed PR #88 theorem and PR #90/zero-ledger interface; PR #98's optional zero deflation should consume the same ledger rather than a parallel table.
3. **Direct-`xi` base before deflation.** PR #88 precedes PR #96; PR #97 is only a trigger and has no evidentiary value without an artifact.
4. **Carrier source before closure.** The finite mathematics of PR #82 may be integrated separately, but its production midpoint moat must be repaired before PR #85 treats fast shards as proof-grade. PR #85 then still needs the complete coefficient, complement, and residual artifacts. PR #86 follows only as a trigger/result carrier.
5. **Off-lattice finite/global split.** PR #91 may integrate its finite formulas only after removing or explicitly blocking the bounded-operator/Ritz paragraph. The continuum theorem needs a new form-core proof and must remain separate and proposed.
6. **Independent route.** PR #98 does not depend on the carrier or direct-`xi` stacks and may be reviewed/integrated independently.

## Connections other contributors missed

### Shared certified-zero measure

PRs #87, #90, #96, and #98 need the same expensive arithmetic fact in different forms. `O-20804` proposes one endpoint-safe, multiplicity-aware ledger that records both total and critical-line counts. A positive discrepancy nominates an off-line zero; a zero discrepancy exports exact finite positive line mass for all three deflation routes. This reduces duplicate computation while increasing cross-checkability. The proposal is new and remains `PROPOSED`; it does not repair the frozen PRs.

### Scalar-first search ordering

PR #98's prime-knot scalar table should be the first consumer of any very large complete prime-power manifest. Once a directed `Psi` table exists, the scalar sign, three-value metric defects, FIR Toeplitz forms, Gaussian witnesses, and zero-deflated residuals all reuse it. This is substantially cheaper and more audit-friendly than recomputing separate huge-phase carrier tables.

### Finite witness duality

PRs #80/#90 test the logarithmic derivative, PRs #88/#96 test direct completed-`xi` modulus values, and PR #98 tests the screw function. These are not interchangeable numerical features, but all support small exact fixed-vector or determinant consumers. A candidate that appears in more than one family should be escalated immediately because the primitive and normalization failure modes are largely independent.

## SERIOUS RESOLUTION PATH

**YES — a serious exact path is present, but it is not a completed proof or counterexample.**

The cleanest path in this review set is PR #98's scalar Suzuki screw programme:

\[
\Psi(t)=-g_\zeta(t),
\qquad
\text{RH}\Longleftrightarrow\Psi(t)\ge0\text{ for all real }t
\]

under the located source normalization. `L-9503` reduces every finite interval to prime-power knots and at most one monotone stationary point per cell, with a recurrence designed for directed streaming. This removes huge phases, eigensolver conditioning, and division by `xi` from the primary decision problem.

The exact missing steps are:

1. complete a second independent source-level reconstruction of Suzuki's normalization and the stated RH equivalence;
2. build an immutable, duplicate-free prime-power manifest and a proof-producing directed recurrence with independent checkpoint reconstruction;
3. obtain either:
   - one strict finite negative cell/value, followed by an independent arithmetic producer and source audit; or
   - a symbolic cofinal lower theorem covering every cell beyond arbitrary finite cutoff;
4. bind every decisive artifact to source, compiler/backend, constants, and exact endpoint conventions;
5. for a positive resolution, supply the genuinely global cofinal lower bound—arbitrarily long finite positive scans are insufficient.

The most direct counterexample route is PR #87: a positive exact total-minus-line discrepancy in one endpoint-safe slab would immediately disprove RH. It presently lacks a completed workflow artifact and requires the endpoint fix above.

No reviewed PR currently proves or disproves RH. The serious path assessment means the repository has exact, independently checkable decision interfaces whose remaining obligations are sharply stated—not that the finish line has already been crossed.

## Final pre-public recommendation

- Preserve PR #98 as the strongest fully reviewed contribution in this set.
- Apply the listed fixes before presenting PRs #80, #87–#90, and #96 as proof-producing consumers.
- Do not present PRs #82, #85, #86, #91, #92, #94, or #97 as completed proof results.
- Keep all finite-positive conclusions explicitly finite.
- Keep every RH implication conditional on its named analytic normalization until the dependency has itself passed review.
