# Independent review of marked holonomy response

Reviewed commit: `e7fc8b0af2c42ce43384543972df2ed44f343300`.

Review object: the six files introduced under
`research/exploratory/marked-holonomy-response/` at this commit, including
its local checkout attributes. The working files inspected were confirmed
to have no diff from this frozen commit.

Verdict: no mathematical or implementation blocker found for the stated
based-representation and marked-automaton model. The source enrichment is
explicit, and the result does not claim descent to the earlier unmarked
graph problem or an arithmetic realization.

## Evidence boundary

I independently read the complete proof and implementation, its primitive
source contract and all nine tests, and reconstructed the return-operator,
trace, determinant, gauge, and cycle arguments. I did not execute a test,
producer, linter, or numerical job. The implementation agent reports Ruff,
producer `--write`, ordinary and optimized `--check`, and nine tests in each
mode passing, with proof-object digest
`bf2d2af9fae943db5e538ca02885d871eddec9d53548cebf256d4093d4ca52b6`.
These are reported execution results, not independent executions by this
reviewer.

## Source and mathematical audit

The parent data precede the spectrum: a representation of the free group on
a,b, its declared element c=(ab)^(-1), and the two marked three-edge cycle
automata cab and cba. The time grading counts automaton edges. It is not
reduced group-word length; cab reduces to the identity without losing its
three-edge clock. This distinction is essential and is stated prominently.

For unitary U,V, the return operators are I and K=(UV)*(VU). The cube of
each transfer matrix is block diagonal, with cyclically rotated products
as its diagonal blocks. Invertible labels make these products similar.
Consequently only powers divisible by three have nonzero trace, and those
traces are 3d and 3 tr(K^r). The trace-log identity gives exactly

`det(I-tT0)=(1-t^3)^d` and `det(I-tT1)=det(I-t^3 K)`.

The primitive-cycle Euler interpretation uses the same automata, rather
than a separately fitted determinant. Since K is unitary, the indicated
formal trace series also converges for |t|<1.

For A=UV and B=VU, the identity
`||A-B||_F^2=2d-2 Re tr(A*B)` gives the stated real third-trace gap.
It vanishes exactly when U and V commute. Equality of the determinants
forces equality of their t^3 coefficients and hence the same vanishing
condition; conversely commuting labels give K=I. Therefore determinant
equality for this pair is equivalent to abelian image of the two-generator
representation. Quantifying over all pairs in a subgroup gives precisely
the stated abelian-subgroup criterion.

Every one-dimensional character gives the same word holonomy for cab and
cba. Higher-dimensional unitary representations of the abelianization
split into commuting characters and remain blind. The noncommuting
examples therefore distinguish information absent from all those scalar
word observations. This does not say that the group marking or the words
themselves can be reconstructed from scalar observations.

The sharp finite controls are correct. For the transpositions (12),(23), K
is a three-cycle, giving (1-t^3)^3 versus 1-t^9 and trace gap nine. The
lifted automata consist of three three-cycles versus one nine-cycle.
Permutation degrees one and two are blind. The two-dimensional orthogonal
anticommuting example gives K=-I, determinant pair (1-t^3)^2 and
(1+t^3)^2, and gap twelve. Matrix-label dimension and permutation degree
remain separate statements.

## Gauge boundary

Simultaneously conjugating the based representation conjugates both
transfer matrices and K, so the observables are well-defined on
Hom(F,U(d))/U(d). After the transfer matrices have been constructed, each
can also be changed by independent vertex-fibre bases without changing
its determinant or trace. The tests exercise both forms of covariance.

This resolves the earlier limitation by adding a based representation and
a prescribed comparison of words to the source. It does not retroactively
make the previous operation on an unmarked cover gauge invariant. The
common holonomy source cannot be discarded while its numerical labels are
reused as if they were intrinsic to either unmarked cover. The manuscript
states this distinction correctly.

## Implementation and adversarial checks

- Current matrix-library bytes are checked against the compiled normalized
  hash before module execution. Full payload production additionally reads
  the library from the exact original commit
  `26314df4e5ed9a5c16b7da61e155a48d325789cc` and verifies its content.
  Corrupted working library data are an explicit refusal control.
- The return word is formed by matrix multiplication from the primitive
  word contract. A separate block construction checks complete transfer
  determinants through dimension six. Direct Leibniz expansion and Newton
  reconstruction provide different determinant paths.
- Literal lifted permutation graphs are traversed using a sparse successor
  map on at most twelve vertices. Their cycle lengths are checked against
  three times the return-permutation lengths. This tests the proposed
  return-cycle interpretation without an unnecessary nine- or twelve-
  dimensional Leibniz expansion.
- The complete pair census in degrees one, two, and three, the three
  unchanged degree-four controls, and the orthogonal full-transfer example
  exercise blind and distinguishing cases. These finite controls do not
  certify the all-dimensional theorem; its proof is separate.
- Exact rational orthogonality, permutation rows and columns, dimensions,
  total cycle degree, and Boolean word-choice parameters are checked.
  Nonunitary, floating-point, Boolean-entry, invalid-permutation, oversized,
  and altered primitive-source cases are refused.
- The gauge tests use a rational orthogonal conjugating matrix and distinct
  vertex gauges, rather than testing only one scalar basis change.
- Full recomputation is required for fixture acceptance. A matching internal
  payload checksum alone is insufficient. Production checks use exceptions,
  not Python assertions. The local attributes retain the canonical fixture's
  LF checkout convention.

No concrete implementation defect was identified by inspection. The exact
Git commit above remains the review identity; changing code and regenerating
its internal hashes does not preserve this review.

## Contribution and remaining burden

Based holonomy, character observables, Wilson loops, and matrix-weighted
graph zetas are classical. The cited
[Matsuura--Ohta paper](https://arxiv.org/abs/2208.14032) is an appropriate
primary baseline for that setting, without importing its different
Bartholdi conventions or large-N claims. No external priority is established
for the present elementary combination.

The repository contribution is a small, explicit source enrichment that
makes the comparison invariant under its declared equivalences, with exact
trace, determinant, Euler, positivity, and sparse-cover checks. To use it
arithmetically still requires a source-defined map into this based holonomy
object that preserves a specified native observable. The packet supplies
no such map, no gamma factor, functional equation, purity statement,
arithmetic estimate, new L-function, or RH/GRH consequence.
