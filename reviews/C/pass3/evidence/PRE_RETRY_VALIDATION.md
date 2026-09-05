# Reviewer C — second-pass independent validation and coverage

**Historical head-comparison coverage is complete for its declared 340-PR denominator. Full research/public-release coverage is not complete. A decisive source-level nonvacuity defect was found in the formal actual-Xi input package.**

Scientific baseline: `GettysburgResearch/riemann@8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Existing review PR: **#798**, branch `review/C/2026-09-05-post-release-audit`.
Exact published head read back: **`7466ad8081101508be7c7acf0065cb2e0944a639`**.

**Publication boundary:** this second pass is a prepared review-only patch, not a new pushed commit. The currently exposed GitHub actions are read-only; discovery of `update` returned no tools, and the installed-plugin search did not expose an alternate write action. No main or research branch, setting, permission or workflow was changed. `pass2/PUBLICATION.json` separates the existing published head from the unpushed deliverables. Nothing here claims an asynchronous publication.

C worked independently. Outstanding A/B scientific dispositions are **pending integrator reconciliation**, not failed reviews or accepted claims. C's own omitted work remains C's responsibility. The first-pass report and census are preserved unchanged in `pass2/evidence/PASS1_*`.

## 1. What coverage was completed

| Review aspect | Exact scope and outcome |
|---|---|
| Historical source heads | All **312** previously unchecked PR heads were read. Combined with **28** first-pass observations, this covers **340/340** real sources: **338 MATCH**, **#568 and #599 DIFFERENT**. The explicit absent #417 is not a PR or failed review. |
| Historical source deltas | Two #568 paths and fourteen #599 paths enumerated. Both #568 text artifacts and all thirteen #599 text files inspected; one archival PDF remains uninspected. Four recovered #599 claim texts independently desk-audited at their exact head. |
| Formal release catalog | All **31 canonical delta rows and 6 API rows** reconciled. All **34 declaration-bearing catalog entries**, comprising **33 unique declarations in 15 defining modules**, read through their declaration and body. Three canonical rows are open producer estimates without declarations. |
| Critical shared input | Entire Xi ChallengeDeps input file read, including normalization, source enumerations and all input fields. Empty-input proof reconstructed independently; a regression candidate is supplied but uncompiled. |
| Bounded computation | Six author-script executions, six mutated-script executions and thirty GNU grep executions, plus an independently written exact finite-algebra checker and fail-closed inventory tests. See retained run receipts and reproduction commands. |

This does not mean 340 PRs were mathematically re-proved. Nor do 33 read declarations constitute all resident Lean declarations or full transitive import/kernel coverage. The denominator is stated so that version coverage, declaration inspection, mathematical validity, compilation and public readiness cannot be conflated.

## 2. Source census and observation semantics

`CENSUS.tsv` retains 566 core inventory records, including the original 341 historical rows (340 real PRs and the absent #417), 79 post-review-cut PR objects through #797, all eleven programmes, selected claim/external/dependency records and explicit omissions. The historical PR set is `{337} ∪ ({368,…,707} \ {417})`. The older 333 numbered dispositions and 139 canonical claim rows are different denominators.

`pass2/HISTORICAL_HEAD_COMPARISON.tsv` gives both the recorded reviewed-source SHA and observed current SHA for each real historical source, with observation pass, time, endpoint and comparison. The original `frozen_source` column was not overwritten. Updated coverage `B1` means a head match; `B2` means a source difference requiring its own delta treatment; neither grants scientific acceptance.

The 28 earlier observations are explicitly inherited, not claimed as new reads. The 312 fresh head fields were transcribed from GitHub connector GET responses and retained in `pass2/evidence/observed_heads.json`. This is not a signed raw API export or an atomic snapshot of every mutable repository ref. The offline checker can test consistency with those receipts; it cannot independently authenticate that an API read occurred or that no later mutation happened.

Both differing head commits precede August 22. Therefore these are **reviewed-source selection differences**, not evidence of post-release changes based only on a later `updated_at`.

## 3. #568: replay-only difference, bounded equivalence checked

Recorded source: `085d046905bfd32a5725632650039e58bb7fc1f7`.
Observed head: `3a70470e3a8bbd60e0b7387ea46fd391cfb1d2e2`.
Head commit date: `2026-08-17T12:57:21Z`. Ahead by one commit.

Only `experiments/X-97010-parity-grouping-hardening/verify.py` and its `results/verification.json` differ. The script change adds comments and changes a value iteration into key/value iteration with an unused key. Exact old and new script bytes were authenticated by Git blobs `c946104810907deb55db18a4f2897e28618a04db` and `f0e8f85e195162d745477cfb69e68b9b24443289`. The old script and old JSON formatting were reconstructed from the read source/diff and then checked against their exact Git blob identities, rather than assumed identical.

Old/new scripts in ordinary/optimized Python produced the same output bytes. The earlier retained JSON differs only in formatting; its exact historical bytes were also authenticated. C's verdict is **replay delta resolved, no claim-file change**.

The result is not a fresh certificate of the imported directed-interval endpoints. The checker combines copied Decimal endpoints, finite parity data and a hardcoded factorization comparison. Its scope is not ASHP67, a new Landau theorem or RH. The independent algebra checker in this pass supplies a separate symbolic factorization test rather than counting the duplicated hardcoded tuple as a proof.

## 4. #599: a substantive packet beyond the historical census pin

Recorded source: `223f11259b3e7134f78d6492795e6e94caca8be3`.
Observed head: `8daa0a5d94de56c68a1ce710824b26cacc1a9bbc`.
Head commit date: `2026-08-18T06:10:22Z`. Ahead by four commits; fourteen added paths.

The provenance files explain why `223f…` occurs: it is the intentional PR #590 scientific freeze. Publication base `4f1283c67f0d4a4b504badd4c4113ba227521162` includes two PDF/publisher-only commits. The new factor-67 route was reidentified from occupied 97900-series IDs to 97910-series IDs. That lineage is not itself a malformed source lock. The historical #599 census row does not identify the final new packet. Whether another exact review covers it is **pending integrator reconciliation**, not assumed absent from all other reports.

### Independent claim dispositions

| Claim | C's reconstructed argument and boundary |
|---|---|
| L-97910 | The complete small-prime expansion gives `a ∏(1−1/p)` with error `O(X^(−1/2) ∏(1+p^(−1/2)))`. At `Z=(κ log X log log X)^2`, fixed `κ<1/2` gives error `X^(κ−1/2+o(1))`. The strict exponent is consistent given the declared base asymptotic and PNT/Mertens inputs; those transitive source theorems were not fully re-audited. |
| L-97911 | The largest-prime ownership identity is exact. The terminal strip bound `O(H²/log X)` is small relative to the cube when `H² log Z=o(log X)`. The immediate owner-child scale `X/p` must not be confused with a fully expanded product-child scale. |
| L-97912 | Separating the positive Euler main leaves an exact signed remainder. The bulk estimate has exponent `κ+(β−1)/2`, negative for `β<1−2κ`; the product-boundary remainder remains unsigned/uncontrolled. This is not a positive asymptotic for the native whole source. |
| T-97910 | ESBLP67 and AFPBR67 are two alternative open sufficient interfaces, not two already-proved estimates or automatically intersectable localizations. The all-scale source/annular-consumer composition still needs its exact dependencies. No open signed gate was proved by C. |

For a decomposition `M + E + R`, the exact sign condition is `R ≥ −M−E`. Knowing only `|E|≤B`, the safe sufficient condition is `R ≥ −M+B`, not `R ≥ −M−B`. This is a clarification for downstream adapters, not an allegation that the packet explicitly proves the wrong sign.

The author checker uses a rational toy source and ordinary floating-point asymptotic sanity values. Its full committed JSON was reproduced byte-for-byte, with SHA256 `ad594acfe7c23191fdb4577e592842cf48ed136ff391543da2e55f1d741a8843`; the embedded canonical payload digest is separately checked. The program does not read and authenticate the native annular source or independently prove PNT, Mertens or its named RH-facing estimates. A self-hash does not add those missing obligations.

The inherited `.github/workflows/t97700-publish-pdf.yml` is a branch-specific publisher with `contents: write`, persistent checkout credentials and `git push`. It verifies a fixed downloaded PDF hash, but should not be copied blindly as scientific-checker infrastructure. It was not run. The original source archive and archival PDF were not acquired, visually reviewed or rights-cleared.

## 5. Formal fidelity: a concrete failure, not merely missing build coverage

Read **[the complete nonvacuity proof](pass2/FORMAL_NONVACUITY.md)** first.

The shared definition uses the raw totalized product `riemannXi(s) = (1/2) s(s−1) completedRiemannZeta(s)`. It is exactly zero at `s=1`. Consequently `centeredXi(1/2)=0`, and Lean's division-by-zero convention makes `actualXiNodeP(1/2)=0` without evaluating the derivative. But an `ActualXiOrderThreeInputs` instance supplies strict positivity at every positive node and a grouped expansion to which that field applies. At `x=1/2` it implies `0<0`. The input type is empty.

Five actual-Xi canonical entries therefore have a **FAIL_NONVACUITY_OF_HEADLINE_INPUT** disposition at this source, despite their historically reported `PROVED_CONDITIONAL` labels. Correctly proving an implication from empty inputs is not Lean unsoundness. It also does not disprove the ordinary Xi theorem. It blocks promotion of these declarations as a usable source-faithful realization until the input and function are repaired and reviewed.

Independently, an injective `ℕ → ReflectedOffLineOrbit` cannot encode empty or finite off-line spectra. The repair must cover those cases rather than merely correcting the point `x=1/2`. Pinned Mathlib provides an entire `completedRiemannZeta₀` and a proved identity giving the normalization repair `ξ(s) = 1/2 + s(s−1)Λ₀(s)/2`. The packet includes an uncompiled Lean regression and exact-source runner, not an applied repair or successful build.

The general `NonremovableAt` predicate is merely `¬ AnalyticAt` for the assigned function value. It is weaker than punctured analytic nonextendability; the point-spike counterexample and implications are given in the same note. The transfer lemmas remain valid for that weaker predicate, and negative meromorphic-order hypotheses make the actual pole application stronger. No false conditional RH proof is inferred solely from the name.

The catalog counts themselves reconcile: 31 canonical rows have 28 declaration-bearing entries and three open producer entries; six API mappings make 34 catalog entries and 33 distinct declarations. The reported ten proved statuses include three formalized refutations. The bootstrap RH proposition supplies the additional stated row. These are status/count facts, not thirty-three independent global theorems.

## 6. Replays and adversarial outcomes

`pass2/reports/` retains stdout/stderr, outcomes, arithmetic classifications and source locks. Replay drivers authenticate copied target bytes before executing them in temporary directories; author code is not installed into production.

| Driver | Declared bounded scope |
|---|---|
| `replay_changed_packets.py` | Six executions: #568 old/new and #599, each in ordinary and optimized Python. Exact retained output comparisons. |
| `replay_packet_mutations.py` | Three deliberately corrupted temporary copies, each in two modes. All three reject normally but emit PASS under `python -O`; assertions are not fail-closed acceptance checks. |
| `replay_tactic_guard.py` | Fifteen text fixtures against the baseline and a candidate PCRE: thirty GNU grep calls. Baseline misses ten ordinary tactic-suggestion spellings and flags `apply?x`. Candidate handles these fixtures but is not a full Lean lexer. |
| `independent_finite_algebra.py` | Independent commuting formal-variable largest-owner expansion through ranks 0–8 (511 coefficients), separately expanded fixed 5:3 factorization, and an adverse error-sign fixture. The general finite identity also has the direct ownership proof; no asymptotic inference is made from finite testing. |
| `validate_pass2.py` | Exact archived-source identities, all historical comparison rows, catalog/source boundaries, current-census consistency, and malformed-input rejection tests. It explicitly denies scientific or all-ref completeness certification. |

Run, from repository root in a disposable checkout or the unpacked review packet:

```sh
python reviews/C/check_census.py
python -O reviews/C/check_census.py
python reviews/C/pass2/scripts/validate_pass2.py
python -O reviews/C/pass2/scripts/validate_pass2.py
python reviews/C/pass2/scripts/replay_changed_packets.py
python reviews/C/pass2/scripts/replay_packet_mutations.py
python reviews/C/pass2/scripts/replay_tactic_guard.py
python reviews/C/pass2/scripts/independent_finite_algebra.py
```

The drivers overwrite only their own review receipts. Temporary path text may differ across runs; compare outcomes and authenticated reproduced artifacts rather than requiring identical logs. The first-pass consumer/parser receipts remain historical evidence, not newly rerun here. The uncompiled Xi regression is explicitly separate from these executed Python/grep tests.

## 7. Remaining C omissions

`pass2/COVERAGE.tsv` is the controlling scope matrix. Complete claim-level extraction across all 79 later PRs, all new PRs beyond the original cutoff, branch-only deposits, full mutable discussion snapshots, attachments and transitive links remains incomplete. Only the first branch-name search page was examined; it is not an all-branch SHA census. Most later PR coverage remains inherited metadata or selected-source inspection.

The formal pass now reaches every listed declaration's definition and body, but not every uncataloged helper, external analytic proof, upstream dependency or compiled environment. No Lean/Lake/Comparator/Nanoda run, compiler installation, broad numerical campaign, full-history secret/PII audit, all-import license/NOTICE/paper-rights audit, or owner ruleset/access verification occurred. The #599 PDF is explicitly outside the reviewed content. C does not claim these are complete or depend on an unpublished A/B report to complete them.

**Public-release readiness remains not cleared.** The narrower historical version census is closed; the wider scientific, build and launch attestations are not.
