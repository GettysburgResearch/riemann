# Frozen-source receipt: spectral mean and shifted Gauss continuation

**Reviewer:** `scale_covariance_attack`. **Date:** 2026-10-10.

**Verdict:** **PASS at the exact source-conditional scope stated below.**
The two reviewed proof files in the published source are byte-for-byte
identical to the contents independently reconstructed in the earlier
review. This receipt binds that review to an immutable Git commit. It
does not amend either proof or the earlier review.

This is an AI-agent analytic review. The reviewer did not author
`SPECTRAL_ROW_MEAN.md` or `SECOND_REFLECTION_BOOTSTRAP.md`. Authored
dependencies and the resulting independence boundary are disclosed in
Section 4.

## 1. Exact frozen source

- Repository: `GettysburgResearch/riemann`.
- Source commit: [`8f2acaacddc10bd8fb053a66070a1d06d25aa922`](https://github.com/GettysburgResearch/riemann/commit/8f2acaacddc10bd8fb053a66070a1d06d25aa922).
- Source tree: `94bf5570710b88d2bb254cc6d274b4654411510f`.
- Sole parent: `2edc467ef4dea4aa685219ac6a558a158b88768d`.
- Directory: `standalone/2026-10-10-signed-covariance-descent/`.

The following are the raw committed blob identities, not hashes
inferred from a branch name or from a working-tree path.

| File | Git blob | SHA-256 | Bytes |
|---|---|---|---:|
| `SPECTRAL_ROW_MEAN.md` | `bb4f6d8948a3e0ccd0f690e7380c1a71d20cf223` | `5154dc7d0502555f9a198eed386b9926bf1769ac61ae6b7c6fa319eadec7ace1` | 11136 |
| `SECOND_REFLECTION_BOOTSTRAP.md` | `38a2594ee38b14abbb8c6217352c9047e869e0f1` | `e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0` | 18957 |
| `INDEPENDENT_SPECTRAL_BOOTSTRAP_REVIEW.md` | `5f714b17ca509cf292871ab2e01ba3d9e9e36556` | `a356fa28787228ac87f70fc2452918063d5f1509aaf3257faf6c5a8470f78864` | 10865 |

The first two SHA-256 values and byte counts exactly match the table
in the committed independent review. The committed review itself
matches the previously issued review contents.

## 2. What was checked against the commit

The reviewer inspected the commit metadata and tree, obtained the
proof and review contents using `git show <commit>:<path>`, computed
SHA-256 hashes and byte counts of those raw bytes, and checked their
Git blob identities. Both complete proof files and the earlier review
were read from the committed objects. Their current working copies
were also compared and are identical, but that working-copy comparison
is not the source lock.

There is no changed proof content requiring a new mathematical
reconstruction. On rereading the committed files, the reviewer again
checked the cube exponent and omitted-prime masks, the two dyadic
crossovers and strict strip margins, the identity `K_p y_p=x_p`, the
change of variable `u=v-s`, the conditioned-divisor convergence
exponent, and the physical exponent comparison. The detailed
independent reconstruction remains in the committed
`INDEPENDENT_SPECTRAL_BOOTSTRAP_REVIEW.md` identified above.

The original reconstruction directly consulted the imported October 5
`paper2.tex`, including `eq:T`, `eq:completed-twist`, and `prop:R`,
at the retained OpenAI/math source
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The conditioned-theta
interfaces from PR #920 remain fixed at mathematical source
`6aceafc1729ca0962eb12519b407b69c3b5a4d5f`. This receipt does not
substitute a later version of either source.

## 3. Accepted mathematical scope

### Spectral row mean

The complete statement and proof of `SPECTRAL_ROW_MEAN.md`, Theorem
1.1, are accepted conditional on its declared imported completed-theta
mean square and classical squarefree sextic large sieve. The family is
the literal canonical Gauss family, with squarefree primary rows,
fixed bad-prime and finite ray data, and a moving squarefree auxiliary
divisor `d`. It retains the character zeros at the moving row and at
`d`, including the cube completion's omission of `d`.

Both the completed and uncompleted Dirichlet families continue
holomorphically to `Re(u)>1/2`. On each strict closed strip
`5/8<a_0<=Re(u)<=a_1<1`, the accepted estimate is

\[
\sum_{k\in\mathcal K_Q}|G_{k,d}(a+it)|^2
\ll Q^{1+\epsilon}(Nd)^{1-a+\epsilon}(2+|t|)^M,
\qquad a=\Re(u),
\]

uniformly over the stated row subsets and fixed finite ray family.
The same estimate holds for its exact cube completion. No endpoint
claim at `a=5/8` is accepted.

The checks include the uniform use of source Proposition R as the
smooth block length tends to infinity, weighted Cauchy over all cube
indices, normal dyadic convergence, the two conductor crossovers,
vertical smooth seminorms, and uniform division by the absolutely
convergent cube Euler factor. They do not reprove the imported
automorphy foundation or its all-row theorem.

### Shifted Gauss continuation and its row mean

The acceptance covers `SECOND_REFLECTION_BOOTSTRAP.md`, Sections
1--4, the mean-square implication in Section 6, the exact interface
requirements in Section 7, and the conditional physical exponent
comparison in Section 8.

For the standard-face object defined there, the hypothesis
`varrho^3=bar-rho^3` is retained. It yields `K_p y_p=x_p` on good
primes. Summing every cube valuation first cancels the exact exterior
reciprocal Euler factor. Extracting `K_p` at the squarefree primes
then gives the canonical Gauss variable `u=v-s`, with the literal
conditioned-divisor zero mask. This proves the claimed continuation
to

\[
\Re(v-s)>\tfrac12,\qquad
\Re(v)<1,\qquad
\Re(v)-3\Re(s)>1,
\]

and its stated individual conductor bound on strict subregions.
Combining that representation with the reviewed spectral theorem gives
the square-root row norm when additionally `5/8<Re(v-s)<1`. The
row-dependent divisor coefficient is bounded as a contraction; it is
not presumed independent of the row.

The limiting balanced scalar exponent `13/16` and Section 8's
comparison of the candidate energy `Q D^(13/8)` with the previous
factorwise/classical minimum are accepted at their stated conditional
scope. That candidate is dominated by the previous minimum at every
row scale. This receipt does not promote the candidate to an
unconditionally composed bound for the whole physical completion.

For Section 5, the elementary inactive-frequency identity and the
displayed norm exponent were checked. Its narrative assertion about
restoration of every phase under the repeated involution is not used
by the accepted theorems and is not separately certified here.

## 4. Authored dependencies and review independence

This reviewer authored the following other files in the same frozen
source:

| Authored file | SHA-256 | Role in the reviewed notes |
|---|---|---|
| `ALL_CUSP_COEFFICIENT_ADAPTER.md` | `bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1` | Supplies part of the additional all-cusp interface named in bootstrap Section 7. |
| `SUPPORT_PRUNED_COVARIANCE.md` | `83ba41487ce6e0d1e81e2efbecc21be5c364134b97639afa0b12680765f0c8e3` | Contains one source account of the physical envelope used in bootstrap Section 8's comparison. |

Those committed blobs were also obtained and hashed to confirm their
identities. This receipt is **not** an independent review of either
authored file. In particular, the review of bootstrap Section 7 checks
the required interface and its use; it does not independently certify
this reviewer's own coefficient adapter. Section 8's accepted
comparison is the algebraic comparison under its specified physical
bounds, not a claim that the authored source proof has received an
independent review from its author.

Neither core theorem requires silently assuming the complete all-cusp
identification: the spectral theorem concerns its explicitly defined
canonical family, and the bootstrap theorem retains its explicit cube
character hypothesis. Identification with the actual reunited
three-cusp object requires the separately reviewed coefficient adapter,
finite cube covariance, and full composition. This receipt does not
independently accept `FULL_CUSP_DESCENT.md` or replace the separate
reviews of those dependencies.

## 5. Final acceptance boundary

The exact committed spectral theorem and the specified bootstrap
deductions pass with their declared analytic inputs and strict domains.
The essential source dependency is the imported uniform completed-theta
estimate for the exact normalized and masked family; a failure of that
input, or a mismatch in the cube identity or canonical coefficient
family, would invalidate the respective deduction. These inputs are
explicit, not supplied by a numerical experiment.

No source proof or earlier review was changed during this frozen
verification. No Lean build, numerical moment experiment, external
human review, or independent reproof of the imported theta foundation
is claimed. The original fourth and generalized inverse moments,
their all-row extension, and their critical long-dual covariance are
not accepted as proved by this receipt.
