# Post-integration scientific review — pass 1 of 2

**Review only. Not an integration branch, release, or change to the accepted scientific baseline. RH remains unproved.**

Scientific reference: September 6 integration PR #800, merge `4f461e5ad46e452b1eafa69eddff3b76cd0c12be`. Current main inspected: `c07aa6adcb1e8afa8bac4c5d6f921a822629b236`, including its subsequent cumulative presentation, contribution guidance and maintenance changes. This review preserves that public-facing organization.

Read [REPORT.md](REPORT.md) for mathematical findings, [CENSUS.tsv](CENSUS.tsv) for packet coverage, [CLAIMS.tsv](CLAIMS.tsv) for component recommendations, [DEPENDENCIES.md](DEPENDENCIES.md) for the remaining logical premises, and [PASS2.md](PASS2.md) for the unfinished review work. [SOURCE_FREEZE.json](SOURCE_FREEZE.json) resolves the source keys used in the census; [SOURCES.tsv](SOURCES.tsv) identifies the inspected proof files. [VALIDATION.md](VALIDATION.md) records actual reviewer computations and limitations.

## Coverage at this handoff

Ten research PRs and one branch-only deposit contain **39 identified packets**. Twelve packets received substantive paper review in this pass; 27 remain at inventory/triage depth. The twelve are not blanket approvals of all supporting files in those packets. In particular the length-one positivity and intrinsic-entropy numerical certificates have not been independently replayed here.

The important new components include an all-scale Jordan density argument, a logarithmic operator core and convergent strong-residual construction, target-dependent approximation to the actual source-space floor, square-grid localization of prime discrepancy, an all-rank rational spectral classification, and precise limits on stability-based closure. The report explains what each actually changes and what it does not prove.

Fresh reviewer-written code reconstructs finite algebra and the complete finite torsion classification: **14,926 checks pass in both ordinary and optimized Python**, with identical outputs. That is not a count of theorems, an author-certificate replay, or a machine verification of the analytic arguments. No complete repository checkout, Lean build, historical research campaign, or CI success is claimed.

## How to use this review

All recommendations are provisional input to the second review pass and a later user-requested integration. They do not edit canonical statuses or authorize merging entire research branches. Review depth, mathematical scope, source version and execution evidence are separate fields. An author file named `REVIEW.md` is not independently accepted review evidence.

The fresh derivations and checker implementation provide methodological independence; a common agent name or GitHub account does not establish a distinct non-author referee. Do not count this packet as an additional non-author vote for a contribution whose authorship overlaps the reviewer. Resolve that provenance at the component level under the existing review policy rather than inventing a new approval bureaucracy.
