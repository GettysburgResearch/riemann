# Heat-Hankel synthesis: intrinsic inertia and source-only finite capture

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH and the final arithmetic matrix inequality are NOT proved.
Scope: actual invariant xi; all zero multiplicities; fixed tau>=0; a prescribed
rational/dyadic test hierarchy, with no verified zero prefix or simplicity input.
Base: PR #790 at 634d9a8ec4b0819442e601686a109ff7015b7b0b.
Cross-inputs: PR #793 Hardy capture and PR #792 Laguerre/boundary work, as
itemized in CROSS_REVIEW.md. General Hankel/Hardy theory is classical.
Local labels ASTRA-HH-01 through ASTRA-HH-06 are scoped to this directory.

## 1. An elementary source budget, independent of a zero census

Set X(u)=xi(1/2+sqrt(u+1/4)), h=X'/X. Let A=rho(1-rho), where rho runs
over nontrivial zeta zeros with Im rho>0, counted with multiplicity.
The invariant genus-zero product gives

    h(u)=sum_A 1/(u+A),
    H:=h(0)=1+gamma_E/2-log(4pi)/2.                         (1)

The sum is absolutely convergent; the invariant entire function has order
1/2. Conjugation closes the A list. A nonreal A corresponds to an off-line
quartet, not a real zero of xi. Put x=Re A, y=Im A. The critical strip gives

    x=gamma^2+beta(1-beta)>0,   y=gamma(1-2beta),   y^2<=x. (2)

Every Re(1/A)=x/(x^2+y^2) is positive. Hence H>0. Elementary gamma_E<1,
pi>3 and e<3 imply log(4pi)>2 and H<1/2. Moreover

    Re(1/A)>=1/(x+1),   x>=H^(-1)-1=:x0>1,
    sum_A 1/x <= H/(1-H)=:C<1.                             (3)

Indeed each summand in (1) is at most H, giving the bound on x. Then
1/x=(1+y^2/x^2)Re(1/A)<=(1+1/x)Re(1/A)<=Re(1/A)/(1-H).
Sum this inequality. These are coarse source-derived bounds on the invariant parameters,
not a finite zero census or a location of an individual zero. Multiplicities are counted in the sum; the lower bound on
x is valid for each individual occurrence too.

## 2. ASTRA-HH-01: one source-defined trace-class Hankel operator

For tau>=0 define on L2(0,infinity)

    Gamma_tau(s,t)=S(tau+s+t),
    S(v)=sum_A exp(-v A),   v>0.                            (4)

At tau=0 the possible corner singularity is interpreted through the
trace-class expansion, not a pointwise value S(0). With f_A(t)=exp(-A t),

    Gamma_tau=sum_A exp(-tau A) |f_A><f_(bar A)|.           (5)

The inner product is conjugate-linear in the first entry. The rank-one
operator |v><w| sends f to v<w,f>. Thus its kernel is v(s)conjugate(w(t)).
This fixes both the conjugation and the Hankel, rather than Toeplitz, sign.
Each term in (5) has trace norm exp(-tau x)/(2x). Equations (2)--(3) prove
absolute trace-norm convergence, self-adjointness, and

    ||Gamma_tau||_1 <= (C/2)exp(-tau x0),
    Tr Gamma_tau=(1/2)sum_A exp(-tau A)/A,
    Tr Gamma_0=H/2.                                       (6)

All kernel and quadratic-form identities follow first on finite sums and
then by trace-norm convergence. For tau>0 the kernel is smooth. At tau=0,
normal convergence away from s+t=0 identifies the kernel with (4).

The definition is independent of a guessed zero set. For tau=0 its complete
finite exponential-test matrix is specified by h on the safe positive axis:

    K_0(p,q)=<exp(-p t),Gamma_0 exp(-q t)>
            =(h(p)-h(q))/(q-p),   p!=q;
    K_0(p,p)=-h'(p).                                      (7)

On that axis let s=1/2+sqrt(u+1/4)>1. The ordinary absolutely convergent
Euler source is

    h(u)=[1/s+1/(s-1)-(log pi)/2+(1/2)psi(s/2)
                        -sum_(n>=2)Lambda(n)n^(-s)]/(2s-1). (8)

Here psi is digamma. Equations (7)--(8), the density of exponential
polynomials (uniqueness of the Laplace transform), and existence (5) determine Gamma_0 from arithmetic data.
For tau>0 use

    h_tau(u)=int_0^infinity exp(-u v)S(tau+v)dv
            =exp(tau u)[h(u)-int_0^tau exp(-u v)S(v)dv],    (9)

and replace h by h_tau in (7). The finite integral is convergent at zero.
S itself has the unconditional prime/gamma expression

    S(v)=1+exp(-v/4)/(4pi) int_R exp(-v z^2)Omega(z)dz
       -exp(-v/4)/(2sqrt(pi v))
                          sum_(n>=2)Lambda(n)n^(-1/2)
                                    exp(-(log n)^2/(4v)),
    Omega(z)=Re psi(1/4+iz/2)-log pi.                       (10)

Each v>0 sum converges absolutely. Formula (10) retains the m=0 endpoint
term 1. It is not a claim that its separate terms may be integrated across
v=0 without the usual dominating estimates. The zero representation proves
S(v)=O(v^(-1/2)log(2/v)) there, which suffices for (9).
The positivity S(v)>0 from the earlier packet is NOT needed for (3)--(10).

There is also an unconditional, all-rank but insufficient bound:

    0<=Tr (Gamma_0)_- <= H^2/[4(1-H)].                     (11)

It follows from Tr T_-=(||T||_1-Tr T)/2 and (6). This is not positivity:
a small negative trace is still a negative trace.

## 3. ASTRA-HH-02: exact negative index, at every thermal shift

Let q be the number of DISTINCT conjugate pairs of nonreal invariant A's,
possibly infinity. This equals the number of distinct off-critical zeta
quartets. A zero's multiplicity is a positive weight, not additional
independent evaluation directions. Then

    number of negative eigenvalues of Gamma_tau, with eigenvalue
    multiplicity, equals q, for every tau>=0.              (12)

In particular Gamma_tau>=0 for ONE fixed tau>=0 iff RH.

### Proof of the lower bound and complete background capture

Fix any finite collection of target nonreal pairs. Remove these locations
from the list of DISTINCT A's and form the normalized right-half-plane
Blaschke product B with zeros at every remaining location. It exists because

    sum_distinct Re A/(1+|A|^2) <= sum_occurrences 1/x <infinity.

B is nonzero at each of the finitely many omitted targets. In the Hardy
space of the right half-plane, the subspace B H2 vanishes at every
background node. For targets p_i, the residual reproducing-kernel Gram (inner product
conjugate-linear in the first entry) is

    G_(ij)= B(p_i)conjugate(B(p_j))/(p_i+conjugate(p_j)).   (13)

Indeed k_p(t)=exp(-bar(p)t) has <k_p,k_q>=1/(p+bar(q)), and
its projection onto B H2 is conjugate(B(p)) B k_p.
This Gram is positive definite: the Cauchy kernel is strictly positive on
distinct right-half-plane nodes and the diagonal B factors are nonzero.
Thus arbitrary target values can be interpolated by a function in B H2.
The Laplace isometry supplies the corresponding L2 test function.

If F is the Laplace transform of f, the quadratic form is

    <f,Gamma_tau f>
        =sum_A exp(-tau A) conjugate(F(bar A))F(A).         (14)

All background terms vanish. One target pair of common multiplicity m
has, on its two evaluation coordinates, Hermitian coefficient matrix

    m [[0,exp(-tau bar A)],[exp(-tau A),0]],

with one positive and one negative eigenvalue. Surjective interpolation
realizes the direct sum of these coefficient forms in a finite-dimensional
test subspace. Therefore every finite selection of k pairs gives a
k-dimensional strictly negative subspace of Gamma_tau. All interchanges
in (14) are justified by the trace-norm bound in (5).

For finite q the converse bound follows by decomposing each pair's
rank-two form into one positive rank-one and one negative rank-one form.
All real A terms are positive; the sum of negative summands has rank at most
q. The min-max principle gives at most q negative eigenvalues. For infinite
q the lower bound already proves (12). This argument handles arbitrarily
close distinct nodes and arbitrary positive integer zero multiplicities.

For finite q, the finite negative rank-one forms can be obtained directly
by writing a pair as c|v><w|+conjugate(c)|w><v|, absorbing the phase of
c into v, and applying the difference-of-two-squares identity.
Thus the upper-index argument does not assume an orthonormal zero frame.
No lower sampling bound uniform in the unknown zeros is asserted.
General finite-rank Hankel inertia is classical (Yafaev); the present proof
adapts PR #793's complete Hardy-background removal to the invariant heat
parameters and retains the infinite tail through trace-class convergence.

Thermal smoothing does not remove this index. If U_a is the right-shift
isometry, then Gamma_tau=U_(tau/2)^* Gamma_0 U_(tau/2). Its negative trace
can tend to zero while its negative index remains nonzero for every finite
tau. This rules out inferring positivity from that limiting smallness.

## 4. ASTRA-HH-03: predetermined dyadic finite spaces, explicit capture

For integers k>=1, J>=0 set

    B_(k,J)(p)=product_(j=0)^J [(p-2^j)/(p+2^j)]^(2k),
    V_(k,J)=span{t^r exp(-2^j t): 0<=j<=J, 0<=r<2k},
    N=dim V_(k,J)=2k(J+1).                                (15)

Let P_(k,J) be the ORTHOGONAL projection in the original L2 metric. These
spaces and their metrics are fixed without inspecting any zero.
Hardy model-space projection gives

    ||(I-P)f_A||=|B_(k,J)(bar A)| ||f_A||.                 (16)

For completeness, V is the inverse Laplace image of H2 minus B_(k,J)H2;
repeated factors correspond exactly to confluent exponential-polynomial
vectors. Projecting the reproducing kernel gives (16).

If 1<=x<=2^J, select a dyadic b with b<=x<=2b and 1<=b<=2^J. By y^2<=x,

    |(A-b)/(A+b)|^2 <=1/3.                                (17)

Here is an all-parameter proof, not a numerical sample. The desired
inequality is x^2-4bx+b^2+y^2<=0. Write x=br, 1<=r<=2. Its left side is
at most b^2(r^2-4r+1)+br <=b^2(r^2-3r+1)<=-b^2.
The other Blaschke factors have modulus at most one, hence

    |B_(k,J)(A)|<=3^(-k),   1<=x<=2^J.                    (18)

The rank-one identity T-PTP=(I-P)T+PT(I-P), applied before summation, gives

    ||Gamma_tau-P Gamma_tau P||_1
       <=sum_A exp(-tau x)|B_(k,J)(A)|/x.                 (19)

No assertion about contractivity of a non-isometric compression is used.

### Positive thermal shift: accuracy exponential in k

Fix tau>0 and choose the smallest J>=0 with tau*2^J>=2k. Splitting (19)
at x=2^J, (18) controls the lower range and exp(-tau x)<=exp(-2k)<3^(-k)
controls the upper range. Equation (3) then proves

    ||Gamma_tau-P_(k,J)Gamma_tau P_(k,J)||_1
          <= C 3^(-k) <3^(-k).                           (20)

Thus dimension is O_tau(k log(k+2)), with a specified rational error for
every k. This is a rank/error theorem, not a claim of practical numerical
conditioning or positivity. It uses no zero locations, finite zero
verification, or density asymptotic beyond the convergent product (1).

### Zero thermal shift: safe Euler derivatives only

For R=2^J, x>R, equations (2) give

    Re(1/(R+A))=(R+x)/[(R+x)^2+y^2]>=1/(5x).

Consequently the fully source-evaluable bound is

    ||Gamma_0-P_(k,J)Gamma_0 P_(k,J)||_1
                         <=C3^(-k)+5h(2^J).              (21)

The elementary digamma inequality psi(s)<=log s for s>0 and (8), dropping
the negative Euler sum, give for u>=1

    0<h(u)<=[2+(log u)/8]/sqrt(u).                         (22)

Indeed s>3/2, 1/s+1/(s-1)<3, s<=2sqrt(u), and 2s-1>=2sqrt(u).
One proof of psi(s)<log s uses its standard positive integral remainder
log s-psi(s)=int_0^infinity exp(-s t)[1/(1-exp(-t))-1/t]dt.

Set J=4k. Then N=2k(4k+1) and

    ||Gamma_0-P_(k,4k)Gamma_0 P_(k,4k)||_1 <= epsilon_k,
    epsilon_k=C3^(-k)+(10+5k/2)4^(-k)
            <3^(-k)+(10+5k/2)4^(-k) ->0.                 (23)

This unheated version needs only finitely many derivatives of the
absolutely convergent Euler source (8). The thermal version needs (9).
The two versions are not silently identified computationally.

## 5. ASTRA-HH-04: exact arithmetic matrices in the inherited metric

In the raw basis e_(j,r)=t^r exp(-2^j t), the metric is exactly

    G_((j,r),(l,s))=(r+s)!/(2^j+2^l)^(r+s+1).              (24)

It is positive definite by linear independence. Let Q be the actual form
matrix. With p=2^j,q=2^l it is

    Q_((j,r),(l,s))=(-partial_p)^r(-partial_q)^s
                       [(h_tau(p)-h_tau(q))/(q-p)],        (25)

using continuous confluent limits. Equivalently

    Q_((j,r),(l,s))=r!s! sum_A exp(-tau A)
                           /[(A+p)^(r+1)(A+q)^(s+1)].    (26)

The matrix of the orthogonal compression is M=G^(-1/2)QG^(-1/2), not Q
with an arbitrary Euclidean norm. PSD can be tested on Q by congruence;
trace norms and eigenvalue error must use M or the generalized pair (Q,G).

An explicitly orthonormal alternative avoids changing the metric. Order
all repeated dyadic poles b_1,...,b_N and use the Takenaka--Malmquist
Laplace transforms

    R_j(z)=sqrt(2b_j)/(z+b_j)
                          product_(l<j)(z-b_l)/(z+b_l).   (27)

Their inverse Laplace transforms form a real orthonormal basis of V.
A quick proof: each all-pass factor is an isometry on H2, and it vanishes
at the previous interpolation point, giving orthogonality to the previous
normalized reproducing kernel; induct on the number of factors. This also
covers repeated b_j. The matrix entry is sum_A exp(-tau A)R_i(A)R_j(A).
Partial fractions of the finite rational function R_i R_j express it in
safe source derivatives, using

    sum_A exp(-tau A)/(A+b)^r
             =(-1)^(r-1)h_tau^(r-1)(b)/(r-1)!.            (28)

There is no zero interpolation in the definition (27). The zero
interpolation in Section 3 is only the proof of the capture theorem.

### The exact prime/gamma quadratic form

For a real linear combination f in V let R(z)=int exp(-z t)f(t)dt.
Define g(z)=exp(-tau(z^2+1/4))R(z^2+1/4)^2. It is even and analytic in
a strip wider than |Im z|<=1/2: all its rational poles are at
z=+/-i sqrt(b+1/4), with b>=1. For tau=0 it decays at least as |z|^-4;
for tau>0 it has Gaussian strip decay. The unconditional explicit formula
therefore gives, with ghat(ell)=int_R g(x)exp(-i ell x)dx,

    4pi <f,Gamma_tau f>
      =4pi R(0)^2+int_R g(x)Omega(x)dx
                   -2 sum_(n>=2)Lambda(n)/sqrt(n)ghat(log n). (29)

The endpoint term 4pi R(0)^2 is compulsory unless R(0)=0. The full prime
sum is absolutely convergent: shift the Fourier contour to a fixed line
strictly between heights 1/2 and sqrt(5/4). This is a legal source formula,
not a claim of positivity based on g(x)>=0 on the real line.

## 6. ASTRA-HH-05: certified brackets for the intrinsic negative mass

Let nu_tau=Tr(Gamma_tau)_- and nu_(k,J)=Tr(M_(k,J))_-. For any orthogonal
finite compression,

    0<=nu_(k,J)<=nu_tau,
    nu_tau<=nu_(k,J)+||Gamma_tau-P Gamma_tau P||_1.          (30)

The first inequality is the variational characterization of negative trace
as sup_(0<=Z<=I) -Tr(Z T). The same characterization makes this functional
1-Lipschitz in trace norm, proving the second inequality.
Use (20) or (23) for a fully explicit bracket. For fixed tau>0 the spaces
are nested as k and the specified J grow, so their negative traces increase
to nu_tau. The unheated spaces J=4k are also nested.

If an approximate symmetric matrix Mtilde satisfies ||Mtilde-M||_1<=eta,
its computed negative trace gives the enclosure

    max(0,Tr(Mtilde)_--eta) <=nu_tau
             <=Tr(Mtilde)_-+eta+epsilon.                  (31)

For entrywise errors at most delta in an orthonormal basis, the elementary
safe bound eta<=N^2 delta suffices. A raw-basis error cannot use this bound
without paying the G metric. No interval eigensolver is claimed here.

Every hypothetical off-line quartet forces nu_tau>0 by (12), and is thus
detected by some FINITE matrix in this predetermined hierarchy. Even a
finite isolated exception cannot disappear in the infinite background.
No target-independent lower bound on nu_tau or universal first detection
rank is claimed. Arbitrarily small defects can require arbitrarily high rank.

## 7. ASTRA-HH-06: full attack, proved near-positivity, and the open sign

This synthesis replaces the scalar heat-derivative tests by a complete
source-only matrix hierarchy. At ONE fixed tau>=0, each condition is
now equivalent to RH:

    Gamma_tau>=0;
    Q_(k,J(k))>=0 for every k;
    Tr(M_(k,J(k)))_- ->0;
    [tau=0] ||Gamma_0||_1=H/2.                            (32)

These follow from (12), density/trace-norm capture, and (30). The error and
capture arrows are proved; the arithmetic matrix inequality is OPEN.
The unconditional result (11), together with (30), bounds every finite
negative trace by H^2/[4(1-H)] in the unheated hierarchy. It does not force
that bound to be zero.

The attempted proof was to insert the positive heat source into (25) and
use the newly controlled prime diagonal of PR #792. Neither step establishes
PSD. Positive S makes (4) a pointwise positive kernel, and even makes Q
entrywise positive in the nonnegative raw basis, but arbitrary signed
linear combinations require a stronger property. The #792 diagonal belongs
to a different signed two-variable energy; no equality to (29) or domination
of its cross terms has been proved. Its PNT-preserving countermodel warns
against asserting one from the diagonal alone.

Here is an exact rejection of the generic heat-to-Hankel step. For the
NONNATIVE polynomial F(u)=(1+u)(1+4u/5+u^2/5), its invariant parameters are
1,2+i,2-i and S_F(t)=exp(-t)+2exp(-2t)cos t>0 for every t>0.
For t<=log2 this follows from log2<1<pi/2; for t>log2 it follows from
exp(t)>2. Yet the real L2 test

    f(t)=exp(-t)(22-114t+70t^2),
    R(A)=2(A-1)(11A-24)/(A+1)^3

has R(1)=0, R(2+i)=i, R(2-i)=-i, and

    <f,Gamma_0^F f>=-2,    ||f||^2=697.                   (33)

In the first three unit-Laguerre functions, the same operator has matrix

    [[41/50,   22/125,   48/625],
     [22/125, 48/625,   82/3125],
     [48/625,82/3125, 88/15625]],
    determinant=-2/15625.

All displayed entries are positive. This is not a counterexample to RH,
and it does not preserve the literal zeta Euler data. It proves precisely
that the positive scalar heat theorem does not supply the matrix step.

Nor can the small bound (11) be upgraded using an integer-valued index.
For any real c>=5, the NONNATIVE source

    S_c(t)=exp(-ct)+2exp(-2ct)cos t

is positive for every t>0 by the same split at t=(log2)/c. Its parameters
c,2c+i,2c-i satisfy y^2<=x and H_c=1/c+4c/(4c^2+1)<2/c<1/2.
It has exactly one negative eigenvalue, but the trace/norm calculation gives

    0<Tr(Gamma_0^c)_- <=1/[4c(4c^2+1)]<1/(16c^3).         (34)

Indeed ||Gamma_0^c||_1<=1/c and Tr Gamma_0^c=H_c/2; apply the same negative
trace formula. This family shows that a positive heat source, the parabolic
strip constraint, and arbitrarily small negative spectral mass can coexist.
It does not preserve the xi Euler product or the exact xi value of H.

A valid completion would prove (29)>=0 for every real rational coefficient
vector in the prescribed spaces, or prove their negative traces tend to
zero by another literal-source argument. Rational coefficient vectors are
sufficient by continuity. No such all-k estimate has been obtained here.
The present result closes effective operator capture and gives a full
source/metric dictionary; it does NOT close RH.
