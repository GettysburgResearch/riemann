# Immutable-commit review: overlap, continuum audit and original HLC weights

Reviewer: `/root/middle_joint`.

**Disposition: accepted within the mathematical and publication scope
specified below.** The selected remote mathematical objects are exactly
the reviewed files. The committed README preserves the distinction
between proved component/root results, imported analytic premises and
the still-open native estimate. No scope drift was found.

## 1. Exact remote object binding

Repository: `GettysburgResearch/riemann`.

* Reviewed mathematical commit:
  [`8b2c6d50ad2d729c681745717c615095bd8f1d9d`](https://github.com/GettysburgResearch/riemann/commit/8b2c6d50ad2d729c681745717c615095bd8f1d9d).
* Its root tree: `bca4d3e66472fa7fb4c7f37c56b426359a397cb1`.
* Its sole parent: `3a07737bb7b802a5671acaa22a8f86e6b0acbd40`.
* Reviewed directory:
  `standalone/2026-10-25-hlc-zero-free-transfer/fourth-pass/`.

I independently fetched the Git commit object at that immutable SHA,
then the recursive tree at its exact tree SHA. The commit's tree and
parent match the identifiers above. The recursive tree response was
not truncated. I fetched each selected blob by the blob SHA appearing
at its path in that tree. The README was additionally fetched through
its raw URL pinned to the commit; that content matches the blob fetch.
No branch name or default-branch read substitutes for these checks.

For every object below I recomputed both SHA256 of the fetched UTF-8
bytes and Git's SHA1 of `blob <byte-count>\0<bytes>`. The latter
matches the tree's blob ID, the byte count matches its recorded size,
and the fetched bytes equal the local frozen object. All mathematical
hashes match the earlier review or dependency freeze.

| File | Exact remote Git blob | SHA256 |
|---|---|---|
| `COHERENT_IDENTITY.md` | `db0ff0799e983bc43f20dd1b1a9f292f6dbc1490` | `5bd8db8047d5474fd2d33c4691d94e9f38f97b7b97b67ad215ee0ac4fb45a068` |
| `check_coherent_identity.py` | `6becd4af41e58928a997471a100c627fed34f850` | `dc31cbdf26e3ac1da2c3917e63b9a42e736909c2ef8e0d9dcf15f6a59189e0ee` |
| `ATTEMPT_AUDIT.md` | `5a242ae15925c0c0a58e2686e46436981d40e1fe` | `5209ac000a0646d07fc923f3a9c943236489c2645763c14f713d6993830a08ea` |
| `CLOSED_TRIANGLE_WEIGHT.md` | `999510900504d8ee0e3e318dc79a856f29e28bd4` | `169112b8b41ede59ba23009e5b23d06184e19c03cad209d40940edf1568f7e37` |
| `check_closed_triangle_weight.py` | `9467a1a1766e945e43a66bfe9c3fcc61c39a0840` | `3aed0d03eda009fbe93b2f17de320c89d7ce94b93f5487c843114d9e8d6a6d1b` |
| `THREE_EDGE_INTEGER_BRIDGE.md` | `481645aba5dc6d87455f7a69b7421c979b43a7d5` | `9f4f7e2c327a30b8ce530da9d588d671367eb9d8bb1778c3c3dc8bccb68ff067` |
| `check_three_edge_integer_bridge.py` | `ca5e38f028b1c39bb12deae087e4844e52d8a786` | `65b15c1ed27765285347b85b0235f2524ceab33b52229957dba4b5f206909866` |
| `README.md` | `c31b75a931e1c850a984f7514a1b188d5e1e75d3` | `1d17ecbfaaf47bc3cc00e47eab914c85f6383110be6630794d0998a50f477dcc` |

This record binds the mathematical commit above. It does not purport
to bind itself inside that earlier commit or approve an arbitrary
later branch head.

## 2. Mathematical review carried forward to these remote bytes

The independent mathematical reviews are recorded in
`REVIEW_COHERENT_IDENTITY.md`, `REVIEW_ATTEMPT_AUDIT.md`, and
`REVIEW_CLOSED_TRIANGLE_WEIGHT_MIDDLE.md`. Their conclusions apply
to the exact remote bytes identified above.

For the coherent overlap, I reviewed the three-Mellin representation,
the common character and row mask, the order of contour/tail treatment,
the same-bin exponent bound, and the exact four-term corner identity.
The coefficient return does not establish a signed row-mean lower
bound or allow an unproved intersection estimate to be assumed.

For the continuum audit, I checked the original source kernel
normalization, the logarithmic-T derivative and its support, the
uniform original-far estimate, Sobolev before Chebyshev, the one common
buffer and exceptional set, and the exact repeated primal coefficient.
The rejected extra raw `1/Y` normalization stays rejected. Varying
the ratio scale supplies simultaneous localization but no free
orthogonality or extra power saving.

For the closed triangle, I checked the actual root-orbit measure,
all three symmetrization factors, the unique shared-list labeling,
prime-level distinctness forced by legal replacements, and one line
draw per used prime. I checked the global-root candidate multiplicity,
the weighted gcd sum, the original `d_0/D` edge factor, and the
source's Appendix A.5 discrepancy budget. The bridge dependency was
reviewed here for the candidate-count and gcd inputs used by that
triangle theorem; its other independent review covers the full
integer/Eisenstein bridge note.

The relevant finite checkers were previously run independently under
Python optimization. This publication review verifies their exact
remote identities; it does not repeat an optional full test run.
It does not make a GitHub Actions or CI-status claim.

## 3. Audit of the committed README's native conclusions

I read the complete committed README fetched at the exact SHA above.
Its opening status correctly says that RH and a new unconditional
zero-free region remain unproved. The native analytic deductions are
explicitly relative to their pinned external framework.

The narrow primal coefficient retains the two actual Möbius factors,
the original natural character, the ordinary factor and the stated
smooth band `U^.735<Nm<2U^.773`. The README gives the active buffered
zero/amplitude box and reports the complementary count margins as
`23/16000`, `371959/307200000`, and `1099/768000`. It identifies
the finite-ray coefficient, mask, inducing-character, prime-support
and row-profile conditions as retained in the detailed notes.

The large-value assertion `(W_thin)` is expressly open. The boundary
`0.8748856` is identified as a conditional consumer target requiring
that estimate and the imported analytic premises. The corresponding
Dirichlet and zeta statement is confined to the inherited base-change
scope. The auxiliary row parameter delta is not misidentified as the
real part of a target zeta zero.

The large-divisor representation is not presented as an independent
second Möbius saving. Its compensating signs and positive resource gap
are displayed. Likewise, the signed affine formulation keeps the
natural zeros, conjugation, primitive contents and field-valued shift;
its sufficient one-sided aggregate estimate is still labeled open.
The equal-sixth-core bound is a proved resonant-locus payment, not a
proof of the remaining correlation.

## 4. Audit of the committed README's root and HLC conclusions

The README separates complete finite-field bridge laws from actual
integer-path distributions. It does not infer that a conditioned
source history has a Haar or independent root law. It retains the
source kernel's `d_0/D` factor and explains that the proposed extra
raw `1/Y` factor was rejected.

The first paid triangle class is identified as the common-shared-list,
list-diagonal raw three-edge contribution. The later theorem explicitly
extends to different endpoint lists while retaining both coordinates
of the source root vector. Neither is described as a bound for the
complete raw or centered operator, arbitrary surrounding histories,
changing shared lists, or the native inverse expression.

The root-count summary correctly states an absolute matrix-class
discrepancy `H^(kappa-1+epsilon)`, uniform in squarefree S, and the
prescribed-line discrepancy `S^2 H^(kappa-1+epsilon)` with the exact
odd-root density. It expressly warns that an absolute error need not
be small relative to a matrix-class main term. The elementary
kappa=3/4 proof and the imported classical kappa=1/2 bound are
distinguished; no priority claim for the classical methods is made.

The full common-D error exponent `(4J+13) beta-(1-kappa) delta`
and the example with J=K=1, H>=x^(1/4), and prime band
`[x^(1/800),x^(1/400)]` agree with the written corollary. The
elementary bound is exactly
`x^(-1/800+epsilon)+x^(-1/50+epsilon)`. The README explicitly
keeps this x-scale separate from the native U-scale. It restricts the
polynomial-band example to fixed J rather than claiming that the
source's original growing-J scheme has been transferred.

These statements preserve the proved and unproved boundaries of the
committed mathematics.

## 5. Bounds of this attestation

This is an internal independent-agent review. I authored
`MIDDLE_JOINT.md`, `OFF_DIAGONAL_TRANSFER.md`, and
`ROOT_COUNT_REFINEMENT.md`; their independent proof reviews were
performed by other agents. This record does not claim an independent
author review of those files. Its original independent proof reviews
concern the overlap, continuum audit and closed-triangle source
weights, and its present README audit checks the committed summary
against the established theorem scopes.

The exact remote checks above cover the eight listed objects. The
repository-wide preservation check of all old blobs, the complete
new-payload manifest, and the isolated ten-checker replay belong to
the separate root publication record. I do not infer those broader
checks from this selected-file verification.

No frozen mathematical file was edited during this attestation.
No merge, branch update, main-branch modification, or external review
status is certified by this document. It records acceptance of the
identified mathematical commit within the scopes stated here.
