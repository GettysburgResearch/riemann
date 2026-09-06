# Integration history and source lifecycle

The [August 22 scientific release](integration/2026-08-22/README.md) remains immutable and covers research through PR707 at its recorded source versions. Formal-v0.1 was a separate formalization release; PR794 subsequently added contributor onboarding without integrating newer research.

The [September 6 integration](integration/2026-09-06/README.md), PR800, consolidates A #795, B #796, C #798 (including its newer mathematical supplement) and D #799 (all four passes). C #797 is the earlier scaffold, not a second completed review. Exact reviewer trees are preserved under `reviews/`; original research branches are not bulk-merged.

The [prior detailed chronological ledger](https://github.com/GettysburgResearch/riemann/blob/8d16f8d9c475db290bc85e53d775b93b9bcdb336/HISTORY.md) is preserved at the exact baseline and copied in this release's [previous-frontdoor archive](integration/2026-09-06/previous-frontdoors/README.md). Its numerical claim IDs must be interpreted with their PR, commit and path because historical namespace collisions exist.

## Lifecycle rule

An exploratory deposit, a reviewed theorem, a conditional adapter, a retained certificate, a refuted mechanism and an unreviewed source are different dispositions. Closing a review PR as incorporated means its evidence was preserved and reconciled; it does not mean every research claim it discusses was accepted. Source branches and old failures stay reachable. A repair receives a new identity rather than rewriting the reviewed past.

The [C census](reviews/C/CENSUS.tsv) retains its original coverage and omissions. New review/publication records are tracked in the [integration lifecycle file](integration/2026-09-06/PR_DISPOSITIONS.tsv). It does not pretend to complete C's unperformed full branch/attachment/dependency archaeology.
