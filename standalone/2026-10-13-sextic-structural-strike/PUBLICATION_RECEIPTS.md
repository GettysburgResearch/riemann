# Publication receipts and immutable content binding

**Status:** proposed standalone research. These records bind the reviewed
files to their actual GitHub contents. They are not external expert
certification, formal verification, integrated acceptance, or a proof of
the native moment hierarchy or RH.

## Frozen content

| Object | Immutable identity |
|---|---|
| Repository | GettysburgResearch/riemann |
| Content commit | [988f4571bf9ffec65cd73ccb092301550c054ae0](https://github.com/GettysburgResearch/riemann/commit/988f4571bf9ffec65cd73ccb092301550c054ae0) |
| Root tree | 593dfbf7d305c28e4faa439bef1d64513aedd034 |
| Sole parent | f9939c957f5aac6b2099b591e4988991700a152b |
| Parent tree | e1ad0b4069c4a62d283d41874921762d1d05beba |
| Packet subtree | ddb89add00daf8e1cf05c8d3f7f8a46bc28b0692 |
| Manifest Git blob | 87a50860c891147b84110536917abc158d1f0562 |
| Manifest SHA256 | 1dede6bc1b60de11b86ccc2abe03cea1560644e2b9ddfabfed9ee27bb2b3f1a8 |
| Research branch | research/sextic-structural-strike-20261013 |
| Draft PR base | research/sextic-signed-reunion-20261010 |

All reads recorded here occurred on 2026-10-13 UTC. The content commit
contains 50 packet files, of which the manifest inventories 49, plus the
four-line top-level README addition. The final top-level README explicitly
qualifies the order, field, local character type and fixed background.

This receipt file is added in a subsequent direct child commit. That
commit is restricted to adding this file; the reviewed mathematics,
sources, diagnostics, review reports and manifest remain unchanged.
The manifest deliberately excludes itself and this receipt file, so
there is no circular self-hash. The containing Git commit authenticates
the receipt file itself.

## Root verification

The root compared the staged content tree with the GitHub-created tree
and obtained exact equality. A subsequent independent GitHub GET of the
actual content commit confirmed its tree and sole parent, and a branch
GET confirmed that the new research branch pointed to that commit.

The root then fetched all seven complete mathematical files, the packet
README, the manifest and the top-level README at the immutable content
commit. Every full UTF-8 content string and returned Git blob identifier
matched its frozen local counterpart. The mathematical SHA256 values
are recorded in [VALIDATION.md](VALIDATION.md), and the complete file
inventory is in [MANIFEST.json](MANIFEST.json).

The extraction lane additionally reconstructed all 13 relevant Git tree
objects, read every actual packet file through base64 transport, checked
all 49 manifest bindings, compared the exact parent/current tree scope,
and freshly authenticated all eleven copied sources at their original
immutable commit/path pairs. Its full receipt below records the checks
and their limits.

The three finite diagnostics were replayed by the root in ordinary Python
and with optimization enabled. All six executions reproduced their
recorded reports byte-for-byte. The final packet integrity run passed
after inclusion of the metadata review: 49 inventoried files, eleven
source transports, seven mathematical files and three identical report
pairs. The extraction lane separately ran the ordinary verifier on a
directory reconstructed from the actual remote bytes.

The final metadata/verifier audit is
[reviews/metadata_integrity.md](reviews/metadata_integrity.md). The
substantive mathematical reconstructions and disclosed authorship
overlap are mapped in [VALIDATION.md](VALIDATION.md).

The root also reconstructed the raw local commit object from the remote
metadata and required its Git object ID to equal the published commit
before advancing the local branch. No mathematical change was introduced
by local synchronization.

Exact source and review bytes were preserved, including terminal blank
lines and the literal context spaces in historical unified diffs.
A standard whitespace scan consequently reports those archival details;
the authored-content scan, excluding historical diff contexts and
allowing terminal blank lines, found no additional whitespace issue.
No normalization was applied to a hash-frozen reviewed source.

At the final base/main read-back before the receipt addition, the base
branch still pointed to f9939c957f5aac6b2099b591e4988991700a152b and main
to f99d9e3908dde4865377c75d9ca051c1f545bf4f. The publication changes only
this research branch.

## Original reviewer receipts

The following three records are reproduced in full. Text between each
BEGIN/END ORIGINAL RECEIPT marker is the exact UTF-8 source receipt,
including its final newline. The SHA256 values authenticate those
embedded source bytes; each author's scope and overlap disclosures
remain intact.

| Lane | Original bytes | Original SHA256 |
|---|---:|---|
| Extraction | 12042 | da5989d2b3a6878a1be6ad8ff31ed21297ccb17b6a83ed023f2b3e51968636e0 |
| Native | 11682 | d3a30f370fc34e91bc496e6352b00244ffbdb4b66e4bba7071d3e298fe83a051 |
| Bilinear | 11721 | 97079c1acd98add46fc67b047f46496429607da44090b9ae65ca8e73923502f8 |

<!-- BEGIN ORIGINAL RECEIPT: extraction -->
# Extraction-lane receipt for the frozen remote content

Reviewer: `/root/extraction_radical_attack`.

**Verdict: PASS for exact remote content identity and the previously
recorded scoped mathematical reconstructions.** I performed the
read-back through read-only GitHub requests on 2026-10-13 UTC. No
repository file, branch, commit, pull request or review was changed by
this reviewer.

This is a same-team review receipt. It is not an external expert
endorsement, a formal proof certificate, or a proof of the full native
moment hierarchy or RH.

## 1. Immutable publication object

Repository: `GettysburgResearch/riemann`.

- Content commit: [`988f4571bf9ffec65cd73ccb092301550c054ae0`](https://github.com/GettysburgResearch/riemann/commit/988f4571bf9ffec65cd73ccb092301550c054ae0).
- Root tree: `593dfbf7d305c28e4faa439bef1d64513aedd034`.
- Sole parent: `f9939c957f5aac6b2099b591e4988991700a152b`.
- Parent tree: `e1ad0b4069c4a62d283d41874921762d1d05beba`.
- New packet subtree: `ddb89add00daf8e1cf05c8d3f7f8a46bc28b0692`.
- Branch observed pointing to that exact commit:
  `refs/heads/research/sextic-structural-strike-20261013`.

I fetched the GitHub commit and ref objects directly. The commit has
the root tree and sole parent displayed above. I separately fetched
the parent commit and checked its tree. The branch identity is an
observation at the time of this receipt; the immutable content commit
is the object to which this review remains bound if the branch later
advances.

I fetched complete, nontruncated root and standalone trees for both
the content commit and its parent, and a complete recursive tree for
the new packet. I reconstructed their Git tree hashes from the exact
names, modes and child object IDs: four nonrecursive tree objects and
all nine trees comprising the packet subtree, including its root.
Every reconstructed object ID agrees with GitHub's response.

## 2. Exact change scope

The remote comparison reports one commit ahead of the parent, zero
behind, and exactly 51 changed paths:

- 50 newly added files under
  `standalone/2026-10-13-sextic-structural-strike/`;
- one modification to the repository's top-level `README.md`, consisting
  of four added lines and no deletions.

The root tree has the same path set as its parent's root tree. Only
the README blob and standalone tree differ. Every previously existing
standalone subtree retains its previous object ID; the new packet is
the sole added standalone subtree. Thus the receipt does not rely
only on a potentially abbreviated file-diff listing to establish
change scope.

The final top-level README has 12,638 bytes, Git blob
`ae2a627261fbff1b9fd57d972cca0952d990840e`, and SHA256
`a0cd7fadf0f9d3df1ef021f401138333abae7cc9471f62759b2bd7c807bc7a9b`.
I read its complete addition against the parent. The addition retains
the necessary qualifications: order `n>=3`, a fixed field containing
the relevant roots of unity, the specified conjugate sextic local
type, fixed background, a feasible native sector, and the full fourth
moment, hierarchy and RH still open. It does not claim a universal
sextic conductor mean or an integrated acceptance decision.

## 3. Manifest and complete remote byte read-back

The published manifest is:

| Property | Value |
|---|---|
| Path | `standalone/2026-10-13-sextic-structural-strike/MANIFEST.json` |
| Bytes | 11569 |
| Git blob | `87a50860c891147b84110536917abc158d1f0562` |
| SHA256 | `1dede6bc1b60de11b86ccc2abe03cea1560644e2b9ddfabfed9ee27bb2b3f1a8` |
| Inventoried files | 49 |

I fetched the actual contents of all 50 packet files at the immutable
content commit, using base64 transport so that exact bytes and final
newlines could be reconstructed without rendered-text normalization.
There are 47 distinct blob objects because three ordinary/optimized
report pairs have identical contents.

For every path, I decoded the returned bytes, recomputed byte length,
SHA256 and Git blob identity, checked the remote tree entry, and
compared the bytes directly with the reviewed local file. All 50
comparisons passed. The 49 manifest entries cover exactly the 50
published packet files minus the manifest itself. Every manifest
identity agrees with the actual remote bytes, including the copied
metadata review added after the provisional 48-file inventory audit.

`PUBLICATION_RECEIPTS.md` does not yet occur in this frozen content
tree. Its intended later addition and the manifest's exclusion of it
avoid circular receipt hashing; no future receipt commit is certified
by this observation.

## 4. Published mathematical source identities

The following identities were recomputed from the remote contents.
All paths in this table are relative to the new packet.

| File | Bytes | Git blob | SHA256 |
|---|---:|---|---|
| `EULER_TRACE_RESONANCE.md` | 10757 | `d4be020948057b86e90a37df1242ff0a05a32038` | `c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10` |
| `RESONANT_SHORT_TRACE.md` | 14564 | `d49c771aaf48a1e244905928307c9bef2fed1b8f` | `1c043c4650e72d9c78daef4111a3a2485c6f5d285a1ca2afee62283c9286a70f` |
| `SHORT_FACTOR_NONSMALLNESS.md` | 13252 | `30cddb1c877aaeb8eaa97d2e5f9dc80525b1c855` | `0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935` |
| `HORIZON_NECKLACE_FACTORIZATION.md` | 20252 | `1582d4c23d48edf386f9cb08f10ab5b268f07378` | `a6aa7ab8925eac3f1f514b6e4138baa87735e3902fa3c5a78679480c7cf925ab` |
| `CONJUGATE_PAIR_CONDUCTOR_SIEVE.md` | 22931 | `395791010f9bdba0395915c7c7150596bea3ae19` | `220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2` |
| `CONDUCTOR_COROLLARIES.md` | 8872 | `35dbcad0dc80b6980f7a2262758f01a52ca456f3` | `49d471154fbfb2b8589742a70343f9abfa8e407172648b73f33a14d5f3e3031d` |
| `PRIME_DEGREE_COHERENCE.md` | 22934 | `e51dc82a0146e667e3f7c894c3bf4bcb7e9e8c19` | `2290ce3d8d24f832259b3d701607beb125ceb5111f86b39d82be200eea1c27fb` |

### Independent reconstructions retained by this reviewer

My conductor review and its final update remain applicable to the
published pair-sieve bytes. The review reconstructed the squarefree
conjugate-pair Poisson reduction at every fixed order `n>=3`, the exact
primitive residual conductor, the split root number with no surviving
mixed factor in that case, and the retention of nonunit/common-divisor
masks before using positive norms. It also checked the two coefficient
vectors created by Mellin separation, the moving-background approximate
functional equation with its primitive associate and zero extensions,
and the native unit projection and conductor accounting. The named
de Faveri inputs were read in the primary source; this review does
not re-certify the full external large-sieve proof.

My corollary review remains applicable to its published final bytes.
The conductor-sized mean is for the stated conjugate sextic local
type with fixed background. The finite `+/-1` local-exponent coverage
uses the special orders three, four and six. The `11/8` limitation is
the exact optimum of the stated five-label positive bound envelope;
it is not an arithmetic lower bound for the family. The native sector
improvement remains a scoped sufficient estimate, not a proof of the
full fourth moment.

My necklace review remains applicable to its published final bytes.
It reconstructed the primitive-necklace multiplicities, absolute
coefficient convergence of the remainder when
`min(Re(s_i)) > 1/(J+1)`, and exact preservation of every coefficient
inside the full anisotropic physical norm horizon after replacing
the indicated factors by literal short polynomials. The proof keeps
all coordinate exponents nonnegative and retains literal zero values
at nonunits. The general ideal statement is distinguished from the
Eisenstein element-row trace. These identities do not transfer the
previous representation's tube estimates, and the new polynomial
pointwise bounds alone do not prove a native moment saving.

The corresponding published review hashes are:

| Review file | SHA256 |
|---|---|
| `reviews/conjugate_pair_initial.md` | `910732baf00a49e7a9d865cc212bd8f9af7c7cee6dab15d6f7f71ea9fb34f04c` |
| `reviews/conjugate_pair_update.md` | `7a86bf818dd7d43db5e7b3829f797f3d5833d24f29836ef548c45ba601c3a957` |
| `reviews/conductor_corollaries.md` | `f64d585b4119236a9a2f7e70742fad8de1c9aa58ab4af72683c688f71284603d` |
| `reviews/necklace_extraction.md` | `1dd5fda2825450c68f826a7168aa06c32c720259485709b870f30817afc81860` |

### Authorship overlap and remaining boundaries

I authored the short-factor non-smallness lemma and the first-order
Euler-trace refutation and contributed to early collision development
underlying the root's CT1 composition. My reconstruction of that
composition has that disclosed overlap; my own work is not counted
as independent review of my own components. Other lanes' reconstructions
are preserved in the packet. Although this receipt checks the final
bytes of all seven mathematical documents, it does not misattribute
the native lane's prime-sector proof or other reviewers' full
reconstructions to me.

The refutations concern the specified larger unfiltered traces, with
their stated trivial datum and legal masks. They do not refute the
native moments obtained after the physical coefficient filters. The
all-distinct signed prime-column result likewise remains a selected
contribution and supplies no lower bound for the complete signed
prime/composite core. These distinctions are present in the published
README and validation text at the previously reviewed hashes.

## 5. Original-source commit/path authentication

In addition to reading the copies from the new content commit, I
freshly fetched every one of the eleven source transports from its
original `PROVENANCE.json` commit and source path through GitHub.
For all eleven, the original remote bytes agree exactly with the
published copied bytes, and their byte count, SHA256 and returned Git
blob agree with provenance.

This covers the seven PR #911 source files, the two PR #929 files,
the PR #913 moment-obstruction file and the PR #914 conductor-sector
file. It completes the original-source authentication deliberately
left outside the earlier local metadata audit. It does not constitute
blanket mathematical revalidation of any of those earlier branches.

## 6. Remote verifier and metadata binding

I reconstructed an isolated packet directory from the remote base64
file contents and ran its already reviewed `verify_packet.py` in
ordinary mode. It returned:

| Check | Result |
|---|---:|
| Overall status | PASS |
| Manifest files | 49 |
| Copied source transports | 11 |
| Mathematical files | 7 |
| Identical ordinary/optimized report pairs | 3 |
| Producer replays in this receipt run | 0 |

The six producer executions reported in validation were performed by
the root before freezing. I do not relabel that earlier execution as
my own. My metadata audit independently exercised the ordinary mode
and five isolated fail-closed controls; this receipt independently
checks that the reviewed code, reports and proof bindings are the
actual published bytes.

The published summary and metadata retain these hashes:

| File | SHA256 |
|---|---|
| `README.md` | `99bddd1fa16ac04171b42ff0cd40a99d32c8752389a4480b239863e0e777493e` |
| `VALIDATION.md` | `c831d02beb41b09e30080b060fbe8000d3b2b6ed4183a020055d291abdbba62f` |
| `PROVENANCE.json` | `5d5f92fbdeccdbb3baec4014adb6dccd140f46739c4acb829626ff6ef8e319d2` |
| `verify_packet.py` | `167619c3585292c6e84518a32b6a763bff5b1a2bcbf7689f95c8ab4a061b314e` |
| `reviews/readme_scope.md` | `622c5c151ab007210c58f236640a7ce17675ede80fc59d172648e3a599e06018` |
| `reviews/metadata_integrity.md` | `0a72afc965081081d4097d6f7abe684ebe9ecc5bb22e7b698f95e912b53c025d` |

The previously pending content-commit and final-manifest binding is
therefore complete for `988f4571bf9ffec65cd73ccb092301550c054ae0`.
Any subsequent publication-receipt commit requires its own check that
the already inventoried mathematical, diagnostic, source and review
files remain unchanged. No mathematical scope is enlarged by this
transport receipt.
<!-- END ORIGINAL RECEIPT: extraction -->

<!-- BEGIN ORIGINAL RECEIPT: native -->
# Native-lane publication receipt

**Disposition:** PASS for immutable-byte binding of the four proofs listed
below to the native-lane mathematical reconstructions already completed.
This receipt is not a new proof, formal verification, external expert
endorsement, or approval of the open native moment hypothesis.

**Reviewer:** /root/native_structural_attack.

**Remote read-back completed:** 2026-10-13 UTC.

**Repository:** GettysburgResearch/riemann.

**Frozen mathematical content commit:**
988f4571bf9ffec65cd73ccb092301550c054ae0.

[Immutable commit](https://github.com/GettysburgResearch/riemann/commit/988f4571bf9ffec65cd73ccb092301550c054ae0)

**Commit tree:** 593dfbf7d305c28e4faa439bef1d64513aedd034.

**Parent:** f9939c957f5aac6b2099b591e4988991700a152b.

The actual Git commit object was read and confirms that tree and parent.
The branch name supplied by the root researcher was
research/sextic-structural-strike-20261013; this receipt is bound to the
immutable commit, not to the subsequently movable branch.

All paths below are relative to
standalone/2026-10-13-sextic-structural-strike/.

## 1. Exact remote proof identities

### EULER_TRACE_RESONANCE.md

[Immutable proof](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/EULER_TRACE_RESONANCE.md)

- Bytes: 10757.
- Git blob SHA1: d4be020948057b86e90a37df1242ff0a05a32038.
- SHA256: c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10.
- Complete remote UTF-8 content equals the exact previously reviewed
  text, including the final newline.
- Returned remote Git blob identity equals the independently computed
  local Git blob identity.

**Bound reconstruction:** the original P13 finite Euler trace has the
stated superpolynomial resonance for every fixed \(k\ge1\), with the
permitted trivial datum and a fixed legal cross-pair deletion mask.
The local numerators and exterior mask make every row contribution
nonnegative. The retained unit row, the chosen prime phases and the
named classical prime ideal theorem give the lower bound. The proof
does not lower-bound a full signed Mellin integral by that row.

### RESONANT_SHORT_TRACE.md

[Immutable proof](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/RESONANT_SHORT_TRACE.md)

- Bytes: 14564.
- Git blob SHA1: d49c771aaf48a1e244905928307c9bef2fed1b8f.
- SHA256: 1c043c4650e72d9c78daef4111a3a2485c6f5d285a1ca2afee62283c9286a70f.
- Complete remote UTF-8 content equals the exact previously reviewed
  text, including the final newline.
- Returned remote Git blob identity equals the independently computed
  local Git blob identity.

**Bound reconstruction:** for every fixed \(k\ge2\) and
\(1/3<\sigma<1/2\), the opposite left-frequency clusters and conjugate
right clusters yield a positive degree-two logarithmic contribution.
The all-\(k\) model coefficient is
\(-[k-2(\lceil k/2\rceil-\lfloor k/2\rfloor)^2]\), which is strictly
negative. The legal fixed mask makes the complete paired trace
nonnegative on every row. The short-factor product lemma supplies a
common permitted grid point, and the frequencies lie outside the
literal WT1 tube. This refutes the exact overly strong CT1 contract,
not the complete norm-filtered native moment.

### SHORT_FACTOR_NONSMALLNESS.md

[Immutable proof](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/SHORT_FACTOR_NONSMALLNESS.md)

- Bytes: 13252.
- Git blob SHA1: 30cddb1c877aaeb8eaa97d2e5f9dc80525b1c855.
- SHA256: 0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935.
- Complete remote UTF-8 content equals the exact previously reviewed
  text, including the final newline.
- Returned remote Git blob identity equals the independently computed
  local Git blob identity.

**Bound reconstruction:** the actual finite Dirichlet-polynomial product
has a nonzero anchor at real part four. Explicit derivative bounds,
complex divided-difference interpolation and a prescribed
\(O(\log Y)\)-point grid force simultaneous product nonsmallness with
loss \(\exp[-C\log Y\log\log Y]\). The argument handles the full product
at one frequency, rather than choosing unrelated good points for its
factors. It uses the literal constant coefficient and coefficient
bounds, not an assumed nonvanishing theorem on the target line.

### HORIZON_NECKLACE_FACTORIZATION.md

[Immutable proof](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/HORIZON_NECKLACE_FACTORIZATION.md)

- Bytes: 20252.
- Git blob SHA1: 1582d4c23d48edf386f9cb08f10ab5b268f07378.
- SHA256: a6aa7ab8925eac3f1f514b6e4138baa87735e3902fa3c5a78679480c7cf925ab.
- Complete remote UTF-8 content equals the exact previously reviewed
  text, including the final newline.
- Returned remote Git blob identity equals the independently computed
  local Git blob identity.

**Bound reconstruction:** the classical primitive-necklace formula has
nonnegative integer multiplicities; cancellation through degree \(J\)
gives absolute coefficient convergence when
\((J+1)\min_i\Re s_i>1\). Every retained factor may be truncated at its
exact physical norm horizon because exponent arrays are nonnegative
and the physical rectangle is a downset. This preserves ideal
coefficients, literal nonunit zeros, and separate equal-norm prime
ideals. Complete Mellin inversion and the all-frequency polynomial
majorant are valid. The smooth plateau variant has the same physical
coefficient rectangle. General fixed-field ideal statements are
distinguished from the specifically two-dimensional Eisenstein row
trace. The full same-side fixed-character twist is retained.

The bound removes the specific superpolynomial representation defect.
It does not prove the stronger signed trace estimate (7.1), improve
the native higher-moment interpolation exponent, or transfer old
partial-tube estimates to the new representation.

## 2. Existing review reports bound to this commit

Both reports were themselves fetched directly from the same remote
commit and their complete contents matched the previously frozen
native-lane reports.

### reviews/resonance_native.md

[Immutable review](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/reviews/resonance_native.md)

- Bytes: 16027.
- Git blob SHA1: 59a1fac2c90c232946be7a7d44bab522b7c3bc3b.
- SHA256: ed607767f2eeb533fde9744a5807c44cc3cad4dae6bdf36dc4dfaef484dab562.

This report binds the first three proofs above. It records reconstruction
of their source contracts, masks, positivity, convergence and
interpolation. The classical prime ideal theorem is a named analytic
input; the report does not claim to reprove that theorem from scratch.

### reviews/necklace_native.md

[Immutable review](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/reviews/necklace_native.md)

- Bytes: 15881.
- Git blob SHA1: cd8ae471f2d5b762c427140d39b7980225c1356f.
- SHA256: 9c682c0610f159b9ebfe4a660ab33fab93139b9e72c58222e6157a657fb71534.

This report binds the fourth proof above. It reconstructs Lemmas 2.1
and 3.1, Theorem 4.1, Corollary 4.2 and Theorem 5.1, together with
their stated critical-line specialization and conditional incidence
price. It does not approve the open trace estimate as a theorem.

## 3. Method of remote authentication

The read-back used the GitHub connector to fetch the commit and each
file with the full immutable 40-character commit as its ref.
No branch-default lookup was used for a proof or review file.

For each of the four proof files and both review files:

1. The entire returned UTF-8 string was compared with the exact
   frozen local content used in the completed reconstruction.
2. The remote returned Git blob SHA1 was compared with the value
   independently calculated from the actual local file bytes using
   the Git blob header, decimal byte count, NUL separator and content.
3. The byte count and SHA256 of those same bytes were checked against
   the previously frozen proof or review identity.

All comparisons passed. Remote string lengths in JavaScript can differ
from UTF-8 byte counts because the manuscripts contain Unicode; no
string-length value was substituted for a byte count.

The actual Git commit object was also read, confirming the tree and
parent stated above. The full commit's unrelated mathematical files
are not approved merely because its metadata was fetched.

## 4. Manifest and public scope disclosures

I also fetched and compared the remote MANIFEST.json, README.md and
VALIDATION.md with the inspected assembled versions. Their full
contents and Git blob identities matched.

### MANIFEST.json

- Bytes: 11569.
- Git blob SHA1: 87a50860c891147b84110536917abc158d1f0562.
- SHA256: 1dede6bc1b60de11b86ccc2abe03cea1560644e2b9ddfabfed9ee27bb2b3f1a8.

This is the exact manifest identity supplied with the frozen content
commit. Its self-exclusion and publication-receipt exclusion are
explicit, avoiding a circular self-hash.

### README.md

- Bytes: 18031.
- Git blob SHA1: b1e38ca23feec6e92609571410e1fe716be68c61.
- SHA256: 99bddd1fa16ac04171b42ff0cd40a99d32c8752389a4480b239863e0e777493e.

### VALIDATION.md

- Bytes: 11612.
- Git blob SHA1: 4ec3bdf7d0d10619a6a10a626a3429e2bcf80007.
- SHA256: c831d02beb41b09e30080b060fbe8000d3b2b6ed4183a020055d291abdbba62f.

For the four proofs within this receipt's scope, those disclosures
correctly distinguish the permitted trivial-twist refutations, complete
norm-filtered identities, partial-frequency-region limitations,
polynomial representation repair, and still-open signed trace and
moment targets. They also correctly disclose the same-team reviews
and development overlap.

This paragraph is a scope check for the objects reviewed here; it is
not an additional independent mathematical review of the conductor
theorems or all other content summarized in the README.

## 5. Independence, computations, and remaining limits

The reviewer and authors are separate agents in the same team and can
share the same model. Their agreement is not formal proof or external
human certification.

For the resonance proofs, I had exchanged preliminary informal
admissibility and sign checks before reconstructing the written
arguments. I did not author the frozen three proof manuscripts.

For the necklace proof, the root supplied and authored the main
construction. I independently checked its horizon mechanism before
freezing, suggested the smooth plateau variant, and authored the
finite necklace diagnostic. Accordingly, this is a separate written
reconstruction with disclosed development overlap, not full
independence from every part of the result's creation.

The finite diagnostics and their ordinary/optimized runs are recorded
in the existing review and VALIDATION files. They were not rerun during
this publication read-back; byte transport, commit binding and scope
disclosure were the purpose of this pass. No finite test is promoted
to an infinite analytic theorem.

No mathematical or repository file was edited during this receipt
task, and no GitHub write was performed. The only newly written file
from this lane is this requested scratch receipt.

The receipt preserves the prior verdicts at the exact immutable bytes.
The full native fourth moment, generalized \(2k\)-th moment hierarchy,
signed long-singleton estimate and RH remain open.

<!-- END ORIGINAL RECEIPT: native -->

<!-- BEGIN ORIGINAL RECEIPT: bilinear -->
# Immutable content-commit receipt: bilinear review lane

**Result:** all six requested remote proof files and the packet manifest match the exact local bytes whose hashes were frozen for this review lane. The two separately authored mathematical reconstructions below bind to the four specified remote proofs at the immutable content commit. The two conductor files are bound as authorship verification, not as independent review.

## 1. Repository and immutable commit

- Repository: `GettysburgResearch/riemann`.
- Content commit: [`988f4571bf9ffec65cd73ccb092301550c054ae0`](https://github.com/GettysburgResearch/riemann/commit/988f4571bf9ffec65cd73ccb092301550c054ae0).
- Tree: `593dfbf7d305c28e4faa439bef1d64513aedd034`.
- Sole parent: `f9939c957f5aac6b2099b591e4988991700a152b`.
- Packet directory: `standalone/2026-10-13-sextic-structural-strike/`.
- Remote read-back completed: 2026-10-13 00:04:50 UTC.

The commit, tree, and sole-parent values were read through the GitHub Git-data GET endpoint and checked against the supplied frozen identifiers. The proof files and manifest were fetched by that full commit hash through the GitHub connector. No mutable branch name was used as the content reference.

## 2. What was checked remotely

Before the remote read, I loaded each corresponding final local UTF-8 file, verified its expected SHA256, and computed its exact byte count and Git blob identifier. I then fetched the entire remote content of each file at the immutable commit. Each returned content string equals the frozen local UTF-8 content exactly; each returned Git blob identifier also equals the independently computed local blob identifier. All seven comparisons passed, counting the manifest.

The SHA256 and byte counts below therefore apply to the exact remote contents, not merely to files with matching names. The Git blob identifiers independently bind the same contents within the returned Git tree. No proof text, review text, repository file, or GitHub object was edited during this read-back.

## 3. Separately authored native reconstruction bound to the commit

| Immutable remote file | Bytes | Git blob SHA-1 | Content SHA256 |
|---|---:|---|---|
| [PRIME_DEGREE_COHERENCE.md](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/PRIME_DEGREE_COHERENCE.md) | 22,934 | `e51dc82a0146e667e3f7c894c3bf4bcb7e9e8c19` | `2290ce3d8d24f832259b3d701607beb125ceb5111f86b39d82be200eea1c27fb` |

The mathematical reconstruction is recorded in `pass3_bilinear_native_review.md`, SHA256 `648e60dad3b1cd236050633eb45616805ee05c4b942e8bb88061d4c4b237ef56`. I did not author the native manuscript. The review first inspected historical hash `f80d42fd162a207889b1e858c2b28660bb5fdfed9011d58991f373f4f709e0bf`, identified two scope issues, and checked the author's two-hunk correction to the final hash in the table. The exact remote content is that final corrected version.

**Scoped verdict:** no load-bearing defect found in the following claims:

- The finite partition-lattice identity and the uniform inequality comparing the complete signed all-distinct Hermitian polynomial with the full positive power, including the explicit constant and the weighted-row consequence.
- The complete signed prime-column lower bound, with original coefficients on every retained column, every original nonunit zero, the contribution from sixth-power rows, and the precise range `0 < h < 6k/5`. The possible negative contribution of all other rows is bounded by the finite inequality.
- The noninteger prime-degree deformation's local analytic obstruction at one, the scalar Mellin contradiction, the distinct limsup moment amplification, and the tangent-coefficient calculation.
- The independent-residue counting benchmark and its exact limitations, and the source-preserving prime-rooting and nonlinear pairing identities.

The corrected prose limits the distinctness conclusion to removing repeated columns; it makes no unsupported assertion about an undefined connected-tuple selector. It also identifies the untwisted prime piece with the rooting identity's `m=1` term only when `nu=1`, retaining `nu(p)` for a general fixed twist.

**Boundary:** the prime-column selector and deformed coefficients are additional source information. Their lower bounds do not refute the complete composite-column native Möbius moment or its full singleton sector. The exact rooting identity does not itself estimate the missing signed cancellation.

## 4. Separately authored resonance reconstruction bound to the commit

| Immutable remote file | Bytes | Git blob SHA-1 | Content SHA256 |
|---|---:|---|---|
| [EULER_TRACE_RESONANCE.md](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/EULER_TRACE_RESONANCE.md) | 10,757 | `d4be020948057b86e90a37df1242ff0a05a32038` | `c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10` |
| [RESONANT_SHORT_TRACE.md](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/RESONANT_SHORT_TRACE.md) | 14,564 | `d49c771aaf48a1e244905928307c9bef2fed1b8f` | `1c043c4650e72d9c78daef4111a3a2485c6f5d285a1ca2afee62283c9286a70f` |
| [SHORT_FACTOR_NONSMALLNESS.md](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/SHORT_FACTOR_NONSMALLNESS.md) | 13,252 | `30cddb1c877aaeb8eaa97d2e5f9dc80525b1c855` | `0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935` |

The mathematical reconstruction is recorded in `pass3_bilinear_resonance_review.md`, SHA256 `e692c23d2176b4df12739e0f7e019c7739ca3f01f46faec43c75831d35bab142`. I did not author any of these three notes. Their exact remote contents equal the respective final hashes reviewed in that document.

**Scoped verdict:** no load-bearing defect found in the following claims:

- `EULER_TRACE_RESONANCE.md`: the first-order counterexample to the original P13 unfiltered Euler-numerator contract. It covers every fixed `k >= 1` at real part `1/2`; its broader theorem covers every fixed `0 < sigma_0 < 1`. Its common conjugate frequency is explicit.
- `RESONANT_SHORT_TRACE.md`: the second-order counterexample to the subcritical CT1 unfiltered short-trace contract, for every fixed `k >= 2` and `1/3 < sigma < 1/2`. Its opposite phase clusters lie outside the exact WT1 tube.
- `SHORT_FACTOR_NONSMALLNESS.md`: the simultaneous lower value for a fixed product of the actual short polynomials on a predetermined shrinking frequency grid, proved by an absolute-chamber anchor and complex interpolation with explicit derivative and amplification bounds.

The reconstruction checked the legal fixed cross-pair incidence allocation; the requirement `Y >= NQ` before that fixed allocation becomes eligible; positivity of every row in the actual paired traces, with literal zeros; the unit row's positive source weight; fixed-scale convergence; the prime-weight comparisons; the real logarithm expansion; the complete pair coefficient; the interpolation remainder; the simultaneous nature of the short-factor lower bound; and domination of every fixed polynomial loss.

**Boundary:** P13 and CT1 estimate different unfiltered objects. The P13 argument does not contradict the previously bounded common-slice collision ratio. The CT1 argument does not establish a critical-line short-trace refutation and does not apply at `k=1`. Neither lower bound passes to the complete signed multivariate Mellin integral with every physical column norm test. The native moment conjecture and the exact filtered identities remain unrefuted.

## 5. Conductor authorship verification, separately labeled

| Immutable remote file | Bytes | Git blob SHA-1 | Content SHA256 |
|---|---:|---|---|
| [CONJUGATE_PAIR_CONDUCTOR_SIEVE.md](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/CONJUGATE_PAIR_CONDUCTOR_SIEVE.md) | 22,931 | `395791010f9bdba0395915c7c7150596bea3ae19` | `220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2` |
| [CONDUCTOR_COROLLARIES.md](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/CONDUCTOR_COROLLARIES.md) | 8,872 | `35dbcad0dc80b6980f7a2262758f01a52ca456f3` | `49d471154fbfb2b8589742a70343f9abfa8e407172648b73f33a14d5f3e3031d` |

I authored these two files. This receipt confirms that the remotely stored contents are the final versions I supplied; it does not count my own work as an independent mathematical review.

`CONJUGATE_PAIR_CONDUCTOR_SIEVE.md` is the source-qualified general-order conjugate-pair conductor deduction, its uniform moving-background mean, and its native positive-accounting application. The final version includes the requested Cauchy–Schwarz step for the two Mellin coefficient vectors, the primitive-associate convention for the background, and the exact compactly supported source majorant.

`CONDUCTOR_COROLLARIES.md` is the fixed-background conductor-size corollary and the exact five-label bound-envelope limitation. Its relative hyperlink names `CONJUGATE_PAIR_CONDUCTOR_SIEVE.md` and its source hash is the final `220d767...` value shown above. Its coverage of all locally exact-order powers applies precisely to the standard-family cases `n=3,4,6`; for order six it omits local components of orders two and three. The combined five-label inequalities still have universal weighted exponent `11/8` for their stated objective.

The conductor proof was separately reviewed by the root and extraction lanes. My receipt makes no new claim about that independent review beyond distinguishing it from my authorship. The imported de Faveri fixed-order sieve and other named analytic source inputs are not re-certified by a content-hash match.

## 6. Manifest binding

- Remote file: [MANIFEST.json](https://github.com/GettysburgResearch/riemann/blob/988f4571bf9ffec65cd73ccb092301550c054ae0/standalone/2026-10-13-sextic-structural-strike/MANIFEST.json).
- Exact bytes: 11,569.
- Git blob SHA-1: `87a50860c891147b84110536917abc158d1f0562`.
- Content SHA256: `1dede6bc1b60de11b86ccc2abe03cea1560644e2b9ddfabfed9ee27bb2b3f1a8`.

The remote manifest content equals the final local manifest exactly, and the supplied expected manifest SHA256 was checked. This confirms the frozen packet's manifest identity; it does not imply that I independently reconstructed every other file enumerated in the manifest.

## 7. Receipt scope

This is a same-team, separate-authorship review receipt for the four proofs in Sections 3–4, together with the explicitly labeled authorship verification in Section 5. It is not external peer review, a proof-assistant certificate, or a whole-repository correctness assertion. No new review verdict for other packet files is implied.

The mathematical reviews were completed before this remote binding; this step verifies that the immutable GitHub contents are exactly those reviewed. The classical prime ideal theorem and the fixed-order analytic sieve remain named inputs with their respective scopes. Finite diagnostics authenticate finite algebra and exponent bookkeeping and are not promoted to proofs of infinite moments.

The full generalized native moment hierarchy and RH remain open. All proof-byte and commit bindings in this receipt refer specifically to content commit `988f4571bf9ffec65cd73ccb092301550c054ae0`. A later metadata or receipt commit must preserve these proof bytes to inherit these scoped verdicts.

<!-- END ORIGINAL RECEIPT: bilinear -->


## Late source-credit and concurrent-work addendum

**Scope:** bibliographic and theorem-scope comparison after the initial
publication freeze. This addendum changes no proof, diagnostic,
manifest entry, or integrated status. The original content commit and
the exact three reviewer receipts above remain immutable records of
what was checked before these additional sources were inspected.
There is no claim of priority for results shared with earlier or
concurrent drafts.

### Earlier collision and necklace work: PR #916

The final freshness check led back to PR #916, frozen at
[dd70e580a5ffdbe5b140784ba6cebd173cb84792](https://github.com/GettysburgResearch/riemann/commit/dd70e580a5ffdbe5b140784ba6cebd173cb84792).
The root and bilinear lane read its actual
[PROOF.md](https://github.com/GettysburgResearch/riemann/blob/dd70e580a5ffdbe5b140784ba6cebd173cb84792/standalone/2026-10-10-all-order-collision-removal/PROOF.md)
and
[CYCLE_FACTORIZATION.md](https://github.com/GettysburgResearch/riemann/blob/dd70e580a5ffdbe5b140784ba6cebd173cb84792/standalone/2026-10-10-all-order-collision-removal/continuation-balanced-closure/CYCLE_FACTORIZATION.md).
Their Git blobs are fd93d4424751a17cc89368039aecbd61e687ad81 and
6d0b1a48b6b5a05535efb63c99f6ce501e243e35, respectively.

That packet already contains:

- the full multivariate primitive-necklace formula, with its proof;
- every fixed-degree factorization and the remainder threshold
  \(\min_i\Re s_i>1/(J+1)\);
- forward and inverse finite convolution with independently shortened
  factor scales and literal row zeros;
- the critical absolute kernel cost
  \((1+\log Z)^{\binom r2}\).

Those are **not new results of this packet**. Its explicit additional
construction is
\(\mathcal R_J\prod_\alpha
T_{\alpha,X_\alpha}^{w_\alpha}\), with every copy shortened separately
at \(X_\alpha=\min_{\alpha_i>0}Y_i^{1/\alpha_i}\) and the absolutely
convergent remainder left unshortened. It spells out the exact
coefficient transport for the physical source. Mixed Hermitian phases
and unequal windows are explicit in this construction, but the earlier
formal-variable and rectangular-convolution arguments already preserve
that geometry.

The original finite exclusion is retained here because only the
remainder's upper and absolute-coefficient bounds are needed: it is
allowed to vanish. The earlier cycle theorem enlarged the fixed
exclusion to control both the remainder and its reciprocal and to
establish nonvanishing. These are different stated scopes, not a
contradiction.

### Concurrent finite repair and stronger CT1 scope: PR #931

PR #931, at content commit
[3968d1b7135900e6130412f58a39bc67e73d4ecb](https://github.com/GettysburgResearch/riemann/commit/3968d1b7135900e6130412f58a39bc67e73d4ecb),
explicitly credits and applies #916 in
[HISTORICAL_CONNECTIONS.md, HC1--HC6](https://github.com/GettysburgResearch/riemann/blob/3968d1b7135900e6130412f58a39bc67e73d4ecb/standalone/2026-10-13-signed-moment-reassessment/HISTORICAL_CONNECTIONS.md).
Its whole-kernel norm-box truncation already gives a polynomial
all-frequency repair. At equal horizons on the critical line, its
collision bound times the short-factor majorants gives the same
\(HY^k(1+\log Y)^{k(2k-1)}\) trace majorant as this packet.
The per-factor construction here is therefore an alternative
implementation, **not the first polynomial repair or an improved
critical bound**. Below one half, its displayed bound need not improve
HC6 either.

The same concurrent packet's
[SIGNED_TRACE_OBSTRUCTION.md](https://github.com/GettysburgResearch/riemann/blob/3968d1b7135900e6130412f58a39bc67e73d4ecb/standalone/2026-10-13-signed-moment-reassessment/SIGNED_TRACE_OBSTRUCTION.md)
gives a different complete-row CT1 refutation, for every fixed
\(k\ge1\) and every fixed finite-order datum, along an unbounded
sequence of permitted real cutoffs. Its two-slot analytic propagation
and higher-slot maximum-principle argument cover a broader twist/order
scope. This packet's CT1 theorem instead uses the trivial datum,
\(k\ge2\), a positive paired trace, explicitly small frequency clusters,
and every sufficiently large cutoff. Its separate first-order P13
Euler-trace refutation is a different target.

Both packets retain the complete norm-filtered identity and leave the
physical native moment open. No partial-tube estimate is transferred
between their representations without proof. The root read #931's
trace, moving-contour and historical comparison notes; this credit
check is not a full independent mathematical review of that packet.

### Concurrent prime-face and deformation work: PR #930

PR #930, at content commit
[c07b9f653b8d0eb82d9f056d935a4ecef6770f56](https://github.com/GettysburgResearch/riemann/commit/c07b9f653b8d0eb82d9f056d935a4ecef6770f56),
already contains the whole signed all-distinct prime-face obstruction
and the neighboring prime-count/deformation and
\(\mu_K\omega_K\) tangent barriers in
[ARITHMETIC_PARITY_OBSTRUCTION.md](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/ARITHMETIC_PARITY_OBSTRUCTION.md),
Git blob d90f394a8026eb983da28edb82a5fba8fa91bb29.
The root and native lane read that actual proof.

Its prime-face theorem holds on arbitrarily large scales for
\(0<h<6/5\). The relative collision inequality in this packet improves
the error after absorption to \(O(H(D/\log D)^k)\), yielding
\(0<h<6k/5\). The named prime ideal theorem gives the stronger
all-sufficiently-large-scale conclusion and explicit logarithmic
denominator here. In the intended range \(h>1\) close to one, #930
already establishes the qualitative obstruction and its exponent
price.

The deformation conclusions overlap after the parameter substitution
\(w=-z\) between the two coefficient conventions. This packet supplies
an alternative amplification argument and a larger stated parameter
disk; it does not newly discover the strategically relevant
deformation barrier. The #930 proof has the advantage of requiring
only its elementary lattice and Mellin arguments.

The native lane also read #930's
[PARITY_DAMPED_MOMENTS.md](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/PARITY_DAMPED_MOMENTS.md)
and the cube-fiber comparison. Its complete positive damped hierarchy
is a substantive complementary result with its stated pointwise and
second-moment premises. The elementary unconditional threshold is
\(t=1/2\); the exact inverse comparison costs \(D^{2kt}\).
Thus the proved damping threshold does not close the undamped
native moment. This is a bounded overlap and scope check, not a
full independent review of every #930 theorem.

### What remains distinct and what remains open

The conjugate-pair conductor deduction, its moving-background native
sector application, the explicit relative finite collision inequality,
and the stated source-contract resonance constructions should be
assessed from their exact proofs. Shared classical identities and
overlapping obstructions are credited above. The per-factor horizon
construction is useful as an exact analytic interface, but its
existence does not constitute a new moment saving.

PR #932 was also noticed in the final frontier check, at head
c63b5aaa5d53dd183abb20299cea4628f0ab57b7. Its PR description reports an
ordinary-zeta bridge and still-open arithmetic capture estimates.
Only that metadata was inspected for this addendum; none of its
theorems is imported or independently certified here.

The complete physical undamped moment, including its long signed
prime/composite singleton contribution, remains the unresolved
arithmetic target. The bibliography and comparison update does not
alter any prior proof's mathematical conclusion.
