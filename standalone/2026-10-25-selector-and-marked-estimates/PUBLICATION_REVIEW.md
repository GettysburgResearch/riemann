# Publication binding review of the frozen second-pass packet

Date: 25 October 2026.

Reviewer: `fractional_attack`, a separate agent from the root author who assembled and uploaded the Git tree.

**Verdict: PASS for exact publication binding at the immutable commit below.** Every new remote blob matches the local raw bytes, all manifest entries match, the previous repository content is preserved, and the component-review hashes bind the published mathematical notes.

## 1. Authorship disclosure and review scope

I authored the two fractional notes and wrote the earlier independent mathematical review of the three marked notes. I therefore do not present this publication check as a new independent mathematical review of my own work. The separate `spectral_selector` agent reviewed the fractional notes at the exact hashes bound here; the separate marked-count agent reviewed the spectral components. Their reports and the overview review are themselves included in the verified publication.

This report checks the immutable Git objects and their relationship to the local files, frozen manifest, and earlier review receipts. The mathematical dispositions and their qualifications remain those of the component reviews. The packet explicitly records `new_zero_free_region_claimed: false`.

Only GitHub read operations and local read-only checks were used for verification. My only local write in this publication-review task is this report. I performed no remote write, branch update, commit, index mutation, or change to the mathematical packet.

## 2. Commit, tree, and parent independently read from GitHub

| Object | Verified identifier |
|---|---|
| Frozen mathematical commit | `0f07049ff1e8cc7765f6de01b4e176ad627bba4b` |
| Complete repository tree | `6ecae1638e1552b018977202679f874bd2d4c065` |
| Sole parent commit | `a00d68e9f0e7ada5462e6be45c123cfaa6b3ffb0` |
| Parent repository tree | `64273a5ab57c6ca56dd2be20eaf87c382b81f09b` |
| New packet subtree | `cd16a6c3152903d672b523fdbfde0eac7d9a4744` |

The GitHub Git-commit response has exactly one parent, with the identifier shown above, and names exactly the displayed complete tree. I read the [frozen commit](https://github.com/GettysburgResearch/riemann/commit/0f07049ff1e8cc7765f6de01b4e176ad627bba4b), its [Git-commit object](https://api.github.com/repos/GettysburgResearch/riemann/git/commits/0f07049ff1e8cc7765f6de01b4e176ad627bba4b), and the [parent Git-commit object](https://api.github.com/repos/GettysburgResearch/riemann/git/commits/a00d68e9f0e7ada5462e6be45c123cfaa6b3ffb0) through the connected GitHub read tools.

I separately fetched the recursive [new tree](https://api.github.com/repos/GettysburgResearch/riemann/git/trees/6ecae1638e1552b018977202679f874bd2d4c065?recursive=1) and [parent tree](https://api.github.com/repos/GettysburgResearch/riemann/git/trees/64273a5ab57c6ca56dd2be20eaf87c382b81f09b?recursive=1). Both responses have `truncated: false`. These checks use the immutable object identifiers, rather than relying on a branch name or the publisher's claimed comparison.

## 3. Exact additive scope and preservation of the parent

The parent recursive tree contains 1,044 entries: 857 blobs and 187 directory trees. The new recursive tree contains 1,074 entries: 881 blobs and 193 directory trees.

Comparing every path, type, mode, and object identifier gives:

- Exactly 24 added blobs, all within `standalone/2026-10-25-selector-and-marked-estimates/` and all mode `100644`.
- Exactly six added directory-tree entries: the packet root, `fractional`, `marked`, `reviews`, `spectral`, and `spectral/source`.
- No removed path, and no changed blob, blob mode, or object type anywhere in the prior repository.
- The only changed pre-existing directory-tree entry is the necessary `standalone` ancestor. Its old identifier is `8baebd4f9dc9f1007981ed69a92086f58e44b2c0`; its new identifier is `0321b81ed2e41bdf7c053c48ea5210c828d1a60e`.

In particular, the complete first-pass packet `standalone/2026-10-24-fresh-zero-free-routes` has the identical subtree identifier `18e46948dfa404c3f9ed00de77f3961f6756d0b4` in parent and child. This binds preservation of its notes, numerical artifacts, manifest, and review report.

## 4. Every remote blob checked against raw local bytes

I fetched all 24 new blobs separately by their immutable SHA through the GitHub blob-read tool. For each UTF-8 result I re-encoded the returned text to bytes, compared it byte for byte with the local file, and independently computed:

- The Git blob identity `SHA1(b"blob " + decimal_byte_length + b"\0" + raw_bytes)`.
- SHA-256 of the raw bytes.
- The raw byte count.

Every remote byte sequence equals its local counterpart. Every computed Git blob identity and byte count equals the corresponding remote tree entry. The 24 files total **219,436 bytes**. No newline normalization or other content transformation was applied during these comparisons.

The following is the complete set of added file paths, relative to the packet root:

| Added file | Bytes | Verified Git blob SHA-1 |
|---|---:|---|
| `fractional/NORM_TWIST_AND_BAND_TRANSFER.md` | 11429 | `8977202773091758ab7515174278769c1f64c583` |
| `fractional/UNIFORM_FRACTIONAL_WINDOW.md` | 10847 | `15378a3d56ec8a0d16ee185f16dbc00482910079` |
| `MANIFEST.json` | 6399 | `30b6cc296fc5781f344c00f68a00895952a6d7b7` |
| `marked/check_marked_convolution.py` | 4492 | `af3be99db0d46e9907b7924916ec5eb74e55aea4` |
| `marked/GEVREY_INTEGER_WINDOW.md` | 10938 | `515016d2041b7264d47d69606115ba451b19f81c` |
| `marked/GROWING_INTEGER_RESONANCE.md` | 12526 | `a7115a0b715be35463387f15a1e5de6b0461cbfe` |
| `marked/marked_convolution_checks.json` | 1838 | `cd8771e35c5e717841a094ee6e7f515b64d26c1f` |
| `marked/MATCHED_PRIME_SQUAREFREE_REMAINDER.md` | 14717 | `5b9947c67f63be3aa7667e23648e9e5fa9786527` |
| `README.md` | 13433 | `48ea62c56ee6209a99a39545ed4e37d7f1b5850e` |
| `reviews/OVERVIEW_REVIEW.md` | 11654 | `5b1a49f149bf9cdd810f2f174292bf22dffda053` |
| `reviews/REVIEW_FRACTIONAL_2026-10-25.md` | 7032 | `aed31e011ff6f1fdeef4aae899ba0edccb195e1d` |
| `reviews/REVIEW_OF_MARKED_COMPONENTS.md` | 11482 | `27b7fd7093f0a20e340a4ef5c269f1e446338276` |
| `reviews/ROOT_REPLAY.json` | 1945 | `ffa7ef41bedb706816280d729391f47320b5d849` |
| `reviews/SPECTRAL_CONSUMERS_REVIEW.md` | 9808 | `f9bf1f857ec0c49d113b1dee8456effc6399bf6a` |
| `SOURCES.md` | 4080 | `bffe9c929e5b7196fc3a9e0cdd3dd9e90932e140` |
| `spectral/EVEN_FINITE_SELECTOR_CONSUMER.md` | 13707 | `916abee0b89a46c7e0d8ba4b5c4d9c562803cb40` |
| `spectral/NUMERICAL_SELECTOR_DIAGNOSTICS.md` | 7002 | `ce74a719d15ead9ff3533d3022a7fa2d47625b9c` |
| `spectral/selector_experiment.py` | 6609 | `eb9377becfe541a7d39698a70647a9af2b81b1aa` |
| `spectral/selector_n16.json` | 15117 | `c2363e94bfb0023d7585d5db83029aaf7d99a49c` |
| `spectral/selector_n32.json` | 11664 | `5c28b3970c46234d35f16d931bcd5729c876eec3` |
| `spectral/selector_root_replay.json` | 3718 | `67dd6d6f933e9dc1b17455a2fa9fbbc4d3f612b7` |
| `spectral/source/experiment.py` | 9128 | `b0d2b2f72fed1db9632fb910f37acb849ba60784` |
| `spectral/source/NUMERICS.md` | 5860 | `ce5d614fcea767f964fa847c7bfdec03bc170b43` |
| `spectral/SPECTRAL_GROWTH_AND_TIGHT_POSITIVE_SELECTION.md` | 14011 | `43f2a7d41e35064e486b05b31eea5a9b0c157c65` |

`MANIFEST.json` contains 23 entries and explicitly excludes itself and a possible later `PUBLICATION_REVIEW.md`. All 23 paths, byte counts, Git blob SHA-1 values, SHA-256 values, and recorded file modes match the raw-byte checks and the remote tree. The manifest plus those 23 files is exactly the 24-file frozen packet.

The manifest itself is independently bound as follows:

| Manifest property | Verified value |
|---|---|
| Bytes | `6399` |
| Git blob SHA-1 | `30b6cc296fc5781f344c00f68a00895952a6d7b7` |
| SHA-256 | `346b36a103e75e40a1301110e4aca4ed78b71d85c5c942d48299363a6d7b4157` |

## 5. Binding the mathematical review receipts

I read the review tables and checked each named target digest against the actual published bytes and manifest. The two fractional notes, three marked notes, and two spectral component notes have exactly the hashes named by their respective mathematical reviews.

| Published review | Published SHA-256 | Bound targets |
|---|---|---|
| `reviews/REVIEW_FRACTIONAL_2026-10-25.md` | `4b5b27ca696a1eb0935c00d24b13820f416ec97e254dad71d5925c0d972604d7` | Both fractional notes, independently reviewed by the spectral agent |
| `reviews/REVIEW_OF_MARKED_COMPONENTS.md` | `9d9dea0fadb325e0a10b3b5a23bffe87f80fc78b83cfde972ebd52dfa73ea7e8` | All three marked component notes, reviewed by me independently of their author |
| `reviews/SPECTRAL_CONSUMERS_REVIEW.md` | `9ce62609098f402074f346a66aabcf3e36258c7734eb546a9ca2a792c5d3ed9b` | Both spectral component notes, independently reviewed by the marked-count agent |
| `reviews/OVERVIEW_REVIEW.md` | `c431315d3770b8f9fd164a8c1ba0204454d9f48353704db40d08e2d5ddab4bd5` | The exact overview, sources, root replay receipt and selector replay, with all seven component digests cross-checked |

The overview review's four directly reviewed object hashes also match the published bytes: `README.md`, `SOURCES.md`, `reviews/ROOT_REPLAY.json`, and `spectral/selector_root_replay.json`. Its references to the component hashes agree with the component reviews and the manifest. The copied source members and numerical artifacts are bound to their published hashes by this check; the earlier source-authentication and numerical-replay conclusions retain the scope stated in their existing receipts.

### Documented one-byte review-file normalization

The overview review names the original spectral review hash `c85345c53b579152893c66897a55c9918aebb7d25827926111f3af719ad5979d`. The published spectral review has the different hash shown in the table. I independently compared the original 9,809-byte review with its 9,808-byte published copy and verified the exact byte identity

```text
original_review_bytes == published_review_bytes + b"\n"
```

Thus precisely one extra final LF was removed. Every other byte is identical, including both reviewed spectral-note hashes and all qualifications. The frozen manifest records the actual published review hash. No mathematical note changed in this normalization.

## 6. Binding limit and follow-up handling

This report binds the exact mathematical commit and tree in Section 2. It is intentionally absent from that frozen tree and excluded from its manifest. A subsequent review-only publication should add this file while preserving all 24 frozen blobs and the parent relationship to the mathematical commit.

The checks above establish the exact publication relationship. They do not supply a missing all-scale arithmetic or spectral estimate, strengthen an imported theorem, turn finite diagnostics into certificates, or establish a smaller zero-free region. Live branch or pull-request head changes are separate operations and were not performed by this reviewer.
