# Primitive cycle determinants with logarithmic-cost regularization

Status: PROPOSED complete component arguments, awaiting independent mathematical
review. No RH proof or new zeta zero-free half-plane is claimed. The required
centered height bound below remains OPEN. The matrices are positive, but their
spectrum is not asserted to be the spectrum of the Riemann zeros.

Exact parent: #993, 5569defd8d77f1f8f3586b326577aacb384ffb23,
ZERO_PRESERVING_ROUTE.md. Retain its full ordinary-integer source

    A_N=product_(p^j<=N) p^(N-p^j),
    C(x)=sum_(n<=x)(x-n)Lambda(n), C(N)=log A_N.

Classical cyclotomic identities are credited to the literature, not claimed
new; see Akiyama--Kaneko, arXiv:2204.11267v6, (1)--(2), Remark 2 and the
Lehmer/Jordan discussion. The contribution proposed here is the complete
fixed-source matrix assembly, the explicit logarithmic comparison and the
one-sided consumer. Sums, divisibility masks and prime powers are not replaced
by a favorable subfamily.

## 1. One rational positive matrix for the exact primitive integer

For n>=2 let S_n be the cyclic permutation matrix, L_n=2I-S_n-S_n^T, and

    c_n(k)=sum_(d|gcd(n,k)) d mu(n/d),
    (P_n)_(i,j)=c_n(i-j)/n, 0<=i,j<n.

Finite Fourier inversion shows that P_n is the orthogonal projector onto
ALL primitive nth Fourier modes. Indeed the coprimality indicator
sum_(d|gcd(a,n))mu(d), followed by a geometric sum, gives
c_n(k)=sum_(1<=a<=n,gcd(a,n)=1)exp(2pi i ak/n). Consequently

    P_n=P_n^T=P_n^2, tr(P_n)=phi(n), P_n S_n=S_n P_n.

It is rational. For t>=0 put

    H_n(t)=I-P_n+P_n(L_n+tI),
    H_N(t)=direct_sum_(n=2)^N H_n(t) repeated (N-n) times,
    V_N(t)=(1/2)log det H_N(t).

An empty direct sum has determinant one. Complementary modes have eigenvalue
one; primitive modes have eigenvalues

    t+4sin^2(pi a/n), 1<=a<n, gcd(a,n)=1.                (1)

Thus EVERY matrix is real symmetric positive definite, including t=0.
For rational t the matrix entries are rational. Complementary modes are
retained, not discarded during a determinant computation.

### Theorem 1

With D_n(t)=det H_n(t), n>=2,

    D_n(t)=Res_x(Phi_n(x),x^2-(2+t)x+1) in Z[t],
    D_n(0)=Phi_n(1)^2=exp(2Lambda(n)),
    det H_N(0)=A_N^2, V_N(0)=log A_N.                    (2)

Every coefficient of D_n is positive, and it is monic. Its roots are the
negative eigenvalues in (1) at t=0, counted with multiplicity.

Proof. At a primitive root zeta, the quadratic in (2) equals
-zeta[(2+t)-zeta-zeta^(-1)]. The product of primitive roots is
(-1)^phi(n)Phi_n(0)=(-1)^phi(n), so the signs and roots cancel in the
resultant, giving (1). Integrality follows from the integer resultant;
coefficient positivity follows from its product of positive linear factors.
The classical identity Phi_n(1)=product_(d|n)d^mu(n/d)=exp Lambda(n)
includes every prime power. It gives the last assertions. QED.

For reproducibility there is a second, wholly integer construction. Set
C_0(t)=0,C_1(t)=t, and

    C_(n+1)(t)=(2+t)C_n(t)-C_(n-1)(t)+2t.

The full cycle spectrum, equivalently the Chebyshev recurrence, gives

    C_n(t)=2[T_n(1+t/2)-1]=product_(d|n)D_d(t), D_1(t)=t. (3)

Successive exact polynomial division computes every D_n without numerical
roots or a prime-power assumption.

For 0<=c<=1, t=c^2/N^2, the bound sin(pi/n)>=2/n gives

    lambda_min(H_N(t))>=min(1,16/N^2),
    lambda_max(H_N(t))<=4+1/N^2

whenever the direct sum is nonempty. Hence condition-number growth is at
most quadratic. This is not a zero-location assertion for zeta.

## 2. An explicit infinite regularization constant

Define, continuously at zero,

    f(u)=log(sinh(u/2)/(u/2)),
    F(v)=integral_0^1(1-y)f(vy)dy,
    B(c)=sum_(m>=1)mu(m)F(c/m)/m.                         (4)

Euler's sinh product gives 0<=f(u)<=u^2/24, f'(0)=0 and
0<=f'(u)<=u/12. Also

    f''(u)=1/u^2-1/[4sinh^2(u/2)]>=0.

Therefore (4) converges absolutely, and for every K>=1 its entire tail is
bounded by

    sum_(m>K)|mu(m)F(c/m)/m|<=c^2/(576K^2).              (5)

Expanding the sinh product, putting a=mj and using
sum_(m|a)mu(m)/m=phi(a)/a gives the positive representation

    B(c)=sum_(a>=1)phi(a)/a
       integral_0^1(1-y)log(1+(cy/(2pi a))^2)dy.         (6)

Absolute convergence under the quadratic majorant justifies rearrangement.
Thus B(c)>0 for c>0; as a function of c^2 it is increasing and concave.
For |c|<2pi one also has the full convergent expansion

    B(c)=sum_(j>=1) B_(2j)c^(2j)
      /[2j(2j)!(2j+1)(2j+2)zeta(2j+1)].                (7)

Here B_(2j) are Bernoulli numbers. The first term is
c^2/[288zeta(3)]. No truncation or fitted decimal replaces B in the theorem.

## 3. A logarithmic-error bound for the COMPLETE displacement

### Theorem 2

For every integer N>=2 and every real 0<=c<=1,

    |V_N(c^2/N^2)-log A_N-N^2 B(c)|
                         <=c^2(1+log N)/24.             (8)

This is an unconditional upper bound for the actual radial displacement.
It is not yet a bound for the centered prime error log A_N-(N-1)^2/2.

Proof. First set t=2(cosh h-1), r=exp(-h). Equation (1) gives
D_n(t)=r^(-phi(n))Phi_n(r)^2. Apply the exact identity
log(1-exp(-u))=log u-u/2+f(u) to the full cyclotomic divisor product.
For n>1, sum_(d|n)mu(n/d)=0; the linear term is phi(n) and cancels the
exterior r factor. Consequently

    V_N(t)-log A_N
      =sum_(n=2)^N(N-n)sum_(d|n)mu(n/d)f(hd).           (9)

Put h=b/N and extend g_m(x)=(N-mx)f(bx/N), 0<=x<=N/m, by zero outside
that interval. The right side of (9) is exactly

    sum_(m<=N)mu(m)sum_(d>=1)g_m(d)-(N-1)f(b/N).         (10)

The last term removes the UNIT n=1. Furthermore

    integral_R g_m(x)dx=N^2 F(b/m)/m.                   (11)

The endpoint matters for a sharp comparison. The function g_m is continuous,
g_m'(0)=0, and its derivative jumps by m f(b/m) at L=N/m. In the interior,

    g_m''=-2m(b/N)f'(bx/N)+(N-mx)(b/N)^2 f''(bx/N).

The integrals of these two nonnegative magnitudes are 2m f(b/m) and
m f(b/m), respectively, by integration and f(0)=f'(0)=0. Including the
endpoint jump gives total variation of the measure dg_m' at most

    4m f(b/m)<=b^2/(6m).

Twice integrating the periodic Bernoulli polynomial B_2({x}), whose
absolute supremum is 1/6, proves

    |sum_(d in Z)g_m(d)-integral g_m|
       <=(1/12)total_variation(dg_m')<=b^2/(72m).        (12)

This formula follows from (B_2({x})/2)'=B_1({x}) and
B_1'=1-sum delta_d. It remains valid for nonintegral L: the jump of g_m'
is part of its second distributional derivative. It is not silently set
to zero.

Sum (12) over m<=N, paying |mu(m)|<=1, the complete tail (5), and the
unit term in (10). If H_N^harm=sum_(m<=N)1/m, this gives

    |V_N(2(cosh(b/N)-1))-log A_N-N^2 B(b)|
       <=b^2[H_N^harm/72+1/(24N)+1/576].                (13)

The logarithm, rather than the O(N) cost of first-order quadrature, comes
from the complete second-variation bound.

To obtain the RATIONAL mass c^2/N^2, set b=2N asinh(c/(2N)). Then
0<=b<=c and c-b<=c^3/(24N^2), by integrating
1-(1+x^2)^(-1/2)<=x^2/2. Absolute differentiation in (4) gives
|B'(v)|<=v zeta(3)/144<=v/72, hence
N^2|B(c)-B(b)|<=c^4/1728. A finer rational bound than (8) is therefore

    error<=c^2[H_N^harm/72+1/(24N)+1/576]+c^4/1728.     (14)

Finally H_N^harm<=1+log N and, for N>=2,c<=1,
1/(24N)+1/576+1/1728<=5/216<1/36. This proves (8). QED.

No prime number theorem, proposed quasi-RH strip, Hecke family mean,
or unproved critical moment is used in Theorems 1--2.

## 4. A direct ONE-SIDED positive-matrix height target

Fix one c in (0,1], e.g. c=1. The following statement remains OPEN:

    V_N(c^2/N^2)<=(N-1)^2/2+N^2 B(c)
                    +O_epsilon(N^(3/2+epsilon))
    for every epsilon>0 and every integer N>=2.          (OPEN-PH)

Together with (8), this is equivalent to RH. Unlike #993's displayed
absolute-error target, this asks only for an UPPER bound on one positive
matrix. The arithmetic content is not claimed weaker than RH.

Here is the complete one-sided argument. Let E(x)=C(x)-(x-1)^2/2.
Between integers E is its endpoint interpolation plus
(x-N)(N+1-x)/2<=1/8. Thus an upper estimate at all integers gives one
for all real x. Direct termwise integration gives

    integral_1^infinity E(x)x^(-s-2)dx
      =[-zeta'/zeta(s)-1/(s-1)]/[s(s+1)], Re s>1.       (15)

At every nontrivial zero rho the continued expression has NONZERO residue
-m_rho/[rho(rho+1)]. Its apparent pole at one cancels. It is holomorphic
at every REAL s>0: for 0<s<1 the alternating-series expression for zeta
shows that zeta is nonzero; above one use its Euler product.

For fixed epsilon>0, an upper bound implies that, beyond some x_0,
F(x)=Kx^(3/2+epsilon)-E(x)>=0. Landau's positivity lemma for the Laplace
transform says that a finite convergence abscissa of a nonnegative
function is a singularity at that real point. Apply it after x=exp u.
The transform of F initially converges for Re s>max(1,1/2+epsilon), and
(15) continues it holomorphically at every real s>1/2+epsilon. Its abscissa
is therefore at most 1/2+epsilon. The integral is holomorphic throughout
that half-plane. Subtracting the explicit K term and the finite initial
integral makes (15) holomorphic there as well. Its nonzero zero residues
cannot occur. Choose epsilon separately for each point to get RH by the
functional equation. No rightmost-zero, spacing or simplicity assumption
is made.

For clarity, Landau's elementary proof is as follows. If a nonnegative
Laplace transform is analytic at its finite real convergence abscissa a,
choose a small disk about a and a real b>a inside it. The Taylor series
of F(b-z) has nonnegative coefficients, namely the exponentially weighted
moments divided by factorials. Choose positive z inside its convergence
radius with b-z<a. Tonelli sums these moments to the transform at b-z,
contradicting the definition of a. If the abscissa is minus infinity
there is no obstruction to the conclusion.

Conversely the classical RH bound psi(x)-x=O(sqrt(x)log^2(2x)), followed
by integration, gives the absolute estimate for E, and (8) gives OPEN-PH.
This consumer is for ordinary zeta; arbitrary number fields are not
silently included.

## 5. The drift itself is not a free way to exclude zeros

For 1<Re s<2, its positive representation gives

    integral_0^infinity B(c)c^(-s-1)dc
       =pi(2pi)^(-s)zeta(s)
        /[s(s+1)(s+2)sin(pi s/2)zeta(s+1)].             (16)

Indeed the elementary logarithmic-kernel integral is
pi/[s sin(pi s/2)], the y integral is 1/[(s+1)(s+2)], and
sum phi(a)/a^(s+1)=zeta(s)/zeta(s+1). The initial strip follows from
B(c)=O(c^2) at zero and O(c) at infinity, using f(u)<=min(u^2/24,u/2).
The continuation of (16) has a pole at every rho-1: in -1<Re s<0,
zeta(s) is nonzero by its functional equation and the zero-free Euler
half-plane. The other factors do not cancel the pole. Its order retains
the zero multiplicity. Thus an unproved sharp large-c asymptotic for B
would merely relocate the individual-zero problem. Theorem 2 fixes c
and assumes no such asymptotic.

## 6. The upper bound actually attempted, and its failure

The raw coordinate Hadamard bound is

    log det H_n(t)<=n log[1+(1+t)phi(n)/n-2mu(n)/n].     (17)

This is the EXACT diagonal entry of the rational matrix, not a heuristic
spectrum. Its weighted bound is generally order N^3, not the order N^2
height in OPEN-PH. It cannot close that estimate. Fourier diagonalization
computes the determinant but leaves the arithmetic cancellation over
primitive angles; it does not estimate the centered height.

The Green construction bounds inert-prime mass in a quadratic field,
not this all-prime determinant. Its inequalities cannot be inserted here
without a proved adapter. Positive definiteness and real-rootedness of
D_n concern a different variable from the zeta zeros. Differentiating
(8) is also not justified merely by a bound on its error, and integrating
a resolvent estimate would require an independently controlled normalization.

The route is now a fixed-source, one-sided matrix HEIGHT problem with
explicit rational positive matrices and only logarithmic regularization
cost. The required critical height saving is still missing, not concealed
as a matrix-positivity or source-identification assumption.
