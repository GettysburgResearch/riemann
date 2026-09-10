# PCR26: bounded native completions and the off-diagonal collision problem

**Status: PROPOSED component proofs, pending independent mathematical review.**
**RH and the all-scale native covariance estimate remain OPEN.**

Date: 2026-09-10. Parent research: PR848 at
`6671339d48c7f9bb846c15d8265e53f6856c2852`.
This is a new source construction and estimate, not a change to the earlier
one-atom optimum or a claim that a previously open bound has been verified.
All claims below are rederived. Summation by parts, Dirichlet/Newton inversion,
positive Gram decompositions and divisor bounds are classical; no broad
priority claim is made.

## 0. Exact objects and the full-problem target

For a finite real sequence a indexed by positive integers, put

    A_a(x)=sum_(n<=x) a_n, P_a(s)=sum a_n n^(-s),
    m_a(k)=sum_(n<=k) a_n/n,
    J(a)=integral_1^infinity A_a(x)^2 dx/x^2.

The integral includes the whole future after the last nonzero coefficient.
For the actual Mobius function, use

    M(k)=sum_(n<=k) mu(n), m(k)=sum_(n<=k) mu(n)/n,
    F_Y=sum_(k=1)^Y m(k)^2, E_Y=sum_(k=1)^Y M(k)^2/[k(k+1)],
    b=Y+1, B=b^2-1.

These are NOT natural or probabilistic averages over replacement coefficients.
Dirichlet convolution is `(a*c)(n)=sum_(d|n)a(d)c(n/d)`; the constant arithmetic
function is `1(n)=1`, and delta is its convolution identity.

The exact identities

    J(a)=sum_(k>=0)(P_a(1)-m_a(k))^2,
    E_Y=F_Y-(Y+1)u_Y^2 <= F_Y,
    u_Y=(1/(Y+1))sum_(k=0)^Y m(k)                         (0.1)

follow by `1/max(r,s)=min(r,s)/(rs)` and finite summation by parts. When
P_a(1)=0, the innovations m_a(k) are orthonormal source coordinates.
The earlier NIR26 proof supplied these identities. A subpower bound for F_Y
on the square ladder would imply RH; Section 5 reconstructs that ending.

The objective here is to use actual arithmetic before bounding the quadratic
extension. We first remove a representation-created large coefficient. This
makes the COMPLETE coalesced product diagonal polylogarithmic at every scale.
Only then do we separate and attempt to bound the signed cross term.

## 1. PCR26-1: the minimum-energy completion with bounded coefficients

### 1.1 The native endpoint is bounded without a prime-error theorem

The complete divisor identity `sum_(d|n)mu(d)=delta_(n=1)` implies

    sum_(r<=Y)mu(r)floor(Y/r)=1,
    Y m(Y)=1+sum_(r<=Y)mu(r){Y/r}.

The r=1 fractional part is zero. Since |mu(r)|<=1, this gives

    |m(Y)|<=1,                                           (1.1)

with strict inequality when Y>1. No PNT, RH, random signs, or unproved
cancellation estimate is involved. This is the first use of native arithmetic.

### 1.2 Exact clipped completion

Let a=|m(Y)|, epsilon=sign(m(Y)), and r_0=a. Preserve `c_n=mu(n)` for n<=Y.
For j>=1, until the residual first reaches zero, define

    c_(Y+j)=-epsilon * min(3, (Y+j) r_(j-1)),
    r_j=max(0, r_(j-1)-3/(Y+j)).                          (1.2)

All later coefficients are zero. When a=0, no tail is added. Let J be the
number of added coefficients and L=Y+J (L=Y in the zero-tail case). Then

    |c_n|<=3, P_c(1)=0,
    J<=ceil(Y/2), L<=Y+ceil(Y/2)<=2Y,                    (1.3)
    m_c(Y+j)=epsilon r_j.

To prove termination, put h=ceil(Y/2). The available reciprocal correction is

    sum_(j=1)^h 3/(Y+j) >= 3h/(Y+h) >=1 >= a.

Thus the construction stops in the stated finite interval. It is a rational
algorithm on the known prefix, with no new Mobius coefficient as input.
The sign of the last coefficient is fixed and its magnitude is at most three.

### 1.3 A paid trace estimate

For 1<=j<=ceil(Y/2),

    3/(Y+j) >= 1/(Y-j+1),

since `2Y+3>=4j`. Hence

    r_j <= (a-sum_(i=1)^j 1/(Y-i+1))_+
         <= |m(Y-j)|.                                   (1.4)

The second inequality is the reverse triangle inequality and
`|m(Y)-m(Y-j)|<=sum_(i=1)^j 1/(Y-i+1)`.
Consequently, with the tail innovations counted at every integer,

    T_Y:=sum_(k=Y+1)^(L-1) m_c(k)^2 <= F_Y,
    J(c)=F_Y+T_Y <=2F_Y.                                 (1.5)

This retains, rather than discards, the normalization price. It also explains
why merely spreading a large collar uniformly is not enough: the stopping
length must respond to the actual endpoint magnitude.

### 1.4 Optimality in the stated bounded-tail class

Among all finite real completions preserving the prefix, satisfying P(1)=0,
and obeying |a_n|<=3 for n>Y, (1.2) uniquely minimizes J. Indeed at every future
index Y+j the triangle inequality forces

    |m_a(Y+j)| >= (a-3 sum_(i=1)^j 1/(Y+i))_+=r_j.

The clipped construction attains all these lower bounds simultaneously. Until
zero is attainable it uses the maximum opposite-sign correction; afterward
its innovations vanish identically. Equality of the whole sum of squares
forces those same innovations, hence the same coefficients. This is a finite
attained optimum, not just an infimum over progressively later tails.

The one-atom source in NIR26 has smaller unrestricted energy F_Y but may have
an unbounded coefficient `(Y+1)m(Y)`. Our new source pays at most a factor two
for a UNIFORM coefficient cap. The earlier norm-one projection onto the new
native prefix is unchanged. No previous optimum is overwritten.

## 2. PCR26-2: exact Newton extension and centered dilation packets

For the bounded source c, define the coalesced integer product coefficients

    z(d)=(c*c)(d)=sum_(rs=d)c_r c_s, 1<=d<=L^2,
    v=2c-1*z,
    q(k)=sum_(n<=k)v(n)/n.

All pairs with the SAME integer product are summed into z(d) BEFORE any square
or diagonal estimate. Splitting such a term into multiple artificial atoms
would change the diagonal and is not this construction.

### 2.1 Exact native prefix, independent of the later completion

Set e=delta-1*c. The native divisor equations give e(n)=0 for n<b. Algebra in
the convolution ring gives

    mu-v=mu*e*e,
    v(n)=mu(n) for n<b^2,
    mu(b^2)-v(b^2)=e(b)^2.                                (2.1)

The endpoint b^2 is not silently included. This is the classical short-source
Newton identity, here applied to a different, bounded completion. It uses ALL
prefix divisor equations, not merely the reciprocal moment in (1.1).

### 2.2 Exact centering, not an independence assumption

Let H_0=0, H_j=sum_(r=1)^j 1/r. For d,k>=1 define

    kappa_d(k)=[H_floor(k/d)-H_k+log d]/d.                 (2.2)

The source moment P_c(1)=0 gives the two exact finite identities

    sum_d z(d)/d=0,
    sum_d z(d)log d/d=0.                                  (2.3)

The latter is twice the product of `sum c_n/n` with `sum c_n log n/n`.
Equivalently every prime-log coefficient vanishes separately, because the
valuation v_p(d) is additive on products. The checker verifies those rational
prime-by-prime identities; it does not infer equality of transcendental numbers
from a rounded numerical sum.

Finite divisor summation now yields, for EVERY integer k>=1,

    q(k)=2m_c(k)-Q_Y(k),
    Q_Y(k)=sum_d z(d) kappa_d(k)
          =sum_d z(d)H_floor(k/d)/d.                     (2.4)

Thus the aggregate Q_Y(k) is rational even though the individual centered
packets contain logarithms. Every integer endpoint in H_floor(k/d) is literal.
No Fourier midpoint convention or replacement of floor by its average is used.

### 2.3 The whole source is legitimate

For x>=L the cumulative output is

    V(x)=2 sum c_n-sum_d z(d)floor(x/d)
        =2 sum c_n+sum_d z(d){x/d}.

Hence |V(x)|<=K:=2|sum c_n|+(sum |c_n|)^2. Its physical energy is finite and
its tail above X>=L is at most K^2/X. The packet bound below implies q(k)->0
and q belongs to ell2. Applying (0.1) to finite prefixes of v, or summation by
parts with the bound on V, gives the whole identity

    J(v)=sum_(k>=1)q(k)^2.                                (2.5)

For example `q(k)=V(k)/k-integral_k^infinity V(x)dx/x^2` and the finite
mean term vanishes in the limit. The full output is not truncated merely
because c and z have finite support. Projection onto k<=B is still exactly
c_B in NIR26's unrestricted innovation coordinates, and has norm one.

## 3. PCR26-3: a complete polylogarithmic collision-diagonal bound

### 3.1 Universal packet energy

For every integer d>=1,

    sum_(k>=1) kappa_d(k)^2 <=18/d.                      (3.1)

Here kappa_1=0. To prove the uniform bound, let

    r(t)=H_floor(t)-log t-gamma, t>0.

The elementary integral bounds for harmonic numbers give 0<gamma<1 and
`0<H_n-log n-gamma<1/n`. For n<=t<n+1, these imply

    |r(t)|<=1/t when t>=1,
    |r(t)|<=log(1/t)+1 when 0<t<1.

For the lower estimate in the first line use
`H_n=H_(n+1)-1/(n+1)`; for the upper estimate use
`log(t/n)>=1/n-1/t`. These avoid any uniformity problem between integer cells.
Therefore

    sum_(k>=1)r(k/d)^2 <=5d+2d=7d,
    sum_(k>=1)r(k)^2 <=2.

The first term is bounded by the decreasing-function integral
`integral_0^d (log(d/t)+1)^2 dt=5d`; the remaining reciprocal-square tail is
at most 2d. Since `kappa_d(k)=[r(k/d)-r(k)]/d`, (3.1) follows from
`(u-v)^2<=2u^2+2v^2`:

    sum kappa_d^2 <=14/d+4/d^2<=18/d.

Also |kappa_d(k)|<=2/k for k>=d. Thus the entire omitted packet tail from
k=R>=max(d,2) is at most 4/(R-1). For the aggregate Q after k>=L^2,

    sum_(k>R) Q_Y(k)^2 <=4 (sum_d |z(d)|)^2/R, R>=L^2.   (3.2)

This is a complete infinite-tail inequality, not a frequency-window estimate.

### 3.2 All product coincidences are paid

Because |c_n|<=3,

    |z(d)|<=9 tau_2(d),
    tau_2(d)^2<=tau_4(d).

The second bound follows prime power by prime power:
`(e+1)^2<=binomial(e+3,3)` is equivalent to `e(e-1)>=0`.
Thus

    sum_(d<=L^2) z(d)^2/d
        <=81 sum_(d<=L^2)tau_4(d)/d
        <=81 H_(L^2)^4.                                  (3.3)

For the last inequality, expand tau_4 as the number of ordered quadruples
with product d, and enlarge the product-constrained quadruple region to the
box in which each index is at most L^2.

Define the ACTUAL annular diagonal

    D_Y=sum_d z(d)^2 sum_(k=b)^B kappa_d(k)^2.

Combining (3.1)--(3.3) gives the all-scale theorem

    0<=D_Y<=1458 H_(L^2)^4=O((1+log Y)^4).               (3.4)

It includes EVERY coalesced product and EVERY annular time, with the stronger
whole-packet bound used only as an upper estimate. The coefficient cap is
what removes the previous single-collar large-diagonal burden. Neither signs
of different products nor any estimate for Mertens sums is used in (3.4).

The bound is intentionally loose. It is not an asserted asymptotic formula,
and making its finite constant smaller does not solve the remaining problem.

## 4. PCR26-4: exact native covariance accounting

Define the ORDERED, signed off-diagonal covariance

    C_Y=sum_(d!=e) z(d)z(e) sum_(k=b)^B kappa_d(k)kappa_e(k).

Do not insert absolute values or call these packets mutually orthogonal.
Put t_k=m_c(k) on the annulus and

    T_Y=sum_(k=b)^B t_k^2,
    L_Y=sum_(k=b)^B t_k Q_Y(k).

(The support makes this T_Y identical to (1.5).) The exact scalar update is

    F_B=F_Y+4T_Y+D_Y+C_Y-4L_Y.                            (4.1)

Its entire collar, cross term and native output are retained. Since
`m(k)=2t_k-Q_Y(k)` for k<=B, Cauchy--Schwarz gives the one-sided bound

    F_B<=9F_Y+2916 H_(L^2)^4+2C_Y.                       (4.2)

This remains correct when C_Y is negative: D_Y+C_Y is exactly ||Q_Y||^2.
Conversely

    C_Y<=||Q_Y||^2<=8T_Y+2(F_B-F_Y)<=8F_B.               (4.3)

Equations (4.1)--(4.3) are statements about ONE complete native source per Y.
No new input envelope is assumed after a Newton extension or recompletion.

### What has actually been removed from the full-proof problem

The coincident-product diagonal is unconditionally polylogarithmic. The
linear/collar part is bounded by the OLD native energy. Any new power-scale
obstruction at this map must occur in the positive part of C_Y, that is,
in coherent interaction between DISTINCT integer products.

This does not make that interaction routine. On the square ladder, a subpower
upper bound for C_Y^+ is equivalent to the already-open subpower F target:
(4.3) gives one direction; iterating (4.2) gives the other. It is a localization
of the mathematical burden, not an assertion that its arithmetic strength
has disappeared. Individual nonpositive covariance is a stronger sufficient
condition, not a consequence of RH assumed here.

## 5. PCR26-5: full-problem implication and the direct sign attempt

### 5.1 A definite all-scale inequality that would finish

If C_Y<=0 at all sufficiently late square-ladder cutoffs
`Y_j=2^(2^j)-1`, then (4.2), L<=2Y and H_n<=1+log n imply

    F_(Y_(j+1))<=9 F_(Y_j)+O(16^j).

Since 9<16, F_(Y_j)=O(16^j). Monotonicity between successive ladder values
then gives

    F_X=O((1+log X)^4).                                  (5.1)

More generally a fixed power of log Y upper bound on C_Y gives a polylogarithmic
F bound, with the recursion's homogeneous factor retained. A bound

    C_Y^+<=C (1+log b)^K (1+F_Y)^(2-delta), 0<delta<1,    (5.2)

gives the previous subquadratic closing recurrence after enlarging constants.
Even `C_(Y_j)^+=Y_j^o(1)` suffices: for each epsilon>0 iterate (4.2) with
`C_(Y_i)^+<=C_epsilon exp(epsilon*2^i)`. The factor 9^j and all logarithmic
terms have logarithms O(j), whereas log Y_j has order 2^j. Let epsilon tend
to zero to get F_(Y_j)=Y_j^o(1), then use monotonicity.

For completeness, E_X<=F_X=X^o(1) makes

    I(s)=integral_1^infinity M(x)x^(-s-1)dx

holomorphic for Re s>1/2. On each dyadic shell Cauchy--Schwarz bounds the
absolute integral by O(2^(j(epsilon/2+1/2-Re s))); logarithmic derivative
factors are summable too. On Re s>1, absolute Mobius inversion gives
`s I(s)=1/zeta(s)`. Analytic continuation of

    (s-1)zeta(s)sI(s)=s-1

rules out every nontrivial zero with Re s>1/2; the functional equation reflects
the remaining half. This is an end-to-end conditional proof, not a finite-height
zero-free statement. No estimate (5.1) or (5.2) is established in this packet.

### 5.2 The proposed native sign has only finite evidence

Directed complete-annulus evaluation gives C_Y<0 for

    Y=1,...,24,31,32,47,63.

Every index k=b,...,b^2-1 and every nonzero coalesced product d is included in
those certificates. Their largest output cutoff is 4095. These are not a
cofinal sequence, an all-Y sign theorem, or independently reviewed proofs.
The exact intervals are in result.json. No asymptotic fit is performed.

The first attempted sign proof, making every pair nonpositive, is FALSE on
the literal native source. At Y=3,

    c=(1,-1,-1,-2/3) on indices1,2,3,4,
    z(2)=z(3)=-2.

The complete contribution of the pair2,3 and its transpose is

    2 z(2)z(3) sum_(k=4)^15 kappa_2(k)kappa_3(k)>1/40.    (5.3)

The bounded log series in the checker certifies this strict rational margin.
The TOTAL covariance at Y=3 is nevertheless negative. Thus any eventual sign
argument must retain cancellation BETWEEN covariance pairs, not just within
each packet or between the two occurrences of one integer product.

## 6. PCR26-6: bounded coefficients and normalization alone still fail

Take the non-native prefix a_1=1 and a_n=0 for2<=n<=Y. Apply the SAME clipped
completion. It has F_Y=Y, |c_n|<=3, P_c(1)=0 and J(c)<=2Y. It violates native
divisor inversion already at n=2. Thus it is a control, not a modified Mobius
claim or an RH counterexample.

Write c_d=-d alpha_d on its tail b<=d<=L. Then alpha_d>=0,
`sum alpha_d=1`, and L<=Y+ceil(Y/2)<3b/2. For L<=k<b^2, no product of two tail
indices can contribute. The exact reciprocal Newton output is

    q(k)=-H_k+2 sum_(d=b)^L alpha_d H_floor(k/d).

Using the same r(t) bounds as before,

    q(k)=log k+gamma-2 sum alpha_d log d+e_k,
    |e_k|<4b/k.                                         (6.1)

Let b>=128 and choose the two disjoint integer blocks

    I=[ceil(b^2/4),floor(b^2/3)],
    J=[ceil(3b^2/4),b^2-1].

They lie above L. For i in I and j in J,

    q(j)-q(i) >= log(9/4)-64/(3b)>1/2.

The elementary lower bound `log(9/4)>10/13` follows from the first term of
`log x=2 atanh((x-1)/(x+1))`. Also |I|>=b^2/16 and |J|>=|I|. Summing the
squared differences and using `(u-v)^2<=2u^2+2v^2` shows

    sum_(k in I union J) q(k)^2 >= |I|/8 >= b^2/128.

Here t_k=0, so Q_Y(k)=-q(k). The same universal diagonal estimate therefore
implies the ALL-PARAMETER control

    C_Y >= b^2/128-1458 H_(L^2)^4, b>=128.                (6.2)

In particular C_Y=Omega(Y^2) on this non-native family. This refutes the proposed
nonpositive or subquadratic covariance bound on the larger class of normalized,
bounded-prefix, bounded-tail sources. The complete native divisor relations must
be used for more than endpoint normalization. The finite controls Y=16,32,64
also have strictly positive covariance, certified separately rather than by
claiming (6.2)'s loose numerical lower bound is positive there.

## 7. Review and precise continuation

The established proposed components are: finite optimal clipped completion
with paid energy; literal prefix squaring; full centered-packet bounds; and a
polylogarithmic bound on the entire coalesced collision diagonal. The remaining
claim is NOT proved: control C_Y on the full, dynamically generated native
prefixes, either by a one-sided sign/budget or a genuine all-scale gain.

The old artificial-collar problem is removed, but no source coefficient is
redrawn and no finite negative covariance plot is promoted to a universal sign.
A further attack should combine the complete divisor equations with groups of
different products in C_Y. Per-pair nonpositivity is already refuted at Y=3.
The arbitrary bounded-vector extension is refuted at every large scale by
(6.2). No claim that reviewer work can fill the missing estimate routinely is
made. New statements and exact evidence require independent review.
