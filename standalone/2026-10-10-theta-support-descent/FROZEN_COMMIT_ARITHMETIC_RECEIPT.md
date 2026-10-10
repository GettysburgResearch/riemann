# Frozen-commit arithmetic review receipt

Date: 10 October 2026.

Reviewer: moment_arithmetic.

**Frozen mathematical source commit:**
1fc00c42c5c897291f4f941c4071da1d18649cfb.

**Verified parent commit, PR #915 baseline:**
9959364671f89b86f3992ec5ed5e19f804eb607b.

**Result: PASS for committed-byte identity and confirmation of the
review scopes stated below.** The two proof files independently
reviewed by this reviewer have exactly the bytes previously reviewed.
This receipt was written after the source freeze; it records that
source commit and does not assign its own later metadata to that
commit.

## 1. Committed objects actually hashed

Every path below is relative to
standalone/2026-10-10-theta-support-descent/ in the frozen commit.
The SHA256 values were computed from raw Git blob contents obtained
with git cat-file, independently of the working-tree files.

| File | Actual Git blob ID | SHA256 of committed contents |
| --- | --- | --- |
| HIGHER_ANGULAR_SECOND_MOMENT.md | 956445e9baa91356a352cc089852dbf34f90dbef | 82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959 |
| POST_REFLECTION_EULER_CONTINUATION.md | 3a28bbd99315ea0b4e469c7e9cef5456f49c6a1a | 7ddcaf96aba2f109fb5696880ed9098e435712e2075613e72474b76fc00a3072 |
| POST_REFLECTION_INDEPENDENT_REVIEW.md | fcdfa88a8dec5ed3477080e7985d7b70be120199 | 4fd13a92b58e283f2f12d9117d24f489859e92d17c79d0e6371132bf12b78f8a |
| OPPOSITE_DERIVATIVE_REFLECTION.md | 2966032ea89396ec2e0a423b1b23841645a1fb47 | 9532f14dc452edf9a50e7ec905e0629c54d510fd9937c5d8c19bcf7dfb4e9ccb |
| INDEPENDENT_THETA_REVIEW.md | 6c65ab39791dd86e14a436b1305bd0444c59d629 | 8bcc06f680a66d188d7999179a3e24a0f8ab6c3fe774e61c556d3ffd94202854 |
| DEFORMED_GAUSS_CONTINUATION.md | d91fe4491b9f192a60733e69e921554e5b4389a7 | b01b17194884b3e2331d9f668ee71abb33a5e2f1e047d16cb2e906a1c5b32c81 |

The committed HIGHER_ANGULAR_SECOND_MOMENT and
POST_REFLECTION_EULER_CONTINUATION hashes match this reviewer's
previously recorded final reviewed hashes. The committed
POST_REFLECTION_INDEPENDENT_REVIEW also matches its previously
recorded final hash and names the same post-reflection proof hash.

## 2. This reviewer's independent mathematical scope

The reviewer did not author HIGHER_ANGULAR_SECOND_MOMENT.md.
Its previously completed independent review is confirmed for the
committed object above: **PASS at the stated source-conditional
scope.** The checks covered the pure higher derivative and Mellin
normalization, the completed norm estimate with repeated rows,
the arbitrary-residual transfer specialized to a fixed angular
character, finite smooth seminorms, the exact initial parameter -r,
the excluded inverse full-row type r=-1, the fixed-row extraction,
and the conductor-uniform lattice/logarithm reciprocal argument.
The imported arithmetic, theta automorphy, sieve, transfer and
finite induction remain explicit inputs.

The reviewer did not author POST_REFLECTION_EULER_CONTINUATION.md.
The independent review archived in
[POST_REFLECTION_INDEPENDENT_REVIEW.md](POST_REFLECTION_INDEPENDENT_REVIEW.md)
is confirmed for the committed object above: **PASS at its stated
source-conditional scope.** Its checks cover the exponent-3 and
exponent-4 Gauss/CRT scalar, the plus-derivative Mellin normalization,
finite ray decomposition, signed divisor Euler product, normal
convergence, moving zero masks, possible polar divisors,
polynomial vertical growth, and the possible-residue formula.

The final precision sentence after that proof's equation (2.4)
was checked: chi_p(-1) squared equals one removes exponent -2,
while the other exponents 21 and 8 reduce modulo six to 3 and 2.
The committed proof includes that sentence and the unchanged
formulas reviewed with it.

The reviewer authored DEFORMED_GAUSS_CONTINUATION.md, an earlier
dependency of the post-reflection theorem. Its hash is included
above for disclosure and source binding. Independent review of
that earlier theorem belongs to joint_series_review and the
separate review record; this receipt does not count its author
as its independent reviewer.

None of these confirmations establishes the full generalized
moment, a new zeta zero-free exponent, nonvanishing of the possible
residue, or equality of that residue with an initial Poisson
diagonal. The conductor and contour limitations in the reviewed
proofs remain part of their scope.

## 3. Identity-only binding of theta_review's archived report

The committed INDEPENDENT_THETA_REVIEW.md attributes its work to
theta_review. Its recorded target hashes were compared with the
actual committed blobs:

- Its opposite-derivative target hash is
  9532f14dc452edf9a50e7ec905e0629c54d510fd9937c5d8c19bcf7dfb4e9ccb,
  exactly the committed OPPOSITE_DERIVATIVE_REFLECTION.md hash.
- Its fixed-angular target hash is
  82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959,
  exactly the committed HIGHER_ANGULAR_SECOND_MOMENT.md hash.

This section confirms the identity of the archived report and its
targets. Authorship and review credit for that report remain with
theta_review. The opposite-derivative assessment here is an
identity binding of their archived review; it is not an additional
mathematical review performed by moment_arithmetic. The separate
independent fixed-angular review performed by moment_arithmetic
is described in Section 2.

## 4. Replay and acceptance rule

The verification read the parent with git rev-parse, resolved each
commit:path to its actual blob ID, read the raw contents with
git cat-file blob, and computed hashlib.sha256 on those bytes.
It also read the committed archived review and checked that its
two stated target hashes equal the corresponding computed hashes.

The essential replay operation for each file is:

    git rev-parse 1fc00c42c5c897291f4f941c4071da1d18649cfb:path
    git cat-file blob <returned-blob-id>

The second command's raw output, without text decoding or newline
normalization, is the input to SHA256. The comparison script used
explicit exceptions on a parent mismatch, any mismatch with a
previously reviewed hash, or a missing target hash in the archived
report. All checks succeeded.

This verifies exact committed identities and binds the completed
reviews to them. It does not replay the imported theta automorphy,
the analytic proofs by computation, or any global zero census.
No mathematical source file was changed during this receipt task.

## 5. Published-source identity confirmation

Publication verification date: 10 October 2026.

**Published mathematical source commit:**
6aceafc1729ca0962eb12519b407b69c3b5a4d5f.

The reviewer independently compared this fetched published commit
with the local frozen source commit
1fc00c42c5c897291f4f941c4071da1d18649cfb. Both have exactly:

- Complete Git tree: ab9ea56041c100620cd825f9d98b17734ec27d49.
- Parent: 9959364671f89b86f3992ec5ed5e19f804eb607b.

Every file in the committed-object table in Section 1 was then
resolved independently at the published SHA. Its actual blob ID,
raw contents, and recomputed SHA256 matched the corresponding
local-source object exactly. In particular:

- Published HIGHER_ANGULAR_SECOND_MOMENT.md is blob
  956445e9baa91356a352cc089852dbf34f90dbef, with SHA256
  82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959.
- Published POST_REFLECTION_EULER_CONTINUATION.md is blob
  3a28bbd99315ea0b4e469c7e9cef5456f49c6a1a, with SHA256
  7ddcaf96aba2f109fb5696880ed9098e435712e2075613e72474b76fc00a3072.

The committed post-reflection review, archived theta_review report,
its opposite-derivative target, and the earlier divisor-conditioning
dependency also have exactly the blob IDs and SHA256 values in
Section 1. The full-tree comparison additionally binds all remaining
source-tree contents.

**Result: PASS.** This reviewer's same source-conditional mathematical
verdicts in Section 2 apply to published source commit
6aceafc1729ca0962eb12519b407b69c3b5a4d5f by exact committed-content
identity. The authorship disclosure for the earlier
divisor-conditioning dependency is unchanged. The binding of
theta_review's archived opposite-derivative assessment remains
identity-only, with the scope and credit specified in Section 3.

The publication comparison used git rev-parse for both commit trees,
parents, and each commit:path, followed by git cat-file blob and
SHA256 of its raw bytes. Explicit exceptions would have rejected any
tree, parent, blob-ID, or raw-content mismatch. All comparisons
succeeded. This confirmation appends publication provenance; it
changes no proof, reviewed claim, or mathematical scope.
