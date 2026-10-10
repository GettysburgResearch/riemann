# Bounded relationship check against the subsequent moving-label packet

Result: **the frozen overlap proof, its exact pinned comparisons, and its stated remaining gap remain accurate. No proof change is needed.**

Scope of this check: a complete read of the README and the matching/overlap manuscript below, at the exact PR #924 head. This is a source-relationship check, not an independent review of that packet's analytic proofs, theta framework, or new external sieve.

## Exact sources

Repository: GettysburgResearch/riemann. PR #924, commit:

    725b2d25ab47e57500049d93985560098c7ef3fa

Both files were fetched from that exact commit, verified against their Git blob identities, and materialized without byte changes at their repository paths under the local riemann checkout.

| Repository path | Git blob | Bytes | SHA256 |
| --- | --- | ---: | --- |
| standalone/2026-10-10-sextic-moving-labels/README.md | 72fca43dba97f3e751647ef23311487903d64a26 | 13,165 | 180f373a0d245a188f2a2b393a7f7f19411a6486c2f8f0d1130414665e787563 |
| standalone/2026-10-10-sextic-moving-labels/CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md | 4bdc8aeed00538360d8365f6b7ad99915221a803 | 24,368 | 9dc37104e3a06c11d11f48d4e3cb2a6653b64c844aa4c316c8bf1f2cd93d9d05 |

## Relationship to the double-triangle result

Theorem 4.1 of CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md controls prescribed disjoint cross-side matching events \(N(n_i,m_i)\ge T\), allowing bounded one-sided selectors that depend only on shared incidence labels. The theorem explicitly imposes no further cross conditions. For \(m\le k-1\) matching edges, writing \(T=D/R_{\rm match}\), its bound is
\[
H D^{k+(2b-1)(k-1-m)+\epsilon}R_{\rm match}^{(2b-1)m}.
\]
A full matching has the corresponding \(k-1\)-edge cost.

Our sixth-moment double-triangle block has six within-side pair ideals and no cross-side shared prime. Every cross-side gcd is exactly the unit ideal. Consequently it is absent from every nonempty matching event with \(T>1\). At \(T=1\) the matching constraints impose no restriction, and the stated theorem retains the ordinary power loss; it does not assert a diagonal estimate for this block.

Our higher-order embedding adds exactly \(k-3\) matched cross pairs of norm comparable to \(D\), leaving the same two triangles on three unbarred and three barred positions. Applying the new matching theorem with \(m=k-3\) and bounded \(R_{\rm match}\) gives an excess \(2(2b-1)\), equal to \(3/2\) at \(b=7/8\). Our grouped cubic argument supplies an additional estimate for that remaining six-factor incidence configuration, reaching diagonal size at the displayed grouped cutoff. These are complementary sector statements.

The comparisons in the frozen overlap manuscript explicitly concern PR #921 and PR #923 at their stated exact commits, for the matched double-triangle configuration. They remain correct. This check does not describe those pinned sources as the latest state of the repository.

## Fourth-moment and A2 relationship

Theorem 6.1 of the new matching manuscript handles the complete union of four fourth-moment cross-gcd events, including every intersection. It removes the earlier disjoint-event restriction and is uniform in the within-side cutoff \(C\). It therefore addresses restrictions different from our sharper within-side common-factor tail. Our proof does not depend on this newer theorem.

The new README also states a full normalized A2 bound of \(D^{31/19+\epsilon}\) at arithmetic row height \(H=D^{1/2}\), with all correction labels summed under its source hypotheses. Its Sections 6 and 7 expressly retain the exact signed first-Poisson remainder as open: that object has two independently corrected columns, a coupled row kernel, a strict off-diagonal restriction, and a signed auxiliary sum. The matching manuscript's Section 8 likewise retains the balanced mutually separated fourth-moment and higher-moment sectors as open.

Accordingly our remaining-gap statement—long singleton sextic cores or the signed long-conductor average that covers them—is consistent with this new packet. The full A2 result should be acknowledged as subsequent progress, without treating it as a proof of the initial signed long-dual moment.

## Suggested README/provenance wording

After freezing the overlap manuscript, we checked PR #924 at commit 725b2d25ab47e57500049d93985560098c7ef3fa. Its full moving-label A2 estimate and complete cross-gcd/matching sectors are additional source-qualified progress. The new double-triangle sector here has no cross-side matching edge; its higher-order embedding leaves three unmatched pairs after the new matching theorem is applied. Our exact comparisons with pinned PRs #921 and #923, and the remaining signed long-conductor gap, are unchanged. No proof in this packet imports PR #924's separately credited 4/7 spectral-sieve extension.

The frozen overlap proof remains bound to SHA256:

    980c0e5d4e82e4c6105a21db37aeeb84ff19da9c985be571002fe4f3e9bfba04
