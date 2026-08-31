# Native occupation moments: a curved source body above an order polytope

Status: proposed proof with a separately preregistered bounded producer.
This continues the source-owned six-dimensional variation theorem in
NATIVE_CURVATURE_SPAN.md. Its literal source acquisition is pinned to
`bae7184724093d3589ad16b278dc104322428d6a`; the whole acquisition is replayed.
All statements retain primes2,3,5, every63 ordered factor pair up to
physical product25, the original2ds measure, and physical1/sqrt(nm).

The linear span of path variations does not describe which points one
monotone path can attain. Six elementary occupation moments give an exact
coordinate system for this remaining source constraint. Even a coherent
distribution of event-order words can fail that constraint.

## 1. Six exact source coordinates

For a continuous piecewise smooth monotone path from0 to1 put u=u_2,
v=u_3,w=u_5, and define

    A=int v du,        B=int u v du,       C=int v^2 du,
    D=int w du,        E=int u w du,       F=int w dv.              (1)

Use the six source vectors of the curvature theorem, in its stated order.
Let B_ref be the actual path source obtained by activating2, then3, then5.
Its six moments are all zero. The complete actual source vector is

    B_path = B_ref
        + A V_23,0 + B V_23,2 + (C/2) V_23,3
        + D V_25,0 + E V_25,2 + F V_35,0.                         (2)

This is an equality in the full63-record source before observation.
The one-forms in(1) have exactly the curvature polynomials1,u,v and1,u
needed in the preceding theorem, with the factor2 on the derivative of
v^2. Subtracting the right side of(2) from the native source one-form
therefore leaves a closed polynomial one-form on the cube. Its integral
depends only on the endpoints; the reference path fixes that constant.

One can also check the source directly on all nonconstant coordinates
with n<m:

    B_(2,3)=A/2,             B_(2,6)=-B/4,
    B_(3,4)=1/8+3A/8,       B_(2,9)=1/2-3A/8,
    B_(3,6)=-1/8+C/8,       B_(2,12)=-A/4+3B/16,
    B_(3,8)=(1-A)/16,       B_(4,6)=3B/16,
    B_(2,5)=D/2,            B_(2,10)=-E/4,
    B_(4,5)=-3D/8,          B_(3,5)=F/2.                          (3)

Reversed entries follow from the fixed symmetric endpoint source.
Same-prime and unit coordinates are path independent. The corrected
ratio map is injective on these six variation vectors, so equality of
the complete observed fields implies equality of all six moments.
This does not identify arbitrary path parameter coordinates with moments.

## 2. An exact thirty-word outer polytope

Choose independent random activation times with continuous distribution
functions u,v,w: two iid times of label2, two iid times of label3, and
one time of label5. A monotone continuous source path supplies these
distributions through its Stieltjes measures du,dv,dw. Independence
is a probabilistic representation of the actual products in(1); it
does not assert independence of arithmetic source atoms.

The five times are almost surely distinct. Their label order is one of
the30 words with multiset{2,2,3,3,5}. For such a word define six rational
coordinates:

    a(word) = #{(3,2) pairs with3 earlier}/4;
    b(word) = #{3 labels before the last2}/4;
    c(word) = #{2 labels after the last3}/2;
    d(word) = #{2 labels after5}/2;
    e(word) = 1_{5 before the last2}/2;
    f(word) = #{3 labels after5}/2.                               (4)

Then (A,B,C,D,E,F) is the expectation of(4) under the actual word law.
For example, P(T_3<max(T_2,1,T_2,2))=2 int u v du=2B; averaging the
two possible label3 choices gives exactly the denominator4 in b(word).
Likewise c(word) represents P(max(T_3,1,T_3,2)<T_2).

Consequently every native moment vector lies in the convex hull of
these30 rational points. This is a necessary source constraint and an
exact finite construction, not a claim that every word law is produced
by independent activation distributions. A new bounded replay will
enumerate all30 words rather than fitting a polytope from path samples.

## 3. The order polytope is strictly too large

For every actual path, use the probability measure du, whose total mass
is one. Jensen's inequality and0<=v<=1 give

    A^2 <= C <= A.                                               (5)

The word(3,2,2,3,5) has rational vector

    (a,b,c,d,e,f)=(1/2,1/4,0,0,0,0).                             (6)

It belongs to the thirty-word convex hull by construction, but violates
C>=A^2. Thus even a completely declared event-order point need not be
native-source faithful. By(2) and injectivity of the physical observation,
its affine source/field cannot equal the source/field of any actual
monotone path. This is a finite observation obstruction, not a statement
about the complete post-renewal decoder.

The obstruction is not merely an unfortunate finite word choice. The
projection of the actual source moment set onto(A,C) is EXACTLY

    {(a,c): 0<=a<=1, a^2<=c<=a}.                                (7)

Necessity is(5). For0<a<=1 and a^2<=c<=a, put h=c/a and
t_0=1-a/h=1-a^2/c. Take the actual monotone path:

    move u from0 to t_0 while v=0;
    move v from0 to h while u=t_0;
    finish u from t_0 to1 while v=h;
    finish v from h to1;
    activate w last.

Then A=h(1-t_0)=a and C=h^2(1-t_0)=c. The limiting case a=0 uses u
before v, and a=1 forces c=1 and uses v before u. All segments are
continuous monotone source paths; a coordinate pause is not a deleted
source interval. The remaining moments on the interior construction are

    B=a-a^3/(2c),    D=E=F=0.                                   (8)

In particular c=a^2 gives the attainable parabola
(A,B,C)=(a,a/2,a^2). The projection(7) has a curved boundary and is
not a polytope. Therefore neither the full native moment set nor the
convex hull of that set can be a finite polytope: a linear projection of
a finite polytope would be a finite polytope. The exact finite word
polytope is a useful outer relaxation, but cannot be the final source body.

## 4. Further sharp pairwise constraints and a cross-prime constraint

Write v along u-time as a nondecreasing measurable h:[0,1]->[0,1].
Plateaus of u do not affect du integrals. Then A=int h and B=int t h(t)dt.
Chebyshev's integral inequality and the maximal last-interval rearrangement
at fixed mass give

    A/2 <= B <= A-A^2/2.                                        (9)

For a direct lower proof, integrate
(t-s)(h(t)-h(s))>=0 on the unit square.
For the upper proof, compare h with1_{t>=1-A}; moving any mass from
below1-A to above it can only increase its t-weighted integral.
Both endpoints are attained by the constant-height and final-step paths.
The same argument gives

    D/2 <= E <= D-D^2/2.                                        (10)

Finally take one independent activation time of each prime. Every
realized total order satisfies

    0 <= 1_{T3<T2}+1_{T5<T3}-1_{T5<T2} <=1.

Taking expectations proves0<=A+F-D<=1. The thirty-word construction
retains this cross-prime constraint together with the higher order
ones, but it does not remove the nonlinear requirement(5).

No claim is made that(5),(9),(10) and this one cross-prime inequality
characterize the entire six-dimensional source body. Establishing the
remaining compatibility among the three activation distributions is
a separate constructive problem.

## 5. Computation and scope

The planned replay will compare(2) with direct native integration on
declared rational piecewise linear paths, before and after the true
physical ratio coalescence. It will enumerate every word in(4), retain
the exact counterfeit(6), and verify rational samples of(7)--(8).
Those finite controls do not prove Jensen or the continuum realization;
their proofs are above.

The source body may be used to constrain a physical energy optimization.
An optimizer over its word-polytope relaxation is only a lower bound
until it satisfies the actual moment constraints and a path is constructed.
The finite physical energy, source measures, and full retained-gamma
principal member remain distinct. No RH/GRH conclusion is asserted.
