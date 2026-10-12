# A joint angular and radial bound extends the count-free census

Status: complete source-qualified component proof and exact rational
certificate. The existing independently replayed degree-eight and sign
primitives imply a complete simple actual-Xi census through height 3296.
No historical zero-count contract, new endpoint computation, global
real-zero assertion or RH theorem is used.

Dependencies: `xi/outer-ray/EIGHTH_MOMENT_CENSUS_RECOVERY.md` EM1–EM4
at SHA256 d5414e8f8de70b00f1b4dc4e66a091174a64552a0684b270d4c8fb3a539043dc,
its frozen checker c2b21b3e5c913904ecfa0c7add770523853fddf5d264d602155df53c744ff9a1,
the complete theta/strip/even-product source and one-occurrence selection
argument, and the separately reviewed finite-census column theorem.
The native EM checker was independently replayed in normal and optimized
modes, including 556 actual refined signs and the degree-eight coefficient.
Its 7771 older sign facts are imported with their frozen source bindings.

## CM1. The joint corner minimum

Let k>=1, R>0, A>=0 and assume the stronger angular guard

    (2k+1) atan(A/R) < pi/2.                           (CM1)

For x>=R and 0<=y<=A put f_k(x,y)=Re((x+iy)^(-2k)). With
theta=atan(y/x), direct differentiation gives

    partial_x f_k = -2k |x+iy|^(-2k-1) cos((2k+1)theta),
    partial_y f_k = -2k |x+iy|^(-2k-1) sin((2k+1)theta).

The first is strictly negative; the second is negative for y>0 and
zero at y=0. The function is even in y. Consequently, if R<x<=H
and |y|<=A, its minimum is the correlated corner value

    Re((x+iy)^(-2k)) >= Re((H+iA)^(-2k))
        = c_k(H,A)/(H^2+A^2)^k,                       (CM2)

where c_k(H,A)=cos(2k atan(A/H))>0. This retains the relation
between the root's angle and its radial size. Using c_k(R,A) and
the radius H separately loses that relation.

The extra angular condition is necessary for this simple monotonicity
argument. At k=1,R=3/2,A=1, the original doubled angle is acute
(2 atan(2/3)<4/3<pi/2), but
Re((R+iA)^(-3))<0, so partial_x f_1>0 near that corner.
The checker preserves this exact negative control.

## CM2. A stronger complete-residual exclusion criterion

Retain the source's complete even product, all remaining multiplicities
and both members of every unknown nonreal conjugate pair. Suppose every
source zero satisfies |Re rho|>R and |Im rho|<=A. Remove exactly one
occurrence from each authenticated real sign interval, with its negative
reflection, and let T_k be the complete residual inverse-2k moment.

Condition CM1 implies the weaker acute condition for 2k, so every
remaining occurrence has positive real projection. If any remaining
zero has |Re rho|<=H, select its positive-half-plane occurrence.
Its contribution alone is at least CM2, and all other real projections
are nonnegative. Therefore a valid full residual upper bound T_k<=U
and the exact strict guard

    U (H^2+A^2)^k < c_k(H,A)                          (CM3)

exclude every unselected zero and extra multiplicity through H.
This proves a complete simple real census there. No initial uniqueness
or completeness is assumed. The conclusion includes the boundary H
when every selected interval is disjoint from that boundary.

## CM3. Actual Xi reaches height 3296 from unchanged primitives

The complete positive theta seed and strip already proved in the EM
source give R=27/5 and A=1/2. For k=4,

    9 atan(5/54) < 9*(5/54)=5/6 < 3/2 < pi/2,

so CM1 is established by exact rational arithmetic and pi>3.
The separate complete-moment bootstrap to R=14 is not needed here.

Use precisely the full residual upper endpoint U4 from the authenticated
EM receipt: no midpoint roots or selected subset replace its 8049 interval
terms. The accompanying exact checker verifies every imported direct
source hash, all selected boundary geometry and the rational CM3 predicate.
It finds:

| Quantity | Value |
|---|---:|
| Accepted integer height |3296|
| CM3 ratio upper, rounded only for reading |0.9987264451|
| Complete simple positive real zeros through3296 |2761|
| Maximum covered derivative order from the column theorem |6589|

Height 3297 fails this *specific* upper-endpoint/corner predicate.
This is a limit of the present certificate, not a claim of an omitted
zero or a mathematical barrier at 3297. The failure and the accepted
height are both tested exactly, without a floating-point search.

The separately reviewed column theorem consequently gives, for every
integer 0<=r<=6589 and every real lambda>0,

    |T| < 3296-(r+2)/2,  y>=0,
    E_r=Xi^(r)-i lambda Xi^(r+1),
    E_r(T-iy)!=0, E_r'(T-iy)!=0,
    Re(i E_r(T-iy)/E_r'(T-iy))>0.

The horizontal range and derivative order remain finite. The imported
complete analytic source and older primitive sign facts remain explicit;
neither a historical complete-count nor a published large verification
is a hypothesis of this census argument.

## Validation and reproduction

    python literature/check_corner_moment_census.py
    python -O literature/check_corner_moment_census.py

Run from this wave directory, or use the absolute script path. The
checker imports the frozen successful EM receipt (override with
`--eighth-receipt`), verifies all its direct source bindings, and uses
only exact Fraction arithmetic for the new guard and geometry. It
does not repeat the native signs or integration. Their independent
normal/-O replays and the 320 bit real-s coefficient/endpoint oracle
are recorded separately. The checker certifies the finite strict
guards; the complete-source analytic implication is the written
CM1–CM3 proof above.
