# Reviewer C — independent validation and coverage ledger

**Disposition: PUBLIC-RELEASE READINESS NOT CLEARED. This is an independent first-pass audit, not a complete scientific re-review or a completeness certificate.** Outstanding A/B scientific dispositions are **pending integrator reconciliation**. They are not failed reviews, accepted claims, or dependencies on unpublished work. The C coverage omissions below are C's omissions and must not be attributed to A/B.

Repository: `GettysburgResearch/riemann` (stable ID `1309150028`). Review branch: `review/C/2026-09-05-post-release-audit`; review PR **#798**. The controlling baseline is `8d16f8d9c475db290bc85e53d775b93b9bcdb336`, root tree `91742c176e5f7e5df8669e9a55f258c4889a1c12`. Initial observation anchor: `2026-09-05T15:36:41Z`. Reads continued afterwards; this is a collection of exact per-object versions, not an atomic snapshot of all mutable GitHub discussions. No main, original research branch, permissions or repository settings were changed.

## 1. Published census and its exact denominator

The anchor census was published first, at `9ba87fb856ecf5ed45b4bc8bd9dd4daa2fed57da`, before the substantive audit. `CENSUS.tsv` now contains the individually enumerated historical heads, post-review-cut PR heads, all eleven programme slots, inspected claim splits, source references, formal/computation checks, and explicit coverage debts.

The previous release is anchored to its **actual** manifests, not to whatever a PR branch happens to contain today:

| Object | Frozen identity | What was checked |
|---|---|---|
| Main release manifest | `canonical/2026-08-22/manifest.json`, blob `446aec7e1c6d7b1d40a7747f3c9b161d03efdad3` at the baseline | Full content read; links reviewer/source identities |
| Previous Reviewer C source census | PR #712, `a6aa936ba8bf538177e34af60db7e2f0a58f8dfd`, `review/2026-08-22/coverage/PR_CENSUS.tsv`, blob `0c49ffb662312f402097b576b399e50b642fdfa2` | All 341 head cells transcribed by line-window reads |
| Previous Reviewer D reconciliation | PR #721, `06c8ea18ffe20c7efa01b0fdacb8ebea0a2b5b22` | Metadata and its release-manifest binding read; not a fresh review of D's mathematics |
| Reviewed claim manifest | `canonical/2026-08-22/claims.tsv`, blob `6a4157460bf0044c6e110a2713f7dfb62bcb6c28` | Identity/size 95,757 bytes pinned; not all 139 claim proofs reread |

There are **341 historical census rows: 340 real PR sources and the expressly absent #417**. The historical census also includes #337 and #368–374; it is not the same denominator as the 333 numbered dispositions #375–707. The release's 139 claim rows are not 139 independently rebuilt formal theorems.

There are **79 PR objects beyond the #707 review cut through #797**, with exact observed heads, and eleven programme issues: **#736–741, #743, #744, #746, #763, #764**. This is a deliberate superset of literal post-release creation dates: release-preparation/reconciliation PRs #708–722 are retained. #742 and #745 are PRs, not missing programme issues. #798 is this audit and is outside that source denominator.

Five additional older active PRs outside the 341-row manifest are recorded: #348, #351, #352, #355, #356. A post-release `updated_at` is only a discovery signal; it does not prove that mathematical files changed.

### Coverage vocabulary

- `B1`: previous reviewed head and a fresh current PR head match. This is a version check, not a new mathematical acceptance.
- `B0`: previous reviewed source identity is known; the current head/delta was **not** independently compared.
- `P0`: frozen PR-level metadata inventory only; not exhaustive file/claim reading.
- `P1`: selected source/claim or external-boundary inspection in addition to PR metadata; still not a full packet review.
- `H0`: retain the exact historical scope; no new scientific verdict.
- `C0`: C owns documentation, infrastructure, source/validation and extraction review; no mathematical acceptance is implied.
- `pending integrator reconciliation`: A/B scientific routing only. Mixed inspected packets have separate claim and C rows. **The split is not exhaustive for uninspected packets.**

Every abbreviated locator `PRn` means that PR's files at the row's frozen source, not its moving branch. `BASE` means the baseline above. An issue/comment has no intrinsic Git commit: those rows use typed `issue:n@C-observation-2026-09-05` identities and explicitly disclose the absence of a complete immutable body archive. A short SHA remains `UNRESOLVED_SHORT_SHA`, never a fabricated 40-digit pin.

## 2. Older changes and direct-main accounting

Fresh head checks matched the prior source for **28** historical PRs (#370–389 and #700–707). The remaining **312 real historical heads were not freshly compared**. Thus this report does not establish that all older reviewed branches stayed unchanged. They remain individually listed as `B0`, rather than silently inheriting present-day acceptance. The #417 no-object row is not counted as an unperformed comparison.

The entire first-parent main chain from the release to the chosen baseline was inspected:

| Main commit | First parent | Recorded integration source |
|---|---|---|
| `852d8aa05c701ea7818ce8a50543e68987fef5cc` (#722) | `677203992eb0168920365ee45ae9db76bfa97dcf` | `99dcb03f431d06032d205e6a6868616a108e4a99` |
| `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` (#732) | `852d8aa05c701ea7818ce8a50543e68987fef5cc` | `b2c92374d42836b60210bc5700f04a83c965750e` |
| `6dda8b5125457ed936330229f8c9eb6491728e76` (#761) | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` | `74570d73194a1c74a39ea1f3ce58771cb0929894` |
| `8d16f8d9c475db290bc85e53d775b93b9bcdb336` (#794) | `6dda8b5125457ed936330229f8c9eb6491728e76` | `c4cbfad34c21d7dfe63e5ca99bb68be58719aa99` |

There is no separate nonmerge first-parent commit in that interval. This does not mean all merged content is reviewed. The exact compare from `6dda8b...` to the baseline lists only seven navigation/access-guidance paths; **no `formal/` change**. Therefore formal-v0.1's main-tree sources did not change in that final main increment. The full bootstrap/reconciliation diff was not independently line-reviewed.

A final direct ref check confirms PR #722 at `99dcb03f431d06032d205e6a6868616a108e4a99`, matching its merged second parent. PR #715 is the distinct `99cc94c48bafd9b96141f7cef9f1e7aa83012747`. An earlier working-note conflation of these similar prefixes was corrected before publication; it is not a repository defect. Version-aware extraction remains necessary, but no #722 head mismatch is reported.

## 3. Programme and deposit audit

All eleven bodies were requested. All comment collections were acquired through the connector; the displayed long bodies/threads were not all fully inspected or immutably archived. #739 (one comment), #744 (two), #746 (one), and #763 (two) had all comment bodies read. #740 and #764 returned zero comments. #736, #737, #738, #741 and #743 received selected-body reading; #763/#764 long objective bodies were only partially returned. **Complete transitive reference closure is not certified.**

Confirmed dependencies requiring preservation include:

- #743 → #713 → #715/#718/#719/#751; #746 → #727/#730, with #719's carrier correction binding the withdrawn unquotiented packing gate.
- #744 → #714/#716/#720/#723/#724/#726/#729/#731/#772, with exact older checkpoint SHAs distinct from latest PR heads.
- #739 → #771; #763 → #764 and #771, distinct from a complete source-to-principal theorem.
- #738/#741 → #752/#756. Comments `5404086969` and `5404087087` explicitly downgrade the r=4 scout: script, coefficient numerators, exact domain and grid bounds were not retained. The 24,346+34,225 zero-hit totals are not reproducible evidence. The cited short correction `709b6b36` remains unresolved here.

`CENSUS.tsv` records the concrete older checkpoints encountered. Suggested branch names in programme specifications are not called actual deposits without resolution. The absence of a full branch-ref inventory, all attachment payloads and all issue/PR review comments is a release-census blocker, not a claim that those materials do not exist. The reports do not rely on A/B's unpublished work.

## 4. Bounded computational replay actually executed

No broad prime, zero, field, conductor or matrix campaign was launched. No optimizer or imported numerical sidecar was executed. Two short source files were read in full, recreated byte-for-byte locally, authenticated using the Git blob hash, and run only on reviewer-created bounded fixtures in temporary directories. The fixtures are **not** the original scientific data.

### 4.1 Canonical consumer acceptance failure

Source: `canonical/consumers/mellin-landau/validate_consumer.py` at the baseline; **1,880 bytes**, Git blob **`950d5f1193724bd975111a1b37d55e19c9270a35`**. Its complete source and associated CLAIMS/EDGES were read, but the replay below uses synthetic structural tables to isolate acceptance behavior.

Command pattern: `python validate_consumer.py` and `python -O validate_consumer.py`; six cases in each mode, five-second timeout per subprocess, isolated working directories and reduced environment.

| Fixture | Normal exit | `-O` exit | Independent observation |
|---|---:|---:|---|
| Minimal valid shape | 0 | 0 | Structural fixture accepted; not an authentic scientific replay |
| Empty census | 1 | 0 | Optimization removes mandatory checks |
| False VERIFIED labels on open claims | 1 | 0 | Optimization removes status gate |
| Duplicate semantic ID | 0 | 0 | Dictionary construction overwrites duplicate identity |
| No open premise | 1 | 0 | Optimization removes premise gate |
| Malformed source SHA | 0 | 0 | Source identity is not authenticated by this validator |

The file uses `assert` for acceptance and writes `validation.json` itself. It performs finite algebra examples, not a primitive-source proof of the general Mellin–Landau theorem. **It must not be the sole promotion gate.** This result does not demonstrate that the whole repository pipeline accepts a false theorem: it identifies this validator's concrete boundary. Replace assertions with explicit exceptions, reject duplicates, validate typed exact identities, and separate production from verification. Full command/stdout/stderr receipts are supplied in the bounded replay bundle.

### 4.2 Formal axiom-output parser controls

Source: `formal/scripts/audit_axiom_output.py` at the baseline; **3,534 bytes**, Git blob **`ef83fe752f6612617612b259109cfdcab8b108bc`**.

Command pattern: `python [-O] -I audit.py output.txt Print.lean`. Ten cases in each mode, five-second timeout, temporary directories. All **20 expected outcomes** were reproduced: valid allowed-axiom, empty-axiom and multiline outputs pass; missing output, `sorryAx`, custom axioms, unexpected declarations, unterminated lists and garbage after a payload reject. Repeated identical allowed output is accepted because coverage is a set. That does not conceal a missing expected declaration, but is not an exact once-only transcript check.

These are fabricated parser texts, **not actual Lean or Nanoda output**. The parser's source-hash authentication, normal/optimized agreement and rejection behavior are positive evidence about its implementation; they cannot authenticate the origin of a supplied transcript.

## 5. Formal-v0.1: statement and build boundaries

Full source reads included `Analysis/FixedDetectorConsumer.lean`, `Analysis/LandauConsumer.lean`, `Operator/XiExternalInputs.lean`, the trusted root `RiemannFormal.lean`, `check_no_sorry.sh`, `check_axioms.sh`, and the axiom parser. `Operator/XiOrderThree.lean` was read through line 115, not in its entirety. `FORMAL_V0_1.md` was read as a **reported release record**, not as fresh execution evidence.

Findings:

1. The inspected fixed-detector result genuinely uses fixed source/continuation/factor data. The analytic results `MellinLandauBoundarySingularity`, `SubpowerNegativeMassHolomorphy`, `ShiftedReciprocalPoleOrder`, admissible-zero strip/reflection and related continuation hypotheses remain explicit. Its conditional assembly is not an unconditional proof of those premises or RH.
2. The Landau interface retains finite abscissa, nonzero-a.e., local integrability and analytic-domain hypotheses. Supplying a proposition as a theorem argument is not a custom axiom, but the conclusion remains conditional. The named wrappers do not prove the supplied analytic inputs.
3. `plattTrudgian_source_lock_exact := rfl` proves equality of metadata. It does not verify the external zero computation. The input package separately carries verified-height, multiplicity-residual, one-use allocation and C2 approximation data. Those dependencies must stay in the public theorem description.
4. The trusted root does not import `ComparatorSmoke`. Seven Challenge placeholders and their solutions must be tracked separately from trusted production. A repository-wide textual `sorry` count would conflate specifications and proofs. Conversely grep alone does not establish axiom cleanliness.
5. The axiom driver covers nine explicit print modules plus declarations drawn from release deltas. This is a defined coverage set, not every declaration in every external library. The fresh parser replay did not run the driver or build those declarations.
6. The exact main toolchain is **`leanprover/lean4:v4.33.0-rc2`**, blob `c084c7fbe586b0276863b66f16d2955a43bc3fc6`. Main's recorded Mathlib pin is `51e6992efd06126df61a496bebf8f49482a4e129`; recorded Zeta23 pin is `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e`. Reported release counts (58 commands, 8,806 jobs, 21 targets, seven comparator pairs, 139 registry rows) are not new C measurements.

**No local Lean/Lake installation was available; no fresh Lean build, complete axiom transcript, independent kernel run or exhaustive paper-to-Lean statement comparison was performed.** Accessible workflow queries did not supply a current-baseline build receipt. That is missing evidence, not proof that no build ever ran. The full later-formal-PR semantic reconciliation remains outside the inspected subset.

## 6. External-source boundaries #787–#791

| Packet | Exact external source / boundary | C result |
|---|---|---|
| #787 PrimeGaps186 | `openai/PrimeGaps186@61340d0b74163003b32756bb16e91d9209a5e330`; Lean 4.34.0-rc2; `kloosterman3_bound`, `kloosterman2_correlation_bound`, `physical_integral_bounds` | Full import formalization audit read. Conditional endpoint; 152 numerical clauses are an external sidecar, not axiom elimination |
| #787 LongGaps | `openai/LongGapsBetweenPrimes@8f5fa88c88b4750028c05b66b081d56a92418054`; metadata `03a1190d0bc5502d9f54eeb60ad3e45e22b0df0b`; Lean 4.33.0 | Standard-axiom-only status is reported upstream, not independently kernel-replayed. Same 4.33 generation is not the exact main rc2 toolchain |
| #788 | `AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7`; Lean 4.34.0-rc2 | Headline hypotheses `hRvM` and `hPC` are not discharged by finite multiset proofs. Upstream CI and separately documented Comparator/Nanoda are different receipts |
| #789 | `arXiv:2609.04176v1`; PDF SHA256 `1d05b36a5675cb8084935ec6945e004f1af9387c8fae6c48b242b4a94d73bd90` | Current hostile-review disposition is invalid-as-written; scientific confirmation pending integrator reconciliation. Missing 178/235 cell tables and correction propagation must not be hidden by old summaries |
| #790 | checkpoint-specific V100, Platt–Trudgian and interval-Gamma inputs in the evolving research packet | No zero census or fresh interval-Gamma validation performed by C. Old checkpoint receipts cannot validate later all-order claims |
| #791 | FLT reference at `aa2d8b34692b16c70f699536de0d8e75b9a3e9ef`, README blob `f3cfcb92443c29a8ce87494f6c9a7b57e40129e9` | Reference-only documentation, not a code import, trusted dependency or reviewed proof |

The #787 numerical environment states Python 3.12.13, NumPy 2.2.6, python-flint 0.9.0 and **FLINT 3.6.0 with a signed-convolution correction**. The exact patch/binary provenance and all clause coverage were not independently checked. Preserve isolation; do not silently upgrade the root toolchain.

Apache-2.0 LICENSE headers were fetched at the exact code pins: PrimeGaps blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, LongGaps `d645695673349e3947e8e5ae42332d0ac3164cd7`, AxiomMath `57bc88a15a0ee8266c259b2667e64608d3f7e292`. **This is not a full NOTICE/attribution or paper-permission audit.** Paper PDF receipts/rendering assertions were read as prior import records; C did not render or rereview those PDFs. No code license is inferred to cover a paper or attachment.

## 7. Navigation, reproducibility and access

The current README, integration entrypoints, CONTRIBUTING and docs/REVIEWING provide a useful separation of exploration, accepted exact-SHA mathematics, computation and owner responsibility. Their warnings against finite-to-global extrapolation, hash-only self-attestation and claim-ID reuse should be preserved. Navigation does not make branch-only work resident on main.

Confirmed gaps: post-release collision rows are absent from the old aliases catalogue; a whole-repository setup/profile lock is not present at the inspected root; no root LICENSE or SECURITY file was observed in that root inventory. `docs/PUBLIC_LAUNCH.md` does not exist (not a claimed broken existing link). No complete recursive link, license, personal-data or secret-history scan was performed.

`docs/REVIEWING.md` explicitly says that private Free main is not technically protected. CONTRIBUTING's Write-access policy is therefore not an enforced branch restriction. Owner-only launch actions are listed separately in RELEASE_BLOCKERS; C did not alter them.

`.github/workflows/formal.yml` uses ordinary PR events and `contents: read`, positive safety properties. It also uses mutable `actions/checkout@v4`, `ubuntu-latest` and an Elan installer downloaded from `master` into a shell. No claim of exploitation is made; pin, verify and isolate these dependencies before opening privileged contributor workflows.

## 8. Commands, failed acquisitions and omitted checks

Actual local commands included: `python scripts/replay_consumer.py`; `python scripts/replay_axiom_parser.py`; Git-blob SHA1 reconstruction using `b'blob '+length+b'\\0'+bytes`; JSON/TSV parsing and census denominator checks. Replay subprocesses were bounded to five seconds and used reviewer-created data. Fixture receipt files record each command, exit and output. Git exists locally; `gh`, `lean`, and `lake` were not available. Direct GitHub DNS/network acquisition failed. Connector reads, rather than an unverified local checkout, provided source bytes.

A one-shot **read-only metadata export**, with fixed baseline, pinned Actions and caps, was added only on this review branch at `2f191c487a49dad2f4ba6a63d068a2e2f97ceb0f`. Branch and exact-head Actions queries returned no run. It was removed at `bc7ccb0da6c87b588c4f96ccfd14eaa58cb1cfc9`; it is absent from the final diff. No export, research computation or success was inferred. The cause of no run is unconfirmed. No permissions/settings were changed.

Unperformed: 312 historical current-head comparisons; complete all-branch/reference/deposit closure; exhaustive claim-level splits; every producer/checker or all raw coverage artifacts; full 139-claim formal statement audit; clean exact-toolchain builds; full license/NOTICE/attachment permission audit; complete Git-history secret/PII scan; owner access/ruleset enforcement checks. These are explicit release-closure debts. **This first-pass report is independent and finished as a report, but does not certify complete coverage of the requested universe.** The integrator should use the narrow completed findings and the explicit omission ledger, not infer acceptance from the size of the census.
