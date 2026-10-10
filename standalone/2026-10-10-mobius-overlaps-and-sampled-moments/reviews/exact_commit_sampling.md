# Exact-commit seal of the independent sampling-proof review

**Decision: PASS, with the original scoped mathematical review unchanged. No blocker was found.**

Reviewer: moment-obstructions subagent, a nonauthor of the sampling manuscript. This receipt binds the previously completed sampling-proof review to the exact published source of draft PR #926. It does not add a checker-code review or a test replay.

## Published source

- Repository: GettysburgResearch/riemann.
- PR: [#926](https://github.com/GettysburgResearch/riemann/pull/926).
- Exact source commit: [a0a31c4f9775c5516a78d5c9eb69088b9c83595a](https://github.com/GettysburgResearch/riemann/commit/a0a31c4f9775c5516a78d5c9eb69088b9c83595a).
- Release-designated source tree: 5082fe79296a9d701bef4e8e88691b80e818cb33.
- Packet prefix: standalone/2026-10-10-mobius-overlaps-and-sampled-moments/.

The three files below were independently fetched from GitHub with that exact commit as the ref. For each returned content string, its UTF-8 bytes were used to recompute SHA256 and the Git blob identity, SHA1 of the Git blob header followed by those bytes. Every recomputed Git blob equals the blob returned by GitHub. All three fetched byte strings also equal their released local counterparts. The source tree is recorded from the release binding; the independent checks in this receipt authenticate these three commit-pinned files, not a reconstruction of the entire Git tree.

## Verified file identities

Paths in this table are relative to the packet prefix above.

| Path | UTF-8 bytes | SHA256 | Recomputed and GitHub-reported Git blob |
| --- | ---: | --- | --- |
| SAMPLED_MOMENT_CRITERION.md | 28,877 | 18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de | ccb083b8bfd2e3c015c9a8aad5b27ba2754243a4 |
| checks/check_scale_sampling.py | 14,469 | 1d1133e4f920b0e5c350ffc661d37bd7f852e53609a0a13e9400dc09133bdbe5 | 8d077b27784962d18f2dcc59394addfca6d53726 |
| results/scale_sampling.json | 3,459 | bff9dbf6e96007dcca74a4dda275a7f1b1ec7fcce4c77d40008660d3c0eb09a9 | 3e5598014f3710519ed13d8e560298d10726b77a |

The proof SHA256 is exactly the source reviewed before publication. The checker and result SHA256 values also match the released PROVENANCE.json identities. The fetched result internally names the same checker SHA256 and the same associated mathematical-note SHA256.

The result records status PASS and 21,950 checks. Those are authenticated contents of the fetched result, not claims that this reviewer reran or independently audited that checker. This sealing task performed identity and binding checks only for the checker/result pair.

## Prior nonauthor review being sealed

The complete earlier report is the [published full sampling review](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/sampling_review.md), SHA256:

    c97fb1caaad6d1fe803e800dd020ea92624e9833b8e8452f83f7c2f6b3dfba94

That report reviewed the full manuscript at SHA256 18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de. Its PASS covered the infinite-convolution detector and quantitative derivative bounds; measurable-set and discrete-grid interpolation; the growing interpolation-degree choice; fixed-lower-height recovery; the measurable stepwise sixth-power replica cutoff; the stated conditional Mellin extraction; one-sided signed sampling; and the wide-modulation aperture limitation.

Since the fetched published mathematical source is byte-identical, that exact scoped PASS now applies to SAMPLED_MOMENT_CRITERION.md at commit a0a31c4f9775c5516a78d5c9eb69088b9c83595a. The receipt does not extend the review to other packet manuscripts, later commits, imported analytic proofs, or the finite checker implementation.

## Retained premises and open arithmetic

The elementary sampling results use the fixed test's explicit derivative growth, ideal counting, and interpolation. They recover an integral with the common row budget \(X^h\) on \(D\in[X,2X]\); they do not silently interpolate across moving row-entry endpoints.

The moment-to-zero implication remains conditional on the sampled arithmetic moment bound, or on the one-sided sampled signed-remainder upper bound that supplies it. The fixed-row replica cutoff has the stated lower bound by a constant multiple of \(D^{h/6}\), and the source causal moving-cutoff theorem remains an identified analytic dependency. Higher-order compositions retain the inherited native second-moment premise. A cofinal reflected critical-line conclusion also retains the specified family and contragredient coverage.

Neither the published proof nor this receipt establishes the missing sampled Möbius/sextic arithmetic estimate, a full short-row generalized moment hierarchy, a new zero-free boundary, or RH. The wide-modulation result retains its aperture loss and does not supply a fixed-test substitute.

**Final scope:** exact published-source identity confirmed; the prior nonauthor sampling-proof PASS is sealed to that identity; no new mathematical or computational review scope is claimed.
