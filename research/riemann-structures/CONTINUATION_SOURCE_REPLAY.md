# Source acquisition for the continuation checkpoint

The programme heads and exact reviewed sources are different identities:
some independently developed packets were cherry-picked. A checkout of
only the programme head can therefore omit an original reviewed commit.
Fetch the durable source refs without merging them:

    git fetch --no-tags origin refs/heads/codex/review-sources-signed-history-wave2 refs/heads/codex/review-sources-universal-euler-wave2 refs/heads/codex/review-sources-xi-laplace-wave2 refs/heads/codex/review-sources-finite-graded-parent-wave2

Their exact targets for this checkpoint are:

| Source ref suffix | Scientific source |
|---|---|
| signed-history-wave2 | e1a10bc821c22cb341424b18ce6838634262af31 |
| universal-euler-wave2 | 330c6f8b85fa1923f2d4914ce3ab1775b0e56c75 |
| xi-laplace-wave2 | 3b6972320899a82c6caa3a98e2ada5ff703a605a |
| finite-graded-parent-wave2 | 7c9e7bde7980c4cfc0b3c3e521fa022319244caa |

The prefix of each suffix is codex/review-sources-. The Xi source also
retains the earlier scout 939a2496; the signed source retains 5dc85cd5;
the universal-Euler source retains 02e53055. The graded ref preserves the
exact scientific identity named in its audit.

Older source lines remain on their existing research branches:

    git fetch --no-tags origin refs/heads/research/gpt56-pro/105210-simple-zero-record-and-descent refs/heads/research/gpt56-pro/102700-half-divisor-defect-factorization refs/heads/research/gpt56-pro/105300-xi-moderate-saddle-residue-spectrum

These retain respectively the PR731 scientific source 81d52e56,
the source extraction state ec6635b4, and the historical kernel state
686e23d9. A full-history ordinary clone also acquires these branches;
shallow or single-branch clones must fetch missing dependencies explicitly.

All replay acceptance remains commit/path/blob/content based. A branch
name is an acquisition aid, not a substitute for the locked identity.
Source checks fail on a missing object or a mismatched blob.

The independently audited original dependency closure covered 19
manifest paths, 119 source-file versions, and 239 literal source edges.
The finite-graded addition contributes a twentieth manifest; its
executable source is already in the generalized programme ancestry.
No missing locked path or blob mismatch was found. No mutable current
README is an authenticated primitive input.

Do not edit old proof files to make a replay pass. In particular the
Architecture A central-source producer authenticates four current
proof notes against frozen PR760 bytes. Front-door summaries may evolve;
the scientific input files and their frozen identities must remain explicit.
