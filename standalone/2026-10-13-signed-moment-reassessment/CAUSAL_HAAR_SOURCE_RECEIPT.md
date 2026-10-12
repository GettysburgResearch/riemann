# Exact-commit receipt: causal classification and Haar moments

**Reviewer:** `determinant_independent_review`, the independent reviewer
identified in [CAUSAL_HAAR_INDEPENDENT_REVIEW.md](CAUSAL_HAAR_INDEPENDENT_REVIEW.md).

**Receipt time:** October 12, 2026, 23:55:37 UTC.

**Verdict:** PASS. The actual committed blobs below are byte-for-byte
identical to the sources and report from my completed reconstruction.
The prior review's verdict, scope, corrections, and omissions therefore
apply to this exact source commit.

## Frozen source identity

| Object | Exact identifier |
|---|---|
| Source commit | `3968d1b7135900e6130412f58a39bc67e73d4ecb` |
| Tree | `1e71c308a95c616069c29fd20d87907cc5795e1a` |
| Parent | `97bf40329489992e9384c34d7595af6d01a40774` |
| Local branch observed at that commit | `research/signed-moment-reassessment-20261013` |

All four paths below are under
`standalone/2026-10-13-signed-moment-reassessment/` in that commit.

| File | Bytes | SHA-256 of committed content |
|---|---:|---|
| `CAUSAL_ORBITS_AND_DENSE_LIFTS.md` | 44,355 | `dc8f645731302f2e2059cd115cc70564409af98c08c48a3f30f7d081c917a817` |
| `COMPACT_TEST_HAAR_MOMENTS.md` | 7,939 | `49f623d831ae196aab9d1d7e7edd44419999c6995115faa983406da7c3099b23` |
| `README.md` | 15,908 | `a1fdc9f5a7475785a13bda2543006433fec2fcf50737aad12f4d58fd9c930328` |
| `CAUSAL_HAAR_INDEPENDENT_REVIEW.md` | 22,162 | `b63e14ed5235f330835655336728ca9d8a58ac22af224c9150ca1e814d264e71` |

Their Git blob identifiers, in the same order, are:

```text
8e81b2b788bbbf87d21893088705f3cfca744d85
e025b01c2eae6c09ebc9c6181cd9bca77ff6fc2a
dd0819cfa75c6aee6fa5f21cf07902ce945e3588
935e052b6230c4355bd42482dfee2c06dd31d6bc
```

## Authentication performed

I inspected the commit object using `git show -s`, checked its exact
commit, tree, and parent identifiers, and resolved each `commit:path`
with `git rev-parse`. I read each actual committed blob using
`git cat-file blob`, independently recomputed its byte count and SHA-256
with Python, and compared the content directly with the reviewed
working-tree file. Every check passed. This authenticates the committed
content; it is not a fresh reconstruction of unchanged mathematics or a
separate remote-host availability check.

## Scope carried forward

The reconstruction covers the complete causal/Gaussian note and complete
compact-test supplement. The README review remains restricted to
Sections 4 and 5 and the final compact-test discrepancy comparison in
Section 6. It does not approve the README's other research claims.

The approved statements retain the weighted-total-variation restriction
on causal operators, norm grouping and field conjugation, and the
independent Haar probability measure. The normalized product converges
in every fixed even moment above one half. When an invariant constituent
is present, Gaussian moment bounds remain equivalent to target zero
exclusion; no raw Euler-product convergence below one is assumed.
The compact-test converse concerns the entire test class, not one
arbitrary compact test. The physical-discrepancy equivalence is an exact
reformulation of an open bound, not a proof of that bound.

The full report's independence disclosure and omissions remain in force.
This receipt proves no physical-row moment, zero-free boundary, or RH
statement, and does not declare integration or formal certification.
I created only this new receipt; I did not edit either frozen proof,
the frozen content review, or the synopsis, and made no commit or push.
