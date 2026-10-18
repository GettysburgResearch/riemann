# Arbitrary ferromagnetic auxiliaries do not repair the Gaussian mediator

Status: **PROPOSED complete native weak-closure theorem, conditional only
on the stated Lee--Yang property of the auxiliary observable.** This
extends RANK_ONE_HIERARCHY_OBSTRUCTION.md beyond independent auxiliary
spins to arbitrary finite ferromagnetic graphs. It is an obstruction to
a specified all-order completion architecture, not an RH theorem or a
new zero-free region.

## 1. Exact theorem and graph realization

Let Y_N be any symmetric bounded-support random variable whose entire
characteristic function has only real zeros. It can, in particular, be
a nonnegative weighted observable of an arbitrary finite zero-field
ferromagnetic graph. Set M_N(x)=E exp(xY_N). Choose a_N>0 and define

    p_N(x)=Z_N^(-1) exp(-a_N x^2) M_N(x).             (1)

All graph sizes, supports, weights, variances, a_N and interaction
parameters may vary. The Gaussian integral makes (1) integrable.

**Theorem.** If p_N converges weakly to an everywhere-positive continuous
even density p, then for some finite constants C_2,C_4,

    -log[p(x)/p(1)]<=C_2(x^2-1)+C_4 x^4,   x>=1.   (2)

The actual complete theta density has superquartic potential and is
therefore outside this weak closure.

For a finite Ising auxiliary graph, write Y_N=sum_j b_j sigma_j and
give its existing positive interactions J_ij. The joint Gaussian/spin
law proportional to

    exp[-a_N x^2+x sum_j b_j sigma_j
                        +sum_(ij) J_ij sigma_i sigma_j]

has marginal(1). Integrating out x adds positive couplings
`b_i b_j/(2a_N)` to that arbitrary graph. Thus this is a genuine
correlated positive transfer architecture. It includes the rank-one
construction as J=0 and still allows a_N->infinity.

## 2. Exact Hadamard representation

For each N, bounded support gives an even entire characteristic function
of exponential type, normalized to1 at0. Pairing its positive real zeros
lambda, with multiplicities, gives

    M_N(x)=product_j(1+t_{j,N} x^2),
    t_{j,N}=lambda_{j,N}^(-2)>0,
    sum_j t_{j,N}<infinity.                          (3)

The number of factors can be infinite for each finite graph. The
exponential factor in an order-one Hadamard representation is linear;
evenness removes it, and bounded-support order one permits no quadratic
Gaussian exponent. A deterministic zero observable gives the empty
product and is included. The summability in (3) follows from the order
bound and is also authenticated by the finite variance identity.

All sums below converge absolutely for each fixed N and fixed real x.
For u>0, log M_N(sqrt(u)) is a sum of concave functions log(1+t_j u),
so the unnormalized potential

    V_N(x)=a_N x^2-sum_j log(1+t_j x^2)              (4)

is convex as a function of u=x^2.

The native weighted-restriction lemma proved in sections2--3 of
RANK_ONE_HIERARCHY_OBSTRUCTION.md now applies verbatim: for U_N=X_N^2,
restrict to a compact interval I inside (0,infinity), weight by sqrt(u)
and renormalize. Its density is proportional to exp[-V_N(sqrt(u))],
and is logconcave. Weak convergence and the elementary concave-log-density
compactness argument imply

    V_N(x)-V_N(y)->-log[p(x)/p(y)],     x,y>0.       (5)

This is a local ratio theorem; no tail or parameter convergence is
assumed.

## 3. A bounded zero resource from three local ratios

Define for t>=0

    G(t)=-log(1+9t)+(8/3)log(1+4t)-(5/3)log(1+t).  (6)

Strict concavity of log(1+tu), evaluated at u=1,4,9, gives G(t)>0 for
t>0. Direct expansion gives

    G(t)=20t^2+O(t^3),                    t->0;
    G(t)->(8/3)log4-log9>0,               t->infinity.

Therefore a universal c>0 satisfies

    G(t)>=c min(t^2,1),                  t>=0.      (7)

Positivity, continuity and the two positive endpoint limits prove this
bound without numerical optimization. The same normalization-canceling
finite difference as before gives

    V_N(3)-(8/3)V_N(2)+(5/3)V_N(1)=sum_j G(t_{j,N}). (8)

Its left side is bounded by (5). Positivity and (7) therefore give a
finite uniform S such that

    sum_(t_j<=1)t_j^2<=S,     #{j:t_j>1}<=S.         (9)

This controls multiplicities too. Tonelli or monotone limits justify
the positive sum in (8), even when the auxiliary product has infinitely
many zeros.

## 4. Absorb small-zero quadratic terms and bound the potential

Set q(t,x)=t x^2-log(1+t x^2). For real x and t>=0,

    0<=q(t,x)<=t^2 x^4/2.                           (10)

This follows from `y-y^2/2<=log(1+y)<=y`, y>=0. For each N put

    c_N=a_N-sum_(t_j<=1)t_j,

where the subtracted sum is finite for each N by (3). Then

    V_N(x)=c_N x^2+sum_(t_j<=1) q(t_j,x)
                           -sum_(t_j>1)log(1+t_j x^2). (11)

Only differences of the final sum will be used. For x>=1,

    0<=log[(1+t_j x^2)/(1+t_j)]<=2log x.             (12)

There are at most S terms in that sum. Furthermore q(t,x) increases
with x>=0, and its increment from1 to2 is at most8t^2. Subtract (11)
at x=1 from x=2. Equation(5), (9)--(12) imply

    3c_N=V_N(2)-V_N(1)
       -sum_(t_j<=1)[q(t_j,2)-q(t_j,1)]
       +sum_(t_j>1)log[(1+4t_j)/(1+t_j)],

so c_N is bounded above and below uniformly. In particular, for C>=c_N
and every x>=1,

    V_N(x)-V_N(1)
       <=C(x^2-1)+(S/2)x^4.                        (13)

The large-t terms have the favorable nonpositive sign; no upper bound
on their individual size is required. Pass to (5). This proves (2).

The constants in (13) were obtained at the fixed local points1,2,3.
They work at every x simultaneously, so passing separately at each x
does establish a global quartic envelope.

## 5. Actual-target consequence and boundary

The native complete-source calculation in
RANK_ONE_HIERARCHY_OBSTRUCTION.md gives

    -log[p_theta(x)/p_theta(1)]
              =pi exp(2x)-(9/2)x+O(1),    x->infinity.

It contradicts (2). Thus adding any finite positive auxiliary graph to
the Gaussian mediator does not yield a cofinal theta construction,
even with unrestricted size and a vanishing mediator variance.

The theorem concerns a single observed continuous Gaussian coordinate
whose spin coupling is linear, with a symmetric real-zero auxiliary
law. It does not assert that all ferromagnetic spin laws or all
Lee--Yang laws are Gaussian-mediated in this sense. Nonzero real fields,
signed auxiliary interactions, nonquadratic continuous transfer energies,
or a fundamentally different observation map require separate analysis.
