# Integration handoff to Reviewer D

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
`2b35d2b159a4c7af045ffca9214aebe02a423da4`. Its remote `SHA256SUMS` is
byte-identical to the pre-follow-up packet used as the base of this patch.

This cross-review follow-up was **not pushed**, in accordance with the user's
instruction. The accompanying patch is incremental against PR #712 head
`2b35d2b159a4c7af045ffca9214aebe02a423da4`; the ZIP contains the complete
replacement `review/2026-08-22/coverage/` tree.

Suggested publication commands for an authorized writer:

```bash
git switch review/2026-08-22/coverage-genealogy-delta
git reset --hard 2b35d2b159a4c7af045ffca9214aebe02a423da4
git apply reviewer-c-cross-review-followup.patch
python3 review/2026-08-22/coverage/replay/validate_packet.py
python3 review/2026-08-22/coverage/replay/light_fraction_fixtures.py
python3 review/2026-08-22/coverage/replay/cross_review_followup_fixtures.py
git add review/2026-08-22/coverage
git commit -m "review: reconcile cross-review omissions in Reviewer C packet"
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
`2b35d2b159a4c7af045ffca9214aebe02a423da4`, apply the accompanying incremental
patch, rerun all three light scripts, and commit only the
`review/2026-08-22/coverage/` tree. Do not merge and do not claim RH.
