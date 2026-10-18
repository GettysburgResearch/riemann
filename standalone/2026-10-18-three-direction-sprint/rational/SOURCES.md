# Sources and exact scope

Repository source snapshots:

1. Native source #994, exact commit
   `c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
   `standalone/2026-10-18-theta20-and-native-cancellation/native/PROOF.md`.
   Read in full, together with its README, SOURCES, exploration notes and
   copied #848 source. Imported scope: the literal rational old-product
   source, native reciprocal sign crossings, complete low-denominator
   estimate and small-core resource. Its unresolved rough estimate is
   kept unresolved here.
2. All-prefix native consumer #848, exact commit
   `99101457b32b6f10f4eda88ca998048404b860ea`,
   `standalone/2026-09-12-astra-crossing-cofinal/PROOF.md`, blob
   `0f9eac82fcbca61c7887a9fb71eb29d5a4181ce9`. Read in full via #994's
   copied source. Its all-prefix exponent and cofinal crossing result are
   source-qualified imports. Our component estimates do not by themselves
   activate a new global consumer conclusion.

Repository policy/navigation read: `AGENTS.md`, `README.md`, `STATUS.md`,
`RESULTS.md`, `PROGRAMMES.md`, `CONTRIBUTING.md`, `docs/REVIEWING.md`, and
the relevant current/native portions of `RESULTS_INDEX.md`, `OPEN_CUTS.md`
and integrated current results. No inherited mathematical file was edited.

Primary classical sources checked on 2026-10-18:

* Terence Tao, *A remark on partial sums involving the Mobius function*,
  [arXiv:0908.4323](https://arxiv.org/abs/0908.4323), version 5.
  Used for the prime-semigroup uniform masked bound `|m_d(x)|<=1`.
  The elementary counting proof is reproduced in Section 2, so the
  precise needed inequality is independently visible in this proposal.
* [NIST DLMF 27.12, Asymptotic Formulas](https://dlmf.nist.gov/27.12),
  especially 27.12.4. Only the ordinary prime number theorem is used in
  the stated results: fixed relative prime intervals have their usual
  asymptotic mass, and their harmonic sums are asymptotic to a constant
  divided by log Y. No short-interval prime theorem is assumed.
* D. I. Tolev, [*On the distribution of r-tuples of squarefree numbers in
  short intervals*, arXiv:math/0505326v1](https://arxiv.org/pdf/math/0505326),
  Theorem 3, page 3 of the PDF. For the NEW global transport only, its
  r=1,l_1=0 case supplies uniform squarefree density in length
  H=Y^(1/5+eta) intervals at locations comparable with Y. Choosing
  psi(x)=(log x)^(1/2) satisfies its hypotheses eventually. The needed
  density is greater than 1/2; existence alone would not suffice.
  Both candidate factors are handled by pigeonhole using two individual
  interval counts. No theorem conditioned on parity or varying shifts
  is silently imported. Root and the Eisenstein subagent independently
  read the same primary theorem during their component audits.
* G. A. Hiary, D. Patel and A. Yang, [*An improved explicit estimate
  for zeta(1/2+it)*, arXiv:2207.02366v1]
  (https://arxiv.org/pdf/2207.02366), Theorem 1.1, PDF page 2.
  Read directly on 2026-10-18. The unconditional bound
  `|zeta(1/2+it)|<=0.618 t^(1/6)log t` for t>=3 is used ONLY in
  the new compact-flux compression. A fixed exponent theta>1/6
  absorbs its logarithm and bounded heights use continuity. This
  primary paper explicitly repairs the older Kusmin--Landau constant;
  no affected older explicit estimate is imported. We need its exponent,
  not an optimal constant or the latest possible subconvexity record.

Additional current overlap read: #1002, head
`1319373815ee408146705b25a426fba6b22ed755`,
`standalone/2026-10-18-five-route-zero-preserving-attack/NEWTON_BUDGET.md`.
Its all-Y recurrence theorem and original-source adaptive core budget
are credited explicitly in `DIAGONAL_COMPRESSION.md`. Neither supplies
the missing bound for the new balanced reference weights. Its larger
original-source core budget is not silently transferred to that source.

The initial component identities and estimates are proved in
`PROOF.md`; the later named proof files supply their own complete
arguments and explicit imports. Basic divisor inversion, Abel summation, Cauchy--Schwarz,
finite dyadic prefix decompositions and elementary operator norm series
are written to the extent needed for their use. There is no worldwide
novelty claim for these classical tools.

The later Eisenstein mixed-vector components additionally use these
primary interfaces, read directly on 2026-10-18:

* Blomer--Goldmakher--Louvel, [arXiv:1112.1650v1](https://arxiv.org/pdf/1112.1650),
  Theorem 1.3 (PDF page 4), the squarefree cubic large sieve; Lemma 2.2
  (PDF page 6), ordinary primitive GL1 Poisson. Raw nonunit zeros agree
  on the squarefree cubic indices after fixed ray subdivision.
* Goldmakher--Louvel,
  [arXiv:1112.1642v1](https://arxiv.org/pdf/1112.1642v1),
  Definition 1.1, Theorem 1.4 and Corollary 1.5 (PDF pages 1--2),
  for the squarefree quadratic ideal large sieve used in the complete
  cubic-core dual sector. The v1 numbering differs from the published
  source citation Theorem 1.1. The pinned original Eisenstein source's
  `eq:quadratic-sieve` and its family-verification paragraph provide
  the exact fixed-primary convention, primitive inducing characters
  and finite square-class subdivision; every moving mask stays in a
  bounded coefficient or positive row restriction.
* Xu--Sang, [arXiv:2610.17675v1](https://arxiv.org/html/2610.17675v1),
  Sections 3 and 5.5, for the exact explicit sextic Gauss witness and
  its unrestricted-row range. Its later squarefree-row transfer can
  change that vector; no bare-vector conclusion at the transposed
  corner is inferred from that transfer.
* [NIST DLMF 27.12.8](https://dlmf.nist.gov/27.12.E8), fixed modulus 3,
  for the prime ideal interval counts in the hyperbola coefficient
  obstruction, via rational split primes. No moving-ray or genuinely
  short prime-interval theorem is used there.

`TRANSPOSED_GAUSS_MODE.md` also explicitly imports the pinned OpenAI
source's inverse-amplification lemma, `eq:amplified-note`, at r=1.
Its flat-probe conclusion follows by direct Cauchy of the existing
individual second moments. It is not presented as a new full mixed
moment or a fresh zero-free theorem.

The decimal `0.749914...` is only the user's proposed working exponent
budget. The obstruction actually applies to every budget `a+p<2`, so
it neither depends on validating that benchmark nor imports a new external
zeta theorem. No assertion about a current best published zeta boundary
is made by this track.

New overlap read: #1003, exact head
`669b6a01f4d4858ae1ef806b07547be95c08c935`,
`standalone/2026-10-18-theta26-and-critical-family/arithmetic/`:
`NATIVE_FREQUENCY_TAIL.md` and `LOW_FREQUENCY_ATTACK.md`.
The first proves complete high-input-frequency removal for the unmasked
native polynomial; the second proves an explicit generic-coefficient
low-frequency obstruction while excluding a Mobius conclusion.
`BOURGAIN_MASKED_ADDENDUM.md` credits the first result and extends its
removal to the original fixed annular rough masks. It uses Bourgain,
[*Decoupling, exponential sums and the Riemann zeta function*,
arXiv:1408.5794v2](https://arxiv.org/pdf/1408.5794v2), Theorem 5,
PDF page 2. The primary theorem was independently read on 2026-10-18;
its exponent 13/84 also sharpens the frozen square-compression error.
No reciprocal bound or low-frequency contraction is inferred from it.

Further overlap read through the GitHub connector at immutable #1005
head `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1`:

* `standalone/2026-10-18-amplified-boundary-and-global-attacks/native/MOBIUS_CLOSURE_ATTEMPT.md`,
  Git blob `397983f2d0a97e16953640e4b42378316eedf0f3`;
* the same directory's `JOINT_NUMERATOR_CLOSURE.md`, Git blob
  `e6a8fe2fd44eb0e33e13312cb1be28f0b55d7acb`.

The first retains actual Mobius and all products in an exact sawtooth
transform, then pays the complete crossing boundary terms before leaving
the low-frequency interior quadratic norm OPEN. The second proves an
exact obstruction to improving its existing marginal moment comparison
by the stated joint-plain/intermediate-contour optimization. Both were
read and their displayed identities independently reconstructed. Neither
is imported here as a new arithmetic contraction, complete mixed mean,
or accepted new zeta boundary.

The actual adjoint normalizations in the final principal-energy notes
use [rStation paper 10/v2, Section 7](https://rstation.ai/problems/riemann_hypothesis/papers/10),
whose primitive Kubota framework remains an explicit analytic import.
Its unrestricted good numerator convention, two distinct remainder
types and original zero masks are retained. The base-section cusp
density and sixth-power periodicity are the separately pinned inputs
in `../eisenstein/RESIDUE_VALUATIONS.md`; primitive residue periodicity
at a NEW sixth-power prime is not assumed.
