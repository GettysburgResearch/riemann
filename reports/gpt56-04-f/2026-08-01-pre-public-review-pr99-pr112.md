# Pre-public independent review: PRs #99–#112

Reviewer: `gpt56-04-f`  
Review date: 2026-08-01  
Scope: frozen-commit theorem, checker, artifact, dependency, and integration review  
Status boundary: this report verifies only the claims expressly classified below. It does not merge any PR and does not claim RH or a counterexample.

## Frozen heads

Every PR was frozen at the following head before substantive review. Later pushes are outside this report.

| PR | Frozen head SHA |
|---:|---|
| #99 | `73f4af75611ee1586571055fea245fab1a17b781` |
| #100 | `becaa934f59cde17a7e54275a0bab367d901face` |
| #101 | `0db1cd04fa6899c848c1c3f4a5c3e2ce2eedd260` |
| #102 | `4e5d08488b287286bb93c4a917c3ab37587331f7` |
| #103 | `272e0afac5190ecf06517438e828e33a68b3b76e` |
| #104 | `109adb084cbbb6d68b426d65322dbb5b9ac0a3c7` |
| #105 | `a587dff2e06980a5dca7867e56965bd9abf88730` |
| #106 | `7cd5584733ba0a3fca49639b9acd9a8c1faa2b1c` |
| #107 | `2345b4e2db852b892256527be8310d378fea48e8` |
| #108 | `f087d51cf906e0c36e4a57174bf044948bcd54fe` |
| #109 | `0553db2ebce80358b90de00bcf1bdf98b62c0546` |
| #110 | `f7dcf53b077108835adec35dd3518229935e7505` |
| #111 | `c992a15b099367f9fa5f149beec2732ef42a55b1` |
| #112 | `65220c068f80dcf7d9df111e77c211e2ef22ee8a` |

## Review method

I reviewed the frozen theorem and lemma texts, exact checker logic, source-binding rules, retained result summaries, dependency graph, and finite/global claim boundaries. I did not rerun the large FLINT/Arb or direct-`xi` computations. Small checks were limited to exact algebra, sign conventions, multiplicity logic, interval formulas, and static inspection of the standard-library checkers and producers.

`VERIFIED` means the frozen contribution is sound in its declared scope. It does not mean that expensive source artifacts were independently recomputed. `VERIFIED WITH FIXES` means the core theorem or finite result survives, but the listed changes are required before public integration. `GAP/BLOCKED` means a load-bearing dependency or semantic gate is not contained in the frozen PR. `REJECTED` would mean the central claim is false; no assigned PR received that classification.

## Shared dependency findings

### Direct completed-`xi` analytic base

The core horizontal-modulus construction inherited from `L-7501` is sound: under RH the even entire function descends to a genus-zero product in the squared horizontal coordinate, with nonnegative factor locations and the correct multiplicities. The off-line-zero local singularity also gives the advertised existential negative witness.

The positive integral identity used by `L-7504` is sound, but the pre-#105 parent displayed a sign-inconsistent finite-R antiderivative. PR #105 contains the corrected display. This is a local proof repair rather than a failure of total positivity, but every branch frozen before that repair must integrate the corrected parent before publication.

### Conditionality and global scope

All negative-witness implications are conditional in the correct direction:

- total zero counts are unconditional;
- converting those counts into removable **critical-line** mass is explicitly made under RH;
- a strict directed violation then contradicts RH;
- a finite collection of nonnegative rows proves only those rows or the explicitly described finite cone, never RH.

No reviewed PR turns a finite positive scan into a global RH conclusion.

### Checker trust boundary

The strongest checkers use exact `Fraction` arithmetic after source production and recompute interval contractions. Several earlier checkers validate SHA strings and semantic labels syntactically but do not themselves load the source artifact named by the digest. Those checkers remain valid finite consumers, but a public production verdict must be emitted by the source-bound builder or wrapper, not by hand-populating the JSON schema.

## Classification summary

| PR | Classification | Core reviewed object | Required action / boundary |
|---:|---|---|---|
| #99 | **VERIFIED** | `X-9301/RUN_PR71.md` workflow trigger | Operational marker only; no theorem. Do not preserve as a scientific merge artifact. |
| #100 | **VERIFIED WITH FIXES** | `L-9303`; `X-9302` exact count-deflation consumer/producer | Integrate corrected `L-7504`; clarify open/closed endpoint convention in prose. |
| #101 | **VERIFIED** | `X-9302/RUN_PR71.md` workflow trigger | Operational marker only; no theorem. |
| #102 | **VERIFIED** | second `X-9301/RUN_PR71.md` trigger | Operationally supersedes #99; do not merge both marker histories. |
| #103 | **VERIFIED WITH FIXES** | `L-9306`, `L-9307`; shifted and atomized count-deflation results | Rebase/cherry-pick unique work onto the hardened #105 line; do not blindly merge divergent duplicate paths. |
| #104 | **VERIFIED WITH FIXES** | `L-9304-overlapping-interval-count-envelope`; `X-9303` | Rename claim ID before integration; use corrected analytic parent. |
| #105 | **VERIFIED** | hardened `L-7504/L-9301/L-9303/L-9304`; guarded zero blocks; directed PR71 scans | Preferred hardened core. Finite results are positive/no-candidate only; independent reproduction remains necessary for any future negative. |
| #106 | **VERIFIED** | `X-7503` 130-decimal precision-ghost repair | Correctly classified EMPIRICAL; refutes only the rounded-string negative nomination. |
| #107 | **VERIFIED WITH FIXES** | selected-factor deflation `L-9304`; normalized-minor theorem `L-9305`; exact checker | Rename both colliding claim IDs; bind production primitives and zero gates to loaded source artifacts; tighten one dependency sentence. |
| #108 | **VERIFIED WITH FIXES** | `L-9701` saturated sign-chain isolation; `X-9304` | Update stale PR/body references to `L-9701`; retain builder/source files as the production trust boundary. |
| #109 | **VERIFIED WITH FIXES** | witness-adapted count dual `L-9305`; exact primal/dual checker | Rename colliding claim ID; source-bind primitive/count artifacts in production wrapper. |
| #110 | **VERIFIED WITH FIXES** | `L-9702`, `L-9703`; support-gap chord and Hausdorff consumers | Update stale IDs; state the finite-measure/convergence justification explicitly; source-bind support gates. |
| #111 | **VERIFIED WITH FIXES** | `L-9308` resolvent-polynomial portfolio theorem | The theorem is sound, but the checker needs three mandatory production fixes listed below. |
| #112 | **GAP/BLOCKED** | directed 15-row basis replay over the #103 table | Arithmetic replay is internally sound, but the cone-closure conclusion depends on open PR #114 (`L-9309`) plus repaired #111 and the final source-bound integration. |

Counts: 5 `VERIFIED`, 8 `VERIFIED WITH FIXES`, 1 `GAP/BLOCKED`, 0 `REJECTED`.

## Per-PR findings

### PR #99 — VERIFIED

The frozen diff is only the workflow-run marker `experiments/X-9301-zero-deflated-xi-modulus/RUN_PR71.md`. It makes no mathematical or computational-result claim. It is safe as an operational trigger, but should be dropped or squashed rather than merged as research content.

### PR #100 — VERIFIED WITH FIXES

**Reviewed:**

- `claims/lemmas/L-9303-total-zero-count-deflation.md`
- `experiments/X-9302-total-count-zero-deflation/verify_total_count_deflation.py`
- `build_pr71_total_count_certificate.py`
- `flint_pr71_nested_total_counts.c`

The theorem correctly uses nested **total** zero-count lower bounds and postpones conversion to critical-line factor mass until the RH hypothesis is assumed. The order-statistic/shell argument is multiplicity-aware, the residual Stieltjes measure is positive, and the two-point and cross-Loewner conclusions follow.

The consumer uses exact rational intervals, exact logarithm enclosures, and exact determinant contraction. The producer binds the direct-`xi` scale and the exact integer count gates. Before integration, import the corrected `L-7504` display from #105 and say explicitly whether endpoint counts are open, closed, or certified zero-free; the computation already isolates unique endpoint integers, so this is a documentation repair.

### PR #101 — VERIFIED

The frozen diff is only `experiments/X-9302-total-count-zero-deflation/RUN_PR71.md`. It is a workflow trigger, not a theorem or result ledger.

### PR #102 — VERIFIED

The frozen diff is a second `X-9301/RUN_PR71.md` trigger. It has no independent mathematical content and operationally supersedes #99. Preserve the resulting artifacts, not both trigger commits.

### PR #103 — VERIFIED WITH FIXES

**Reviewed:**

- `L-9306-shifted-total-count-reuse.md`
- `L-9307-atomized-count-endpoint-deflation.md`
- `X-9302` retained PR71 summaries, including the atomized minimum

The shifted-radius rule is a direct triangle-inequality bound and is sound. The atomized endpoint construction is also sound: exact endpoint-count differences produce disjoint atom multiplicities, and the farthest endpoint yields a safe squared-distance bound. The retained results are all nonnegative and explicitly nominate no counterexample.

The branch diverges from #105 while modifying many of the same inherited paths. Public integration should take #105 as the hardened core and replay or cherry-pick only #103’s unique shifted/atomized claims, producers, and result ledgers. A blind merge risks restoring superseded files or losing source hardening.

### PR #104 — VERIFIED WITH FIXES

**Reviewed:**

- `L-9304-overlapping-interval-count-envelope.md`
- `X-9303-interval-count-envelope/verify_interval_count_deflation.py`

The atom-cell incidence model is correct. Consecutive interval rows give a totally unimodular incidence matrix, so integer endpoint counts admit integral LP vertices. The pointwise forced cumulative profile is a valid universal order-statistic lower profile, and the exact primal/dual checker safely constructs it.

Required fix: `L-9304` collides with PR #107’s selected-factor claim. Rename one or both before merge and update every dependency/reference. This branch also requires the corrected `L-7504` parent.

### PR #105 — VERIFIED

This is the preferred hardened production stack for the direct-modulus/count-deflation family.

Key points that independently pass review:

- the `L-7504` antiderivative display is corrected;
- the direct-`xi` checker recomputes modulus-square and log intervals with exact rational arithmetic;
- the Hardy-Z producer emits consecutive, ordered, disjoint proof-grade line-zero balls;
- nearest-factor selection is not inferred from a truncated central list: the builder requires unselected guards on both sides and proves `selected_max_upper < every_unselected_lower`;
- the earlier unguarded 256-zero block is explicitly marked superseded;
- multi-precision summaries retain only nested, nonnegative rows and no candidate.

The retained conclusion is finite and negative: no declared row is an RH counterexample. This review did not rerun the expensive FLINT/Arb jobs.

### PR #106 — VERIFIED

**Reviewed:** `X-7503-high-carrier-loewner-precision-repair.md` and `replay_high_precision.py`.

The completed-`xi` modulus formula is implemented correctly at the frozen exact ordinate/nodes. The script recomputes primitives rather than reusing the rounded transport strings, and its sensitivity analysis explains the two sign reversals. It consistently labels the output `EMPIRICAL_HIGH_PRECISION_NOT_CERTIFIED`. The valid conclusion is only that the two apparent rounded-string negatives are precision ghosts; it does not certify the fresh positive signs.

### PR #107 — VERIFIED WITH FIXES

**Reviewed:**

- `L-9304-selected-critical-line-factor-deflation.md`
- `L-9305-vandermonde-normalized-modulus-minors.md`
- `X-9302-selected-factor-modulus/verify_selected_factor.py`

Exact removal of already certified critical-line factors is sound. The Vandermonde-normalized cross-minor formula follows from Andreief plus the Cauchy determinant and is monotone under addition of positive residual measure.

Mandatory integration fixes:

1. both claim IDs collide (`L-9304` with #104; `L-9305` with #109);
2. production points and gate SHA fields must be loaded/recomputed from source artifacts, not merely accepted syntactically;
3. the comparison with endpoint-deflated minors should cite positive-measure/Cauchy-Binet monotonicity, not be described as generic determinant monotonicity under PSD order.

The exact finite contraction itself is sound.

### PR #108 — VERIFIED WITH FIXES

**Reviewed:**

- `L-9701-total-count-saturated-sign-chain.md`
- `X-9304-sign-chain-zero-bins/verify_sign_chain.py`
- `build_sign_chain_certificate.py`
- `refine_hardy_z_bins.py`

The theorem correctly combines a total multiplicity count `m` with `m` disjoint Hardy-Z sign-change intervals. Each interval contains an odd-multiplicity line zero; total multiplicity saturation forces exactly one simple zero in each interval and none elsewhere. Sign-preserving bisection is safe.

The builder loads the rigorous total-count artifact and evaluates directed Hardy-Z intervals at exact dyadic ordinates. The standalone checker deliberately verifies only finite sign/count logic. Update stale PR-body references from the discarded `L-9306` name to the stable `L-9701` ID, and keep the builder plus source artifacts in the production trust boundary.

### PR #109 — VERIFIED WITH FIXES

**Reviewed:** `L-9305-witness-adapted-count-dual.md` and `X-9304-witness-adapted-count-dual/verify.py`.

The main insight is valid: for a fixed nonnegative witness response, minimizing its atom costs over the exact count polytope is a finite LP, and an unrestricted rational dual gives the optimal safe subtraction. This can strictly improve a pointwise radial envelope by retaining count correlations. The checker correctly verifies atom order, consecutive count windows, exact integer primal feasibility, rational dual feasibility, and objective equality.

Required fixes: rename the colliding `L-9305` ID and route production through a wrapper that loads/recomputes the declared primitive and count artifacts. The current checker’s SHA fields are semantic bindings, not source verification by themselves.

### PR #110 — VERIFIED WITH FIXES

**Reviewed:**

- `L-9702-support-gap-hausdorff-residual.md`
- `L-9703-count-only-support-gap-chord.md`
- `X-9305-support-gap-hausdorff/verify_support_gap.py`

The support-gap chord has the correct sign. After scaling the residual Stieltjes measure to `q=(u_0+A)/(u_0+y) in (0,1]`, the derivative moments form a Hausdorff moment sequence, so the finite-difference, Hankel, and `(1-q)` localizer inequalities are valid. The count-only chord response is nonnegative outside the support gap and has a positive floor inside it, so an exact total count yields the claimed subtraction.

Before publication:

- update stale references to the stable `L-9702/L-9703` IDs;
- add one sentence tying finiteness of the scaled measure to convergence of the logarithmic derivative / zero-density estimate;
- source-bind the complete-support gate in the production wrapper rather than trusting only a status string and digest syntax.

### PR #111 — VERIFIED WITH FIXES

**Reviewed:** `L-9308-resolvent-polynomial-log-portfolios.md` and `X-9305-log-portfolio-count-dual/verify.py`.

The theorem is correct. For zero-sum `beta`,

```text
phi_beta'(y) = -P_beta(y) / product_i(y+u_i).
```

If `P_beta` is nonnegative on `[0,infinity)` and `phi_beta(infinity)=0`, then `phi_beta` is nonnegative. Nonnegative monomial coefficients are a valid sufficient certificate.

The production checker requires three fixes:

1. enforce sorted, nonoverlapping atom intervals; currently overlapping atoms can be listed and then double-counted by separate windows;
2. bind/load primitive and count source artifacts, rather than checking only the semantic count string;
3. make each `two_point_control` name its atom/count allocation. The frozen code hardcodes `bounds[0]` and `x[0]` for every control.

These defects do not invalidate `L-9308` or the synthetic example, but they block a public production verdict from this checker until repaired.

### PR #112 — GAP/BLOCKED

**Reviewed:** `X-9306-real-log-portfolio-search/basis_check.py` and `results/basis.json`.

The finite arithmetic replay appears sound: exact rational basis vectors are reconstructed, the response identity `P_beta=y^k` is checked, logarithms use exact rational atanh bounds, and the final Decimal operations are outward rounded at every conversion/multiplication/addition. All 15 frozen basis intervals are strictly positive.

The advertised **entire-cone** conclusion, however, is not self-contained in #112. It depends on open PR #114’s `L-9309` simplicial-cone theorem, on `L-9308` from #111, and on the final source-bound #103 certificate. A targeted dependency inspection finds the algebra of `L-9309` plausible and straightforward, but PR #114 was not among the frozen assigned review targets and its checker/integration were not given a full pre-public review. Therefore #112 remains blocked rather than being used to publish a cone-closure theorem.

Required merge order: repaired #111, independently approved #114, reconciled #103/#105 source artifact, then rerun the 15 basis rows against the final blob.

## Integration and merge-order plan

1. **Use #105 as the direct-modulus hardened core.** It contains the corrected `L-7504` display and the guarded source machinery.
2. **Reconcile #103 onto #105 manually.** Cherry-pick/replay only unique shifted/atomized results; do not merge the divergent inherited trees blindly.
3. **Resolve claim-ID collisions before any public claim registry update.** At minimum:
   - #104 `L-9304-overlapping-interval-count-envelope`;
   - #107 `L-9304-selected-critical-line-factor-deflation`;
   - #107 `L-9305-vandermonde-normalized-modulus-minors`;
   - #109 `L-9305-witness-adapted-count-dual`.
4. Integrate #108 using stable ID `L-9701`, then #110 using `L-9702/L-9703`.
5. Repair #111’s production checker before using it as a source for later cone closure.
6. Review and integrate #114 before #112. Then replay #112 against the final source-bound certificate.
7. Drop/squash #99, #101, and #102 workflow-trigger markers after retaining their generated artifacts.

## Connections contributors appear to have missed

### One count polytope, many witnesses

PR #104’s radial envelope, PR #109’s witness-adapted dual, and PR #111’s portfolio dual are not separate count theories. They all optimize different nonnegative cost vectors over the same interval-incidence count polytope

```text
P(m) = {x >= 0 : A x = m}.
```

A single source-bound atom/count artifact can therefore support many witness-specific rational dual certificates. This connection is developed separately as **PROPOSED** methodology `M-15107`; it does not retroactively verify any flawed checker.

### Sign chains can feed both factor and count consumers

A saturated sign chain (#108) provides simple, disjoint, source-bound line-zero bins. The same bins can feed:

- exact selected-factor removal (#107);
- atomized/count-polytope costs (#104/#109/#111);
- support-gap certification (#110), when combined with the total-count complement.

This should eliminate duplicated zero-bin schemas and inconsistent semantic gate strings.

### Support-gap chords are shifted log portfolios

The three-node chord from #110 is a zero-sum logarithmic portfolio whose response is nonnegative only on the shifted support `y>=A`. It suggests extending #111 from monomial positivity on `[0,infinity)` to a shifted variable `z=y-A`, with exact monomial/SOS certificates. This is a genuine extension and remains **PROPOSED**.

## SERIOUS RESOLUTION PATH

**A serious falsification path is present; no reviewed PR supplies a proof of RH.**

The direct completed-`xi` modulus route is existentially complete on the false-RH side: an off-line zero creates a local logarithmic singularity whose sufficiently small interlaced Loewner minor is negative. The reviewed PRs add increasingly powerful, still RH-valid removal of certified critical-line mass and exact count constraints.

The exact missing steps for a serious resolution attempt are:

1. produce source-bound, directed completed-`xi` rectangles on an adaptive `(T,u)` search rather than a fixed table;
2. produce independent total-count and/or saturated-sign-chain artifacts in the same neighborhood;
3. build one atom/count polytope and evaluate the radial, witness-adapted, shifted-support, and simplicial portfolio families against it;
4. require a strict negative upper endpoint with a conditioning moat;
5. reproduce any negative with an independent special-function/count backend and re-audit normalization, node ordering, and every count-to-line conversion.

If RH is true, exhaustive positivity on finitely many tables cannot prove it. A proof of RH would still need a global theorem covering all `T` and all positive node configurations, or an independent positive spectral/Weil argument. None of PRs #99–#112 supplies that global step.

## Final pre-public verdict

The cluster contains substantial, mostly sound finite mathematics and careful no-candidate computations. The public version should preserve the strict boundary:

- **verified finite theorem/checker** is not **verified source artifact**;
- **verified positive finite table** is not **RH**;
- **proposed extension or repair** does not retroactively verify a frozen original;
- **no reviewed negative candidate exists**.
