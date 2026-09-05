# Independent Reviewer C audit — second-pass handoff

Scientific baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Review PR #798; branch `review/C/2026-09-05-post-release-audit`.
Exact existing published head: `7466ad8081101508be7c7acf0065cb2e0944a639`.

**This second pass is prepared, not pushed: only read-only GitHub actions were exposed.**
See `pass2/PUBLICATION.json`. No main, research source, permission, setting or workflow was changed.

## Read first

**`pass2/FORMAL_NONVACUITY.md` proves from the frozen definitions that the actual-Xi headline input package is empty.** The raw Xi product vanishes at the pole, giving `actualXiNodeP(1/2)=0`, while the input requires strict positivity. Five actual-Xi catalog entries depend on this type. The source-level contradiction is complete; its supplied Lean regression is uncompiled. A separate off-line enumeration defect excludes empty/finite spectra.

Historical version coverage is now **340/340 real PR sources**, after **312 additional observations**: 338 match and #568/#599 differ. #568's replay-only delta is resolved; #599's four recovered claim texts, thirteen changed text files, finite replay and publisher boundary are inspected. Its archival PDF and transitive analytic inputs remain outside the completed review.

Every formal catalog mapping is now scoped against its declaration and body: 31 canonical rows plus six API rows, 34 declaration-bearing mappings, 33 distinct declarations, 15 defining modules. This is not full import/kernel coverage or scientific acceptance of all entries.

`VALIDATION.md` records sources and replays; `RELEASE_BLOCKERS.md` distinguishes closed coverage from confirmed defects and uncompleted gates; `STRUCTURE_AND_EXTRACTION.md` gives the repair/extraction handoff. `CENSUS.tsv` retains the original source pins, and `pass2/HISTORICAL_HEAD_COMPARISON.tsv` records current observations separately. All seven replaced first-pass review files are archived unchanged under `pass2/evidence/PASS1_*`.

## Reproduce the bounded checks

From repository root or the unpacked second-pass review packet:

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

Use a disposable copy: replay drivers replace only their own review receipts. Original target bytes are authenticated; mutation tests affect temporary copies only. Ordinary/optimized Python and bounded GNU grep fixtures were executed. No compiler installation, Lean/Lake/Comparator/Nanoda build, broad numerical campaign or network request is performed by these Python checks.

`pass2/lean/XiInputNonvacuity.lean` and its optional exact-source shell runner are explicitly **NOT RUN**. They are not imported by the trusted project. All prior reviewed claim/source manifests and first-pass consumer/parser files already in PR #798 remain untouched by the patch; the downloadable packet is not a full repository mirror.

**Public-release readiness is not cleared.** All-postcut claim splitting, programme/attachment/transitive and branch-only closure, full build/uncataloged statement coverage, imported rights and all-history/access audits remain incomplete. These are C's omissions, not A/B failed reviews. Their outstanding scientific dispositions remain **pending integrator reconciliation**; no unpublished report was a dependency.
