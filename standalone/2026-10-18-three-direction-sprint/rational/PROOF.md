# Native prime compensation: coherent sector removal and its remaining obstruction

Status: **PROPOSED complete component arguments, requiring independent review.
The complete unweighted rough-core contraction and RH remain OPEN.**

Scope: ordinary rational Mobius source, all old products, complete reduced
denominators, the strict native square step, physical integer cells, and
coherent cross terms. Sections 8 and 11 give a proved target-preserving
compensator: it removes an actual large positive prime-pair sector on its
stated output window at a small coherent cost. The complete reweighted
remainder is still open. A separate probe-space contraction is proved in
Sections 4--6, and its capture limitation is explicit in Section 7.
The obstruction uses an actual Mobius subsector, not replacement coefficients.

Exact starting source: #994 at
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
`standalone/2026-10-18-theta20-and-native-cancellation/native/PROOF.md`.
Its #848 all-prefix consumer is at
`99101457b32b6f10f4eda88ca998048404b860ea`.
All new conclusions here are separate proposed objects. No inherited file or
scientific status is changed. There is no worldwide novelty claim for the
classical ingredients.

## 1. Fixed source and initial results

For an integer Y>=64 put b=Y+1, N=b^2-1 and

    g_Y(n)=mu(n)1_(n<=Y), z_Y=g_Y*g_Y,
    m(x)=sum_(n<=x)mu(n)/n, M_Y=m(Y),
    F_J=sum_(j=1)^J m(j)^2,
    L_J=sum_(n<=J)mu(n)log(n)/n,
    C_Y(q)=sum_(q|d,d<=Y^2) z_Y(d)/d.

Convolution is Dirichlet convolution. Let H_j=sum_(n<=j)1/n, H_0=0,

    R(x)=H_floor(x)-log(x)-gamma,
    S_q(x)=sum_(d|q)mu(q/d)R(x/d), q>=2.

The last expression equals sum_(n<=x)c_q(n)/n+Lambda(q), so S_q is a
step function constant on integer cells. All prime-power centerings remain.
For a fixed 1/2<rho<2/3 use exactly the original annuli

    X_j=2^j b<b^2, U_j=min(2X_j,b^2),
    I_j=[X_j,U_j), Q_j=floor(X_j^rho).

For a function a on these integer cells, its norm is
sum_(k=b)^N |a(k)|^2. Identifying it with its constant extension on
[k,k+1) gives the identical dx norm; there is no interpolation error.

### A. A quantitatively large actual rough-core subsector

Let P_Y be the primes in (Y/2,Y] and n_Y=|P_Y|. Select only denominators
q=p*l with distinct p,l in P_Y, and define

    P_Y(k)=sum_(p<l, p,l in P_Y) C_Y(pl)S_(pl)(k).

For every Y>=512 and every integer k in
[ceil(Y^2/32),floor(Y^2/16)],

    C_Y(pl)=2/(pl),
    S_(pl)(k)>=1/5,
    P_Y(k)>=n_Y(n_Y-1)/(5Y^2).                         (1.1)

Consequently the complete coherent selected-sector energy obeys

    ||P_Y||_2^2 >= n_Y^2(n_Y-1)^2/(1600Y^2)
                >> Y^2/log(Y)^4.                     (1.2)

The final asymptotic imports only the ordinary prime number theorem. The
finite prime-count lower bound before it has no asymptotic input. All these
denominators pass the original large-denominator cutoff and any subpower
large-core cutoff for all sufficiently large Y.

In particular the desired improving estimate cannot hold uniformly after
arbitrary per-denominator contractions. If 0<p0<2 and a+p0<2, then no bound

    ||sum_q omega_q(k) C_Y(q)S_q(k)||_2^2
       << Y^(a+epsilon)(1+F_Y)^p0                    (1.3)

can hold for every |omega_q(k)|<=1 on the retained rough sector and every
epsilon>0. This rules out all parameter pairs
a<(2-p0)*0.749914... proposed for improving the working boundary. It does
not rule out the complete unweighted native estimate: the selected sector
must cancel with its signed complement.

### B. A proved native-energy contraction for balanced large-prime probes

Choose an integer P with P^3>=Y^2 and P<=Y, and write J0=floor(Y/P).
For every old prime p>P put J(p)=floor(Y/p); thus p>sqrt(Y) and J(p)<p.
The prime stratum B_J contains p>P with J(p)=J, in increasing order.

At each physical integer cell k choose real weights w_p(k) satisfying:

* |w_p(k)|<=1, and w_p(k)=0 unless pY>k;
* separately in EVERY stratum B_J,

      sum_(p in B_J) w_p(k)/p=0,
      sum_(p in B_J) w_p(k)/p^2=0;                    (1.4)

* within each ordered stratum, w_p(k) is constant on at most THREE
  intervals of primes and zero elsewhere. The intervals and their three
  values may depend arbitrarily on k. Empty strata give zero weights.

These are nontrivial constraints with elementary exact constructions:
three nonempty consecutive blocks give a homogeneous 2-by-3 rational
matrix of the two sums in (1.4). Choose a nonzero rational kernel vector
and normalize its largest absolute entry to 1. Distinct ordered blocks
have different harmonic-weighted means of 1/p, so this matrix has rank 2.
The support condition is met by choosing blocks only among p>k/Y.

Set

    omega_w(q,k)=sum_(p>P,p|q) w_p(k),
    V_w^rough(k)=sum_(q>Q_j, q cubefree, core(q)>S)
                     omega_w(q,k) C_Y(q)S_q(k), k in I_j,              (1.5)

where core(r^2 s)=s for coprime squarefree r,s. There are at most two
primes p>P in any nonzero old product, so |omega_w|<=2 on C_Y's support.
One may divide all weights by 2 if contractions bounded by 1 are desired.

**Theorem PC.** Fix 1/2<rho<5/9. Let S=S(Y)>=1 be integer valued with
log S=o(log Y). For every epsilon>0, uniformly over ALL the legal weights
above and ALL integers Y with |M_Y|<=1/Y,

    ||V_w^rough||_2^2
       <<_(rho,epsilon,S) Y^epsilon(1+F_floor(Y/P)).    (1.6)

The subpower schedule qualification means that, for each epsilon, the
schedule's factor S H_S^6 is eventually bounded by the required small
power. An explicit finite-Y estimate is (6.9) below; no hidden constant
uniform over arbitrary subpower schedules is asserted.

The estimate has no unknown signed-covariance premise. It controls actual
Mobius probes with large denominators and large squarefree core, output
dependent masks, shared factors and complete windows. In particular P
can be the least integer with P^3>=Y^2, leaving F at a prefix of size
at most Y^(1/3). The hypothesis |M_Y|<=1/Y holds at every native reciprocal
sign crossing; their cofinality is the separate classical/source-qualified
#848 input. This theorem by itself neither bounds the full unweighted
amplitude nor changes the zeta zero-free boundary.

## 2. Classical elementary bounds used below

For d>=1 put m_d(x)=sum_(n<=x,(n,d)=1)mu(n)/n, with value zero for x<1.
The uniform bound |m_d(x)|<=1 follows by the prime-semigroup argument
credited to Tao, arXiv:0908.4323v5. For integer x, let A count the coprime
integers <=x and B the integers <=x supported on primes dividing d.
Divisor inversion gives B=sum_(n<=x,(n,d)=1)mu(n)floor(x/n). Thus

    |x m_d(x)| <= B + sum_(n<=x,(n,d)=1){x/n}
                <= B+A-sum_(n<=x,(n,d)=1)1/n <= x.

The two counting sets intersect only at 1, and the last harmonic sum is
at least 1. Real x follows by taking its integer part. In particular
|m(x)|<=1, F_Y<=Y, and Abel summation gives |L_J|<=2log J.

The ordinary harmonic remainder satisfies |R(x)|<=1/x for x>=1. One
proof is the exact Euler remainder formula

    R(x)=(1/2-{x})/x-integral_x^infinity (1/2-{t})dt/t^2.

At integers use its right-hand value. Also 0<gamma<1, so

    integral_0^infinity |R(x)|^2 dx <=3.               (2.1)

Indeed the (0,1) integral is 2-2gamma+gamma^2<=2 and the remaining
integral is at most 1. Every use of this full norm pays both tails.

For q cubefree write q=r^2s with r,s coprime squarefree. The complete
coefficient identity is

    C_Y(r^2s)=mu(s)/(r^2s)
      sum_(uvw=s) m_(ruw)(Y/(ruw))m_(rvw)(Y/(rvw))/w.   (2.2)

All ordered pairwise-coprime triples occur. To prove it, a prime of r
must divide both old inputs; for p|s expand
1_(p|ac)=1_(p|a)+1_(p|c)-1_(p|a)1_(p|c). For squarefree d,
sum_(a<=Y,d|a)mu(a)/a=mu(d)m_d(Y/d)/d. Substitution gives (2.2).
If q has a prime cube then C_Y(q)=0. In particular

    |q C_Y(q)| <= a(s):=product_(p|s)(2+1/p).           (2.3)

For a self-contained coefficient resource bound, a(s)^2<=d_7(q): at
exponent 1 the local factor is at most 25/4<7 and at exponent 2 it is
1<=28. Counting seven-fold divisor tuples gives

    sum_(q<=Q) q^2|C_Y(q)|^2 <= Q H_floor(Q)^6.         (2.4)

This is weaker in logarithms than #994's sharper 32 Q H_Q^3, but has
the same powers and is sufficient here.

## 3. Proof of the actual prime-pair obstruction

If p>Y/2 divides an old input a<=Y, then a=p. Thus for distinct such
p,l the only old ordered pairs with pl|ac are (p,l) and (l,p), proving
C_Y(pl)=2/(pl). Shared-prime pairs instead produce p^2 and are excluded
from this squarefree subsector, not silently discarded from the source.

For k in the stated interval, k<pl and k/p,k/l>=1. The exact mode is

    S_(pl)(k)=H_k-H_floor(k/p)-H_floor(k/l)
      =log(pl/k)-gamma+R(k)-R(k/p)-R(k/l).              (3.1)

Since pl>Y^2/4 and k<=Y^2/16, its first logarithm exceeds log 4.
The error has magnitude at most (1+p+l)/k <=64/Y+32/Y^2.
The elementary positive series log 2=2(1/3+1/(3^3*3)+...) gives
log 4>4/3. For Y>=512,

    S_(pl)(k)>1/3-64/Y-32/Y^2 >=1/5.

There are at least Y^2/64 integer output cells in this interval, so
(1.1)--(1.2) follow. The prime number theorem gives
n_Y~Y/(2log Y). No short-interval prime theorem is used.

For rho<2/3, Q_j<b^(4/3), whereas pl>Y^2/4; the latter is larger for
Y>=512. The core is pl itself and exceeds any subpower cutoff eventually.
Thus an allowed contraction can select exactly these denominators and
these output cells. Since 1+F_Y<=1+Y<=2Y, an exponent a+p0<2 contradicts
(1.2), after choosing epsilon<2-a-p0. This proves (1.3)'s failure.

## 4. Exact large-prime incidence identity

Define complete (unwindowed) sources

    T_Y(x)=sum_(n<=Y)mu(n)R(x/n)/n,
    Z_J(x)=sum_(n,m<=J)mu(n)mu(m)R(x/(nm))/(nm),
    T_(Y,J)(x)=sum_(n<=J)mu(n)T_Y(x/n)/n,
    A_p(x)=sum_(q>=2,p|q) C_Y(q)S_q(x).               (4.1)

All these sums are finite and include above-output products. Divisor
inversion of the mode formula gives

    sum_(q|d) S_q(x)=R(x/d), with S_1=R.               (4.2)

Let p>sqrt(Y), J=floor(Y/p). Every p-divisible old input is pn with
n<=J<p and mu(pn)=-mu(n). Separating old pairs with exactly one, and
with both, inputs divisible by p gives the exact identity

    A_p(x)=-(2/p)sum_(n<=J)mu(n)/n
                   [T_Y(x/(pn))-T_Y(x/n)]
           +p^-2[-Z_J(x/p^2)+2Z_J(x/p)-Z_J(x)].       (4.3)

For clarity, removing the p-divisible b from the first inner sum adds
(1/p)sum_(m<=J)mu(m)/m[R(x/(p^2nm))-R(x/(pnm))]. Its coefficient
is -2/p, while the both-divisible term is
p^-2[Z_J(x/p^2)-Z_J(x)]. This proves every sign and the factor 2 in (4.3).

For 1<=u<Y+1 finite divisor inversion gives

    T_Y(u)=1+L_Y-(log u+gamma)M_Y.                    (4.4)

On the actual output x>=Y+1 with x<pY, every u=x/(pn), n<=J, lies
in [1,Y), so no omitted terms or limiting continuation enter (4.4).
Writing

    U_J(x)=M_J[1+L_Y-(log x+gamma)M_Y]
               +M_Y L_J-T_(Y,J)(x),

we obtain the low-rank form

    A_p(x)=-(2/p)U_J(x)-(2M_Y M_J/p)log p
           +p^-2[-Z_J(x/p^2)+2Z_J(x/p)-Z_J(x)].       (4.5)

The common U_J is never assumed small. The first balancing condition
in (1.4) cancels it exactly, separately at every cell and in every J.

## 5. Pay the full large-prime probe by smaller native energy

Let A_w(x)=sum_(p>P) w_p(floor x) A_p(x), with zero weights outside
the physical square step. This is exactly sum_q omega_w(q,x)C_Y(q)S_q(x).
Every physical cell remains; multiplying by the varying weights is not a
frequency cutoff.

Within B_J, p belongs to (Y/(J+1),Y/J], so
|log p-log(Y/J)|<=log(1+1/J)<=1/J. The first balance gives

    |sum_J M_J sum_(p in B_J) w_p log p/p|
       <=sum_(p>P)1/[J(p)p]<=2.                       (5.1)

The last inequality uses Jp>Y/2 and at most Y old primes. Therefore
the root norm of the logarithmic M_Y term in (4.5) is at most
4Y|M_Y|. No PNT or prime-density estimate is used here.

For 0<u<J+1, complete divisor inversion gives the exact identity

    Z_J(u)=m(u)-(log u+gamma)M_J^2+2M_J L_J.           (5.2)

Indeed 1*g_J*g_J has coefficient mu(n) at every n<=J. On our support,
x/p^2<Y/p<J+1. Substituting (5.2) into the first error in (4.5), the
second balance sum w_p/p^2=0 removes its entire log x, gamma and L_J
profile. The remaining logarithmic profile has root norm at most 4H,
where

    H=sum_(P<p<=Y, p prime)1/p <=1+log(Y/P).           (5.3)

This follows from the same within-stratum logarithm subtraction and
sum 1/(Jp^2)<=(2/Y)sum 1/p. The native part has root norm at most

    sum_(p>P) (1/p) sqrt(F_floor(Y/p))
       <=H sqrt(F_J0).                               (5.4)

Here dx=p^2du and the integral of m(u)^2 over (0,J+1) is exactly F_J.
Thus the smaller native energy is literal, not a smoothed surrogate.

For u>=J the strict Newton identity and |m|<=1, |M_J|<=1,
|L_J|<=2log J give

    |Z_J(u)|<=6L min(1,J^2/u), L=1+log(Y+1).          (5.5)

For J<=u<(J+1)^2 use
Z_J(u)=2M_J-m(u)-(log u+gamma)M_J^2+2M_J L_J.
For u>=J^2, each R argument is >=1 and the independent full-tail bound
|Z_J(u)|<=J^2/u applies. These ranges overlap, so (5.5) is complete.

Since integral_0^infinity min(1,A/x)^2 dx=2A, Minkowski gives for the
second error term in (4.5) the root bound

    sum_(p>P)12sqrt(2)L J(p)/p^(3/2)
       <=8sqrt(2)L Y/P^(3/2).                        (5.6)

All p-tail sums are bounded by the full integer integrals, including
omitted primes. Finally x>=Y and J^2<=Y imply that the last error has
root norm at most

    sum_(p>P)Y^(3/2)/p^4 <=Y^(3/2)/(3P^3).            (5.7)

The varying bounded weights contract each term's physical norm. Combining
the estimates BEFORE squaring pays every mixed term:

    ||A_w||_2 <=4Y|M_Y|+H sqrt(F_J0)+4H
                +8sqrt(2)L Y/P^(3/2)+Y^(3/2)/(3P^3). (5.8)

This explicit bound is valid at every Y>=64, without a crossing assumption.

## 6. Restore the actual low-denominator and core masks

There are two issues: low denominators and the small-core sector. Both
must be removed from A_w at the amplitude level.

### 6.1 Output-dependent prime blocks: a maximal bound

For integers 1<=Q<=K and any subset B of denominators, the argument
below gives the resource bound

    sum_(K<=k<2K)|sum_(q in B, 2<=q<=Q)C_Y(q)S_q(k)|^2
       <=E(K,Q):=4(1+log Q)^7(Q/K+Q^3/K^2).          (6.1)

For a family of nonnegative integer multiplicity masks n_B(q) whose
total incidence is <=2, the SUM of these squared norms is at most
4E(K,Q). This stronger resource form, rather than an individual bound
multiplied by the number of blocks, is what is used below.

To prove it, for e(t)=exp(2pi it) the exact Abel expansion is

    Z_theta(k)=e(k theta)/[(k+1)(1-e(-theta))]+E_theta(k),
    |E_theta(k)|<=2/[k^2|1-e(theta)|^2].               (6.2)

Here Z_theta=-sum_(n>k)e(n theta)/n in its Dirichlet/Abel sense.
Summing over reduced a/q gives S_q, including its centering. Distinct
reduced frequencies through Q have spacing at least Q^-2. Their geometric
Gram sum has absolute row bound K+2Q^2(1+log Q). Also

    sum_(a mod q)^* |1-e(a/q)|^-2 <=q^2/4.

Thus, writing LQ=1+log Q, (2.4) bounds the leading squared norm by
Q LQ^6/(4K)+Q^3 LQ^7/(2K^2). The full remainder has pointwise modulus
at most Q^2 LQ^3/(2K^2), by Cauchy and sum_(q<=Q)q^2<=Q^3.
Its squared norm is at most Q^4 LQ^6/(4K^3). Combining root terms and
Q<=K proves (6.1), with slack.

For multiplicity masks, at each level sum_B n_B(q)^2<=4. The leading
coefficient resources therefore cost at most 4. The sum of the positive
remainder masses is at most twice the original mass, so their squared
sum also costs at most 4. This proves the stated summed resource bound.

Within each prime stratum pad its list to a power of two and form its
ordinary dyadic interval tree. Put d=1+ceil(log_2 Y). Any prefix decomposes
into at most d tree blocks; Cauchy and then the maximum over prefixes
cost d times the sum of ALL block squared values. Any interval is a
difference of two prefixes and costs a further factor 4. At each tree
level, all the blocks across all strata partition the old primes p>P.
Each nonzero old product contains at most two such primes. Therefore the
summed resource bound above applies at every level.

At a cell the legal weights use at most three intervals per stratum.
Cauchy over at most J0 strata now proves

    ||sum_(q<=Q)omega_w(q,k)C_Y(q)S_q(k)||_l2(K,2K)^2
       <=144 J0 d^2 E(K,Q).                          (6.3)

This proof explicitly permits the intervals and their values to depend
on the physical cell. Applying a fixed-coefficient large sieve directly
to arbitrary moving per-q weights would be invalid.

For alpha=2-3rho>0, the complete dyadic sum is

    sum_j E(X_j,Q_j)
       <=E_Y^*:=1024/(1-2^-alpha)
                     b^-alpha(1+log b)^7.             (6.4)

Indeed Q_j/X_j and Q_j^3/X_j^2 are both <=X_j^-alpha, and
1+log Q_j<=2(1+log b). A shortened last annulus is paid by its full
positive bound. Hence the actual complete low-denominator root cost is

                      12 sqrt(J0) d sqrt(E_Y^*).      (6.5)

### 6.2 Full coherent small-core cost

For arbitrary measurable multipliers |v_q(x)|<=1, the elementary full
norm estimate from the same source is

    ||sum_(q>=2, core(q)<=S) v_q C_Y(q)S_q||_L2(0,infinity)
         <=12 H_Y sqrt(S) H_S^3.                     (6.6)

For completeness, (2.1) gives
||S_q||_2<=sqrt(3q) beta(q), beta(q)=product_(p|q)(1+p^-1/2).
Use (2.3) for q=r^2s and sum beta(r)/r<=3H_Y. This last inequality
follows by expanding beta(r) into its squarefree divisors and bounding
the full convergent sum sum_(e>=1)e^-3/2 by 3. For squarefree s,
a(s)beta(s)<=(9/8)d_4(s). Here for p>=3 the local factor is at most
(7/3)(5/3)=35/9<4, whereas for p=2 it is less than 9/2. Since s is
squarefree, the exceptional ratio (9/2)/4=9/8 occurs AT MOST ONCE,
not once per prime. Elementary partial summation gives
sum_(s<=S)d_4(s)/sqrt(s)<=2sqrt(S)H_S^3. The resulting constant
27sqrt(3)/4 is below 12. This pays all r, all s, both infinite physical
tails, and coherent cross terms by the root-norm triangle inequality.

For omega_w the bound is twice (6.6). To avoid overlap, remove first
ALL q<=Q_j modes; then remove core<=S only among q>Q_j. The latter
additional annular indicator is an allowed measurable multiplier in
(6.6). Consequently

    ||V_w^rough||_2 <= ||A_w||_2
           +12sqrt(J0)d sqrt(E_Y^*)
           +24 H_Y sqrt(S)H_S^3.                     (6.7)

No diagonal subtraction, unaccounted cross term, or extra annulus count
is present.

### 6.3 Finish the contraction

If P^3>=Y^2 then J0<=Y^(1/3), Y/P^(3/2)<=1 and
Y^(3/2)/P^3<=Y^-1/2. If rho<5/9 then alpha>1/3, so

    J0 d^2 E_Y^* = O_rho(Y^(1/3-alpha)log(Y)^9)=o(1).  (6.8)

At |M_Y|<=1/Y, equations (5.8) and (6.7) give the explicit bound

    ||V_w^rough||_2 <=4+H sqrt(F_J0)+4H+8sqrt(2)L
         +1/(3sqrt(Y))+12sqrt(J0)d sqrt(E_Y^*)
         +24H_Y sqrt(S)H_S^3.                        (6.9)

Since the last core cost is Y^o(1), this proves Theorem PC after squaring
the complete root inequality. The narrower choice rho<5/9, rather than
merely rho<2/3, is load-bearing: it pays every stratum's moving-block
maximal loss without an unknown cancellation premise.

## 7. What is not captured, and the next mathematical target

The balanced probe space does NOT span the full constant denominator
weight. This is already visible on the actual prime-pair sector of part A.
At a cell where at least three top primes are active, a linear combination
of balanced probes still has a prime-weight vector v satisfying
sum v_p/p=0 in the top stratum J=1. To equal weight 1 on every distinct
pair denominator pl would require

                        v_p+v_l=1 for every p!=l.

For at least three primes this forces v_p=1/2 for every p, contradicting
sum v_p/p=0. The second balance only further restricts the space. This
is an exact capture obstruction, not a conjectured cost estimate.

The successful calculation identifies a useful, genuinely bounded family
of correlated directions. It also identifies the missing common profiles
U_J and the unbalanced prime-pair directions rather than claiming they
have disappeared. A complete next step must control these complementary
modes or couple them to the no-large-prime sector before taking norms.
Applying (1.6) to the full native source would be a quantifier error.

The prime-pair obstruction says that arbitrary sector contractions cannot
solve this problem. The prime-contrast estimate says that carefully chosen
correlations can nevertheless produce a much smaller native-energy cost.
Neither statement evaluates the remaining full rough-core norm or proves RH.

## 8. A cheap compensator that RETAINS the large prime-pair sector

The contraction space of Theorem PC is deliberately balanced separately
inside each stratum. The following stronger construction instead cancels
a common mode ACROSS strata, and retains the entire prime-pair subsector
in Section 3. It gives an actual signed compensator for that obstruction.

Put

    P1={p prime:Y/2<p<=Y}, P2={p prime:Y/3<p<=Y/2},
    h1=sum_(p in P1)1/p, h2=sum_(p in P2)1/p,
    lambda=-2h1/h2,
    W_Y(x)=sum_(p in P1)A_p(x)+lambda sum_(p in P2)A_p(x).             (8.1)

Assume h2>0. The prime number theorem implies this eventually, as well as

    h1~log(2)/log Y, h2~log(3/2)/log Y,
    lambda ->-2log(2)/log(3/2), |lambda|<4 eventually.                 (8.2)

The weights are exact rational prime harmonic sums. No fitted coefficient
or zero-dependent choice is involved. For every q define the exact fixed
denominator multiplier

    omega_*(q)=#{p in P1:p|q}+lambda #{p in P2:p|q}.                  (8.3)

Thus W_Y=sum_q omega_*(q)C_Y(q)S_q. In particular omega_*(pl)=2 for
EVERY distinct p,l in P1: the target sector has not been annihilated.

Let I_Y be the complete cells from ceil(Y^2/32) through floor(Y^2/16),
with continuous extension [ceil(Y^2/32),floor(Y^2/16)+1). All bounds
below include that last complete cell. For Y>=64 its points satisfy
x>=2Y and x<pY for every selected p. There are at most two selected
primes in any nonzero old product: three primes exceeding Y/3 would
have product greater than Y^3/27>Y^2.
For Y>=64 all their continuous extensions satisfy x>=2Y and x<pY for
every p in P1 union P2. Since M_1=1, M_2=1/2, L_1=0 and
L_2=-log(2)/2, the common profile in (4.5) cancels exactly:

    M_1 h1+lambda M_2 h2=0.                                        (8.4)

Only its logarithmic M_Y remainder and rectangular T_(Y,J) terms remain.
Writing ell_j=sum_(p in Pj)log(p)/p, the coefficient of -2M_Y is

    C1=ell1-(h1/h2)ell2+h1 log2
      =h1[(ell1/h1)-(ell2/h2)+log2],
    |C1|<=h1 log6.                                                 (8.5)

For the last bound, any top prime divided by any middle prime lies
between 1 and 3. If h1=0 every term is zero; otherwise use their positive
harmonic-weighted logarithmic means.

Because x>=2Y>=YJ for J=1,2, the FULL rectangular source satisfies

    |T_(Y,J)(x)|<=YJ/x,
    ||T_(Y,J)||_L2(I_Y)<=sqrt(32)J.                                 (8.6)

This is a genuine full-tail bound: every old product an<=YJ is included,
and |R(x/(an))|<=an/x. There is no Mobius independence assumption.
The rectangular contribution to ||W_Y|| is therefore at most
10sqrt(32)h1.

For any fixed J, (2.1) and dilation give the complete global estimate

    ||p^-2[-Z_J(x/p^2)+2Z_J(x/p)-Z_J(x)]||_2
       <=sqrt(3)/p (sum_(n<=J)|mu(n)|/sqrt(n))^2
                       *(1+2/sqrt(p)+1/p).                         (8.7)

For J=1 the squared sum is 1; for J=2 it is 3/2+sqrt(2)<3.
Since p>Y/3 and Y>=64, the last parenthesis is below 3/2. Its total
weighted root cost is below 7sqrt(3)*(3/2)h1. At |M_Y|<=1/Y,
(8.5) costs at most 2h1 log6. Combining complete ROOT norms gives

                         ||W_Y||_L2(I_Y)<=96h1.                    (8.8)

All cross terms are paid. This bound is valid whenever Y>=64, h2>0 and
|M_Y|<=1/Y; its constant does not require a bound on h1/h2.

### Keep the actual large-denominator, large-core masks

Define on I_Y, using exactly the annular Q_j from Section 1,

    W_Y^rough(k)=sum_(q>Q_j,core(q)>S)
                         omega_*(q)C_Y(q)S_q(k).                   (8.9)

For large Y the multiplier is bounded by 8 on the native support, so
the complete low-denominator root cost is at most 8sqrt(E_Y^*) by
(6.1)--(6.4). These weights are FIXED in the physical output; no moving
coefficient large-sieve shortcut is used.

If S<Y/3, a denominator with a single prime from P1 or P2 to odd
exponent automatically has core>S. A small-core denominator with such
a prime must contain p^2, so BOTH old inputs are p times an integer
at most 1 (P1) or at most 2 (P2). The exact complete coefficients are

    p in P1: C_Y(p^2)=1/p^2;
    p in P2: C_Y(p^2)=1/(4p^2),
             C_Y(2p^2)=-3/(4p^2), C_Y(4p^2)=1/(4p^2).              (8.10)

These are all possibilities; the shared small prime 2 is retained.
Using ||S_q||<=sqrt(3q)beta(q), their complete coherent root cost,
even with arbitrary annular indicators, is at most

    sqrt(3)(1+sqrt(3/Y))[h1+3|lambda|h2] <=24h1.                    (8.11)

Indeed the three P2 coefficients have total local norm factor
3/2+sqrt(2)<3. Thus for every fixed 1/2<rho<2/3 and every S<Y/3,
eventually in Y,

                 ||W_Y^rough||_L2(I_Y)
                       <=120h1+8sqrt(E_Y^*)=O(1/log Y).            (8.12)

This covers every subpower schedule S(Y) eventually. The final asymptotic
uses the ordinary PNT only for (8.2), and the explicit power decay in
E_Y^*. The unconditional source algebra and finite-Y root bounds precede
that asymptotic.

### A source-preserving removal, not an independent-sector deletion

Let R_Y^rough be the full UNWEIGHTED rough amplitude with positive sign.
Subtract (1/2)W_Y^rough on I_Y and zero outside it. Its complete square-step
root norm changes by O(1/log Y). On I_Y this replaces the denominator
weight 1 by 1-omega_*(q)/2. Every distinct top prime-pair denominator is
now absent, while all complementary weights are explicitly retained and
uniformly bounded eventually.

This removes the actual large positive obstruction sector on its witness
window at a vanishing coherent cost. Direct deletion of that sector would
cost >>Y/log(Y)^2 by Section 3. The compensating changes in the other core
orders are essential. This is a new proved source-specific estimate, not
a global bound for the reweighted remainder.

## 9. The exact transition at x=pY and the extension bottleneck

The short inverse identity must not be extended beyond its domain. There
is a useful exact continuation with the missing term visible. For
Y<=x<(Y+1)^2, p>sqrt(Y), J=floor(Y/p), define

    D_p(x)=1_(x>=pY)[m(x/p)-M_Y].                                  (9.1)

Then (4.5) continues exactly as

    A_p(x)=-(2/p)U_J(x)-(2M_Y M_J/p)log p
       +(2/p)D_p(x)
       +p^-2[-Z_J(x/p^2)+2Z_J(x/p)-Z_J(x)].                       (9.2)

At x=pY the bracket in D_p is zero, so no endpoint is ambiguous.
To prove (9.2), the rectangular inverse identity says

    1*g_Y*g_J(n)=g_Y(n)+g_J(n)-mu(n)
                    for n<(Y+1)(J+1).                            (9.3)

Its coefficient defect is
mu*(delta-1*g_Y)*(delta-1*g_J), supported at (Y+1)(J+1).
Since the integer p(J+1) is at least Y+1, throughout the STRICT native
square step u=x/p<(Y+1)^2/p<=(Y+1)(J+1), and u>=J. Thus
weighted summation gives

    sum_(a<=Y,n<=J)mu(a)mu(n)H_floor(u/(an))/(an)
        =m(min(u,Y))+M_J-m(u).                                   (9.4)

Subtract the COMPLETE logarithmic balances. The difference between
(9.4) and its short value M_J is exactly -D_p(x), proving (9.2).
One may also derive it by expanding the old-prefix inverse defect into
harmonic shifts; all shifts 2,...,J cancel by divisor inversion.

For the two-stratum compensator (8.1), its previously omitted transition
term is precisely

    2sum_(p in P1 union P2) w_p/p
                 1_(x>=pY)[m(x/p)-M_Y].                          (9.5)

A direct root-norm bound on the full square step is

    <= 2sum_p |w_p|/sqrt(p) sqrt(F_floor(Y^2/p))
         +2Y|M_Y|sum_p |w_p|/p.                                 (9.6)

Since p is comparable with Y this has generic energy cost of order
Y F_(3Y) times logarithms (or the exact finite prime-weight expression
in (9.6)). That cost does not satisfy the desired improving exponent
budget. The term involves literal native m on [Y,3Y], and cannot be
discarded as an old-prefix balance or bounded by the already proved
subpower contrast theorem.

Thus Section 8 is an actual coupled cancellation across core orders on
its stated window, and Section 9 identifies the specific signed
prime-convolution estimate needed to extend it. The full rough-core
estimate remains open rather than being concealed at the x=pY transition.

## 10. Adaptive cross-stratum compensation with a stated coefficient cost

The transition term can be retained and canceled algebraically, at the
price of a specific arithmetic conditioning problem. This section gives
a conditional norm theorem and a separate exhaustive finite certificate.
The latter does not establish the former's asymptotic hypothesis.

Fix L>=3 and 0<a<1. For sufficiently large Y let

    B_J={p prime:Y/(J+1)<p<=Y/J}, 1<=J<=L,
    h_J=sum_(p in B_J)1/p, ell_J=sum_(p in B_J)log(p)/p,
    v_J=M_J h_J,
    d_J(k)=sum_(p in B_J)1/p * D_p(k),
    K_Y=[ceil(aY^2),(Y+1)^2), on its complete integer cells.

All selected primes exceed sqrt(Y). For each cell k suppose real
coefficients lambda_J(k) satisfy

    lambda_1(k)=1,
    sum_(J=1)^L lambda_J(k)v_J=0,
    sum_(J=1)^L lambda_J(k)d_J(k)=0,
    |lambda_J(k)|<=K(Y), with K(Y)>=1.                             (10.1)

Define the actual complete source probe and its native rough restriction

    W(k)=sum_(J=1)^L lambda_J(k)sum_(p in B_J)A_p(k),
    omega(q,k)=sum_(J=1)^L lambda_J(k)#{p in B_J:p|q},
    W^rough(k)=sum_(q>Q_j,core(q)>S)omega(q,k)C_Y(q)S_q(k).

**Conditional compensator theorem.** At every Y with |M_Y|<=1/Y for
which (10.1) holds, for any fixed 1/2<rho<2/3 and S<Y/(L+1),

    ||W^rough||_L2(K_Y)
       <= C_(a,L) K(Y) H(Y,L)+2K(Y)sqrt(L E_Y^*),
    H(Y,L)=sum_(p>Y/(L+1),p<=Y)1/p.                              (10.2)

In particular ordinary PNT gives H(Y,L)=O_L(1/log Y). A uniformly
bounded coefficient cost would give a vanishing compensator throughout
this entire fixed macroscopic window, INCLUDING the x=pY transitions
and the final native cells above Y^2. A subpower cost would give only
a subpower compensator; it would not by itself imply that the norm
vanishes. No such uniform or cofinal cost is proved here.

Proof. Sum (9.2) with the weights. The common U_J profile is

    U_J(x)=M_J[1+L_Y-(log x+gamma)M_Y]
                         +M_Y L_J-T_(Y,J)(x).

Both its first bracket and the full future defect cancel by (10.1).
The remaining expression is exactly

    W(x)=2sum_J lambda_J(x)h_J T_(Y,J)(x)
       -2M_Y sum_J lambda_J(x)[L_J h_J+M_J ell_J]
       +sum_J lambda_J(x)sum_(p in B_J)E_p(x),                    (10.3)

where E_p is the full three-dilate square correction in (9.2).
Subtract log(Y) times the first zero equation from the logarithmic sum.
Since |M_J|<=1, |L_J|<=2log L and |log(p/Y)|<=log(L+1), its root
cost is at most

    2(Y+1)|M_Y|K(Y)H(Y,L)[2log L+log(L+1)].

For Y>=L/a, every old rectangular product is below x on K_Y, so
|T_(Y,J)(x)|<=YJ/x and

    ||T_(Y,J)||_L2(K_Y)<=J/sqrt(a).

Hence the rectangular root cost is at most
2K(Y)H(Y,L)L/sqrt(a). The global square correction (8.7) costs

    sqrt(3)K(Y)H(Y,L) A_L^2
       *[1+2sqrt((L+1)/Y)+(L+1)/Y],
    A_L=sum_(n<=L)|mu(n)|/sqrt(n).

These estimates use pointwise boundedness of lambda and complete root
norms. They do not require smoothness, slow variation or independence.

For the low-denominator subtraction, let V_J^low be the FIXED prime
incidence source in stratum J with the exact moving annular cutoff.
For every supported q, writing n_J(q)=#{p in B_J:p|q},

    sum_J n_J(q)^2 <= (sum_J n_J(q))^2 <=4.

Apply the coefficient large-sieve resource of (6.1)--(6.4) to these
fixed incidence vectors and sum their squared norms. It is at most
4E_Y^*. The pointwise Cauchy inequality
|sum_J lambda_J(k)V_J^low(k)|^2<=L K(Y)^2 sum_J|V_J^low(k)|^2
proves the second term of (10.2). Thus no large sieve with arbitrary
output-dependent coefficients is being assumed.

Finally S<Y/(L+1) implies every selected prime appearing to odd exponent
survives the core cutoff. A small-core denominator with a selected prime
must be q=p^2 t, where t divides a product of two integers <=J<=L.
Both old inputs are multiples of p; no other selected prime can divide
them once Y>(L+1)^2. All exact shared-prime contributions are retained:

    C_Y(p^2 t)=p^-2 C_J(t),
    C_J(t)=sum_(u,v<=J,t|uv)mu(u)mu(v)/(uv).

For Y large, p does not divide t. Define the explicitly finite constant

    B_L=max_(1<=J<=L) sum_(t<=J^2)|C_J(t)|sqrt(t)beta(t).

Using (6.6), the COMPLETE small-core root cost is at most
sqrt(3)K(Y)H(Y,L)[1+sqrt((L+1)/Y)]B_L. The annular indicator and the
varying coefficients cannot increase this triangle bound. Combining
these three complete costs proves (10.2).

Every distinct pair of primes from B_1 has omega(pl,k)=2, since
lambda_1=1. Thus subtracting W^rough/2 from the unweighted rough source
removes every one of these denominators on K_Y and pays exactly the
root bound (10.2), with all compensating denominator weights explicit.
The full reweighted remainder, and the lower window below aY^2, remain
unestimated. This is a source-preserving cancellation operation rather
than a claim that one has bounded the full source.

### A finite coefficient-budget theorem, separate from (10.2)'s asymptotics

The checker `certify_conditioning.py` uses exact Mobius integers and
outward-rounded integer intervals with 160 fractional bits. At each
distinct nuisance state it checks the exact two-row minimum-Euclidean-
norm solution for lambda_2,...,lambda_L. Put

    A=sum_(J=2)^L v_J^2, B=sum_(J=2)^L d_J^2,
    C=sum_(J=2)^L v_J d_J, Delta=AB-C^2.

If Delta>0 its exact coefficients have numerators

    n_J=v_J(-v_1 B+d_1 C)+d_J(v_1 C-d_1 A),
    lambda_J=n_J/Delta.                                           (10.4)

The code proves Delta>0 and |n_J|<=4Delta by division-free interval
inequalities, and independently checks both nuisance equation residuals.
For the initial d=0 state the one-row solution -v_1 v_J/A is used.
Rank-deficient incompatible states are failures, never discarded.

Each possible change of d_J is exactly at k=pn, n>Y, with jump mu(n)/k.
The producer's prime-times-integer event list is independently checked
at EVERY cell by factoring k itself. Directed native prefixes then
independently reconstruct d at every change state, and exact rational
prefixes authenticate the interval producer. Hence all intervening
physical cells are covered, including cells with zero Mobius jumps.

The resulting finite receipt at Y=517, L=16 and a=1/32 is recorded in
`CONDITIONING_CERTIFICATE.json`. It proves the coefficient budget K=4
for its explicitly recorded complete range; it does not prove the same
budget at any other prefix. Floating wider scouts in `ADAPTIVE_SCOUT.json`
are reconnaissance only. In particular good conditioning on finitely
many future native prefixes is not a uniform conditioning theorem.

## 11. A moving active-prime compensator through almost half the output step

There is a different way to avoid the future defect without assuming
conditioning. It preserves every top-prime pair, allows a large moving
middle coefficient, and pays that coefficient by its harmonic mass.
The complete large-denominator and core masks are retained.

Let P1=(Y/2,Y] intersect the primes and P2=(Y/3,Y/2] intersect the primes.
Assume P2 is nonempty and let p_* be its largest prime. Choose a lower
integer endpoint A>=2Y and put

    J_Y=[A,Y p_*), on its COMPLETE integer cells,
    P2(k)={p in P2:pY>k},
    h2(k)=sum_(p in P2(k))1/p,
    lambda(k)=-2h1/h2(k), h1=sum_(p in P1)1/p,
    w_p(k)=1 for p in P1, lambda(k) for p in P2(k), and 0 otherwise.

Throughout J_Y, h2(k)>0. Every selected prime is active on the entire
cell [k,k+1), so D_p=0. Both old prefixes are still exactly J=1 or 2.
The common profile cancellation is POINTWISE

    h1+lambda(k)h2(k)/2=0,
    sum_p |w_p(k)|/p=3h1.                                         (11.1)

There is no claim that lambda is uniformly bounded. It can be as large
as O(Y/log Y) when a single middle prime remains. Define W and W^rough
with these weights and the exact source and annular masks of Section 1.

**Moving compensator theorem.** Fix 1/2<rho<2/3. For all sufficiently
large Y with |M_Y|<=1/Y, every S<Y/3 and every A satisfying
2Y<=A<Yp_*, write a=A/Y^2. Then

    ||W^rough||_L2(J_Y)
       <= h1 [10/sqrt(a)+2log6+183(1+log(4/a))]
          +12h1 H_N^2 Y^(2rho-1)/sqrt(2rho-1).                    (11.2)

All constants are explicit and every cross term is paid by complete root
norms or pointwise bounds. In particular if a>0 is fixed, ordinary PNT
implies

    ||W^rough||_L2(J_Y)^2 <<_(a,rho,epsilon) Y^(4rho-2+epsilon).
                                                                         (11.3)

Thus for ANY prescribed eta>0 one may choose a fixed
1/2<rho<min(2/3,1/2+eta/4), retaining the original allowed annular
form, so that this compensator has energy O_eta(Y^eta). This last
statement chooses the cutoff exponent with eta; it is not a subpower
claim for one fixed rho. For fixed rho, (11.3) is the asserted bound.

PNT also gives p_*/Y ->1/2. Hence this controls the actual complete rough
compensator through `(1/2-o(1))Y^2`, instead of only the initial witness
window. Every top-prime pair has omega(pl,k)=2 throughout. Subtracting
W^rough/2 removes all of them there and pays precisely (11.2), with
the altered complementary denominator weights retained. This remains
a component operation, not an estimate for the resulting whole source.

Proof of the full-source bound. The same exact identity as in Section 8
has only two moving quantities: the harmonic-weighted mean logarithm
of the active middle primes, and the three-dilate square correction.
The logarithmic coefficient still satisfies |C1(k)|<=h1 log6.
The rectangular part is EXACTLY

    2h1[T_(Y,1)(x)-2T_(Y,2)(x)],

because lambda(k)h2(k)=-2h1. Since x>=A>=2Y,
its complete root cost is at most 10h1/sqrt(a). The log profile costs
at most 2h1 log6. This does not require a bound on the number of active
middle primes.

Set B_a=1+log(4/a). Every R argument in the three square-correction
dilates for J<=2 is at least a/4 on J_Y. Thus |R|<=B_a and the
sum of absolute coefficients in Z_J is at most H_2^2=9/4. Hence

    |E_p(x)|<=9B_a/p^2,
    sum_p |w_p(k)|/p^2 <=(3/Y)sum_p |w_p(k)|/p=9h1/Y.

The square-correction root cost is therefore at most 81B_a h1.
No moving-coefficient large sieve is being used.

The complete small-core subtraction has exactly the p^2,2p^2,4p^2
coefficient list (8.10). For any such q every divisor d has x/d>=a/4,
and |S_q(x)|<=tau(q)B_a<=9B_a. The sum of absolute C coefficients
for a middle prime is 5/(4p^2), and for a top prime it is 1/p^2.
Consequently its pointwise absolute size is at most
(405/4)B_a h1/Y, and its root cost is at most 102B_a h1. This bound
allows every native annular indicator, so no hidden mask is removed.

It remains to pay the low-denominator subtraction without a bound on
lambda. Eventually Q_j<(Y/3)^2. A contributing q<=Q_j then contains
exactly one selected prime p, to first power, and q=pt with p not
dividing t. The integer t is cubefree if C_Y(q) is nonzero. The complete
coefficient and harmonic remainder bounds give

    |C_Y(pt)S_(pt)(k)|
       <=(2+1/p)(1+1/p)/k * a(core(t))*sigma(t)/t.

For cubefree t,

    a(core(t))*sigma(t)/t <=(35/27)d_3(t).                         (11.4)

Indeed at an exponent-one prime the local factor is
`(2+1/l)(1+1/l)`. It is <=3 for l>=5; at l=2 its ratio to 3 is
5/4, and at l=3 it is 28/27. Each exceptional prime occurs at most
once. At exponent two the factor is at most 7/4<d_3(l^2)=6.
Thus the exceptional TOTAL ratio is at most 35/27, not one factor
per prime. Also (2+1/p)(1+1/p)<=3 for p>Y/3 and large Y.
Since sum_(t<=T)d_3(t)<=T H_floor(T)^2, (11.1) yields pointwise

    |W^low(k)|<=12h1 Q_j/k * H_N^2
                         <=12h1 H_N^2 k^(rho-1).

The integral comparison for decreasing k^(2rho-2), starting at A>=2,
gives sum_(k=A)^(Yp_*-1)k^(2rho-2)<=Y^(4rho-2)/(2rho-1).
This proves the final root term of (11.2). Adding the full-source,
low-denominator and already restricted small-core bounds proves it.

The lower endpoint can also move. For A=ceil(Y^(2-delta)), fixed
0<delta<1, (11.2) gives energy

    <<_(delta,rho,epsilon) Y^(max(delta,4rho-2)+epsilon).            (11.5)

In particular one may retain all top-prime pairs from a window beginning
at Y^(2-delta) while paying any exponent larger than max(delta,4rho-2).
This neither estimates the native lower window nor removes the remaining
rough modes. It records exactly how far the concrete signed compensation
extends before the rectangular tail cost becomes too large.

## 12. A tempting global operator cancellation fails the target test exactly

The restriction in Section 11 is not removed by merely allowing output
filters. A concrete global cancellation is possible and cheap, but it
cancels every target top-prime pair. This gives an exact failed approach,
not a heuristic warning.

On L^2((0,infinity),dx) define the commuting dilation D_n f(x)=f(x/n),
whose norm is sqrt(n). Write

    P_J=sum_(n<=J)mu(n)D_n/n, T_Y=P_Y R,
    L_p=(D_p-1)P_J/p, J=floor(Y/p).

The FULL identity (4.1), with no output restriction, is exactly

    A_p=-2L_p P_Y R-L_p^2 R.                                      (12.1)

For top primes J=1 put H1=sum_(p in P1)(D_p-1)/p. Fix one middle prime
p0 in (Y/3,Y/2], so P_2=1-D_2/2 and
L_0=(D_(p0)-1)P_2/p0. Both factors are invertible bounded operators:

    (D_(p0)-1)^-1=sum_(j>=1)D_(p0)^(-j),
    P_2^-1=sum_(j>=0)2^-j D_(2^j).

These series converge in operator norm because the respective norm ratios
are p0^-1/2 and 2^-1/2. In particular

    ||L_0^-1|| <=p0/[(sqrt(p0)-1)(1-1/sqrt(2))].

The filtered compensator

    W_global=sum_(p in P1)A_p-H1 L_0^-1 A_(p0)

therefore exists globally and simplifies EXACTLY to the finite polynomial

    W_global=[H1 L_0-sum_(p in P1)(D_p-1)^2/p^2]R.                 (12.2)

Ordinary PNT and ||R||<=sqrt(3) give
||W_global||_2=O(1/log Y). Indeed ||H1||=O(sqrt(Y)/log Y),
||L_0||=O(Y^-1/2), and the square sum's operator norm is O(1/log Y).
Thus this really is a global small-norm identity.

It does NOT retain the desired detector. To see this without an estimate,
expand (12.2) in the canonical R-dilates. Its support contains only

    1,p,p^2,p0,2,2p,2p0,pp0,2pp0, for p in P1.

No such integer is divisible by two distinct top primes. Since Mobius
inversion gives R(x/d)=sum_(q|d)S_q(x), with S_1=R, the coefficient
of every S_(pl) for distinct p,l in P1 is EXACTLY ZERO.

Before filtering, sum_(p in P1)A_p has coefficient 4/(pl) on S_(pl).
Consequently the ostensibly middle-prime filtered term contributes
exactly -4/(pl). Its inverse dilations multiply the physical argument by
p0^j and thereby remove the middle prime from denominators; they can
create the target modes that the unfiltered middle incidence did not
contain. Treating that filtered term as target-orthogonal would be false.

Equivalently, substituting (12.1) shows directly

    -H1 L_0^-1 A_(p0)=[2H1 P_Y+H1 L_0]R,

a finite polynomial whose target response is the negative of the original
top incidence. The exact contraction is therefore bought by cancellation
of the target itself. Section 11's unfiltered active-prime method avoids
this particular loss, and its output restriction is a substantive part
of its proved scope. This operator calculation does not rule out other
target-preserving global constructions.

## 13. An exact coefficient-budget test using signed two-row minors

The adaptive problem in Section 10 need not be attacked by a uniform
smallest-singular-value estimate. There is a sharper necessary and
sufficient finite-dimensional test. It measures the target residual and
the nuisance dispersion together; a near rank failure is not expensive
if the target approaches the same row.

For any real vectors a_J=(v_J,d_J), J=2,...,L, and r=-(v_1,d_1),
let det denote the two-by-two determinant. If the a_J span R^2, then
there exist real lambda_J with

    sum_(J=2)^L lambda_J a_J=r, |lambda_J|<=K

if and only if, for every J=2,...,L,

    |det(a_J,r)|<=K sum_(H=2)^L |det(a_J,a_H)|.                    (13.1)

Consequently the EXACT minimum uniform coefficient budget is

    K_min=max_(J:a_J!=0)
       |v_J d_1-d_J v_1| / sum_(H=2)^L|v_J d_H-d_J v_H|.           (13.2)

The rank-two hypothesis makes every displayed nonzero-generator
denominator positive. Zero generators impose only the tautology 0<=0.
For prescribed unequal positive budgets K_H, replace the right side
of (13.1) by sum_H K_H|det(a_J,a_H)|. This permits paying different
analytic costs for different strata instead of taking their maximum.

Proof. The attainable targets form the centrally symmetric planar
zonotope Z=sum_H[-K,K]a_H. Each of its edges is parallel to some a_J;
this follows directly by adding line segments in order of angle. Its
support function in a normal n is K sum_H|n dot a_H|. The two opposing
facet inequalities normal to a_J are therefore exactly (13.1). A
convex polygon is the intersection of its facet halfplanes, proving
necessity and sufficiency. Scaling the individual generating segments
gives the unequal-budget statement. This is a finite convex-geometry
fact; no arithmetic randomness is assumed.

In rank one, choose any nonzero generator a. Compatibility requires
det(a,r)=0. If all generators are zero, compatibility is exactly r=0.
Otherwise write a_H=t_H a and r=t a; the exact condition is
|t|<=K sum_H|t_H|, with the obvious unequal-budget version. These cases
must be checked rather than deleting singular output cells. For the
initial d=0 state of Section 10 the condition reduces to

    |v_1|<=K sum_(J=2)^L |v_J|.

This criterion separates the needed arithmetic assertion from a stronger
operator-norm assertion. A small Gram determinant by itself does not
invalidate (13.1), and a good singular value at finitely many outputs
does not establish it uniformly. The arithmetic quantities d_J are
still the literal complete future defects, so (13.1) is not a proof of
their required bound.

The optional `--box-bound` mode of `certify_conditioning.py` checks all
these facet inequalities with directed integer intervals at every state
of its declared finite window. It uses the already authenticated rank
partition; each pair minor is computed once and added to both relevant
facet capacities. This is an independent existence certificate for a
coefficient budget, which can be smaller than the budget of the explicit
minimum-Euclidean-norm solution in (10.4). Its scope is exactly the
prefix and physical cells recorded in its receipt.

## 14. Global transport in an enlarged actual old-pair probe class

`GLOBAL_TRANSPORT.md` gives a separate stronger component construction.
It retains the complete strict native step and both original masks,
preserves every distinct top-prime-pair coefficient, and has subpower
coherent energy for any fixed 1/2<rho<5/8 and subpower core schedule.
It does not need a native sign crossing. The proof uses the uniform
classical short-interval squarefree count stated there, a pointwise
complete harmonic-jump lemma, a sharp near-balanced lattice count,
the resource form of (6.2), and complete small-core root bounds.

Its scope differs from the prime-incidence results above: it weights
actual old ordered Mobius pairs by O(sqrt(Y)), and may create nonzero
coefficients where the original aggregate C_Y(q) vanished. All new terms
are explicit and paid; it is not an arbitrary denominator contraction.
The complete reweighted complementary source remains unestimated. The
construction therefore removes the actual large positive sector without
claiming a full rough-core contraction or a new zeta boundary.

## 15. Complete-source reductions and the current exact open target

The later files retain these definitions and isolate stronger complete
source statements rather than changing any earlier scope.

`DIAGONAL_COMPRESSION.md` first transports the entire original signed
source at every product scale to near-balanced actual old pairs, with
all projections paid. `FLUX_COMPRESSION.md` proves that the compact
signed transport flux has a small fractional Sobolev norm. Its exact
Mellin multiplier is zeta on the critical line, so the corrected classical
Weyl bound gives a decaying global transport error. The complete original
native source and the explicit balanced source therefore differ by
subpower energy on every strict square step. No estimate for that
remaining source is asserted.

`MASKED_COMPRESSION.md` applies the same argument to the original mask
FIRST. Each fixed native annulus has exact R coefficients
alpha_(j,d)=sum_(d|q)mu(q/d)omega_j(q)C_Y(q)<<Y^epsilon/d.
Low d and the full top corner are paid directly at the actual integers.
This permits ANY prefix-dependent original core cutoff, including the
polynomial energy-adaptive budget imported explicitly from #1002. The
new target is its full annular reference R source; no fresh reference
core projection is taken. Its source error is subpower, so a successful
actual a,p contraction would have no artificial exponent floor.

`SQUARE_COMPRESSION.md` supplies a deliberately simpler one-dimensional
alternative: an explicit signed square-shell moving average times
R(k/r^2), with all original masks encoded in the coefficients. Its error
energy is Y^(2/3+epsilon), and its optional small-root sector is also
paid. The conditional zero-boundary floor is 2/3; a hypothetical 5/6
target is compatible with this larger error, but RH does not follow.
That file proves why projecting away its low-core reference squares
would be invalid: a legal small deformation can be amplified by at
least Y^(2/3-epsilon)/log(Y)^2 under that fresh core projection.

These reductions leave actual signed local z_Y or masked-C_Y averages.
Their apparent reference Mobius signs are canceled by their exact
weights. The transported actual positive prime sector still has large
energy inside the same balanced geometry, ruling out a generic improving
operator bound based only on support and weight caps. The complete
signed cancellation estimate remains OPEN after all these constructions.
