# Synthesis and the attempted end-to-end proof

## 1. The current picture, not another integration verdict

The scientific reference is the September 6 integration identified by #827:
PR #800 at 4f461e5ad46e452b1eafa69eddff3b76cd0c12be. The current research branch
for this continuation is #803 at 31a35a90b0b924dc98a2c89c463fb59577f45a4e.
No main, integrator decision, or earlier manuscript is changed by this work.

The newly read #827 first-pass report identifies 39 original post-integration
packets, then three later additions, of which only twelve had substantive
paper review. Its recommendations are scoped and are not a blanket acceptance.
I used that report as orientation, not as a substitute for reading the precise
norms in #803, #818, #819, #825 and #826. Details of direct reading are recorded
in SOURCES.json. The older #804/#805/#811/#812/#814/#817/#823 lineages were
contextualized through their supplied records and the new review; this is NOT
a fresh full dependency review or a replay of their numerical campaigns.

The strongest broad distinction is now not finite versus infinite computation
alone. Several papers really have paid infinite tails or controlled growing
families. What remains is an arithmetic sign or a target-dependent upper bound
inside the exact original norm. The following objects must stay separate.

| Source | Retained object at the stated proposed scope | Unpaid object |
| --- | --- | --- |
| #803 logarithmic core/local window | Operator graph core, converging two-sided Schur enclosures; a proposed whole-function length-one sign | All-length actual signs; numerical acceptance of the length-one packet remains separate |
| #803 annular/sparse-sign work | Literal prime-power scalar, pole capture, conditional feedback from any fixed failure-count power saving | The native count saving, not its implication to RH |
| #803 residual packets | Actual finite coefficient optimization, matching unknown-edge growth exponent, uniform full-tail rational enclosures | A subpower UPPER bound for growing-prefix minima |
| #804/#812/#817 | Actual causal source domain, admissible local reproduction, approximation toward the intrinsic floor | The floor itself, or growing-horizon subpower output cost |
| #818 square-grid localization | Summable all-cell local detail in the original prime discrepancy metric | Accumulated cell levels and their signed inter-cell work |
| #819 intrinsic entropy | The BSY defect J and its exact target sensitivity, retaining every inner zero | J=0; small numerical upper bounds do not give equality |
| #790/#825/#826 | Positive complete divisor form and quantitative inverse off its harmonic mode | Identification and smallness of the physical forcing, coherent channel and full source couplings |
| #823 late-tail controls | Nearby positive, finite-jet-matched sources can acquire further inner zeros | The unmodified infinite arithmetic identity cannot be replaced by those approximation properties |

The new contribution in PROOF.md answers a specific proposed bridge between
the third and seventh rows. A coefficient-uniform graph-to-residual estimate
with only subpower loss is FALSE. Its sharp fixed-ratio order is Y/log Y,
even when the relevant native-prefix constraints survive. This does not remove
the graph theorem's useful inverse or reject its correctly identified cusp
applications. The norms have different geometry.

## 2. The most direct complete implication still available

There are two honest end-to-end conditional routes worth distinguishing.

**Residual route.** Construct finite polynomials p_j preserving mu below
Y_j->infinity and p_j(1)=0, p_j'(1)=1, with E(p_j)=Y_j^o(1). For any zero
rho with beta>1/2, the delayed error transform is in H2 and has the two values

    H(rho-1/2)=Y_j^(rho-1/2)/rho, H(1/2)=0.

The complementary evaluation-kernel norm is
|rho-1|^2/[(2beta-1)|rho|^2]. Projection therefore forces

    E(p_j)>=(2beta-1)Y_j^(2beta-1)/|rho-1|^2,

a contradiction. Reflection gives RH. This implication retains the original
norm, arbitrary finite support, complete future, and hypothetical multiplicity.
ANT2 does NOT supply its premise: Y exp(-c Phi(log Y)) is Y^(1-o(1)).

**Prime-discrepancy route.** Let s_n=pi(n^2)-Li_2(n^2), where Li_2 has lower
endpoint 2, and w_n=1/n^2-1/(n+1)^2. Prove

    sum_(n>=2) w_n s_n^2 < infinity.                        (OPEN)

The #818 paper supplies a bounded invertible adapter to the complete prime
state and an unconditional summable error from replacing it by these square
samples. It then constructs an analytic exponential on Re s>1/2, identified
with (s-1)zeta(s)/s^2 first in the Euler half-plane. Hence OPEN implies RH.
The reverse implication uses a separately stated classical RH-conditional
mean-square theorem; it is not an unconditional input.

For a_n=s_(n+1)-s_n, direct finite telescoping gives

    sum_(n=2)^(M-1)w_n s_n^2+s_M^2/M^2
      =s_2^2/4+sum_(n=2)^(M-1)[2s_n a_n+a_n^2]/(n+1)^2.   (WORK)

A uniform upper bound on the right side would establish OPEN, since the left
side is nonnegative and contains all partial sums. Neither the local sieve
increment bound nor the divisor gap bounds the signed 2s_n a_n work. Dropping
it, resetting s_n, or dropping the terminal term would change the problem.

My research judgment is to prioritize an exact arithmetic decomposition of
WORK, or a native-specific residual estimate, over further refinement of a
finite solver. This is a priority judgment, not evidence that either estimate
is easier than RH or nearly settled. The new norm-transfer theorem explains
why one attractive solver/gap synthesis does not accomplish that decomposition.

## 3. What this pass does add unconditionally

ANT1 gives a fixed, bounded-coefficient, linear-support family with all three
normalizations. ANT2 propagates an existing classical Mertens estimate through
the complete original residual norm and gives E=o(Y), with every frequency
retained. ANT3--ANT5 quantify the exact loss in the attempted graph adapter,
including variations preserving ANY FIXED number of the indicated moments.
These are complete proposed component arguments, not merely an untested plan.
They do not evaluate an unknown zero boundary or infer an infinite theorem
from the finite profile certificate.

## 4. Questions for independent reviewers

Check especially:

- ANT1's three equations, disjoint coefficient blocks, and distinction between
  coefficient energy and physical energy.
- ANT2's complete infinite moment tails, its (1+|t|) factor, and the complete
  low/high frequency split. The imported Mertens and convexity bounds are
  unconditional; their numerical producers are not replayed.
- ANT3's coordinates c_n versus c_n/sqrt(n), all prime powers, and the fact that
  every vertex below Y remains present with coefficient zero. Deleting those
  graph vertices would invalidate the lower diagonal argument.
- ANT4's three zero moments and the native-prefix parallelogram comparison.
  Its negative conclusion is about a UNIFORM norm adapter, not the minimum or RH.
- ANT5's scaled Riemann sums and the full tail in the constant certificate.
  The computed constant concerns a variation profile, not actual zeta data.

No proof step has been left for a reviewer to invent under the heading of a
complete RH proposal. The two OPEN premises above are intentionally unresolved.
