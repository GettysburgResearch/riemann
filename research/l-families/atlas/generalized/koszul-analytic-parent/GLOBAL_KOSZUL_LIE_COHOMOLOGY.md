# The actual S3 Koszul Lie arithmetic parent and its first branch obstruction

This companion unifies two previously separate constructions. It takes
the actual exponentially growing Koszul Lie source M_n, places it on
the actual S3 cover, and forms its finite arithmetic cohomology before
completing. It is not the polynomial-growth R_n cohomological sum.
The resulting ordinary signed Fredholm object exists on its sharp
trace-class disk, has a genuine initial place Euler product, and has
an explicit ramified correction relative to the Segre-coefficient
Euler product. For Q congruent to 1 modulo 3, its first negative
grading boundary is a genuine cubic branch point.

The quadratic source, dual convention and equivariant PBW theorem are
those of [the original analytic parent](MATHEMATICS.md). The actual
S3 cover and its cohomological constituents are those of
[the ramified S3 source](S3_RAMIFICATION_AND_GRADED_FAMILY.md) and
[the genus-three Galois closure](../global-s3-prym/GALOIS_CLOSURE_AND_TWO_ELLIPTIC_MAPS.md).
Assume char(F_Q)>3, A!=0 and -4A^3-27B^2!=0 for
E:y^2=x^3+Ax+B with base coordinate u=y. Let Z be its constant
S3 Galois closure and D its discriminant elliptic quotient. All
finite-cover cohomology, trace formula and purity inputs are classical.
There is no new RH theorem or external priority claim.

## 1. Actual finite Lie modules and their arithmetic cohomology

Use V=std_2 and W=perm_3 on the common unramified open set. The
quadratic Segre source defines the Lie superalgebra L and the modules
M_n=L_n^*, with source parity n modulo 2. Restricting this functorial
construction to the S3 monodromy gives actual finite local systems,
not virtual coefficients fitted to a desired Euler factor.
The quadratic presentation and the S3 action are defined over Q.
Form each finite M_n over Q and extend scalars to Q_ell for the
arithmetic local system; the complex Hilbert realization is a later
choice. This keeps the algebraic and arithmetic source functors aligned.

Write epsilon_n=dim M_n and let s_n,c_n be its transposition and
three-cycle traces. The multiplicity spaces of 1,sign,std have dimensions

    a_n=(epsilon_n+3s_n+2c_n)/6,
    b_n=(epsilon_n-3s_n+2c_n)/6,
    c'_n=(epsilon_n-c_n)/3.                             (1.1)

The prime on c'_n distinguishes a multiplicity from the cycle trace.
These are nonnegative integers because they are multiplicities of an
actual representation. In particular M_1 has character (6,0,0), so
it is the regular S3 representation. Its finite arithmetic factor
is exactly Z(Z,T).

The finite middle-extension cohomology is

    H^0_n=A_n,                  H^2_n=A_n(-1),
    H^1_n=(B_n tensor H^1(D)) direct_sum
                              (C_n tensor H^1(E)),     (1.2)

where A_n,B_n,C_n are the actual multiplicity spaces in (1.1).
Consequently

    L(M_n,T)=Z(P1,T)^a_n P_D(T)^b_n P_E(T)^c'_n.       (1.3)

All bad-point factors in (1.3) use M_n^I and the actual residual
Frobenius. Taking inertia invariants is exact in characteristic zero,
but is not monoidal. The [ramification correction note](S3_LIE_RAMIFICATION_CORRECTION.md)
computes the resulting discrepancy with the full invariant Segre
algebra, including the nonsplit residual action at infinity.

The established source bounds give epsilon_n~2^n/n. Define

    e_n=(-1)^(n+1),       P_g(z)=sum_(n>=1) e_n tr(g|M_n)z^n.

The actual transposition and cycle primitive series have radii
2^(-1/2) and 2^(-1/3), respectively, strictly larger than 1/2.
Cauchy's coefficient bound on any intermediate circle therefore gives
s_n=o(epsilon_n) and c_n=o(epsilon_n). Thus

    a_n~epsilon_n/6, b_n~epsilon_n/6, c'_n~epsilon_n/3,
    dim H^1_n=2b_n+2c'_n~epsilon_n.                    (1.4)

These limits hold along both parity subsequences. No finite dimension
table is being used to infer the infinite growth or positivity.

## 2. Sharp Hilbert and Schatten domains of the arithmetic Lie source

Realize the finitely many actual Frobenius modules in (1.2) over C
and fix Hermitian norms, using the same norm in every repeated copy,
as explained in the earlier global cohomological packet. Let

    H_i=Hilbert_direct_sum_(n>=1) H^i_n,
    K_i(z)|H^i_n=z^n Fr_i.

Retain the grade parity on every H_i. The direct sums are boundedly
equivalent under changes of the fixed finite norms. No identification
with the cohomology of an infinite-rank sheaf is asserted.

For p>=1 the exact Schatten sums are

    ||K_0(z)||_p^p=sum_n a_n |z|^(pn),
    ||K_2(z)||_p^p=Q^p sum_n a_n |z|^(pn),
    ||K_1(z)||_p^p=sum_n |z|^(pn)
          [b_n||Fr_D||_p^p+c'_n||Fr_E||_p^p].           (2.1)

The same formulas restricted to even or odd n give the corresponding
parity blocks. By (1.4), every nonzero one of these blocks belongs
to S_p exactly for

    |z|<2^(-1/p).                                      (2.2)

At equality the tail is harmonic and diverges. They are compact
exactly for |z|<1, bounded noncompact on |z|=1, and unbounded for
|z|>1. Holomorphy in S_p on its strict disk follows from uniform
convergence of the source block series and its differentiated series.

For |z|<1/2 define the ordinary signed cohomological Fredholm ratio

    L_Lie(z,T)=product_(n>=1) L(M_n,Tz^n)^e_n
              = product_(i=0,1,2; n>=1)
                    det(1-Tz^n Fr_i|H^i_n)^((-1)^(n+i)). (2.3)

The numerator is total parity n+i even, and the denominator is total
parity odd. Each is an ordinary trace-class Fredholm determinant,
jointly holomorphic in z,T on this disk times C_T; the ratio is
meromorphic there. In particular L_Lie(0,T)=1. This is an arithmetic
realization of the exponential Lie source, and does not improve its
operator-ideal threshold to the unit disk of the different R_n sum.

## 3. The initial place Euler product and the exact bad-place correction

For a closed point v of degree f, the actual local factor is

    product_(n>=1)
      det(1-T^f z^(nf) Fr_v|M_n^(I_v))^((-1)^n).        (3.1)

The product over all places converges absolutely in logarithm if

    |z|<1/2,                    Q|Tz|<1.              (3.2)

Indeed the finite monodromy traces are bounded by epsilon_n. With
r=|z| the absolute logarithm is at most

    sum_n epsilon_n[-log(1-Q|T|r^n)-log(1-|T|r^n)]
    <=(Q+1)|T|/(1-Q|T|r) sum_n epsilon_n r^n,

which is finite. The finite-grade trace formula and absolute
interchange identify this actual Euler product with (2.3).

At T=1 the unramified factor (3.1) is exactly F_(Fr_v)(z^f), where
F_g(t)=sum_r tr(g|R_r)t^r, by the source PBW identity. The parity
sign is essential: taking the opposite signed global product would
give its reciprocal.

At a ramified place let

    B_(I,phi)(t)=product_n det(1-t^n phi|M_n^I)^((-1)^n),
    F_(I,phi)(t)=sum_r tr(phi|R_r^I)t^r.

Both are source-defined. Their equality is false in general. If
E_Segre(z)=product_v F_(I_v,Fr_v)(z^deg(v)), then, on |z|<1/Q,

    L_Lie(z,1)=E_Segre(z)
          product_(v ramified) B_(I_v,Fr_v)(z^deg(v))
                                  /F_(I_v,Fr_v)(z^deg(v)).      (3.3)

There are finitely many correction factors. This formula does not
declare an unramified identity at a bad place; it records the exact
source-level failure to commute invariants with PBW. The ramification
note gives explicit Mahler equations for these B factors and tests
their first unequal coefficients against the invariant Segre source.

## 4. The first grading boundary remembers actual closure point counts

Set tau=-1/2 and specialize T=1. Write e_D=tr(Fr|H^1(D)) and
e_E=tr(Fr|H^1(E)). The first-power coefficient series of the logarithm
of (2.3) is

    P_ar(z)=sum_n e_n[(1+Q)a_n-e_D b_n-e_E c'_n]z^n
           =alpha P_e(z)+beta P_s(z)+gamma P_c(z),     (4.1)

where

    alpha=(1+Q-e_D-2e_E)/6=#Z(F_Q)/6,
    beta=(1+Q+e_D)/2,
    gamma=(1+Q-e_D+e_E)/3.                            (4.2)

The equality for alpha uses the actual genus-three closure identity
P_Z=P_D P_E^2, equivalently its finite-cover trace formula.
At the identity, Mobius inversion gives

    P_e(z)=sum_(k>=1) mu(k)/k log F_e(z^k),
    F_e(z)=(1+2z)/(1-z)^4.                            (4.3)

For |z|<r<sqrt(1/2), the k>=2 terms have a holomorphic sum, with
the log branches at zero: |z^k|<1/2 and log F_e(w)=O(w) uniformly
on the relevant small disks. The other two P_g are holomorphic on
such a disk as well. Hence near tau the only logarithmic term in
(4.1) is alpha log(1+2z).

One must not use the original arithmetic logarithm series beyond
Q|z|<1 without a new argument. Choose r with 1/2<r<sqrt(1/2) and
an integer N with Qr^(N+1)<1. Separate the first N complete finite
factors of (2.3). For the remaining grades, the terms of Frobenius
power m>=2 have absolute sum bounded on |z|<=r by

    2Q^2/(1-Qr^(N+1)) sum_(n>N) epsilon_n r^(2n),      (4.4)

which is finite because 2r^2<1. Here the total cohomology dimension
is at most 2epsilon_n and each m-th power trace is bounded by that
dimension times Q^m. Thus this remainder is holomorphic past tau.
The removed first-power terms are a finite polynomial in z.

The first N finite cohomological factors have neither zeros nor
poles at tau. The H^0 condition would require 2^n=1; the H^2
condition would require Q=2^n; an H^1 zero would require Q=4^n by
purity. All are impossible for n>=1 and odd Q. Finite zeros and
poles can occur elsewhere between zero and tau. Accordingly the
continuation is taken along a path avoiding those finite factors;
no globally nonvanishing disk is claimed.

It follows that a continued germ near tau has the exact form

    L_Lie(z,1)=(1+2z)^alpha H(z),                      (4.5)

where H is holomorphic and nonzero in a neighbourhood of tau,
and the power uses the branch obtained along the chosen path.
The local exponent alpha is independent of that path. A noninteger
alpha prevents any single-valued meromorphic extension at tau.

### Actual cubic monodromy when Q=1 modulo 3

Every unramified rational base point contributes zero or six
rational points to the Galois closure. At a rational finite branch
point the inertia is C2, whose normalizer in S3 is C2 itself; hence
the normalized fibre consists of three rational points. Its base
coordinate is nonzero, because the source elliptic discriminant is
nonzero, and the finite branch polynomial is even in u. Such branch
points occur in distinct pairs u,-u and contribute multiples of six.
Infinity contributes two rational points exactly when Q=1 modulo 3,
and zero when Q=2 modulo 3. Therefore

    #Z(F_Q)=2 modulo 6,      alpha is an integer plus 1/3,
                                      if Q=1 modulo 3. (4.6)

The local monodromy of (4.5) is then a primitive cube root of unity.
This gives an actual arithmetic obstruction at the trace-class
grading boundary of the Lie completion. It is not inferred from
the failure of trace class alone. For Q=2 modulo 3 this particular
congruence gives an integer exponent and does not establish a branch
obstruction; later boundaries or other mechanisms require new work.

### The arithmetic parameter gives a uniform monodromy test

The same proof applies locally uniformly near any T_0 outside the
locally finite exceptional set

    E={1/(lambda*tau^n): lambda an eigenvalue of a nonzero
                    finite H^i_n Frobenius block, n>=1}.      (4.7)

Indeed the possible eigenvalue magnitudes are 1, sqrt(Q) and Q,
so their exceptional T-values tend to infinity with n. On a small
closed neighbourhood of T_0 choose the same r as above and N so that
Q max|T| r^(N+1)<1. Bound (4.4) then has the harmless additional
factor max|T|^2 and denominator 1-Q max|T| r^(N+1), proving uniform
holomorphy of the higher-power remainder. The first-power series is
T P_ar(z), and the finite factors are locally holomorphic and nonzero
near (tau,T_0). Thus the continued local family has the form

    L_Lie(z,T)=(1+2z)^(alpha*T) U(z,T),                (4.8)

with U holomorphic and nonzero there. The arithmetic T=1 theorem is
one specialization of this source-derived family, not a fitted exponent.

If #Z(F_Q)>0, the local monodromy is exp(2*pi*i*alpha*T).
It has infinite order whenever alpha*T is not rational. No fixed
finite branched cover of the grading variable can make this family
single-valued meromorphic over a nonempty open T-set: a ramification
index d would require d*alpha*T to be an integer throughout that
open set. This statement concerns the same analytically continued
source family; it does not exclude a newly defined regularization.
When Q=1 modulo 3, positivity of #Z(F_Q) follows already from the
two rational points at infinity.

## 5. Finite duality and exact bounded replay

Let kappa_n=b_n+c'_n-a_n. Finite curve duality gives

    L_Lie,N(z,T)=Q^(K_N) T^(2K_N) z^(2W_N)
                           L_Lie,N(1/z,1/(QT)),
    K_N=sum_(n<=N)e_n kappa_n,
    W_N=sum_(n<=N)n e_n kappa_n.                       (5.1)

Since kappa_n~2^n/(3n), the geometric end of each alternating sum
dominates, and

    K_N~(-1)^(N+1) 2^(N+1)/(9N),
    W_N~(-1)^(N+1) 2^(N+1)/9.                        (5.2)

For example divide the K sum by (-1)^(N+1)2^N/N and set j=N-n.
For j<=N/2, dominated convergence uses 2^(-j)N/(N-j)<=2*2^(-j);
the remaining half is exponentially negligible. The limiting sum
is (1/3)sum_j(-1/2)^j=2/9. The W sum is the same argument without
N/(N-j). The finite prefactors therefore have no ordinary finite
limit; this does not exclude every proposed new regularization.

The replay uses actual finite Lie characters, source multiplicity
spaces, the two frozen elliptic point-count polynomials, and the full
ramified finite-fibre histograms. It checks finite cohomological
duality, the n=1 regular-source identity, low-degree ramified defects,
the Mahler coefficient laws and the closure congruence independently
of the analytic asymptotic proof. All polynomial manipulations use
short exact coefficient arrays rather than expanded state spaces.

For an ordinary finite-grade logarithm check at positive r<1/(2Q),
epsilon_n<=3*2^n gives the explicit tail after grade N

    6Q(2r)^(N+1)/[(1-2r)(1-Qr^(N+1))].               (5.3)

The finite source logarithms are evaluated with outward rational
intervals. The first-boundary proof is certified by (4.1)--(4.6),
not by numerically approaching a branch point or fitting an exponent.

## 6. Compact support explains the correction and cancels the first branch

The cubic branch in Section 4 belongs to the ordinary arithmetic
Lie parent with its actual ramified Artin factors. It must not be
promoted to an obstruction for every corrected Segre source. The
correction (3.3) has a precise compact-support interpretation and
removes the first fractional branch at T=1.

Let U=P1 minus the four finite geometric branch points and infinity.
For each finite M_n the exact sequence of extension sheaves

    0 -> j_!M_n -> j_*M_n ->
              direct_sum_(x in P1-U) i_(x,*) M_n^(I_x) -> 0

gives the Frobenius-equivariant localization sequence

    0 -> H^0_n -> direct_sum_x M_n^(I_x) ->
            H_c^1(U,M_n) -> H^1_n -> 0,
    H_c^0(U,M_n)=0,       H_c^2(U,M_n)=H^2_n.          (6.1)

The boundary sum here is over geometric points with its actual
Frobenius permutation, not a list of rational points only. A compactly
supported global section of a lisse sheaf on this connected nonproper
curve is zero. The remaining exactness follows by taking cohomology
of the displayed sheaf sequence. For the classical compact-support
definition and exactness, see Milne,
[Lectures on Etale Cohomology](https://www.jmilne.org/math/CourseNotes/LEC.pdf),
Definition 18.1 and Proposition 18.3, read directly for this extension.
The characteristic-zero version is obtained from the compatible finite
coefficient systems, as in the preceding finite-cover applications.

The geometric boundary dimension is
4(a_n+c'_n)+(a_n+b_n)=5a_n+b_n+4c'_n. Therefore

    dim H_c^1(U,M_n)=4a_n+3b_n+6c'_n=a_n+3epsilon_n,
    dim H_c^2(U,M_n)=a_n.                             (6.2)

These are actual cohomology spaces, with the same source decomposition
into finitely many fixed compact-support Frobenius modules. Their
Hilbert sums and both grade parities have the same sharp S_p threshold
2^(-1/p). The H_c^1 Frobenius eigenvalues have weights zero or one:
the boundary quotient in (6.1) has finite-order Frobenius, while the
closed H^1 part has the already proved pure weight one. No unsupported
identification with pure projective H^1 is made.

The corresponding ordinary signed compact-support determinant satisfies

    L_Lie,c(z,1)=L_Lie(z,1)/product_(v bad) B_(I_v,Fr_v)(z^deg(v))
               =product_(v in U) F_(Fr_v)(z^deg(v)),   (6.3)

initially for |z|<1/Q and then as its meromorphic determinant germ
on |z|<1/2. Thus the full invariant-Segre Euler source is obtained by
gluing the actual finite bad-place character series:

    E_Segre(z)=L_Lie,c(z,1)
                       product_(v bad) F_(I_v,Fr_v)(z^deg(v)). (6.4)

This is a localization construction, not an unexplained fitted multiplier.
It remains different from the original closed arithmetic Lie operator.

For the exact first-boundary comparison, let u be the number of rational
unramified base points whose Frobenius is identity, let b be the number
of rational finite branch points, and put i=1 if Q=1 modulo 3 and zero
otherwise. The normalized fibre counts give

    #Z(F_Q)=6u+3b+2i,
    alpha=u+b/2+i/3.                                 (6.5)

Each rational C2 factor B has exponent 1/2 at tau=-1/2, and split
C3 infinity has exponent 1/3. Nonsplit infinity is analytic and
nonzero there. Higher-degree bad-place arguments tau^f lie strictly
inside |t|<1/2, where their parent products are nonzero. At tau the
full invariant-Segre factors themselves are respectively

    F_C2(tau)=8/9,    F_C3(tau)=16/27,
    F_(C3,s)(tau)=16/9.                              (6.6)

These follow from F_e(tau)=0, F_s(tau)=16/9 and F_c(tau)=8/9.
All higher-degree real bad arguments have positive, nonzero invariant
character factors as well. Dividing (4.5) by the bad parent products
therefore subtracts b/2+i/3 from its exponent. Both L_Lie,c(z,1)
and the full source E_Segre(z) extend holomorphically through tau,
with exact zero order

    ord_(z=-1/2) E_Segre = u.                         (6.7)

If u=0 they are nonzero there. This is a local-germ conclusion, not
a claim of a globally pole-free disk or removal of later boundaries.
It is the required counterweight to the cubic branch theorem: the
source-defined ramification correction cancels that fractional branch,
while every exponential Hilbert operator retains its original sharp
trace-class threshold.
