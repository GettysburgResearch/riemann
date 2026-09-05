# Short safe-source computation with a uniform, degree-dependent analytic tail

Status: PROPOSED COMPLETE COMPONENT PROOFS plus executed rational interval
certificates; independent mathematical review required. RH is not proved.
Scope: full zeta, reciprocal-zeta Laguerre coefficients, and the actual moment
and Hardy matrices. This is not a claim of a novel Euler--Maclaurin algorithm.
Local labels SC1--SC5 belong only to this packet.

## 1. Why this is different from truncating the source

The sharp tail theorem requires an exponential raw integer cutoff for a
source-independent subexponential error. Here we use a short integer sum PLUS
its Euler--Maclaurin analytic continuation and a proved remainder. The
continuation is part of the source. It is never silently discarded, nor is
an entire Taylor polynomial mistaken for a uniformly bounded analytic limit.

For sigma in {3/2,2,5/2}, define

    s_sigma(z)=sigma+2z/(1-z),          |z|<=1/8.

Throughout these three disks,

    Re s>=23/18>1,       |s|<=39/14<3,
    |1/zeta(s)|<=zeta(23/18)<=23/5<5.                    (SC1)

The last inequality follows by the absolutely convergent inverse Euler
series and sum_(k>=1) k^(-t)<=1+1/(t-1) for t>1. Only the classical safe
half-plane is used, not a proposed zero-free continuation.

For requested degree N>=0 and extra precision B>=0 (both integers), put

    M=N+ceil(B/4)+4,        K=2M+3,        delta=4/36^M.

The analytical theorem has no upper N cap. The public Python implementation
has explicit resource caps and refuses uncertified output.

## 2. SC1: uniform Euler--Maclaurin remainder

Let Z_M(s) be the exact expression

    sum_(1<=k<K) k^(-s) + K^(1-s)/(s-1) + K^(-s)/2
      +sum_(j=1)^M B_(2j)/(2j)! (s)_(2j-1) K^(1-s-2j).

Then throughout every disk above,

    |Z_M(s)-zeta(s)|<=delta.                              (SC2)

Proof. Euler--Maclaurin gives a remainder, up to an irrelevant sign,

    (s)_(2M)/(2M)! integral_K^infinity
                    B_(2M)({x}) x^(-s-2M)dx.

The periodic Bernoulli Fourier series gives

    sup_x |B_(2M)({x})|<=|B_(2M)|,
    |B_(2M)|/(2M)! <4/6^(2M).

For the second estimate, use
|B_(2M)|=2(2M)!zeta(2M)/(2pi)^(2M), zeta(2M)<2, pi>3.
Moreover |(s)_(2M)|<=(2M+2)^(2M)<K^(2M). Integrating the
absolute power gives the remainder bound

    4/36^M * K^(1-Re s)/(Re s+2M-1) <=delta.

This proves SC2 uniformly before any coefficient extraction. It does not
bound a moving derivative by a fixed-order remainder without Cauchy.

Since 5delta<1/6, SC1--SC2 give |1/Z_M|<=6 on the same disk.

## 3. SC2: all Mobius coefficients through degree N

For sigma=3/2 set

    A(z)=1/[(1-z)zeta(s_sigma(z))(1-67^(-s_sigma(z)))],
    A_M(z)=1/[(1-z)Z_M(s_sigma(z))(1-67^(-s_sigma(z)))].

Both are analytic on |z|<=1/8. The inverse difference, SC1--SC2, and
|(1-67^(-s))^-1|<=67/66 give

    sup_(|z|<=1/8)|A_M-A|<=36delta.

Therefore, for every 0<=n<=N,

    |[z^n]A_M-a_n|<=36delta*8^n
                         <2^(-N-B-13).                  (SC3)

To check the last constant, use 36>16 and
144/36^4=1/11664<2^-13; also 8^N/36^N<=2^-N and
36^(-ceil(B/4))<=2^-B.

The exact nonzero constant denominator permits finite formal inversion
through degree N. All constants needed are rational numbers, square roots
of positive integers, and logarithms of positive rationals. Interval
arithmetic enclosing those constants and every finite operation, followed
by widening the nth coefficient by 36delta*8^n, gives an enclosure for the
FULL infinite Mobius coefficient. The error is not a claim that the raw
Dirichlet sum through K approximates that coefficient.

Only K-1=2N+2ceil(B/4)+10 integers occur in the retained zeta sum, plus the
local factor 67. There are M Bernoulli corrections. The number of finite
series operations is polynomial in N and B; a linear running-time or
bit-complexity bound is NOT claimed. With arbitrarily accurate rational
interval arithmetic the enclosures eventually meet width 2^(-N-B), because
the fixed analytic remainder leaves a strict margin. The default code uses
640-bit outward binary endpoints, caps degree at 32 and B at 512, and fails
rather than accepting a width or denominator failure.

## 4. SC3: logarithmic-derivative and gamma jets with explicit errors

Let Z(z)=zeta(s_sigma(z)), Z_E(z)=Z_M(s_sigma(z)). On the disk,

    ell(z)=log(Z_E(z)/Z(z))

has the branch near zero and |ell(z)|<=10delta. It is analytic since
|Z_E/Z-1|<=5delta<1/2. Since ds/dz=2/(1-z)^2, the error in the s-logarithmic
derivative is (1-z)^2 ell'(z)/2. Cauchy's estimates, including the derivative
index n+1, prove

    |[z^n](Z_M'(s)/Z_M(s)-zeta'(s)/zeta(s))|
       <=55(n+1)delta*8^n.                               (SC4)

Explicitly the coefficient is one half of
(n+1)ell_(n+1)-2n ell_n+(n-1)ell_(n-1), with nonexistent terms zero.
Thus its absolute value is at most
5delta*8^n[8(n+1)+2n+max(n-1,0)/8], bounded by SC4. The producer computes the
zeta series through N+1 before differentiating; computing only through N
would lose the last required coefficient.

For v=s/2 use the exact shift

    psi(v)=psi(v+K)-sum_(j=0)^(K-1)1/(v+j).

Approximate the first term by

    log(v+K)-1/[2(v+K)]
                 -sum_(j=1)^M B_(2j)/[2j(v+K)^(2j)].

The Euler--Maclaurin remainder is bounded by

    |B_(2M)|/[2M(Re(v+K))^(2M)] <=delta.                  (SC5)

One obtains this directly from the periodic-Bernoulli integral remainder
for digamma. Re(v+K)>K, and the Bernoulli estimate above with
(2M)!<=(2M)^(2M) proves the last inequality. The bound allows a remainder
of the same order as the last displayed term; it is not an assertion of a
convergent Stirling series. Cauchy gives coefficient errors delta*8^n.

The safe logarithmic derivative of completed xi is

    L(s)=1/s+1/(s-1)-log(pi)/2+psi(s/2)/2+zeta'(s)/zeta(s).

Rational functions are expanded exactly. The computed nth L coefficient is
widened by [55(n+1)+1/2]delta*8^n. Constants log(pi), logarithms and square
roots have their separate rational interval enclosures. The analytic part
is less than 2^(-N-B-12) for n<=N: use
(N+1)(4/9)^N<=1 and 222/36^4<2^-12.

## 5. SC4: export to the invariant moments and the full Hardy compression

### Invariant moments at s=2

Let h(u) be the solution of 3h+h^2=u, h(0)=0. Then

    h_1=1/3, h_n=-(1/3)sum_(1<=j<n)h_j h_(n-j),
    z(u)=h(u)/(2+h(u)),
    q(u)=L(s_2(z(u)))/(3+2h(u)).

This equals the predecessor's actual invariant logarithmic derivative at
center s=2. Its moments are m_j=(-1)^j[u^j]q(u). Formal composition through
N uses only N source coefficients because z(0)=0. Interval propagation
therefore retains SC4--SC5 without an unbounded-order substitution.

### Hardy matrix in the fixed Laguerre basis

Retain exactly the parent operator a=1, b=3/2. Put r(z)=2/(1-z) and

    c(z)=[L(1/2+r(z))-(2r(z)/3)L(2)]/[9/4-r(z)^2].

The numerator uses the safe sigma=5/2 jet and the separate constant at s=2.
The denominator at z=0 is -7/4. Expand it by finite series inversion.
The actual matrix is defined by

    sum_(i,j>=0) A_ij z^i w^j=2(c(z)+c(w))/(2-z-w).

Thus, with negative indices zero,

    A_ij=c_i 1_(j=0)+c_j 1_(i=0)+(A_(i-1,j)+A_(i,j-1))/2.

This is the exact full-source compression from pass3, not the operator
obtained by dropping all sufficiently large primes. Its capture theorem is
an imported parent component; no new infinite-operator sign is assumed.

There is a useful dimension-paid precision estimate. If the first d scalar
c coefficients are each approximated within eps, then

    max_(i,j<d)|Delta A_ij|<=4eps,
    ||Delta A_d||_op<=4d eps.                              (SC6)

Indeed expand (c(z)+c(w))/(1-(z+w)/2). Each of the two coefficient sums
has nonnegative weights whose total is at most
sum_(j>=0)binom(j+n,n)2^(-j-n)=2. This proves the entry bound; the row-sum
bound proves the operator estimate. It concerns coefficient-error transport,
not a lower bound for the eigenvalues of the actual matrix.

## 6. SC5: executed actual-source certificates

The default producer freshly reconstructs these three finite outputs:

1. The 13 Mobius coefficients a_0,...,a_12, using N=12, B=96,
   M=40, K=83. The retained integer sum has 82 terms. Every resulting
   interval has width below 2^-108 after the infinite-tail widening.
2. Ten invariant log moments m_0,...,m_9 using N=9,B=192. Positive diagonal
   scaling gives H_ij=200^(i+j)m_(i+j) and
   Hplus_ij=200^(i+j+1)m_(i+j+1), 0<=i,j<5. All ten interval LDL pivots
   have strictly positive lower endpoints.
3. The full eight-by-eight Hardy compression using B=192. All eight
   interval LDL pivots have strictly positive lower endpoints. The final
   pivot is about 2.4623564e-21, so mere entrywise rounding would not suffice.

The ten moment signs imply a positive FIVE-node resolvent quadrature
matching all ten log moments. For completeness, on degree<=4 polynomials
with inner product ell(PQ), define the positive self-adjoint J by
<P,JQ>=ell(xPQ). In monomials J=H_raw^-1 Hplus_raw. It agrees with
multiplication by x through degree three, hence 1,J1,...,J^4 1 are independent
and 1 is cyclic. The five eigenvalues are distinct and positive and their
spectral weights at 1 are positive. Splitting k=i+j, i,j<=4, proves exact
moment agreement through k=8; <J^4 1,J J^4 1>=ell(x^9) supplies the tenth.
Thus sum_j w_j/(1+u lambda_j)=q(u)+O(u^10). This is NOT a rank-five ordinary
determinant: w_j/lambda_j need not be integers.

These finite positive signs neither estimate all higher Hankel minors nor
prove that all Hardy compressions are positive. The uniform source compiler
would also correctly report a negative source matrix were one found. Its
purpose is to eliminate uncontrolled arithmetic truncation from that test.

## 7. What was attempted at the final sign

The natural attempted argument was: replace the long arithmetic sum by its
short certified source, exploit the positive low-order matrices, and extend
the signs through the exact recurrences. The first replacement is completed
by SC1--SC6; the sign propagation is NOT. The Hardy recurrence has a signed
boundary forcing, and no induction preserves PSD automatically. Likewise a
positive five-node moment quadrature supplies no all-order extension.

The new signed coefficients also do not yet obey an all-degree
subexponential energy bound. Accurate evaluation and positivity at finitely
many dimensions are not the missing uniform inequality. All three RH-facing
endpoints remain open. No finite computation is promoted to a global sign.
