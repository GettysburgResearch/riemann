# Sharp real taper threshold for unit-circle reciprocal polynomials

Proposer: semantic_skeptic. Date: 17 November 2026. Status: complete ordinary-analysis proof proposed; independent challenge requested. This extends the separately reviewed integer-power window theorem. It is a finite polynomial/H2 result, not a zeta estimate or a historical-novelty claim. All asymptotic statements keep m and p fixed.

## Statement

Let m>=1 be an integer, p>=0 a real number, and

Q(z)=product_(j=1..m)(1-q_j z), |q_j|=1,

1/Q(z)=sum_(n>=0)b_n z^n.

For every integer M>=1 define

A_(M,p)(z)=sum_(n=0..M-1)b_n(1-n/M)^p z^n,

E_(M,p)=||1-Q A_(M,p)||_H2^2,

with normalized H2 norm equal to the coefficient square sum. Every weight used in A has strictly positive base, so there is no real-power branch ambiguity, including p=0. Roots may coincide or depend arbitrarily on M.

**Proposed sharp threshold:** a finite constant C_(m,p), independent of M and all root locations/collisions, exists with

E_(M,p)<=C_(m,p)/M

if and only if

p>m-1/2.

At the critical power p=m-1/2, all roots still obey a universal upper bound O_m((1+logM)/M), and complete coalescence Q=(1-z)^m has the matching order

E_(M,m-1/2) asymp_m logM/M.

Thus the smallest admissible nonnegative integer power is m, but the real-power threshold lies strictly below m. This does not supply uniformity in growing m or in p approaching the threshold without the explicit constants below.

## 1. A discrete power-difference bound, including the singular endpoint

For this section assume p>=m-1/2>0. For k=1,...,m, write

(p)_k=product_(s=0..k-1)(p-s)>0,

D_(p,k)=2^k k^p+(p)_k max{k^((p-k)_+),2^((k-p)_+)}.

For every integer j>=0, the forward difference of x^p satisfies

|Delta_forward^k(j^p)|<=D_(p,k)(j+1)^(p-k).                         (1)

At j=0, this follows directly from the finite sum and the bound sum_(l=0..k)binom(k,l)l^p<=2^k k^p, with0^p=0. No derivative at0 is invoked.

For j>=1, the repeated integral formula gives an integral of(p)_k(j+t_1+...+t_k)^(p-k) over[0,1]^k. If p-k>=0, use j+k<=k(j+1). If p-k<0, use j>=(j+1)/2. These give the second term in D. This avoids applying a smooth-derivative estimate at the endpoint where the highest derivative is singular.

Let n=M-j,1<=n<=M, and extend the weight by w_n=(1-n/M)^p for n<=M and0 for n>M. Then

|Delta_backward^k w_n|
 =M^(-p)|Delta_forward^k(j^p)|
 <=D_(p,k)M^(-p)(j+1)^(p-k).                                    (2)

Whenever the reciprocal subset term is nonzero, n>=k, so every weight index used lies between0 and M. Values of w at negative indices are irrelevant because the corresponding reciprocal coefficients are0.

## 2. Collision-uniform bulk and terminal estimates

Use the exact twisted-difference identity independently reviewed in `audits/adversarial_reviews/polynomial_window_third_round3.md`. For each indexed subset J of size k, its coefficient contribution is

q_J h_(n-k)(q_j:j in J) Delta_backward^k w_n.

The complete homogeneous coefficient obeys

|h_(n-k)|<=binom(n-1,k-1)<=M^(k-1)/(k-1)!,

and vanishes when n<k. Define

H_(m,p)=sum_(k=1..m)binom(m,k)D_(p,k)/(k-1)!.

Writing x=(j+1)/M in(0,1], k<=m implies x^(p-k)<=x^(p-m). Thus the bulk residual coefficients satisfy

|r_(M-j)|<=H_(m,p) M^(-1)[(j+1)/M]^(p-m), 0<=j<=M-1.            (3)

The residual constant term is0. Put alpha=2(p-m). Squaring and summing(3) gives

E_bulk<=H_(m,p)^2 M^(-2-alpha) sum_(s=1..M)s^alpha.               (4)

For the terminal block n=M+r,1<=r<=m-1, the coefficient bound |b_l|<=M^(m-1),0<=l<=M-1, yields

|r_(M+r)|<=T_(m,p,r) M^(m-1-p),

T_(m,p,r)=sum_(j=r+1..m)binom(m,j)(j-r)^p.

Set U_(m,p)=sum_(r=1..m-1)T_(m,p,r)^2. Therefore

E_tail<=U_(m,p) M^(-2-alpha).                                  (5)

For m=1 the terminal sum is empty. These estimates are valid at M=1 and contain no root-separation term.

If p>m-1/2, then alpha>-1 and

sum_(s=1..M)s^alpha<=max{1,1/(alpha+1)}M^(alpha+1).

The negative-exponent case follows by integrating x^alpha on[0,M]; the nonnegative-exponent case follows by bounding each summand by M^alpha. Equations(4)–(5) prove the explicit universal bound

E_(M,p)
 <=[H_(m,p)^2 max{1,1/(2p-2m+1)}+U_(m,p)]/M.                   (6)

At p=m-1/2, alpha=-1. Using the harmonic-sum bound gives

E_(M,p)<=[H_(m,p)^2(1+logM)+U_(m,p)]/M.                        (7)

This proves the upper halves of the statement, including a quantitative display of the deterioration at the critical power.

## 3. Subcritical powers: exact terminal obstruction

Take complete coalescence Q=(1-z)^m. The last residual coefficient, at degree M+m-1, has exactly the modulus

binom(M+m-2,m-1)/M^p.

For fixed m and every p<m-1/2, its square multiplied by M is asymptotic to

M^(2m-1-2p)/[(m-1)!]^2,

which tends to infinity. This rules out any O(1/M) bound even at this one root configuration. It includes p=0 without requiring the endpoint weight convention used in the upper proof.

## 4. Critical power: signed endpoint dominance gives the missing logarithm

Fix p=m-1/2. Let

P(u)=product_(l=1..m-1)(u+l)/(m-1)!,

a_M(u)=M^(-p)P(u)(M-u)^p, u<M.

At nonnegative integer indices below M these are exactly the coalesced approximant coefficients. Set a_m=(p)_m>0 and

d_m=sum_(k=1..m-1)binom(m,k)[(p)_k/(p)_m]
       (m-1)_(m-k) 2^(m-k),

epsilon_m=min{1/4,1/[2 max(1,d_m)]},

c_m=(p)_m/[2^m(m-1)!].

Empty sums/products have their usual meanings, so d_1=0. All these constants are explicit and positive where required.

For u>=M/2 and0<=r<=m-1,

0<=P^(r)(u)/P(u)<=(m-1)_r(2/M)^r.                              (8)

This follows by differentiating the product: the ratio is r! times the r-th elementary symmetric polynomial in the reciprocals1/(u+l).

Write t=M-u. In the m-th derivative of a_M, the term differentiating the power m times is

(-1)^m M^(-p)P(u)(p)_m t^(-1/2).

By(8), the sum of the magnitudes of all remaining terms divided by this main magnitude is at most

sum_(k=1..m-1)binom(m,k)[(p)_k/(p)_m](m-1)_(m-k)
 2^(m-k)(t/M)^(m-k)
 <=d_m epsilon_m<=1/2

whenever0<t<=epsilon_m M. Hence the derivative has a fixed sign there and

(-1)^m a_M^(m)(u)
 >=(1/2)M^(-p)P(u)(p)_m t^(-1/2)
 >=c_m M^(-1/2)t^(-1/2).                                     (9)

The last inequality uses u>=M/2 and P(u)>=(M/2)^(m-1)/(m-1)!.

For each integer1<=j<=J=floor(epsilon_m M)-m, take n=M-j. Every point sampled by the m-fold backward-difference integral then has t between j and j+m, inside the sign-controlled region. These indices are nonnegative, so no polynomial extension or negative-index convention is needed. Equation(9) gives

|r_(M-j)|=|Delta_backward^m a_M(M-j)|
 >=c_m/[sqrt(M)sqrt(j+m)].                                   (10)

Summing(10), and taking M large enough that J>=1, proves

E_(M,m-1/2)
 >=(c_m^2/M)sum_(j=1..J)1/(j+m)
 >=(c_m^2/M)log[epsilon_m M/(m+1)].                           (11)

In particular, for M>=max{2,ceil[((m+1)/epsilon_m)^2]},

E_(M,m-1/2)>=(c_m^2/2)(logM)/M.                              (12)

Together with(7), this proves the claimed critical order and rules out O(1/M) at equality. The logarithm is obtained from an interval of bulk coefficients with controlled sign, not from an unjustified pointwise differentiation at the singular terminal point.

## 5. A one-root sanity check and precise limits

For m=1,p=1/2, the residual coefficients give the exact identity

E_(M,1/2)=M^(-1)sum_(j=0..M-1)[sqrt(j+1)-sqrt(j)]^2.

The summand is asymptotic to1/(4j), so M E/logM tends to1/4. This independently confirms the logarithmic mechanism in the simplest case. The theorem above does not claim an exact critical leading constant for general m; only explicit two-sided order bounds are proved.

The result concerns fixed finite m,p, arbitrary unit phases and polynomial degree cutoff M-1. It does not establish an arithmetic counterpart, solve a multiple-cluster growing-m problem, or identify any historical priority. Prior Riesz/Cesaro approximation literature still needs to be searched before any novelty attribution. Independent adversarial review is required before elevating this proposed extension.
