# Local polynomial uniformity for the actual Eisenstein norm coefficients

Status: PROPOSED complete deductions from a published unconditional theorem.
No independent mathematical review or proof-assistant verification has occurred.
No new zeta zero-free region, full physical sextic moment, or RH proof is claimed.

This packet changes two things relative to #960: its cancellation input and its
arithmetic source. It uses MRSTT (2026), Theorem 1.1(i), rather than MRT (2015),
and treats the actual complete Eisenstein norm fibers, whose prime values can
be -2. It does not misapply a one-bounded theorem to those fibers.

## 1. The result and its price

Put K=Q(omega), omega^2+omega+1=0. Fix finite sets S_i of prime ideals, i=1,...,k.
At a good ideal prime p, q=Np, choose one of these formal local coefficient series:

    native:       1-x;
    coupled:      1-(1-1/q)x-b_p q^(m/2-1)x^m;
    two-channel:  (1-x)(1-b_p q^(m/2-1)x^m);
    geometric:    1-(1-1/q)x/(1-b_p q^(m/2-1)x^m).       (1)

Here m>=2 is an integer and |b_p|<=1. At every excluded prime the ENTIRE
factor is 1. Each of the k columns may have a different family, degree and
profile. Optional twists xi_i(NI), where xi_i is a fixed ordinary Dirichlet
character, are allowed. These are norm twists, NOT general sextic row twists.
Denote the resulting ideal coefficients by c_i(I).

Let each W_i be a left-continuous complex bounded-variation function on (0,infinity), tending
to zero at infinity, with total variation V_i<infinity. Hard interval indicators
and the literal Gaussian

    W_c(y)=y^(-c) exp[-(log y)^2/4]/(2 sqrt(pi))            (2)

are included. Choose arbitrary scales D_i>0 and define the exact tensor
coefficient, retaining ALL ideals of each norm,

    a_D(n)= sum_(prod_i NI_i=n) prod_i [c_i(I_i) W_i(NI_i/D_i)]. (3)

At each n this is a finite sum. It is the coefficient of the actual k-fold
product of the selected ideal polynomials, not the coefficient of an uncapped
surrogate. Empty/zero tests cause no difficulty. For k=1 and the native family,
a(n)=sum_(NI=n,(I,S)=1) mu_K(I) when the test is omitted on the range in use.

For a finite integer interval J and polynomial degree ell>=1 put

    U_a(x,H)=sup_(deg P<=ell; Q an arithmetic progression in (x,x+H])
                          |sum_(n in Q) a(n) exp(2 pi i P(n))|.    (4)

Q may be empty, a singleton, or any finite progression. Thus (4) includes all
endpoint truncations. Both Q and P may be chosen separately for EVERY x.

### Theorem 1 (phase-adaptive square mean of the actual tensor)

For every fixed k,ell, every B>0 and 0<epsilon<1/(24k),

    integral_X^(2X) U_(a_D)(x,H)^2 dx
       <<_(k,ell,B,epsilon,S_i,xi_i) (prod_i V_i)^2
                                  X H^2 / (log X)^B,    (5)

whenever X is sufficiently large and

    X^(1-1/(3k)+epsilon) <= H <= X^(1-epsilon).           (6)

The constants are UNIFORM in all D_i, m_i>=2, and profiles b_{i,p}. Degrees
and profiles can therefore be chosen afresh at each X,H. The supremum over
these source parameters is not put inside the integral. k,ell,S_i,xi_i stay
fixed. There is no Mellin-twist average or independent-prime randomization.

For k=1, the threshold is X^(2/3+epsilon). For k=2 it is X^(5/6+epsilon)
in PRODUCT-norm coordinates. If the two original columns have size D, that
means shifts of product norm at least D^(5/3+2epsilon), not shifts of size D.
There is no assertion at the endpoint exponent with epsilon=0.

Over Q the same proof gives threshold X^(1-2/(3k)+epsilon), in particular
X^(1/3+epsilon) for one column. The fixed-width logarithmic rate from #960
is replaced, in these more restricted ranges, by ANY fixed logarithmic power.
Theorem 1 does not dominate #960's much shorter-H assertion everywhere.

### Corollary 2 (exceptional interval measure)

For any fixed A,B>0 the set of x in [X,2X] for which U_a(x,H)>H/(log X)^A
has measure O(X/(log X)^B), under (6). Choose exponent B+2A in (5).
The constant includes the fixed test variation. This is not an assertion
about every individual interval, nor a power saving in X.

## 2. The exact external input

Use Matomaki--Radziwill--Shao--Tao--Teravainen, *Higher uniformity of arithmetic
functions in short intervals II. Almost all intervals*, Invent. Math. 244
(2026), 967--1091, DOI 10.1007/s00222-026-01408-6, Theorem 1.1(i).
The statement and its star notation were checked on published PDF page 970;
arXiv:2411.05770v2, printed pp. 3--4, is the corresponding author version.

For a fixed ell, delta>0 and A>0, the theorem on the circle nilmanifold yields

    sup_(deg P<=ell; Q AP in (y,y+h]) |sum_Q mu(n)e(P(n))|
                       <= h/(log Y)^A                  (7)

outside a set of measure O(Y/(log Y)^A), for y in [Y,2Y] and
Y^(1/3+delta)<=h<=Y^(1-delta). Polynomial coefficients have no size bound.
The supremum in (7) is pointwise in y, not outside its integral. Since mu is
bounded by one and h>=1, (7) and the trivial bound h+1 imply

    integral_Y^(2Y) U_mu(y,h)^2 dy << Y h^2/(log Y)^A.   (8)

A fixed Dirichlet character chi costs only its modulus: split an AP into
residue classes modulo that modulus. Each intersection is again an AP, and
chi is constant there. Thus (8) also holds for mu(n)chi(n), with a fixed
modulus-dependent constant. No uniformity in a growing conductor is inferred.

Only this published result supplies deep cancellation. The remainder of the
proof is hyperbola decomposition, positive coefficient estimates, and finite
Fourier algebra. We do not claim a new proof of (7), its nilsequence machinery,
or global literature priority for these methods.

## 3. A capped convolution lemma; no column cap is lost

Let r>=1 and fixed Dirichlet characters chi_1,...,chi_r be given. Partition the
r factor indices into disjoint groups. For each group require that the product
of its factors lies in an arbitrary fixed interval (L_j,U_j]. Define

    C(n)=sum_(d_1...d_r=n, all group constraints)
                                       prod_i mu(d_i)chi_i(d_i). (9)

Constraints/scales may vary with X,H but are fixed as x varies. Put

    theta_r=1-2/(3r).

Then for all A>0 and small fixed epsilon>0,

    integral_X^(2X) U_C(x,H)^2 dx << X H^2/(log X)^A,    (10)

uniformly in every group interval, for X^(theta_r+epsilon)<=H<=X^(1-epsilon).

**Proof.** Assign each tuple to its LARGEST factor, breaking ties by the first
index. Fix its index j and all other factors; write a for their product and b
for the free factor. Because n<=3X and b is largest,

    a <= (3X)^(1-1/r).                                  (11)

All group constraints not involving j are now either satisfied or false.
The constraint involving j gives one interval for b. The largest-factor and
tie conditions give another interval: b>=d_i for i>j and b>d_i for i<j.
Their intersection is an interval; it is NOT estimated by deleting signs.
The preimage of the selected progression in n=ab is a progression in b or
empty, including when a shares factors with its modulus. Intersect with the
interval constraints. The phase P(ab) is a polynomial in b of degree <=ell.
Hence the inner sum is bounded by U_(mu chi_j)(x/a,H/a).

Write Y=X/a and h=H/a. With delta=epsilon/2, (11) gives, for large X,

    h >= Y^(1/3+delta),    h <= Y^(1-delta),
    Y >= 3^(-1+1/r) X^(1/r).                            (12)

Indeed the lower logarithmic exponent margin is epsilon-delta/r>0; the upper
one is at most -epsilon+delta<0. Thus (8), with substitution x=ay, bounds the
L2 norm of this term by

    C sqrt(X) H / [a (log X)^M]                         (13)

for any prescribed M. Crucially the weight is 1/a, not 1/sqrt(a).
Minkowski applies even though the phase/progression is optimized inside each
integral: the supremum is subadditive. Finally

    sum_(d_i, i!=j; product<=3X) 1/(prod d_i)
                  <= (1+log(3X))^(r-1).                 (14)

Sum over j and take M large enough. This proves (10). There is one owner per
tuple, all shared factors remain, and no unbounded number of exceptional sets
has been union-bounded. Their costs were integrated before summing (13). QED.

The elementary bound |C(n)|<=d_r(n) holds uniformly in all caps. Also

    sum_(n<=T) d_r(n)^2 <= T(1+log T)^(r^2-1).           (15)

For completeness d_r(p^e)^2<=d_(r^2)(p^e): two weak r-compositions of e can
be realized as row/column sums of an r by r nonnegative integer matrix. Pick
a deterministic such matrix. Different pairs of margins give different
matrices, giving an injection. Multiply over primes; repeated harmonic
summation bounds the prefix of d_(r^2). No asymptotic divisor estimate is needed.

## 4. Exact Eisenstein factorization and completion kernels

For the FULL unmasked Eisenstein norm fibers,

    sum_(NI=n) mu_K(I) = (mu * (mu chi_-3))(n).           (16)

This is an equality of formal coefficients. For a rational prime p!=3,
x^2+x+1 splits mod p precisely for p=1 mod 3. The inverse ideal Euler factors
are (1-p^-s)^2 at split primes and 1-p^-2s at inert primes; at 3 the factor
is 1-3^-s. They agree exactly with (1-p^-s)(1-chi_-3(p)p^-s).
Both conjugate ideals at a split prime therefore remain. A value -2 at a split
rational prime is NOT replaced by the bounded value -1.

For a completed column divide its local factor (1) by 1-x, initially FORMALLY.
At p outside S put r_q=1/q and D_q=b_p q^(m/2-1)x^m. The correction factors are

    native:       1;
    coupled:      1+(r_q x-D_q)/(1-x);
    two-channel:  1-D_q;
    geometric:    1+x(r_q-D_q)/[(1-x)(1-D_q)].           (17)

At p in S the correction is (1-x)^(-1), not 1: this cancels the original
unmasked native factor. Optional norm twists multiply the coefficients by
xi(n), with their literal zero values preserved.

The absolute coefficients in (17) have nonnegative majorants obtained by
replacing the minus signs in the nonconstant numerators by plus signs and
D_q by q^(m/2-1)x^m in geometric denominators. Call their rational-norm
aggregation J_m(n). Norm grouping uses a triangle inequality only for this
majorant, not for the source identity.

Uniformly in m>=2 and b, these majorants satisfy

    sum_n J_m(n)n^(-3/4) <= C_S,
    sum_(n<=T) J_m(n)n^(-1/2) <= C_S(1+log(3T))^72.     (18)

Here constants depend on the fixed field K and S. To verify (18), at the
critical local argument t=q^-1/2 the powerful term has size exactly 1/q.
The respective nonconstant masses are bounded by

    (q^-3/2+q^-1)/(1-q^-1/2),
    q^-1,
    2q^-3/2/[(1-q^-1/2)(1-q^-1)].                      (19)

Each is <=12/q for q>=2. This follows by monotonicity after multiplying by q;
at q=2, use 1/sqrt(2)<5/7 to check the largest rational upper bound <12.
At t=q^-3/4 all three nonconstant masses are <=10q^-3/2, uniformly in m.
The geometric denominator converges since its powerful argument is
q^(-1-m/4)<=q^-3/2. The finitely many excluded factors have finite masses
at both weights. Tonelli for the positive formal series proves the first
inequality of (18).

For the second inequality only primes with q<=T can occur. Elementary Euler
products at s=1+1/log T and zeta(s)<=1+1/(s-1) imply

    sum_(p<=T) 1/p <= 3 log(1+log T).

There are at most two ideal primes over each rational prime and q>=p, so
(19) gives the deliberately coarse exponent 72. This requires no PNT or
zero-free region. The stronger one-log budgets in #951 are compatible but
are not needed. For k corrections their convolution J has

    sum J(n)n^-3/4<=C,
    sum_(n<=T)J(n)n^-1/2<=C(1+log(3T))^(72k).           (20)

All products/identities have so far been formal or absolutely majorized;
no Euler product was continued through unknown reciprocal-zeta poles.

## 5. Transfer of local uniformity, including microscopic dilations

Insert (16)--(17) separately in every column of (3). For hard tests this is
EXACTLY a sum over correction norms d_i; the remaining native column cap
is (L_i/d_i,U_i/d_i]. Write d=prod d_i. The residual source is (9) with r=2k,
the factors grouped into their original pairs. The character twists split
completely multiplicatively between these factors and d_i.

We prove (5) in root norm. Put R=(log X)^L, where L will be fixed in terms of
the desired saving. Split correction tuples by their PRODUCT d, not by m.

For d<=R, apply (10) at Y=X/d, h=H/d, using epsilon/2 in place of epsilon.
All modified caps are allowed in that lemma. Minkowski and (20) give root norm
O(sqrt(X)H/(log X)^A) with any prescribed A, since sum J(d)/d<=C.

For R<d<=H, do not invoke cancellation. The elementary divisor bound (15),
Cauchy in each window, and Fubini give

    integral_Y^(2Y) [sum_(y<n<=y+h)d_r(n)]^2 dy
                   << Y h^2 (log(3Y))^(r^2-1), h>=1.   (21)

After x=dy its root contribution is at most

    C sqrt(X)H (log(3X))^((r^2-1)/2)
                      sum_(d>R)J(d)/d
      <= C sqrt(X)H (log(3X))^((r^2-1)/2) R^-1/4.      (22)

For H<d<=3X, h<1. Each base window contains at most one integer (endpoints
have measure zero), so the corresponding version of (21) is

    integral_Y^(2Y) [sum_(y<n<=y+h)d_r(n)]^2 dy
                    << Y h (log(3+Y))^(r^2-1).        (23)

The harmless range 1/3<=Y<1 is covered by enlarging the constant. On undoing
the dilation and summing (20), (23) costs at most

    C sqrt(XH) (log(3X))^(72k+(r^2-1)/2).               (24)

It is smaller than sqrt(X)H/(log X)^A for every fixed A in (6).
For d>3X the source is empty on all windows being integrated. No Gaussian
tail or ideal term in those windows has been thrown away.

Choose L large enough in (22), then the input saving large enough for the
small d range. This proves (5) for hard intervals. It handles m growing with
X: a small ideal-power base can still have huge dilation, and that term is
charged to (23), not incorrectly sent through (7).

For BV tests use the Stieltjes decomposition

    W_i(v/D_i) = - integral_(t>=v) d[W_i(t/D_i)].        (25)

Use the Lebesgue--Stieltjes signed measure for the left-continuous version:
the tail [v,infinity) represents (0,t] indicators, and point masses represent
jumps. This fixes the values at integer norm endpoints, rather than ignoring
them as null sets of coefficient indices. Total variation is V_i, independent of D_i.
On every local product-norm window all NI_i<=3X, so coefficient-level sums
are finite. Apply Minkowski to the finite-variation integrals and the uniform
hard-cap result. This proves (5) for the full Gaussian as well. It is not a
replacement of the actual noncompact test by one compact approximation. QED.

## 6. Growing additive correlations and the Gaussian shell

For k=1 let f(n) be the complete norm coefficients with tests equal to one
on the range in use. This can be implemented by a hard cap above 4X. For any
complex G on [1,4X] with sum |G(n)|^2<=A_G X and integers H in the stricter
range X^(2/3+epsilon)<=H<=X^(1-epsilon), define

    C_h(Y)=sum_(X<n<=Y) f(n) conjugate(G(n+h)), X<=Y<=2X.

Then for every B>0,

    sum_(h<=H) max_Y |C_h(Y)|
                        << sqrt(A_G) XH/(log X)^B.     (26)

The same assertion holds for the tensor (3), with threshold 1-1/(3k) and
a multiplicative factor prod V_i on its right side. In the proof below
normalize prod V_i<=1; arbitrary variation follows by homogeneity.
We supply the maximal step rather than interchanging maximum and sum.

First (15),(20) and ordinary l2 convolution give a uniform square prefix

    sum_(n<=T)|f(n)|^2 << T(log(3T))^Gamma,             (27)
    Gamma=(2k)^2-1+144k

(a deliberately nonsharp exponent). Let f_Y=f 1_(X, Y] and extend G by zero.
For window length 2H, finite expansion and Fourier orthogonality give

    J(alpha)=integral_R S_(f_Y)(x,alpha)conj(S_G(x,alpha))dx,
    integral_0^1 |J(alpha)|^2 d alpha
         =sum_h (2H-|h|)_+^2 |C_h(Y)|^2.               (28)

Cauchy in x and Parseval for G show, uniformly for every Y,

    sum_(h<=H)|C_h(Y)|^2 << A_G HX^2/(log X)^M          (29)

with arbitrary M. The source windows in (28) lie in [X-2H,2X], covered by two
comparable dyadic intervals for large X. Intersecting them with (X,Y] is an
AP truncation allowed by (4). Use smaller fixed epsilon in (5). Therefore
(29) does not use an unproved hard-endpoint estimate.

Put V=sum|f|^2, W=sum|G|^2 and take J0 a positive integer. Declare atoms with
|f(n)|^2>V/J0 heavy. Partition the remaining light square mass into at most
J0+1 consecutive bins, each of mass <=2V/J0. Approximate a prefix by its
preceding bin endpoint. The light error for each h is <=sqrt(2VW/J0).
There are fewer than J0 heavy atoms; Cauchy and summation over h bound their
squared contribution by J0 VW. Use (29) at every grid endpoint, including
endpoints selected by f. This yields

    sum_h max_Y |C_h(Y)|^2
     << A_G HX^2 [J0(log X)^(-M)+(log X)^Gamma/J0
                                      +J0(log X)^Gamma/H].     (30)

Choose J0=ceil((log X)^(2B+Gamma+2)) and M sufficiently large. The polynomial
lower bound for H pays the last term. Cauchy in h proves (26). The heavy-atom
argument is inherited from #960 and explicitly reused, not claimed as new.

For two completed principal norm sources f,g, (27) supplies A_G of polylog
size; it can be absorbed because B in (26) is arbitrary. For the actual #952
Gaussian kernel,

    K_D(v,w)=kappa_c/sqrt(vw) exp[-log(v/w)^2/8]
                  Phi(log D-log(vw)/2-(2c-1)),
    kappa_c=exp((2c-1)^2/2)/(2sqrt(2pi)),

partial summation in n therefore proves

    sum_(h<=H) |sum_(D<n<=2D) f(n)conj(g(n+h))K_D(n,n+h)|
                                  << H/(log D)^B       (31)

for D^(2/3+epsilon)<=H<=D^(1-epsilon). Indeed the supremum plus variation of
K_D(n,n+h) on that shell is O_c(1/D), uniformly in h<=D. Every coefficient of
every rational-norm fiber in the selected shell and band remains in (31).

## 7. Exact boundary of progress

The new arithmetic coverage is principal Eisenstein norm fibers and their
actual capped/Gaussian tensors. Neither arbitrary physical sextic characters
chi_I(u) nor all number fields have been reduced to (16). Fixed norm Dirichlet
twists and fixed ideal exclusions are allowed; growing conductors/masks are not.
No claim that these local correlations equal CT's low-powerful theta pairing
is made. In particular OPEN-L in #961 is not proved.

Although (31) saves every fixed logarithmic power, at H=D^theta it is still
D^theta/(log D)^B. No choice of FIXED B turns that into D^epsilon for every
epsilon>0. No uniform B=B(D) bound is available. The theorem also does not
control all n shells at once. Thus it does not improve the zero-free exponent,
the full native 2k-th moment, or RH. This is a new source-specific bridge and
stronger cancellation theorem in the displayed range, not a completed endpoint
argument. A quantitative power saving or a signed recombination across the
remaining shifts, with the actual theta adapter, is still missing.
