# Direct attack on the failure count: an exact expansion and a fixed-moment obstruction

Date: 2026-09-07.
Status: the requested bound is NOT proved. The component arguments below are
proposed proofs requiring independent review. No new positive range is claimed.
Parent: PR #803 at 44a8ed8193a2a81d68c1f5c2bb592b266698032d.
Scope: the literal integer prime-power source and the unchanged annular scalar.

The requested conclusion is

    for every eps>0 there is C_eps such that
    N_-(M) <= C_eps M^(1/2+eps) for every real M>=2.         (TARGET)

The preceding packet proves that TARGET implies RH, not TARGET itself.
This pass tries a direct exceptional-set moment argument. It obtains an exact
native correlation expansion and an unconditional diagonal asymptotic. It also
proves that a proposed fixed-even-moment upper estimate is incompatible even
with RH. It does not manufacture an arithmetic upper bound from this obstruction.
Local labels FC1--FC4 are not canonical claim IDs. No priority claim is made.

## 1. Definitions and the attempted upper bound

Let Lambda(p^r)=log(p), for every prime p and r>=1, and zero otherwise.
Extend the weight by zero outside [1/4,4]:

    w(u)=u/3-1/(192u^2),       1/4<u<=1,
         1/(3u^2)-u/192,       1<u<4.

It is continuous, nonnegative, vanishes at the outside endpoints, and
integral w=45/128=:a. For integers j>=2 put

    P_j=(1/j) sum_n Lambda(n)w(n/j^2),
    R_j=a*j-P_j=1/4-D(j),
    N_-(M)=#{j integer: 2<=j<=M and R_j>1/4}.

Here R_j is a discrepancy, not its positive part. For every integer k>=1,

    N_-(M) <= 16^k sum_(2<=j<=M) R_j^(2k).                  (1)

This follows termwise, including the strict threshold. Equation (1) is a
valid upper bound. The attempted next step, a sublinear power bound for the
fixed moment on its right, is NOT valid: FC3 below proves its incompatibility
with RH. Thus (1) with a fixed k cannot supply TARGET by that estimate.

The case eps>=1/2 of TARGET is immediate with C_eps=1 from N_-(M)<=M.
No unconditional proof is supplied for every 0<eps<1/2.

## 2. FC1: exact centered prime-correlation expansion

All sums in this section are finite. Put

    K_j(n)=w(n/j^2)/j,
    L_j=sum_n K_j(n), delta_j=a*j-L_j,
    e_n=Lambda(n)-1, T_j=sum_n e_n K_j(n).

The subtraction by one runs over ALL positive integers, not just prime powers.
It is a comparison with integer density and does not alter the native P_j.
Then

    R_j=delta_j-T_j.                                       (2)

Define

    H_M(n,l)=sum_(2<=j<=M) K_j(n)K_j(l),
    b_M(n)=sum_(2<=j<=M) delta_j K_j(n).

Every K, H and b is rational at integer j. H is a positive semidefinite Gram
matrix with nonnegative entries and support n,l<=4 floor(M)^2. Exact expansion:

    sum R_j^2 = sum delta_j^2 - 2 sum_n e_n b_M(n)
                                + sum_(n,l) e_n e_l H_M(n,l).     (3)

The last sum includes its entire ordered off-diagonal. Neither H>=0 nor
Lambda>=0 says that these centered off-diagonal terms have a favorable sign.

### 2.1 The lattice correction is completely harmless

For the zero-extended w, the derivative has jumps

    1 at 1/4,  -65/64 at 1,  1/64 at 4.

On the two open pieces its total variations are 21/32 and 21/32. Hence

    Var(w')=107/32.                                        (4)

The composite trapezoid formula for a compactly supported continuous function
whose derivative has bounded variation gives

    |h sum_n w(nh)-integral w| <= h^2 Var(w')/8.             (5)

Here is a proof covering knots not on the grid. In a cell [u,u+h] compare w
with its linear interpolant. The signed Dirichlet Green representation gives
the difference. Integrating that Green function in the observation variable
leaves (t-u)(u+h-t)/2, between zero and h^2/8. Sum the absolute measure bounds
over cells. At a shared grid endpoint this kernel is zero, so endpoint atoms
are not counted twice. The finite trapezoid sum equals h sum w(nh), since w
has compact support. This proves (5) with no differentiability at the knots.

Set h=j^-2 in (5) and divide by jh. It follows that

    |delta_j| <= 107/(256 j^3).                             (6)

The elementary prime-power Chebyshev bound psi(x)<3x and max w=21/64 imply
P_j<63j/16<4j. Equations (6) and a=45/128 give L_j<j for j>=2; thus
|T_j|<=P_j+L_j<5j. From (2),

    |sum R_j^2 - sum T_j^2| < 5,                           (7)

uniformly in M. Indeed bound sum(delta_j^2+2|delta_j T_j|) by
(107/256)^2 sum j^-6+(1070/256) sum j^-2<5, using
sum_(j>=2)j^-2<=1 and sum_(j>=2)j^-6<=1. This is unconditional.
The elementary estimate psi<3x is reconstructed in the locked PC parent.

## 3. FC2: the unconditional size of the centered diagonal

Write

    Q_M=sum_n e_n^2 H_M(n,n),
    O_M=sum_(n!=l) e_n e_l H_M(n,l),
    sum T_j^2=Q_M+O_M.                                    (8)

Under the ordinary prime number theorem (unconditional),

    Q_M ~ c_w M log M,
    c_w=2 integral_(1/4)^4 w(u)^2 du
       =455/3072-log(2)/36 >0.                             (9)

No rate, finite-height input, or RH premise is asserted in (9).

Proof. The PNT gives theta(x)=sum_(p<=x)log p~x. Partial summation yields
sum_(p<=x)(log p)^2~x log x. Higher prime powers contribute at most
O(sqrt(x) log^3(x)), which is o(x log x). Therefore

    sum_(n<=x)(Lambda(n)-1)^2
       =sum Lambda(n)^2 -2psi(x)+floor(x) ~ x log x.         (10)

The PNT for theta follows from that for psi because the complete higher-power
contribution is O(sqrt(x)log^2(x)); the same elementary counting argument
bounds all exponents, not a fixed truncation.

Apply Stieltjes integration to the fixed compact test w^2. The convergence
in (10) is uniform after scaling over u in [1/4,4]. It gives, with X=j^2,

    sum_n e_n^2 K_j(n)^2 ~ 2 log(j) integral w^2.

Summing over j gives (9). The integral is evaluated on both pieces:
each contributes 455/12288-log(2)/144. Both endpoint values of w^2 vanish.
This supplies the complete diagonal, not an upper bound on Q_M+O_M.

Under RH, the inherited spectral representation makes R_j bounded. Thus
(7)--(9) imply, CONDITIONALLY,

    O_M=-Q_M+O(M),
    O_M/(M log M) -> -c_w.                                (11)

In particular dropping centered off-diagonal correlations misses a leading
cancellation even in the case where every D(j) is positive. Equation (11) is
not claimed unconditionally and does not itself bound the failure count.

## 4. FC3: every fixed even moment has positive logarithmic mean under RH

The source input for this section is the RH-conditional paired-zero expansion
from the locked annular packet, Section 4, together with the exact filtered
source identity from its Section 2. It is not a new definition of the source.
With b=3/2 and

    A(z)=65/64-(4^z+4^-z)/8,

write Gamma for the set of DISTINCT positive ordinates and m_gamma for their
analytic multiplicities. Under RH,

    R_j=V(2 log j)+E(j^2),
    V(t)=sum_(gamma in Gamma) c_gamma cos(gamma t),
    c_gamma=2m_gamma A(i gamma)/(b^2+gamma^2)>0,
    sum c_gamma=C0<infinity, E(j^2)->0.                    (12)

The complete multiplicity belongs inside c_gamma. No linear independence
hypothesis about ordinates is used. The absolute convergence follows from
the classical O(T log(T+2)) multiplicity-counting bound and gamma^-2 weights.
Also A(i gamma)=|1-exp(i gamma log4)/8|^2>=49/64.

**FC3a.** Under RH,

    (1/log M) sum_(2<=j<=M) R_j^2/j
       -> mu_2 := (1/2) sum_(gamma in Gamma) c_gamma^2 >0.  (13)

Proof. For any FIXED real t!=0,

    (1/log M) sum_(2<=j<=M) j^(-1+it) ->0.                 (14)

Compare with the integral using derivative (-1+it)x^(-2+it); its absolute
integral from 1 to infinity is finite for fixed t. The integral itself is
(M^(it)-1)/(it), bounded. For t=0 the limit is one. Thus, in any finite
trigonometric sum, the only surviving products of two distinct-positive-
frequency cosines are the equal-frequency products, each of mean 1/2.
The tail in (12) is uniformly small. The logarithmic averaging operators
have uniformly bounded norm because sum_(j<=M)1/j=log M+O(1). They therefore
permit passage to the uniformly convergent full V and its square. The
bounded error E(j^2)->0 has zero logarithmic Cesaro contribution. This proves
(13). At least one nontrivial zero exists, so at least one c_gamma>0; this is
the ordinary classical zero-existence input, not a new zero calculation.

**FC3b.** For each FIXED integer k>=1, under RH there is a constant mu_(2k)>0
such that

    (1/log M) sum_(2<=j<=M) R_j^(2k)/j -> mu_(2k),
    mu_(2k)>=mu_2^k.                                     (15)

For existence, expand finite trigonometric sums to the fixed power 2k and
use (14). Frequency resonances at higher orders are retained; they are NOT
ruled out by independence of ordinates. Uniform approximation passes to the
full series. The lower bound follows from Jensen's inequality for the
probability weights (1/j)/(sum_(2<=j<=M)1/j), then (13). The vanishing E error
is handled by boundedness and a fixed-power difference estimate.

**FC3c.** Under RH, for every fixed k>=1 and every theta<1,

    sum_(2<=j<=M) R_j^(2k) is NOT O(M^theta).               (16)

If A_k(M)=sum R_j^(2k) were O(M^theta), partial summation would make
sum R_j^(2k)/j bounded: A_k(M)/M+integral_2^M A_k(t)t^-2 dt
has a finite bound when theta<1. This contradicts (15).

Consequently the particular proof strategy (1) plus a sublinear power bound
for a fixed raw even moment would require an estimate that fails even when
RH holds and N_-(M)=0. This does NOT refute TARGET, all moment methods,
threshold-sensitive majorants, subtraction of a suitable oscillatory baseline,
or methods whose order grows with M. It rejects only the stated fixed-moment
route. Conditional obstruction is distinguished from unconditional failure.

The argument is an elementary logarithmic mean computation in an absolutely
convergent Fourier series; no external novelty is claimed.

## 5. What a growing-order argument would actually need

The same elementary Markov inequality holds when k=k(M). For illustration,
let

    k(M)=ceil(log(M)/(2 log(25/9))).

An arithmetic estimate

    sum_(2<=j<=M) R_j^(2k(M)) <= M(3/20)^(2k(M))             (17)

would give N_-(M)<=M^(1/2), since 16*(3/20)^2=9/25. It would therefore
prove TARGET. NO unconditional proof of (17) is supplied here.
Under RH, the parent has |V|<=C0<1/20 and 0<=E<1/10 for j>=2, so (17)
follows from |R_j|<3/20. Using that RH-dependent bound to establish (17)
unconditionally would be circular. Fixed-k identities or fixed-k asymptotics
do not become uniform at k proportional to log M by changing a subscript.

The exact kth-moment expansion contains all products of up to 2k genuine
prime-power coefficients, centered against the same main term. The algebra
is finite, but its uniform arithmetic estimate is still missing. A proof
controlling the threshold-crossing part rather than the full fixed moment
could avoid FC3, but no such estimate is proved in this pass.

## 6. Relation to the requested quantifiers and the stopped argument

The parent supplies a fully quantified obstruction: a zero beta>1/2 gives
limsup log(1+N_-(M))/log M>=beta. Thus TARGET, with
0<eps<beta-1/2, excludes that zero. The parent's other direction says that
RH makes D(j)>1/10 at every j>=2. Together they make TARGET equivalent to
RH at the source-qualified scope already recorded there. This is background
calibration; repeating it is not a proof of TARGET.

For clarity: this pass proves (3), (6), (7) directly; (9) using classical
PNT; and (13)--(16) conditionally on RH and the declared source expansion.
It does NOT prove (17), a nontrivial unconditional failure-count upper bound,
a stronger positive arithmetic range, or RH. The only unconditional general
count bound obtained remains N_-(M)<=floor(M)-1.

This is a failed direct counting attempt with retained component proofs, not
an RH completion or an assertion that no different proof can succeed.
