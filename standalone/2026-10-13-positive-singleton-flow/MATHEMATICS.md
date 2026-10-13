# Positive singleton flow: third-moment matching and a coercive remainder

Status: PROPOSED component mathematics, complete proofs at the stated scope.
No native moment exponent, zero-free boundary, or RH conclusion improves here.
Proof and computation have one author; no independent review is claimed.

This continues #940 at 59d5a8ebcd390ff898d63b2fc5ed7290995ae58b. The two-point
law is the CLASSICAL Mammen wild-bootstrap multiplier, not a new distribution.
Its fourth-moment extremality is also classical. Peano-kernel error formulas
are classical. The contribution proposed here is their source-preserving
application to the singleton remainder, including a positive all-order
compensation, quantitative coercivity, and complete finite native diagnostics.

## 1. The local multiplier and why an exact positive singleton projector fails

Put phi=(1+sqrt(5))/2, a=1-phi, b=phi, and let Z take b with probability
p=(1-1/sqrt(5))/2 and a with probability q=(1+1/sqrt(5))/2. Then

    E Z=0,   E Z^2=E Z^3=1,   E Z^4=2.                       (1)

Because Z^2=Z+1, its integer moments obey m_0=1, m_1=0,
m_j=m_(j-1)+m_(j-2). In particular m_j is positive for j>=2 and equals the
Fibonacci number F_(j-1). These statements follow directly from the two atoms.

Among REAL probability laws with first three moments 0,1,1,

    E (Z^2-Z-1)^2 = E Z^4-2 >=0.                             (2)

Equality forces support on {a,b}; the zero mean then fixes the probabilities.
Thus the law is the unique minimum-fourth-moment choice. In particular no real
probability law can have m_1=0 and m_2=m_3=m_4=1. The corresponding Hankel
matrix [[1,0,1],[0,1,1],[1,1,1]] has determinant -1. This excludes an exact
positive primewise projector that deletes only single occurrences while
retaining every other fourth-order occurrence unchanged. The Mammen law
repairs that defect by changing only the fourth occurrence from 1 to 2.

## 2. A positive Peano kernel, with explicit moments

For g in C^4([a,b]) define

    Lg = E g(Z)-g(1)+g'(0).

It annihilates polynomials of degree at most three, by (1). Taylor's integral
remainder, followed by this finite linear functional, gives

    Lg = integral_a^b K(t) g''''(t) dt,                       (3)

where, using x_+=max(x,0),

    6K(t)=p(b-t)_+^3+q(a-t)_+^3-(1-t)_+^3+3(-t)_+^2.         (4)

All exchanges are of integrals on a fixed compact interval. No asymptotic
quadrature theorem is being invoked without its hypotheses.

The kernel is nonnegative. It is zero outside [a,b]. For a<=t<=0 the cubic
moment identities reduce 6K(t) to q(t-a)^3. For 0<=t<=1 it is
p(b-t)^3-(1-t)^3, nonnegative since (b-t)/(1-t)>=b and pb^3>1 (the endpoint
t=1 is immediate). For 1<=t<=b it is p(b-t)^3. It is positive in the interior.

Apply (3) to t^4,t^5,t^6 to obtain, exactly,

    integral K=1/24,   integral tK=1/60,   integral t^2K=1/90.

The probability measure 24K(t)dt therefore has mean 2/5 and variance 8/75.
In particular Lg>=0 whenever g''''>=0.

## 3. Coercive compensation at every even order

For U,V in C and an integer k>=2, write

    R_k(U,V)=E|U+ZV|^(2k)-|U+V|^(2k)
               +2k |U|^(2k-2) Re(U conjugate(V)).             (5)

**Theorem 1.** For every U,V,

    R_k(U,V) >= c_k |V|^(2k) >=0,
    c_k=((2k)(2k-1)(2k-2)(2k-3)/24)*(8/75)^(k-2).             (6)

At k=2 the exact formula is R_2=|V|^4. At k=3, for V!=0 and
U/V=x+iy, the exact formula is

    R_3=|V|^6 [15(x+2/5)^2+3y^2+8/5].                       (7)

Proof. V=0 is immediate. For V!=0 set g(t)=|V|^(2k)((x+t)^2+y^2)^k.
Expand the integer power in nonnegative powers of y^2. Every term in its
fourth derivative is nonnegative, and its highest-power term gives

    g''''(t)>=(2k)(2k-1)(2k-2)(2k-3)|V|^(2k)(x+t)^(2k-4).

Equation (3) proves positivity. For k=2 the integral mass gives equality.
For k>=3 use Jensen on the nonnegative variable (x+t)^2 under 24K(t)dt:

    E_K |x+t|^(2k-4) >= (E_K (x+t)^2)^(k-2)
                         >= (8/75)^(k-2).

This proves (6). Expanding the degree-six polynomial gives
15x^2+12x+4+3y^2, which is (7). QED.

The sharp fourth-order identity is particularly simple:

    |U+V|^4 = E|U+ZV|^4 +4|U|^2 Re(U conjugate(V))-|V|^4.    (8)

This retains the singleton term but removes the cubic-occurrence term present
with symmetric Rademacher multipliers. The last term is a genuine nonnegative
energy with a negative sign, not a discarded signed covariance.

There is NO general monotonicity. U=V=1 gives 16=13+4-1; U=1,V=-1 gives
0=5-4-1. Thus merely replacing a randomized prime by its native value may
increase or decrease the moment.

## 4. The exact arithmetic family and the controlled positive start

Work over K=Q(sqrt(-3)). Indices are integral IDEALS, not rational norms;
conjugate split primes remain distinct. Fix bad primes S and a column exclusion
Q. Let xi_u(n)=nu(n)chi_n(u), with a fixed finite-order nu and the original
sextic symbol, completely multiplicative on squarefree products. Its value is
zero on nonunits. Let W be a fixed compact smooth test supported in (0,b_0].
At fixed D set X=max(3,b_0 D). The following bounds also hold for arbitrary
bounded row-dependent coefficients on squarefree ideals Nn<=X; no large sieve
for row-independent arrays is silently used.

Let B contain the primes with norm <=y. Give each prime outside B an independent
copy Z_p of (1). Multipliers in B are deterministically 1. Define

    P_B(D,u;Z)=sum_((n,SQ)=1) mu_K(n) xi_u(n) W(Nn/D)
                                  product_(p|n,p not in B) Z_p.
    G_(k,B)(D,w)=sum_u w(u) E|P_B(D,u;Z)|^(2k),               (9)

for any nonnegative finite row measure w of mass Z_w. Every variable in (9)
is auxiliary; the physical rows and all their original zeros stay unchanged.
Restoring every multiplier to 1 recovers exactly the native A_u(D).

**Theorem 2.** For every fixed k and epsilon>0, at y=(log X)^2,

    G_(k,B)(D,w) <<_(K,k,W,epsilon) Z_w X^(k+epsilon).         (10)

For coefficients normalized to modulus <=1 there is also a constant C_K,
independent of k,X,u, such that for sufficiently large X and 1<=k<=log X,

    (E|P_B(u;Z)|^(2k))^(1/(2k))
     <= X^[1/2+log log log X/(2 log log X)+C_K/log log X].     (11)

The same holds for a normalized nonzero row average. These are RANDOMIZED
reference bounds, not full native moment estimates.

Proof. Expand the finite moment and use absolute values only to bound this
reference. If a prime has total occurrence j across the 2k columns, its local
expectation is m_j. All m_j are nonnegative; the singleton expectation is zero.
Insert Rankin factors X^(2k sigma), sigma>1/2, before dropping the individual
norm caps. The positive bound has local factors

    (1+r)^(2k) at p in B,
    W_k(r)=sum_(j=0)^(2k) binom(2k,j)m_j r^j at p outside B,
    r=(Np)^(-sigma).                                        (12)

Masks can only remove terms from the positive upper count. For fixed k,
W_k(r)=1+binom(2k,2)r^2+O_k(r^3), so the large-prime product converges at
sigma>1/2. The small-prime log product is at most 2k sum_(Np<=y)(Np)^(-sigma),
which is o(log X) at y=(log X)^2 for each fixed sigma>1/2. Choosing sigma
sufficiently close to 1/2 proves (10).

For the claimed k-uniform version, m_j<=phi^j gives
log W_k(r)<=C k^2 r^2 whenever 2k phi r<=1, with absolute C. Put L=log X,
v=log L, delta=log(v)/(2v), sigma=1/2+delta. For k<=L and p>L^2 this
condition holds once v>=4. Elementary Chebyshev and ideal counts give

    sum_(Np<=L^2)(Np)^(-1/2) <= C_K L/v,
    sum_(Np>L^2)(Np)^(-1-2delta) <= C_K/(v log v).

For clarity, ideals up to z number O_K(z) by Eisenstein lattice counting;
partial summation yields sum_(Np>z)(Np)^(-1-a)<=C_K z^(-a)/a.
Prime ideals in this quadratic field have norms p or p^2, so the elementary
Chebyshev rational-prime bound gives the first estimate. These are the same
explicit classical counts used in #940, not a new prime-distribution theorem.
Consequently

    log E|P_B|^(2k)<=kL+2k delta L+C_K kL/v+C_K k^2/(v log v).

Division by 2k, using k<=L, proves (11). QED.

## 5. A positive completion of the larger #940 sector

Let E_(k,B) denote the exact signed native tuple sum with every singleton in B.
In G_(k,B) the SAME tuple has weight product_(p not in B)m_(c_p). Thus second
and third occurrences have weight one; discrepancies start only at total
occurrence four. For every fixed k, sigma>1/2 and y>=3, positive Rankin counting
bounds the absolute difference by

    |G_(k,B)-E_(k,B)|
      <= C_(k,sigma,K) Z_w X^(2k sigma)
           exp(2k sum_(Np<=y)(Np)^(-sigma))
           y^(1-4sigma)/log(2y),                             (13)

when B is exactly the norm cutoff <=y; fixed bad primes may be omitted.
For a bounded window absorb its fixed sup norm in the constant.

Indeed the old rough local factor is V_k=(1+r)^(2k)-2kr. The new one satisfies
0<=W_k-V_k<=C_k r^4. The difference of their convergent positive Euler products
is bounded by a constant times sum_(Np>y)(Np)^(-4sigma). Chebyshev and partial
summation bound the last sum by C_sigma y^(1-4sigma)/log(2y). The finite-prime
factor is the displayed exponential. This proves (13).

At y=(log X)^2 it implies, for fixed k and every epsilon>0,

    |G_(k,B)-E_(k,B)| << Z_w X^(k+epsilon)/(y log(2y)).         (14)

This is a specified upper bound, NOT an o(Z_w X^k) conclusion: the epsilon
factor may grow faster than the logarithmic denominator. Nor is E claimed
positive. The point is an explicit positive completion and a quantified cost.

For the native FOURTH moment the completion is also an exact causal identity.
Write E_(Q,B)(D,u), G_(Q,B)(D,u) with the exclusion Q visible and no row sum.
Then, over squarefree d supported outside B and coprime to SQ,

    G_(Q,B)(D,u)=sum_d 1_((d,u)=1) E_(Qd,B)(D/Nd,u),
    E_(Q,B)(D,u)=sum_d mu_K(d)1_((d,u)=1) G_(Qd,B)(D/Nd,u).    (15)

Only finitely many terms can occur. In the fourth expansion, m_4=2 and every
other allowed rough multiplicity has weight one. The common divisor of all
four columns therefore contributes 2^omega(g)=sum_(d|g)1. Factoring each such
d from all four columns leaves the exact shorter test, exclusion Qd, and the
mask 1_((d,u)=1). Möbius signs occur four times and all finite character phases
cancel. This proves the first identity. For the second, each rough common
prime has total weight 2-1=1. This proves it without losing the masks or
introducing an extra, unjustified coprimality condition. QED.

## 6. Exact prime restoration with positive compensation

Take any order of the relevant primes outside B, fixed before the arithmetic
sums. Initially they all have the independent law (1). Restore one coordinate
at a time to its actual multiplier 1. At step j, condition on the later random
coordinates, with earlier ones already restored. Squarefreeness gives exactly

    P=U_(j,u)+Z_(p_j)V_(j,u),
    V_(j,u)=-xi_u(p_j)
       sum_((m,p_j SQ)=1) mu_K(m)xi_u(m)
           W(Nm/(D/Np_j)) product_(ell|m,ell still random)Z_ell. (16)

U uses columns coprime to p_j. V keeps all actual composite cofactors, the
shortened scale D/Np_j and the same row u. If p_j divides u then V=0.
Earlier restored primes in m retain their native Möbius signs.

Set, with expectations only over the still-random coordinates,

    I_k=2k sum_j sum_u w(u) E[|U_j|^(2k-2) Re(U_j conjugate(V_j))],
    D_k=sum_j sum_u w(u) E R_k(U_j,V_j).

**Theorem 3.** The complete native moment obeys the finite identity

    M_(2k)(D,w)=G_(k,B)(D,w)+I_k-D_k,                         (17)
    D_k>=c_k sum_j sum_u w(u) E|V_j|^(2k)>=0.                 (18)

At order four,

    D_2=sum_j sum_u w(u) E|V_j|^4.                            (19)

Proof. Apply (5) to each conditional polynomial and telescope. The prime and probability sums are finite. Row sums converge absolutely:
coefficient support and multiplier range are bounded and w has finite mass.
Theorem 1 gives (18)-(19). QED.

The derivative at zero in I_k selects the active prime in exactly ONE of the
2k slots. Triple occurrences have cancelled in the local comparison, rather
than being estimated separately. At k=2 the only correction is the full
fourfold coincidence (19). At larger orders the correction is not termwise
positive in its tuple expansion; its positivity is proved by (3), and must
not be asserted after arbitrary tuple deletion.

The endpoint I_k-D_k is independent of prime order; I_k and D_k separately need
not be. Order choice alone cannot change the missing arithmetic estimate.
The census gives an actual example where both change by 48 and cancel exactly.

## 7. The remaining estimate and the relation to OPEN-2

For hard physical rows the mass is O_K(H). At the safe log-square cutoff,
(10) supplies a diagonal-sized start. The specific sufficient target is

    I_2 <= D_2+C_epsilon H D^(2+epsilon).                    (OPEN-Q4)

More generally replace 2 by k and allow a whole-moment excess e_k. A bound
I_k<=(1-eta)D_k+C H D^(k+e_k+epsilon), eta>0, would be stronger and sufficient.
Neither bound is proved here. Cauchy applied separately to U and V merely
creates a new unpaid sum; the nonnegative compensation is not a proof that
it dominates the signed derivative.

With the #940 notation M=E-2k Re Gamma, our identity gives exactly

    I_k-D_k=-2k Re Gamma+E-G.                                (20)

Both E and G have the stated diagonal upper bounds. Thus (OPEN-Q4) and the
old one-sided target are equivalent up to those bounded starts; this packet
does not call the new target a weaker problem. It supplies a local positive
structure in which to attempt it, rather than another unsupported positivity
claim about the original singleton sector.

The existing extraction would turn a full averaged/native moment excess e_k
at H=D^h into the boundary 1/2+5h/(12k)+e_k/(2k), with its original tests,
twists and shortened-scale requirements. In particular OPEN-Q4 at admissible
fixed h down to 1 would activate the proposed 17/24 route. That arithmetic
hypothesis, the full generalized hierarchy, and RH remain open. No bound on
zero ordinate follows from (11): X is a column scale, not a zero's height.

The freezing and microscopic-phase obstructions in #941/#943 are not evaded
by this identity. A controlled randomized start cannot be extended to every
intermediate freezing cutoff by assumption. The full cofactor and signed
sum in (17) must be retained, including any compensating large excursions.

## Sources and credit

- Base #940, 59d5a8ebcd390ff898d63b2fc5ed7290995ae58b, singleton-budget/
  MATHEMATICS.md, read in full from the preserved packet. It supplies the
  original selected union, elementary counts and largest-singleton target.
- #937, 9f3250198a9b0551f42eb73dfd74a265c2a66854, PRIME_FREEZING.md, full text
  available in the preceding live reads: symmetric sign freezing, exact
  odd-binomial flux and its physical-density limitation are prior work.
- #943, 24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed, DEGREE_GEOMETRY.md, read in
  full through GitHub: signed singleton matrices need not be positive; complete
  native moment benchmarks used by the checker are credited, not new values.
  MICROSCOPIC_PHASE.md and #941 were inspected at PR-description scope only.
- E. Mammen (1993), Bootstrap and Wild Bootstrap for High Dimensional Linear
  Models, Annals of Statistics 21(1), 255-285, DOI 10.1214/aos/1176349025.
  Distribution attribution, not a bootstrap theorem used as an analytic input.
- D. Roodman, M. O. Nielsen, J. G. MacKinnon, M. D. Webb (2019), Fast and wild:
  Bootstrap inference in Stata using boottest, Stata Journal 19(1), 4-60,
  DOI 10.1177/1536867X19830877, section 3.3. The accessible primary article
  explicitly records the law, moments and minimum kurtosis. These are classical.
- K. Petras (1992), Error Bounds for Gaussian and Related Quadrature and
  Applications to R-Convex Functions, SIAM J. Numer. Anal.,
  DOI 10.1137/0729037. Peano-kernel positivity is a classical method; the
  complete particular kernel needed here is derived in Sections 2-3.
- A. J. Harper, Moments of random multiplicative functions, II: High moments,
  arXiv:1804.04114, prior model-moment literature. Its sharper estimates are
  not inputs and are not claimed to be improved by (10)-(11).

No exhaustive literature-priority claim is made. No upstream theta theorem,
GRH, native second moment, numerical asymptotic inference or external
bootstrap approximation theorem enters the component proofs above.
