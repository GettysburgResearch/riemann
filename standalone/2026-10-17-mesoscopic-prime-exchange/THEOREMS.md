# Fixed-twist mesoscopic prime-exchange covariance

Status: PROPOSED complete unconditional component arguments. Same-author
proof and computations; no independent referee or formal build. No RH proof,
full critical-energy upper bound, or full native higher-moment estimate.

Scope: one principal scalar source over K=Q(omega), omega^2+omega+1=0,
not an average over Mellin twists or a replacement by independent primes.
The final result evaluates a growing family of incomparable ideal pairs
inside a narrowing relative norm band. It is a positive selected covariance,
not a bound for the whole band or for the whole energy.

Sources and credits: #952's exact Gaussian energy kernel; #953's ideal-
divisibility analysis; #954's grouping of complete rational-norm fibers and
tensor-square pole. The local correlation, complex continuation, moving-prime
asymptotic and mesoscopic estimates used here are proved below. Classical
Euler products, Gaussian Mellin inversion, the prime number theorem in the
FIXED progression 1 mod 3, and Selberg's elementary upper sieve are credited.
The upper-sieve lemma is reconstructed in full. No quasi-RH, GRH, prime-pair
conjecture, short-interval PNT, or new automorphic input is used.

## 1. The source and the main result

Fix a finite set S of prime IDEALS of K, containing those above 2 and 3.
The set need not be conjugation invariant. Fix an integer m>=4. For each
prime ideal p outside S, of norm q, choose b_p with |b_p|<=1. Define the
multiplicative coefficients c by

    c(p)=-(1-1/q),       c(p^m)=-b_p q^(m/2-1),
    c(p^e)=0 for e not in {0,1,m},       c(1)=1.           (1)

All positive exponents at an ideal in S have coefficient zero. This is the
actual coupled 0/1/m family used in #948--#954, specialized to the principal
ordinary phase a_p=1. Its b_p values need not be Hecke characters. In particular
m=6 includes the algebraic principal source with its actual unit theta phases.
No automorphic realization is claimed for other m. The original ideal Mobius
source c(n)=mu_K(n)1_((n,S)=1) is treated throughout as a separate variant.

All equal-norm ideals remain distinct. Only AFTER defining their coefficients
set

    A(n)=sum_(N a=n) c(a),       d(n)=|A(n)|^2.           (2)

These functions of rational positive integers are multiplicative. The scalar
Gaussian and critical energy are

    W_c0(y)=y^(-c0) exp[-(log y)^2/4]/(2 sqrt(pi)),
    B(X)=sum_a c(a) W_c0(N a/X),
    E(D)=integral_0^D |B(X)|^2 dX/X^2.

The source's c0 is 5/6; any fixed real c0 works below. Put beta=2c0-1 and
kappa=exp(beta^2/2)/(2 sqrt(2pi)). The exact pair kernel is

    K_D(v,z)=kappa/sqrt(vz) exp[-log(v/z)^2/8]
                       Phi(log D-log(vz)/2-beta),        (3)

where Phi is the standard normal CDF. In particular

    E(D)=sum_(v,z>=1) A(v) conjugate(A(z)) K_D(v,z).      (4)

This is the full ideal-pair expansion with the norm fibers summed, not a
one-ideal-per-norm approximation. Its absolute convergence at every fixed D
follows from sum_(N a<=x)|c(a)|<=C_K x and Gaussian partial summation.
Indeed c(a) has the unique representation a=r h^m with r,h squarefree and
coprime, and |c(a)|<=(N h)^(m/2-1); discarding these restrictions in a positive
count gives C_K x sum_h (N h)^(-m/2-1). The latter converges. The native
variant is easier. This proves all finite-D exchanges of absolutely convergent
physical sums used below.

For distinct rational primes p,q that split in K and do not lie below S,
define the COMPLETE exchange channel

    X_pq(D)=sum_(k>=1) A(pk) conjugate(A(qk)) K_D(pk,qk). (5)

Every ordered ideal pair with reduced rational norm ratio p/q occurs exactly
once in (5). Its rational gcd is k; the IDEAL gcd is not being replaced by k.
The two norms are unequal and neither ideal can divide the other, since p/q
is not an integer in either direction. A shared prime in k is permitted.

For Y>=2 and 1<=H<=Y let P(Y) be the split rational primes in [Y,2Y] not
below S, and set

    X(D;Y,H)=sum_(p,q in P(Y), 0<|p-q|<=H) X_pq(D).    (6)

Both orientations are retained. There is no Mellin-twist average.

### Theorem 1: a sharp growing, narrowing-band covariance

For every fixed 0<eta<theta<1, at Y=D^theta and H=D^eta,

    0 < c_(m,S,c0,theta,eta) D^eta
        <= X(D;D^theta,D^eta)
        <= C_(m,S,c0,theta,eta) D^eta                   (7)

for all sufficiently large D. The constants and the threshold can be chosen
uniformly over all profiles |b_p|<=1. The native Mobius source satisfies the
same conclusion, with its own constants.

In particular, at theta=3/4 and eta=1/4,

    X(D;D^(3/4),D^(1/4)) asymp D^(1/4),                 (8)

although every selected pair satisfies

    |N a/N b - 1| <= D^(-1/2).                         (9)

Thus a narrowing, genuinely incomparable, fixed-twist covariance sector has
positive power-sized mass. This is BOTH an upper and a lower bound, not a
new upper bound for E(D). It rules out a subpower upper bound for this
particular selected sector, NOT for the complete band or complete energy.
The selection is stated exactly; it contains all prime-exchange norm fibers
in (6), not every pair satisfying (9).

### Theorem 1A: the upper bound permits all physical phases and masks

For the upper bound only, allow arbitrary row-dependent phases |a_p(u)|,
|b_p(u)|<=1 in the original local source. At every nonunit/excluded prime set
BOTH phases to zero. Let w be ANY nonnegative finite row measure of mass Z,
held fixed at every scale. Let AbsX be the sum of ABSOLUTE ideal-pair
contributions with reduced rational norm ratio p/q as in (6), including every
ideal in both norm fibers. Then, for Y,H sufficiently large and 1<=H<=Y,

 AbsX(D;Y,H;w)
    <= C_(K,c0) Z H [1+log_+(D/Y)]^2 /[log(2Y)log(2H)]. (7a)

Here log_+(t)=max(0,log t). The constant is independent of m>=4, phases,
physical rows, and extra excluded primes. The same assertion holds for
native Mobius columns. At Y=D^theta,H=D^eta this is O_(theta,eta)(Z D^eta).
For the principal scalar data, Theorem 1 proves that the power D^eta cannot
in general be improved for this selector. Thus the result includes an
actual uniform absolute UPPER bound as well as the signed positive lower
bound. Its application does not erase any physical zero in an identity.

Sections 2--6 prove the theorems. Section 4 also supplies an exact polynomial
main term with a power-saving Mellin error before estimating the prime pairs.

## 2. Exact local sign: two exchanges give positive correlation

Take a split rational prime p outside S and denote its two ideal phases by
b_+,b_-. Put v=1-1/p and h=p^(m/2-1). The COMPLETE norm Euler polynomial is

    (1-v t-b_+ h t^m)(1-v t-b_- h t^m)
      =1-2v t+v^2 t^2-h(b_++b_-)t^m
               +v h(b_++b_-)t^(m+1)+h^2 b_+b_- t^(2m). (10)

For m>=4 the displayed degrees are distinct and their consecutive overlaps
are exactly at e=0,1,m. Consequently

    A(p^(e+1)) conjugate(A(p^e)) = -r_p(e),
    r_p(0)=2v,
    r_p(1)=2v^3,
    r_p(m)=v p^(m-2)|b_++b_-|^2,
    r_p(e)=0 otherwise.                               (11)

All r_p(e) are real and nonnegative; r_p(0)>0. For the native source replace
(10) by (1-t)^2, giving r_p(0)=r_p(1)=2 and all other r_p(e)=0.
At an inert rational prime the norm polynomial has only even degrees, so a
rational exponent difference one contributes zero.

For p!=q write k=p^i q^j k0 with (k0,pq)=1. Multiplicativity gives exactly

    A(pk) conjugate(A(qk))=r_p(i)r_q(j)|A(k0)|^2>=0.     (12)

No independence, coprimality of k with pq, or cancellation assumption was
used. All common prime powers remain. Since k=1 has positive coefficient and
K_D>0, X_pq(D)>0 for EVERY D>0.

More generally, for relatively prime squarefree rational integers a,b all
of whose prime factors split outside S,

    sign[A(ak) conjugate(A(bk))]=(-1)^omega(ab)          (13)

whenever that coefficient is nonzero. This follows by applying (11) at every
prime of ab and |A(p^e)|^2 at all other primes. The complete ratio channel
has this strict sign for every D>0. Individual ideal-pair summands need not
have this sign; complete norm aggregation is essential.

The restrictions are substantive. At m=3, b_+=b_-=-1 makes A(p^3)>0 and
A(p^2)>0, so the extra consecutive product at e=2 is positive, contrary to
(11). Arbitrary ordinary phases a_p also need not satisfy (11). The theorem
is not promoted to all physical character rows or moving exclusions.

## 3. The norm-square Dirichlet series: a pole of order two

Let

    Q_p(s)=sum_e |A(p^e)|^2 p^(-es),
    F(s)=sum_(n>=1) d(n)n^(-s)=product_p Q_p(s), Re s>1.

At a good split prime, put B=b_++b_-, C=b_+b_-. From (10),

 Q_p(s)=1+4v^2 p^(-s)+v^4 p^(-2s)
   +|B|^2 p^(m-2-ms)+v^2|B|^2 p^(m-2-(m+1)s)
   +|C|^2 p^(2m-4-2ms).                               (14)

At an inert prime p, the local factor is

    1+(1-p^(-2))^2 p^(-2s)+|b|^2 p^(2m-4-2ms).        (15)

At finitely many primes below S keep the literal surviving polynomial.
Let rho=1-1/m. Then

    F(s)=zeta_K(s)^2 G(s),       Re s>1,                (16)

where G is holomorphic on Re s>rho and bounded uniformly in the b-profile on
every closed sub-half-plane. It is given by multiplying Q_p by
(1-p^(-s))^4 at split primes and by (1-p^(-2s))^2 at inert primes, with the
actual finite ramified/excluded factors.

Here is a direct convergence proof, without invoking #954's Tauberian limit.
The split local product minus one is bounded on Re s>=sigma>rho by a constant
(depending on m,sigma) times

    p^(-1-sigma)+p^(-2sigma)+p^(m-2-m sigma).           (17)

The first term retains the small difference 4v^2-4; it is NOT set to zero.
All three powers have prime-sum decay strictly greater than one. The other
terms from multiplication by (1-p^(-s))^4 are smaller. The inert local error
is bounded by p^(-2sigma)+p^(2m-4-2m sigma), also summable. Finite exceptional
factors are polynomials. This proves normal convergence and uniform bounds.
For real s>rho all local factors are positive. In particular G(1)>0, with
upper and lower bounds depending only on fixed S, uniformly in b (and for
G(1) also in m>=4). This follows from 1+O(p^-2) and positivity of the finitely
many initial factors. Since the ordinary linear coefficient remains, there
is no profile which makes the residue vanish.

For the native source the same argument works on Re s>1/2: split Q_p is
1+4p^-s+p^-2s, and inert Q_p is 1+p^-2s.

Only elementary continuation theory is needed here. Use

    zeta_K(s)=zeta(s)L(s,chi_-3),
    zeta(s)=s/(s-1)-s integral_1^infinity {x}x^(-s-1)dx,
    L(s,chi_-3)=s integral_1^infinity A_chi(x)x^(-s-1)dx,
    |A_chi(x)|<=1.                                    (18)

These formulas give meromorphic continuation and polynomial vertical bounds
on positive closed strips, with the sole pole at one. The residue of
zeta_K at one is positive. Hence F has a double pole at one, and no other
poles on Re s>rho. Zeta zeros are harmless here: all zeta factors MULTIPLY;
no inverse-zeta estimate or zero-free hypothesis appears.

Write its Laurent expansion as

    F(1+z)=C_* z^(-2)+B_* z^(-1)+D_*+O(z),
    C_*=(Res_(s=1) zeta_K(s))^2 G(1)>0.                (19)

At fixed m,S the coefficients in (19), and sufficient derivatives of G near
one, are bounded uniformly over the b-profile; C_* has a uniform positive
lower bound. Normal convergence on a fixed disk about one proves this.

For later use define the positive polynomial

    R_p(s)=sum_e r_p(e)p^(-es)
      =2v+2v^3p^(-s)+v|B|^2p^(m-2-ms).                (20)

Let F_pq(s) be the Dirichlet series of the coefficients in (12). Exactly,

    F_pq(s)=R_p(s)R_q(s) product_(l!=p,q) Q_l(s).       (21)

Equation (21), rather than division by possibly zero local polynomials, is
the definition of its continuation. Multiplying the same zeta_K(s)^2 by
the product in (17) with two factors omitted and inserting the appropriate
local inverse-zeta polynomials and R_p,R_q gives holomorphy and polynomial
vertical bounds, UNIFORMLY in p,q. For sigma>rho, (20) is uniformly bounded
at every p>=7, as are the inserted inverse-zeta polynomials. No local zero
exclusion is needed for this argument.

Near s=1 it is legitimate to write F_pq=F t_p t_q, t_p=R_p/Q_p, since Q_p(1)>0.
The Laurent coefficients are explicitly

    C_pq=C_* t_p(1)t_q(1),
    B_pq=B_* t_p(1)t_q(1)+C_* (t_p t_q)'(1),
    D_pq=D_* t_p(1)t_q(1)+B_* (t_p t_q)'(1)
                                  +(C_*/2)(t_p t_q)''(1). (22)

Uniformly at large split p,

    t_p(1)=2+O_m(1/p),
    t_p'(1)=O_m(log p/p),
    t_p''(1)=O_m((log p)^2/p).                          (23)

These follow directly from (14),(20); the powerful terms at s=1 have
size O(p^-2). They also hold in the native case. Constants are uniform in b.

## 4. An explicit full logarithmic polynomial with a power error

For T>0 put

    H_pq(T)=sum_k A(pk)conjugate(A(qk))/k
                               Phi(log T-log k-beta). (24)

### Theorem 2: moving-prime-uniform Mellin evaluation

For any fixed 0<delta<1/m, uniformly in distinct good split primes p,q,
all T>0, and |b_p|<=1,

 H_pq(T)=(C_pq/2)[(log T-beta)^2+1]
                 +B_pq(log T-beta)+D_pq+O_(m,S,c0,delta)(T^-delta). (25)

For the native source, any 0<delta<1/2 is allowed. All constants retain the
fixed S dependence. This improves #954's leading norm-collision asymptotic
in this quadratic, fixed-m setting to a full polynomial with a power error;
it is not a uniform-in-m error exponent.

Proof. For u>0, Gaussian Mellin inversion gives

 Phi(log u-beta)=(1/(2pi i)) integral_(Re z=a>0)
                       exp(z^2/2-beta z)u^z dz/z.     (26)

One may differentiate with respect to log u and use the elementary Gaussian
Fourier integral, then take the limit u->0, to establish (26). On the initial
line absolute Dirichlet convergence and the Gaussian justify Fubini in (24):

 H_pq(T)=(1/(2pi i)) integral_(a)
            exp(z^2/2-beta z) F_pq(1+z) T^z dz/z.      (27)

Move the contour to Re z=-delta. Section 3 gives uniform polynomial vertical
bounds and no poles except at zero. Horizontal integrals vanish by
exp(-Im(z)^2/2); the new integral is O(T^-delta), uniformly in p,q, including
when T<1. The residue of the third-order pole is exactly (25), by (22).
This is a positive-square correlation series, not the critical inverse-zeta
series whose zeros are in question. QED.

The same formula with (C_*,B_*,D_*) and no p,q gives a complete quadratic
polynomial plus O(T^-delta) for the full equal-norm harmonic sum. This
equal-norm corollary is credited as an extension of #954, not its rediscovery.

From the homogeneous Gaussian kernel,

 X_pq(D)=kappa exp[-log(p/q)^2/8]/sqrt(pq)
                                      H_pq(D/sqrt(pq)). (28)

Thus (25) evaluates the ENTIRE ratio channel, not a truncation in common k.
For any finite collection of ordered prime pairs, the sum of remainders in
(28) is at most

 C D^-delta sum_(p,q) (pq)^((delta-1)/2)
                                      exp[-log(p/q)^2/8]. (29)

This is a rigorous error bound for an explicit residue-polynomial main term,
even though a prime-pair asymptotic in every short interval is unavailable.

For fixed theta in (0,1), put Y=D^theta. Uniformly for p,q in [Y,2Y], (22)--(25)
give

 H_pq(D/sqrt(pq))=2 C_* (1-theta)^2(log D)^2+O_(m,S,c0,theta)(log D). (30)

For clarity, before absorption the error is bounded by

 C[log D+(log D+log Y)^2/Y+(D/(2Y))^-delta].

The O(log D) statement is valid for sufficiently large D with theta fixed.
In particular there are positive constants c,C, uniform in b, such that

 c (log D)^2/Y <= X_pq(D) <= C (log D)^2/Y.             (31)

The lower bound is substantive because C_* stays uniformly positive.

## 5. Short pair counts without assuming any prime-pair conjecture

Let N(Y,H) count ordered distinct split-prime pairs p,q in [Y,2Y] with
|p-q|<=H. For every fixed lambda in (0,1),

    N(Y,Y^lambda) asymp_lambda Y^(1+lambda)/(log Y)^2. (32)

This is a TWO-SIDED ORDER BOUND, not an asymptotic with the Hardy--Littlewood
constant, and not a claim about a particular fixed prime gap.

Lower bound. The classical PNT in the fixed progression 1 mod 3 gives
M:=#P(Y)~Y/(2 log Y). Partition [Y,2Y] into J<=Y/H+2 intervals of length at
most H. If their prime counts are M_j, then

    N(Y,H)>=sum_j M_j(M_j-1)>=M^2/J-M.                 (33)

For H/log Y->infinity this is >=c YH/(log Y)^2. This argument needs no
prime distribution theorem WITHIN those short intervals. Finite S has no
asymptotic effect.

Upper bound. We prove the elementary uniform estimate

    pi(x+L)-pi(x)<=C L/log L, for L sufficiently large, x>=0. (34)

Let z=floor(L^(1/8)) and G(z)=sum_(r<=z)mu(r)^2/phi(r). Define

 y_r=mu(r)/(phi(r)G(z)),
 lambda_d=d sum_(k<=z/d)mu(k)y_(dk).

Then lambda_1=1, lambda_d=0 for nonsquarefree d, and by Mobius inversion

 sum_(d<=z, r|d)lambda_d/d=y_r.

The lcm identity 1/[d,e]=sum_(r|d,e)phi(r)/(de) gives

 sum_(d,e<=z)lambda_d lambda_e/[d,e]
          =sum_(r<=z)phi(r)y_r^2=1/G(z).               (35)

For squarefree d,

 lambda_d=mu(d)d/[phi(d)G(z)]
               sum_(k<=z/d,(k,d)=1)mu(k)^2/phi(k),

so |lambda_d|<=d and sum|lambda_d|<=z(z+1)/2.
Every integer with no prime factor <=z has sum_(d|n,d<=z)lambda_d=1.
Counting integers in the interval by residue classes therefore bounds
such integers by

    L/G(z)+O((sum|lambda_d|)^2)=L/G(z)+O(z^4).         (36)

Squarefree counting by the union of multiples of d^2 gives
sum_(n<=t)mu(n)^2>=t/4-1, since sum_(d>=2)d^-2<=3/4.
Partial summation then gives G(z)>=sum_(n<=z)mu(n)^2/n>=c log z for large z.
Primes <=z add at most z to (36). As z^4=O(L^(1/2)), (34) follows.
This is the classical Selberg quadratic upper-sieve calculation, included
to avoid treating a short-interval PNT as an input.

For each p in [Y,2Y], (34) applied to an interval of length 2H bounds the
possible q by C H/log H. Together with M=O(Y/log Y),

    N(Y,H)<=C YH/(log Y log H).                        (37)

Set H=Y^lambda. Equations (33),(37) prove (32). No unproved twin-prime,
prime-pair, or short-interval equidistribution assertion occurs.

## 6. Proof of the theorems and a macroscopic asymptotic

First prove the uniform upper statement (7a). Let M_m(n) be the complete
positive norm-fiber majorant, obtained by replacing the ideal local factors
by 1+(1-1/q)t+q^(m/2-1)t^m and using only the exclusions above 2 and 3.
Then sum_(N a=n)|c(a;u)|<=M_m(n) for every physical row and every mask. For
m>=4 its rational-prime norm polynomial has the same coefficient magnitudes
as the PRINCIPAL UNIT-b source in (10). Thus M_m(n)=|A_unit(n)|. Consequently

 M_m(pk)M_m(qk)=r_p,unit(i) r_q,unit(j) M_m(k0)^2,

using k=p^i q^j k0 as in (12). All terms are positive. This identity is for
a MAJORANT, not a claim that arbitrary physical phases have the principal
sign. Bounding the physical ideal-pair absolute sum by this majorant is valid.

For 0<u<=1 the positive Euler comparison in (14)--(17) ON THE REAL LINE gives

 sum_n M_m(n)^2/n^(1+u) <= C_K zeta_K(1+u)^2 <= C'_K/u^2, (37a)

uniformly in m. To check uniformity, at a split prime the powerful square
terms at 1+u have sizes <=4/p^2, 4/p^3, 1/p^4. The unmatched linear term is
O(p^-2); the product of the resulting 1+C/p^2 factors converges. Inert primes
have summable errors as well. The native variant has no powerful terms.
Moreover R_p,unit(1+u)<3 and Q_p,unit(1+u)>=1, so the exchange series at 1+u
is at most nine times (37a), independently of p,q,m.

The elementary Gaussian exponential-moment inequality

 Phi(log(T/n)-beta)<=exp(u^2/2-u beta)(T/n)^u

follows by applying Markov's inequality to exp(-u Z_0) for a standard normal
Z_0; it can also be verified directly by completing the square in its
integral. Take u=1/log T for T>=e and u=1 for 0<T<e. Equation (37a) yields

 H_pq,unit(T)<=C_(K,c0)[1+log_+ T]^2,                  (37b)

uniformly in m and p,q. Multiply (37b) by kappa/sqrt(pq)<=kappa/Y and the
prime-pair upper count (37). Since T=D/sqrt(pq)<=D/Y, this is (7a). Sum over
w; its total mass is the only cost. This proof uses a uniform real Rankin
bound, rather than pretending that the fixed-m contour width stays fixed
as m tends to infinity.

For the principal signed two-sided statement, choose lambda=eta/theta.
Multiply (31) by (32), with Y=D^theta:

    X(D;Y,H) asymp [(log D)^2/Y] [YH/(log Y)^2]
                asymp_(theta,eta) H.

This proves (7), and then (8)--(9). The equality of the signed channel with
a nonnegative expression was proved BEFORE taking any norms, in (12).
We have not replaced the remaining full energy by the sum of absolute
values. The result is valid for the complete Gaussian, not just ideals
below D.

There is also an explicit leading asymptotic when H=Y (all p,q in [Y,2Y]):

 X(D;D^theta,D^theta)
   ~ (kappa C_*/2) [(1-theta)/theta]^2 J D^theta,
 J=integral_1^2 integral_1^2 exp[-log(u/v)^2/8]/sqrt(uv) du dv>0. (38)

To verify constants, (30) contributes 2 C_* (1-theta)^2 log^2 D;
(28) contributes kappa/Y times the displayed kernel; the two PNT densities
for rational split primes contribute Y^2/[4 log^2 Y]. Their product is
(38). Diagonal p=q is excluded and has smaller order. PNT and partial
summation justify the two-dimensional continuous weight, uniformly on the
compact square [1,2]^2. The limit is for fixed m,S and fixed b-profile.
Equation (29) is the power-error statement relative to the exact prime-
indexed polynomial; (38) itself uses only o(1) from the classical PNT.
Do not call the latter a power-saving prime-distribution error.

## 7. Interpretation, scope, and remaining target

The gain over #953 is a quantitative theorem for pairs where NEITHER ideal
divides the other, BOTH reduced rational cores grow polynomially, and their
ratio tends to one. The gain over #954's bounded-degree norm graph is a
source-specific signed evaluation; it is not a long Mellin average. The
power-error logarithmic polynomial extends the quadratic equal-norm
analysis, but the shrinking prime-exchange law is the main new target here.
No exhaustive literature-priority claim is made.

This theorem does not imply E(D) asymp D^eta. The selector in (6) is not a
positive-semidefinite subprojection of the full moment. Other ratio sectors
have both signs, as (13) exhibits. In particular one may NOT infer a lower
bound E(D)>=X(D;Y,H) from positivity of E or positivity of this selected sum.

If the desired E(D)=O_epsilon(D^epsilon) holds, the complement of (6) must
cancel this power-sized positive contribution. That is a conditional
necessity, not a newly established cancellation. The theorem explains why
bounding the large-core covariance one same-sign exchange pattern at a
time cannot close the critical estimate. All exchange parities and their
actual common-core coefficients must be combined before the final upper
bound. Existing finite-prime completions do not by themselves prove that
combination is small.

The full fixed-twist signed energy, generalized sextic moments at the
required physical heights, and RH remain unproved in this packet.
