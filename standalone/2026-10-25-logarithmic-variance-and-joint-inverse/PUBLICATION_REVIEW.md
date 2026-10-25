# Publication review: logarithmic variance and the joint inverse

25 October 2026. Coordinator review, with a separate independent remote
authentication appended below.

Status: reviewed proposed analytic components at their stated source
scope. **No improved zero-free boundary is accepted by this report.**
Independent agent review is not external peer review or formal proof
verification.

## Frozen mathematical object

- Mathematical commit:
  df2879b2d5c7f36a2ae50e303ad8c4197c9c0397.
- Tree:
  9580faa4c3862f3c126f9312664c3a090a0df00d.
- Parent:
  9b6aaaf8b969cdb55b909a5bd5d5e949dc49f154.
- Branch:
  research/fresh-zero-free-routes-20261024.
- PR:
  https://github.com/GettysburgResearch/riemann/pull/1021.

The mathematical commit adds exactly 15 files under
standalone/2026-10-25-logarithmic-variance-and-joint-inverse.
The parent, previous two packets, and every other repository path are
unchanged. Main was read at
f99d9e3908dde4865377c75d9ca051c1f545bf4f.

The coordinator computed the local staged Git tree before publication,
created the remote tree, and verified exact equality of both tree
identities. A fresh GitHub commit-object read independently confirmed
the parent and tree. Fetching the published branch produced the same
objects; the local checkout was synchronized only after checking that
its staged tree was identical.

The frozen manifest has 3,643 bytes, SHA256
8e8f9748de69d1772435a72744a44ec23ba9ac2a5e09e84100da1100a9b27a94,
and Git blob ae9d70ba61207ce1296fb52811a7e861b7e409ee.
It identifies the other 14 files. This review-only follow-up adds the
present report without modifying that manifest or any frozen proof.

## Load-bearing proofs

| File | SHA256 | Git blob |
| --- | --- | --- |
| spectral/LOGARITHMIC_VARIANCE_SELECTOR.md | e7910ca304881bf384c1b1a3781eb486b2c803446a313e3475242a7d871265c3 | 6a0f6f8ee30c4596b4cf06e7c1e2fbca1ffd2453 |
| spectral/SIGNED_GAUSSIAN_SELECTOR.md | 3572375e7c00898cd284d3a843955dbdd07cbd075c7e98d8bc6823e3b85f0efa | f8d267d5df3094a33ef9cc824adf403b00c884bc |
| spectral/PRIME_MODEL_SPECTRAL_FLOOR.md | 642acd096866d14193e6554b8273819f94e11423177886270e622ef78135412b | bf6fcc0d62c93da6cc810f273051af33dae59dd0 |
| native/JOINT_LOG_DERIVATIVE.md | 4a1156b0dfafe64eb8f6dbf8f76a597a6a4c09bb6c65308e3dde6868571dcb29 | cf9b3b3b7eb317b9f7738d64c385fe2d29b98339 |
| fractional/JACOBI_NORM_TRANSFER.md | b8eb20ac49897174dbb502da30fce92a1b4d4a1816082911b69d661df1956567 | cd6c8358325c9e23de3012bc2b819fc75b75b3ce |

## Mathematical review and authorship

### Logarithmic-variance selector

The coordinator authored this proof. Its independent analytic reviewers
were fractional_global and spectral_floor. The latter also contributed
the earlier Gaussian selector and discussed its extension; that overlap
is disclosed in the review. The fractional reviewer did not author the
new argument.

The reviews check the actual Connes--van Suijlekom matrix-class theorem,
the full-legality rank-one reduction, removal of the compulsory Fourier
zeros, the exponent V minus twice the compulsory variance, and the
polynomial bound for total variation. They verify the ceiling margin
and the compatible cosine-power example without treating it as a
solution of the source equation.

The growing Gaussian estimates have constants uniform for M>=1.
Endpoint subtraction leaves a C1 zero extension, and the weighted
residual bound retains every prime, pole and archimedean term. The
positive overlap decays only as M^(-1/2), while the residual at
M=a/(10 log a) decays as exp(-c a log a+O(a)).
The variational proof handles negative and nonnegative legal shifts.

The fixed transform exp(1-cosh(z/10)) has the stated contour-strip
decay and the required doubly exponential real-frequency decay.
Its finite approximation is checked against the complete source.
The Laplace residues never vanish, and the nonnegative-integrand
argument applies to every hypothetical off-line zero.

Review found a missing plus sign in the sum of errors in equation (31).
It was corrected before the reviewed hashes and mathematical freeze.
The source-dependent inequality V_a<=a/(10 log a) remains open.

### Fixed-variance Gaussian selector

spectral_floor authored this note; native_bootstrap independently
reviewed it. The coordinator read the full proof and checked the
compulsory-zero compatibility before publication. The first attempted
Fourier schedule would have made the variance requirement impossible;
the final compatible schedule and explicit witness resolve that issue.

The independent reviewer required the explicit hypothesis eta>=0 in
the spectral-growth consumer. Without it, absorption of the fixed
Gaussian form term would be invalid. The final file contains that
hypothesis; its eta=0 application was unaffected.

The result removes physical positivity under the exact stated
all-scale variance and full-legality conditions. It does not construct
such a family of resolvents.

### Prime-discrepancy floor

spectral_floor authored this note; native_bootstrap independently
reviewed it. The coordinator independently checked the cancellation
of the e^(|u|/2) pole contribution, the remaining Fourier multiplier,
the digamma recurrence, the endpoint term in the differentiated
autocorrelation, and the sign of Stieltjes integration by parts.

The coordinator and reviewer opened Johnston--Yang's primary source
and verified Theorem 1.4, equation (1.7), including its constants and
x>=23 threshold. Its underlying numerical verification was not rerun.
The source-dependent spectral bound is proved from that imported
arithmetic estimate. It returns the same power exponent beta and
cannot be reported as a bootstrap to a stronger zero-free boundary.

### Joint inverse and prime-square correction

native_bootstrap authored the note. spectral_floor supplied the
hash-bound independent review. fractional_global separately checked
the complete-convolution and prime-square formulas before publication;
the coordinator also reconstructed their signs and scaling.

The identity mu_E*Lambda_E=-mu_E log N applies to the same completely
multiplicative zero extension and common norm height. The reverse
profile adapter requires large enough total length on its fixed
annular support. Both directions are retained, so the complete
convolution is not called an improved inverse exponent.

The prime-square coefficient is 1/sqrt(L Np); the exact single-prime
deletion series includes its geometric norm and phase factors.
Minkowski uses the original unmarked moment on every nonempty
residual scale. Review prompted explicit direct treatment of supported
scales below one, where only finitely many ideals occur and an O(U)
moment suffices.

The coordinator separately recomputed the critical class in
Q(sqrt(8289)): its defining polynomial, the exact length split, the
intersection of the displayed long and short counts, and R=2/3 agree.
Decimal values in the note remain diagnostic, not directed intervals.

The squarefree prime-divisor weight is still outside the native
coefficient scope. No lower bound for a selected annular product in
terms of the complete signed convolution is inferred.

### Jacobi norm transfer

fractional_global authored the note; native_bootstrap independently
reviewed it. The coordinator checked the local fractional-linear
substitution, the norm-profile completion, the moving-radical cost,
and the actual total loss.

Review prompted explicit treatment of x=0,-1, where a zero multiplier
must not be passed to the moving-twist theorem. Their possible
unit-ideal terms are paid directly, and the self-dual lattice measure
is normalized to covolume one. The nonprincipal subfamily qualification
and all excluded principal-inducing cases remain visible.

The paid bound is worse than the direct trivial estimate. This note
is an exact exploratory transfer with an identified failed estimate,
not a native mean saving.

## Review records and computation scope

Seven separate hash-bound reports are resident in reviews/:

- LOG_VARIANCE_REVIEW_FRACTIONAL.md.
- LOG_VARIANCE_REVIEW_SPECTRAL.md.
- NATIVE_REVIEW_SIGNED_GAUSSIAN.md.
- NATIVE_REVIEW_PRIME_MODEL.md.
- JOINT_LOG_DERIVATIVE_REVIEW_SPECTRAL.md.
- NATIVE_REVIEW_JACOBI_TRANSFER.md.
- OVERVIEW_REVIEW.md.

The overview review verified the comparison with the earlier positive
finite-selector theorem, all displayed source qualifications, and the
large-total-length condition for reversibility. It also independently
confirmed that PR #1022's later head adds reviews only.

The new results are analytic proofs and source-qualified implications.
No matrix census, positivity grid, asymptotic fit, or generic JSON check
is offered as proof of the all-scale variance condition. Hash and tree
checks authenticate publication bytes and preservation, not arithmetic
cancellation. The small exact algebra recalculations support the
displayed constants and critical-class identities only.

## Remaining claim boundary

The strongest new sufficient spectral hypothesis is the actual full
legal selector inequality V_a<=a/(10 log a), with N_a=ceil(4a log a).
No cofinal family satisfying it has been established.

The arithmetic gain needed at the critical detector lengths remains
an estimate for the squarefree divisor-weighted Mobius polynomial, or
a new valid lower-bound mechanism for the complete signed convolution.

The inherited working zero-free boundary is unchanged. Neither this
report nor the internal reviews approve integration of an RH claim
or an improved boundary.

---

## Independent remote authentication

The following report was written by fractional_global after reading the
exact published commit through the GitHub connector. It is appended
without changing the frozen mathematical files.

# Independent authentication of the frozen third-pass packet

Date: 25 October 2026.
Reviewer: `/root/fractional_global`.
Status: **PASS for exact remote-object and byte authentication.**

This is a read-only authentication of the mathematical freeze. It does not prove the open all-scale selector hypothesis, strengthen any source theorem, certify an external preprint, or establish a new zero-free region. The separate analytic reviews retain their original scope.

## 1. Exact remote identity

- Mathematical commit: `df2879b2d5c7f36a2ae50e303ad8c4197c9c0397`.
- Commit tree: `9580faa4c3862f3c126f9312664c3a090a0df00d`.
- Sole parent: `9b6aaaf8b969cdb55b909a5bd5d5e949dc49f154`.
- Parent tree: `c6d5c8ad65be84a5197bc71951fcc3b4f5018563`.
- Packet: `standalone/2026-10-25-logarithmic-variance-and-joint-inverse/`.

I independently fetched the exact commit object, its parent object, both recursive trees, the parent-to-commit comparison, and all fifteen new blob contents through the GitHub connector. Both recursive trees explicitly report that they are not truncated.

Read endpoints:

- [Frozen commit object](https://api.github.com/repos/GettysburgResearch/riemann/git/commits/df2879b2d5c7f36a2ae50e303ad8c4197c9c0397).
- [Frozen recursive tree](https://api.github.com/repos/GettysburgResearch/riemann/git/trees/9580faa4c3862f3c126f9312664c3a090a0df00d?recursive=1).
- [Parent commit object](https://api.github.com/repos/GettysburgResearch/riemann/git/commits/9b6aaaf8b969cdb55b909a5bd5d5e949dc49f154).
- [Parent comparison](https://api.github.com/repos/GettysburgResearch/riemann/compare/9b6aaaf8b969cdb55b909a5bd5d5e949dc49f154...df2879b2d5c7f36a2ae50e303ad8c4197c9c0397).

The commit object has the stated tree and sole parent. The comparison is one commit ahead and zero behind, with exactly fifteen added files, zero modifications, and zero deletions. Every added path lies in the stated packet.

## 2. Checks performed independently of the manifest

For every remote blob, I UTF-8 encoded the connector's retrieved content and independently computed:

1. Its exact byte count.
2. SHA256 of those bytes.
3. Its Git blob identifier, using the standard `blob <length>` header, NUL separator, and content bytes.
4. Literal equality with the corresponding local file bytes.

All fifteen contents matched their remote tree identifiers and sizes and their local bytes. This is not merely a comparison between manifest fields: the remote contents themselves were fetched and rehashed.

I also reconstructed all 199 tree-object hashes in the new recursive tree and all 194 tree-object hashes in the parent tree from their modes, names, and child object identifiers. Every object matched. A separate read-only `git ls-files --stage -z` inspection found only stage-zero entries; reconstruction of the complete local staged tree yielded exactly `9580faa4c3862f3c126f9312664c3a090a0df00d`. No ref, index, repository file, or remote object was mutated by these checks.

## 3. Main theorem and its prior analytic review

The remote `spectral/LOGARITHMIC_VARIANCE_SELECTOR.md` is:

- **20,052 bytes**.
- SHA256: `e7910ca304881bf384c1b1a3781eb486b2c803446a313e3475242a7d871265c3`.
- Git blob: `6a0f6f8ee30c4596b4cf06e7c1e2fbca1ffd2453`.

These bytes equal both the local packet copy and the separate scratch theorem used for the independent analytic review. The approved hash includes the corrected addition of errors in equation (31) and the explicit finite rank-one reduction. Publication has not changed that mathematical object.

The corresponding `reviews/LOG_VARIANCE_REVIEW_FRACTIONAL.md` is also authenticated below at its previously reported SHA256. Its approval remains a conditional analytic approval; it does not supply the unresolved variance bound for actual legal source resolvents.

## 4. Manifest authentication

The remote `MANIFEST.json` is:

- **3,643 bytes**.
- SHA256: `8e8f9748de69d1772435a72744a44ec23ba9ac2a5e09e84100da1100a9b27a94`.
- Git blob: `ae9d70ba61207ce1296fb52811a7e861b7e409ee`.

It contains exactly fourteen entries, one for every other packet file and no additional path. Each entry's path, byte count, SHA256, and Git blob equals the independently computed remote-content result. Its parent pin equals the actual commit parent. The manifest itself was fetched and authenticated separately, rather than being expected to list its own hash.

## 5. Complete authenticated file list

Paths below are relative to the packet directory.

| File | Bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| MANIFEST.json | 3,643 | `8e8f9748de69d1772435a72744a44ec23ba9ac2a5e09e84100da1100a9b27a94` | `ae9d70ba61207ce1296fb52811a7e861b7e409ee` |
| README.md | 9,752 | `0fb745228bdf21fbeab677411e7910decc69d7081058483cb90b0d7ee6013afe` | `4fd45755a6ea6d8dbb9fdb9d0352183907c11500` |
| SOURCES.md | 4,507 | `3b34c3104b52bab23593abbf6eeaaf4025e45997a7c9eec073c992f4de9aed4f` | `1bf333c36075f98c27ecb4618fe4251b349d9074` |
| fractional/JACOBI_NORM_TRANSFER.md | 8,735 | `b8eb20ac49897174dbb502da30fce92a1b4d4a1816082911b69d661df1956567` | `cd6c8358325c9e23de3012bc2b819fc75b75b3ce` |
| native/JOINT_LOG_DERIVATIVE.md | 15,669 | `4a1156b0dfafe64eb8f6dbf8f76a597a6a4c09bb6c65308e3dde6868571dcb29` | `cf9b3b3b7eb317b9f7738d64c385fe2d29b98339` |
| reviews/JOINT_LOG_DERIVATIVE_REVIEW_SPECTRAL.md | 8,984 | `f18c7228fb20d85929d647315afcb33b8559075952929eb468f19b342180cecb` | `1d2d7421d18f7635296411198bd0ca9f8e3f2237` |
| reviews/LOG_VARIANCE_REVIEW_FRACTIONAL.md | 12,369 | `9d0e96af89f53b5fb6b72079fb5c289facf9a51c4616b51c828793f5e310e027` | `ae03ecc8d5b81abb0bde698a1640cd908f4bbdd2` |
| reviews/LOG_VARIANCE_REVIEW_SPECTRAL.md | 9,907 | `d5374e390808fc7d0f60983f6a62f53e5168d4a161e63491f0294f117db9fc93` | `6af8a92caf8c44859847bdb72b9055324df24e92` |
| reviews/NATIVE_REVIEW_JACOBI_TRANSFER.md | 5,032 | `bae340f2ec78bc5f23f37310ff858e1daa5f11e84ec01b12470ffed5090a396c` | `d006f5812ac5f566dd1d4f0939f20990c18e07db` |
| reviews/NATIVE_REVIEW_PRIME_MODEL.md | 4,700 | `e10b1ca6fbfb53fdd7c7ea1e680a4fd6e2b1f2e2098d80d98cb8e2a04e43cacb` | `e41ae4439ea6ebac4e7ac4c89de20b2a9eab50c6` |
| reviews/NATIVE_REVIEW_SIGNED_GAUSSIAN.md | 6,767 | `9442ed00c24fd6304ea0344c0fe56acaad75e470f9ce3eea78fe71cf004ba0e1` | `ea1dd23a1e0c4b0ca4677d9bc446b546f0d9ff3b` |
| reviews/OVERVIEW_REVIEW.md | 6,226 | `755a282fe0ed2dae8cf41dc5621e32db8e6b56933818cec93769df027c2c7d25` | `a03b2ae89b4020fab3887818078e4e1f9b804bc8` |
| spectral/LOGARITHMIC_VARIANCE_SELECTOR.md | 20,052 | `e7910ca304881bf384c1b1a3781eb486b2c803446a313e3475242a7d871265c3` | `6a0f6f8ee30c4596b4cf06e7c1e2fbca1ffd2453` |
| spectral/PRIME_MODEL_SPECTRAL_FLOOR.md | 10,049 | `642acd096866d14193e6554b8273819f94e11423177886270e622ef78135412b` | `bf6fcc0d62c93da6cc810f273051af33dae59dd0` |
| spectral/SIGNED_GAUSSIAN_SELECTOR.md | 22,345 | `3572375e7c00898cd284d3a843955dbdd07cbd075c7e98d8bc6823e3b85f0efa` | `f8d267d5df3094a33ef9cc824adf403b00c884bc` |

## 6. Preservation of the prior packets and repository

A full comparison of the parent and new recursive file maps found that all **882 pre-existing file objects** retain the same path, mode, type, and object identifier. No prior file was deleted. In particular:

| Prior packet | Unchanged subtree | Existing files |
| --- | --- | ---: |
| standalone/2026-10-24-fresh-zero-free-routes | `18e46948dfa404c3f9ed00de77f3961f6756d0b4` | 31 |
| standalone/2026-10-25-selector-and-marked-estimates | `f60b99fb0b5060032376601ba177301d96c3f78c` | 25 |

The two prior mathematical packets are therefore byte-identical across this commit. This preservation conclusion concerns the exact frozen parent and child objects, not an assumption about a live branch name.

## 7. Publication boundary

The remote mathematical freeze matches the local staged tree and all independently reviewed hashes reported here. The authentication result supports publishing a review-only follow-up. It does not authorize changing the frozen mathematics under the same identity; any such change needs its own hash and applicable review.

Only scratch authentication evidence and this report were written during this task. The frozen repository files were not modified.
