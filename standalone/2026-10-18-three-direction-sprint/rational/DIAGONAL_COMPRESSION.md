# Complete native-source compression to nearby balanced old inputs

Status: **PROPOSED component theorem. The remaining balanced source is
not bounded here. No improved zeta boundary or RH is claimed.**

This extends `GLOBAL_TRANSPORT.md` from one positive prime sector to the
ENTIRE signed original source. It gives an error energy strictly below
the currently imported native energy exponent, while preserving the full
physical output interval and every old product. The new coefficients are
explicit pair weights; they are not arbitrary denominator contractions.
In particular an original aggregate zero need not remain zero.

**Later strengthening:** `FLUX_COMPRESSION.md` replaces the power error
below by a subpower error, using the SAME source and projections. The
elementary power proof here remains valid and supplies the full reference
coefficient, boundary and small-core details used by that strengthening.

## 1. Precise theorem

Use the source and conventions of `PROOF.md` Section 1. Thus

    z_Y(d)=sum_(ab=d,a,b<=Y) mu(a)mu(b),
    C_Y(q)=sum_(q|d,d<=Y^2)z_Y(d)/d,
    R(u)=H_floor(u)-log(u)-gamma,
    R(x/d)=sum_(q|d)S_q(x), S_1=R.

The strict native cells are Y+1<=k< (Y+1)^2, grouped in the actual
annuli I_j with left endpoints K_j=2^j(Y+1) and shortened last annulus.
Put Q_j=floor(K_j^rho), with FIXED 1/2<rho<4/7. Define

    V_Y(k)=sum_(q>Q_j) C_Y(q)S_q(k), k in I_j.                    (1)

For every sufficiently large Y there is an explicit rational old-pair
source

    B_Y(x)=sum_(a,b<=Y) w_Y(a,b)mu(a)mu(b)/(ab) R(x/(ab)),       (2)

where w_Y is symmetric. Its nonzero unordered pairs have squarefree
inputs and, written with a<b, satisfy

    a<b, |a-b|<=C(ab)^(1/4),
    |w_Y(a,b)|<<_epsilon (ab)^(1/4+epsilon),                     (3)

and defined in Section 2 below from the ACTUAL signed z_Y. Write
D_Y(q)=sum_(q|ab)w_Y(a,b)mu(a)mu(b)/(ab), with all old pairs retained,
and B_Y^large(k)=sum_(q>Q_j)D_Y(q)S_q(k). Then

    ||V_Y-B_Y^large||_2^2 <<_(epsilon,rho) Y^(14/33+epsilon).    (4)

The norm is over ALL strict native cells. There is no reciprocal
sign-crossing assumption. For any fixed subpower schedule S(Y), the
same estimate holds after applying the exact extra mask core(q)>S(Y)
to BOTH sides. More quantitatively, the additional root cost for this
extra projection is at most

    Y^epsilon H_S^5 [sqrt(S)H_Y+S],                              (5)

for every epsilon>0, in addition to the displayed full-source error.
The proof allows the exact native q>Q_j mask and coherent cross terms.

The theorem compresses a hyperbolic old-pair population into a strip
around the diagonal. The weights in that strip retain the full signed
arithmetic z_Y; estimating that source remains the open problem.

## 2. Definition of every transported coefficient

Discard first d<=floor(sqrt(Y)); their contribution to (1) is EXACTLY
zero for large Y, since q|d implies q<=sqrt(Y)<Q_j. Put in a separate
corner source all old products

    d>Y^2-20Y^(3/2).                                             (6)

For the remaining products use the integer dyadic blocks D<=d<2D,
D a power of two, and write X=sqrt(D). Then X is between a constant
times Y^(1/4) and Y. On each block |z_Y(d)|<=tau(d)<<_epsilon X^epsilon.
Zero z_Y(d) is simply a zero signed transport mass; no individual
old-pair sign has been replaced by an independent variable.

Fix 0<eta<1/20, let H_X=ceil(X^(1/5+eta)), and let
G_X=ceil(C sqrt(X)H_X) for a sufficiently large absolute constant.
For every target integer d in this block, put r=floor(sqrt(d)),

    T=(r+1)(r+2)-d,
    k_0=max{k>=0:k(k+1)<=T},
    a_k=r+1-k, b_k=r+2+k, k_0<=k<k_0+H_X.                       (7)

The elementary geometry of `GLOBAL_TRANSPORT.md` Section 2 gives

    cX<=a_k<b_k<=CX, |a_k-b_k|<=C sqrt(X),
    |a_k b_k-d|<=G_X.                                           (8)

All inputs are <=Y: away from the top corner, sqrt(d)<=Y-10sqrt(Y),
whereas b_k<=sqrt(d)+C sqrt(sqrt(d))+H_X+O(1)<Y for large Y. For
smaller d the same assertion follows directly from (7). All inputs
are positive, and a_k+b_k=2r+3 is odd.

Let G_d be ALL pairs in (7) for which both inputs are squarefree,
and let g_d=|G_d|. Tolev's uniform short-interval count, with the exact
primary source and hypotheses given in `GLOBAL_TRANSPORT.md` Section 2,
gives g_d>=H_X/5 for sufficiently large Y. It is uniform here because
X>=cY^(1/4) tends to infinity and both input intervals have location
comparable to X. Their densities each exceed 3/5; pigeonhole gives
the intersection. No conditioned parity or squarefree correlation
theorem is needed. All shared input primes are allowed.

Define the block source and its balanced reference source by

    A_X(x)=sum_d z_Y(d)/d R(x/d),
    B_X(x)=sum_d z_Y(d)/(d g_d) sum_((a,b) in G_d)R(x/(ab)),
    W_X=A_X-B_X.                                                 (9)

Sum B_X over all blocks to obtain (2). Each target has reference
probability one, so W_X has exactly zero total R coefficient. Its
canonical expansion therefore has no q=1 term.

For a fixed unordered reference pair (a,b), at most 2G_X+1 integer
targets can use it. Thus its ABSOLUTE R coefficient is at most

    sum_d |z_Y(d)|/(d g_d)
      <<_epsilon X^epsilon G_X/(X^2 H_X)
      <<_epsilon X^(-3/2+epsilon).                              (10)

The equivalent ordered input weight is explicitly

    w_X(a,b)=mu(a)mu(b)ab/2
                sum_(d:(a,b) in G_d) z_Y(d)/(d g_d).             (11)

Equation (10) proves (3). Since ab is comparable to D, only a bounded
number of adjacent product blocks can contribute to any fixed pair.
Oppositely signed target masses are added exactly, not estimated as
though they had a common sign. For upper bounds (10) deliberately uses
their absolute values.

## 3. A global modulus for two nearby R dilations

If 0<N<=M, Delta=M-N<=N/2, then

    integral_0^infinity |R(x/N)-R(x/M)|^2 dx
       << Delta[1+log(N/Delta)],                                (12)

with the zero difference understood when Delta=0. This estimate pays
the entire physical tail and does not use a truncated harmonic model.

Indeed the difference equals log(N/M) plus

    sum_(j>=1) j^-1 1_[jN,jM)(x).

Up to L=N^2/(2Delta), these jump intervals are disjoint: jDelta<N
for every interval beginning below L. Their squared integral is at
most Delta H_floor(N/(2Delta)). The constant logarithm costs at most
L(Delta/N)^2<=Delta/2, and a factor two pays its cross term. For the
remaining tail use |R(u)|<=1/u, valid for every u>0. For u>=1 this
is the elementary harmonic remainder estimate; for u<1 it follows
from -log u<=1/u-1 and 0<gamma<1. Consequently the tail is at most
(N+M)^2/L<<Delta. This proves (12).

The total absolute target mass in a block is
sum_d |z_Y(d)|/d<<_epsilon X^epsilon. Applying Minkowski to (12),
including the probability average, gives the first complete bound

    ||W_X||_L2(0,infinity) <<_epsilon X^(g/2+epsilon),
    g=7/10+eta.                                                 (13)

## 4. A second bound using every harmonic jump at the native horizon

At 0<x<=2Y^2 the log difference in (9) is
O_epsilon(X^epsilon G_X/X^2). In the harmonic part, an index j can
contribute for a given target d only if |d-x/j|<=G_X. At each fixed
x,j there are at most 2G_X+2 such integer targets. Their signed
coefficients have absolute value O_epsilon(X^(-2+epsilon)). The index
range is j<=CY^2/X^2. Summing the complete harmonic weights 1/j gives

    |W_X(x)|<<_epsilon X^epsilon(G_X+1)X^-2(1+log Y),
    ||W_X||_L2(0,2Y^2)
           <<_epsilon Y X^(g-2+epsilon)(1+log Y).                (14)

This argument uses distinct integer d, rather than claiming their
factorizations are unique. The multiplicity |z_Y(d)| has already
been paid by tau(d). It covers every harmonic jump, however many
j occur for the smaller product blocks.

For X>=1,

    min(X^(g/2),Y X^(g-2)) <=Y^(g/(4-g)).                        (15)

Split at X=Y^(2/(4-g)) to verify (15). The sum of the O(log Y)
block root norms therefore has squared size

    <<_epsilon Y^(2g/(4-g)+epsilon).                            (16)

For any requested final epsilon, choose the fixed positive eta and
the divisor-bound losses sufficiently small. Since
2(7/10)/(4-7/10)=14/33, (16) gives the exponent in (4).

## 5. The complete low-denominator projection

A bound on W_X alone would not pay the native projections. We now
give a resource for ALL coefficients, including shared input primes.
For an arbitrary fixed old-pair mask |v_ab|<=1, expansion of the
divisibility conditions gives

    |q C_v(q)|<=H_Y^2 a(s), q=r^2s,
    a(s)=product_(p|s)(2+1/p).                                  (17)

To see the H_Y^2 factor explicitly, assign each p|s to a only,
b only, or both. The both assignment has an additional reciprocal
p. The square r divides both inputs. After dropping coprimality,
the two remaining reciprocal sums are each at most H_Y. Thus
the target part of (9), including its product mask, has resource

    sum_(q<=Q)q^2|C_target(q)|^2<<Q(1+log Y)^C.                 (18)

Here a(s)^2<=d_7(s), and ordinary divisor summation suffices. No
masked Tao cancellation is asserted for this arbitrary product mask.

For references, repeat the SHARP strip count in `GLOBAL_TRANSPORT.md`
Section 5 with Y replaced by X and strip width Csqrt(X). Together
with (10), it gives, for squarefree coprime r,s,

    |D_X(r^2s)|<<_epsilon X^epsilon d_3(s)
                    [1/(r^2s)+1/(sqrt(X)r sqrt(s))].            (19)

In detail s=uvw, ruw|a,rvw|b, and the number of pairs is at most

    C X^(3/2)/(q w)+CX/[r w max(u,v)].

Since w max(u,v)>=sqrt(s), the boundary term yields exactly the
second term of (19). It cannot be discarded. Every reference product
is <=CX^2, so with Q'=min(Q,CX^2),

    sum_(q<=Q)q^2|D_X(q)|^2
       <<_epsilon X^epsilon [Q'+(Q')^2/X](1+log Q')^8
       <<_epsilon Y^epsilon Q^(3/2)(1+log Y)^8.                 (20)

The last inequality follows from X>=c sqrt(Q') and Q'>=1.
It is valid even when Q exceeds the entire product support. Summing
the O(log Y) product blocks costs only another fixed logarithmic
power by Cauchy; targets obey the cheaper (18).

For ANY fixed coefficients b_q the complete Abel/Gram resource in
`GLOBAL_TRANSPORT.md` (14) is

    sum_(K<=k<2K)|sum_(2<=q<=Q)b_q S_q(k)|^2
     <<(1+log Q)(1/K+Q^2/K^2)sum_q q^2|b_q|^2.                 (21)

This includes the full reciprocal Abel remainder and prime-power
centerings. On the actual native annuli, (20)--(21) give

    <<_epsilon Y^epsilon
       [K^((3/2)rho-1)+K^((7/2)rho-2)].                        (22)

Both terms decrease for 1/2<rho<4/7. Summing every annulus, including
the shortened last one, costs

    <<_epsilon Y^(-delta_rho+epsilon),
    delta_rho=min(1-(3/2)rho,2-(7/2)rho)>0.                     (23)

For rho=13/24 one can take delta_rho=5/48. All coefficient vectors
are fixed after Y is fixed; no output-dependent weight is put into
a fixed-coefficient sieve.

## 6. All small squarefree cores, with the actual moving mask

The target product-mask bound (17), the global mode norm
||S_q||_2<=sqrt(3q)beta(q), and the proof in `PROOF.md` Section 6.2
give root cost O(H_Y^3 sqrt(S)H_S^3). For references, every r divides
gcd(a,b) and hence |a-b|, so r<=C sqrt(X). From (19) the complete
root cost, with arbitrary actual q>Q_j indicators, is at most

    X^epsilon sum_(s<=S)^flat d_3(s)beta(s)
       [s^-1/2 sum_(r<=Csqrt(X))beta(r)/r
                         +X^-1/2 sum_(r<=Csqrt(X))beta(r)]
      <<_epsilon X^epsilon H_S^5[sqrt(S)H_Y+S].                 (24)

We used sum_(r<=R)beta(r)/r<<H_R,
sum_(r<=R)beta(r)<<R, and d_3(s)beta(s)<=d_6(s) for squarefree s.
Dropping coprimality only increases this positive majorant. Summing
all blocks absorbs logarithms into Y^epsilon and proves (5). Thus
the small-core assertion does not omit squares, shared prime squares,
cross terms, or modes above a physical cell.

## 7. Low products, top corner, and the full exact remainder

The low-product source d<=floor(sqrt(Y)) has zero native large-
denominator projection, as observed in Section 2, even with the
additional core mask.

If ab is in (6), with a,b<=Y, then both inputs exceed Y-20sqrt(Y).
There are O(Y) ordered integer pairs there. Each coefficient has
absolute value <=1/(ab), and ||R(x/(ab))||_L2(0,infinity)
<=sqrt(3ab). The full corner root norm is therefore O(1).
Its q=1 coefficient is O(1/Y), whose R norm is also paid. Apply
(17)--(18) and (21) to its actual fixed product mask to pay its
complete low-denominator projection. Its additional small-core
cost is O(H_Y^3 sqrt(S)H_S^3). Thus the whole corner costs Y^o(1)
for a fixed subpower S schedule, and O(1) plus a decaying resource
when no small-core projection is made.

For each transported block W_X has zero q=1 coefficient, so its
native large-denominator projection is W_X minus exactly its low
denominators. Equations (16), (23), and the corner estimate prove
(4). Inserting the actual core mask adds (24) and the target/core
costs just proved. The discrete norm equals the norm on the complete
constant extension to [Y+1,(Y+1)^2); all endpoints are integral.

## 8. The remaining contraction target and the exact exponent budget

The error exponent 14/33 is a bound for a COMPLETE source difference,
not for B_Y^large itself. It is smaller than the imported energy
benchmark kappa_0=2B_0-1 approximately 0.749914. Consequently an
estimate for the ACTUAL source (2) of the form

    ||B_Y^large||_2^2 <<_epsilon
         Y^(a+epsilon)(1+F_Y)^p, 1<=p<2,                         (25)

would be useful when a<(2-p)kappa_0: at exponent kappa_0, the
native source energy is bounded by the larger of a+p kappa_0 and
14/33. Neither term has been estimated away by definition.

For example a=1/3,p=3/2 would give the open target exponent
35/24 at scale Y, or 35/48 at scale Y^2; the compression error
14/33 at scale Y is much smaller. These are hypothetical arithmetic
consequences. This file does not prove (25).

The exact all-prefix/cofinal exponent theorem imported by #994
from #848 says that lim log(1+F_Y)/log(Y+1)=kappa at EVERY prefix,
with kappa=2Theta-1. It can therefore be used at both the explicitly
retained native crossings Y and their endpoints (Y+1)^2-1. Together
with #994's complete native-energy comparison, it would turn (25) into

    2kappa <=max(a+p kappa,14/33),
    kappa<=max(a/(2-p),7/33).                                  (26)

This uses that SOURCE THEOREM, not a false all-Y recurrence deduced
from unspecified sparse cuts. The elementary Mellin implication then
would exclude zeta zeros with real part greater than

    [1+max(a/(2-p),7/33)]/2.                                   (27)

The different ALL-Y recurrence theorem in #1002 `NEWTON_BUDGET.md`
at 1319373815ee408146705b25a426fba6b22ed755 is compatible with this
budget, but its all-Y premise is not obtained merely from crossing
identities. Its original-source adaptive core cutoff cannot be
transferred without paying the new source's small-core resource (24).
For B_Y itself (24) permits a separate cutoff of order sqrt(G_Y)
up to divisor and logarithmic losses if a root budget sqrt(G_Y) is
available. The stronger original-source cutoff of order G_Y is not
claimed for these new coefficients.

The balanced weights (11) are deterministic local averages of
z_Y(d)/d. Treating them as independent bounded coefficients would
throw away the only currently visible arithmetic cancellation.
The remaining task is an estimate for this specified complete source,
not a bound uniform over all weights satisfying (3).
