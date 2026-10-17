# Complete long-twist moments and the transport dimension

Status: PROPOSED unconditional component mathematics, not independently reviewed.
No pointwise critical moment, improved zero-free exponent, or RH proof is claimed.
All orders below are FIXED; constants are not uniform as k tends to infinity.
The method is classical multiplicative-energy / transport-polytope counting.
The source-specific extensions and bounds below are not a global priority claim.

## 1. Statements and the distinction that matters

Fix a number field F and a finite excluded set S of prime ideals. Write
F tensor_Q F = E_1 x ... x E_r, with repeated factors counted, and put

    a(F,k) = r k^2 - 2k + 1.                                  (1)

Thus r=2 for a quadratic field. Keep any nonnegative row measure w of finite
mass Z. At every allowed ideal prime p of norm q choose measurable complex
values |a_p(u)|, |b_p(u)| <= 1, fixed as the column scale varies. A nonunit
mask sets BOTH values to zero. Fix any integer m>=2, and choose one family:

    native       1-a_p x;
    coupled      1-(1-1/q)a_p x-b_p q^(m/2-1)x^m;
    two-channel  (1-a_p x)(1-b_p q^(m/2-1)x^m);
    geometric    1-(1-1/q)a_p x/(1-b_p q^(m/2-1)x^m).          (2)

Let f(I,u) denote the resulting multiplicative ideal coefficients; the local
factor at S is 1. Distinct prime ideals of equal norm remain distinct.
For bounded W supported in (0,1], set

    A_t(X,u) = sum_I f(I,u) (NI)^(it) W(NI/X),
    g_T(t) = exp(-t^2/(2T^2))/(sqrt(2pi) T), T>0,
    M_k(X,T,t0;w) = integral_R g_T(t-t0)
                                  integral |A_t(X,u)|^(2k) dw(u) dt. (3)

These are the actual arithmetic coefficients and a real Mellin-twist
average. No independent-prime randomization is made.

**Theorem 1 (complete moment upper bound).** For every fixed k>=1 and X>=2,

    M_k(X,T,t0;w) <= C_(F,k) ||W||_infinity^(2k) Z X^k
                      (log(3X))^a(F,k) (1+X^k/T).            (4)

This is uniform in t0, m>=2, S, all masks, and all the allowed phase profiles.
It is not discriminant-uniform. For T>=2X^k the ENTIRE averaged moment has
its diagonal power X^k, with the displayed logarithm. T is not a physical
row height and this assertion does not bound the principal twist t=0.

**Theorem 2 (sharp order for the original principal native source).**
Let F=Q(omega), omega^2+omega+1=0, let S be fixed and include the primes
above 2 and 3, let f=mu_F, and let W=1_(1/2,1]. For each fixed k>=1,
all sufficiently large X, all t0 real and all T>=2X^k,

    c_(S,k) X^k (log X)^(2k^2-2k+1)
      <= M_k(X,T,t0;1)
      <= C_(S,k) X^k (log X)^(2k^2-2k+1).                (5)

This is a sharp order, NOT an asymptotic with an identified leading constant.
The orders 2,4,6 give respectively X log X, X^2 log^5 X, X^3 log^13 X.
The whole moment, including unequal-product-norm terms, occurs in (5).
The averaging window has length at least twice the product length X^k.

**Theorem 3 (full Gaussian cumulative version).** For the unchanged Gaussian

    W_c(y)=y^(-c) exp(-(log y)^2/4)/(2 sqrt(pi)),
    E_(k,t)(D;w)=integral_0^D integral |A_t(X,u)|^(2k) dw(u) dX/X^(k+1),

where the SAME w is used at every X, every D>=2 and T>0 satisfy

    integral_R g_T(t-t0) E_(k,t)(D;w) dt
       <= C_(F,k,c) Z [log(3D)^(a(F,k)+1)
                         +(D^k/T)log(3D)^a(F,k)].        (6)

All Gaussian tails and all ideal tuples are included. At k=1 for the native
and coupled families this recovers #954's bound, rather than claiming it as
new. At k=2 over Q(omega), (6) is O(Z[log^6 D+(D^2/T)log^5 D]).

**Audit of the previous claimed signed progress.** For principal native
Mobius coefficients over Q(omega), EVERY nonzero underlying tuple term with
equal product rational norms is nonnegative (Section 6). The earlier
log-squared 'signed equal-norm covariance' is valid, but it contains no
cancellation of opposite Mobius signs. Calling it evidence of having
controlled the difficult signed cancellation overstated its significance.
This observation is source-specific: general physical phases and the
coupled powerful coefficients do not inherit that termwise sign.

## 2. A multivariable, critically summable arithmetic comparison

A common positive majorant for all four families is defined at p by

    T_(m,q)(x)=(1+x)/(1-q^(m/2-1)x^m).                    (7)

Let t_m(I) be its ideal coefficients, and
B_m(n)=sum_(NI=n)t_m(I). These rational-norm coefficients are nonnegative
and multiplicative. No source coefficients or masks are changed by using
this upper majorant. Let P_m be the 2k-variable formal Dirichlet series
whose coefficient at (n_1,...,n_k;l_1,...,l_k) is

    1_(prod n_i=prod l_j) prod_i B_m(n_i) prod_j B_m(l_j). (8)

For the finite etale algebra F tensor F put

    Z_2(s)=product_(v=1)^r zeta_(E_v)(s)=sum_n z(n)n^(-s).

Its coefficients are nonnegative. Classical fixed-field ideal counting gives

    sum_(n<=x) z(n) <= C_F x (1+log x)^(r-1).             (9)

Indeed convolve the r ideal-count sequences; each has prefix O(x) and
harmonic prefix O(1+log x). This uses no statement about zeros.

We claim the exact formal factorization

    P_m(s_1,...,s_k;t_1,...,t_k)
      = H_m(s;t) product_(i,j) Z_2(s_i+t_j),              (10)

where the signed coefficient array h_m of H_m has the UNIFORM critical mass

    sum_(R_1,...,R_k;S_1,...,S_k)
       |h_m(R;S)| / sqrt(prod R_i prod S_j) <= C_(F,k).   (11)

Every supported h_m term still has prod R_i=prod S_j. The quotient is not
positive; (11) explicitly uses its absolute coefficients.

Proof of (11). Work at a rational prime p outside a fixed finite bad set.
Let f_1,...,f_g be the residue degrees in F and r_p the number equal to one.
At critical weight q^(-1/2), an ideal-prime factor (7) has total mass

    (1+q^(-1/2))/(1-q^(-1))=1/(1-q^(-1/2)),              (12)

independently of m. In k left slots the total mass of rational degree 1 is
k r_p/sqrt(p), and the mass of degrees >=2 is O_(F,k)(1/p). To see the latter,
put v=p^(-1/2). Factors with residue degree 1 are bounded by (1-v)^(-k r_p);
the remaining factors are bounded by (1-v^2)^(-k(g-r_p)). Their constant
and linear terms are precisely 1 and k r_p v, and the remainder is O(v^2)
uniformly for 0<=v<=1/sqrt(2). The same reasoning applies to the right slots.
The balance condition in (8) forces the two total degrees to agree.
Thus the local factor Q_p of P_m, at critical weight but retaining formal
slot variables z_i,w_j, is

    Q_p=1+(r_p^2/p)sum_(i,j) z_i w_j + R_p,
    ||R_p||_1 <= C_(F,k)/p^2.                            (13)

The remainder bound follows by multiplying the two degree-at-least-two
masses; it does NOT erase distinct norm fibers.

Outside the bad set, the number of degree-one primes in F tensor F is
r_p^2. This follows directly from
F_(p^a) tensor_Fp F_(p^b) = F_(p^lcm(a,b))^gcd(a,b).
Consequently the inverse local factor V_p of product_(i,j) Z_2(s_i+t_j)
is a finite polynomial with critical expansion

    V_p=1-(r_p^2/p)sum_(i,j) z_i w_j + O_l1,F,k(p^-2).

Multiplication gives ||Q_p V_p-1||_1=O_(F,k)(p^-2).
The local norms at the finitely many bad primes are bounded uniformly in m
by (12) and the finite inverse polynomial. Therefore product_p ||Q_p V_p||_1
converges and proves (11), first for finite products and then by monotone
convergence of the absolute majorant. All coefficient identities use only
finitely many divisors and are formal. Normal convergence of a multivariable
analytic continuation is not an extra premise. QED.

## 3. The transport-box bound with unequal slot caps

Here is the gain missing from the previous one-variable norm majorant.
For arbitrary caps X_i,Y_j>=1, and L=1+log(2 max(X_i,Y_j)), define

    Q(X;Y)=sum_(n_ij>=1; prod_j n_ij<=X_i; prod_i n_ij<=Y_j)
                                                    prod_(i,j) z(n_ij).

Then

    Q(X;Y) <= C_(F,k) sqrt(prod X_i prod Y_j)
                                  L^(r k^2-2k+1).        (14)

Proof. Place n_ij in [2^b_ij,2^(b_ij+1)), b_ij nonnegative integers.
By (9), the weight of a box is at most

    C_(F,k) 2^(sum b_ij) (1+max b_ij)^(k^2(r-1)).

Let R_i=floor(log_2 X_i), C_j=floor(log_2 Y_j), A=sum R_i,
B=sum C_j, and s=sum b_ij. Put delta=(A+B)/2-s>=0. The row deficits
R_i-sum_j b_ij and column deficits C_j-sum_i b_ij are nonnegative.
At fixed s their totals are A-s and B-s. Choose the first k-1 deficits on
each side, and the first (k-1)^2 matrix entries; all other entries are then
determined. Thus the number of boxes at that delta is at most

    (1+max(R_i,C_j))^((k-1)^2) (1+2delta)^(2k-2).         (15)

Choices producing negative entries are just omitted. This is an injection,
not an assertion that every choice is feasible. Delta may be half-integral.
Sum the geometric factor 2^(-delta) times (1+2delta)^(2k-2); the sum is finite
for each fixed k. Multiplying the logarithmic powers gives
k^2(r-1)+(k-1)^2=r k^2-2k+1. Also 2^((A+B)/2)<=sqrt(prod X_i prod Y_j).
This proves (14), including unbalanced caps and k=1. QED.

The free (k-1)^2 coordinates are the classical transport/Birkhoff dimension.
The calculation is elementary and no asymptotic polytope theorem is imported.

Combining the coefficient identity (10), absolute h_m, and (14) with
X_i=X/R_i, Y_j=X/S_j proves

    sum_(prod n_i=prod l_j; all n_i,l_j<=X)
                            prod B_m(n_i)prod B_m(l_j)
       <= C_(F,k) X^k (log(3X))^a(F,k).                  (16)

Terms whose new caps are below one contribute zero. The square-root factor
from (14) is X^k/sqrt(prod R_i prod S_j), so (11) pays the ENTIRE convolution,
with no added logarithm. This is why replacing (10) by a single product-norm
prefix bound loses the 2k-1 logarithms.

For the actual source, define

    C_X(N,u)=sum_(prod_i NI_i=N) prod_i[f(I_i,u)W(NI_i/X)],
    D_k(X;w)=sum_N integral |C_X(N,u)|^2 dw(u).            (17)

Every ideal tuple, shared prime, sixth-power alias and nonunit zero remains.
Equation (16) proves

    D_k <= D_k,absolute <= C_(F,k)||W||_infinity^(2k)
                                      Z X^k log(3X)^a.   (18)

The absolute version sums the moduli of all underlying equal-product-norm
2k-tuple terms, rather than just the modulus after grouping.

## 4. From the norm block to the COMPLETE finite-time mean

At fixed X, A_t(X,u)^k=sum_(N<=X^k) C_X(N,u) N^(it).
The elementary Fourier transform of the normalized Gaussian gives EXACTLY

    M_k=sum_(N,M) exp[-T^2 log(N/M)^2/2]
               exp[it0 log(N/M)] integral C_X(N)conj(C_X(M)) dw. (19)

This is a finite sum: there is no limiting independent-prime law.
Let L0=floor(X^k). For distinct integers 1<=N,M<=L0,

    |log(N/M)| >= |N-M|/L0.

The absolute off-diagonal row sum of the Gram matrix in (19) is at most

    rho(T/L0)=2 sum_(j>=1) exp[-(T j/L0)^2/2]
             <= sqrt(2pi)L0/T.                          (20)

Cauchy in the row measure and 2ab<=a^2+b^2 therefore show

    |M_k-D_k| <= rho(T/L0) D_k.                          (21)

At T>=2L0, rho<=2 sum_(j>=1)e^(-2j^2)<1/3. For a completely rational
verification of this strict constant, e^2>7 and j^2>=j give
2 sum e^(-2j^2)<2 sum 7^(-j)=1/3. Thus

    (2/3)D_k <= M_k <= (4/3)D_k       when T>=2X^k.       (22)

Equations (18),(20),(21) prove Theorem 1, with any t0. In particular, the
unequal-norm remainder is genuinely bounded here, but ONLY after the explicit
long twist average. It is not bounded at t=0 by this argument.

## 5. Keeping the complete Gaussian

Decompose W_c into dyadic annuli 2^j<y<=2^(j+1). After rescaling each annulus
to (1/2,1], its sup norm is at most
C_c exp(-c0 j^2+C_c|j|), for one absolute c0>0. Apply Theorem 1 to each
finite annular polynomial at scale 2^(j+1)X, and use Minkowski in
L^(2k)(w times g_T). The factors produced by rescaling are at most

    2^((j+1)/2) (1+2^(k(j+1)))^(1/(2k))
                               (1+|j|)^(a/(2k)),

times X^(1/2) log(3X)^(a/(2k))(1+X^k/T)^(1/(2k)) for X>=1.
Their product with the Gaussian annular sup norm is summable over all j.
This proves the fixed-X Gaussian analogue of (4); it justifies passage from
finite to infinite annular sums in that Lp norm as well.

Uniformly in m, the ideal majorant (7) has first absolute prefix O_F(x):
write I=R J^m, sum over squarefree R and unrestricted J, and use ideal counting.
The outer summation has weight (NJ)^(-m/2-1), bounded by zeta_F(2).
The same Gaussian tail estimate gives |A_t(X,u)|=O_(F,c,B)(X^B) for every
fixed B>0 as 0<X<=1, uniformly in t, masks and m. This pays (0,1] in (6).
Integrating the fixed-X bound over 1<=X<=D against dX/X^(k+1) gives (6).
Tonelli applies to these nonnegative integrands. No scale-varying row
measure, truncated Gaussian, or unproved contour shift is used. QED.

## 6. Native signs are determined by rational norm

In Q(omega), away from 3, a rational split prime has two degree-one ideal
primes, and an inert prime has one degree-two ideal prime. For any product
of squarefree ideals, the total Mobius sign at a split rational prime is
(-1)^e, where e is its total rational-norm valuation. At an inert rational
prime the valuation is even and the sign is (-1)^(e/2). These formulae depend
only on the product rational norm, not on the individual ideal tuple.
Thus two tuples of equal product norm have identical signs. Their product
is +1 whenever neither coefficient vanishes. Fixed exclusions do not change
this conclusion. With a nonnegative test, every equal-product-norm term
in (17) is nonnegative. This proves the audit in Section 1.

This is not an assertion for arbitrary number fields, nonprincipal twists,
row phases, or the powerful coefficients in the coupled family.

## 7. Sharp lower bound: enough coprime transport boxes

We prove Theorem 2 rather than infer sharpness from a fitted exponent.
Define the nonnegative rational multiplicative function

    g(n)=4^omega(n) if n is squarefree and every prime p|n satisfies p=1 mod 3;
    g(n)=0 otherwise.

Removing any fixed finite prime set P gives g_P. Its Dirichlet series is
product_(p=1 mod3, p notin P)(1+4p^(-s)). The quotient by zeta_K(s)^2
has local factors 1+O(p^(-2 Re s)) outside the finite excluded set: at split
primes use (1+4x)(1-x)^4, at inert primes (1-x^2)^2. Hence the quotient's
absolute coefficient series converges for Re s>1/2, and its value at 1 is
positive. Classical ideal counting in K gives

    sum_(n<=y) g_P(n) ~ c_P y log y, c_P>0.              (23)

For completeness, this asymptotic needs no zero-free theorem: the lattice
count I_K(y)=r_K y+O(sqrt(y)+1) gives by Dirichlet's hyperbola method
sum_(n<=y)[zeta_K^2]_n=r_K^2 y log y+O_K(y). Convolve with the quotient.
Its absolute mass at 1 is finite; dominated convergence, using the uniform
O(y log(2y)) bound, proves (23). Subtract two endpoints to get the same
positive order in every fixed relative interval [Y,(1+eta)Y], eta>0.

We will use the following elementary coprimality consequence. For any fixed
s and eta>0, and Y_1,...,Y_s tending to infinity, with

    c log X <= log Y_i <= C log X,

there is a constant c_(s,eta,c,C)>0 such that the total weight prod_i g(n_i)
of PAIRWISE COPRIME n_i in these s relative intervals is at least

    c_(s,eta,c,C) prod_i [Y_i log Y_i].                   (24)

Proof. First remove every prime <=P and every originally excluded prime.
By (23), the unrestricted product of the s interval weights is at least
(c_P eta/2)^s prod Y_i log Y_i once all Y_i are large. For a prime p>P
forced into two entries, g(pn)<=4g(n) (including the nonsquarefree case,
where the left side is zero). The uniform prefix bound for g therefore
bounds that bad weight by
C_(s,c,C) p^(-2) prod Y_i log Y_i. Sum over the finitely many pairs of
entries and all primes >P; using all integers as an upper bound costs O(1/P).
Finally c_P=c_empty prod_(p<=P,p=1 mod3)(1+4/p)^(-1), up to fixed factors.
The classical elementary upper bound sum_(p<=P)1/p<=log log(3P)+O(1) gives
c_P>=c (log(3P))^(-4). Therefore 1/P=o(c_P^s). Choose P large ONCE, depending
on fixed s and the fixed exclusions, so the bad part is less than half the
unrestricted lower bound. This proves (24). Neither P nor the error is
allowed to move with X after that choice. QED.

Apply (24) with s=k^2. Let L=floor(log_2 X), and choose a k by k nonnegative
integer base matrix with every row and column sum L and entries L/k+O_k(1).
One construction gives floor(L/k) to every entry and distributes the
remaining L mod k units using that many disjoint permutation matrices.
Vary its first (k-1)^2 entries by integers of magnitude <=c_k L, and choose
the last row and column to preserve all margins. With c_k sufficiently
small, every entry b_ij lies between L/(2k) and 2L/k. There are
Omega_k(L^((k-1)^2)) such matrices (one when k=1).

Set lambda=(3X/(4*2^L))^(1/k) and

    Y_ij=lambda 2^b_ij,   n_ij in [Y_ij,(1+eta)Y_ij],

with fixed eta>0 chosen so (1+eta)^k<4/3. All row and column products lie
strictly in (X/2,X], and all log Y_ij are comparable to log X. The integer
boxes are disjoint when the b matrices differ, since eta<1.
For each box keep only pairwise coprime entries. Their total weight is
Omega_(S,k)(X^k (log X)^(k^2)) by (24).

Map a matrix of entries to left norms N_i=prod_j n_ij and right norms
M_j=prod_i n_ij. Pairwise coprimality gives gcd(N_i,M_j)=n_ij, so the map
is injective. Every N_i and M_j is squarefree with split prime support.
For such a rational n, the native sum over all ideals of norm n is
(-2)^omega(n), provided all its rational primes avoid S. Thus the weight
of this norm-tuple in (17) is exactly prod_(i,j)g(n_ij), and its sign is
positive. Summing the disjoint boxes proves

    D_k(X;1) >= c_(S,k) X^k (log X)^(k^2+(k-1)^2).      (25)

All other norm-tuple terms are nonnegative by Section 6. Since
k^2+(k-1)^2=2k^2-2k+1, (18),(22),(25) prove Theorem 2. QED.

## 8. Why the averaging cost cannot be suppressed uniformly

The upper theorem includes the allowed profile a_p=-1 in its native family.
It changes f(I) to |mu_F(I)|. With W=1_(1/2,1], classical squarefree-ideal
counting gives sum f(I)W(NI/X) asymp_F,S X. This follows, for example, from
zeta_F(s)/zeta_F(2s) and the elementary square-divisor convolution.
For |t|<=1/2 the arguments of (NI/X)^(it) range over an arc of length at
most (log 2)/2, so the modulus of the polynomial is >=c X. Consequently,
for every T>=1,

    M_k(X,T,0;1) >= c_(F,S,k) X^(2k)/T.                 (26)

A coefficient-uniform diagonal-power theorem cannot replace the X^k-scale
averaging window by X^(k-delta), for fixed delta>0, while retaining only
logarithmic losses. This is a sharp POWER cost for a uniform statement,
not a lower bound for the original principal Mobius source. That source
may have additional cancellation, but none is proved by (26).

The fixed-twist unequal-product-norm estimate remains the genuine RH-bearing
problem. This packet proves a full averaged theorem and sharper arithmetic
norm blocks; it does not turn averaging, the positive norm blocks, or a
transport dimension into that missing signed estimate.
