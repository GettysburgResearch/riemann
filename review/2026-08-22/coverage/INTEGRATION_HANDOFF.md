# Integration handoff to Reviewer D

## Final controlling instruction

This document contains historical pass-one publication instructions. For the
completed packet, the **final controlling base** is PR #712 head
`899d5efc37025b84a03f231fd6006a2b7a97e6e3`, and the final incremental patch
must be applied only there. `PASS2_FINAL_REVIEW.tsv`,
`FINAL_HEAD_RECONCILIATION.tsv`, `FINAL_REPORT.md`, and
`replay/validate_final.py` control over earlier intermediate counts.


## Frozen inputs

- Main: `677203992eb0168920365ee45ae9db76bfa97dcf`
- Reviewer B PR #708: `eb1987502ef9043e782ac6ab1e19c47be9daef93`
- Reviewer A PR #709: `55fe0b6f23d9163e2b602608da84194ba243d7c4`
- Reviewer C intended branch: `review/2026-08-22/coverage-genealogy-delta`
- Research census terminal PR: `#707`
- RH status: **UNPROVED**

This packet is additive. It does not replace A/B claim-level review and does not overrule their verdicts by coverage labels.

## Consumption order

1. Read A and B at their exact heads.
2. Load `PR_CENSUS.tsv`; require one disposition for each PR #375–#707.
3. Use `HISTORICAL_PROPOSALS.tsv` to avoid re-reading obsolete full manuscripts after a later exact counterexample.
4. Merge `DELTA_CLAIMS.tsv`, `DELTA_REFUTATIONS.tsv` and `DELTA_ALIASES.tsv` into the canonical claim graph using semantic IDs, not bare numerical IDs.
5. Import `DELTA_COMPUTATIONS.tsv` only as a provenance inventory. No heavy campaign was rerun.
6. Resolve every `PROVENANCE_DEFECTS.tsv` row before copying a SHA/path/hash into a canonical record.
7. Run `replay/validate_packet.py` and `replay/light_fraction_fixtures.py`.

## Proposed lifecycle actions

- Close or archive failed proposal wrappers only after linking the exact controlling review/refutation and extracting surviving local theorems.
- Keep #652/#653 as the controlling native-source descendants.
- Keep #393–#396 and #446 as distinct operator theorem families; do not collapse transform criteria into low-order Pick positivity.
- Keep #388 as the controlling Brownian Bohr firewall.
- Keep #606 as the Q4 UOSACF/finite-filter classification endpoint, with earlier finite Q4 theorems extracted separately.
- Keep #674/#675/#689 and #696/#702/#707 as live criterion/reduction lineages with explicit terminal gates.
- Never merge a finite certificate into a global implication edge.

## Publication status

The original Reviewer C packet was subsequently published by a separate writer
as draft PR #712 on branch
`review/2026-08-22/coverage-genealogy-delta`, exact head
`a520556ac7f30290a11e1fcba7b6f6a24269153e`. Its remote `SHA256SUMS` was read back before pass-one generation. The incremental patch must be applied only to that exact head.

This pass-one update was **not pushed**, in accordance with the user's instruction. The accompanying patch is incremental against PR #712 head
`a520556ac7f30290a11e1fcba7b6f6a24269153e`; the ZIP contains the complete
replacement `review/2026-08-22/coverage/` tree.

Suggested publication commands for an authorized writer:

```bash
git switch review/2026-08-22/coverage-genealogy-delta
git reset --hard a520556ac7f30290a11e1fcba7b6f6a24269153e
git apply reviewer-c-pass1-incremental.patch
python3 review/2026-08-22/coverage/replay/validate_packet.py
python3 review/2026-08-22/coverage/replay/light_fraction_fixtures.py
python3 review/2026-08-22/coverage/replay/cross_review_followup_fixtures.py
python3 review/2026-08-22/coverage/replay/validate_pass1.py
git add review/2026-08-22/coverage
git commit -m "review: resolve Reviewer C pass-one heads, genealogy, and issue archaeology"
# Update draft PR #712; do not merge.
```

## Acceptance check

`validate_packet.py` enforces:

- all required files and exact TSV headers;
- all PRs #375–#707 present exactly once;
- every row has a permitted disposition;
- unresolved exact heads fail closed to `TARGETED_REVIEW_STILL_REQUIRED`;
- PRs #708/#709 do not appear as research claims;
- computation rows declare `HEAVY_CAMPAIGN_NOT_RE_RUN`;
- RH status remains unproved;
- duplicate IDs and malformed SHA fields are reported rather than normalized.

## Cross-review follow-up inputs

Reviewer D must additionally consume:

- Reviewer A cross-review PR #710 at
  `e91d6aa25d2e8576e82d26170127941eec430f75`;
- Reviewer B cross-review PR #711 at
  `27784928fbcecff975bc947e13c3a30d3b630ce0`;
- `CROSS_REVIEW_FOLLOWUP.tsv` and `CROSS_REVIEW_FOLLOWUP.md`.

The follow-up adds no new research census range and changes no A/B verdict by
fiat. It path-pins omitted local theorems, sharpens PR #620’s first broken
arrow, and supplies exact heavy-campaign records for PRs #508 and #630.

For an existing Reviewer C branch at PR #712/head
`a520556ac7f30290a11e1fcba7b6f6a24269153e`, apply the accompanying incremental
patch, rerun all four light scripts, and commit only the
`review/2026-08-22/coverage/` tree. Do not merge and do not claim RH.


## Reviewer C pass-one update

Apply this packet incrementally to PR #712 at exact head
`a520556ac7f30290a11e1fcba7b6f6a24269153e`.

New consumption order:

1. load `HEAD_RECONCILIATION.tsv`;
2. apply `PASS1_TARGETED_REVIEW.tsv` to PRs #399–#499;
3. import only material/control rows from `ISSUE_CENSUS.tsv`;
4. use `PASS2_BACKLOG.tsv` as the bounded next Reviewer C queue;
5. run the updated validator.

Pass one reduces targeted rows from 149 to 67 and blank heads from
154 to 72. No heavy campaign was rerun. Do not merge and do not claim RH.


## Reviewer C final pass

The final incremental packet applies to PR #712 at exact head
`899d5efc37025b84a03f231fd6006a2b7a97e6e3`. It resolves all 73 rows in the
former `PASS2_BACKLOG.tsv`; 72 actual PR heads/titles are pinned and #417 is an
explicit no-object sequence gap. `PASS2_FINAL_REVIEW.tsv`,
`FINAL_HEAD_RECONCILIATION.tsv`, `FINAL_REPORT.md` and
`FINAL_CLOSURE_MAP.md` are normative.

Run:

```bash
python3 review/2026-08-22/coverage/replay/validate_packet.py
python3 review/2026-08-22/coverage/replay/light_fraction_fixtures.py
python3 review/2026-08-22/coverage/replay/cross_review_followup_fixtures.py
python3 review/2026-08-22/coverage/replay/validate_pass1.py
python3 review/2026-08-22/coverage/replay/validate_final.py
```

Do not merge this review PR as a proof claim. RH remains unproved.
