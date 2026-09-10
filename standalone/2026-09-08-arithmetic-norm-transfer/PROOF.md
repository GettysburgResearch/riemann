# Native cancellation and the sharp divisor-to-residual norm transfer

Date: 2026-09-08. Author research continuation of PR #803.
Status: PROPOSED COMPONENT PROOFS; independent mathematical/code review required.
**No complete unconditional proof of RH is obtained.**
The source-specific subpower residual bound and sparse-sign saving remain open.
Local labels ANT1--ANT5 are not canonical acceptance identifiers.

## 0. The attempted synthesis and its outcome

The post-integration corpus now contains full-source norm certification (#803),
quantitative capture toward an intrinsic source-space floor (#817/#819),
summable within-cell prime detail (#818), and actual prime-power graph gaps
(#790/#825/#826). I tested the proposed closing step: use the latter arithmetic
gap to control the former physical residual. This note proves the sharp size
of that missing adapter on fixed-ratio tail blocks. It loses a factor of order
Y/log Y, not a polylogarithm. That statement is established inside the literal
arithmetic completion class, even with its two safe jets and centering retained.
It does NOT refute a special bound for a selected native minimizer.

There is a constructive result as well: an explicit three-block completion
simultaneously has the exact Mobius prefix, p(1)=0, p'(1)=1, p(0)=-2, bounded
coefficients, and logarithmic coefficient norm, with support below 8Y. Using
only classical unconditional Mertens cancellation and zeta convexity, its FULL
physical energy is O(Y exp(-c (log Y)^(3/5)(log log Y)^(-1/5))). This improves
the elementary linear bound but supplies no fixed power saving. The general
method and imported analytic estimates are classical; external novelty is not
claimed. The finite tests do not prove the infinite arguments.

## 1. Objects and exact metric identities

Write mu for the ordinary Mobius function, and Lambda(p^k)=log p for EVERY
prime power. Coefficients at nonsquarefree correction indices are allowed.
For a finite real polynomial p(s)=sum a_n n^(-s) with p(1)=0 define

    A_p(x)=sum a_n floor(x/n),
    E(p)=integral_1^infinity |1-A_p(x)|^2 dx/x^2.             (1)

For a balanced variation q(s)=sum c_n n^(-s), define instead

    R(q)=integral_1^infinity |A_q(x)|^2 dx/x^2,
    S(q)=sum |c_n|^2/n.                                     (2)

R is a homogeneous variation norm. E is the affine target norm; they must
not be equated. For support <=N, put c_n=0 at every omitted index and

    G_N(q)=sum_(p^k j<=N) (log p)/(p^k j)
                                  |c_(p^k j)-c_j|^2.        (3)

This is exactly the complete divisor form of #790/#825/#826 in their f(n)=c_n
coordinates, or their Euclidean coordinates v_n=c_n/sqrt(n). No graph metric is
silently replaced. All vertices 1,...,N and all allowed prime powers are retained.
In particular balance is orthogonality to the harmonic null vector in Euclidean
coordinates; it does not identify G_N with R.

If p agrees with mu below integer Y>=2, Mobius inversion gives A_p=1 on [1,Y).
Balance gives A_p=-sum a_n {x/n}, so the full norm (1) is finite. Termwise
integration for Re s>1, followed by continuation using boundedness of the error,
gives

    integral_1^infinity (1-A_p(x))x^(-s-1)dx
                              =[1-zeta(s)p(s)]/s, Re s>0.    (4)

The possible pole at one is removable. After t=log x, Fourier Plancherel gives

    E(p)=(1/(2pi))integral_R
           |1-zeta(1/2+it)p(1/2+it)|^2/(1/4+t^2)dt.          (5)

The same reasoning with zero target applies to R. These are complete norms,
not finite-frequency formulas or formal contour shifts across zeta zeros.

## 2. ANT1: three exact normalizations with bounded coefficients

For every integer Y>=2 set

    m_Y=sum_(n<Y) mu(n)/n,
    l_Y=sum_(n<Y) mu(n)log n/n,
    ell_Y=(1/Y)sum_(Y<=n<2Y)log n,
    s_Y=sum_(n<Y)mu(n),
    t_Y=(m_Y ell_Y-l_Y-1)/log2,
    u_Y=(-2-s_Y)/[(3Y-1)/2].                               (6)

Let

    A_Y=u_Y-2t_Y,
    B_Y=3t_Y-2u_Y-2m_Y,
    C_Y=u_Y+m_Y-t_Y,
    Q_Y(s)=(1/Y)sum_(Y<=n<2Y)n^(1-s),
    p_Y^c(s)=sum_(n<Y)mu(n)n^(-s)
                    +Q_Y(s)[A_Y+B_Y 2^(1-s)+C_Y 4^(1-s)]. (7)

**ANT1.** This prescribed polynomial, with no solve or zero input, satisfies

    p_Y^c[n]=mu(n) for n<Y;
    p_Y^c(1)=0, (p_Y^c)'(1)=1, p_Y^c(0)=-2;
    support(p_Y^c) subset [1,8Y);
    |p_Y^c[n]|<84;
    S(p_Y^c)<1924+log Y.                                  (8)

The last norm is the coefficient diagonal, not E. Centering p(0)=-2 makes the
mean of 1-A_p over a common integer period zero; it does not make E zero.

Proof of the identities. Q_Y(1)=1, Q_Y'(1)=-ell_Y, Q_Y(0)=(3Y-1)/2. Directly,

    A_Y+B_Y+C_Y=-m_Y,
    B_Y+2C_Y=t_Y,
    A_Y+2B_Y+4C_Y=u_Y.

These give the three displayed jets and the prescribed prefix. The blocks
n,2n,4n with Y<=n<2Y are disjoint. Their coefficients are A_Y n/Y,
2B_Y n/Y, and 4C_Y n/Y, respectively.

Here are the elementary bounds, rederived to specify the all-Y scope. From
sum_(n<=K)mu(n)floor(K/n)=1 and the vanishing fractional part at n=1,
|sum_(n<=x)mu(n)/n|<=1. Write

    F(x)=sum_(n<=x) mu(n)log(x/n)/n.

The EXACT harmonic divisor identity
sum_(n<=x)mu(n) H_floor(x/n)/n=1 and

    H_floor(v)=log v+gamma+epsilon(v), |epsilon(v)|<=1/v

give |F(x)-1|<2. One proof of the last harmonic estimate is to bound
H_K-log K-gamma between 1/[2(K+1)] and 1/(2K), by telescoping integrals;
then let K<=v<K+1 and use log(1+1/K)<=1/K (K=1 separately).
At x=Y the final term of F is zero. Since 0<=ell_Y-log Y<log2,

    |t_Y| <= |m_Y|+(|F(Y)-1|/log2)<5,
    |u_Y| <= (Y+1)/[(3Y-1)/2]<2.

Here log2>1/2. Hence |A_Y|<12, |B_Y|<21 and |C_Y|<8. This proves the
coefficient bound. The exact coefficient norm is

    S(p_Y^c)=sum_(n<Y)mu(n)^2/n
       +(3Y-1)/(2Y) [A_Y^2+2B_Y^2+4C_Y^2].                (9)

The bracket is <144+882+256=1282. The prefix is <=1+log Y, proving (8).
No PNT or statistical model is used in ANT1. Its construction does NOT promise
a bounded-factor approximation to a previous physical-energy minimizer.

## 3. ANT2: an unconditional upper bound for the FULL native energy

Let Phi(v)=v^(3/5)(log v)^(-1/5), for v sufficiently large. We import precisely
the classical unconditional Mertens estimate [E1]: for some positive constants
K,a,x0,

    |M(x)|<=K x exp(-a Phi(log x)), x>=x0,
    M(x)=sum_(n<=x)mu(n).                                  (10)

No numerical values, zero census, or external computation are rerun here. We
also use the coarse UNCONDITIONAL convexity consequence of the approximate
functional equation [E2], enlarged on a compact interval:

    |zeta(1/2+it)|^2 <= K_zeta (1+|t|)^(5/8), t real.        (11)

Only finiteness of these constants is used. In particular neither input is
RH-conditional or a critical-line estimate for 1/zeta.

**ANT2.** There are positive c,C such that for all sufficiently large Y,

    E(p_Y^c) <= C Y exp(-c Phi(log Y)).                     (12)

Consequently E(p_Y^c)=o(Y) and E(p_Y^c)=O_A(Y/(log Y)^A) for every fixed A>0.
By enlarging C and extending Phi harmlessly over a fixed initial interval,
(12) has an all-Y version. No numerical threshold or constant is certified.
This is a consequence of classical-scale cancellation, NOT a new Mertens bound,
not a new zero-free region, and not a bound O(Y^(1-delta)) for any fixed delta.

### 3.1 The moments and the prefix at all frequencies

For every fixed nonnegative integer j and L large, (10) implies

    integral_L^infinity (1+v-L)^j exp(-a Phi(v))dv
                                      <= C_j exp(-a_j Phi(L)). (13)

Indeed Phi(v)/sqrt(v) is increasing for v>=e^2, so Phi(v)>=Phi(L)sqrt(v/L).
Substitute y=sqrt(v/L). Integrating the resulting polynomial times
exp(-a Phi(L)y) gives a polynomial in L and Phi(L)^(-1) times exp(-a Phi(L)).
Since log L=o(Phi(L)), decreasing a_j absorbs that polynomial. This proves
(13) including j=0,1 needed below, without an unbounded log loss.

Partial summation now makes sum mu(n)/n and sum mu(n)log n/n converge; their
values are 0 and -1, respectively, by Abel's theorem for the reciprocal Euler
series as real s decreases to 1. Normal convergence is only needed on Re s>1;
the absolutely controlled coefficient tails justify these boundary limits.
Therefore

    m_Y=O(exp(-a1 Phi(log Y))),
    F(Y)-1=sum_(n>=Y)mu(n)log(n/Y)/n
                         =O(exp(-a1 Phi(log Y))).           (14)

For the second equation, differentiate the TEST weight log(x/Y)/x inside
partial summation; (13) pays its complete tail. Its value at Y is zero.
Since |s_Y|<=K Y exp(-a Phi(log(Y-1))) for Y large, (6),(14) imply

    |A_Y|+|B_Y|+|C_Y| <=K1 exp(-a1 Phi(log Y)).             (15)

The fixed -2 in u_Y costs only O(1/Y).

For ALL real t, split the twisted prefix at sqrt(Y). Bound its initial part
absolutely by 2Y^(1/4). On [sqrt(Y),Y-1/2], Stieltjes partial summation and
(10), with the derivative of x^(-1/2-it), give

    |sum_(n<Y)mu(n)n^(-1/2-it)|
       <=K2(1+|t|)sqrt(Y) exp(-a2 Phi(log Y)).              (16)

The use of Y-1/2 retains exactly n<Y. The factor (1+|t|) is NOT suppressed.
Monotonicity and Phi((log Y)/2)>=2^(-3/5)Phi(log Y) justify a fixed a2>0.
The initial Y^(1/4) is absorbed since Phi(log Y)=o(log Y).
Using |Q_Y(1/2+it)|<=2sqrt(Y) and (15) gives the same bound for p_Y^c.
Separately its literal coefficient formula gives |p_Y^c(1/2+it)|<=B sqrt(Y)
for an absolute B, every Y and every t. Thus for some 0<delta_Y<=1/2 tending
to zero with delta_Y=O(exp(-a3 Phi(log Y))),

    |p_Y^c(1/2+it)|/sqrt(Y)
                       <= min(B,delta_Y(1+|t|)).            (17)

### 3.2 A complete frequency integral, not a pointwise-to-global shortcut

Insert (17) into (5), using |1-zeta p|^2<=2+2|zeta|^2|p|^2. The constant
term contributes exactly 2. For the other term, split at T=1/delta_Y.
Equations (11),(17) give, including BOTH frequency tails,

    E(p_Y^c) <=2+K3 Y [
          delta_Y^2 integral_0^T (1+t)^(5/8)dt
             + B^2 integral_T^infinity (1+t)^(-11/8)dt]
             <=2+K4 Y delta_Y^(3/8).                      (18)

The bounded ratio (1+t)^2/(1/4+t^2) and its reciprocal comparison are
absorbed in K3; no frequency is omitted. The two integrals are elementary.
Since Y exp(-c Phi(log Y)) tends to infinity, the constant 2 is absorbed.
This proves (12). The same proof applies to the parent's two-endpoint
p_Y^sharp, replacing (15) by its two moment bounds; its earlier O(196Y)
bound likewise has this classical-scale improvement.

## 4. ANT3: what a divisor gap can transfer to a physical norm

Fix A>=2 and suppose q is supported on integers [Y,N], N<=AY, with q(1)=0.
Its coefficients can be complex and arbitrarily large. Write

    psi(A)=sum_(2<=r<=A)Lambda(r),
    C(A)=log A+sum_(2<=r<=A)Lambda(r)/r
                         +2sum_(2<=r<=A)Lambda(r)/sqrt(r).

**ANT3.** Uniformly over all such q,

    R(q) <= A^2 Y S(q),
    G_N(q) >= [log Y-psi(A)] S(q),
    |G_N(q)-(log Y)S(q)| <= C(A)S(q).                    (19)

In particular, if log Y>=2psi(A),

    R(q) <=2A^2 (Y/log Y) G_N(q).                        (20)

These are statements in the actual two metrics, not an identification of them.

Proof. A_q vanishes below Y, and balance bounds its absolute value by sum|c_n|.
Weighted Cauchy--Schwarz gives (sum|c_n|)^2 <= S(q)sum_(n<=N)n<=N^2 S(q).
Integrating x^-2 above Y proves the first inequality.

For each child n in the coefficient support, retain only downward edges whose
parent n/r<Y. Their squared difference is |c_n|^2. The total log-prime weight
of ALL downward edges is sum_(r|n)Lambda(r)=log n. The excluded downward
weight is at most psi(n/Y)<=psi(A). This proves the second inequality by
positivity of all other edges. No squarefree restriction is made.

For the third, expand (3) in Euclidean coordinates v_n=c_n/sqrt(n): its
diagonal is log n+M(N/n), M(x)=sum_(r<=x)Lambda(r)/r. Both endpoints of an
internal cross edge lie in [Y,N], so its ratio is at most A. The shift sending
coordinate j to rj has norm at most one, and its coefficient is Lambda(r)/sqrt(r).
Thus the internal cross operator has norm at most 2sum_(r<=A)Lambda(r)/sqrt(r).
Also log(n/Y)<=log A and M(N/n)<=M(A). This proves (19), and (20) follows.
The unconditional whole-graph upper bound G_N(q)<=2(log N+3)S(q) follows by
expanding the squares and M(x)<=log x+3. The latter follows from the exact
factorial identity and the elementary psi(x)<3x bound.

## 5. ANT4: the factor Y/log Y is necessary even with the exact jets

Set

    q_Y(s)=Q_Y(s)(1-2^(1-s))^2(1-2^(-s)).                  (21)

In the variable z=2^(-s), the polynomial multiplier is

    (1-2z)^2(1-z)=1-5z+8z^2-4z^3.                       (22)

Its coefficients are, for Y<=n<2Y, respectively

    c_n=n/Y, c_(2n)=-5n/Y, c_(4n)=8n/Y, c_(8n)=-4n/Y.   (23)

The four blocks are disjoint and supported below 16Y. Exactly,

    q_Y(1)=q_Y'(1)=q_Y(0)=0,
    |c_n|<16,
    S(q_Y)=(3Y-1)/(2Y)*(63/2) <189/4.                   (24)

**ANT4.** At EVERY integer Y>=2,

    R(q_Y)>=Y/24,
    G_(16Y)(q_Y)<(189/2)[log(16Y)+3].                    (25)

On x in [3Y/2,2Y), only the first coefficient block is active, and each
floor(x/n) there is 1 when n<=x and 0 otherwise. At least Y/2 such terms
have n/Y>=1, so A_q(x)>=Y/2. Its square integrates to at least
(Y^2/4)[2/(3Y)-1/(2Y)]=Y/24. Endpoints have measure zero.
The graph bound follows from (24) and the whole-graph bound after (20).

Let Gamma(Y) be the supremum of R(q)/G_(16Y)(q) over nonzero REAL variations
supported in [Y,16Y] with q(1)=q'(1)=q(0)=0. The graph denominator is positive:
a constant coefficient null vector with zero coordinates below Y must vanish.
Then (20),(25) prove

    Gamma(Y) = Theta(Y/log Y).                            (26)

For example its lower bound is Y/[2268(log(16Y)+3)], and its upper bound is
512Y/log Y whenever log Y>=2psi(16). Constants are deliberately not optimized.
Thus NO polylogarithmic, or Y^epsilon with epsilon<1, coefficient-uniform
transfer from this graph energy to the physical variation norm can hold.
A stronger gap for the same graph cannot remove this already witnessed loss.

### 5.1 The obstruction is inside the admissible native-prefix class

Use the centered normalized p_Y^c from (7). BOTH p_Y^c+q_Y and p_Y^c-q_Y
retain the SAME literal Mobius prefix, p(1)=0, p'(1)=1 and p(0)=-2. Both
have support below 16Y, uniformly bounded coefficients and S=O(log Y).
Their graph energies are consequently O((log Y)^2), by the whole-graph bound.
But the exact parallelogram identity gives

    [E(p_Y^c+q_Y)+E(p_Y^c-q_Y)]/2=E(p_Y^c)+R(q_Y).       (27)

In particular at least one has E>=Y/24. The sign choice may depend on Y.
In contrast ANT2 gives E(p_Y^c)=o(Y). These variations do not change the
underlying zeta function or assert a nonreal zero. They are different allowed
representations; (27) does NOT say that their constrained minimum is large.

For any FIXED numbers of jets r>=2 and t>=1, replace (21) by
Q_Y(s)(1-2^(1-s))^r(1-2^(-s))^t. It has zeros of orders r at 1 and t at 0,
unchanged initial coefficient block, support below 2^(r+t+1)Y, and S=O_(r,t)(1).
The same low-interval proof gives R>=Y/24, while (19) gives G=O_(r,t)(log Y).
Thus adding any fixed finite number of these moment constraints does not
repair the uniform comparison. No uniformity as r or t grows is claimed.

## 6. ANT5: the explicit comparison has a full, computable limit

For the fixed q_Y in (21), set d=(1,-5,8,-4) and define

    H(t)=integral_1^2 v floor(t/v)dv,
    F(t)=sum_(j=0)^3 d_j H(t/2^j),
    C_*=integral_1^infinity F(t)^2 dt/t^2.                (28)

Riemann sums in v, with finitely many jumps for each fixed t, show
A_(q_Y)(Yt)/Y -> F(t). Balance and the coefficient bound give a uniform
constant bound for A_(q_Y)(Yt)/Y; it vanishes for t<1. Dominated convergence
against dt/t^2 yields

    R(q_Y)/Y -> C_*,
    G_(16Y)(q_Y)/log Y ->189/4,
    (log Y/Y) R(q_Y)/G_(16Y)(q_Y) ->4C_*/189.              (29)

The graph limit follows from (19),(24), with A=16 fixed. It is a limit for
this explicit sequence, NOT the optimal leading constant in (26).
On 1<t<2, F(t)=(t^2-1)/2, so C_*>=5/24>0.

For a complete tail bound, write B1(u)={u}-1/2 and take its periodic primitive
B2({u})/2, of absolute value at most 1/12. Changing variables v=t/u gives

    H(t)=t-3/4-t^2 integral_(t/2)^t B1(u)u^(-3)du,
    |H(t)-t+3/4|<=4/(3t).                               (30)

Integration by parts proves the bound, including the boundary contributions.
Since sum d_j/2^j=sum d_j=0 and sum |d_j|2^j=75,

    |F(t)|<=100/t,
    integral_T^infinity F(t)^2 dt/t^2<=10000/(3T^3).       (31)

Every finite integral can be evaluated rationally. On a unit cell [r,r+1),
put U_j=floor(r/2^j), L_j=floor(r/2^(j+1)) and H2_k=sum_(h<=k)1/h^2. Then

    F(t)=A_r t^2+B_r,
    A_r=sum_j d_j[H2_(U_j)-H2_(L_j)]/(2*4^j),
    B_r=sum_j d_j(2L_j-U_j/2).

Consequently the exact cell integral is

    A_r^2(3r^2+3r+1)/3+2A_r B_r+B_r^2/[r(r+1)].          (32)

The checker sums all 4095 cells through T=4096 using Fraction arithmetic and
adds (31). The resulting outward enclosure is

    1.704219450036 < C_* < 1.704219498544.                (33)

This is a certificate for the explicit non-Mobius VARIATION profile, not a
new native zeta sign or minimum. No quadrature or floating constant enters it.

## 7. End-to-end attempt: the precise stopped step

The new native bound (12) is asymptotically stronger than O(Y), but for every
fixed delta>0,

    Y exp(-c Phi(log Y)) / Y^(1-delta) -> infinity.       (34)

This compares two bounds; it is NOT a lower bound on E. It therefore supplies
neither a fixed power saving nor the needed subpower upper bound. It remains
compatible with every hypothetical-zero obstruction

    E(p)>=(2beta-1)Y^(2beta-1)/|1-rho|^2, beta>1/2,

and with the parent's unevaluated exponent 2Theta-1, including Theta=1.
The latter lower bound follows from the exact delayed Hardy value plus the
safe-jet constraint, not from the divisor graph. Its source is pinned in
SOURCES.json; it is not independently accepted by finite tests here.

The attempted shortcut from the new graph gaps to small residual norms fails
by (26)-(27). Those gaps remain useful for the graph and its identified cusp
sector. They do not lose their validity because the physically different norm
has an expensive comparison. Conversely this does NOT rule out a genuinely
native-specific upper estimate for a carefully selected minimizer, a new
source factorization, or a proof using the exact functional equation.

A sufficient closing construction is still: finite p_j with prefix mu below
Y_j->infinity, both safe normalizations, and log(1+E(p_j))/log Y_j->0. Any one
off-line zero would contradict it. Nothing here constructs that sequence.
The current proof record must therefore NOT be sent as a completed RH proof.

## References and import scope

[E1] E. S. Lee and N. Leong, New explicit bounds for Mertens function and the
reciprocal of the Riemann zeta-function, arXiv:2208.06141v4, Theorem 1.2.
https://arxiv.org/html/2208.06141v4 . Only existence of positive constants in
(10) is imported; external numerical constants and certificate campaigns are
not reproduced or needed here.

[E2] NIST DLMF 25.9, https://dlmf.nist.gov/25.9 . The approximate functional
equation supplies the classical convexity consequence (11), after absorbing
logarithms. Fourier Plancherel, Abel's theorem, dominated convergence and
partial summation are the other standard analytic inputs.

The graph identity/path-gap literature in the source PRs and the Nyman--Beurling
lineage are explicitly contextual dependencies, not claimed inventions of this
note. No external priority assessment or formal Lean verification is claimed.
