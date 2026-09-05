# A source-built Hardy operator, conserved trace moments, and linear finite sections

Status: PROPOSED COMPLETE PROOFS; independent mathematical and code review required.
RH, positivity of every finite section, and the original subexponential inequality remain OPEN.
Scope: the actual Riemann xi function and all its zero multiplicities; fixed a=3/4, b=3/2; all degrees. Separately identified finite polynomial controls.
Exact parents: PR #792 at 875e8dd47186e924445533513a1ad405af09d7a7; PR #793 at f22b67db113d1aa4f986fe35a2fc0321fdff7d47, pass2/R3_HARDY_CAPTURE.md.
What was executed: bounded rational/Gaussian-rational identities and one actual 4-by-4 safe-source interval certificate, not an all-order sign test.
Smallest remaining gap: positivity of the explicit arithmetic form in Section 8, or a new cancellation estimate implying it.
Local labels HL-1 through HL-6 have no canonical-registry status. No external priority claim.

## 1. Freeze the common normalization

Write xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2, Xi(z)=xi(1/2+iz),
and L(r)=(xi'/xi)(1/2+r). Fix a=3/4 and b=2a=3/2. The symbol z below
labels ALL DISTINCT Xi zeros, including both signs, with multiplicity m_z.
Write z=gamma+iy, where |y|<1/2. This is not a list restricted to positive
ordinates. The usual even product and N_*(T)=O(T log(eT)) suffice.

Use the operator already constructed in #793:

    h_z(t)=sqrt(b) exp(-a t+izt)/(b-iz),
    T=sum_z m_z |h_z><h_(bar z)|,            t>=0,
    W_b(x)=sum_z m_z exp(izx)/(b^2+z^2),
    T(t,u)=b exp(-a(t+u)) W_b(t-u).

Inner products are linear in the second argument. The sum is trace-class
and self-adjoint. In fact Section 2 reconstructs T as an absolutely
trace-norm-convergent ARITHMETIC series, without using unknown zeros to
specify the operator or to prove its trace-class existence.

The parent's safe source identity is

    g(r):=int_0^infty exp(-rx) W_b(x)dx
        =[L(r)-(r/b)L(b)]/(b^2-r^2),          r>1/2.

The singularity at r=b is removable. The old coefficient sequence is

    sum_(n>=0) d_n w^n=d_0/2+(3/8)L(b(1-w)/(1+w)),
    d_0=(b/2)L(b).

Thus these are exactly #792's d_n, not a newly normalized observable.

## 2. HL-1: an explicit arithmetic trace-class construction

Set c_j=2j+1/2 for j>=1 and C_b=(1-gamma_E-log(2pi))/3. Directly from
Euler's product and the digamma partial fractions, the actual kernel is

    W_b(x) = (1/2)exp(|x|/2)+C_b exp(-b|x|)
       + sum_(j>=1) exp(-c_j|x|)/(c_j^2-b^2)
       - (1/3) sum_(n>=2) Lambda(n)/sqrt(n)
          [exp(-b|x-log n|)+exp(-b|x+log n|)].                 (A1)

All prime powers and their exact von Mangoldt weights are retained.
Every series is locally uniformly convergent in x. A stronger statement is

    ||T||_1 < 30.                                           (A2)

This numerical ceiling is deliberately coarse. It requires no RH, zero
prefix, prime number theorem, or numerical evaluation of xi.

### Derivation of A1

For a constant L(r)=C, the source transform g is C/[b(b+r)] and its
inverse is (C/b)exp(-b|x|). For L(r)=1/(r+c), its inverse source is

    [exp(-c|x|)-(c/b)exp(-b|x|)]/(b^2-c^2).                  (A3)

All identities can be checked by a half-line Laplace transform. Take the
removable limiting value if c=b. Here c=-1/2 and c=c_j never equal b.
The completion gives

    L_Gamma(r)=1/(r-1/2)+(1-gamma_E-log pi)/2
                +sum_(j>=1)[1/(2j+2)-1/(r+c_j)].

The 1/(r+1/2) term is cancelled by the j=0 digamma pole; the remaining
constant 1/2 is included. Since 2j+2=c_j+b, each bracket in the sum has
inverse source [exp(-c_j|x|)-exp(-b|x|)]/(c_j^2-b^2).
Finally

    sum_(j>=1) 1/(c_j^2-b^2)=1/6+(log 2)/3.

This follows from 1/[2(2j-1)(j+1)]=1/[3(2j-1)]-1/[6(j+1)].
Combining this with A3 at c=-1/2 gives the first three terms of A1.

For the single prime-power term L_n(r)=-q_n exp(-r ell), where
q_n=Lambda(n)/sqrt(n) and ell=log n, the inverse source is

    W_n(x)=-q_n/(2b)[exp(-b|x-ell|)+exp(-b|x+ell|)].          (A4)

For example, on 0<=x<=ell it is -(q_n/b)exp(-b ell)cosh(bx);
on x>=ell it is -(q_n/b)cosh(b ell)exp(-bx). Its Laplace transform is
[-q_n exp(-r ell)+(r/b)q_n exp(-b ell)]/(b^2-r^2).
This proves A1, first for r sufficiently large and then by uniqueness.

### Proof of arithmetic trace-norm convergence

Let H_c have kernel b exp(-a(t+u))exp(-c|t-u|). For c>=0, H_c is positive
trace-class with trace one: the exponential difference kernel is positive
definite, and its damped diagonal integrates to b/(2a)=1.

H_(-1/2) is also trace-class, but need not be positive. The identity, for
c=1/2,

    exp(c|t-u|)=exp(c(t+u))
             -2c int_0^min(t,u) exp(c(t+u-2v))dv

writes H_(-1/2) as a positive rank-one operator of trace 3 minus a positive
trace-class operator of trace 2. Hence ||H_(-1/2)||_1<=5.

Let H_ell^- have kernel b exp(-a(t+u))exp(-b|t-u-ell|), and set
H_ell^+=(H_ell^-)^*. If V_ell is the right-shift isometry on L2(0,infty),
then exactly

    H_ell^-=exp(-a ell)V_ell H_b
           +b exp(-b ell)|u_ell><v|,
    u_ell(t)=1_[0,ell](t)exp((b-a)t),
    v(t)=exp(-(b+a)t).

The rank-one norm is at most exp(-a ell)/sqrt(3). Consequently

    ||T_n||_1 <= (1+1/sqrt(3))/b * Lambda(n)n^(-5/4),          (A5)
    T_n=-q_n/(2b)(H_ell^-+H_ell^+).

The exponent 5/4 is obtained BEFORE the sum over n. It is not an
unjustified boundary use of the Euler product. Since Lambda(n)<=log n,

    sum_(n>=2) Lambda(n)n^(-5/4)
       <=int_1^infty log(x+1)x^(-5/4)dx
       <=16+4log2<19,

and (1+1/sqrt3)/b<4/3. Also |C_b|<2/3 and
sum_j 1/(c_j^2-b^2)<2/5. Thus

    ||T||_1 < 5/2+2/3+2/5+(4/3)19 <30.

This proves A2 from arithmetic source data. For integer cutoffs X>=2,
J>=1, the discarded prime-power and archimedean tails satisfy

    ||T-T_(X,J)||_1
      <=1/(4J)+(4/3)X^(-1/4)(4log X+19),                     (A6)

with H_(-1/2) and C_b H_b kept exactly. The gamma bound uses
c_j^2-b^2>=4j^2. The prime bound is the same integral comparison from X.
The finite cutoff T_(X,J) is still an operator; projection onto finitely
many basis functions is a separate step below.

## 3. HL-2: one safe arithmetic jet produces every fixed matrix

Use the predetermined orthonormal Laguerre basis

    e_j(t)=sqrt(b) exp(-bt/2)L_j(bt),          j>=0.

Completeness and orthogonality are the classical alpha=0 Laguerre facts.
Let M_ij=<e_i,T e_j>. The bivariate source generating function is

    sum_(i,j>=0) M_ij z^i w^j
      = b [g(b/(1-z))+g(b/(1-w))]/(2-z-w).                   (A7)

Initially it is an identity near (0,0), which suffices to extract every
finite coefficient. The source on each compact subdisk is Euler-safe:
Re(b/(1-z))>b/2=3/4, so Re(s)>5/4. It is not being continued to the
critical line by assumption.

To prove A7, sum the Laguerre generating functions in the two integrals.
The resulting exponent parameters are r=b/(1-z), s=b/(1-w). Splitting
the quadrant into t>=u and u>=t gives

    int int exp(-rt-su)W_b(t-u)dtdu=[g(r)+g(s)]/(r+s).

The prefactors give A7. All these integrals converge absolutely near zero.
If G_k=[z^k]g(b/(1-z)), then

    M_00=bG_0,
    2M_i0=M_(i-1,0)+bG_i,           i>=1,
    2M_ij=M_(i-1,j)+M_(i,j-1),      i,j>=1.                  (A8)

The matrix is real symmetric. Its leading K-by-K section requires only
G_0,...,G_(K-1), equivalently L's Taylor coefficients through order K
at r=b (the xi logarithmic derivative at s=2). No zero locations are input.

An independent zero-side expression, used to prove identities and tail
bounds but NOT to assemble the actual certificate, is

    M_ij=sum_z m_z b^2/(b^2+z^2)^2 q_z^i p_z^j,
    q_z=-iz/(b-iz), p_z=iz/(b+iz).                            (A9)

It follows by integrating one Laguerre polynomial. Both |q_z| and |p_z|
are strictly below one. Since q_z+p_z=2q_z p_z, A9 also proves A8 in the
interior and checks its orientation.

## 4. HL-3: exact conserved form and the original Chebyshev moments

Identify the basis with l2 and let S e_j=e_(j+1), A=I-2S. Then

    A^* T A=T,                                              (A10)
    d_n=(b^2/2)Tr(T A^n)=(9/8)Tr(T A^n),        n>=0.         (A11)

A10 follows immediately from the interior recurrence in A8. Boundedness
extends it from finite vectors to the whole space. For A11 note that
A^* h_z=lambda_z h_z, lambda_z=(b+iz)/(b-iz), while
conjugate(lambda_(bar z))=lambda_z^(-1). Moreover

    <h_(bar z),h_z>=1/(b^2+z^2).

Cyclicity for trace-class products and the paired product give
Tr(T A^n)=sum_z m_z lambda_z^(-n)/(b^2+z^2). The symmetry z->-z changes
lambda into its reciprocal, so this equals (2/b^2)d_n. Every sum converges
at fixed n. This establishes exact normalization, including n=0.

If T>=0, Hilbert--Schmidt Cauchy--Schwarz and A10 give

    |Tr(T A^n)|<=sqrt(Tr T Tr(A^(*n)T A^n))=Tr T,
    |d_n|<=d_0.                                             (A12)

This implication supplies the original bound without an additional
cofinal capture or family-to-principal premise. But T>=0 is NOT proved.
In particular A10 does not imply positivity of its conserved form.

## 5. HL-4: a linear-size trace section, not exponential dimension

Let P_M project onto e_0,...,e_(M-1). For M>=n and M>=1, define

    J_(M,n)=Tr(P_M T A^n P_M)
       =sum_(i=0)^(M-1) sum_(j=0)^n binom(n,j)(-2)^j M_(i,i+j).

This is computed from the leading (M+n)-by-(M+n) source matrix. It is NOT
Tr((P_M T P_M)(P_M A P_M)^n); deleting the entries with i+j>=M would
change the identity.

The complete exact tail is

    (2/b^2)d_n-J_(M,n)
      =sum_z m_z/(b^2+z^2)
        [z^2/(b^2+z^2)]^M lambda_z^(-n).                    (A13)

Sum the geometric i series in A9 after the finite binomial j sum.
This argument retains all interference before estimating it.

Suppose N_*(T)<=C T log(eT) for T>=1, including all signs and multiplicities.
Then uniformly for M>=n,

    |d_n-(9/8)J_(M,n)|
       <=27 C log(e sqrt M)/sqrt M.                         (A14)

For the actual xi one may take the deliberately crude C=40 below. Thus
the ceiling in A14 can be replaced by 1080 log(e sqrt M)/sqrt M.

### The source-specific damping estimate

Put R=|z|^2, y=Im z and D_-=R+b^2-2b|y|, D_+=R+b^2+2b|y|. Then
D_->=gamma^2+1 and, for M>=n,

    |z^2/(b^2+z^2)|^M max(|lambda_z|,|lambda_z|^-1)^n
       <=(R/D_-)^M
       <=exp[-3M/(4(1+gamma^2))].                           (A15)

Indeed the first expression is
R^M D_+^((n-M)/2) D_-^(-(n+M)/2). Also D_--R>=3/4 and
R+3/4<=gamma^2+1. Finally |b^2+z^2|>=D_->=1+gamma^2.
This proves that A13 is bounded by

    sum_z m_z/(1+gamma^2) exp[-3M/(4(1+gamma^2))].            (A16)

The zero-count bound makes A16 at most 24 C log(e sqrt M)/sqrt M.
For an elementary proof put Y=sqrt M. Above Y, shells
[2^kY,2^(k+1)Y) cost at most
C/Y [4log(eY)+8log2] in total. Between 1 and Y, shells
(Y/2^(k+1),Y/2^k] cost at most

    (4C log(eY)/Y) sum_(k>=0) 2^k exp(-3*4^k/8)
       <=8C log(eY)/Y.

For k>=1 use 4^k>=4k and log4<3/2; the k=0 term is below one.
The zeros with |gamma|<1 cost at most C exp(-3M/8)<=C/Y.
These bounds are smaller than 24 C log(eY)/Y. Multiplication by 9/8
proves A14.

### An explicit coarse count independent of finite zero verification

Jensen at s=2 on concentric radii T+2 and 2(T+2), using the positive theta
integral and xi(2)>1/2, gives

    N_*(T) log2 <= 2log(2T+6)+(T+4)log(T+4)+log2.

Here N_* counts both signs. Gamma log convexity between neighboring
integers bounds Gamma(T+3) by (T+4)^(T+4). For T>=1 the right side is
at most 17 T log(eT): use T+4<=5T, 2T+6<=8T, log5<2, log8<3.
Since log2>1/2, C=40 is valid. No numerical zero census is used.

### Why this is a genuine improvement over a generic norm transfer

The ambient norm is ||A^n||=3^n. Under the standard Hardy identification S
is multiplication by z, so A^n is multiplication by (1-2z)^n; its norm
is the supremum 3^n. A generic trace-norm approximation would therefore
multiply its error by 3^n. A13--A15 exploit the actual paired spectral
geometry and avoid that loss for truncation: choose M=n and use only 2n
source coordinates, with an O(log n/sqrt n) error.
This does NOT eliminate the binomial conditioning of the finite linear
functional J_(M,n) when its entries carry independent errors. It also does
not prove J_(M,n) bounded. Those two distinctions are essential.

## 6. HL-5: predetermined sections capture every negative direction

Let T_M=P_M T P_M, extended by zero. For M>=8,

    ||T-T_M||_1 <=200 C log(e sqrt M)/sqrt M.                 (A17)

Indeed the Laguerre coefficient sequence of h_z is geometric with ratio
q_z, so ||(I-P_M)h_z||=|q_z|^M||h_z||. Moreover

    ||h_z||||h_(bar z)|| <=(3/sqrt5)/(1+gamma^2),
    |q_z|^M, |p_z|^M <=exp[-3M/(8(gamma^2+4))].

Decomposing each rank-one compression error bounds the left side by
(6/sqrt5) times A16 with M replaced by M/8. The shell proof above and
(6/sqrt5)*24*sqrt8<200 prove A17. These estimates do not use RH.

Therefore every negative eigenvalue -eta of T is detected by this FIXED
source-defined sequence once the A17 ceiling is less than eta. No
zero-adapted interpolation nodes, unknown Blaschke products, or new frame
hypotheses are needed to assemble a detecting section. The required M
still depends on the negative gap; no uniform nonzero gap is asserted.
A negative quadratic value of an EXACT compression already witnesses
negativity of T and needs no tail payment. The tail is needed to guarantee
that an unknown negative direction will eventually be captured.

Also |Tr(T_-)-Tr((T_M)_-)|<=||T-T_M||_1, by the variational formula for
negative trace. Thus the negative trace is approximable with this error;
a finite small upper bound is not proof that it is zero.

If T_(M+n)>=0, A10 and finite Cauchy--Schwarz give
|J_(M,n)|<=Tr(T_M): the two vectors e_i and A^n e_i both belong to the
section, and their T-quadratic values are equal. This is a finite
conditional bridge, not unconditional positivity of those sections.

## 7. HL-6: a rational actual-source certificate and a hostile control

The code constructs the actual leading 4-by-4 matrix using ONLY source
jets at s=2, with rational outward intervals. It does not input any zeros.
Its four strict LDL pivot intervals are approximately

    1.644018388766449e-4,
    1.4032312955080464e-6,
    2.273967636099558e-9,
    8.041153138641404e-12.

The decimal display is not acceptance data; exact rational endpoints are
in result.json. This is a finite matrix of the literal operator, not a
finite positive determinant completion of xi. It does not extend the
classical verified zero range or prove another section positive.

### Source enclosure proof

For N=64,m=12 use the Euler--Maclaurin expression

    zeta(s)=sum_(k<N)k^-s+N^(1-s)/(s-1)+N^-s/2
      +sum_(j=1)^m B_(2j)/(2j)! (s)_(2j-1)N^(1-s-2j)+R(s),
    R(s)=-(s)_(24)/24! int_N^infty B_24({x})x^(-s-24)dx.

On |s-2|=1/4,

    |R(s)| <= R0:=|B24|/24 * [prod_(j=0)^23(j+9/4)/24!] N^-24.

The exact periodic Bernoulli bound follows from its absolutely convergent
Fourier series. Cauchy therefore bounds the coefficient [h^j]R(2+h)
by 4^j R0. The checker retains terms through j=8; this is more than the
five derivatives needed for the 4-by-4 section. Finite Taylor convolution
and reciprocal-series recurrence give zeta'/zeta with interval enclosure.

For gamma_E use H_(N-1)-log N+1/(2N)+sum_(j=1)^m B_(2j)/(2j N^(2j)),
with error at most |B24|/(24 N^24). For integer k=2,...,8 use the same
Euler--Maclaurin formula at k with remainder ceiling
|B24|(k)_24/[24!(k+23)N^(k+23)]. The gamma contribution at s=2 is
log Gamma(1+h/2)=-gamma_E h/2+sum_(k>=2)(-1)^k zeta(k)h^k/(k 2^k).
The remaining factors log(2+h), log(1+h), and -(h/2)log pi are explicit.
The code computes Bernoulli numbers by an exact rational recurrence.

Pi is enclosed by Machin's identity using 80 alternating terms of each
arctangent. Logarithms use power-of-two reduction and 180 terms of
2sum y^(2j+1)/(2j+1), with the geometric positive remainder and |y|<=1/3.
Every interval operation rounds outwards to the rational grid 10^-80.
No floating-point special-function routine is used for acceptance.

### Why conservation and four positive dimensions do not finish

Take the six Xi-like zero locations

    Z_*={+1,-1, 3+i/4,3-i/4,-3+i/4,-3-i/4},

all with multiplicity one. Use these as a separately declared finite
polynomial control in A9. Its operator is real, self-adjoint, finite rank,
trace-class, satisfies A10 and all the exact trace identities, and has a
positive leading 4-by-4 section. Its fifth LDL pivot is STRICTLY NEGATIVE;
the sixth is negative too. The exact rational pivots are reconstructed.
Thus conservation plus trace-class compactness plus the first four signs
does not force positivity. This is not a spectrum of actual xi and does
not have its Euler product.

This same control has a positive invariant heat density for every t>0.
Its invariant A parameters are 5/4 and 147/16 +/-3i/2. Hence

    S_*(t)=exp(-5t/4)+2exp(-147t/16)cos(3t/2)>0.

Up to t=pi/3 the cosine is nonnegative. Thereafter the first exponential
dominates since exp((127/16)t)>2. Thus even the all-order ordinary
Bernstein-logarithm layer does not fix this failed positivity inference.

## 8. The actual completion attempt and its still-open arithmetic step

The synthesis gives an exact source-first chain:

    convergent arithmetic operator A1
      -> finite matrices from jets at s=2
      -> [OPEN: all-section positivity]
      -> positive conserved form A10
      -> bounded traces A12
      -> original d_n and c_n(2) bound
      -> RH.

The first two arrows, the trace identities, linear finite-section error,
and predetermined negative-witness capture are proved above. They are
not the missing sign arrow. Two attempted proofs of that arrow fail:

1. Conservation + compactness: the six-node rational control disproves it.
2. Absolute prime-form domination: the exact cost is different from A5.

For the latter, put q_n=Lambda(n)/sqrt(n). For every compactly supported
L2 function f, Fourier transformation of exp(-b|x|) gives

    |<f,T_n f>| <=(q_n/b)<f,H_b f>.                          (A18)

This constant is SHARP. Set g(t)=exp(-at)f(t), extend by zero to R, and
use the multiplier ratio -(q_n/b)cos(omega log n). Long smooth packets
supported far from zero and concentrated near omega=0 or pi/log n attain
the two limiting signs. Thus the relative-form constant is q_n/b, NOT
the decaying trace-norm constant O(q_n n^-a) from A5. Their sum diverges.
The choice of packets permits large but finite f-norm; the inequality is
homogeneous and asserts no uniform norm bound on those trial packets.

A5 and A6 genuinely control the entire prime operator and its cutoff
error, but do not make it a small relative perturbation of H_b. Taking
absolute values in A18 does not establish gamma domination. The literal
signed arithmetic still has to be used before this last comparison.
Neither all-section positivity nor a signed replacement for A18 is proved.

The results belong to the classical Weil/Hardy/Stieltjes framework; Suzuki's
work is relevant prior literature. The claimed contribution is this exact
cross-PR normalization, arithmetic nuclear construction, source matrix,
and linear-size trace/capture transfer, not a new general RH criterion.
