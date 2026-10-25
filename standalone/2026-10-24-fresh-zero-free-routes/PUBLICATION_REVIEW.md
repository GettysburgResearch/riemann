# Exact-commit publication and source review

Reviewer: `family_escape`. Review date: 25 October 2026.

**Disposition:** the remote mathematical packet matches the reviewed local
bytes and manifest. Its exact commit adds only the stated exploratory
packet. No source mismatch, omitted packet file, or unreported alteration
of the base tree was found. One minor README presentation defect was
detected and corrected as the separately identified editorial delta below;
the correction changes no mathematical statement.

This is a publication/source verification, together with remote spot-reads.
The earlier mathematical reviews retain their own scopes and authorship
disclosures. This report does not establish any of the open analytic
estimates or a new zero-free region.

## 1. Exact remote object reviewed

| Object | Identity |
| --- | --- |
| Repository | `GettysburgResearch/riemann` |
| Mathematical source commit | `742e952be4ef7843de86ea12678c0bdd3d3579c3` |
| Complete source tree | `804d396a70edb41a81fde61dfbdadf2c193a81be` |
| Sole parent and comparison base | `f99d9e3908dde4865377c75d9ca051c1f545bf4f` |
| Packet directory | `standalone/2026-10-24-fresh-zero-free-routes/` |
| Branch at review | `research/fresh-zero-free-routes-20261024` |
| Pull request | [#1021](https://github.com/GettysburgResearch/riemann/pull/1021), open draft at review |

The [mathematical commit](https://github.com/GettysburgResearch/riemann/commit/742e952be4ef7843de86ea12678c0bdd3d3579c3)
was fetched independently from GitHub's Git commit endpoint. The returned
commit has exactly the tree and sole parent shown above. The remote branch
ref and PR head both pointed to this same mathematical commit when read.

The complete recursive tree was fetched independently from GitHub, not
inferred from the publisher's description. The response contains 1,043
tree entries and reports `truncated=false`. The local repository's HEAD
and HEAD tree also match the two remote identities above; its worktree
was clean before this review-only file was created.

## 2. Additive-change verification

GitHub's compare operation from the exact base to the exact mathematical
commit reports one commit ahead, none behind, and exactly 30 changed files.
Every change has status `added`, zero deletions, and a path under the
packet directory. The PR independently reports 30 changed files and zero
deletions.

The remote recursive tree contains exactly 30 packet blobs, all regular
mode `100644`. There are no additional packet files omitted from the
local inventory, and no local packet file omitted remotely. Existing base
files, including the integrated mathematics and repository instructions,
are unchanged by this source commit.

This file was not present in that mathematical commit. It is a later
review addition that refers to the frozen source rather than rewriting
its identity. Its accompanying typesetting correction and corresponding
manifest change are described separately in Section 5.

## 3. Complete manifest and blob verification

Before the Section 5 editorial correction, I independently recomputed
from each frozen local packet file's raw bytes:

- its byte count;
- its SHA-256 digest;
- its Git blob SHA-1, including the `blob <length>` header and NUL byte.

All 29 manifest rows match those computations. For every row, the remote
tree's blob identity and size also match. The manifest intentionally
excludes itself and any later publication-only review; its own local
blob was checked against the thirtieth remote entry separately.

| Manifest identity | Value |
| --- | --- |
| Byte count | `7247` |
| Git blob SHA-1 | `0c4c2e73dd150304a4bf71864f6e9179b8ade969` |
| SHA-256 | `6bdd7ff22a1fc854f6d78f464972e8c205a96dab6dfe321272215f66a01d49ef` |

Thus all **30 remote blobs** match the complete local source packet,
and all **29 manifest rows** pass both digest and size checks. These
identities authenticate the source bytes; they do not authenticate an
analytic theorem merely because the bytes have hashes.

I also matched the previously frozen hashes for the eleven principal
mathematical and overview notes against the published manifest and
remote blobs. They agree with the exact file identities recorded in the
component reviews. In particular the logarithmic-transport note is the
corrected version specifying unitary zero extension, all positive
shorter scales, and a common omitted-prime Euler convention.

## 4. Remote spot-reads

The following four files were fetched as full raw text from GitHub at the
exact mathematical commit. Their raw decoded text matches the local
source, independently of the tree/blob comparison. I read the full
overview and the indicated load-bearing passages from these remote
responses.

| File | SHA-256 | Passages read remotely |
| --- | --- | --- |
| `README.md` | `6eb134b9230eb8a434042f1ab12f68660585acbe2a6d2ecde93bd2cb10320a11` | Complete overview, conditional consequences, source qualifications, finite experiment scope, and next steps |
| `POSITIVE_MARKED_COUNT_TARGET.md` | `18e58007abfa604c3e884e60b4721e6b15c86e63335e23c147dcff13364540af` | Elementary disk, principal subtraction, real-integral formulas, Mellin continuation, and both monodromy criteria |
| `arithmetic/COEFFICIENT_CONTINUATION.md` | `3df080e36d31d6862d290e165adc199428289a9689fcaae98338d30c3a7e85fd` | Positive-measure interpolation, pointwise-constant transfer, fixed-power saving qualification, and centered moments |
| `spectral/THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md` | `783c98402482a109d3ebf5743792f3c6cb15cc1d17efe519014e65aa5c98196b` | Deep-shift theorem, operator-domain and resolvent estimates, nearby-zero argument, and remaining selection scope |

The remote texts retain the distinctions accepted in the component
reviews. In particular the marked-count error estimate is open; the
coefficient moment remains an assumption; the deep-shift obstruction is
confined to its proved regime; and normality does not identify Xi. The
README explicitly states that no smaller zero-free boundary is proved.

## 5. Separately identified typesetting correction

The frozen README contains a literal carriage-return byte `0x0D` at
zero-based byte offset 5805, in the displayed sixth-power-free row
formula. It occupies the position where the LaTeX command `\rm` was
intended. At the publisher's request I replaced exactly that one control
byte with the two bytes for literal backslash-r, retaining the following
`m` and every other byte exactly. This restores the intended LaTeX
command and changes no mathematical statement.

This was detected by comparing raw text with universal-newline reads;
the latter silently convert that byte to a newline. An explicit scan of
all 30 packet files found no other control bytes outside tab and newline.
The remote README contains precisely the same byte as the frozen local
file, so this is a presentation defect in the source rather than a
publication mismatch.

| README identity | Frozen source | Corrected typesetting |
| --- | --- | --- |
| Byte count | `10459` | `10460` |
| Git blob SHA-1 | `9aff63b7c5e749372b19de717cb6d496db7b7655` | `8077b343dcd385c6a62bd96c459731b686c9420e` |
| SHA-256 | `6eb134b9230eb8a434042f1ab12f68660585acbe2a6d2ecde93bd2cb10320a11` | `6de255a9bb25d7f6e08f2dd34d6b3fd8cd1aa5e822b9115fe10590d93218cdd8` |

Only the README row's byte count and two hashes were updated in
`MANIFEST.json`; the other 28 file entries and all manifest metadata
remain identical. The corrected manifest is 7,247 bytes, with Git blob
SHA-1 `544829beb31ac92eadd3613c7d135540da0b93e6` and SHA-256
`e21bfe3aaf487524c7f7d7016201e3cbca26723cc2fe235d9d5f77fe86532c0e`.

The intended follow-up has exactly three changed paths: this new review,
the README typesetting correction, and its manifest row. Every
load-bearing mathematical note, checker, output, source list, and
previous review remains byte-for-byte identical to the frozen
mathematical commit. The prior overview review keeps its original hash
binding; this report separately reviews the specified editorial delta.

This report continues to bind the exact original mathematical commit.
The remote identity and exact three-file diff of the subsequent
publication follow-up must be checked separately after it is published.

## 6. Mathematical review and replay boundaries

The earlier reports are physically present in the verified source:

- `family/ARITHMETIC_CONTINUATION_REVIEW.md` independently reviews the
  three arithmetic notes at their recorded hashes.
- `family/FINAL_SPECTRAL_REVIEW.md` independently reviews the specified
  spectral arguments and explicitly discloses the reviewer-authored
  variance bound and prescribed-strip quartet.
- `family/OVERVIEW_REVIEW.md` checks the overview, displayed finite
  values, and source descriptions at their frozen hashes.
- `arithmetic/POSITIVE_MARKED_COUNT_REVIEW.md` records the separate
  arithmetic agent's review of the marked-count construction.
- `reviews/SPECTRAL_AGENT_FAMILY_AND_SEXTIC_REVIEW.md` records a
  separate agent's review of this reviewer's two family notes and the
  finite sextic experiment, with exact final hashes.

I authored the family reductions and the two disclosed spectral lemmas;
this publication review does not turn my authorship into independent
mathematical review of those contributions. The component reports also
distinguish agent review from external peer review and formal verification.

This publication pass recomputed source identities and checked remote
publication. It did not rerun the numerical/finite checkers, reprove
every component, verify the complete imported preprints, or promote
exploration to the integrated accepted record. Prior replay results and
their independent arithmetic checks remain exactly those stated in the
verified component reports and receipts.

No remote mutation was performed by this reviewer. The only repository
paths touched during this publication pass are this review, the
specified README typesetting correction, and the README manifest entry.
