# Twenty source moments at every fixed-three-prime horizon

Keep the same primitive half-source on primes2,3,5 and its independent
monotone activation coordinates(u,v,w). This extends the source-record
description, not the six-dimensional H25 quotient or its synchronization
map. No full retained-gamma identification is asserted.

The source is L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, exact blob
`6810bcece309b0c54ae6c8fc84b314990004549c` for
`claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md`.
The actual2ds normalization and coefficient extraction are also frozen
in `GEODESIC_FACTOR_EXCHANGE.md` at
`15967a52e846f1037bb0446db43f3d4a9c3fc821`. The independent dimension
count is recorded in `MULTIGROUP_NATIVE_CURVATURE_DIMENSION.md`;
the present note gives explicit moment and support operators.

## 1. Finite dependence before any physical quotient

For every local exponent e, the coefficient

    h_e(t)=[z^e]((1-t)sqrt(1-z^2)+t sqrt(1-z))           (1)

is affine in t. Thus every prime-supported integer n has a raw
coefficient Lambda_n in P1(u) tensor P1(v) tensor P1(w), regardless
of the physical horizon. Only finitely many such n occur at each
fixed horizon. The literal ordered-record coefficient is

    z_(n,m)(path)=2 integral Lambda_m dLambda_n,          (2)

before the physical1/sqrt(nm) factor and before collecting equal
ratios. Formula(2) retains the actual source measure; a derivative
site may still be kept as provenance rather than prematurely deleted.

Expand Lambda_n=sum_a c_n(a)x^a for a in{0,1}^3. For one ordered
monomial pair(a,b), put m=a+b and s=a-b. Then

    2 x^b d(x^a)=d(x^m)+sum_i s_i x^(m-e_i)dx_i.         (3)

Only coordinates with m_i=1 appear in the last sum. Write
I(m)={i:m_i=1} and J(m)={i:m_i=2}. The endpoint contribution in(3)
is1 for m nonzero and0 for m=0.

If J(m) is nonempty, retain one moment
M_(m,i)=integral x^(m-e_i)dx_i for every i in I(m).
If J(m) is empty and I(m) is nonempty, choose its largest coordinate
r as anchor and use

    M_(m,r)=1-sum_(i in I(m),i!=r) M_(m,i).              (4)

The resulting coefficient for this group is the constant
1+s_r plus sum_(i!=r)(s_i-s_r)M_(m,i). If J is nonempty it is
instead1+sum_i s_i M_(m,i). Cases with I empty contribute only
their endpoint constant. These formulas are an explicit rational
decoder for EVERY ordered monomial pair, hence for every record(2).

The retained moment count is

    3+2 + 9+6 =20.                                     (5)

The first two terms come from squarefree totals with two or three
coordinates. The last two come from totals having a squared
coordinate and respectively one or two coordinates of exponent1.
Different total monomials cannot mix under differentiation. Within
one total, the only exact-form relation is(4) when J is empty;
if J is nonempty, an exact multiple of d(x^m) would have a nonzero
component in a J coordinate, absent from the retained forms. This
also proves independence modulo endpoint-exact forms.

An explicit basis consists of the following integrals:

| Family | Integrands, with the indicated differential |
|---|---|
| squarefree totals | v du; w du; w dv; vw du; uw dv |
| one unsquared coordinate | w^2 du; v^2 du; v^2w^2 du; w^2 dv; u^2 dv; u^2w^2 dv; v^2 dw; u^2 dw; u^2v^2 dw |
| two unsquared coordinates | vw^2 du; uw^2 dv; v^2w du; uv^2 dw; u^2w dv; u^2v dw |

Thus every horizon has an exact affine20-moment SOURCE-RECORD map.
This is not a claim that all20 directions remain independent after
physical-ratio coalescence at a particular horizon. That is the
separate measured rank question in the horizon atlas.

## 2. The horizon changes a physical Gram, not these source moments

For each finite horizon H, retain its complete declared ordered
records and apply their original1/sqrt(nm) physical weights and
Mellin phases. Substituting(3)-(4) before the ratio collection gives

    F_H(path)=F_(H,0)+sum_(j=1)^20 M_j(path)V_(H,j),
    I_H=c_H+2g_H.M+M^t G_H M.                           (6)

Every entry of G_H is an inner product in the SAME original Mellin
measure. It is positive semidefinite; positive definiteness and
rank depend on the actual physical readout and horizon and are not
assumed. The source path moment set in(6) is fixed, but its image
and metric are horizon dependent. Arbitrary points of its convex
hull are not thereby declared actual paths.

This construction preserves record coefficients and the complete
observed sum. It does not identify the grouped norm with a literal
derivative-site diagonal, whose measure and site history stay separate.

## 3. Last-activation paths still have a three-moment planar operator

On a path that keeps w=0 until(u,v)=(1,1), every basis moment
containing a positive w power against du or dv is zero. Every dw
basis moment equals1 because u=v=1 while w rises. The remaining
nonconstant moments are

    A=integral v du, C=integral v^2 du,
    integral u^2 dv=1-2B, B=integral uv du.               (7)

Consequently the restriction of(6) to last-activation paths is an
affine function of(A,B,C/2) for EVERY three-prime-supported horizon.
Its gradient support problem is still

    minimize integral[c v^2+(a+bu)v]du,                 (8)

with horizon-dependent coefficients from the original physical Gram.
For c>0 the same clipped affine or isotonic constant profile solves
this support problem. A self-consistent profile proves a minimum in
this restricted family, but needs a full-path support check to give
a global result, just as at H25. No sign in(8) is assumed to persist
when the horizon changes.

## 4. A polynomial full-path support cone

Given a candidate's20-moment gradient, reconstruct its source
one-form ell=P du+Q dv+R dw using the above finite basis. Initially
the differentiated coordinate has degree at most1 and the other
coordinates degree at most2. Remove its dw term by the exact
potential

    T(u,v,w)=integral_0^w R(u,v,s)ds.                   (9)

Subtracting dT changes only a fixed endpoint constant. The remaining
du and dv coefficients have degree at most2 in w. Write them as

    P0(u,v)+w P1(u,v)+w^2 P2(u,v),
    Q0(u,v)+w Q1(u,v)+w^2 Q2(u,v).                      (10)

The terms involving w vanish on the candidate last-activation path.
A sufficient full-source condition is that the four polynomials

    P1, P1+P2, Q1, Q1+Q2                               (11)

are nonnegative on the unit(u,v) square. Then P1+wP2 and Q1+wQ2
are nonnegative for every w in[0,1], so every competing monotone
path pays a nonnegative additional support cost. Combining(11)
with the planar support solution(8) and the original Gram identity
proves a global source minimum. This is a sufficient cone; a failed
polynomial certificate does not disprove the candidate minimum.

The polynomial degrees are bounded independently of H. Exact
Bernstein-coefficient nonnegativity on a declared subdivision, or
a direct low-degree real-algebraic check, can certify(11). Such a
check must use the actual gradient coefficients and retain failure;
no new numerical claim is made in this proof-only note. This gives
a concrete next experiment beyond the H25 minimum without assuming
the smaller moment quotient continues to hold.
