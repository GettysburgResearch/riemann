# Independent review of fixed-label cycle response

Reviewed commit: `26314df4e5ed9a5c16b7da61e155a48d325789cc`.

Review object: the six files introduced under
`research/exploratory/fixed-label-cycle-response/` at that commit. This report
is outside the implementation worktree and does not change the frozen packet.

Reviewer role: independent mathematical and adversarial source inspection.
Verdict: no mathematical or implementation blocker found for the explicitly
fixed-label, finite directed graph claims. One minor front-door wording
precision remains below. External novelty and arithmetic transfer are not
certified.

## Inspection and evidence boundary

I read the frozen `MATHEMATICS.md`, `cycle_response.py`,
`tests/test_cycle_response.py`, `source.json`, and `README.md`, and inspected
the generation and full-recomputation acceptance path for `verification.json`.
I did not independently rerun a producer, test, linter, or numerical job in
this review; the session is serializing computation to limit concurrent RAM
use. The implementation agent reported producer `--write`, `--check`, and
optimized `-O --check`, all 18 tests in normal and optimized modes, and Ruff
passing at this freeze. Those execution results are reported evidence, not
independent executions by this reviewer.

The JSON's source hashes are an internal consistency record. This review is
bound to the exact Git commit above; recomputing internal hashes after changing
both sources and outputs does not preserve that review identity.

## Mathematical checks

1. The directed-cycle convention is coherent: loops, immediate returns, and
   parallel edges are allowed, while cyclic words are identified under rotation
   and not reversal. The trace-log and primitive-cycle proof therefore belongs
   to the directed adjacency determinant setting. It is not silently importing
   the undirected nonbacktracking Ihara convention.
2. Simultaneous transposition preserves the entire commuting multivariable
   determinant. Pairwise commuting complex labels, including nonsemisimple
   labels, give equal lifted determinants by simultaneous triangularization.
   This is an edge-label assertion, not an assertion about all covers with an
   abelian based-loop group.
3. The two-vertex source has the declared colored non-isomorphism and common
   determinant `1-zt-xy t^2`. The block Schur complements give
   `det(I-tW-t^2 UV)` and `det(I-tW-t^2 VU)`, without assuming invertible U, V,
   or W. The third-trace difference is `3 tr(WUV-WVU)`; the first two traces
   coincide.
4. With unitary U,V and W=(UV)*, K=(UV)*(VU) gives the difference
   `3(d-tr K)`. Taking real parts yields exactly
   `(3/2)||UV-VU||_F^2`. Its vanishing criterion and the all-label-triples
   subgroup criterion follow as stated. The complex trace itself need not be
   a nonnegative real number; the theorem correctly uses its real part.
5. The three-sheet permutation example, both characteristic polynomials, the
   common principal factor, both standard factors, and the orthogonal
   dimension-two example agree with the symbolic block calculation. All
   permutations of degree at most two commute, so the claimed minimal
   permutation degree is sharp for this pair. This is distinct from the
   dimension threshold for general unitary labels.
6. The two-source contradiction proves the stated no-descent theorem for a
   function of the commuting determinant alone, without hidden continuity or
   linearity hypotheses. It makes no claim about restricted source classes
   omitting one member of the pair, richer path data, or all-cover inverse
   problems.
7. The natural transpose duality is correctly separated from the held-fixed
   label operation. For complex unitary labels, inverse labels give the
   conjugated-coefficient determinant; exact equality with the original
   determinant is not asserted in general.

## Corrected finding and remaining wording nit

An earlier draft said that independent vertexwise gauge changes can destroy
the alignment W=(UV)*. That was false: with unitary vertex gauges,
U'=G0*UG1, V'=G1*VG0, W'=G0*WG0 still satisfy the alignment. The frozen
manuscript now states this correctly and identifies the actual limitation:
the fixed numerical identification used for the reversed-source comparison
changes under these gauges.

The new executable gauge control is materially useful. Taking G0=I and
G1=U* produces U'=I and V'=UV, preserves W and the original lifted
determinant, and changes the fixed-label response from 9 to 0. This rules out
reading the proposed response as an invariant of the underlying unmarked
cover or of arbitrary vertexwise gauge equivalence. It does not invalidate
the explicitly marked operation that is proved here.

The README currently says the first distinguishing trace is an exact
nonnegative commutator energy. For general complex unitary labels, replace
this with: "the real part of the first trace difference is an exact
nonnegative commutator energy." The theorem and proof already have this
precision. This is a front-door wording repair, not a missing proof.

## Adversarial implementation inspection

- The source-edge incidence constructor is separate from the hard-coded block
  constructor, and the payload checks their equality for both orientations.
- Leibniz determinant expansion is checked against Newton reconstruction from
  independently multiplied traces. Closed-walk counts use an edge-list dynamic
  program, while primitive cycles use literal edge-word enumeration. The latter
  preserves distinct parallel-edge identities; its rotation and repetition
  tests implement the manuscript's convention.
- Euler coefficients are checked against the reciprocal determinant series,
  and rooted walk counts against primitive-period counts. These checks are
  structurally different enough to detect several plausible orientation,
  multiplicity, and primitive-cycle bookkeeping errors.
- All nine label triples in S1 and S2 are checked, rather than only aligned
  triples. The S3 witness, 36 aligned S3 pairs, three declared S4 controls,
  rational orthogonal controls, nonsemisimple commuting labels, simultaneous
  transpose, wrong alignment, and the gauge control cover distinct boundaries.
- The S4 pairs are a declared model-development holdout, not an independently
  blinded experiment or evidence for the universal theorem. The universal
  quantifiers depend on the prose proof.
- Exact rational entry/type checks reject floats, complex entries, and booleans
  in the finite replay. Dimensions, trace lengths, determinant enumeration,
  primitive-cycle lengths, and recursive visits are bounded. Acceptance uses
  explicit exceptions rather than Python `assert`, so optimized execution
  does not remove production acceptance checks.
- `--check` recomputes the complete payload and compares exact rendered bytes.
  Primitive source mutation is rejected before derived output is accepted.
  No numerical eigenvalue fit, zero search, or large parameter scan occurs.

No concrete implementation defect was identified by this inspection. This
does not turn finite fixtures into a proof of the all-size or complex-unitary
statements.

## Contribution and unresolved boundaries

The directed-cycle determinant identity, graph covers, matrix edge weights,
and the loss of information under commuting specialization are established
mathematical themes. The manuscript gives self-contained proofs of the
identities it uses and names primary literature without claiming unread
publisher material as a load-bearing verification.

The defensible repository contribution is the explicit source-defined pair,
the universal commutator-energy separator for its declared operation, sharp
finite thresholds, and an exact no-descent statement accompanied by genuine
duality and gauge controls. This review does not establish that the combination
is externally novel. It also supplies no arithmetic source binding, canonical
arithmetic twist functor, analytic continuation, functional equation,
positive arithmetic operator, new L-function, or RH/GRH implication.

The fixed-label qualification must remain visible when this packet is linked
from programmes #763 and #764. Removing it would change the theorem being
reviewed.
