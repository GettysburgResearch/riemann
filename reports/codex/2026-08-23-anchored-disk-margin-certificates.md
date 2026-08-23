# Anchored variation and finite-disk quotient-margin certificates

Date: 2026-08-23

Checkpoint base: b52e4b4dceefb0b6c56b0ffe303d4ca01ffe9c56

## Outcome

The absolute-envelope fork now has finite certificate formats rather than an
unnamed lower-bound obligation.  For either programme denominator
\(G=L\) or \(G=LA\), the exact margin is an anchor value times the exponential
of its downward log drop.  Total log-modulus variation provides a sufficient
upper ledger.

A second format covers an edge by disks and proves a positive margin from
center values and derivative enclosures.  Its positive slack is noncircular:
it authenticates nonvanishing rather than assuming it.

## Normalized-derivative inputs

Writing

\[
L=F'/F,\qquad A=F''/F,\qquad B=F'''/F,
\]

gives

\[
L'=A-L^2,
\qquad
(LA)'=A^2+LB-2L^2A.
\]

Thus the first three normalized derivatives are the exact finite local data
needed by a first-derivative disk implementation.

## Exact fixtures

For \(F_0=e^{z-z^2/8}\) on \([0,1]\), the first and product margins are
\(3/4\) and \(15/64\), with exact anchor-drop ratios \(4/3\) and \(16/5\).
Two radius-\(1/4\) disks recover the first margin exactly and certify the
product margin by the rational slack \(841/4096\).

The product firewall keeps the first margin bounded away from zero while the
product margin collapses.  A separate real-even \(Q_S\) family keeps the
complete first manifest, target residue, first selector, and every prescribed
anchor value fixed while both denominator values collapse between anchors.

## Prior-art audit

No L/T/R/M/X-105111 collision exists across the current tree or fetched
refs.  The closest antecedents are L/T-105109, which identify the missing
margins; L/T/R-105110, which develop the alternative oriented-cancellation
route; draft PR #720 L-104521, which reduces a limiting vertical flux to
horizontal argument variation without bounding this edge; and L-91009, which
assumes an upper zeta log-derivative bound in a different annular Pick
problem.  Across-ref L-91810 and L-20001 contain classical completed-Xi
logarithmic-modulus identities, not reciprocal denominator or disk-margin
certificates.

Logarithmic integration, line-segment derivative estimates, and disk-cover
reasoning are classical.  Novelty is claimed only for their exact
denominator-specific placement in this programme.

## Exact authentication

    PASS_T105111_ANCHORED_DISK_MARGIN_CERTIFICATE
    19 focused tests in normal and optimized Python
    7bafdd3d8fb379e8d8de2cd30df8b96331378d7e4f244bb801439493a2e132cd

No numerical quadrature or heavy computation is used.

## Remaining gate

A Xi application needs authenticated anchors, \(F\)-zero-free disks,
denominator holomorphy, rigorous
normalized-derivative enclosures, cofinal variation or positive slack, and
absorption of selector growth and changing edge length.  The alternative
principal-part/remainder route of T-105110 remains open.  Both routes must
still feed correction, multiplicity-defect, and strict-coherence ledgers.
RCMV104530 and RH remain open.
