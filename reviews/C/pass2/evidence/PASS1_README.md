# Independent Reviewer C first-pass audit

Review PR #798; branch `review/C/2026-09-05-post-release-audit`.
Baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.

**Public-release readiness is not cleared. This is not a complete-coverage certificate.**
The 566-row census inventories 341 previous release rows (340 PRs and an explicit
no-object slot), 79 post-review-cut PRs, all eleven programme issues, selected
claim/deposit/external splits, direct-main history and explicit gaps.
Only 28 old heads were freshly compared; 312 remain unperformed. Most later PRs
have metadata-level coverage. Complete claim splits, branch/attachment closure,
formal statement/build coverage and permissions/history review remain incomplete.
These are C's coverage debts, not A/B failed reviews. A/B scientific dispositions
are **pending integrator reconciliation**. No unpublished report was a dependency.

Read `VALIDATION.md` for inspected sources, exact evidence and unperformed checks;
`RELEASE_BLOCKERS.md` for confirmed defects and owner-only gates;
`STRUCTURE_AND_EXTRACTION.md` for concrete schemas, documentation and extraction order.

## Reproduce the bounded checks

From repository root, in a disposable working copy:

```sh
python reviews/C/check_census.py
python -O reviews/C/check_census.py
python reviews/C/replay/scripts/replay_consumer.py
python reviews/C/replay/scripts/replay_axiom_parser.py
```

The census command checks structure and the DECLARED denominator, not complete
review coverage. Both replay drivers authenticate their frozen target bytes before
execution and use only reviewer-created bounded fixtures in temporary directories.
They write new execution receipts into `replay/reports/`; use a disposable copy to
preserve the original receipts. Exact stdout/stderr includes run-specific temporary
paths. Compare acceptance outcomes rather than assuming byte-identical rerun logs.
No Lean, compiler installation, network request or broad scientific campaign is run.
The consumer driver records the six observed cases in both modes; the parser driver
also checks its ten expected outcomes in both modes. Neither is a mathematical proof.

## Frozen source copies

`evidence/REVIEWED_PR_CENSUS.tsv` is the original blob
`0c49ffb662312f402097b576b399e50b642fdfa2` from PR #712 at
`a6aa936ba8bf538177e34af60db7e2f0a58f8dfd`.
`evidence/RELEASE_MANIFEST.json` is main's original manifest blob
`446aec7e1c6d7b1d40a7747f3c9b161d03efdad3`.
`evidence/REVIEWED_CLAIMS.tsv` is main's original claim manifest blob
`6a4157460bf0044c6e110a2713f7dfb62bcb6c28`.
They are copied unchanged, not newly reviewed or generated acceptance records.

The two Python targets under `replay/references/` are exact archived copies of the
baseline repository files, including the consumer's deliberately preserved flawed
acceptance behavior. They are not repairs and are not imported into production.
Main, original research branches, permissions and settings were not changed.
A read-only metadata export workflow was briefly added on this branch, no run was
observed, and it was removed; the final diff contains only `reviews/C/` files.
