# Source acquisition for the structures continuation checkpoint

The programme checkout and an independently reviewed scientific source
can have different commit identities because packets were cherry-picked.
Fetching only the programme branch can omit the original reviewed commit.
Fetch these source refs without merging them:

    git fetch --no-tags origin refs/heads/codex/review-sources-signed-history-wave2 refs/heads/codex/review-sources-xi-laplace-wave2 refs/heads/codex/review-sources-xi-physical-band-wave2 refs/heads/codex/review-sources-xi-positive-kernel-wave2 refs/heads/codex/review-sources-hardy-inner-width-wave2

Their exact targets for this checkpoint are:

| Source ref suffix | Frozen source target |
|---|---|
| signed-history-wave2 | e1a10bc821c22cb341424b18ce6838634262af31 |
| xi-laplace-wave2 | 3b6972320899a82c6caa3a98e2ada5ff703a605a |
| xi-physical-band-wave2 | 1b5547c3fcd1ba116106953f44a2ee4ceb81b525 |
| xi-positive-kernel-wave2 | e2d145ce1b113c1bb87dd2bc67f717f72be74328 |
| hardy-inner-width-wave2 | ef7bbb8dca978269f24e7ff9d97b6dceeed5b460 |

The common prefix is codex/review-sources-. The signed source retains
5dc85cd5; the actual-kernel source retains 939a2496. The physical-band ref
retains the coarse confluent source 8ef225b8 and finite physical theorem
a07e9c3b as well as the high-derivative theorem at its target. The last two
refs preserve the exact positive-kernel and all-inner/source-duality
scientific commits named by their reviews.

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

- fourteen root manifests and fourteen distinct manifest paths;
- fifteen frozen manifest versions;
- 118 literal source edges;
- 56 unique frozen commit/path file versions;
- nineteen source commits.

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
