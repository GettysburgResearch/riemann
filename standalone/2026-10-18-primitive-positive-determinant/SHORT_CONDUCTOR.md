# Square-root-conductor prime bias and a positive complex-zero budget

Status: PROPOSED complete component deductions, awaiting independent mathematical
review. The complex-zero conclusion is a conductor-scaled LOW-HEIGHT statement
near s=1. It is not RH or a new fixed all-height zero-free half-plane.

Exact parent: #993, 5569defd8d77f1f8f3586b326577aacb384ffb23,
RECTANGULAR_JETS.md. Its independent ordinary-jet rank lemma, full Frobenius
row reduction and exact valuation lower template are the inherited algebraic
inputs. Their proofs were read and the original finite replay was rerun.
That replay does not certify the infinite arguments. The supplied note's
printed author attribution remains independently unauthenticated.

## 1. A finite explicit prime-bias statement below the conductor

Let chi be primitive, nonprincipal and real of conductor q>=3, associated
to Q(sqrt(d)) with d squarefree and D=|d|<=q. For an integer R set

    B=ceil(log(2R)), S=J=floor(R/B),
    a=ceil(2sqrt(R)D^(1/4)), b=ceil(2sqrt(R)D^(-1/4)),
    H=a+b sqrt(D), P=ceil(R/S), alpha=1-1/R-1/(2S).

### Theorem 1

For every integer R>=16 satisfying

                         R>=64sqrt(q) B^2,              (1)

one has

    A_chi(R):=sum_(p<=R,chi(p)=-1)log(p)/p
           <=(1/2)log R+(1/4)log D+4log B+30.            (2)

A sharper finite bound in the proof retains the exact a,b,S and alpha.
In particular, for each fixed eta>0, the same leading bound applies at
R=q^(1/2+eta) for sufficiently large q (use an integer endpoint). The old
#993 statement required R>=q. This changes the accessible SUPPORT RANGE,
not the leading coefficient for the old range and not a zeta-strip coordinate.

### Complete parameter check

Condition (1) gives R>=64B^2 and
D^(1/4)<=sqrt(R)/(8B). Hence B>=4 and

    a<=R/(4B)+1<=R/(2B)<=S, b<=a,
    4R<=ab<=9R, S<=R/4, H<=6sqrt(R)D^(1/4).             (3)

For example ab<=4R+2sqrt(R)(D^(1/4)+D^(-1/4))+1<=9R,
and H<=4sqrt(R)D^(1/4)+1+sqrt(D)<=6sqrt(R)D^(1/4).
The floor bound S>=R/(2B) uses R>=2B. Also S>=B; writing R=BS+r,
0<=r<B, gives P<=B+1<=2B. These facts retain both ceilings and the floor.

In the actual rectangular quadratic grid there are ab points, incidence
parameter M=a, and ordinary z-jet depth J=S. The inherited sufficient rank
condition is

    Jab > M(R+S)+2RS+(J-M)_+S.

By M<=S, its right side equals MR+2RS+S^2<=3RS+S^2<4RS,
whereas the left side is at least 4RS. Thus the Gram matrix is nonsingular.
The trace-expanded quadratic form is positive and integral for both signs
of d, so its Gram determinant G is a positive rational integer. This is
the SAME ordinary-jet construction as in the parent; Hasse jets are not used.

Hadamard's complete finite bound, with both embeddings and all abJ columns,
is

    log det G<=RS log(2abS)+2RS(S-1)log R
                                  +RS(R+S-2)log H.

Write its normalization by SR^2 as

    T=log(2abS)/R+2(S-1)log R/R+(R+S-2)log H/R.          (4)

## 2. All prime ranges and an explicit constant

For each inert odd prime p, the full unipotent row reduction in #993 gives

    v_p(det G)>=E_p(R,S),
    E_p=2sum_(h=1)^K(R-ph)(S-h),
    K=min(floor((R-1)/p),S-1),
    E_p/(SR^2)>=alpha/p-2/R-R/(3S p^2).                 (5)

These are lower bounds, not asserted equalities for actual valuations.
Ordinary derivatives of z^p-w are p-divisible at EVERY order, so J may
exceed p. All terms from the complete coefficient rectangle remain.

For completeness, the elementary bound theta(x)=sum_(p<=x)log p<=4x
holds for x>=1. For integer N, all primes ceil(N/2)<p<=N divide
binom(N,floor(N/2)), giving theta(N)<=theta(ceil(N/2))+Nlog 2.
Induction, starting at N=1, yields the stated loose bound. Partial summation
therefore gives

    sum_(p>=P)log p/p^2<=8/P,
    sum_(p<P)log p/p<=4+4log P.                          (6)

Sum (5) over inert P<=p<=R and compare the resulting positive divisibility
with (4). Since R/(SP)<=1 and all these primes are odd,

    alpha sum_(P<=p<=R,chi(p)=-1)log p/p<=T+32/3.

Thus the fully explicit intermediate result is

    A_chi(R)<=(T+32/3)/alpha+4+4log P.                   (7)

The small primes, including p=2, have not been silently given a large-prime
valuation weight.

To obtain (2), put L=(1/2)log R+(1/4)log D. Conditions (1)--(3) imply
L<=log R<=B and

    T<=L+7, T<=B+7,
    1-alpha<=2B/R<=1/(32B), alpha>=127/128.

Indeed log H<=L+log 6, (S/R)log H<=(B+2)/B<=3/2,
2(S/R)log R<=2, and log(2abS)/R<=(3+2B)/R<1.
Furthermore T(1/alpha-1)<=4(B+7)/(127B)<1. Consequently
(T+32/3)/alpha<=L+19. Since P<=2B, (7) is at most
L+4log B+26, which is stronger than (2). This proves Theorem 1.
All constants in this finite prime-sum bound are explicit. QED.

## 3. Retaining the full transition scale improves the Laplace input

Put ell=log q. Theorem 1 begins at square-root-conductor scale with only
logarithmic factors. More precisely, for

    y_q=ell/2+4log(ell+2)+20,

every y>=y_q gives an admissible R=floor(exp y) in (1):
B<=y+2, floor(exp y)>=exp y/2, and
exp(y_q)>=128sqrt(q)(y_q+2)^2. The latter follows, for ell>=log3,
from y_q+2<=16(ell+2) and exp(20)>2^20. The ratio exp y/(y+2)^2
is increasing there.

For y>=y_q, (2) gives
A_chi(exp y)<=y/2+ell/4+4log(y+2)+30. Below this threshold use the
classical elementary Mertens estimate sum_(p<=x)log p/p=log x+O(1).
The narrow interval [ell/2,y_q] costs only O(log(ell+2)). Therefore one
valid global cumulative majorant is

    A_chi(exp y)<=y-(1/2)(y-ell/2)_+
                    +O(1+log(ell+2)+log(y+2)), y>=0.    (8)

The coefficient transition at ell/2 is retained. Replacing the whole
initial range by an unrestricted extra y/2 term would lose the next result.

For 0<t<=1 define the complete inert prime series

    I_-(t)=sum_(chi(p)=-1)log p/p^(1+t)
          =t integral_0^infinity A_chi(exp y)e^(-ty)dy.

Integrating (8) exactly and bounding the logarithmic error by concavity gives

    I_-(t)<=[1-(1/2)e^(-t ell/2)]/t
              +O(1+log(ell+2)+log(2+1/t)).              (9)

No zero-density result or presumed absence of an exceptional character is
an input. The full prime series satisfies P_0(t)=1/t+O(1). All character
prime-power tails of exponent >=2 are absolutely bounded uniformly on this
range. Finally sum_(p|q)log p/p=O(1+log(ell+2)): split at p=ell and use
Mertens below, and sum_(p|q)log p<=ell above. Hence

    -L'/L(1+t,chi)>=-(1-e^(-t ell/2))/t
                  -O(1+log(ell+2)+log(2+1/t)).         (10)

These classical Dirichlet-series identities and the next Hadamard identity
were re-read from the original pinned OpenAI TeX, Section 'The prime bias
forced by a real zero', equation eq:hadamard. They are not new theorems,
and that source's no-Siegel-zero conclusion is not assumed.

## 4. A positive budget for ALL nontrivial zeros, including complex ones

The classical completed Dirichlet Hadamard formula, at real 1<s<=2, is

    -L'/L(s,chi)=(1/2)log(q/pi)
       +(1/2)Gamma'/Gamma((s+parity)/2)
       -sum_rho Re[1/(s-rho)].                          (11)

All zeros are counted with multiplicity, the real-part sum converges,
and every summand is positive. The gamma term is bounded uniformly for
both parities in this range. Keep the ENTIRE sum, not just a real zero.
Combining (10)--(11), for every fixed tau>0 and t=tau/ell, proves:

### Theorem 2

Let u_rho=(1-Re rho)ell and v_rho=(Im rho)ell. As q tends to infinity,

    sum_rho (tau+u_rho)/[(tau+u_rho)^2+v_rho^2]
       <= B_zero(tau)+O_tau(log ell/ell),
    B_zero(tau)=1/2+(1-e^(-tau/2))/tau.                 (12)

The error is uniform for tau in compact subintervals of (0,infinity).
This is a bound for one specified real character's full zero multiset,
not a family average. No zero is removed. For the limiting choice
t=ell^(-2), equivalently tau=ell^(-1), the right side is
1+O(log ell/ell), by the explicit error in (10).

For a zero beta+i gamma of multiplicity m, reality of chi supplies its
conjugate when gamma!=0. Consequently (12) implies

    2m(tau+u)/[(tau+u)^2+v^2]
            <=B_zero(tau)+O_tau(log ell/ell)             (13)

for a nonreal pair; a real zero has m, not 2m, in the numerator.
Keeping multiplicities and the conjugate count is essential.

For example, along any bounded sequence of scaled coordinates (u,v),
a simple nonreal pair obeys the following asymptotic disk exclusions:

    (u-1)^2+v^2>=1-o(1),                               (14)
    (u-1/9)^2+v^2>=100/81-o(1).                         (15)

Equation (14) uses tau=ell^(-1). For (15), take tau=1 and note
B_zero(1)=3/2-e^(-1/2)<9/10, since e^(1/2)<5/3.
Thus 2(1+u)/[(1+u)^2+v^2]<=9/10+o(1); completing the square gives (15).
The exact exponential expression (13) is a little stronger. On bounded
scaled sets the error is O(log ell/ell). These disks live within distances
of order 1/log q from 1, including heights of that same order. They are
NOT disks of a fixed size in the original s-plane.

For a real zero of fixed multiplicity m, the tau=ell^(-1) version gives
(1-beta)ell>=m-O_m(log ell/ell). For m=1 this recovers the parent's
asymptotic real gap; it is not a new larger simple-real-zero constant.
The new analytic statement is the full positive complex-zero budget.

## 5. Relation to the full-RH route and review obligations

This is a quantitative improvement to the same arithmetic determinant
method: its support begins near sqrt(q), with an explicit prime-sum constant,
and its consequence need not discard complex zeros near the real axis.
It does not control a zero of ordinary zeta at arbitrary height and real
part 3/4. Those primes require the all-prime positive determinant of
POSITIVE_DETERMINANT.md, whose critical one-sided height remains open.

Priority review: the inherited rank lemma for J>M; ordinary-jet Frobenius
compatibility; every ceiling/floor in (1)--(7); the initial conductor range
in (8); full prime powers and ramification in (10); and the positive
Hadamard sum with conjugate multiplicity in (12)--(15). A finite checker
validates substitutions and exact models, not these infinite arguments.
No global literature-priority or best-known-zero-region claim is made.
