# Exact early-activation descent in the original source metric

This is a source-directed fallback for the registered H25/H30/H60
campaign. It does not change that acquisition, assert that its sufficient
cone fails, or claim that an improving path has been found. It gives a
test that would distinguish failure of a sufficient polynomial cone from
an actual decrease of the complete original observed energy.

The source is the literal polarized current of L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`. Its exact factor2,
ordered records, physical1/sqrt(nm) factors and ratio collection are
retained. The observation is the original measure authenticated by
`global_geodesic_scout.py` at
`5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4`, blob
`32a4c01750e99a37c4d1992fa6bddafeaea8fe06`. No diagonal norm replaces
the full observed sum. The twenty-moment source decoder and polynomial
coefficients are those of `ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md`
and `EIGHT_QUADRATIC_LAST_ACTIVATION_CONE.md`.

## 1. An actual one-parameter source path

Fix a finite horizon H and a continuous monotone planar path
z(s)=(u(s),v(s)), from(0,0) to(1,1), parametrized by
s=u+v in[0,2]. Let gamma_0 keep w=0 along this entire path and then
raise w to1 at its endpoint. Choose any marked planar point s0.
For 0<=delta<=1, define gamma_delta by the following ordered steps:

1. Follow z to s0 with w=0.
2. Raise w from0 to delta at that fixed planar point.
3. Follow the remaining planar path with w=delta.
4. Raise w from delta to1 at(1,1).

Every gamma_delta is an actual continuous monotone BV source path,
with inserted vertical segments. This is not a convex mixture of
observed fields. At delta=0 it is gamma_0, up to pauses. The points
s0=0 and s0=2 are allowed and retain the respective endpoint orders.

## 2. Exact vector-valued source identity

Write the complete physical field as

    F_H(gamma)=F_(H,0)+sum_j M_j(gamma)V_j.             (1)

All V_j are actual finite Mellin fields in the original Hilbert space.
Apply the twenty-moment exact-form reduction with vector coefficients.
Its dw coefficient R(u,v) is independent of w. Subtracting the exact
potential T=wR changes only a fixed endpoint field. The remaining
vector one-form is

    [P0+w P1+w^2 P2]du+[Q0+w Q1+w^2 Q2]dv.            (2)

Vertical w segments have zero integral in(2), while their full original
contribution is retained by the endpoint potential. Therefore define

    L(s0)=integral_(s0)^2 [P1 du+Q1 dv],
    Q(s0)=integral_(s0)^2 [P2 du+Q2 dv].                (3)

Then the exact complete-field identity is

    F_H(gamma_delta)-F_H(gamma_0)
       =delta L(s0)+delta^2 Q(s0).                    (4)

This includes every ordered source record and every equal-ratio alias.
The identity also holds before physical collection in the vector space
of integrated ordered records. It does not identify a derivative-site
diagonal with the norm after those records have been summed.

## 3. The original energy is an exact quartic

Put F*=F_H(gamma_0), L=L(s0), Q=Q(s0), and use real parts of the
original Hilbert inner products. Set

    a=Re<L,F*>, b=Re<Q,F*>,
    c=2b+||L||^2, d=2Re<L,Q>, e=||Q||^2.

Expanding(4) gives

    I_H(gamma_delta)-I_H(gamma_0)
       =2a delta+c delta^2+d delta^3+e delta^4.         (5)

There is no omitted mixed term in(5). In particular a negative scalar
tail is an actual source descent direction, not merely a failure of
one sufficient square-positivity test.

For a fully quantitative choice, let a<0 and take any certified bound

    Mbar >= 2|b|+(||L||+||Q||)^2,  Mbar>0.

If abar<0 is a certified upper bound for a, every positive rational

    delta <= min(1,-abar/Mbar)                         (6)

satisfies

    I_H(gamma_delta)-I_H(gamma_0) <= delta abar <0.      (7)

Indeed for delta<=1 the quadratic and higher terms in the direct
norm expansion are at most delta^2 Mbar. Thus(6) can be checked with
outward rational intervals and yields a finite actual path, without
using a floating optimizer as an acceptance decision.

If a is proved EXACTLY zero and c<0, the next-order test is equally
explicit: a bound Dbar>=|d|+e, Dbar>0, and
0<delta<=min(1,-cbar/(2Dbar)), where cbar<0 bounds c above, give
an energy decrease at most cbar delta^2/2. Merely having an interval
for a that contains zero does not justify this second-order test.

For a fixed s0 the full minimum of(5) on[0,1] is attained at an
endpoint or at a real root in(0,1) of

    2a+2c delta+3d delta^2+4e delta^3=0.                (8)

Any future root isolation must retain endpoint and uncertain-sign
guards. An unresolved interval is not a certified improving path.

## 4. An exact fixed-planar first-order criterion

Let c_j=Re<V_j,F*> be the FULL twenty-coordinate half-gradient.
Use these coefficients in the scalar P1,Q1 of the eight-quadratic
note. The scalar tail

    A(s0)=integral_(s0)^2 [P1 du+Q1 dv]                (9)

is exactly a in(5). A pointwise negative P1 or Q1 need not make any
tail negative, so failure of the sufficient global cone cannot be
substituted for(9).

More generally replace the planar value w=0 by w=delta h(s), where
h is any nondecreasing function with0<=h<=1, and complete w at the
endpoint. Such an h is a probability mixture of threshold controls;
an endpoint mass represents any unused activation. Fubini and the
atomlessness of du,dv give

    derivative_(delta=0) I_H
       =2 integral A(t)dmu(t).                        (10)

Consequently A(t)>=0 for every t is NECESSARY AND SUFFICIENT for
absence of an infinitesimal early-w descent on this fixed planar
path. If some A(t)<0, the single marked activation at that t already
gives the strict descent in(6)-(7). This criterion is stronger than
testing only a chosen finite set of marks, but remains a fixed-planar
criterion. It does not decide arbitrary changes of the planar path.

When all tails are nonnegative, a finite activation may still need
the quartic test(5). The signed quadratic source measure is not
discarded. Its convex and concave cases are separately treated in
`NATIVE_FIXED_PLANAR_LAST_COORDINATE_SUPPORT.md`.

## 5. Finite exact evaluation on the clipped candidate

For a rational clipped-affine profile v=clip(lambda+mu u), mu>0,
include the initial and final vertical completions as ordered planar
segments. On each horizontal or affine part, substitution into P1,Q1
has degree at most3 in the segment variable; the tails therefore have
polynomial antiderivatives of degree at most4. The same is true of
P2,Q2. Vertical parts reduce to univariate polynomials of degree at
most2. Thus all quantities in(3),(9) are exact rational combinations
of the physical field columns and the candidate parameters.

The minimum of a tail on one segment can be checked at its endpoints
and the real roots of its degree-at-most3 derivative. For a root-box
candidate, outward interval substitution must respect its strict
clipping regime; a guard failure stays a failure. Alternatively, use
a nearby rational candidate and recompute its original gradient and
all ordered source coefficients. A negative certified tail at that
actual rational path then proves its own strict improvement directly.

The norms and cross terms in(5) use the original Gamma matrix already
defined by the finite source. A future bounded experiment should
retain its marked point, full path vertices, all ordered record
coefficients, physical-ratio array, exact quartic and all acceptance
margins. It should have a new producer identity rather than rewriting
the registered H25/H30/H60 outcomes. This note asserts no numerical
sign or all-horizon optimum and supplies no full retained-gamma map.
