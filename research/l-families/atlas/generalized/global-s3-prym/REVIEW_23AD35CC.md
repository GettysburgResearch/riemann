# Independent review: global S3 elliptic and ramified Prym source

Reviewed commit: `23ad35cc8010f72cf1df54f09eccb4dcba108879`.
Reviewer: independent `recent_landscape` agent, 2026-08-31.
Scope: the seven-file `research/l-families/atlas/generalized/global-s3-prym/`
packet at that commit. Any later closed-point Euler replay is outside this review.

Conclusion: no blocking mathematical or executable-replay defect remains in
the stated characteristic-greater-than-three function-field scope. The finite
pushforward and inertia-invariant identifications support the asserted elliptic
and degree-four Prym factors, including the ramified places. The packet is an
explicit classical-source adapter and limitation theorem; it does not prove
number-field RH or transfer positivity to global Frobenius weights.

## Evidence and execution boundary

I independently read the complete mathematical draft, source, producer and tests,
then read the full frozen proof and the frozen hardening changes from Git.
The normalized proof hash in the frozen binding is
`966ce26a41caf4a99d36d807a290726ccdc812e6353d202a53b830c9119efa04`.
The primitive artifact hash is
`ef71c4c1cea44ef62bb93c612adea8443cf1b432b56e3acefc4b2da98e456af8`.

The root reports successful Ruff, complete producer replay in ordinary and
optimized Python, and 16 ordinary plus 16 optimized tests. I did not execute
those jobs independently. Root serialized computation to respect the shared
machine's memory budget. My independent work was source/proof/code inspection,
direct reconstruction of the formulas, and primary-reference verification.

## Load-bearing source and ramification audit

The source equations are fixed before counts or eigenvalues. The map
`E -> P1_t`, `t=y`, has degree three, and the curve is geometrically connected.
For nonzero A and nonsingular discriminant, its quartic branch polynomial has
four distinct finite roots. Each has transposition inertia; the pole at infinity
has index three. Transitivity and a transposition force geometric S3, and hence
arithmetic S3 in the same degree-three action.

Finite pushforward from the smooth normal source has geometric stalks indexed
by the distinct geometric points of the fibre, equivalently by inertia orbits
in the generic fibre. The generic augmentation projector `I-J/3` commutes with
monodromy and hence acts on each invariant stalk. This gives the decomposition
`f_* Q_l = Q_l direct_sum j_*W` on the complete base, not just the unramified open.

At a finite branch point, the formula `r=3(t^2-B)/(2A)` for the double root and
the simple root `-2r` are correct; both are rational over the residue field.
Thus the standard invariant line has Frobenius eigenvalue +1. Its local factor
is `(1-T^deg(v))^-1`. At infinity the standard invariant space is zero.
The invariant dimensions and conductor degree six follow directly from tame
inertia. The unramified three cycle-type factors have the correct signs.

The frozen text correctly distinguishes two traces at a ramified fibre. The
generic unit/trace splitting weights the inertia orbits by their sizes; the
trace of Frobenius on the pushforward stalk counts distinct fixed points.
Confusing these would invalidate the projector extension, and the explicit
test on vectors `(a,a,b)` checks this distinction.

The finite-pushforward cohomology decomposition identifies the augmentation
H1 with H1(E), while its H0 and H2 vanish. Consequently the Euler product is
`Z(E)/Z(P1)=P_E`, and its degree two is a geometric statement, not a fitted
recurrence from point counts.

For the double cover `C -> E`, `y=w^2`, the three simple zeros of y and its
odd-order pole give precisely four branch points. The cover is connected and
Riemann--Hurwitz gives genus three. On the common open, the degree-six
permutation system splits as `1 + W + chi_t + W tensor chi_t`. Taking inertia
invariants extends this decomposition to the full finite pushforward. The
quadratic Kummer summand has L-factor one because its covering curve and base
are both P1.

It follows that the twisted standard L-factor is `Z(C)/Z(E)`. The involution
splits H1(C) into the pullback of H1(E) and its four-dimensional anti-invariant
part. This proves that the quotient is a degree-four polynomial before any
computed polynomial division. The integer-coefficient claim then also follows
from the formal quotient of integral curve polynomials with constant term one.

The twist is genuinely ramified: zero has inertia -I and no invariant vector;
each old finite branch retains one invariant line with Frobenius eigenvalue
`chi_(k(v))(t_v)`; infinity has eigenvalues `-zeta_3,-zeta_3^2` and no invariants.
Thus the total conductor degree is eight. The old branch signs must be taken
over the residue field; the proof and replay both do so.

## Positivity, duality and deformation boundaries

For two distinct transpositions the commutator is a three-cycle, and
`H=I-(k+k^-1)/2=(3/2)(I-J/3)`. It is central in the S3 permutation action and
extends across branch stalks. The actual idempotent is `(2/3)H`, not H itself.
Its real positive-semidefinite interpretation is kept distinct from Q_l
coefficient theory.

The cup product, not finite-fibre positivity, gives the reciprocal pairing.
Its restriction to the anti-invariant H1 summand is nondegenerate because the
plus and minus summands are orthogonal. This gives the displayed reciprocal
degree-four polynomial. The absolute-value statements use the independently
imported curve weight theorem; no implication from the Gram matrix is claimed.

At A=0 and B nonzero, geometric monodromy is C3 but the elliptic and Prym
cohomology remain. If q is 1 modulo three, arithmetic monodromy is also C3 and
every such commutator defect vanishes. If q is 2 modulo three, arithmetic
Frobenius acts by inversion and arithmetic monodromy is S3. The text explicitly
does not claim arithmetic commutator vanishing in that case. The family changes
its branch and ramification configuration, so it is correctly not described as
a deformation in a fixed punctured-local-system category.

## Replay and corrected findings

The replay constructs bounded polynomial finite fields rather than using field
tables. Its irreducibility criterion, multiplication, additive character signs,
double-root formula and primitive point histograms were checked by reading.
The identities between complete curve counts and middle-extension stalk sums
follow directly from those source equations. The Newton signs agree with
`#X=1+q^n-tr(F^n|H1)`.

The exact quartic weight criterion is valid: after passing from a reciprocal
quartic to the quadratic in `alpha+q/alpha`, the discriminant/slack inequalities
are precisely the condition that both real traces lie in `[-2 sqrt(q),2 sqrt(q)]`.
Its hostile controls include reciprocal quartics with incorrect weight or sign.

Elliptic degrees three and four are held out from the degree-two reconstruction.
The Prym degrees three and four are also checked from the first two degrees
using the proved reciprocity; this is explicitly labelled theorem-assisted,
rather than four entirely independent predictions. Direct prime-field equation
counts, multiplicative-group extension counts, alternate field models, and the
prescribed negative Kummer branch supply useful independent finite controls.

Two implementation findings were repaired before this freeze:

1. Python object equality identifies integers with equal-valued floats and
   Booleans. Comparing canonical JSON now prevents a coordinated artifact and
   binding rewrite from passing the exact-type contract. A hostile test covers
   the substitutions.
2. Negative exponents in binary-power loops would not terminate. Both field and
   polynomial power helpers now reject negative, inexact and oversized exponents
   before looping. Tests cover those cases.

Neither finding changed the source mathematics or valid-input point-count
artifact. The frozen producer has the repairs. No proof-critical check relies
on Python `assert`.

The current artifact covers six prime-field source curves and all extension
degrees one through four, 24 complete bounded field replays. Its branch rows
are extension-rational stalk data, not an explicit census of closed places.
That additional Euler-factor census would be an independent strengthening,
but its absence does not undermine the all-place mathematical proof or the
accurately stated finite coverage here.

## Independently verified primary references

- [Stacks 03QN](https://stacks.math.columbia.edu/tag/03QN), finite direct image,
  exactness and base change; [Stacks 0C1B](https://stacks.math.columbia.edu/tag/0C1B),
  tame Riemann--Hurwitz.
- Deligne, [La conjecture de Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf),
  Sections 1.5--1.6, 1.14--1.15 and 2.3--2.6: cohomological determinants,
  weights, constructible-sheaf Euler products, Frobenius convention and duality.
- Milne, [Lectures on Etale Cohomology](https://www.jmilne.org/math/CourseNotes/LEC.pdf),
  Theorems 24.1, 27.15 and 29.6, as supporting accounts.

The conductor counts are independently computed from tame inertia, and the
polynomial degrees are proved through genera and direct summands. No unverified
conductor formula is needed to carry the main argument.
