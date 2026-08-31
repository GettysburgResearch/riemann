# Synchronization does not descend through the complete native source

Status: proposed all-height source theorem, with a bounded exact producer
still to be run. Scope: primes2,3,5 and the literal half-source product,
original2ds integration, physical1/sqrt(nm), and arbitrary finite
physical-product horizons. This extends no full retained-gamma decoder.

Exact dependencies: literal half-source lemmaL-102707 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc; complete curvature theorem at
6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537; occupation source coordinates at
a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc. The producer authenticates their
Git blobs before reconstructing new coefficients from the binomial formula.

The horizon25 synchronization retraction is a real source operation at
that horizon. It need not descend through source observations at a
larger horizon. Here two actual monotone paths have IDENTICAL original
integrated coefficients for every2/3/5-supported pair(n,m), but their
synchronized fields differ already at product horizon60.

1. Construct two actual paths.
Choose a nonzero rational polynomial Q of degree at most4 satisfying
int_0^1 t^j t^3(1-t)^2 Q(t)dt=0 for j=0,1,3,4.
Such a Q exists by four linear equations in five rational coefficients.
Its moment with j=2 is nonzero: otherwise Q is orthogonal to every
polynomial of degree at most4 in the positive weight t^3(1-t)^2dt,
including itself. The five-dimensional weighted Gram matrix is positive
definite, so the four-row system has rank4 and its kernel has dimension1.

Put P=t^3(1-t)^2Q. Clear rational denominators and fix the sign by a
positive highest coefficient before choosing
delta=1/(1+sum |coefficients of P'(t)/t^2|).
Then |delta P'(t)| <= c t^2 on[0,1] for a constant c<1. Consequently
w_plus(t)=t^3+delta P(t), w_minus(t)=t^3-delta P(t)
both have derivative at least2t^2, start at0 and finish at1.
They are actual continuous monotone polynomial schedules.

Each full path first activates v=u3 from0 to1 while u=u2 and w=u5
are zero. It then follows (u,v,w)=(t,1,w_plus/minus(t)).
Both paths have the same endpoints, prime labels and source measures.

2. All original coefficients agree, at every horizon.
For each fixed integer n supported on2,3,5, the literal coefficient
Lambda_n(u,v,w) is separately affine in each of u,v,w. On the main
segment v=1 it is a constant multiple of a bilinear polynomial in u,w.
Every polarized source one-form2dLambda_n Lambda_m is therefore a
linear combination of u^i w^j du (i<=1,j<=2) and
u^i w^j dw (i<=2,j<=1).

Modulo exact polynomial differentials and their common endpoints, these
forms are determined by the four sufficient moments
int w du, int u w du, int w^2 du, int u w^2 du.
Indeed integrate each dw term by parts; pure-u and endpoint terms
are fixed. The plus/minus differences of the four moments are,
respectively,2delta times moments0,1 of P and4delta times moments3,4
of P. They all vanish by construction. The initial v segment is common.
Thus B_nm(plus)=B_nm(minus) for EVERY supported n,m, before observation,
and hence their physically observed fields agree at every finite horizon.
This is an all-height polynomial-form proof, not an extrapolation of a
finite enumeration.

3. Synchronization exposes the missing moment.
Apply T(u,v,w)=(u,u,w) to both actual paths. The common initial v
segment becomes constant. Their main segments are(t,t,w_plus/minus(t)).
At physical-product horizon60, the only ordered rows with n/m=3/5 are
(3,5) and(6,10). Direct literal differentiation gives the coalesced
physical amplitude
1/sqrt15 [ (1/2)int w du + (1/8)int u^2 w du ].
The factor1/8 includes the actual common-factor weight1/2 from(6,10);
omitting it would give the wrong observation.

Therefore the plus-minus difference at ratio3/5 is
delta/(4sqrt15) int t^2 P(t)dt !=0.
Finite exponential independence in the original nonzero observation
measure makes the synchronized fields distinct in that Hilbert space.
In particular no function of the original complete integrated pair
source, nor of its observed field, can implement this synchronization
on every source path. This refutes nonlinear as well as linear descent.
It does not refute the operation on labelled paths themselves.

4. A finite constructive enlargement, before physical coalescence.
The preceding four moments were sufficient, but not minimal.
For bilinear source functions span{1,u,w,uw}, wedge antisymmetry makes
the original pair-curvature span exactly{1,u,w}du wedge dw.
The uw coefficient cancels. Three occupation moments suffice:
int w du, int u w du, int w^2 du.

After synchronization the actual source functions span
{1,u,u^2,w,uw,u^2w}. These are obtained, up to nonzero rational constants,
from literal indices1,2,6,5,10,30. Their pair-curvature span is exactly
{1,u,u^2,u^3,w,uw,u^2w}du wedge dw.
For f=u^i w^j,g=u^k w^l the coefficient is
(i*l-j*k)u^(i+k-1)w^(j+l-1); the putative top u^3w term cancels.
Every listed monomial occurs, and pairs of those actual indices with
nonzero curvature have product at most300.

Thus a seven-moment enlargement suffices for every synchronized pair:
int u^k w du for k=0,1,2,3 and
int u^k w^2 du for k=0,1,2.
It adds four occupation coordinates to the three original ones.
The minimality statement here concerns the literal source curvature
space modulo exact endpoint forms. The complete physical coalescence
rank at horizon300 is a separate finite test, not presumed from record
rank. Seven distinct rational rectangle witnesses can realize the full
source variation span by Stokes and polynomial interpolation.

This provides a constructive repair of the loss of information: retain
the needed higher occupation moments before observation. It does not
claim that the old observation secretly already contained them, or that
this small prime laboratory supplies a cofinal arithmetic decoder.
