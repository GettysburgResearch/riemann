# A complete conditional mixed-witness consumer, with aggregate tuple costs

**PROPOSED component mathematics. No new zero-free region is claimed.**
The arithmetic estimate in (1) below is OPEN. This note proves a concrete
full consumer for it, using the pinned original Eisenstein-field physical
framework. Its balanced geometry and aggregate tuple bookkeeping are
audited here; no priority over existing geometry refinements is claimed. In particular the
consumer covers every witness length, every dynamic/amplitude bin, and
both frequency endpoints. A corner-only threshold is insufficient.

The source is the original OpenAI TeX saved as
`_source-original-quasi.tex`, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
Its full source provenance is in NOTES.md. All references below concern
that exact file. We import its reflection-energy theorem, detector,
selected-prime moments, physical identities, and continuation criterion;
we do not claim to have independently reproved that entire framework.
Only E=Q(omega) is used. No all-number-fields theorem is required.

## 1. The actual all-length arithmetic input

Let the two central polynomials have their native common character,
finite ray twist, orientation and height:

    M_u(D)=D^(-1/2) sum_d mu(d) nu(d) chi_d(u)^sign W_M(Nd/D),
    S_u(N)=N^(-1/2) sum_n       nu(n) chi_n(u)^sign W_S(Nn/N).

Keep all sixth-power-free physical rows u with Nu≈U, all original
nonunit zeros, every power of n, and every shared prime of d,n,u.
The proposed sufficient input is

    sum_(u sixth-power-free, Nu≈U) |M_u(D)S_u(N)|^2
       <<_epsilon U(UDN)^epsilon (1+T)^A,                    (1)

uniformly for the detector's whole common smooth-profile family and

    D=U^r, N=U^m,
    1<=r<=3/2, 0<=m<=1/2, 3/2<=r+m<=2.                      (2)

The displayed polygon is the limiting domain. The actual sufficient
input must also be ROBUST at its boundary: for every sufficiently small
fixed eta>0, assume the same bound with U replaced by U^(1+C eta),
where C is fixed, on

    1-eta<=r<=3/2+eta, 0<=m<=1/2+eta,
    3/2-eta<=r+m<=2+2eta.                                (2a)

The native witness has r>=1-O(preliminary epsilon),
m<=1/2+O(preliminary epsilon), and dyadic support errors O(1/log U).
Choose those preliminary losses and the lower threshold so all witnesses
lie in (2a). The count (3) then has an additional O(eta) term. It is
absorbed into the strict margins below by choosing eta after those
margins. A theorem only on the exact polygon, without this robustness
or another legal boundary reduction, would leave a scope gap.

The rowwise smooth parameters, fixed finite ray twists, and original
masks have precisely the scope in the pinned detector/moment interface.
The order A is fixed before the final small height exponent is chosen.
Arbitrary independently chosen arithmetic coefficients in different rows
are not allowed. Formula (1) is a theorem target, not a result of this
sprint. It includes the difficult long-inverse edge m=0; the existing
inverse exponent e(r)=max(1,(1+5r)/6) does not supply it there.

At detector cutoff t=3/2, the matched witness has squared spike at least
U^(delta(r+m)-epsilon). From (1), Markov and the complete domain (2),

    R_mix(delta)<=1-3delta/2.

For a harmless nonnegative count envelope we may weaken this to

    R_mix(delta)<=max(0,1-3delta/2).                         (3)

This is valid on the WHOLE witness polygon, including the long-inverse
edge and the largest product r+m=2. The rowwise profile/height choices
are handled by the stipulated common Sobolev interface before Markov.

For comparison, the weaker candidate mean `U+D^(2/3)N` would instead give

    R_candidate(delta)<=max(3/2-2delta,7/6-3delta/2).         (4)

For delta<2/3 its maximum occurs at r=3/2,m=1/2, not at the
r=1,m=1/2 corner. Extending the latter corner's branch to all middle
bins is incorrect. The first exploratory .873016667 certificate used
that incorrect extension; it was withdrawn and replaced by the complete
uniform-U consumer here. No result relies on that exploratory number.

## 2. Aggregate rescaled tuples extend the existing low estimate

Choose general physical exponents

    M=1-ell, x=(1-ell-b)/2, y=x+b, h=1-x+ell,
    0<=b, 0<ell<1/3, x>ell, x-ell>=5b/6.                    (6)

For a rescaled subset J of the fixed slot list put
`d=sum_(i in J)ell_i`, `M'=M-2d`, `ell'=ell-d`.
The source's actual residual row length H and powerful part O satisfy
`H<=M'-O+o(1)`. Its proof of `old-eq:5.3`, around lines
8125--8330, uses

    T_d<=H+(M+ell-1)-3d+o(1)=H-3d+o(1).

The two reflected energy branches, before summing H, become

    M'-Delta_H,
    M'+[1+3ell-2M+d-2Delta_H]/4,

up to prescribed small powers. Both decrease with Delta_H>=-o(1).
Therefore the completed-row ENERGY for this subset is at most

    Z^[ M'+((5ell-1+d)/4)_+ +epsilon ].                       (7)

This is the literal source proof with its fixed geometry replaced by
(6); no extra row count is taken after its principal/powerful counts.
The full joint Gaussian profile, all surviving marked slots and all
shared-prime factors remain the ones in that proof.

It is unnecessary to demand that (7) be Z^(M'+epsilon) separately for
every d. In the final physical triangle, the source's `old-eq:5.5`,
around lines 8580--8635, counts ALL rescaled tuples by
Z^(d+epsilon), multiplies their exact coefficient Z^(-3d/2), and has
an X' square-root factor Z^(-d/2). These three factors give -d in the
final physical exponent. Taking the square root of (7) adds only

    -d+(5ell-1+d)_+/8 <= (5ell-1)_+/8.                       (8)

There are finitely many subsets J because the slot count is fixed
before Z. No loss proportional to a moving number of slot tuples is
omitted. The retained joint-profile seminorm and Gaussian tails are
summed exactly as in the source; the length intervals remain compact
for the fixed exponents used below.

The additive Gram theorem is already stated at general Q,Y'. Under
(6), P_a=Y'^2/Q has exponent b and P_a^2/Y'<=P_a^(1/6) uniformly in
all rescaled tuples. For b=0 choose the fixed scale constant
`Y=q_(b_*) X`, so P_a=1 exactly. This avoids applying the source's
P_a>=1 assertion to a fixed constant smaller than one. Such a fixed
constant changes no exponent or target pole.

Cauchy now gives the aggregate low estimate

    |I_modified(Z)|
       << Z^[x/2+b/12+(5ell-1)_+/8+epsilon].                  (9)

The unchanged principal signal has exponent

    C(s)=s-5/6+x/3+ell/6.

Its low-side comparison boundary is consequently

    B_low=11/12-ell/4+(5ell-1)_+/8.                           (10)

For ell<=1/5 the aggregate extra is zero. This audits a general geometry beyond the fixed source's convenient
subsetwise choice ell=1/6. The source-only optimization reproduces the
existing refinement near .874957; this bookkeeping is not presented as
a new zero-free theorem or a priority claim.

## 3. Existing prime counts, floor bin and exact high exponent

Use the imported fixed-field 7/8 bound as the working foundation.
Under a contradiction beta_*>B with B<7/8, take kappa=3/4 in the
source's positive-slot theorem. Its hypothesis
beta_*<=(1+kappa)/2=7/8 holds. The parameter kappa must not be lowered
below its stated range merely because B is smaller.

For a nonfloor bin let delta=2a-1, q=x_amp delta,
0<=x_amp<=1/2. The source's `detector-counts` proposition and its
endpoint optimization, with Delta=0, give

    D_x=3-17x_amp/9,
    P_x=(2-8x_amp/9)(1-x_amp),
    J=(5/6-delta)D_x+delta P_x,
    R_source=1-delta+(5/6-delta)delta P_x/(2J).                (11)

This is uniform when the available prime length ell/d_row exceeds
7/37 with fixed margin. One may take the better of (3) and (11). The explicit conditional
consumer below only needs (3), so it does not depend on applying the
selected-prime count at a new geometry. The floor
a0=51/100, delta0=1/50 has no zero witness and must instead use R=1.

For every retained frequency 0<=d_row<=h, the actual central exponent
relative to C(B) is

    E(d_row)=a-B+h(17/50-1/6)-a y-ell/2+q ell
                 +d_row[R+delta/2-17/50].                  (12)

It is affine in d_row. Therefore checking BOTH endpoints 0,h is a
complete frequency check; no sign assumption on its slope is required.
Every row/amplitude subdivision is made after the original holomorphic
contour move, as in `bin-contour-accounting`. The pointwise choice
between (3) and (11) supplies an upper bound on that retained integral;
it is not a separately continued or integrated arithmetic expression.

## 4. Target and tail interfaces

For every fixed slot list the unchanged principal normalizer is

    A_T(Z)=(-1)^K Z^(-ell/6)
       product_i sum_(p in allowed ray annulus i)
                         W_i(Np/P_i)(Np)^(-5/6).

The fixed-ray prime ideal theorem gives A_T asymptotic to a nonzero
constant times (log Z)^(-K). Deleting the finite S set affects only
the lower threshold. The full local compensated identity is unchanged.
At the principal residue its local ratio is -1 plus a power-decaying
error on any closed strip near the proposed B>.86. Explicitly, put
`d_p=Q^(-s)`, `R_p=kappa(p)Q^(3-6s)` and
`A_p=1-(1-Q^(-1))d_p-R_p/Q`. The exact original local series gives

    B_p+1=(1-Q^(-1))
       [Q^s R_p-(1-Q^(-1))d_p-R_p/Q]/A_p.

The same local contraction makes A_p nonzero and, for sigma>=3/4,
`B_p+1=O(Q^(-sigma))`. On the full principal extraction rectangle
sigma>=.86,w>=.95,z>=33/200, the absolute remainder exponents include
`4-6sigma-6z<=-2.15` and `-(sigma+w)<=-1.81`.
Thus its quotient-free local product and height bounds retain strict
convergence margins below the source's convenient 7/8 rectangle. The complete
principal H factor has the same elementary Euler proof as H_FACTOR.md,
with the OLD source's own phase `kappa(p)=bar alpha(p)^6`:

    H_p(s)=(1-Q^(-2))
       [1-(1-Q^(-1))Q^(-s)-kappa(p)Q^(2-6s)]
       /[(1-kappa(p)Q^(3-6s))(1-Q^(-s))].

The numerator never vanishes for Re s>1/2 because
`(1-Q^(-1))Q^(-1/2)+Q^(-1)<1`; the remaining regular product
converges normally there after extracting `L_E^S(6s-3,kappa)`.
In Re s>2/3 that L-function is in its absolutely convergent,
nonzero Euler domain. This argument uses the old legal E source and
makes no mu_12 field substitution. Hence H is nonzero in the needed
half-plane. Thus the
normalizer and H retain every zero of zeta_E, including every ordinary
zeta zero through zeta_E=zeta L(s,chi_-3). Extra auxiliary zeros do not
cancel a target zero. The Gaussian and radial principal scalar are
unchanged and nonzero.

For small rows the source's absolute correction bound gives the margin

    h(17/50-1/6)-y/2+(63/50)d_min,                            (13)

with fixed small d_min>0. Large rows beyond h+zeta are controlled by
a sufficiently large absolute z contour. The principal leftover w and
z contours have positive margins y/20 and h/600. These are the same
source interfaces at the new fixed geometry; all height orders are
fixed before the final small height power, and all normalizer logarithms
are absorbed only after strict margins have been reserved.

## 5. An explicit full consumer for the open row-size mean

Take

    ell=3/16, b=0, x=y=13/32, h=25/32,
    B_*=167/192=0.869791666666... .                           (14)

All rescaled lengths are positive, the Gram scale is fixed at one as
explained above, and ell<1/5, so (9) has low exponent 13/64.
The principal exponent is C(s)=s-2/3 and C(B_*)=13/64.

For every nonfloor bin, q<=delta/2 and (12) at d_row=h imply

    E(h)<=1/6-ell/2-B+h[delta+max(0,1-3delta/2)].             (15)

On the ENTIRE interval 1/50<=delta<=3/4, the bracket is at most 99/100:
it decreases linearly from 99/100 to 2/3, then increases to 3/4.
At B=B_*+1/10000, (15) is at most -1883/80000.
At d_row=0, using the imported ceiling a<=beta_*<=7/8 rather
than incorrectly assuming a<=B, a direct endpoint bound is

    E(0)<=h(7/8+17/50-1/6)-B-ell
         =-38141/160000.                                  (16)

These two endpoint estimates cover all intermediate frequencies even
where their coefficient changes sign. The floor bin, which has no
witness, is bounded separately with R=1 and q<=delta0/2. At (14) its
upper exponent is exactly B_*-B, hence -1/10000 at the explicit value.
This is the binding high constraint. Equating this floor boundary with
(10) gives ell=3/16 and B_*=167/192 in the balanced family; silently
applying the zero witness to the floor would give an incorrect answer.

With d_min=1/100 the small-row margin (13) is
-6613/120000. Large rows and principal leftovers retain the positive
margins described in Section 4. The available selected-prime supply,
although not needed for (15), exceeds 7/37 by 47/925.

All these are strict rational margins. Choose the length-neighborhood eta and a small retained-row
extension zeta>0 after them; then choose detector buffers, amplitude
mesh, arithmetic output powers, and external height exponent so their
finite total loss is smaller than a fixed fraction of the minimum
margin. Choose the absolute outer contour after zeta and fix each tail
order after its corresponding finite polynomial bound. The fixed
normalizer has only logarithmic inverse growth. This is the source's
usual ordered choice of losses and does not renew height allowances.

Conditional on the OPEN uniform row-size estimate (1) and the pinned
source interfaces, the continuation criterion therefore excludes target
zeros to the right of 104387/120000=0.869891666666... . The same algebra
with an arbitrarily small strict excess above B_* yields the conditional
boundary B_*=167/192. This would beat the reported ordinary-zeta working
benchmark near .874957, but (1) has NOT been proved here.

The complete normalized physical principal function is still
`H(s)/zeta_E^S(s)` times a nonzero Gaussian/radial scalar and the
nonzero logarithmic prime normalizer. Every ordinary zeta zero is
retained. No all-number-fields requirement enters this conditional
consumer. It does still require the whole fixed-field nonprincipal-row
analytic family introduced by Poisson.

## 6. Exact checks and present status

`mixed_consumer_check.py` runs with exact rational arithmetic and uses
runtime checks which remain active under Python -O. Normal and optimized
runs both pass. It checks the complete piecewise-affine delta envelope,
all rational physical margins in (14)--(16), 20,301 aggregate tuple
inequalities, and 151 full-polygon checks of the weaker candidate (4),
including the middle-bin regression that caught the withdrawn corner
extrapolation. `MIXED_CONSUMER_CHECKS.json` records the final values.
The analytic inequalities in this note, not a sampled parameter grid,
supply the continuum argument.

The arithmetic mixed mean (1) is still open. Bounds for one flat Gauss
probe, the low-conductor form, or the complementary bare coefficient
projection do not supply it. Existing source-only count optimization
recovers the earlier refinement and supplies no improvement over the
reported Liu v2 benchmark. No unconditional boundary is claimed.
