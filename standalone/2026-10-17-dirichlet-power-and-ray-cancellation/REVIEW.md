# Mathematical review record and remaining obligations

This is a proposed research component. The written arguments were reviewed
by parallel mathematical agents within this session and by the coordinating
agent. Those reviews are separate passes over the mathematics, not external
peer review, proof-assistant certification, or acceptance by the repository.
Finite checker success has the narrower meaning in VALIDATION.md.

## Direct Fourier and analytic adapter

Two other mathematical agents read DIRECT_FOURIER.md in full. The author
of STRIP_AND_MAJOR_ARCS.md and a separate sources reviewer checked the
fixed reciprocal product, the finite inverse identity, the Type I/II
split, and the exponent budget. The coordinating agent separately read
the entire analytic adapter and direct proof. No unresolved structural
gap was identified in those passes at the written ZF(theta) scope.

The review explicitly checked:

- ZF(theta) quantifies over every primitive Dirichlet conductor and every
  height; fixed-character nonvanishing would not give the uniform major
  arcs required here.
- Reciprocal bounds retain the principal pole normalization and every
  imprimitive Euler factor. The oscillatory Mellin kernel has a square-root
  frequency cost; replacing that by a full derivative cost loses the result.
- The sharp Perron error is integrated near the integer endpoints. It is
  not falsely asserted to be uniformly small at every integration point.
- The cofactor is the entire q-supported part (n,q^infinity), with all
  powers through the fixed convolution order. Character orthogonality
  retains zero extensions and the reduced rational phase.
- E^J has support starting at (U+1)^J. The identity uses strict absence
  below that endpoint, not absence at the first possible nonzero term.
- Type I's dyadic interval can contain q' even when its lower scale M is
  less than q'. The final proof treats the actual upper endpoint and the
  O(1+M/q') exceptional multiples. This corrected an imprecise intermediate
  formulation; the bound and claimed exponent are unchanged.
- The inverse identity is applied on the outer interval (x/2,x]. Thus
  every contributing dyadic box has total product comparable to x; no
  small-product box is forced into a bound whose hypotheses it lacks.
- Type II keeps the product cutoff by half-integer Perron inversion,
  without assuming smoothness of the arbitrary divisor-bounded coefficients.

The common 7/8 theorem remains an imported recent-paper input. Reading
its exact statement does not certify its deep proof. The abstract deduction
from ZF(theta), 2/3<=theta<1, is the mathematical claim proved in this
packet; its 15/16 numerical application has that explicit dependency.
The rational Mobius theorem and method are credited to Baker--Harman.

## Completion and endpoint-maximal covariances

The coordinating agent read COMPLETION_AND_COVARIANCE.md in full, including
the original local factors, the exact cap owner rule, and the maximal step.
The proof keeps every original ideal-prime exclusion and each column cap
before applying cancellation. Different split-prime exclusions are allowed
here, without identifying conjugate prime ideals.

An intermediate square-mass statement was made more precise during review.
Absolute correction-kernel mass at every sigma>1/2 alone does not justify
the claimed polylogarithmic square-prefix estimate at sigma=1/2. The final
proof instead establishes the sufficient X^(1+epsilon) estimate directly
by Minkowski and the truncated critical kernel mass. It then allocates this
small loss explicitly in the maximal covariance bound. The endpoint
partition isolates heavy atoms, so no unsupported small-bin assumption or
extra J/H term is used.

The resulting exponent is 1-1/(16k) for each fixed k at theta=7/8.
Its linear-phase range, growing-shift threshold, fixed conductors, fixed
order, and uniformity over scales/degrees/profiles are written separately.
No fixed-shift Chowla estimate or polynomial-phase power estimate follows.

## Native angular rays, full tails, and obstruction

The sources reviewer read the full main ray theorem and its Gaussian energy
extension. The coordinating agent separately checked the main argument,
positive control, and the complete moving-angular obstruction. The review
covered the rational-content bijection, ideal Mobius signs, the masked
periodic character sum, the summable cofactor weight, and the positive
density of primitive squarefree cores.

It also checked that equality of angular values means equality of the
primitive rational ray, that the determinant separation applies modulo
the six units, and that the Gaussian Schur argument includes every angular
integer. For the noncompact norm weight the polarized estimate is summed
over all pairs of dyadic bands. The small-scale integral and the Gaussian
diagonal's lower order have separate proofs. Thus neither a discarded
Gaussian tail nor an omitted cross-band term is carrying the energy claim.

The obstruction uses actual native signs at the fixed radial parameter
t=0. Split-prime phase limits are compatible with a genuine integer angular
orbit. Inert signs survive, giving zeta_K^S(s)/zeta_Q^Q(2s)^2; that quotient
was checked against its local factors and elementary summatory formula.
This rules out a narrower width for the stated bound uniform in angular
centers. It says nothing of the same kind about a fixed principal center.

## What is still open

The two estimates control different objects. Additive Fourier uniformity
has exponent 15/16 at the imported input, whereas the angular theorem
controls a probability average of order log D at critical energy. The
unconditional angular argument does not inherit the Fourier theorem's
more flexible ideal exclusions, and the Fourier theorem does not remove
the angular average.

The required estimate for the fixed principal angular member remains
unproved. Positivity extracts it only after paying the inverse probability
of that member, of order the angular width. A successful next argument
must control the actual cross-ray coherence at that fixed member. No
new Dedekind zero-free boundary, stronger common Dirichlet strip, accepted
integrated lemma, or full RH proof is claimed by this packet.
