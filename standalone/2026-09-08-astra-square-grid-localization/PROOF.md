# SSQ26: sieve-controlled local detail and the remaining square-grid energy

Status: PROPOSED COMPONENT THEOREMS; independent mathematical review pending.
The global energy bound, source-domain completeness, and RH remain unproved.
Date: 2026-09-08. Author: Astra. This is research, not a Reviewer D verdict.
Parent: PR818 at 52b6d58cef49a41bf5c07c84018c09b55e408d51.

The new unconditional assertion is a summable bound for the FULL local detail
inside every consecutive-square interval. It does not bound the cumulative
level from one interval to the next. All details and cross terms are kept in
an orthogonal decomposition. No prime exists-between-squares assumption is
made. The imported sieve theorem is the classical Brun--Titchmarsh interval
bound, not an RH estimate or a result proved by this packet's finite code.

## 1. Ordinary prime count and an exact adapter to the parent metric

Let pi(x) count all ordinary primes p<=x, including p=2, and define

    Li_2(x)=integral_2^x du/log u,
    e(x)=pi(x)-Li_2(x), x>=2; e(2-)=0.
    K=integral_2^infinity e(x)^2 dx/x^2 in [0,infinity].       (1)

Li_2 is NOT an unspecified choice of li: its lower endpoint is exactly 2.
For t>=log 2 put z(t)=exp(-t/2)e(exp t), and set z=0 earlier. The
letter z in this paragraph denotes a time function, not a Laplace variable.
Then K=||z||_2^2, with the extended-value convention.

The parent's quantities are

    R(x)=sum_(p<=x)sqrt p-integral_2^x sqrt u/log u du,
    v(t)=exp(-t)R(exp t),
    J=||v||_2^2=integral_2^infinity R(x)^2 dx/x^3.            (2)

**SSQ26.T1 (bounded invertible source adapter).** Exactly, as locally
integrable causal functions,

    v=z-(1/2)k_1*z,      z=v+(1/2)k_(1/2)*v,
    k_a(t)=exp(-a t)1_(t>=0).                             (3)

Consequently J is finite if and only if K is finite, and when they are finite

    K/4 <= J <= K.                                        (4)

Proof. Stieltjes integration by parts, retaining e(2-)=0 and the full prime-2
jump, gives

    R(x)=sqrt x e(x)-(1/2)integral_2^x e(u)/sqrt u du.

Changing variables gives the first identity in (3). The causal resolvent
identity, or multiplication of the stable rational factors, gives the inverse.
Both kernels are L1, so finiteness in either direction implies finiteness in
the other. In the Laplace variable w, the transfer is

    V(w)=[(w+1/2)/(w+1)]Z(w).

On w=iy its squared modulus is (y^2+1/4)/(y^2+1), between 1/4 and 1.
Plancherel, normalized by dy/(2pi), proves (4). This is an actual bounded
adapter; it is not a free change of measure or metric. In particular (4)
is a GLOBAL norm statement and is not asserted for arbitrary tail restrictions,
which would have additional memory terms.

## 2. The only new external estimate

We use the classical Montgomery--Vaughan form of Brun--Titchmarsh:

    pi(a+h)-pi(a) <= 2h/log h,       a>0, h>1.             (BT)

Only this coarse upper bound is imported. We do not use a lower count in
short intervals, a conjectural asymptotic, or any sharpened numerical constant.
The interval convention is (a,a+h]. The statement is documented by the original
1973 large-sieve paper and explicitly restated as (1), C=2, in Yamada's
arXiv:2312.16090v1, Introduction. SOURCES.json gives exact references. The
sharper 0.8601 constant and its computational proof are NOT used.

Here is the elementary energy lemma to which BT is applied. Suppose on a
finite interval I a real function E is the difference of two nondecreasing
functions having total increments P and L, respectively. Then

    ess sup_I E-ess inf_I E <= max(P,L).                   (5)

Indeed, for ordered points u<v, E(v)-E(u) lies between -L and P. Whichever
of an extremizing pair comes first, its absolute difference is at most
max(P,L). Approximation handles unattained essential extrema.

For any finite positive measure mu on I, put w=mu(I)>0 and
m=w^(-1)integral_I E dmu. The exact identity is

    integral_I E^2 dmu = w m^2 + integral_I(E-m)^2 dmu.    (6)

If the range width is at most B, then

    integral_I(E-m)^2 dmu <= w B^2/4.                    (7)

For completeness, if a<=E<=b, averaging (E-a)(b-E)>=0 gives
Var(E)<= (m-a)(b-m)<= (b-a)^2/4 in the probability measure mu/w.
Limit a,b to the essential bounds. This proves (7) without a sampled sign
or a hidden orthogonality assumption.

## 3. An unconditional complete local-detail bound on square cells

For each integer n>=2 define

    a_n=n^2, b_n=(n+1)^2, h_n=2n+1,
    w_n=integral_(a_n)^(b_n) dx/x^2
       =1/n^2-1/(n+1)^2,
    m_n=(1/w_n)integral_(a_n)^(b_n) e(x) dx/x^2,
    d_n=integral_(a_n)^(b_n) [e(x)-m_n]^2 dx/x^2.          (8)

The symbols b_n here are cell endpoints, not the damping of the parent.
Every endpoint n^2, n>=2, is composite, so no prime is lost by the cell
convention. Values at endpoints do not affect the integrals.

**SSQ26.T2 (all-square-cell detail is summable).** Unconditionally,

    d_n <= h_n^3/[n^2(n+1)^2 log^2 h_n]
         <= 125/[8n log^2 n],
    sum_(n>=N) d_n < 28/log N,              every integer N>=2.    (9)

Proof. The total prime increment P_n is at most 2h_n/log h_n by (BT).
The continuous increment is at most h_n/(2log n). Since 2n+1<=n^4 for
n>=2, that is also at most 2h_n/log h_n. Equations (5)-(7) give

    d_n <= w_n h_n^2/log^2 h_n.

Use h_n<=5n/2, (n+1)^2>=n^2 and log h_n>=log n to obtain the second bound.
The function 1/(x log^2 x) decreases on x>1, so

    sum_(n>=N)1/(n log^2 n)
       <= 1/(N log^2 N)+integral_N^infinity dx/(x log^2 x)
       = [1+1/(N log N)]/log N.

Because N log N>=2log2>4/3, multiplication by 125/8 gives the constant
875/32<28. This pays every cell up to infinity, not a finite cell census.
Only log2>2/3 is needed for that simplification.

Define m(x)=m_n on each square cell, and m(x)=e(x) on [2,4). The exact,
possibly infinite decomposition is

    K=integral_2^4 e(x)^2 dx/x^2
             +sum_(n>=2) w_n m_n^2 +sum_(n>=2)d_n.       (10)

This is obtained by summing the nonnegative finite identities (6). It is
valid before global L2 membership is known. On the logarithmic half-line,
e^(-t/2)[e(e^t)-m(e^t)] is an L2 vector unconditionally, with squared tail
beyond 2log N less than 28/log N. It is orthogonal to every cell-constant
coarse vector in the same weighted metric. All possible infinite energy
is therefore in the COARSE LEVELS m_n, not the paid local detail.

This does not make either sum in a signed off-diagonal decomposition positive;
it is an orthogonal decomposition of the actual discrepancy vector itself.
It also does not assert that pi is correctly approximated by its continuous
main term on each cell: a prime-free cell is permitted by the theorem.

### Exact arithmetic formula for each coarse coefficient

Set a=n^2, b=(n+1)^2, w=1/a-1/b and E=e(a). Finite Fubini gives

    m_n=E+(1/w)[sum_(a<p<b)(1/p-1/b)
                 -log(log b/log a)+(Li_2(b)-Li_2(a))/b].       (11)

Indeed a prime at p contributes integral_p^b x^-2 dx. The continuous
increment contributes integral_a^b(1/u-1/b)du/log u. The old cumulative
level E in (11) is mandatory. BT bounds the new within-cell terms; it does
not bound E or allow it to be reset to zero.

## 4. Even endpoint samples have a complete summable error

Put s_n=e(n^2), and define the held field s(x)=s_n on the n-th square cell.
The range estimate in Section 3 gives, without squaring an unknown coarse level,

    integral_(N^2)^infinity |e(x)-s(x)|^2 dx/x^2
                                    <112/log N.              (12)

This follows from |e(x)-e(n^2)|<=2h_n/log h_n and the same summation as (9),
without the variance factor 1/4. Set s=e on [2,4) when using whole-line norms.

In particular,

    K<infinity <=> sum_(n>=2) w_n s_n^2<infinity
               <=> sum_(n>=2) [pi(n^2)-Li_2(n^2)]^2/n^3<infinity.  (13)

For the last equivalence, 1/n^3<w_n<2/n^3 for n>=2. The first follows
from (12) and the triangle inequality, in either direction. It does NOT use
an interchange of two divergent signed sums. For finite 2<=N<M the useful
quantitative comparison is

    | (integral_(N^2)^(M^2)e^2 dx/x^2)^(1/2)
           -(sum_(n=N)^(M-1)w_n s_n^2)^(1/2) |
                             <=sqrt(112/log N).               (14)

No pointwise limit for s_n/n is inferred from summability. The squares in
(13) are predetermined integer endpoints, not sample nodes selected after
knowing a hypothetical zero.

## 5. A more general mesh: how much can be discarded without an RH bound?

Let x_j increase to infinity, with h_j=x_(j+1)-x_j>1 and h_j<=x_j. Define
the local weighted mean and detail as in (8), with measure dx/x^2.
Here the continuous increment is <=h_j/log x_j<=2h_j/log h_j. The SAME
argument proves the completely unconditional bound

    detail_j <= h_j^3/[x_j^2 log^2 h_j].                    (15)

Thus any prescribed partition for which the right sides are summable has a
finite global detail. For example, for any fixed real 0<=alpha<1/2, take

    x_(j+1)=x_j+sqrt(x_j)(log x_j)^alpha

starting sufficiently large that h_j>1 and h_j<=x_j. This has

    sum_(x_j>=Y) detail_j
                         =O_alpha((log Y)^(2alpha-1)).        (16)

To verify summation, h_j/x_j->0 and
log h_j=(1/2)log x_j+alpha log log x_j. The expression in (15) is
h_j times O_alpha((log x_j)^(2alpha-2)/x_j), uniformly over each cell.
Cellwise integral comparison reduces the tail to
integral_Y^infinity (log x)^(2alpha-2)dx/x, which converges precisely when
alpha<1/2. At alpha>=1/2 THIS MAJORANT ceases to be summable. No sharp
threshold for the actual prime details is asserted from that failure.
The explicit all-N constants in (9) and (12) pertain to square cells only.

## 6. Relation to RH and the original source domain

Combining (4), (10), (13) and the parent's source-qualified J criterion gives

    RH <=> sum_(n>=2)w_n m_n^2<infinity
       <=> sum_(n>=2) [pi(n^2)-Li_2(n^2)]^2/n^3<infinity.   (17)

The NEW component in this equivalence is the unconditional sieve-controlled
approximation. This is not claimed as a novel general characterization of RH.
The parent obtains RH=>J<infinity using the classical RH-conditional Cramer
mean-square theorem. We do not reclassify that input as unconditional.
Here is a self-contained proof of the needed other implication from K.

If K<infinity, then z from Section 1 is in L2. For Re s>1/2,

    C(s)=s integral_(log2)^infinity exp(-(s-1/2)t)z(t)dt       (18)

is analytic by Cauchy--Schwarz and locally uniform differentiated estimates.
For Re s>1, Stieltjes integration by parts at 2- proves

    C(s)=sum_p p^-s-integral_2^infinity x^-s/log x dx.

There is no missing lower endpoint since e(2-)=0. Put a=log2 and

    B(s)=-gamma-log a+Ein((s-1)a)-2log s,
    V(s)=sum_p sum_(k>=2)p^(-ks)/k.

B and V are analytic on Re s>1/2, with the canonical right-half-plane
logarithm and absolutely locally uniformly convergent V. In Re s>1,
E1(w)=Ein(w)-gamma-log w and Euler's product give

    exp(B(s)+C(s)+V(s))=(s-1)zeta(s)/s^2.

Analytic uniqueness extends this identity to Re s>1/2. Its left side never
vanishes, so no zeta zero lies there. The functional equation excludes the
reflected zeros to the left of 1/2. This retains all multiplicities and
never assumes a logarithm of zeta across unknown zeros.

Accordingly a proof of either coarse upper bound in (17) would finish the
route, then give the source-domain conclusions of the parent lineage. NO
SUCH UNCONDITIONAL BOUND IS PROVED HERE. BT has paid the fine detail, not
the cumulative signed arithmetic in m_n or s_n. ATTEMPT.md states the actual
remaining sum, the unsuccessful upper estimate and a control against the
unsupported final inference.

## 7. Bounded computation, separate from the all-scale theorem

check.py computes an integer sieve through 128^2 and six fully enclosed
finite sample-energy prefixes

    S_M=sum_(n=2)^(M-1) w_n [pi(n^2)-Li_2(n^2)]^2,
                   M=4,8,16,32,64,128.

Li_2 is enclosed by its convergent exponential-integral difference series,
with directed integer logarithms and explicit series remainders. No zeta,
zero, gamma or special-function oracle is used. This is an ENDPOINT-SAMPLE
energy, not the orthogonal mean energy, not a total J value, and not a norm
of an optimally chosen approximant. In particular at M=128,

    0.565641628407 < S_128 < 0.565641628409.              (19)

Every term is nonnegative; increase of this finite partial sum is automatic
and says nothing about its unbounded limit. No tail of the coarse sum is
bounded by the finite experiment. The bound (9) controls a DIFFERENT tail:
the within-cell detail, whose proof uses BT and holds independently of the
computed values. Validation reports distinguish finite fixtures from the
imported sieve and infinite analytic arguments.
