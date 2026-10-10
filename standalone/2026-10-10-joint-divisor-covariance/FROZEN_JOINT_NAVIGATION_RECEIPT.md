# Frozen-source receipt: joint divisor proof and navigation scope

**Reviewer:** signed_conductor_attack.

**Date:** 2026-10-10.

**Result:** PASS. The exact Git objects identified below are identical
to the contents approved in my joint-divisor and navigation reviews.
Those scoped approvals therefore bind to the stated source commit.
This receipt adds an exact-commit identity check; it does not enlarge
either review's mathematical scope.

## 1. Exact source commit

- Source commit: 5ad900ff27d34f1a8f94d28e19c47a3b37de6e39.
- Tree: 2a6e93c5cef50ecba6f5e4b4c490f8353906e3c0.
- Sole parent: f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32.
- Source: [frozen GitHub commit](https://github.com/GettysburgResearch/riemann/commit/5ad900ff27d34f1a8f94d28e19c47a3b37de6e39).

I read the fetched commit object and checked its tree and complete parent
list. I then read each file below from the exact Git object using
git show with this commit and the full repository path. SHA256 values
and byte counts were computed from those returned bytes, not inferred
from branch names, a review label, or a working-tree manifest.

Unless marked “root,” every filename in the tables is under
standalone/2026-10-10-joint-divisor-covariance/.

## 2. Joint proof and its independent review

| File | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| JOINT_DIVISOR_MEAN.md | c985bf32eb270ed684722e410c5551e25d942b9c | 22,983 | 7b42abe2c3c62acfd934b663405821748eac54bb440f1d1071671961a9e97035 |
| JOINT_DIVISOR_INDEPENDENT_REVIEW.md | 914b15b3c7c366a289c471738d9dc5566ac7b789 | 14,509 | 6c282fd3e3b847885dd0035ad967e2244496f53ebfafdb56bc3a7122d9515684 |

Both hashes match the previously approved identities exactly.
The committed review names the committed proof's same final hash,
including the completed citation-only repair.

**Mathematical scope carried forward:** Sections 1–6 of the proof are
approved as deductions conditional on the exact imported theta mean
and squarefree sextic large sieve. This includes the literal cube
reciprocal, absolutely summable quadratic-row expansion, joint
polynomial recombination with every moving mask, completed block
estimate, dyadic reconstruction and large-divisor tail.

The tail conclusion remains

$$
\|\operatorname{tail}_{Nd\ge R}\|_2
\ll Q^{1-a+\epsilon}R^{-\eta+\epsilon}
(2+|\Im u|)^M,
$$

for $1/2<a<5/6$, $b=(3-a)/2+\eta$, $\eta>0$,
and $R\ge Q^{2/3}$. The $Q^{1/4}$ norm saving at
$a=3/4$ applies to that specified tail. The full-series
condition $2b+a>3$ is unchanged.

Section 7 is approved only at finite A2 coefficient-algebra scope.
The approval excludes a global A2 adapter, a new second functional
equation for the actual moving angular family, replay of the imported
analytic foundations, an improved full moment, and RH.

## 3. Navigation files and their independent review

| File | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Packet README.md | 81ac46aaabd379631cdfa53daf2e12d7b2c26d10 | 13,910 | 011d918be3ddc0bfb290381ac3e2608a9c8f07e8404544fc968cdf66976818dc |
| Root README.md | 9e5a73bfb5eb499629c07409dbb5371940b4a753 | 12,072 | c6417e230a3e7f14d8e3ca711235a001c3bd8b0f0d2168b2e0d86e97c3ea158e |
| NAVIGATION_SCOPE_REVIEW.md | e3e5b268a48064d0628b8cf20b0bbaf06625608a | 10,931 | 02a82eccc8f7c0d508e6d25782d596ff8b7952ecc7f091dd283ae09bfeeebd4b |

All three hashes match the reviewed identities. The overview contains
the three previously requested scope repairs: the fixed-test and
all-scale moment quantifiers, the nonprincipal conductor and radial
majorant hypotheses, and the nonnegative loss parameter with the
specified universal Mellin-factor test.

**Root README scope is restricted to its new section.** The approved
excerpt starts with the heading “Further research: joint divisors and
additional moment sectors” and ends immediately before the next
License heading, including the two preceding newlines. Its identity is:

- Bytes: 856.
- SHA256: 54df4d1ca6fee8120e1e1a7e331720c8e216209ea398cc8f8ff1ccc90b3bc6c8.

This is an excerpt of the full root blob, not a separately tracked
Git file. I extracted it from the frozen source bytes and recomputed
its hash. Deleting precisely that excerpt gives bytes exactly equal
to the root README read from the sole parent commit. Consequently
the whole-file hash above identifies the containing file but does
not extend approval to inherited root prose.

**Navigation scope carried forward:** the packet overview faithfully
summarizes the four proof notes and preserves their hypotheses,
conditional status and unresolved signed remainder. The moment
implication is checked against PR #913 at
6498d6cc2eded03159c7332b25fd224ad07f89c1, as recorded
in the navigation review. The boundary $1/2+5/(12k)$ and
the value $17/24$ at $k=2$ remain conditional implications
from unproved full moments with the required tests and scales.
They are not new zero-free results of this packet.

The four-note comparison does not replace the notes' separate
detailed reviews. The navigation review does not certify
the inherited root README, upstream theorem proofs, a global
A2 analytic composition, checker implementation integrity, or
the full moment hierarchy.

## 4. Identity of the other proof notes used in navigation

These additional frozen objects match the content identities used
for the navigation comparison:

| File | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| MOVING_AUXILIARY_ADAPTER.md | 8044ad07468dba818afcffebf54636f7f734c0b4 | 30,631 | e91e0f7b3c3d885587fc9197539beaf1caa8e0c80ed9c8bba5c15340090b5eda |
| OPTIMIZED_A2_TRANSFER.md | 329095c682a29bcb40d953fda4d8d28e290d5667 | 14,739 | d5a87c27959b64e62df7dd3aa2fdd33cc8b42af6e5a64e9bfb20d6b74af0277a |
| SIGNED_CONDUCTOR_PROGRESS.md | c904ac06527a3c47bfc31b808b2a058030b0b2ea | 22,968 | d973468a0e0a893f43327e6f3a4ac706076952ec44a2a3114423ea515bdc4e4a |

This table is an identity confirmation for the navigation dependencies.
It does not claim a new independent proof review of these three files
by this receipt's author. In particular I authored the signed-conductor
note; its independent mathematical review is a different agent's
record.

## 5. What was independently performed

I independently performed the following read-only checks against
the fetched Git objects:

1. Parsed the source commit and checked its exact tree and sole parent.
2. Read all eight listed files through git show at the source commit.
3. Resolved each exact Git blob and computed its SHA256 and byte count.
4. Compared every digest with the identity established during review.
5. Re-extracted the restricted root section, checked its own digest,
   and checked exact equality with the parent's root README after
   deleting that section.

All checks passed. The fetched bytes also match the corresponding
working-tree files, but that agreement is supplementary; the source
binding rests on the direct Git-object reads.

No mathematical proof was altered, no old review was edited, and no
commit was made in preparing this receipt. No infinite theorem or
upstream analytic premise was tested by these finite identity checks.
The receipt binds scoped AI-agent reviews to the stated mathematical
source commit; it is not integrated acceptance, external human peer
review, or Lean verification.
