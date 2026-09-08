# Post-integration synthesis and the attempted full proof

Status: research assessment plus new component theorems; NOT an independent audit
or a full unconditional RH proof. Freeze: main f99d9e3908dde4865377c75d9ca051c1f545bf4f.
The scientific integration reference is PR #800; later documentation releases do
not count as acceptance of live research. No source branch is modified.

## 1. What changed after integration

The live #827 pass-one review inventory records 42 identified packets, twelve
substantively paper-reviewed and thirty pending. This pass uses that inventory
as a discovery aid, not as an acceptance verdict or a substitute for proof.
It is a SELECTED synthesis of the analytic/native-source and divisor fronts,
not a re-review of all 42 packets or the branch-only L-object classification.

Three groups now have unusually precise interfaces.

**Finite source certification.** #803's newest rational residual-capture proof
represents the complete infinite residual norm by a finite rational quadratic
form with a relative error uniform over every coefficient. The period-mean term
V/H survives; optimization cannot evade the tail by choosing large coefficients.
The balancing, derivative-jet and prefix classes remain different. Its all-rank
capture theorem prices a finite minimum but does not make that minimum small.
The current proof and current PR metadata were read in this pass.

**Critical-domain constructions.** #804/#805 and #812/#814/#817 construct actual
causal or integer sources, pay horizons and tails, and separate finite stability
from convergence toward an intrinsic floor. #819 identifies that floor with the
classical BSY logarithmic defect, not a new evaluated constant. #823 proves why
finite-horizon/finite-jet closeness and positive-source perturbation arguments
cannot establish exact vanishing. These predecessors are inherited research
context, not newly kernel-checked or numerically replayed here. Current #805
metadata was reread; the earlier supplied manuscripts remain the content source
for the longer lineage. No unpublished agent continuation is a dependency.

**Prime error and arithmetic graph.** #811 has a complete physical discrepancy
square and source-bound zero detection. #818 pays all local square-cell detail
unconditionally with Brun--Titchmarsh; its cumulative cell levels remain open.
#825 and #826 prove complementary bounds for the complete prime-power graph,
with explicit inverses modulo the harmonic mode. #825 gives O(log log P) cost
independent of exponent depth; #826 supplies a direct decoder, a depth-dependent
alternative, and full rectangular spectra. Their full graph proofs were read;
current #811/#818 descriptions were reread with their conditional inputs intact.
No prime-error numerical campaign or predecessor checker was rerun.

## 2. The most tempting composition, tested rather than asserted

The tempting chain was

    square-cell detail is summable
    + divisor fluctuations have a quantitative inverse
    + finite causal corrections converge with an explicit rate
    -> the whole critical source has subpower norm
    -> RH.

That third arrow is not justified. These are different decompositions. The
square-cell theorem retains cumulative levels; the divisor graph retains a
whole Hilbert-valued coherent mode; the causal theorem converges to the possibly
nonzero source-domain floor. A small estimate on one complement cannot pay a
mean from another space without a source-exact adapter.

COHERENT_SOURCE.md supplies such an adapter for a very simple literal Mobius
filter. It proves that the FULL native norm is exactly the harmonic projection
that the graph annihilates. The same field's complete prime-power edge energy
is c_sf N log N+O(N), by an unconditional squarefree calculation. The graph
bound points the wrong way for an upper bound on the native coherent norm.
This is not merely a synthetic objection; both statements concern the actual
same Mobius vertex field. Synthetic additions to its coherent mode are used
only to show why a universal graph-only estimate cannot fill that gap.

## 3. New positive theorem and sharpness

PROOF.md solves the optimal ANCHORED inverse problem on every finite squarefree
prime box. Its cost is the largest eigenvalue of a diagonal-plus-rank-one matrix
and the unique root of one monotone scalar equation, with all normalization
factors fixed. The complete root Green function is a finite subset sum or an
integral of a positive finite Euler product.

As all primes <=P enter, the optimal anchored constant is

    (6/pi^2)log log P+O(1),

while the centered Poincare constant on the very same boxes is exactly
2/(3log2). Therefore #825's log-log anchored order is sharp on its stated
all-support class. It is not a reason to declare the centered graph inverse
uniformly ill-conditioned, and it is not a disproof of a constant centered
gap on other support classes. This resolves a concrete ambiguity in how the
two new spectral-gap papers can be used.

The proof reconstructs all required graph, squarefree, Euler-mass and
rank-one identities. Classical finite-product, Green-function and Poincare
methods are credited. No external novelty or priority assertion is made.

## 4. The end-to-end route I retain

For a fixed, completely specified filter the native norm is

    J_N=sum_(k<N)M(k)^2/[k(k+1)]+M(N)^2/N,
    M(k)=sum_(n<=k)mu(n).

It is positive, rational, and computable with its full stopped-input future.
Convolution with the UNCHANGED factorial source gives legitimate outputs
matching a fixed target through log(N+1). A hypothetical off-line zero forces
J_N to grow at a fixed positive power at EVERY sufficiently large cutoff.
Thus one unbounded subpower subsequence would give an unconditional RH proof.
All steps of that implication are supplied in COHERENT_SOURCE.md, with no
inner-factor completeness premise. The subpower upper bound is OPEN.

The most direct sufficient one-sided estimate is now explicitly the signed work

    2sum_(n<=N) mu(n) M(n-1)/n <= C_epsilon N^epsilon
    for every epsilon>0 and all sufficiently large N.

This is classical-scale Mobius cancellation in a source-exact coordinate, not
a theorem newly made easy by writing it here. The diagonal costs only O(log N).
No bound on that work at the required scale was obtained in this attempt.
Absolute values, local block resets and a random-prime surrogate do not prove it.

The alternative prime-side route remains the all-scale coarse energy in #818,
which avoids reciprocal-zeta inverse derivatives but retains an unproved
cumulative prime estimate. The full Weil route remains viable only after its
coherent/mean Schur operator is explicitly controlled. These are alternatives,
not accepted implications between different unbound source fields.

## 5. Precise review priorities

Review CCS1's normalization at the root and rank-one secular equation; CCS2's
coefficient 1/zeta(2) and both halves of its O(1) remainder; CCS3's full
prime-power diagonal and the zero higher-power mixed terms; and the actual
coherent projection and delayed Laplace estimate. These are the proposed new
proofs. Reviewers are not asked to invent the signed-work upper estimate or
accept an RH proof with that estimate omitted.

The packet does not depend on the proposed HC26 Sobolev/capture rate, the
numerical intrinsic-entropy bound, or a general prime-graph-to-Weil sign map.
It does not change any integration verdict. No entire-repository completeness,
source permission, formal build, independent peer acceptance or public-launch
clearance is claimed by this research pass.

## Sources and attribution

- Frozen repository sources and inspection depths: SOURCE_LOCK.json.
- Andrew Beveridge, A Hitting Time Formula for the Discrete Green's Function,
  arXiv:1505.06989 (2015), published CPC 25 (2016), 362-379. General Green/
  inverse/hitting-time background only; this proof derives its own formula.
  https://arxiv.org/abs/1505.06989
- Alexei Kulik, Poincare inequality and exponential integrability of the hitting
  times of a Markov process, arXiv:1303.1257. General distinction between a
  spectral gap and hitting a set; no external constants imported here.
  https://arxiv.org/abs/1303.1257
- NIST DLMF 27.4 and 27.5: absolute Euler products, Dirichlet convolution,
  Mobius inversion. The needed finite identities and squarefree estimate are
  proved explicitly. https://dlmf.nist.gov/27.4 ; https://dlmf.nist.gov/27.5
- The optional RH-to-Mertens converse is the classical Littlewood implication,
  as separately recorded in the source-domain predecessors. It is never an
  unconditional input to a new inequality. No probability model for mu is used.
