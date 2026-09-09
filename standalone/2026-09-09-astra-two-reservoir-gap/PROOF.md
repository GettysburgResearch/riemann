# TRG26: a sharp centered spectral-gap obstruction on genuine divisor-closed supports

Date: 2026-09-09. Author: Astra.
Status: proposed component theorems with complete paper proofs; independent review pending.
This is NOT a proof of RH. No bound for the native prime discrepancy or the intrinsic
zeta-domain defect is obtained. The new conclusion concerns the literal prime-power
arithmetic graph, not an operator asserted to have the zeta zeros as its spectrum.

Parent source: PR828 at 528b33ac8d57b5a046260ee45d585cd3fe720f4c. The previous
packet solved ANCHORED costs on product reservoirs but explicitly left open the
sharp order of CENTERED gaps on arbitrary divisor-closed supports. We resolve that
order here. Classical finite spectral decomposition, Schur reduction and min-max
are used with their complete needed calculations. No PNT, RH or zero census is used.

## 1. Unchanged graph and the new theorem

For a finite divisor-closed set S of positive integers let

    ||f||_S^2 = sum_(n in S) |f(n)|^2/n,
    E_S(f) = sum_(p prime, k>=1, j p^k in S)
                    (log p)/(j p^k) |f(j p^k)-f(j)|^2.       (1)

The self-adjoint generator is taken in this harmonic metric. Equivalently, in
Euclidean coordinates v_n=f(n)/sqrt(n), it is exactly the earlier matrix D-C.
All allowed prime powers are retained. Let gamma(S) be its smallest positive
eigenvalue, or the optimal centered gap:

    gamma(S) = inf_(f nonconstant) E_S(f)/min_c ||f-c||_S^2.

Our example will be squarefree, so no powers k>=2 are permitted by its support.
This is not the deletion of edges from an otherwise unchanged support.

Write Z(P)=product_(p<=P)(1+1/p). For real P>=17, let Q=Q(P) be the largest prime
such that

    Z(Q)^3 <= Z(P).                                          (2)

This is a finite rational comparison, not a choice using a zeta zero. Set

    A={primes p<=Q}, B={primes Q<p<=P},
    S_A={squarefree products of primes in A},
    S_B={squarefree products of primes in B},
    S(P)=S_A union S_B.

Each set is divisor closed. The two boxes intersect ONLY at 1. Both alphabets
are nonempty for P>=17, since Z(17)=41472/12155>27/8 and Z(P)>1. Denote their masses by
Z_A=Z(Q), Z_B=Z(P)/Z(Q), so the union has mass Z_A+Z_B-1.
The union is NOT their Cartesian product and is NOT the ordinary cutoff n<=N.

**Theorem TRG26.T1 (sharp centered order).** As P tends to infinity through all
real cutoffs,

    gamma(S(P)) = 3 zeta(2)/log log P + O((log log P)^(-2)).    (3)

Every eigenvalue after the zero eigenvalue and this first positive one is at least

    g0=(3/2)log 2.                                           (4)

Thus there is precisely ONE additional slow mode; the rest of the centered
operator has an absolute gap. The asymptotic constants are not numerically
instantiated. The graph is finite at each P, even though its size can be enormous.

Combining (3) with the all-support upper bound proved in Section 7 gives

    sup_(finite divisor-closed S, primes(S)<=P) 1/gamma(S)
                              = Theta(log log P).           (5)

Singleton supports are omitted from the supremum. In particular the log-log loss
cannot be removed from the CENTERED theorem over the stated all-support class.
This does not establish deterioration for S={1,...,N}; that narrower case remains
unsettled here. It also does not contradict constant gaps on product boxes.

## 2. Exact two-reservoir equation at every finite alphabet

For ANY two disjoint nonempty finite prime alphabets A,B, retain their squarefree
boxes and union as above. Put

    a_p=(1+1/p)log p,
    lambda_D=sum_(p in D) a_p,
    n_D=product_(p in D) p,
    K_i(lambda)=sum_(empty != D subset i) 1/[n_D(lambda_D-lambda)],
    G_i=K_i(0),           i=A,B,
    g=min_(p in A union B) a_p.                             (6)

There are finitely many terms; coincident lambda_D remain separate terms. No
assumption of linear independence of log primes is made. For 0<lambda<g define

    F(lambda)=Z_A+Z_B-1
      -lambda[(Z_A-1)K_B(lambda)+(Z_B-1)K_A(lambda)]
      -lambda^2 K_A(lambda)K_B(lambda).                    (7)

**Theorem TRG26.T2 (exact full-graph reduction).** The centered gap of the UNION
is the unique root of F(lambda)=0 in (0,g). Every other positive eigenvalue is
at least g. Formula (7) retains the common vertex's mass exactly ONCE.
It is valid even when the two root-killed resolvents have a simultaneous zero.

### 2.1 Each product box, with its actual metric

For one prime p, the values f(0),f(1) have masses 1,1/p. The generator is

    (L_p f)(0)=(log p)/p [f(0)-f(1)],
    (L_p f)(1)=(log p)   [f(1)-f(0)].

Its eigenvalues are 0 and a_p. In its probability metric the normalized nonconstant
vector is -1/sqrt(p) at 0 and sqrt(p) at 1. Finite tensor products give a complete
orthonormal probability basis u_D of a box, with eigenvalues lambda_D and
u_D(1)^2=1/n_D. The constant is u_empty=1. Since a_x has derivative (x+1-log x)/x^2>0 for
x>=2, a box containing prime 2 has gap g0. This directly reproduces the squarefree
part of DPG26/GCP26 rather than assuming its extension to a union.

Let e_1 be 1 at the root and zero elsewhere. In the unnormalized harmonic metric
its norm is 1. For 0<lambda<g the FULL box operator L_i-lambda I is invertible,
and its root resolvent value is

    r_i(lambda)=[(L_i-lambda I)^(-1)e_1](1)
               =[-1/lambda+K_i(lambda)]/Z_i.                (8)

The factor Z_i in (8) is essential. The probability and unnormalized generators
have the same eigenvalues, but their normalized evaluation vectors differ.

### 2.2 Gluing, without an invalid inverse at a Dirichlet pole

A union eigenvector with eigenvalue lambda in (0,g), restricted to box i, satisfies

    (L_i-lambda I)f_i=c_i e_1

for some scalar c_i, since the nonroot equations are unchanged. Hence
f_i=c_i(L_i-lambda I)^(-1)e_1. The shared root value h must satisfy

    c_A r_A=c_B r_B=h,
    c_A+c_B+lambda h=0.                                   (9)

The plus lambda h in the last equation compensates for subtracting the root
mass twice in the separate equations. The root conductances add, whereas the
union's root mass is only 1.

Eliminating c_A,c_B without dividing by r_A or r_B shows that (9) has a nonzero
solution precisely when

    r_A+r_B+lambda r_A r_B=0.

By (8) this is exactly F(lambda)=0. If r_A=r_B=0 take (c_A,c_B)=(1,-1).
Otherwise (c_A,c_B)=(r_B,r_A) works at a root. This explicitly handles the case
which would be lost by dividing by a root-killed resolvent.

F(0+)=Z_A+Z_B-1>0. Every K_i is positive and increasing on (0,g), so F is strictly
decreasing there. At least one K_i diverges at g, and the other box has Z_j-1>0,
so F tends to minus infinity. There is exactly one root in (0,g), and (9) makes
it a genuine full-graph eigenvalue.

To exclude other eigenvalues below g independently, impose mean_A(f)=mean_B(f)=0.
This is a codimension-two subspace. On it the box gaps give

    E_S(f)=E_A(f_A)+E_B(f_B)
      >=g[||f_A||_A^2+||f_B||_B^2]
      =g[||f||_S^2+|f(1)|^2] >=g||f||_S^2.               (10)

The finite-dimensional min-max principle implies the third eigenvalue, numbering
from the zero eigenvalue, is at least g. The graph is connected through 1, so its
only zero vectors are constants. This proves Theorem T2 and (4).

### 2.3 A constructive eigenvector, not an unspecified optimizer

Every box resolvent in (9) has the explicit finite expression

    [(L_i-lambda I)^(-1)e_1](n)
      = (1/Z_i)[-1/lambda
           +sum_(empty!=D subset i) chi_D(n)/(lambda_D-lambda)],
    chi_D(n)=product_(p in D) [-1 if p divides n, 1/p otherwise]. (11)

Thus a scalar bracket for the root of (7) determines the complete slow mode.
There is no dense inverse and no unknown zeta parameter in (11). Formula (10)
then gives an absolute inverse bound 1/g on the orthogonal complement of this
mode AND the constants. Removing only the constants does not give that bound.
This is a graph spectral reduction, not a map from the native zeta residual.
With Hilbert-valued vertices, each retained scalar eigenmode becomes a copy of
that Hilbert space; it is not a two-scalar correction in that setting.

## 3. Elementary Euler mass bounds used to choose the two alphabets

For x>=2 let Z_geo(x)=product_(p<=x)(1-1/p)^(-1). We need only

    (1/2)log x <= Z(x) <= Z_geo(x) <40 log x.                (12)

Here is an elementary proof. Central-binomial valuations give
psi(2n)-psi(n)<=2n log2. Dyadic summation and monotonicity give psi(x)<3x.
The exact identity sum_(d<=x) Lambda(d)floor(x/d)=log(floor(x)!) then yields
M(x)=sum_(d<=x)Lambda(d)/d <=log x+3.

Furthermore

    sum_p<=x log p/(p-1)
      <= M(x)+sum_(n>=2) log n/[n(n-1)] <=log x+5.

The last series equals log2+sum_(n>=2)log(1+1/n)/n<2, by log(1+t)<=t and an
integral bound for sum n^-2. Normalize 1/n over all x-smooth integers. Its expected
logarithm is the preceding prime sum, B. Markov's inequality places at least half
its mass below exp(2B), whose harmonic sum is at most 1+2B. Consequently

    Z_geo(x)<=2+4B<=22+4log x<40log x.

This sums ALL smooth exponents, not a finite smooth-number table. Conversely
Z_geo(x)>=sum_(n<=x)1/n>=log x, since all n<=x are x-smooth. Finally

    Z(x)=Z_geo(x) product_(p<=x)(1-p^-2)
         >= Z_geo(x)/zeta(2) >(1/2)Z_geo(x).

The product at 2 converges absolutely, and 1<zeta(2)<2 by an integral comparison.
This proves (12), with no prime number theorem.

By maximality in (2), if q+ is the next prime after Q (which is at most P),

    Z_A^3 <= Z(P) < Z_A^3(1+1/q+)^3.                       (13)

As P increases, Q increases to infinity by (12). Thus

    Z_B=Z_A^2[1+O(1/Q)],
    Z_A/Z_B=O(1/Z_A) ->0,
    log log P=3 log log Q+O(1).                            (14)

All cutoffs and alphabet membership in this construction are prescribed by
finite rational Euler products. An arbitrarily long prime-free gap does not
invalidate (13) or the all-real-cutoff limit.

## 4. Root capacity asymptotic reconstructed without PNT

For the complete first box, let a(n)=sum_(p|n)(1+1/p)log p for squarefree n>1.
Then the spectral formula gives

    G_A=sum_(n>1, n squarefree Q-smooth) 1/[n a(n)].          (15)

Here mu is the ordinary Mobius function. Write a(n)=log n+delta(n),
delta(n)=sum_(p|n)(log p)/p. Replacing a(n) by log n
in (15) has a bounded error UNIFORMLY in Q, since that error is at most

    sum_(n>=2) mu(n)^2 delta(n)/[n(log n)^2]
    <=sum_p (log p)/p^2 sum_(m>=1) 1/[m(log(pm))^2] <infinity. (16)

The inner sum is at most 1/(log p)^2+1/log p, by decreasing integral comparison.
Thus (16) is bounded by a convergent integer p^-2 majorant. Dropping squarefree
and coprimality restrictions was legitimate only for this positive upper bound.

All squarefree integers n<=Q occur in (15). The remaining 1/(n log n) sum over
n>Q is at most Z(Q)/log Q<40. Therefore

    G_A=sum_(2<=n<=Q) mu(n)^2/[n log n]+O(1).                (17)

The elementary squarefree count is

    sum_(n<=x) mu(n)^2=x/zeta(2)+O(sqrt x).

Indeed expand mu(n)^2=sum_(d^2|n)mu(d), retain every floor, and bound both the
at-most-sqrt(x) floor errors and the tail x sum_(d>sqrt(x))1/d^2. The absolutely
convergent Euler product identifies sum mu(d)/d^2=1/zeta(2).
Partial summation against 1/(x log x) now proves

    G_A=(1/zeta(2))log log Q+O(1).                         (18)

The partial-summation error converges because sqrt(x) times the absolute derivative
of 1/(x log x) is integrable at infinity. This reconstructs the squarefree capacity
asymptotic in the previous packet by a different, short route.

We also need its second spectral moment, uniformly bounded:

    H_A=sum_(empty!=D subset A) 1/[n_D lambda_D^2]
          <=sum_(n>=2)1/[n(log n)^2]<infinity.              (19)

This is not an assumption about reciprocal derivatives at zeta zeros.

## 5. Proof of the sharp centered asymptotic

Let lambda=gamma(S(P)), the root of (7). Its monotone equation immediately yields

    lambda <= (Z_A+Z_B-1)/[(Z_B-1)G_A] = O(1/G_A).          (20)

Since G_A diverges, lambda tends to zero and eventually lambda<g0/2. By (19),

    K_A(lambda)=G_A+O(lambda).                            (21)

The second box has gap g_B>=log Q, because all its primes exceed Q. Its complete
root weight is sum_(D!=empty)1/n_D=Z_B-1. Consequently

    K_B(lambda) <= (Z_B-1)/(g_B-lambda).                    (22)

No approximation of its possibly enormous collection of modes is needed.
Divide (7), at its root, by lambda(Z_B-1). Equations (21)-(22) give

    (Z_A+Z_B-1)/[lambda(Z_B-1)]
       = K_A(lambda)+(Z_A-1)K_B(lambda)/(Z_B-1)
                         +lambda K_A(lambda)K_B(lambda)/(Z_B-1)
       =G_A+O(1).                                        (23)

For the middle error use Z_A/log Q<=40. For the last use lambda G_A=O(1)
and g_B>=log Q. The estimates concern the entire second reservoir, not a dropped
tail or an assumed bounded unweighted root functional.

Now (14) gives (Z_A+Z_B-1)/(Z_B-1)=1+O(1/Z_A). Since G_A/Z_A tends to zero,
(23) implies

    lambda=1/G_A+O(1/G_A^2).

Use (18) and log log P=3log log Q+O(1) to obtain precisely (3).
This proves Theorem T1. Every support in the construction is finite and uses
ordinary prime rates. The theorem gives a family of small POSITIVE graph gaps,
not a negative eigenvalue of any zeta form.

## 6. What becomes small: a collective reservoir contrast

The two isolated boxes have absolute centered gaps, while the combined system
has a low-cost near-constant contrast between their bulk values. A direct trial
also explains the mechanism. In the first box let h_A be its mean-zero root
Green vector, so

    h_A(1)=G_A, E_A^prob(h_A)=G_A, ||h_A||_prob^2=H_A.

Take f_A=1-h_A/G_A and f_B=0; both have root value zero. In the union probability
metric put alpha=Z_A/(Z_A+Z_B-1). Exactly,

    E_S^prob(f)=alpha/G_A,
    Var_S(f)=alpha(1-alpha)+alpha H_A/G_A^2,
    gamma(S) <=1/[(1-alpha)G_A+H_A/G_A].                   (24)

This proves a matching-order test without a limiting eigenvalue approximation.
It is mean-centered globally, not an anchored theorem disguised as a gap claim.
For the chosen split alpha tends to zero. The small reservoir is nevertheless
allowed in the all-support Poincare inequality, whose test vectors need not have
a fixed lower bound on their stationary support mass.

The uniform estimate after removing this additional mode is positive and useful:
if P_slow is its exact spectral projection and P_const the constant projection,

    L_S >= lambda P_slow+g0(I-P_const-P_slow).              (25)

In particular the inverse on the second complement costs at most 1/g0, not
log log P. A compatible Schur application must retain BOTH coarse coordinates
(constants and the slow contrast) and all their couplings. Nothing here proves
the sign of a remaining physical or Xi block.

## 7. Matching all-support upper order (reconstruction of the earlier argument)

For completeness, a slightly looser version of ADG26 proves the matching order
without depending on that manuscript's acceptance. In an arbitrary divisor-closed
S, remove the full power of the smallest prime at each step toward 1. For a
nonroot vertex a with smallest prime p, its descendants are a times integers
supported on primes strictly below p. Their harmonic mass is at most
Z_geo(p)<40log p. All exponent tails have already been included in (12).

For t>1 write Delta_a=f(a)-f(parent(a)), and let omega count distinct prime
factors. Weighted Cauchy--Schwarz on the path to n gives

    |f(n)-f(1)|^2 <= [t/(t-1)] t^omega(n)
                     sum_(a on path n) t^(-omega(a))|Delta_a|^2.

For a descendant n=a m of a, the factors of m are strictly smaller than the
least prime p of a; hence omega(n)=omega(a)+omega(m). Sum the last inequality
with weight 1/n and use positive Fubini. The multiplier at |Delta_a|^2/a is
at most [t/(t-1)] product_(q<p)[1+t/(q-1)]. Bernoulli convexity bounds that
product by Z_geo(p)^t<(40log p)^t. Finally compare with the original edge
(log p)|Delta_a|^2/a and maximize log p at log P. This gives

    sum_(n in S)|f(n)-f(1)|^2/n
      <= [40t/(t-1)(40log P)^(t-1)] E_S(f).              (26)

Here the descendant factor is product_(q<p)[1+t/(q-1)], because a prime's full
power contributes t once. Bernoulli's inequality bounds it by
[product_(q<p)(1-1/q)^(-1)]^t. Each selected tree edge is an original edge with
weight (log p)/a. These facts yield (26) with no dependence on exponent depth.
Taking t=1+1/log(40log P), e<3 and then minimizing the left side over constants,

    1/gamma(S) <=120[1+log(40log P)].                       (27)

The earlier packet's 48[1+log(16log P)] is stronger numerically. The present
reconstruction suffices for the order in (5). Equations (3) and (27) establish
both sides of (5) for all sufficiently large real P.

## 8. Limits on the attempted RH composition

The graph (1) remains a different quadratic form from the native floor residual
and the critical Xi kernel. The new result settles a question explicitly left
open by the graph papers: an absolute centered all-support gap is false. It does
not settle the ordinary integer-cutoff subclass or its native arithmetic state.

The exact scalar equation and uniformly gapped remainder furnish a two-coordinate
reduction FOR THIS GRAPH. In particular one may not infer that a signed gamma or
continuum perturbation is small on that remainder without proving its norm and
domain conditions. Nor does a controlled inverse bound an affine minimum from
above without an admissible small-error vector. ATTEMPT.md records the failed
closing transfer and the actual still-open RH-strength source estimate.

The asymptotic theorem is a paper proof. The bounded checker below confirms finite
algebra and two actual logarithmic gap brackets; it does not prove the limit.
