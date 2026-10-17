# Joint archimedean resolution of the complete native moment

Status: PROPOSED unconditional component proofs. No independent mathematical
review, new zero-free half-plane, principal-member moment theorem, or RH proof.
The additional average in this note is part of the theorem, not an omitted
hypothesis. All moment orders are FIXED. Constants need not be uniform in k.

## 1. Exact family and statements

Let K=Q(omega), omega^2+omega+1=0, O=Z[omega]. Ideals are integral and nonzero.
An ideal I=(alpha) has norm |alpha|^2. Its six generators differing by units
have the same

    psi_l(I)=(alpha/|alpha|)^(6l), l in Z.                    (1)

This is a genuine unitary multiplicative ideal character. For l!=0 it has
infinite order; it is NOT one of the finite-order characters in #959.
Distinct ideals with equal rational norm are not identified. At l=1 the
value is exactly alpha^6/(NI)^3 in Q(omega).

Fix a nonnegative measure w of finite mass Z_w. It can be the original
nonzero Eisenstein element rows in a ball, and is held FIXED at every column
scale. At each prime ideal p of norm q choose measurable |a_p(u)|,|b_p(u)|<=1.
Deleting p sets both to zero. A fixed or moving exclusion is implemented this
way, without changing the row measure. Choose one of the exact local sources
used in #955, for an integer m>=2:

    native       1-a_p x;
    coupled      1-(1-1/q)a_p x-b_p q^(m/2-1)x^m;
    two-channel  (1-a_p x)(1-b_p q^(m/2-1)x^m);
    geometric    1-(1-1/q)a_p x/(1-b_p q^(m/2-1)x^m).       (2)

Denote the multiplicative coefficients by c(I,u). The native sextic source
is a_p(u)=nu(p)chi_p(u), with its literal zero at a nonunit; its original
Mobius signs are unchanged. Powerful terms keep their original masks and
coefficients. The twist in (1) multiplies the ENTIRE ideal, not only its radical.

For bounded W supported in (0,1], set

    A_(t,l)(X,u)=sum_I c(I,u) W(NI/X) (NI)^(it) psi_l(I).

Write a_k=(k-1)^2. For R>=1 put

    g_R(t)=exp(-t^2/(2R^2))/(sqrt(2pi) R),
    p_R(l)=exp(-l^2/(2R^2))/sum_(j in Z)exp(-j^2/(2R^2)).

For centers t0 real, l0 integer, angled brackets denote

    <F>_R=sum_l p_R(l-l0) integral_R g_R(t-t0) F(t,l) dt.   (3)

Both infinite tails are retained. This is a deterministic Hecke-character
average, not independent-prime randomization.

**Theorem A (full hybrid moment).** For every fixed integer k>=1, X>=2,

    < integral |A_(t,l)(X,u)|^(2k) dw(u) >_R
      <= C_k ||W||_infinity^(2k) Z_w X^k
                     log(3X)^a_k (1+X^k/R^2).              (4)

Constants are uniform in m, the phase/mask profiles, the exclusions, centers,
and row measure. They depend on k and the fixed field. No finite-order Hecke
zero-free theorem, theta bound, or unknown native moment is used.

Define the L2 ideal-product diagonal by expanding the ACTUAL product

    A_(t,l)(X,u)^k=sum_J B_J(X,u)(NJ)^(it)psi_l(J),
    D_k(X;w)=sum_J integral |B_J(X,u)|^2 dw(u).              (5)

All ideal products and factorization multiplicities occur. For R>=2 X^(k/2),

    (1-600/2401)D_k <= <moment>_R <= (1+600/2401)D_k.       (6)

For scalar principal native coefficients with a fixed excluded set S and
W=1_(1/2,1], both sides have the sharp order

    X^k log(X)^((k-1)^2).                                 (7)

This is order of magnitude, not an asymptotic leading constant. For orders
2,4,6 it is X, X^2 log X, X^3 log^4 X. None is a fixed-(t,l) bound.

## 2. An explicit geometric large-sieve calculation

We first prove a statement for ANY finite Hilbert-space-valued ideal array
v_I, NI<=Y. It is independent of (2).

Let phi_I=6 arg(alpha) modulo 2pi. Poisson summation for the one-dimensional
Gaussian, or its directly computed Fourier series, gives

    Theta_R(theta)=sum_l p_R(l) exp(i l theta)
      = [sum_j exp(-R^2(theta-2pi j)^2/2)]
                       /[sum_j exp(-2pi^2 R^2 j^2)].       (8)

The denominator is at least one. If delta=dist(theta,2pi Z) in [0,pi],
then for R>=1

    0<=Theta_R(theta)<=3 exp(-R^2 delta^2/2),
    Theta_R(0)=1.                                         (9)

For the first inequality, take the two nearest representatives; their terms
are each at most exp(-R^2 delta^2/2). Every next pair has additional squared
distance at least 4pi^2 j^2, j>=1. The resulting multiplicative factor is
at most 2[1+sum_(j>=1)exp(-2pi^2 j^2)]<3. This deliberately loose constant
also covers an endpoint tie.

The exact averaging kernel, apart from its center phase of modulus one, is

    K_R(I,J)=exp(-R^2 log(NI/NJ)^2/2) Theta_R(phi_I-phi_J).
                                                               (10)

For a fixed generator alpha of I, choose a generator beta of J by a unit
rotation so that the angle theta between them has |theta|<=pi/6. Then
6|theta|=delta. With NI,NJ<=Y,

 |alpha-beta|^2
   =(|alpha|-|beta|)^2+4|alpha beta| sin(theta/2)^2
   <=Y [log(NI/NJ)^2/4+delta^2/36]
   <=(Y/4)[log(NI/NJ)^2+delta^2].                           (11)

Here 1-exp(-v)<=v bounds the radial difference. If I!=J, alpha-beta is a
NONZERO Eisenstein integer; its norm is at least one. For fixed I the chosen
beta, hence beta-alpha, is injective in J. Ties are fixed once.
Consequently

    sup_I sum_(J!=I) |K_R(I,J)| <= rho(R/sqrt(Y)),
    rho(s)=3 sum_(0!=z in O) exp(-2s^2 Nz).                (12)

Since N(a+b omega)>= (a^2+b^2)/2, elementary Gaussian sums imply

    rho(s)<=C/s^2, s>0;   rho(s)<=C exp(-s^2), s>=1.       (13)

For s<=1 use sum_(n in Z)e^(-s^2n^2)<=1+sqrt(pi)/s. For s>=1,
sum_(n>=1)e^(-s^2n^2)<=e^(-s^2)/(1-e^(-s^2)); the square of the resulting
one-dimensional bound, minus one, is O(e^(-s^2)). Enlarging C proves (13).

The Schur bound follows without a scalar-coefficient assumption: expand the
quadratic form, apply Hilbert Cauchy and 2ab<=a^2+b^2 to each pair. Thus

 | <||sum_I v_I (NI)^(it)psi_l(I)||^2>_R - sum_I||v_I||^2 |
       <=rho(R/sqrt(Y)) sum_I||v_I||^2.                    (14)

For s>=2, use e^4>50 and n^2>=n to get the explicit bound

 rho(s)<=3[(1+2/(e^4-1))^2-1]
          <3[(1+2/49)^2-1]=600/2401<1/3.                  (15)

The inequality e^4>50 follows already from its Taylor terms through degree
seven. This proves (6), once Y=X^k. It also proves that at LARGE widths the
complete hybrid moment converges to the IDEAL diagonal, rather than the
larger rational-norm diagonal. No signed off-diagonal has been discarded.

The operator estimate also gives the polarized bound

    |B_R(v,z)|<=C Y/R^2 ||v||_ell2 ||z||_ell2,             (16)

where B_R is the averaged pairing minus the ideal-diagonal pairing and the
union of the two coefficient supports lies in NI<=Y. Indeed the matrix in
(14) is Hermitian with zero diagonal and Schur operator norm <=C Y/R^2.

## 3. Arithmetic diagonal with the ideal identity retained

A common positive coefficient majorant for every source (2) is

    T_(m,q)(x)=(1+x)/(1-q^(m/2-1)x^m).                     (17)

Its coefficient t_m(I) has the unique representation I=b d^m, b squarefree,
with no imposed coprimality between b and d; its value is (Nd)^(m/2-1).
At any x>=1, ideal counting therefore gives, uniformly in m>=2,

    sum_(NI<=x)t_m(I) <=C_K zeta_K(2)x,
    sum_(NI<=x)t_m(I)^2 <=C_K zeta_K(2)x.                  (18)

For example, in the squared sum first sum b with Nb<=x/(Nd)^m; its contribution
is <=C_K x/(Nd)^2. Every actual |c(I,u)| is at most t_m(I), including at deleted
primes. We enlarge the majorant to ALL primes, so the constants are independent
of a varying excluded set.

We give the sharper multivariable count needed for general k. Introduce the
2k-variable ideal-coefficient array selecting EXACT ideal-product equality

    I_1 ... I_k = J_1 ... J_k

and having coefficient product_i t_m(I_i)t_m(J_i). Its formal Dirichlet series
factors as

    P_m(s;t)=H_m(s;t) product_(i,j) zeta_K(s_i+t_j).        (19)

The signed coefficient array h_m of H_m satisfies

    sum_(R_i,S_j) |h_m(R;S)|/sqrt(product_i NR_i product_j NS_j)
          <=C_(K,k),                                    (20)

uniformly in m. Every term of h_m balances the two ideal products.

Here is a local proof, including the uniformity. Set r=q^(-1/2). The total
critical absolute mass of (17) is (1+r)/(1-r^2)=1/(1-r). The total mass of
k slots is (1-r)^(-k), its degree-one part is exactly k r, and its terms of
ideal-prime degree >=2 have total O_k(r^2), uniformly in m and 0<r<=1/sqrt(2).
Equality of the two degrees makes the balanced local factor

    1+q^(-1)sum_(i,j) z_i w_j+O_ell1,k(q^-2),              (21)

where the formal slot variables retain all allocations. The tail is bounded
by the product of the two degree-at-least-two masses. Multiplying by
product_(i,j)(1-z_i w_j/q), the critical version of the inverse zeta factors,
removes exactly the displayed term. Hence the local quotient has absolute
mass 1+O_k(q^-2). The prime-ideal sum of q^-2 converges. The finitely many
small primes are bounded by (1-r)^(-2k)(1+r^2)^(k^2). Multiplying proves (20).
These are formal coefficient identities and absolute mass estimates; no
meromorphic continuation or conditional Euler product is used.

For arbitrary caps X_i,Y_j>=1, let Q(X;Y) count k by k matrices of ideals
A_ij with row-product norm <=X_i and column-product norm <=Y_j. Then

    Q(X;Y)<=C_(K,k) sqrt(product X_i product Y_j)
                 [1+log(2 max(X_i,Y_j))]^((k-1)^2).        (22)

Proof. Put NA_ij in [2^b_ij,2^(b_ij+1)), b_ij>=0. Ideal counting bounds the
box by C_k 2^(sum b_ij). Let R_i=floor(log_2 X_i), C_j=floor(log_2 Y_j),
A=sum R_i,B=sum C_j,s=sum b_ij, delta=(A+B)/2-s. Both row and column deficits
are nonnegative. At fixed s their totals are A-s,B-s. Choose the first k-1
row and column deficits and the first (k-1)^2 matrix entries; the remaining
entries are determined. Thus at most

    (1+max(R_i,C_j))^((k-1)^2)(1+2delta)^(2k-2)

boxes occur. Sum 2^(-delta)(1+2delta)^(2k-2) over the nonnegative integer or
half-integer grid. This sum is finite for fixed k. The prefactor
2^((A+B)/2) is at most sqrt(product X_i product Y_j), proving (22).
This is the classical transportation-matrix argument; it is credited to the
preceding #955 implementation, not claimed as a new counting principle.

Convolve (22) with h_m using caps X/NR_i,X/NS_j. Caps below one contribute
nothing. Their square-root factor pays exactly the denominator in (20).
Consequently

    D_k(X;w)<=C_(K,k)||W||_infinity^(2k) Z_w X^k log(3X)^a_k. (23)

Together (13),(14),(23) prove Theorem A. Replacing ideal equality by rational
norm equality would instead use zeta_(K tensor K) in (19), as in #955, and
would give the larger exponent 2k^2-2k+1. That replacement is NOT made here.

## 4. Sharp lower order for the principal native source

Fix S and the hard window (X/2,X]. For each product ideal J, every ordered
factorization into squarefree columns has the same Mobius product sign,
(-1)^Omega(J). Thus its contribution to D_k is a positive squared multiplicity.
It suffices to count a subset of tuples with ideal-product equality.

We give the elementary lower construction. For fixed r, ideals A_1,...,A_r in
independent short multiplicative boxes (B_i,(1+eta)B_i], all B_i tending to
infinity, are squarefree, pairwise coprime and prime to S with count

    >=c_(K,r,S,eta) product B_i.                            (24)

To justify uniformity over the boxes, first impose the finitely many local
conditions at Np<=L. Ideal counting in multiples of each fixed ideal has
main term Res(zeta_K,1)x/Nd and o(x), uniformly as the minimum B_i tends to
infinity. Inclusion-exclusion gives a product of positive local densities.
Outside S the factor is (1-1/q)^r(1+r/q), which is 1+O_r(q^-2); its product
is positive. At primes in S the factor is (1-1/q)^r. The bad tuples at Np>L
have either p^2 dividing one ideal or p dividing two ideals. Counting these
multiples using #ideals<=Cx gives at most
C_r product B_i sum_(Np>L)q^-2. Choose fixed L sufficiently large, then let
min B_i grow. This proves (24); no prime ideal theorem is needed.

Use r=k^2 and boxes for a matrix A_ij. Set R0=3X/4 and choose fixed eta>0
with (1+eta)^k<4/3. Specify log B_ij=(log R0)/k+h n_ij, where h>log(1+eta)
and all integer row and column sums of n_ij are zero. Choose the first
(k-1)^2 entries independently with |n_ij|<=c_k log X, with c_k sufficiently
small; the last row and column are determined. All B_ij>=X^(1/(2k)) for
large X. There are >=c_k(log X)^((k-1)^2) choices, and their free-coordinate
boxes are disjoint. Each box tuple has product_ij B_ij=R0^k. By (24) each
contributes >=c_k X^k pairwise-coprime squarefree matrices prime to S.

Set I_i=product_j A_ij and J_j=product_i A_ij. Every column is squarefree,
all norms belong to (X/2,X], and the products agree as IDEALS. The matrix is
recoverable as A_ij=gcd(I_i,J_j), so these tuples are not multiply counted.
This proves D_k>=c_k X^k log(X)^a_k, including k=1 with no free coordinates.
Use (6) to obtain (7). This is classical multiplicative-energy lower geometry,
not a statement of global novelty.

## 5. What the change of averaging buys, and what it does not

For k=2, #955's norm-only mean has order X^2 log^5 X after a one-dimensional
window T>=2X^2. The present full two-parameter mean has order X^2 log X with
both widths R>=2X. Their probability measures DIFFER. The new effective
parameter volume R^2 is still of order X^2; the theorem does not save a power
of total averaging volume. It resolves the extra equal-norm ideal collisions
rather than proving their Mobius signs cancel.

More generally (23) covers any coefficient array pointwise dominated by t_m;
multiplicativity of that array is unnecessary. In particular t_2(I)=1, so
arbitrary bounded ideal coefficients are covered as well. This confirms that
the gain is geometric resolution under the declared average, NOT a newly
proved Mobius-specific cancellation mechanism. The geometric estimate (14)
allows entirely arbitrary coefficients and retains their actual ideal-product
energy. The physical measure w may be arbitrary; its mass is explicitly paid.

At no point may one remove the l average, set t=l=0 after averaging, or apply
#959's finite-order Hecke zero-free statement to psi_l. No bound for the
original fixed-principal-twist critical covariance, no 17/24 result, and no
shrinking band in zero ordinate follows. A uniform growing-k constant is
also not supplied. The actual new estimate is the complete hybrid moment
and, in GAUSSIAN_ENERGY.md, its full-tail cumulative energy.

## 6. The averaging-volume price is necessary even for native coefficients

For scalar principal native coefficients, fixed S and W=1_(1/2,1], there are
centers t0=t0(X) with l0=0 such that, for EVERY R>=1,

    <|A_(t,l)(X)|^(2k)>_R >=c_(k,S) X^(2k)/R^2.           (25)

This is a supremum-over-centers statement, not a claim at center zero. It
shows that the power threshold R^2~X^k cannot be improved for the theorem's
uniform-center formulation, apart from logarithms. It extends the same
native-center warning in #955 to the present TWO-parameter measure, rather
than purporting to evade it.

Proof. For each rational prime p supporting a good ideal of norm <=X, prescribe
p^(it0) close to -1 at a split prime and close to i at an inert prime. If
the ramified prime over 3 is not excluded, prescribe 3^(it0) close to -1
as well. Then every allowed ideal-prime norm has phase close to -1, including
the inert norm p^2.
Distinct split prime ideals are retained; the same -1 is correct at both.
Choose the approximation sufficiently accurate, say angle error less than
1/(100 log(2X)) per rational prime. Unique factorization of integers implies
that the finitely many log p are linearly independent over Q. The continuous
orbit t -> (exp(it log p)) is dense in the finite torus: a proof is to average
a smooth nonnegative bump in any desired box along 0<=t<=T. Its absolutely
convergent Fourier series has nonconstant frequencies sum_j n_j log p_j !=0,
whose averages tend to zero. The limiting average is the positive torus
integral, so the orbit enters the box. Thus an appropriate t0 exists. No
polynomial or effective upper bound for it is claimed here.

For every good squarefree I in the window, mu_K(I)(NI)^(it0) is within a
fixed small angle of 1, since Omega(I)<=log X/log 2. At l=0 and |s|<=1/10,
remove the common phase X^(is); the additional angle s log(NI/X) is at most
(log 2)/10. Hence |A_(t0+s,0)(X)|>=c times the number of such ideals, which
is >=c_S X by the elementary squarefree density proved in GAUSSIAN_ENERGY.md.
For R>=1, p_R(0)>=c/R and g_R(s)>=c/R on this fixed interval. Retaining only
l=0 and |s|<=1/10 in the NONNEGATIVE full average proves (25).

The equality-of-ideals diagonal is O(X^k log^a_k X). Therefore a bound of this
size uniform in all centers forces R^2>=X^k/log^O_k(1)X. A proposed principal
member argument must retain its fixed center instead of using this adversarial
supremum. The positive results (4),(G1) still hold at all centers.

## 7. A logarithmic improvement for the SAME short radial average

The two-coordinate theorem also gives a bound without leaving an angular
average in the conclusion. Its cost must be paid explicitly.

**Corollary D.** For any FIXED angular character psi_(l0), T>=1,

 integral_R g_T(t-t0) integral |A_(t,l0)(X,u)|^(2k) dw dt
       <= C_k Z_w ||W||_infinity^(2k) X^k log(3X)^a_k
                                               (T+X^k/T). (26)

For 1<=T<=X^(k/2) this is

       <=C_k Z_w ||W||_infinity^(2k) X^(2k)/T log(3X)^a_k. (27)

In particular, with l0=0 this is the ORIGINAL norm-only average in #955.
Its earlier short-window bound has the same power X^(2k)/T but logarithm
2k^2-2k+1; (27) reduces that logarithmic exponent by k^2. At fourth order
and 1<=T<=X the comparison is X^4 log^5 X/T versus X^4 log X/T.
No power saving or pointwise moment is claimed.

Proof. The exact probability of l=l0 in (3) is p_T(0). The elementary
Gaussian sum gives p_T(0)^(-1)<=1+sqrt(2pi)T<=C T. All summands in the
averaged moment are nonnegative, so the fixed-l0 radial mean is at most
p_T(0)^(-1) times (4), with R=T. This is exactly (26). In the displayed
short-window range, T<=X^k/T, proving (27). This deduction does NOT remove
the angular average at no cost: the factor T is present in (26).

For T outside that range, (26) remains valid but need not beat #955. One
may take the minimum of their two bounds. This concrete same-functional
logarithmic improvement is distinct from the stronger hybrid diagonal
power theorem (4). Neither is a fourth-moment estimate at fixed t=0.
