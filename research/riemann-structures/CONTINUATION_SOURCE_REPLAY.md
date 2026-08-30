# Source acquisition for the structures continuation checkpoint

The programme checkout and an independently reviewed scientific source
can have different commit identities because packets were cherry-picked.
Fetching only the programme branch can omit the original reviewed commit.
Fetch these source refs without merging them:

    git fetch --no-tags origin refs/heads/codex/review-sources-signed-history-wave2 refs/heads/codex/review-sources-xi-laplace-wave2 refs/heads/codex/review-sources-xi-physical-band-wave2 refs/heads/codex/review-sources-xi-positive-kernel-wave2 refs/heads/codex/review-sources-hardy-inner-width-wave2 refs/heads/codex/review-sources-canonical-boolean-diagonal-wave2 refs/heads/codex/review-sources-xi-companion-count-wave2 refs/heads/codex/review-sources-hardy-cofinal-capture-wave2 refs/heads/codex/review-sources-native-boolean-diagnostic-wave2

Their exact targets for this checkpoint are:

| Source ref suffix | Frozen source target |
|---|---|
| signed-history-wave2 | e1a10bc821c22cb341424b18ce6838634262af31 |
| xi-laplace-wave2 | 3b6972320899a82c6caa3a98e2ada5ff703a605a |
| xi-physical-band-wave2 | 1b5547c3fcd1ba116106953f44a2ee4ceb81b525 |
| xi-positive-kernel-wave2 | e2d145ce1b113c1bb87dd2bc67f717f72be74328 |
| hardy-inner-width-wave2 | ef7bbb8dca978269f24e7ff9d97b6dceeed5b460 |
| canonical-boolean-diagonal-wave2 | 7ccd5a044e91b32a0aa66bcf30dcf39d99f96217 |
| xi-companion-count-wave2 | 76454e3db0ccce8f500297ea27668d6088b5091a |
| hardy-cofinal-capture-wave2 | 90e8dff3d184cbfe59974969ca89615856c33c51 |
| native-boolean-diagnostic-wave2 | 2e1293a03486fb74580eef0ddd7ed0caf9ab7808 |

The common prefix is codex/review-sources-. The signed source retains
5dc85cd5; the actual-kernel source retains 939a2496. The physical-band ref
retains the coarse confluent source 8ef225b8 and finite physical theorem
a07e9c3b as well as the high-derivative theorem at its target. The remaining
refs preserve the exact positive-kernel, all-inner/source-duality,
canonical-diagonal and actual companion-count scientific states named by
their reviews. The canonical-diagonal state includes its separate final
manifest-whitespace/hash repair; the unrepaired fixture is not accepted.
The cofinal ref preserves the pure finite-height theorem. The final ref
preserves the one-file exploratory native-decoder diagnostic, which is
not counted as an additional theorem packet.

## Older source branches still required

The following existing research branches retain additional frozen inputs:

    git fetch --no-tags origin refs/heads/research/gpt56-pro/105210-simple-zero-record-and-descent refs/heads/research/gpt56-pro/102700-half-divisor-defect-factorization refs/heads/research/gpt56-pro/105300-xi-moderate-saddle-residue-spectrum refs/heads/research/gpt56-pro/106000-cvxd-lfamily-hybrid-moments refs/heads/codex/beta-bandpass-wavelet refs/heads/research/gpt56-pro/107100-xi-reverse-rolle-execution refs/heads/research/gpt56-pro/pr757-dual-architecture-closure

| Existing branch | Required frozen identity |
|---|---|
| research/gpt56-pro/105210-simple-zero-record-and-descent | 81d52e569cc8bb566e54043fd692fd6157406aab |
| research/gpt56-pro/102700-half-divisor-defect-factorization | ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc |
| research/gpt56-pro/105300-xi-moderate-saddle-residue-spectrum | 686e23d9e5b1005aae83e3362ac1ed53a28a0352 |
| research/gpt56-pro/106000-cvxd-lfamily-hybrid-moments | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b |
| codex/beta-bandpass-wavelet | d79692ece0b7604ad309c459f565b24e9926f5c5 |
| research/gpt56-pro/107100-xi-reverse-rolle-execution | cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57 |
| research/gpt56-pro/pr757-dual-architecture-closure | 3a595dda92ef827a41e50d2395309692a93748ad |

These are required source identities, not promises that the mutable branch
tips always equal them. At the audit, the first three were retained by
tips 6d440eb6c82d989c046e87e13f9bdabf087f920f,
59654c02d13545d6c8c0972315db2628e9efa1f6 and
14f3ef3cb40854fb559deb2528932e5113f72038 respectively. PR760's tip
e3747c946379735d27658c010976cfff051843e9 retained 3a595dda.
The other listed source tips matched their displayed required identities.

Some older objects are also ancestors of the newer source refs. Explicit
fetches avoid relying on incidental local object availability or a
single-branch clone's configuration. A full-history ordinary clone usually
acquires these existing branches; a shallow/single-branch clone may need
the explicit fetches and adequate history.

## Exact closure check

The recursive structures-only source audit passed for:

- seventeen root manifests and seventeen distinct manifest paths;
- eighteen frozen manifest versions;
- 149 literal source edges;
- 71 unique frozen commit/path file versions;
- twenty-three source commits.

The exploratory decoder memo has no separate sources manifest. Its ten
literal commit/path/blob/LF-SHA table entries were independently checked,
and their three source commits are covered by the listed refs. These ten
table entries are not included in the recursive manifest totals above.

Every required source commit is reachable from the programme or from the
listed source/older branch tips. The earlier PR760 identity is necessary:
omitting its branch leaves a real acquisition hole even when a shared
local object database happens to make tests pass.

The generalized-L programme has a separate source closure and acquisition
list in its CONTINUATION_RESULTS.md. Its source refs are not implicitly
substituted for those required by this branch.

Acceptance remains commit/path/blob/content based. Branch names are
acquisition aids, not substitutes for locked identities. Missing objects
and mismatched hashes must fail replay. No mutable README is treated as
an authenticated primitive mathematical input.

## Preserve the scientific boundary

Do not edit old proof files to make a replay pass. In particular the
Architecture A source authenticates four current proof notes against
frozen PR760 bytes. Front-door summaries and separate audit files may
evolve; primitive files retain their explicit scientific identities.

The source-duality correction is a separate new packet. The historical
raw-value formula remains visible, and its convention mismatch with the
explicit column Fourier Gram is stated in the continuation map and audit.
A successful byte check is not a mathematical approval of every historical
claim or downstream consumer.
