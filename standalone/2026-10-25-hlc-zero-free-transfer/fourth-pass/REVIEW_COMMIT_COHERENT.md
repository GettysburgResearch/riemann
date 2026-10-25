# Exact-commit review: coherent-identity worker

**Verdict: PASS for the immutable object binding and the previously stated mathematical review scopes.** This is an independent internal publication review. It binds five earlier source-hash reviews to the remote mathematical freeze; it is not external peer review, formal verification, or a claim that RH or a new unconditional zero-free region has been proved.

## 1. Immutable publication examined

- Repository: `GettysburgResearch/riemann`.
- Mathematical freeze: [`8b2c6d50ad2d729c681745717c615095bd8f1d9d`](https://github.com/GettysburgResearch/riemann/commit/8b2c6d50ad2d729c681745717c615095bd8f1d9d).
- Root tree: `bca4d3e66472fa7fb4c7f37c56b426359a397cb1`.
- Sole parent: `3a07737bb7b802a5671acaa22a8f86e6b0acbd40`.
- Reviewed directory: `standalone/2026-10-25-hlc-zero-free-transfer/fourth-pass/`.

I fetched the Git commit object by its full SHA, the complete recursive tree by the tree SHA above, and each file below with the full commit as its ref. No branch-name resolution was used for the content checks. The commit object identifies exactly the displayed tree and parent. The recursive tree returned 1,119 entries and explicitly reported `truncated: false`.

From those entries I reconstructed all 187 directory tree objects, including the root. Their Git SHA-1 hashes all matched the returned immutable identifiers. For each of the 14 fetched files, I encoded the returned text as UTF-8, counted its bytes, computed SHA256, and recomputed its Git blob identifier from the literal `blob <byte-count>\0` header and bytes. Every result matched the file response and its path entry in the verified recursive tree.

These are object-identity checks, rather than comparisons of rendered text or matching filenames. The separate project-wide preservation audit covers the earlier repository blobs; this review's independently fetched file contents are the 14 objects listed below.

## 2. Mathematical objects identical to the earlier reviews

The following eleven remote objects are byte-for-byte identical to their earlier reviewed local versions. Each also matches the SHA256 and Git blob recorded in the applicable prior review.

| File | UTF-8 bytes | Git blob | SHA256 |
|---|---:|---|---|
| `DETECTOR_LOCALIZATION.md` | 29469 | `b9a47c8abcea7f2784568b8bf70a811bd57bb814` | `aa77d6158d7997801257f947574c08b9efb3f0cfea0b971dc616289f5ce68917` |
| `check_detector_localization.py` | 14203 | `9055ed771075e197c701f29b4d86fae1107f74e8` | `c91b5d531dd84f7b1d5c69aa70bb1ceb43c2c83a968a9b63c0d1e9f450db00ed` |
| `DETECTOR_LOCALIZATION_CHECKS.json` | 33436 | `a522a9279b867d2e32d1c3c2c7ceb25171b0bf03` | `de85ea08076ae610b3885fae742b8b2412e0d4335474cd3d372397a2dc2faf14` |
| `HLC_PATH_CANCELLATION.md` | 28232 | `adbe598b517ad5c6c45385b4adc5e5e20eba25f7` | `dc806ea8c6b26b6419ae90a3fa8003bd971c7358ed4dba7babb8c82dd8b2fc9b` |
| `check_hlc_path_cancellation.py` | 16340 | `618a293bf2b1c7acb7afd2209d31decc7404dc01` | `92f80b303bf21ebcf60470d85176213b2f76ce36017db3f456b9666ea4b61c58` |
| `HLC_ROOT_AVERAGING.md` | 19671 | `81b749827db0683341b82bab0ebd73a4fb17255b` | `1f3cd6e20936830ee91ab8591c5d289133ecdcdf1339633df3231e47fd8f80b0` |
| `check_hlc_root_averaging.py` | 17477 | `008c5bb5d9cb80e5641761716df623f679f30cbd` | `22ca022f856927eaf1dd9ee9490797c95e941bddf8dc9a0ecddcd8d5a3e04c59` |
| `CLOSED_TRIANGLE_WEIGHT.md` | 15616 | `999510900504d8ee0e3e318dc79a856f29e28bd4` | `169112b8b41ede59ba23009e5b23d06184e19c03cad209d40940edf1568f7e37` |
| `check_closed_triangle_weight.py` | 9726 | `9467a1a1766e945e43a66bfe9c3fcc61c39a0840` | `3aed0d03eda009fbe93b2f17de320c89d7ce94b93f5487c843114d9e8d6a6d1b` |
| `COMMON_D_TRIANGLE_EXTENSION.md` | 10714 | `1ec8c0f0444c2d4353454ac2d7a7fce31fd9143f` | `67769f6a6f2a9c6c8beca1aad4c94f7150d71b4d11253515e355df84c3ff7bc9` |
| `check_common_d_triangle_extension.py` | 9256 | `1bdc7ba47731f803739955c40a2dbb4d23150c0f` | `1e449d9aa11395fc9cf6dd76f86cb49ac3a26bf6dd897b079f16217408cfb400` |

The detector report is included because its earlier review checked that exact report as well as the note and checker. Every object in this table is a regular `100644` Git blob at the stated path in the immutable tree.

## 3. Earlier reviews bound to this commit

The source-hash review records being bound are:

| Prior review | SHA256 of the reviewed record |
|---|---|
| `REVIEW_DETECTOR_LOCALIZATION.md` | `9c65321de4488854014c91433e41db19b08d4d1a0a9510ff5888700e2cf5470a` |
| `REVIEW_HLC_PATH_CANCELLATION.md` | `a3d377e44c4727f951d5d18ac98470b66e7718b09c199817c7fe1beabfd27b6c` |
| `REVIEW_HLC_ROOT_AVERAGING.md` | `901b439e84c9d172d3126ce2b1a6098d3a2cc8226f19e7996d3113b651203937` |
| `REVIEW_CLOSED_TRIANGLE_SOURCE.md` | `8bba58f1101a5ad64d482d8d830b188e8524aec2e6e5e8d01b6395be969eb2a7` |
| `REVIEW_COMMON_D_TRIANGLE_EXTENSION.md` | `921e8038a1dad1c97b3f6c24e2475dceef594ec3e6f42640a064d4e4cd1197e1` |

The mathematical freeze contains the mathematical payload; these review records and the present commit-binding record are publication metadata. This document does not imply that a review record was already present in the mathematical-freeze tree.

The earlier review conclusions remain unchanged:

- `DETECTOR_LOCALIZATION.md`: the original native inverse is reduced to the literal primal band with the printed low/high count margins, original character and coefficient scopes, buffered profiles and source exclusions retained. The remaining thin-band count is open.
- `HLC_PATH_CANCELLATION.md`: the finite determinant-operator identities, conditional projection comparison, source-qualified largest-group integer backtrack theorem, and printed phase-separation bound pass at their stated scopes. They do not automatically complete integer paths to a uniform residue bridge.
- `HLC_ROOT_AVERAGING.md`: the exact cofactor lift, CRT grids, once-only recorded-line normalization, actual-root conversion, fixed-family ambiguity bound, conditional-history interface and Eisenstein Haar version pass. The required history density and a native detector root law remain additional hypotheses.
- `CLOSED_TRIANGLE_WEIGHT.md`: the original state, orbit, edge and prime-line weights pay the specified list-diagonal common-shared-list raw triangle. Its conservative discrete version uses the explicitly imported Appendix A.5 estimate.
- `COMMON_D_TRIANGLE_EXTENSION.md`: the collision exclusions and closure congruence pay different endpoint lists as well, proving the full common-shared-list three-edge raw rooted-return bound. Changing shared lists, other return schedules and arbitrary surrounding history are not included.

I authored the scalar closed-congruence theorem in `THREE_EDGE_INTEGER_BRIDGE.md`; I therefore did not describe my source-transfer review as an independent review of that scalar theorem. Its separate independent review is by the HLC worker. Likewise this record does not add an independent proof review of mathematical notes outside the five review assignments above.

## 4. Committed README, manifest and execution record

I also fetched and rehashed the following committed metadata:

| File | UTF-8 bytes | Git blob | SHA256 |
|---|---:|---|---|
| `MANIFEST.json` | 7125 | `e89fdc5685e8c277c15cff2b9d638007f94d37d3` | `1067ba357160e78d76ecb4d8749ab900f7219d53f95781716dd95f339108166a` |
| `CHECKS.json` | 17783 | `5c53e18b25226a10b642991905c7e457d1e71c07` | `0bb7799b1ed1526c0930bf382807d82001fccfd18b9e07b92a9be646502d016f` |
| `README.md` | 20190 | `c31b75a931e1c850a984f7514a1b188d5e1e75d3` | `1d17ecbfaaf47bc3cc00e47eab914c85f6383110be6630794d0998a50f477dcc` |

The manifest contains 29 payload entries, excluding itself and later review/publication records. All 29 listed Git blobs and byte counts match the committed recursive tree. For the fetched files, I additionally checked the manifest's SHA256 against the independently rehashed remote bytes.

The committed `CHECKS.json` records ten successful checker runs. All have return code zero, empty stderr and the displayed `-I -S -B -O` flags. Every recorded checker SHA256 matches the committed manifest. For the five checkers in my reviewed object set, those recorded hashes also match my independently fetched and rehashed remote content. The report records that its 43 third-pass files remained unchanged; the root worker performs the separate repository-wide preservation audit.

I did not rerun the entire suite during this publication binding. The earlier independent checker replays and the root worker's isolated ten-checker run already cover the relevant executions. Here the concrete remaining risk was whether the remote commit contained exactly those reviewed sources and reports; the checks above resolve that risk.

## 5. Scope statements in the committed README

I read the committed README in full. Its principal qualifications are present and consistent with the reviewed objects:

1. It states at the beginning that RH and a new unconditional zero-free region remain unproved, and distinguishes imported native analytic premises from directly proved finite identities.
2. It prints the actual remaining primal band, the narrow parameter box, and the open hypothesis `(W_thin)`. It explicitly identifies `0.8748856` as a conditional target requiring that unpaid estimate and the imported analytic framework.
3. It preserves the natural-character, coefficient, mask, profile and inducing-character restrictions. The large-divisor form is not promoted to a new independent inverse factor; the compensating Möbius signs are stated.
4. It distinguishes complete finite-residue bridge formulas from actual integer path laws, and preserves the preceding-history denominator in the root-average application.
5. It states the correct original raw kernel factor `d_0/D`, without the rejected extra `1/Y` factor. The triangle payment is attributed to the counted integer candidates and once-only prime-line weights.
6. It describes the enlargement from list-diagonal triangles to all common-shared-list three-edge position returns, while leaving changing shared lists, two-edge contractions, centered comparison terms and attached history outside that result.
7. It separates the elementary and classical inputs to the root-count refinement. The elementary input is attributed to the written fourth-moment/Fourier proof; the stronger classical version explicitly imports the Weil--Salié estimate. The separate HLC-worker review covers that refinement's proof.
8. It distinguishes the HLC root scale x from the native detector scale U. Its full-common-D example has the correct elementary discrepancy arithmetic: `(4*1+13)/400-(1/4)*(1/4)=-1/50`, alongside the `x^(-1/800+epsilon)` main term. This does not identify that exponent with a native inverse saving.
9. It states that the signed off-diagonal estimate is still open, that internal reviews are not external peer review, and that finite checkers do not prove the imported analytic inputs or a zero-free conclusion.

The README's claimed stronger root-count theorem and off-diagonal interface belong to their separately reviewed notes. This publication review checks their scope presentation and the displayed numerical example; it does not replace those independent mathematical reviews.

## 6. Acceptance boundary

The object checks found no substitution, byte drift, changed coefficient scope, lost review normalizer, or new unconditional zero-free claim in the reviewed committed material. The previous five review conclusions are therefore bound to the exact mathematical freeze `8b2c6d50ad2d729c681745717c615095bd8f1d9d` and root tree `bca4d3e66472fa7fb4c7f37c56b426359a397cb1`.

The outstanding mathematical tasks remain the unpaid native thin-band or signed off-diagonal estimate, the missing transfers between HLC paths and the native coefficient family, and the unhandled full-path classes. A future change to any reviewed mathematical file requires a new object comparison and an assessment of the change; this acceptance is for the immutable objects above.

