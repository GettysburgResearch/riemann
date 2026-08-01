# Pre-public independent review — PRs #132, #133, #134, #135, #136, #139, #140, #141, #144, #150, #152, #155, #158, #159

Reviewer: `gpt56-pro-09-m`  
Date: 2026-08-01  
Scope: frozen-commit theorem, dependency, notation, finite/global, citation, and checker review  
Status: review artifact; no merge and no RH claim

## Frozen heads

| PR | frozen head SHA | classification |
|---:|---|---|
| #132 | `5c4209e184fbac2a1c4c079f805828645594949e` | **VERIFIED WITH FIXES** |
| #133 | `7402339279f59a17baa002d68c154348a2ae8e47` | **VERIFIED WITH FIXES** |
| #134 | `74ef81273e6b670920e7683c8137bee5cdb9c3c0` | **VERIFIED** |
| #135 | `fb3085e4aca61592ef1c86f36ba3581415ba665d` | **REJECTED** |
| #136 | `0af576255f281f241c6b16f869483909bc832545` | **GAP/BLOCKED** |
| #139 | `20655e4b2b25539cf6587f4c4f3432e8ecf27fd8` | **GAP/BLOCKED** |
| #140 | `5f4df90f890615bde7762278951a8adab7f0083d` | **VERIFIED** |
| #141 | `e15c50341187b7c0e672594654ad9416b55c9ce7` | **VERIFIED** — redundant merge unit |
| #144 | `dd42bda400982e395c4102a8f66d25e2bb940e26` | **VERIFIED WITH FIXES** |
| #150 | `feefc9fa68330a9821f730d634a7b9e4001cfba0` | **VERIFIED** |
| #152 | `bad48a791146218bb2d76a0345d7b60a6d729b64` | **GAP/BLOCKED** |
| #155 | `a099d1303859f26469fc582c152c725fe74f2c81` | **VERIFIED WITH FIXES** |
| #158 | `e2b67e5ecfe3c6742086558a792fb61766a4ce4c` | **GAP/BLOCKED** |
| #159 | `0c94e4bd1997b47e0bd54027ed9e64ac9f7e97ce` | **VERIFIED WITH FIXES** |

## Review method

I reviewed only the frozen SHAs above. I reconstructed the load-bearing finite algebra, checked theorem quantifiers and finite/global boundaries, inspected representative exact checkers and retained artifacts, and checked the most important imported source interfaces against primary sources:

- Connes–Consani–Moscovici, arXiv:2511.22755v1: Proposition 5.7, Theorem 5.10, Lemma 7.3;
- Suzuki, arXiv:2606.09096v1: Corollary 1.2, Theorem 1.3, and the Fourier multiplier formulas;
- Groskin, arXiv:2607.02828: finite Guinand–Weil dictionary and archimedean tail rule;
- Platt–Trudgian, arXiv:2004.09765: rigorous critical-line/simple-zero verification through height `3*10^12`.

No expensive computation was rerun. Small exact algebra was reconstructed directly. A checker is called verified only for the finite implication it actually recomputes; external interval, zero-census, source, or normalization gates remain external unless content-bound and independently replayed.

# Per-PR findings

## PR #132 — VERIFIED WITH FIXES

### Passing claims

- `L-13201-positive-anchor-one-moment-transform.md`: the recurrence
  `a_k=b_(k+1)+w b_k`, the one-free-moment representation, opposing rank-one updates, Schur endpoints, explicit witnesses, and reduced direct-xi contraction are correct.
- `L-13202-multi-anchor-christoffel-ladder.md`: the iterated divided-difference/Christoffel construction and order invariance are correct conditional on the declared positive source measure.
- `L-13203-certified-line-mass-budget-for-anchor-ladders.md`: the positive-submeasure Christoffel lower bound and certified-zero-bin leverage accounting are correct when every bin/factor is source-bound and counted once.
- `X-12101-positive-anchor-ladder/verify.py`: exact Fraction arithmetic, exact solves, and exact LDL replay correctly verify the finite ladder algebra.

### Required fixes

1. In `L-13201`, `H_0` and `H_1` have different dimensions when `D` is even, but the statement uses one vector `z`. Replace it by dimension-specific vectors `z^(0)` and `z^(1)`. The degree-15 specialization happens to have two `8x8` matrices, so the production case is unaffected, but the general theorem is not well-typed as written.
2. `L-13201` overlaps the cleaner one-anchor theorem `L-9314` in PR #134. Choose one canonical theorem and make the other an adapter/corollary rather than maintaining two independent proof interfaces.
3. Production line-mass certificates must bind each zero bin and source factor immutably; the abstract theorem does not authorize reusing one certified mass in multiple ladder factors.

### Integration

Recommended order: #134 first as the canonical one-anchor theorem, then #132 with `L-13201` reduced to an adapter and the dimension fix applied.

## PR #133 — VERIFIED WITH FIXES

### Passing claims

- `L-9316-christoffel-pade-residual-segment-budgets.md`: the Christoffel variational identities, residual-segment upper/lower leverage bounds, monotonicity under measure enlargement, and interval arithmetic are correct.
- The exact checker correctly recomputes rational polynomial evaluations, interval products, and the final leverage budget.

### Required checker repair

`experiments/X-9312-pade-leverage-budget/verify_leverage_budget.py` accepts proof-gated segment records by status/ID but does not bind a unique source-factor allocation. The same physical residual factor can be presented under multiple record IDs and charged more than once. Before production use, add:

- immutable source-factor IDs and upstream content digests;
- an allocation manifest proving each source factor appears exactly once;
- duplicate-allocation rejection;
- explicit linkage from every gate status to the artifact whose contents were hashed.

The theorem remains verified; the current checker is a finite consumer, not a standalone production proof.

### Integration

Merge after the canonical one-/multi-anchor stack (#134 then repaired #132).

## PR #134 — VERIFIED

- `L-9314-positive-node-one-scalar-extension.md`: Geronimus recurrence, Schur interval, explicit square and `y`-times-square witnesses, and the reduced direct-xi contraction are correct.
- `experiments/X-9312-positive-node-extension/verify.py`: exact positive-definite gates, solves, endpoint witnesses, and contraction overlap are sound finite checks.
- The result is finite and conditional on the inherited direct-xi/source table; it makes no global RH inference by itself.

Use this as the canonical one-anchor theorem to avoid duplicate maintenance with `L-13201`.

## PR #135 — REJECTED

This frozen commit is only the original `X-12102` workflow trigger. The subsequent provenance audit found that the old source binding could not validate the intended Git-blob SHA-1 trust boundary, and PR #139 was opened as the repaired trigger. The frozen commit has no associated pull-request workflow run and no proof artifact.

Reject #135 as a proof/result PR and do not merge it. This rejection is operational; it does not refute the positive-anchor mathematics in #132/#134.

## PR #136 — GAP/BLOCKED

The PR contains only run markers for the cross-height direct-xi and critical-line workflows. The frozen commit has no associated pull-request workflow run and no produced certificates or verdicts. Its inherited base theorems are not established by the marker files.

The trigger text is honest, but there is nothing to verify as a result. Keep blocked until immutable workflow artifacts and their checker replays are committed.

## PR #139 — GAP/BLOCKED

This is the corrected `X-12102` trigger after the provenance repair. The marker is appropriately scoped, but the frozen commit has no associated pull-request workflow run and no PA1 result artifact. It supersedes #135 but does not itself prove a sign or a ladder gate.

Keep blocked pending the actual directed run and immutable artifact replay.

## PR #140 — VERIFIED

### Passing theorem/refutation layer

- `L-13801-saturated-sign-chain-with-endpoint-gates.md`: the saturated Hardy-Z sign chain plus exact total multiplicity and endpoint nonvanishing yields exactly one simple critical-line zero in each interval. The endpoint gates are load-bearing and correctly retained.
- `L-13802-fixed-witness-zero-accounting.md`: the fixed-witness zero-accounting implication is correctly stated as conditional on one fixed nonnegative zero expansion; it does not quantify over changing witnesses.
- `L-13803-correct-hermite-hankel-inertia.md`: correct inertia is
  `n_+=r+c`, `n_-=c`, `n_0=deg-(r+2c)`, so signature equals the number of distinct real roots. PSD iff all roots are real; PD iff all are real and simple.
- `R-13803-targeted-li-family-is-not-proved-as-stated.md`: the complex-center derivative coefficient cannot be replaced by its real part; the factor-of-two normalization correction is also valid.
- `R-13804-x5606-terminal-cell-coverage-gap.md`: the original scan omitted a terminal cell, so its global range claim was invalid.

### Computational layer

The repaired `X-5606` scanner includes the terminal cell, a complete-coverage gate, exact binary endpoint serialization, and fail-closed interval assembly. The retained result is a finite same-backend computation conditional on the imported screw normalization and certified zero census; it is not an independent RH proof.

No expensive replay was rerun in this review.

## PR #141 — VERIFIED — redundant merge unit

The corrected Hermite inertia theorem/refutation and exact rational checker independently pass. They duplicate files and claim IDs already present in #140.

Do not merge both PRs. Prefer #140 as the broader canonical audit; close or supersede #141 after confirming no unique artifact remains.

## PR #144 — VERIFIED WITH FIXES

### Passing claims

- `L-14201-localized-weil-support-onset.md`: support monotonicity follows from literal inclusion of compact smooth test spaces. The plateau geometry under false RH is correct once continuity, small-support positivity, and existence of one negative support are imported.
- Primary-source check: Suzuki arXiv:2606.09096v1, Theorem 1.3 does prove continuity of the lowest eigenvalue, and Corollary 1.2 identifies the infimum over compact smooth tests.
- `T-14201-dyadic-fir-toeplitz-equivalence.md`: the increment/zero-sum bijection, dyadic density, real/imaginary reduction, dimension nesting, and exact grid-refinement embedding are correct. The theorem is existentially complete for a finite negative witness, not a positive finite-prefix proof of RH.

### Required theorem repair

`T-14202-localized-weil-finite-element-completeness.md` states convergence along every nested refinement sequence. Nestedness alone is insufficient: a sequence may repeatedly refine only one cell and fail to be dense in `H_0^1`. Require explicitly either

- maximum mesh diameter tending to zero, or
- density of the union in `H_0^1(-a,a)`.

With that hypothesis, the proof from `H_0^1` density and boundedness of the screw operator is correct.

### Integration

Apply the mesh-density repair before using T-14202 as a semidecision theorem. Merge #144 before #152/#155, which depend on `L-14201`.

## PR #150 — VERIFIED

### Primary-source interfaces confirmed

CCM arXiv:2511.22755v1 explicitly gives:

- Proposition 5.7, including `delta_N(xi) != 0` under the even-simple hypothesis;
- Theorem 5.10: the finite transform is entire and has only real zeros;
- Lemma 7.3: the prolate candidate transforms converge uniformly on closed substrips to Xi.

### Passing claims

- `T-14301-finite-diagonal-prolate-weil-criterion.md`: the support-independent Hardy-strip estimate, moving-strip-to-fixed-strip reduction, CCM real-zero import, and Hurwitz argument are correct. It is a conditional implication; no sequence satisfying the weighted approximation is produced.
- `L-14302-weighted-resolvent-ground-state-transfer.md`: the repaired global simple-even gate, weighted resolvent estimate, unnormalized target inequality, and rational Loewner directions are correct.
- `L-14303-ambient-reciprocal-hardy-dual.md`: compression-inverse domination, constraint correction, exact direct Hardy Gram, universal floor `G >= 2I`, reciprocal `sech` kernel, and finite-support tail are correct in the declared Fourier convention.
- The exact checkers correctly verify their finite rational implications and remain explicit about external analytic gates.

### Boundary

This PR supplies a serious finite conditional route, not RH: the missing theorem is a cofinal weighted prolate-Weil approximation or the equivalent residual/coercivity asymptotic.

## PR #152 — GAP/BLOCKED

### Independently passing core claims

- `T-14302-vanishing-lower-envelope-implies-rh.md`: a cofinal rigorous lower envelope with `liminf >= 0` implies all fixed-support forms are nonnegative by support monotonicity, hence RH. The finite/global quantifiers are correct.
- `L-14308-block-temple-schur-spectral-floor.md`: the completion-of-squares bound and its scalar squared-residual specialization are correct.
- `L-14309-radical-truncation-residual-identity.md`: the abstract radical/tail identities are exact; the CCM specialization remains conditional on source/domain compatibility.
- `L-14310-prolate-logarithmic-complement-coercivity.md`: the concentration trace bound and logarithmic-head complement floor are correct as a conservative complement theorem, conditional on exact Suzuki normalization.

### Blocking integration defects

The frozen PR contains multiple incompatible files with the same claim or experiment ID:

- two `L-14312` files;
- two `L-14313` files;
- two `L-14314` files;
- two `L-14315` files;
- two `T-14303` files;
- two separate `X-14307` experiment directories.

These collisions prevent a stable public theorem ledger and obscure which source-packet theorem downstream PRs import. Several later packet claims are successive alternatives or repairs, not simultaneously verified theorems.

Required before integration:

1. allocate unique IDs and mark superseded variants explicitly;
2. choose one canonical source/radical theorem with exact source and form-domain hypotheses;
3. bind every downstream dependency to that canonical file;
4. retain T-14302/L-14308/L-14309/L-14310 as separately verified conditional claims;
5. do not present finite low-block experiments as the cofinal lower envelope.

## PR #155 — VERIFIED WITH FIXES

### Passing claims

- `L-14316-fourier-density-bathtub-floor.md`: the probability-density cap, bathtub lower bound, trace/count corollaries, and directed cell formula are correct.
- `L-14317-packet-leverage-bathtub-floor.md`: the projection leverage cap, Gram formula, constant-packet specialization, and packet-complement floor are correct.
- `T-14305-lower-tail-symbol-envelope-implies-rh.md`: the cofinal implication is correct conditional on an exact complete Suzuki multiplier and a symbolic `liminf` proof.

### Required artifact repair

`X-14310-packet-leverage-floor/verify.py` accepts a production tail gate and packet gate by status plus a 64-character digest, but it does not fetch or content-verify the referenced artifacts. A syntactically valid digest string is not proof of the symbol bound or packet provenance.

Before production use, bind the actual source blobs/certificates and recompute their hashes, or clearly classify the checker as a consumer of external trusted gates rather than a standalone verifier.

No production Suzuki packet-leverage floor or cofinal symbol envelope exists at this frozen head.

## PR #158 — GAP/BLOCKED

### Passing finite/composition layer

- `T-15117-coupled-window-readout-target-preservation.md`: the explicit coupled readout schedule and equivalence between readout decay and complete-window body decay are correct conditional composition statements. It explicitly leaves `b_M -> 0` and `r_M(r) -> 0` open.
- `L-15141-source-bound-singular-seam-quartic-row.md`: the finite matrix chain, basis invariance, realized quartic jet, Schatten-four expression, and directed target row are correct once a complete source package is supplied.
- `L-15142-singular-boundary-space-collapse.md`: the dense-core argument is correct under the manuscript's displayed equality defining `G_R`; if the manuscript intended another trace restriction, that missing condition must be stated.
- `X-15120` correctly fails closed rather than inventing missing source data.

### Blocking facts

- The public source audit reports **17 missing source fields** and preserves `SOURCE_SPECIFICATION_INCOMPLETE`.
- No actual first-window quartic row is determined by the public package.
- The two complete-window body limits in T-15117 remain open.
- The PR contains 245 changed files spanning many successive proposals, refutations, and superseded routes; the current title overstates the frozen result.

Before public integration, split the durable abstract/finite theorems from the incomplete production chain, retain the source-incomplete verdict verbatim, and require the missing source package before any target-preservation or RH conclusion.

## PR #159 — VERIFIED WITH FIXES

### Passing claims

- `L-15304-zero-evaluation-obstruction-to-full-packet-repair.md`: the Hardy evaluation bound, radical zero identity, finite-subspace distance obstruction, and near-kernel/visible split are correct. This is an obstruction/refinement, not a positivity theorem.
- `L-15305-certified-zero-gram-tail-floor.md`: the known-line-zero Gram minus absolute omitted-zero budget gives the stated finite visible-block lower floor, conditional on a complete proof-grade zero block and a strip-uniform tail envelope. Groskin arXiv:2607.02828 confirms the exact finite Guinand–Weil dictionary; the omitted-zero budget is a separate obligation from the archimedean cutoff budget.
- The exact rational checker correctly verifies the finite Gram/singular-value implication and explicitly labels the zero identities and Hardy bounds as external gates.

### Required fixes/dependencies

1. `L-15303-growing-hermite-radical-packets.md` depends on the Gaussian radical-tail theorem in #152. It must cite the single canonical post-cleanup claim ID and restate the exact form-continuity/source normalization used for the uniform cross-tail bound.
2. The X-15302 certificate uses booleans for the certified-zero and common-metric gates. Bind the actual zero manifest, normalization, evaluation intervals, and metric certificate by content hash if the artifact is to be proof-producing.
3. Merge only after #152's duplicate IDs and source theorem are resolved.

# Merge and integration order

Recommended order for the reviewed stack:

1. **#134** — canonical one-anchor finite theorem.
2. **#132 repaired** — multi-anchor and line-mass layer; demote/adapterize duplicate L-13201.
3. **#133 repaired** — source-allocation-safe leverage budget.
4. **#140** — canonical screw/Hermite audit; do not separately merge duplicate #141.
5. **#144 repaired** — support geometry, dyadic criterion, and dense finite-element semidecision.
6. **#150** — finite diagonal positive criterion and weighted finite adapters.
7. **#152 after ID/source cleanup** — retain T-14302 and the block lower-floor core.
8. **#155 repaired** — ambient and packet-leverage complement floors.
9. **#159 repaired** — zero-evaluation split and finite visible-block floor.
10. **#158 only as a split research ledger** until its 17-field source package and body limits are closed.

Close/supersede #135. Keep #136/#139 blocked until real workflow artifacts exist.

# PROPOSED CONNECTIONS — pending independent review

These are integration observations, not retroactive verification or new proved theorems.

1. **Christoffel/Geronimus chain.** PRs #134, #132, and #133 are one coherent stack: one-anchor Geronimus extension -> multi-anchor Christoffel ladder -> source-allocated residual leverage budget. Canonicalizing this chain removes duplicate proof interfaces and makes the PA1 workflow auditable.
2. **Hardy RKHS duality.** PR #150's reciprocal-Hardy residual upper bound and PR #159's certified-zero evaluation lower obstruction use the same evaluation RKHS. The natural packet split is therefore a generalized singular-value split in the Hardy metric, not an ordinary Euclidean SVD. This should feed directly into #155's leverage cap.
3. **Dual semidecision ledgers.** PR #144 supplies an existentially complete finite negative-witness search; #155/#159 supply finite lower-floor components. Running both on one source-normalized support/mesh ledger would prevent finite-compression positivity from being confused with ambient positivity.

# SERIOUS RESOLUTION PATH

**YES — a serious conditional architecture is present, but no reviewed PR resolves RH.**

The most coherent route is the cofinal lower-envelope program:

1. use `T-14302` to reduce RH to rigorous localized lower floors tending to zero from below;
2. use #155 to certify the infinite/ambient complement after a finite low packet is selected;
3. use #159 to split that packet into a certified-zero near-kernel and an evaluation-visible block;
4. use exact radical truncations only on the near-kernel, and certify the visible block by `L-15305`;
5. combine all blocks and cross maps with `L-14308`, including complete directed assembly errors;
6. prove the resulting floor has negative part tending to zero on an unbounded support sequence.

The exact unresolved steps are:

- canonical, source-bound production of the complete Suzuki/Weil symbol and packet at growing supports;
- a uniform capture/conditioning theorem showing the chosen radical packet spans the certified-zero near-kernel with form-norm tails and cross maps tending to zero;
- a strip-uniform omitted-zero bound small enough relative to the visible evaluation Gram, without assuming RH or omitting a possible off-line zero;
- a cofinal complement floor and complete Schur/cross-error budget with a symbolic rate;
- cleanup of #152's claim-ID/source dependencies so every theorem in the chain names one immutable object.

A second serious route is #150: prove the weighted finite prolate-Weil approximation in `T-14301` along one diagonal sequence. Its implication theorem is verified, but no asymptotic approximation theorem is presently available.

Neither route should be advertised as a proof proposal ready for public resolution until its listed asymptotic/source steps are supplied.