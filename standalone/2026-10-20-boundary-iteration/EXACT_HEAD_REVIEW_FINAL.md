# Exact-head review of the second research packet

20 October 2026. This receipt binds **only** commit
`17d7b5b617027cffa4869b47eb898c14eb89e7b9`, based on the first research
commit `9bf9e21f95669abdcaa74e3b2ba54fb93e779503`. It does not bind later
working-tree additions, even if they accompany this receipt in a later
commit. The word "final" in this filename is not an integration decision
or a mathematical certification.

Verdict: no packaging, current-review binding, finite-replay, or claim-scope
defect found within the checks below. The analytic claims remain proposed,
source-dependent research. RH remains unproved, and the numerical
zero-free boundary is unchanged.

## Isolated replay and byte binding

I created a new `git archive` of the exact commit's standalone packet and
extracted it outside the working checkout. The replay used the bundled
Python interpreter with `-I -S -B`. It passed all nine checkers, both
ordinary and optimized, with identical canonical receipts in each pair.
The replay checked all 89 manifest source hashes. Its acceptance checks
remain active under optimization; the replay rejects Python `assert`
nodes in the acceptance checkers.

The frozen hashes are:

| Object | SHA256 |
|---|---|
| MANIFEST.json | `d4d49975b1c69dedd6d8e29ae35baa704530745c238bbb0cbbfa795946847f55` |
| REPLAY_RESULTS.json | `901f72e49967c20dea76a67c08cd44c7997c4876eed3b4d7db59af3870974e5b` |

All 99 archived files were byte-identical to their archived originals
after replay, including the regenerated aggregate and component receipts.
All 97 local Markdown links resolved at the reviewed commit. Of those,
93 resolve inside this packet; the other four point to inherited
repository files and were checked with `git cat-file` at the exact SHA.

Comparison with the separately retained archive of `9bf9e21f` found
all 74 initial files present. Exactly seven changed: README.md,
CLAIMS.md, NEXT_STEPS.md, VALIDATION.md, MANIFEST.json,
REPLAY_RESULTS.json, and replay.py. The remaining **67 initial files
are byte-identical**, including every initial mathematical proof,
component review, scalar certificate, and finite checker. The replay
change is the addition of the positive-cubic checker to the list.

## Current component-review bindings

I checked that the current file hash occurs in each specified review;
these are nine bindings across seven newly reviewed targets:

| Target | Current hash | Reviews |
|---|---|---|
| mixed/JOINT_PAIR_UNEQUAL_CUTOFFS.md | `36277fce41d0c5d425b534b885cd08cd3444a33fbeb49dfa45303f1c13d195c7` | global/REVIEW_JOINT_PAIR.md; type_i/REVIEW_JOINT_PAIR.md |
| mixed/OPPOSITE_CUBIC_JOINT_MEAN.md | `c97a23c55c79a95b6a61080805617a87396285cbd6738b822cd80728efec92aa` | global/REVIEW_OPPOSITE_CUBIC_MEAN.md; type_i/REVIEW_OPPOSITE_CUBIC.md |
| global/SIGNED_MOBIUS_GCD_TAIL.md | `803307e8281f1015b403a8532301db64340e1b4521bb7e2405821c9902efdc84` | mixed/REVIEW_SIGNED_MOBIUS_GCD_TAIL.md |
| global/RECIPROCAL_PROJECTOR_KERNEL.md | `5bc4dafc6165a3bb05e627a288d090e6b4c5ac1af1183d69c1fb238652780564` | mixed/REVIEW_RECIPROCAL_PROJECTOR.md |
| type_i/SIGNED_MOBIUS_COMPLEMENT.md | `acbdcc145517976b4f8cec4d75db1c2fd6a691f3cf7f424bac822a5d3eb9cf61` | global/REVIEW_SIGNED_COMPLEMENT.md |
| type_i/JOINT_ANGULAR_UNIFORMITY.md | `717c00f6f6cf3540d3ef768c800453660eb01de16a906865b29bf44aa8861d03` | mixed/REVIEW_JOINT_ANGULAR_UNIFORMITY.md |
| type_i/CONDITIONAL_ANGULAR_SECTORS.md | `313bb31cf85a967533490ccea53d696d02db968717db194682d61a3ee63945a3` | type_i/REVIEW_CONDITIONAL_ANGULAR_SECTORS.md |

Historical hashes inside reviews are explicitly labeled as earlier
versions. In particular, the current joint-pair review now covers the
added source-overlap comparison and free-column consumers. The initial
exact-head receipts remain correctly restricted to the first commit.

## Claim and source-comparison audit

I read the frozen README, LATER_RESULTS, CLAIMS and VALIDATION together.
They consistently distinguish the following conclusions:

* The pure cubic completed mean and its free-variable bilinear consumer
  are analytic proposals with their theta, large-sieve, closure and
  absorption inputs stated. They are not inserted into a prime-restricted
  inner variable or the quadratic/sextic detector without an additional
  argument.
* The all-unitary assembly expands the proposed covered character family
  at the inherited `B_flat = 0.874886647039964...`. It claims neither a
  smaller numerical boundary nor RH.
* The balanced quadratic/sextic exponent `28/11` is explicitly withdrawn
  as a new best source-recoverable bound. The documentation identifies
  the stronger supplied completed mean that already gives it. The
  alternate proof's smaller dependency set is stated separately.
* The opposite-cubic theorem retains the reviewed range `0 < delta < 2/9`.
  Its natural-count conclusion at `delta=1/6` holds for every conductor
  ratio by the displayed termwise inequalities. Its `N^(8/3+epsilon)`
  consumer has a free smooth inner column, and is not a prime estimate.
  The source comparison is scoped to the checked sources, without a
  claim of exhaustive literature priority.
* The signed common-divisor estimate retains its short-divisor gap. The
  signed complement retains its full-divisor gap. Their respective
  finite-order and full-unitary zero-free premises are kept distinct.
* Conditional smooth sectors are compared to the unconditional result
  present in this reviewed commit. Both retain the exact zero-angular
  term; neither is presented as a prime-counting result.

The new positive-cubic finite-field checker tests the stated local
orientation, finite Fourier identities, natural zeros and a wrong-sign
negative control. Its success is not represented as a proof of the
infinite joint mean. The replay similarly separates the exact closing
scalar algebra from its imported analytic inputs.

## Authorship and limitations

This is an independent packaging and claim-scope audit. I independently
reviewed the other agents' joint-pair, opposite-cubic and signed-complement
arguments, as recorded in their separate hash-bound reviews. I authored
or co-developed the global spherical/guard arguments, quadratic-source
bridge, signed common-divisor estimate and reciprocal-projector note.
Checks of those arguments by me are **coauthor checks**, not independent
mathematical reviews; their independent component reviews are identified
above and in the unchanged initial packet.

This receipt is not a new proof of the analytic imports, a formal
verification of infinite quantifiers, or an integration approval.
