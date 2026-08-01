# Cutoff pull-request ledger

**Cutoff:** `2026-08-01T21:35:52Z`  
**Local cutoff:** `2026-08-02T00:35:52+03:00` (`Asia/Jerusalem`, IDT)  
**Frozen `main`:** `d7fe83f463a2416faa4279cfb406f7283aa34b2c`  
**Population:** 127 open PRs — 126 exact-SHA reviewed source PRs plus review-only PR #212. PR #213 is post-cutoff.

RH remains unsolved. Every review verdict applies only to the exact reviewed SHA and scope. A later repair or current head is a separate object.

## Ledger files

The full ledger is stored as UTF-8 tab-separated batches so it is readable in a text editor, easy to diff, and parseable without a YAML dependency.

| Batch | Population | Ledger | Frozen review evidence |
|---|---|---|---|
| A | #4–#43 assigned set | [`batch-A.tsv`](ledger/batch-A.tsv) | `reports/gpt56-08/2026-08-01-pre-public-review-prs-4-43.md` @ `d1cf0320fb80dbe4d39e0e36d1c8af69bdcf3ff6` |
| B | #44–#63 assigned set | [`batch-B.tsv`](ledger/batch-B.tsv) | `reports/gpt56-global-01/2026-08-01-pre-public-review-pr44-pr63.md` @ `88617ac916d3df6e61ec5b4726e866743b8fc4a3` |
| C | #64–#79 assigned set | [`batch-C.tsv`](ledger/batch-C.tsv) | `reports/gpt56-pro-09-i/2026-08-01-pre-public-review-pr64-pr79.md` @ `7162c2a221fd87e6e7baf4e7245d6f42b5e04de3` |
| D | #80–#98 assigned set | [`batch-D.tsv`](ledger/batch-D.tsv) | `reports/gpt56-03-review/2026-08-01-pre-public-pr80-98-review.md` @ `43b1c54187dd0abdc4cbc34fa1a692b25fbe92cf` |
| E | #99–#112 | [`batch-E.tsv`](ledger/batch-E.tsv) | `reports/gpt56-04-f/2026-08-01-pre-public-review-pr99-pr112.md` @ `0965166d9b12bec576d7728793d9c2542364f2c1` |
| F | #113–#130 assigned set | [`batch-F.tsv`](ledger/batch-F.tsv) | `audits/gpt56-pro-16/2026-08-01-pre-public-pr113-pr130-review.md` @ `a46b6bb9269b46caa205aebe50a7f19ccc9d86da` |
| G | #132–#159 assigned set | [`batch-G.tsv`](ledger/batch-G.tsv) | `reports/gpt56-pro-09-m/2026-08-01-pre-public-pr-review-132-159.md` @ `d29dd935958d88560d73b1865185972ec06f1011` |
| H | #161–#186 assigned set | [`batch-H.tsv`](ledger/batch-H.tsv) | `reports/gpt56-02-p/2026-08-01-pre-public-riemann-review.md` @ `27bb5dcd7a0a1739eeaa26ad97f12eb0a14bc19b` |
| I | #187–#211 assigned set | [`batch-I.tsv`](ledger/batch-I.tsv) | `reports/gpt56-05-l/2026-08-01-pre-public-review-pr187-pr211.md` @ `c3c6c98a580277e22a04790222989bf3816f2ef2` |
| J | review-only #212 | [`batch-J.tsv`](ledger/batch-J.tsv) | #212 @ `88617ac916d3df6e61ec5b4726e866743b8fc4a3` |

[`pr-ledger.json`](pr-ledger.json) is the machine-readable manifest for these files, codes, counts, and review sources.

## Columns

Each TSV row records:

- PR and concise focus;
- exact review-recorded SHA;
- frozen verdict and review report/ref;
- cutoff and present open state;
- directly refreshed present head where one was individually read;
- head-evidence class;
- dependency code;
- conflict and next required action;
- advisory disposition.

Dependency codes are defined in the manifest:

- `D0`: D-0001 / finite Guinand–Weil source, admissibility, and normalization;
- `XI`: completed-ξ or ξ'/ξ normalization and primitive provenance;
- `DX`: direct-ξ modulus plus zero/count/response-moment provenance;
- `RB`: Robin criterion and canonical arithmetic reductions;
- `SW`: Suzuki/CCM/localized-Weil form, metric, and stacked finite algebra;
- `LT`: named literature/source interface;
- `RV`: exact review record.

## Head evidence

- `R_ONLY_PRESENT_HEAD_NOT_INDIVIDUALLY_REFRESHED`: the reviewed SHA is authoritative; the PR was still open, but this pass did not individually read the present SHA.
- `D_SAME`: present head was directly read and equals the reviewed head.
- `D_DELTA_NOT_REVIEWED`: present head was directly read and differs. The old verdict does not cover the delta.

Known directly refreshed deltas are #158, #164, #165, #191, #200, #202, #208, and #211. #212 was refreshed at the same head. No blank present-head field asserts equality.

The timestamp-based snapshot script may emit a reconstructed candidate from commit timestamps. That candidate is `R?`, not an exact historical head, and is never used to extend a review verdict.

## Aggregate

| Verdict on 126 reviewed source PRs | Count |
|---|---:|
| VERIFIED | 29 |
| VERIFIED WITH FIXES | 55 |
| GAP/BLOCKED | 39 |
| REJECTED | 3 |

## Advisory dispositions

- `MERGE CANDIDATE`
- `FIX THEN MERGE`
- `PRESERVE AS PROPOSED`
- `SUPERSEDED/DUPLICATE`
- `GAP/BLOCKED`
- `REJECT/CLOSE CANDIDATE`

They are recommendations only. This integration branch does not merge or close source PRs.
