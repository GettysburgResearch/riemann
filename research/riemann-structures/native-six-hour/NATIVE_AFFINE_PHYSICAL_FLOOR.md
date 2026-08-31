# The affine physical floor and source-feasible halfspace bounds

Status: proposed finite-source theorem before a new bounded scout.
Exact source: NATIVE_CURVATURE_SPAN.md at
6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537 and its complete original
primes2,3,5 / physical-product25 acquisition. All63 ordered records and the
original measure remain present. No full retained-gamma claim is made.

Let F_ref be the field of the actual axis path activating2, then3, then5.
Let V_1,...,V_6 be the six observed curvature vectors in their frozen order.
Every actual monotone path has field
F_ref + sum_i x_i V_i, with x=(A,B,C/2,D,E,F) in the occupation notation.

Use the actual physical inner product, not an unweighted coefficient norm:
G_ij=<V_i,V_j>, g_i=<V_i,F_ref>, c=||F_ref||^2.
The actual even measure makes these numbers real. The frozen injectivity
theorem and finite exponential independence imply G is positive definite.
Thus
E(x)=c+2g^T x+x^T Gx
    = E_aff+(x-x_star)^T G(x-x_star),
x_star=-G^-1 g, E_aff=c-g^T G^-1g.
This is an exact identity and E_aff is a lower bound for every native path.
It is not a claim that x_star is source attainable.

The lower bound is strictly positive in this finite panel. At ratio16,
only the source row(16,1) contributes. Its path-independent source value
is2[binom(1/2,4)-binom(1/2,2)]=11/64 and its physical amplitude is11/256.
All six variations vanish there. Hence zero is outside the affine field
space. A finite-dimensional affine subspace of a Hilbert space is closed;
its positive distance to zero is exactly sqrt(E_aff). No zero-height or
cofinal source-capture assertion is used.

The fixed symmetric source S=(B_ref+B_ref^transpose)/2 is orthogonal to
all six exchange-odd variations under the original even measure. Direct
kernel pairing can check every one of these six zero cross-terms before
interval evaluation. Its norm supplies a separate, possibly weaker,
normalization check. It does not replace the remaining fixed odd part.

For any proven source halfspace Lx<=b, put d=Lx_star-b. If d>0 then the
Cauchy--Schwarz inequality in the G metric gives the stronger bound
E(x)>=E_aff+d^2/(L G^-1 L^T).
Indeed L(x-x_star)<=-d and the squared dual norm of L is L G^-1 L^T.
The maximum of independently certified bounds remains valid. Equality
for one halfspace does not establish compatibility with every source
constraint or construct a native path.

The elementary source constraints include0<=A,D,F<=1,
C<=A, B>=A/2, E>=D/2 and0<=A+F-D<=1.
Jensen C>=A^2 gives, for every fixed real t,
2t A-C<=t^2.
The sharp rearrangement bound B<=A-A^2/2 gives
B-(1-t)A<=t^2/2.
Likewise E-(1-t)D<=t^2/2.
These are valid linear inequalities for all native sources and their
convex hull, despite the nonlinear source body's not being a finite
polytope. The scout uses a fixed rational t grid, not fitted constraints.

The same source gives the stronger square identities
int(v-u)^2 du=C-2B+1/3>=0 and, for all fixed s,t,
int(v-s-tu)^2du=C-2sA-2tB+s^2+st+t^2/3>=0.
These provide further valid source halfspaces before any optimization.

The proposed numerical certificate uses exact multiquadratic/logarithmic
kernel expressions and outward rational intervals. Interval elimination
must certify every pivot away from zero, and all subsequent operations
round outward to a declared dyadic grid. The bounds enclose the exact
affine optimum and each declared halfspace correction. A failed interval
test is recorded as uncertified, not replaced by ordinary high precision.
No grid search over paths can prove the affine minimizer attainable.
