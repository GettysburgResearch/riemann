# The native twist hull: exact worst-center identities and physical replica obstructions

Status: PROPOSED complete unconditional component proofs; no independent review.
This is an obstruction to uniform-center extraction, not an improved fixed-center
estimate, a new zero-free region, or a proof of RH. The basic density mechanism is
classical Kronecker approximation. No literature-priority claim is made.

## 1. What is actually changed from #955

The source is the ORIGINAL ideal Mobius function, not an unsigned replacement
asserted to be a counterexample for it. The variable is the ordinary real Mellin
twist already present in #955. The theorem identifies its exact worst-center
average with the unsigned average, and gives a finite (very large) height bound
for compact-window peaks. Hence restricting the coefficients to native Mobius
does NOT rescue a theorem uniform in every real twist center.

The center is allowed to depend on the column scale. Nothing below refutes a
bound at the one fixed center zero, at every separately fixed center with
center-dependent constants, or in a substantially smaller prescribed height range.

Fix a finite Galois number field F/Q and a finite set S of prime ideals. Write
mu=mu_F. For a rational prime p, all prime ideals over p have the same residue
degree f_p, also at ramified primes. Distinct ideals over p are kept distinct.
For squarefree ideals I,

    z_p = exp(pi*i/f_p),
    product_p z_p^{v_p(NI)} = (-1)^{omega_F(I)} = mu(I).       (1)

In particular this is true for the Eisenstein field K=Q(omega). At a split
rational prime use z_p=-1; at an inert prime use z_p=i. Using -1 at an inert
rational prime would give +1 at its norm p^2, which is WRONG.

Let W>=0. We allow either a bounded function supported in a fixed compact
subinterval of (0,infinity), or the original full Gaussian

    W_c(y)=y^{-c} exp[-(log y)^2/4]/(2 sqrt(pi)), c real.

For measurable 0<=m_u(I)<=1, define

    A_t(X,u)=sum_(I prime to S) mu(I)m_u(I)(NI)^{it}W(NI/X),
    B_t(X,u)=sum_(I prime to S) |mu(I)|m_u(I)(NI)^{it}W(NI/X). (2)

Here m is a nonnegative mask, NOT a general complex sextic character. Actual
sixth-power physical rows have exactly such a mask. For the scalar principal
source take m=1. Keep any nonnegative finite row measure w. The sums converge
absolutely for each fixed X, uniformly in u, using I_F(x)=O_F(x).

Let g_T(t)=exp[-t^2/(2T^2)]/(sqrt(2pi)T), T>0, k>=1 an integer, and put

    Q_A(X,T,t0)=integral g_T(s) integral |A_(t0+s)(X,u)|^{2k} dw ds.

### Theorem 1. Exact native worst-center identity

For every X,T,k and the data just specified,

    sup_(t0 real) Q_A(X,T,t0) = Q_B(X,T,0).                  (3)

There is also the exact pointwise identity

    sup_t integral |A_t(X,u)|^{2k}dw = integral B_0(X,u)^{2k}dw. (4)

The same statements hold after integration in X against any positive measure
for which the corresponding unsigned integral is finite. In particular they
hold for the FULL Gaussian cumulative functional

    E_(k,t)(D;w)=integral_0^D integral |A_t(X,u)|^{2k}dw dX/X^{k+1}. (5)

These are suprema, not necessarily attained maxima. The same approaching
sequence of centers can be used for every fixed finite collection of scales,
nonnegative masks, tests, and moments.

#### Proof

The numbers log p for distinct rational primes are rationally linearly
independent: an integral relation would give equality of two different
integer prime factorizations. Consequently the flow

    t |-> (exp(it log p))_(p in P)

is dense in the torus for every finite prime set P. A self-contained effective
proof of the required approximation is given in Section 3; one need not import
an ineffective simultaneous-approximation theorem.

Choose a sequence t_j that approximates z_p within 1/j for the first j primes.
For every fixed squarefree I, (1) gives

    mu(I)(NI)^{it_j} -> 1.

Absolute convergence then gives A_(t_j+s)(X,u)->B_s(X,u), for every fixed s,X,u.
Moreover |A_t(X,u)|<=B_0(X,u). Dominated convergence, first in the row variable
and s and then in any allowed X measure, proves that the supremum on the left
of (3) is at least its right side, including the cumulative version.

For the converse, expand the even moment into k ideals on either side. Gaussian
Fourier integration supplies the nonnegative factor

    exp[-T^2 log(NI_1...NI_k / NJ_1...NJ_k)^2/2].

Every other factor in the unsigned tuple expansion at center zero is
nonnegative. Each native summand differs by a sign and a unit complex phase.
The triangle inequality for the complete, absolutely convergent expansion
therefore gives Q_A(X,T,t0)<=Q_B(X,T,0). Positive integration preserves the
inequality. Pointwise (4) follows directly from |A_t|<=B_0 and the same sequence.
No independent-prime randomization replaces the physical source. QED.

For the Gaussian, unsigned ideal counting gives B_0(X,u)<=C_(F,c)X for X>=1.
At X->0, the Gaussian gives B_0(X,u)=O_L(X^L) for every fixed L, uniformly in u.
These statements follow by partial summation against I_F(v)<=C_F v, beginning
at v=1. They make (5) finite and justify its dominated-convergence step.

### Consequence 1. The native Gaussian energy really reaches the trivial power

For the scalar principal source over F, every fixed k,c and finite S satisfy

    sup_t E_(k,t)(D;1) asymp_(F,S,k,c) D^k, D large.       (6)

The upper bound is unsigned ideal counting. For the lower bound, squarefree
ideal counting gives B_0(X)>=c_(F,S,c)X for large X: restrict the Gaussian to
any fixed positive annulus, and apply the positive-density squarefree count.
Integrating over D/2<X<D and applying (4) in its cumulative form proves (6).
At k=1 the original native critical energy has supremal order D, despite its
small identical-ideal and equal-norm diagonal sectors.

This is NOT growth of E_(k,0)(D); the maximizing/approaching centers move with D.

## 2. The arithmetic compatibility hypothesis is genuine

A finite list of residue degrees f_1,...,f_g admits a unit complex z with
z^{f_i}=-1 for every i if and only if the integers f_i have the same 2-adic
valuation, equivalently f_i/gcd(f_1,...,f_g) are all odd.

Sufficiency: take z=exp(pi*i/gcd(f_i)). Necessity: write z=exp(pi*i*a/f_1)
with a odd. Each a*f_i/f_1 must be an odd integer, forcing the same power of two
in each f_i. This proves the criterion, and Galois fields satisfy it because
all f_i are equal. Exclusions may remove some prime ideals, but never invalidate
an already compatible list.

The local pattern (1,2) is incompatible: z=-1 forces z^2=1. Thus the exact hull
identity is not asserted for every non-Galois field. Nor is it asserted for
arbitrary complex row phases: the nonnegative-mask hypothesis in (2) matters.
This distinction is stronger than merely saying a sign is constant on each
rational-norm fiber.

## 3. An elementary effective approximation bound

Let P be a nonempty finite set of rational primes, r=|P|, Pprod=product_(p in P)p,
and prescribed angles theta_p. Let 0<delta<=1/2 and choose an integer M such that

    M delta^2/10 >= r log(2M+1)+log 4.                     (7)

For example M=ceil(100 r delta^{-2} log(20r/delta)) satisfies (7). Then EVERY
real interval of length

    R=8 Pprod^M (2M+1)^r                                 (8)

contains a t with dist(t log p-theta_p,2pi Z)<delta for all p in P.

#### Proof

Use the nonnegative trigonometric polynomial

    F(t)=product_p [(1+cos(t log p-theta_p))/2]^M.

Its constant Fourier coefficient is

    a_M^r,  a_M=binom(2M,M)/4^M >= 1/(2M+1),

and the absolute sum of all Fourier coefficients is one. Its nonconstant
frequencies are log(A/B), with A,B distinct positive integers at most Pprod^M.
Since |log(A/B)|>=1/max(A,B), every such frequency has modulus >=Pprod^{-M}.
On any interval of length R, the average of a nonconstant exponential has
modulus at most 2 Pprod^M/R. Thus the average of F is at least

    (2M+1)^{-r} - 2Pprod^M/R >= (3/4)(2M+1)^{-r}.

If t avoids the desired box, one circular angle has distance at least delta.
For an angle d in [-pi,pi],

    (1+cos d)/2 = 1-sin^2(d/2) <= exp(-d^2/pi^2).

Use sin(|d|/2)>=|d|/pi and pi^2<10. Then F(t)<=exp(-M delta^2/10), which by
(7) is at most (1/4)(2M+1)^{-r}. This contradicts the mean lower bound. QED.

For the displayed sufficient M, put L=log(20r/delta). Then L>=log40,
2M+1<=203 r delta^{-2}L, and log(2M+1)<=6L. Also log4<=rL, whereas
M delta^2/10>=10rL. This verifies (7) without assuming the desired approximation.

For a compact norm cap X, set ell=ceil(log_2(2X)), delta=1/(8ell), and let P
contain the rational primes under the allowed ideal primes of norm <=X. An
entirely integer choice is

    L=ceil(log_2(160 r ell)), M=6400 r ell^2 L.           (9)

Every squarefree I with NI<=X then has

    |arg(mu(I)(NI)^{it})| <= delta log_2(NI) <=1/8.      (10)

Indeed the rational-prime exponents of NI have sum <=log_2(NI). With elementary
Chebyshev bounds r=O(X/log X), log Pprod=O(X), (8)-(9) give

    R <= exp(C_F X^2 log^2(3X)).                          (11)

For completeness, theta(2n)-theta(n)<=log binom(2n,n)<=2n log2; dyadic summation
gives theta(x)=O(x). Splitting primes at sqrt(x) gives pi(x)=O(x/log x). These
classical elementary bounds, not a prime number theorem, suffice for (11).
No assertion is made that this extremely generous height bound is near optimal.

## 4. Lower bounds on genuine physical sixth-power rows

Now F=K=Q(omega), O_K=Z[omega], and let S include the primes over 2 and 3. Put

    A_t(X,u)=sum_(X/2<NI<=X, I prime to S) mu_K(I)(NI)^{it} chi_I(u),
    M_k(X,H,T,t0)=integral g_T(t-t0)
                         sum_(0<Nu<=H)|A_t(X,u)|^{2k} dt. (12)

This is the native sextic source with the actual zero extension. It is not a
sum of ideals in place of physical element rows. We use ideals only to index
an injective subset of those rows.

### Theorem 2. Native physical replica peaks

For fixed k>=1 and fixed h>0, H=X^h, all sufficiently large X, every T>0,
there exists a real t0 (one can take 0<=t0<=R from (8)-(9)) such that

    M_k(X,H,T,t0) >= c_(S,k) H^{1/6} X^{2k}/(1+T).      (13)

Constants in the proof are uniform once X and H^{1/6} exceed fixed thresholds;
the threshold along H=X^h may depend on h. The same selected center works for
every moment order k and every T. There is no prime-generator/logarithmic loss
in the number of replicas.

#### Step 1: an elementary two-variable density

Let rho_K=Res_(s=1) zeta_K(s). Lattice counting gives I_K(x)=rho_K x+O(sqrt(x)).
For X,B tending to infinity independently, the number

    P_S(X,B)=#{(I,J): X/2<NI<=X, I squarefree and prime to S,
                         NJ<=B, gcd(I,J)=1}

satisfies

    P_S(X,B) ~ (rho_K^2/2) C_S X B,
    C_S=product_(p in S)(1-1/q)
        *product_(p notin S)(1-2/q^2+1/q^3)>0.          (14)

No assertion about Mobius cancellation is used. For finitely many primes,
ideal counting and inclusion-exclusion give independent local valuation
probabilities. At p notin S, allow v_p(I)=0, or v_p(I)=1 and v_p(J)=0. The
local probability is (1-1/q)+(1-1/q)^2/q=1-2/q^2+1/q^3. At p in S only I must
avoid p. These give the finite-product asymptotic.

The omitted bad pairs from primes q>Y are bounded in absolute number by

    C X B sum_(Np>Y) (Np)^{-2} = O_K(XB/Y):

use I_K(X/q^2)I_K(B) for a square in I, and I_K(X/q)I_K(B/q) for a common
prime. Each count is zero below norm one, so these bounds remain uniform even
for primes larger than X or B. Let X,B grow with Y fixed, then Y grow. The
Euler product is positive and convergent. This proves (14). An additional
fixed exclusion on J changes only finitely many positive local factors.

#### Step 2: literal rows, not hypothetical independent copies

Every ideal J in O_K is principal. Define u_J=beta_J^6 for any generator beta_J.
This does not depend on its six unit choices, is injective as a function of J,
and satisfies N(u_J)=(NJ)^6. Thus NJ<=B=H^{1/6} supplies actual distinct rows
inside (12). At EVERY original column, including nonunits,

    chi_I(u_J)=1_(gcd(I,J)=1).                            (15)

Let S_J(X) count the unsigned squarefree annular columns coprime to S and J.
Then sum_(NJ<=B) S_J(X)=P_S(X,B). Since I_K(B)<=C B, (14) and Holder give

    sum_(NJ<=B) S_J(X)^{2k} >= c_(S,k) B X^{2k}.        (16)

This is why no prime number theorem and no factor 1/log B are needed.

#### Step 3: a common interval of native peaks

Choose t0 by (8)-(10). For |s|<=1/4, remove the harmless common phase X^{is}.
Each surviving summand in e^{-is log X} A_(t0+s)(X,u_J) has argument at most

    1/8+|s| log2 < 3/8,

so its real part is at least 7/8. (The inequality cos v>=1-v^2/2 is enough.)
Therefore |A_(t0+s)(X,u_J)|>=(7/8) S_J(X). Combine with (16). Finally

    integral_(-1/4)^(1/4) g_T(s) ds >= c/(1+T)

for every T>0: for T>=1 bound its density below; for T<=1 use monotonicity of
the central Gaussian probability. This proves (13) with all masks retained.
Dropping non-sixth-power rows is permissible only here because the ORIGINAL
even moment is a nonnegative row sum. No sign is assigned to a selected tuple
expansion on the complement. QED.

### Consequence 2. An exact power cost for uniform-center native hypotheses

If H=X^h, T=X^tau with tau>=0, and a bound

    M_k(X,H,T,t0) <= C_epsilon H X^{k+e+epsilon}

is required for ALL real t0 with a constant independent of t0, then necessarily

    tau >= max(0, k-e-5h/6).                             (17)

For k=2,e=0,h=1 the lower threshold is 7/6; for h=21/20 it is 9/8. For a
single principal scalar row the corresponding necessary threshold is tau>=k-e.
If h_k=o(k) and e_k=o(k), the physical necessary width exponent is k-o(k).
This is a family of fixed-order necessary statements, not an assertion of
uniform asymptotic constants as k grows.

The Gaussian scalar case likewise gives

    sup_t0 integral g_T(t-t0) E_(k,t)(D;1) dt
                         >= c_(F,S,k,c) D^k/(1+T).       (18)

One proof uses (3): on X in [D/2,D] the unsigned source has mass comparable
to X and, after removing X^{it}, changes by at most C|t|X for bounded t, by
partial summation applied to W_c(y)|log y|. A fixed central t interval thus
has amplitude >=cX. Integrate it and then X. All Gaussian tails remain.

## 5. Exact finite native witness (not an asymptotic proof)

With only primes above 2 and 3 excluded, the COMPLETE native ideal window
32<NI<=64 consists of the two ideals over each of 37,43,61 and the squarefree
ideal (7) of norm 49. The native sum is therefore

    A_t(64)=49^{it}-2*37^{it}-2*43^{it}-2*61^{it}.

At t=0 its absolute value is 5. At the actual integer t*=842800609, the
separate rational Taylor checker proves

    Re(49^{-it*} A_(t*)(64)) > 6999/1000.                 (19)

Its unsigned maximum is 7. The check uses rigorous rational enclosures for
logarithms and pi, then a Taylor remainder for cosine, not binary64 evidence.
The exploratory search was floating point; only the separately proved interval
is used in (19). This witness does NOT satisfy or purport to satisfy the entire
prime box (10): it is an independently certified annular native peak.

## 6. What still must be proved

The principal fixed center t0=0 is not covered by an upper estimate here. Neither
(3), (13), nor a generic sextic operator norm bounds the signed unequal-product-
norm covariance there. In particular, no improved native fourth moment, 17/24
boundary, cofinal diagonal hierarchy, or RH proof follows.

A viable use of #955 for the RH problem must keep centers bounded (or price their
height dependence) AND supply an arithmetic estimate for the fixed-center
prime/composite cancellation. The hull identity proves that source specificity
alone cannot improve a bound whose constants are uniform on the whole real line.
