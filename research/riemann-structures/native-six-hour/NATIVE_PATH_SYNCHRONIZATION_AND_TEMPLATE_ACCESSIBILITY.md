# Native path synchronization and the missing quadratic-template observable

This packet studies the original finite half-source at horizon25, with
primes2,3,5, all63 ordered factors, the measure2ds, the physical factors
1/sqrt(nm), and the original Mellin measure nu. It gives a source-defined
retraction, a sharp stability exponent, and an exact limitation of the
shared quadratic schedules used in the earlier discovery. It does not
identify the complete post-renewal gamma source or an orthogonal
principal/Walsh projector.

The frozen curvature source is
`bae7184724093d3589ad16b278dc104322428d6a`; the six occupation coordinates
and their whole-source reconstruction are those of
NATIVE_OCCUPATION_MOMENTS.md at
`a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc`. The quadratic source implementation is
frozen at `b3a8a85021cedefae034aaef7c14a6976429142b`. All statements below
are about continuous piecewise smooth monotone paths with endpoints000
and111. In particular, vertical path segments are allowed, but no jump
of the source parameter is introduced.

## 1. The exact source coordinates

Write the three activation functions as u,v,w and use

    A=integral v du, B=integral uv du, C=integral v^2 du,
    D=integral w du, E=integral uw du, F=integral w dv.

With the2-then3-then5 reference path, the complete source is

    B_path = B_ref + A V23,0 + B V23,2 + (C/2) V23,3
                      + D V25,0 + E V25,2 + F V35,0.       (1)

The physical ratio observation is injective on these six variation
vectors. Thus the coordinate conclusions here survive actual physical
coalescence; they are not assertions about an artificially separated
record norm.

For a direct original-readout check, let z_r be the coefficient of
exp(it log r), including the physical square-root weight and every
ordered pair with that ratio. The horizon25 source gives

    z_1/3 = -B/(8sqrt3),
    z_1/2 = (11+4C)/(96sqrt2),
    z_2/3 = (A/2+3B/32)/sqrt6,
    z_2/5 = D/(2sqrt10), z_3/5 = F/(2sqrt15).              (2)

For example, ratio1/2 contains the fixed(2,4) coefficient5/16 and the
(3,6) coefficient(C-1)/8, with their distinct common-factor weights.
Ratio2/3 also contains(4,6), whose coefficient is3B/16. Omitting those
aliases would give the wrong observation functional.

There is also a continuum of directly source-defined quadratic
constraints. For real s,t,

    integral(v-s-tu)^2 du
       = C-2sA-2tB+s^2+st+t^2/3 >= 0.                  (2a)

Minimizing the right side in s,t gives the stronger Gram inequality

    C-A^2 >= 12(B-A/2)^2.                               (2b)

These use the exact Stieltjes occupation measure du. They do not
replace either the primitive2ds measure or the original Mellin measure
nu. Equation(3) is the particular source square s=0,t=1.

## 2. An exposed source face and a genuine retraction

The affine source functional

    L = C-2B+1/3 = integral (v-u)^2 du >= 0               (3)

is nonnegative on every such path. In physical coefficients it is

    L = 24sqrt2 z_1/2 + 16sqrt3 z_1/3 - 29/12.            (4)

For each path point let delta=|v-u|. If v exceeds u there, later
monotonicity forces u to traverse the interval between those two
values while v is at least its value at that point. If u exceeds v,
the preceding traversal of u gives the analogous estimate. Hence

    L >= delta^3/3,
    ||v-u||_infinity <= (3L)^(1/3).                       (5)

Consequently L=0 holds exactly when u=v everywhere. The zero face has

    (A,B,C)=(1/2,1/3,1/3), F=D.                          (6)

The replacement

    T(u,v,w)=(u,u,w)                                     (7)

is again a legal monotone source path. On the six-coordinate source
chart it is the affine idempotent map

    P(A,B,C,D,E,F)=(1/2,1/3,1/3,D,E,D).                  (8)

Thus (7) induces a source-defined affine retraction onto the exposed
face. Equation(1) and physical injectivity define its corresponding
affine map on the actual observed source space, so the finite source
and physical observation diagrams commute exactly. This is a statement
on this six-dimensional affine family, not on all functions in L2(nu).
No orthogonality follows from idempotence.

The remaining face is exactly

    0<=D<=1, D/2<=E<=D-D^2/2.                            (9)

Necessity follows by writing w as a nondecreasing function of u-time:
the lower bound is Chebyshev's inequality and the upper bound puts
the mass last. For sufficiency, at fixed D combine the constant heightD
and the last-interval indicator1_{u>1-D}. This monotone step profile
has every E in(9), and its vertical changes are realized by ordinary
path segments with u=v fixed. The endpoint cases D=0,1 are immediate.
In particular the exposed face has affine dimension two.

## 3. Sharp stability in the original observed norm

Cauchy--Schwarz and integration by parts give

    |A-1/2| <= sqrtL,
    |B-1/3| <= sqrt(L/3),
    |C-1/3| <= L+2sqrt(L/3),
    F-D = -integral(v-u)dw,
    |F-D| <= (3L)^(1/3).                                (10)

In(1), T preserves D,E. All six observed variation vectors have finite
original L2(nu) norm. Therefore there is a constant depending only on
this fixed native source and its original kernel such that

    ||B_path-B_T(path)||_L2(nu) <= C_native L^(1/3).       (11)

Here0<=L<=1. One explicit admissible constant is the triangle bound
from(10), using the actual norms of V23,0,V23,2,V23,3,V35,0. No
replacement metric is used.

The exponent cannot be improved uniformly. For0<delta<1 take

    000 -> (0,delta,0) -> (0,delta,1)
        -> (delta,delta,1) -> 111.                       (12)

Its exact moments satisfy

    L=delta^3/3, A-1/2=delta^2/2,
    B-1/3=delta^3/6, C-1/3=2delta^3/3,
    D=1, E=1/2, F=1-delta.                              (13)

The observed difference divided by delta tends to -V35,0, a nonzero
vector in the original Mellin norm. For example its ratio3/5
coefficient is1/(2sqrt15). Finite distinct-frequency independence and
the nonzero original measure show that this vector has positive norm.
Thus(11) has sharp exponent1/3, even after physical observation.
The same paths attain equality in the sup-norm bound(5) and in the
|F-D| bound(10).

The same exponent is sharp for distance to the entire exposed source
face. The functional F-D vanishes on that face and is a bounded linear
functional on the finite physical variation space. On(12) it equals
-delta, so the distance to the face is at least a fixed positive
constant times delta. The synchronization estimate gives the matching
upper order L^(1/3). Choosing a different nearest face point therefore
cannot improve the exponent uniformly.

These statements concern the recombined observed current. Applying T
does not preserve literal derivative-site coefficients or any of the
primitive, integrated-site, integrated-pair, or ratio-coalesced
diagonals by a claimed isometry. Those resolutions remain separate.

## 4. The quadratic schedules miss one physical observable

For eta(s)=s(1-s), set

    u=s+a eta, v=s+b eta, w=s+c eta, -1<=a,b,c<=1.         (14)

These are monotone source paths. Direct polynomial integration with
the original measure gives

    A=1/2+(b-a)/6, D=1/2+(c-a)/6, F=1/2+(c-b)/6,
    B=1/3+(b-a)(5+a)/60,
    C=1/3+(b-a)(5+b)/30,
    E=1/3+(c-a)(5+a)/60.                                (15)

In particular

    A+F-D=1/2, L=(b-a)^2/30.                            (16)

The first equality is an exact schedule-family restriction. It is not
a universal source law: the2-then3-then5 path gives0, and the reversed
path gives1. In actual physical coefficients the missing functional is

    A+F-D = 2sqrt6 z_2/3 +(3sqrt3/2)z_1/3
                        +2sqrt15 z_3/5-2sqrt10 z_2/5.   (17)

The affine hull of the whole quadratic family has exactly dimension
five. Indeed let d=b-a,e=c-a. The five independent varying monomials
are d,e,ad,d^2,ae; their triangular map to A,D,B,C,E has nonzero
determinant. Independence is witnessed entirely inside the monotone
parameter cube: take h=1/4 and

    (a,b,c)=(0,h,0),(0,-h,0),(0,0,h),(h,2h,h),(h,h,2h), (18)

relative to(0,0,0). Their monomial matrix has determinant of absolute
value2h^8. The physical image has the same affine dimension by(1).

This is an affine-span statement, not a claim that every point of the
five-dimensional hyperplane is an attainable quadratic schedule. The
actual image has the nonlinear identities obtained from d,e,ad,d^2,ae,
including d(ae)=e(ad), as well as the original parameter bounds.
Nor does the missing-observable theorem identify an optimizer in
either the quadratic family or the full native path family.

## 5. Scope of the computational controls

The bounded replay retains all63 physical factors for the five open
basis witnesses and the reference. It independently compares the
literal polynomial source with(15), verifies(2),(4),(17) after complete
ratio coalescence, and checks source synchronization and sharp
staircase controls using literal path integration. The original
diagonal resolutions are retained for the quadratic controls.

The finite coefficient map and the proof of sharp stability use the
original kernel. They do not make T an orthogonal projector, identify
a parity/Walsh/finite-field augmentation, supply a post-renewal gamma
decoder, or prove a full principal-family estimate.

The declared original-metric probe now decides the orthogonality
question negatively. All eight inner products between the four
kernel directions and the two range directions have certified nonzero
intervals. For example,

    <V23,0, V25,0+V35,0>_L2(nu) > 0,
    approximately 2.3900221964405763.

An orthogonal projection would make every such inner product zero.
Thus this source-defined retraction is nonorthogonal in the actual
original Mellin norm. The producer retains all eight probes, rather
than selecting a favorable one after the computation.

The parent executed Ruff, the three producer modes, and14 ordinary
plus14 optimized tests successfully. The final note binding is replayed
separately before freezing. The retraction is only asserted at the
stated horizon25; extending the horizon requires a new source-closure
check, not an extrapolation from this finite chart.
