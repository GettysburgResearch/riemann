# Reynolds averaging does not produce a single native path

For every arity r>=2, the invariant average of all sequential activation
orders is not the current of any single continuous monotone path. This
is a source-realizability obstruction, even though the average belongs
to the convex hull of actual native currents. It is not a failure of
linear Reynolds averaging on the ambient representation.

The source is the literal half-source of L-102707 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc, blob
6810bcece309b0c54ae6c8fc84b314990004549c. Every current below retains its
original measure2ds. No retained-gamma or arithmetic-cover identification
is made.

## 1. The new compatibility inequality and its predecessors

For any two coordinates u,v of a continuous monotone path from the zero
corner to the one corner, put

    A = integral v du,  B = integral uv du,  C = integral v^2 du.

The occupation note NATIVE_OCCUPATION_MOMENTS.md at
a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc, blob
bea7d2be82e752ffe471a4e9902ca5bbc73c50aa, already proves Jensen and
Chebyshev constraints, including A^2<=C<=A and B>=A/2. The later
NATIVE_PATH_SYNCHRONIZATION_AND_TEMPLATE_ACCESSIBILITY.md at
a455dbe07c8d32fa3e7f3e74361abcfcafc681f9, blob
75f3d7d2b05e0daa29b64971888a26b7574dd03d, proves the lower Gram bound
C-A^2>=12(B-A/2)^2. The following complementary upper bound is derived
here; this is not a claim of priority beyond those named predecessors:

    C-A^2 <= 2B-A.                                      (1)

Indeed, use u itself as the integration coordinate. Its Stieltjes measure
du pushes forward to Lebesgue measure on[0,1], and v has a nondecreasing
representative f(u) in[0,1] almost everywhere. Vertical segments occur
at fixed u and have zero du mass. Any such f is a probability mixture
of threshold functions h_t(u)=1_{u>=t}, t in[0,1]. The endpoint thresholds
t=0 and t=1 supply the constant-one and constant-zero parts. This
representation includes jumps of f and hence completed monotone graphs.

For the uniform variable U on[0,1],

    Var(h_t(U)) = t(1-t) = 2 Cov(U,h_t(U)).

Centering is linear and the squared L2 norm is convex. Jensen applied
to the threshold mixture therefore gives

    Var(f(U)) <= integral Var(h_t(U)) dmu(t)
               = 2 Cov(U,f(U)),

which is exactly(1). A single threshold attains equality, so its factor2
is sharp. This probability representation proves an identity and an
inequality for the original occupation integrals; it does not replace
the primitive2ds or the Mellin measure by a probability measure.

## 2. The invariant sequential average

For each permutation sigma of the r coordinates, let gamma_sigma
activate coordinates one at a time, in that order, completely from0
to1. These are actual continuous monotone paths. Their speeds and pauses
do not change the Stieltjes currents.

For multilinear monomials X^a,X^b define the source matrix

    M(gamma)_(a,b) = 2 integral d(X^a) X^b.

The literal current at an ordered arithmetic pair is
v_n^t M(gamma) v_m, where lambda_n=sum_a v_(n,a) X^a. Coordinate
permutation acts on both monomial indices, so

    M_bar = (1/r!) sum_sigma M(gamma_sigma)              (2)

is exactly the invariant Reynolds average of one sequential current.
The primes attached to coordinates stay fixed when these paths are
observed; no permutation invariance of their physical metric is assumed.

Fix any pair u,v. In half the permutations v is activated before u;
then(A,B,C)=(1,1/2,1). In the other half u comes first, giving(0,0,0).
Consequently the average has

    (A_bar,B_bar,C_bar) = (1/2,1/4,1/2).                (3)

These are linear readouts of the literal source. In particular, for
distinct primes p,q attached to u,v, the actual half-source coefficients
lambda_p=-u/2, lambda_q=-v/2 and lambda_(pq)=uv/4 give

    B_(p,q)  = A/2,
    B_(p,pq) = -B/4,
    B_(q,pq) = (C-1)/8.                               (4)

Here B_(n,m)=2 integral d(lambda_n) lambda_m. The last identity follows
from integral d(uv^2)=1, retaining the endpoint contribution. Other
coordinates do not alter these three coefficients.

If one actual path had the complete averaged source(2), equations(4)
would force its pair moments to be(3). But (1) would read1/4<=0.
Thus no single monotone path realizes the Reynolds average, for every
r>=2. The violation of the quadratic compatibility inequality is
exactly1/4.

This does not contradict convexity of an ambient representation space.
The point(2) is a finite convex combination of legal currents. No linear
functional can strictly separate it from every legal current. The
obstruction is the nonlinear compatibility required of one common path,
not an invalid source weight or a missing permutation sector.
The synchronous path u_1=...=u_r is itself invariant. The conclusion is
that Reynolds averaging does not preserve the set of single-path
currents, not that invariant legal currents are absent.

## 3. A sharp gap in the pair-moment projection

The distance from(3) to the attainable pair-moment set, in the maximum
norm on(A,B,C), is exactly

    epsilon_* = (sqrt(10)-3)/2.                         (5)

To see the lower bound, write deltaA=A-1/2, deltaB=B-1/4 and
deltaC=C-1/2. Inequality(1) implies

    1/4 <= 2 deltaB - deltaC + deltaA^2
         <= 3 epsilon + epsilon^2

when all three absolute deviations are at most epsilon. This gives(5).
For attainment, use the threshold profile f(u)=1_{u>=t} with
t=1/2+epsilon_*. It is the continuous path that first moves u to t,
then activates v, then finishes u. Its moments satisfy

    A=C=1/2-epsilon_*,  B=1/4+epsilon_*,

using epsilon_*^2+3epsilon_*=1/4. Additional coordinates can be activated
afterward. This proves the exact pair-projection distance, not an exact
distance in the full source space or the physical Hilbert norm.

## 4. Original physical observations

Let T_H and T_infinity be the original observations, including every
physical1/sqrt(nm) factor, every reduced-ratio1/d alias and
dnu=|kappa_hat(t)|^2 dt/(2pi). Linearity always gives

    T_H(M_bar) = (1/r!) sum_sigma T_H(M(gamma_sigma)).    (6)

Equation(6) averages actual path observations. It does not define a
Reynolds operator on an arbitrary observed equivalence class: that
descent requires a separate invariant-kernel condition.

For any fixed set of distinct primes, the full tensor observation
T_infinity is injective in the original Hilbert space by
INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md at
822646ffea23d906c385f0273a8c45693e982c4d, blob
f7c42135e276a34d4da00279110666b0f4636080. Hence its averaged field(6)
cannot be the field of a single path. The finite-dimensional moment
gap(5) and this injectivity also give a strictly positive physical
distance, with a norm-comparison constant not evaluated here.

For the concrete primes2,3,5 the obstruction is already visible at H25.
The frozen synchronization note gives the complete coalesced coefficients

    z_(1/3) = -B/(8 sqrt3),
    z_(1/2) = (11+4C)/(96 sqrt2),
    z_(2/3) = (A/2+3B/32)/sqrt6.                       (7)

Thus equality of the actual H25 fields forces equality of A,B,C. The
original positive-density Mellin measure distinguishes the finitely many
different ratio frequencies, so Hilbert-space equality has the same
consequence. The averaged H25 field is therefore not a single-path
field. This uses all aliases in(7), rather than treating the raw records
in(4) as separately observed coordinates.

The same conclusion holds at H450 by its authenticated physical rank20
on all three-prime curvature directions: the bounded atlas is
a4d610431d5edaf26b00bae903bb9111837e4c31, with literal filtration
2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a. Differences of fixed-endpoint
path currents lie in that variation space. Neither this observation nor
the H25 calculation assigns a rank to an untested intermediate horizon.
A cutoff that forgets the required moments is not ruled out by this
argument. No arithmetic Galois/Walsh projector, full retained-gamma
decoder or all-prime conclusion is inferred.

This is a proof-only consequence with exact source readouts. No new
scientific computation or numerical acquisition is needed.
