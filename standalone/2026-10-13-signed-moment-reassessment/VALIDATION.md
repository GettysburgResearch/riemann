# Source freeze, review and validation

## Publication identity

| Field | Value |
|---|---|
| Repository | GettysburgResearch/riemann |
| Contribution | Standalone research reassessment and proposed component theorems |
| Branch | research/signed-moment-reassessment-20261013 |
| Frozen mathematical commit | 3968d1b7135900e6130412f58a39bc67e73d4ecb |
| Frozen tree | 1e71c308a95c616069c29fd20d87907cc5795e1a |
| Parent | 97bf40329489992e9384c34d7595af6d01a40774 |
| Stacked base | PR #929, research/sextic-conductor-averages-20261010 |

[MANIFEST.json](MANIFEST.json) binds all 13 files changed in the
mathematical commit, including the five proof/reassessment notes,
five content reviews, the source lock and the two navigation files.
The later publication commit adds only this validation record, the
manifest and exact-source receipts. It changes no frozen source byte.
The final branch head is recorded by the pull request, without a
self-referential hash inside its own commit.

## Claims and independent reconstruction

| Claim | Mathematical file | Review and exact-source binding |
|---|---|---|
| The full native unfiltered CT1 is false at every fixed order | [Signed trace obstruction](SIGNED_TRACE_OBSTRUCTION.md) | [Historical-agent reconstruction](SIGNED_TRACE_INDEPENDENT_REVIEW.md), [root reconstruction](ROOT_CONTENT_REVIEW.md), [root source receipt](ROOT_SOURCE_RECEIPT.md) |
| The moving contour has the stated uniform factor window and sharp factor-only thresholds | [Moving contour](MOVING_CONTOUR_WINDOW.md) | [Historical-agent reconstruction](MOVING_CONTOUR_INDEPENDENT_REVIEW.md), root reconstruction and source receipt |
| The fixed causal weighted-variation orbit has at most two/four Kummer classes and \(O(H^{1/6})\) rows | [Causal and determinant note](CAUSAL_ORBITS_AND_DENSE_LIFTS.md) | [Fresh independent reconstruction](CAUSAL_HAAR_INDEPENDENT_REVIEW.md), [second scoped review](CAUSAL_HAAR_SECOND_REVIEW.md), [independent source receipt](CAUSAL_HAAR_SOURCE_RECEIPT.md) |
| Every fixed Gaussian Haar moment has square-root scale when the representation has no invariant vector; otherwise the hierarchy is equivalent to target zero exclusion | Causal and determinant note | Fresh independent reconstruction and source receipt; the second review discloses its converse contributions |
| The sufficient hierarchy extends to every compact smooth norm test, with a converse for the entire test class | [Compact-test supplement](COMPACT_TEST_HAAR_MOMENTS.md) | Fresh independent reconstruction and source receipt |
| The compact-test physical moment has an exact open-discrepancy reformulation using the proved Haar benchmark | Compact-test supplement | Fresh independent reconstruction and source receipt |
| The older sources leave the identified observables unpaid; the finite norm-box repair follows from PR #916 | [Historical connections](HISTORICAL_CONNECTIONS.md), HC1--HC6 | Root reconstruction and source receipt |

The fresh causal/Haar reviewer did not author the two proof notes or
contribute to their construction. Root and the signed-family agent
helped develop the all-order converse; their roles are disclosed.
The content reviews preceded the frozen commit, and the later receipts
authenticate the exact committed bytes carrying those reconstructions.
No content verdict is silently extended to a later changed proof.

## Exact sources and what was checked

[SOURCE_LOCK.json](SOURCE_LOCK.json) pins 25 repository inputs by
commit, path, git blob, SHA-256 and bytes. They include the exact PR
#911 CT1/SC4 interface, PR #916's prior collision convolution and norm
frontier, the fixed-character and Gaussian adapters, and the specific
earlier route comparisons. All 25 identities were checked against
their git objects. The root and fresh reviews distinguish full
load-bearing reconstruction from scoped inspection of historical
claims.

The three external entries identify classical inputs from the
prime-ideal theorem and class field theory. Their cited statements
were read in author-hosted or original primary sources. No
critical-strip zero exclusion is assumed for the trace theorem.
No content hash or proof-assistant replay of those external PDFs is
claimed.

The actual verification comprised:

- Independent analytic reconstruction of the stated new component
  arguments, including the full native trace and all-order mixed
  moments.
- Exact integer/rational checks of the sextic determinant polynomial
  through element orders and exterior-power invariant counting.
  The finite mixed-moment coefficient check illustrates an algebraic
  identity; the all-order proof uses the identity itself.
- Source/blob/hash/length checks for the 25 pinned inputs and all 13
  frozen changed files.
- A staged whitespace check and balanced Markdown math delimiters.
- Equality of the API-created GitHub tree and the local staged tree,
  followed by fetching the actual source commit and checking its
  parent, tree and unchanged resident sources.

There is no native finite-row experiment, numerical asymptotic fit,
zero census, test suite, Lean build, or replay of an imported
quasi-Riemann result. These are mathematical proof notes; source
authentication is not substituted for their analytic arguments.

## Smallest statements carrying the new conclusions

For the **trace refutation**, the delicate chain is the exact
two-slot factorization with all row masks, a polynomial nonzero
anchor from the native prime-square coefficient jump, and the
weighted half-plane reduction from each higher order. A factor
lower bound by itself would not prove the complete signed-trace
claim. The reviews explicitly reconstruct this chain.

For the **moving window**, uniformity of the weighted prime sum as
the contour varies is essential. The converse concerns the factor
alone. Its stated positive short-polynomial premise is an open
arithmetic assumption, never an unconditional conclusion.

For the **causal classification**, the discrete measure is forced by
Mellin uniqueness among all finite weighted-variation measures, and
the obstructing coefficients must be grouped by rational norm.
Induced-character equality leaves field conjugation as an
alternative. Omitting it would make the classification false.

For the **Haar hierarchy**, the central estimate is convergence in
every fixed \(L^{2k}\) of the product of locally mean-normalized
determinants. Centering cancels the degree-one mixed terms.
The reciprocal target factor has polynomial vertical growth only
under the stated zero-exclusion assumption when invariant vectors
are present. No raw finite-product convergence below one is used
to evade that assumption.

For the **compact converse**, the premise covers every fixed test.
A chosen nonnegative log-bump detects a hypothetical zero without
requiring any constant uniform across the test class. There is no
claimed converse for a single arbitrary compact test.

For the **finite repair**, coefficient projection must preserve the
entire physically tested convolution. Its polynomial collision cost
does not bound the remaining row trace or a new incidence sum.

## Remaining arithmetic obligation

The independent model's norm-test hierarchy is proved at each fixed
order. An estimate for the actual short row measure is still needed.
For the original family, the compact-test supplement defines an exact
discrepancy \(\Delta_{2k}(D,H;W)\). The bound

\[
|\Delta_{2k}(D,H;W)|\ll_{\epsilon,k,W,\nu,S,\Phi}
H D^{k+\epsilon}
\]

at the required physical height remains open. So does the prior
complete rectangular hierarchy with sublinear height and defect
costs. Neither the model theorem, the causal obstruction, nor the
moving-contour repair supplies this missing cancellation.

The physical generalized moment and RH remain open. This draft
publication changes no integrated status, old proof or main-branch
result. All review here is by AI agents, with no assertion of human
peer review or formal certification.
