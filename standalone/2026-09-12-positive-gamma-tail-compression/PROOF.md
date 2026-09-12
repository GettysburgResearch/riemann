# Positive gamma-tail compression with an explicit growing-order xi error

Date: 2026-09-12. Local labels **RGT26** are proposed research statements, not
canonical acceptance identifiers. **Independent mathematical and implementation
review is required. The Riemann Hypothesis and the vanishing exceptional-zero
defect remain unproved.** No existing source or integrated statement is altered.

## 0. The change of strategy and the actual outcome

The centered gamma papers identify the missing mean, then the missing variance,
of the infinite tail. The endpoint papers show that every fixed centered stage
has a real simple spectral tail but may have finitely many nonreal quartets.
In particular #858 certifies such a quartet at the integer stage N=5. Therefore
neither positivity of the probability law nor an integer-stage interpolation
can be treated as a real-zero theorem.

This continuation replaces the entire omitted gamma tail by a **positive drift
plus a finite sum of independent positive gamma variables**. It is NOT a
probability mixture, not a signed density correction, and not a polynomial
chosen from desired zero locations. A prescribed Gauss--Radau rule matches
2r+1 tail cumulants with r gamma components. The rule is unique in that class
and its first unmatched cumulant has an exact strictly positive deficit.

The main positive result is a fully explicit, simultaneous N/r estimate. With
r=floor(N/4), the normalized reciprocal transform approaches the unchanged xi
function exponentially, on a horizontal strip whose width grows like N/log N,
uniformly over ALL real frequencies. No constants depending on a fixed r are
silently reused when r grows. Exact low-order source parameters and finite
algebra are reconstructed in the companion code; the large-order theorem is
analytic and is not a numerical high-r campaign.

This removes an approximation/finite-positive-source burden. It does not bound
the off-axis zero defect. Section 8 follows the attempted ending all the way to
that unsupplied premise and explains why the positive Laplace remainder does
not itself provide the sign.

Gauss--Radau quadrature, gamma convolution, Stieltjes transforms, Fourier
inversion, and endpoint Watson/Rouche arguments are classical. The packet
claims no external priority for them or an exhaustive novelty survey. The
source-specific construction and constants below are supplied for review.

## 1. The exact arithmetic-probability source

Let independent G_n have gamma shape 2 and rate 1, and set

    X_N = sum_(n=1)^N G_n/n^2,
    X   = sum_(n>=1) G_n/n^2,
    R_N = X-X_N,                     N>=1.                         (1)

All sums are positive, and E X=pi^2/3. Existence follows already from finite
mean. The Biane--Pitman--Yor classical source identity [E1], in this scaling, is

    E (sqrt(X/pi))^s = 2 xi(s),
    E exp(-sX) = (pi sqrt(s)/sinh(pi sqrt(s)))^2.                  (2)

The Mellin identity includes its entire continuation; it is not obtained by
assuming RH. Let f be the density of X, extended as zero on negative x. The
usual theta inversion gives, for x>0,

    f(x)=sum_(n>=1)(4n^4 x-6n^2) exp(-n^2 x),
    f(pi^2/x)=(x/pi)^(5/2) f(x)>0.                               (3)

For h(t)=sqrt(f(pi e^(2t)) f(pi e^(-2t))), the full-line theta convention in
the predecessor gives h=phi/pi. Accordingly,

    Phi(z)=int_R h(t)e^(izt)dt / int_R h(t)dt = Xi(z)/Xi(0),
    Xi(z)=xi(1/2+iz).                                            (4)

The exact gamma/xi identification is imported from [E1]. Its normalization and
reciprocity are retained, not replaced by a random model for primes.

Put b=(N+1)^(-2) and introduce the FINITE positive measure

    sigma_N = sum_(n>N) (2/n^2) delta_(1/n^2),
    m_j = int x^j d sigma_N(x)=2 sum_(n>N)n^(-2j-2),
    tau=m_0.                                                    (5)

It has infinite support in (0,b], no atom at 0, and finite mass tau<=2/N.
Every m_j is an explicit even-zeta value minus a finite rational sum; no
nontrivial zero is needed to define it. The tail Laplace exponent is

    psi(s)=-log E exp(-sR_N)=int log(1+sx)/x d sigma_N(x),
    S(s)=psi'(s)=int (1+sx)^(-1)d sigma_N(x).                     (6)

Use the principal logarithm on Re s>-1/b. This domain is zero-free for the
individual factors and permits differentiation and integration by domination.
The apparent x=0 integrand in (6) has the value s. For comparison, the whole
resolvent can also be written

    S(s)=[pi sqrt(s)coth(pi sqrt(s))-1]/s
                         -2 sum_(n<=N)(n^2+s)^(-1).              (7)

The expression at s=0 is removable; (6), not a square-root branch, is the
controlling analytic definition. Formula (7) is the logarithmic derivative of
the classical product in (2), not a new spectral interpretation of xi.

## 2. RGT1: a unique finite positive tail matching 2r+1 cumulants

For integer r>=1, let p_r be the monic degree-r orthogonal polynomial for
x d sigma_N(x). For r=0 set p_0=1. The moment matrix is positive definite:

    sum_(i,j<r) c_i conjugate(c_j) m_(i+j+1)
       = int x |sum_(i<r)c_i x^i|^2 d sigma_N(x)>0               (8)

for any nonzero coefficient vector. Thus p_r exists uniquely. Its r roots
x_1,...,x_r are distinct and lie strictly in (0,b). To see this without a root
oracle, form the product of its real sign-changing factors inside (0,b).
If there were fewer than r, multiplying p_r by this product would have one
nonzero sign on the support, contradicting orthogonality. Endpoint roots or
nonreal/even-multiplicity roots do not create a sign change; hence all r roots
are simple and interior.

There is a unique quadrature rule

    int P(x)d sigma_N(x) = d P(0)+sum_(j=1)^r w_j P(x_j)
                          for degree(P)<=2r.                   (9)

All weights d,w_j are STRICTLY positive. This is the left Gauss--Radau rule;
its existence and signs are proved here rather than inferred from floating
quadrature. Divide P by x p_r(x); the quotient has degree <=r-1 and integrates
to zero by (8). The remainder has degree <=r and is integrated by its Lagrange
interpolant on 0,x_1,...,x_r. This proves (9). Applying exactness to the square
of each degree-r Lagrange basis polynomial proves its corresponding weight
positive. In particular,

    d=int [p_r(x)/p_r(0)]^2 d sigma_N(x)>0,
    d+sum w_j=tau.                                               (10)

For r=0 the rule is simply d=tau. Define independent variables

    Gamma_j ~ Gamma(shape alpha_j=w_j/x_j, scale x_j),
    Rtilde_(N,r)=d+sum_(j=1)^r Gamma_j.                           (11)

Thus its Laplace exponent and derivative are

    psi_r(s)=d s+sum_j (w_j/x_j)log(1+s x_j),
    S_r(s)=d+sum_j w_j/(1+s x_j).                                (12)

All shapes, scales and drift are positive. It is a convolution law, not a
mixture over different laws. The mean is tau and, for k>=2, the gamma cumulant
formula gives kappa_k(Rtilde)=(k-1)! sum w_j x_j^(k-1). Therefore

    kappa_k(Rtilde_(N,r))=kappa_k(R_N), 1<=k<=2r+1.               (13)

These are cumulants of the positive **gamma tail in x**, not moments or
cumulants of the reciprocal theta density in t. Matching them does not invoke
the Lee--Yang moment-realization result of #842.

### 2.1 Optimal matching order within this finite-component class

Suppose a drift plus r distinct positive gamma scales matches (13). Its
weighted scale measure, including the drift as an atom at 0, matches m_0
through m_(2r). The monic polynomial vanishing at its r positive scales is
orthogonal for x d sigma_N by applying exactness to x^(j+1)p(x), j<r.
It must equal p_r, and then all weights follow uniquely. Fewer positive scales
cannot match these moments, by applying exactness to x times the square of
their vanishing polynomial. Hence (11) is the unique such r-component law.

Set

    E_r=int x p_r(x)^2 d sigma_N(x)>0,
    M=2r+2.                                                     (14)

The first missing moment of the scale measure is exactly E_r: the monic
polynomial x p_r^2 has degree 2r+1, vanishes at all quadrature nodes, and all
its lower-degree terms are integrated exactly. Consequently

    kappa_M(R_N)-kappa_M(Rtilde)=(M-1)! E_r>0.                   (15)

Each m_j lies in Q(pi^2) by the classical even-zeta formula. The coefficients
of p_r therefore lie in that field; its ordered real roots and the weights
are algebraic over it. This is a finite exact parameter specification using
pi and real algebra, not an oracle for unknown xi zeros.

No law in this same r-component class also matches cumulant 2r+2.
This is a parameter-class statement, not a lower bound for arbitrary positive
approximations. Orthogonal minimization and the trial x^r give the complete
bounds

    E_r<=m_(2r+1)<=2/[(4r+3)N^(4r+3)],
    E_r<=tau b^(2r+1).                                         (16)

These bounds cover the entire original tail. They do not use its finite
truncation as primitive data.

### 2.2 One component is completely explicit

Write v=m_1 and w=m_2. Then

    x_1=w/v, w_1=v^2/w, alpha_1=v^3/w^2,
    d=tau-v^2/w,
    E_1=m_3-w^2/v.                                             (17)

Cauchy--Schwarz on the actual infinite measure makes d and E_1 positive.
The first three tail cumulants match exactly. Integral comparison gives

    d ~ 8/(9N), x_1 ~ 3/(5N^2), alpha_1 ~ 50N/27.               (18)

For example the included directed calculation at N=8 yields

    0.1038672837139345023809 < d < 0.1038672837139345023810,
    0.0082201796771761793686 < x_1 < 0.0082201796771761793687,
    15.9554597131608811996568 < alpha_1 < 15.9554597131608811996569.

The exact definitions are (5),(17), not the displayed decimal approximations.
No zeros or optimization fit enter the parameters. The code also encloses
the two-component rules at N=8 and 16 using the complete even-zeta moments.
It does not compute r=floor(N/4) nodes for large N.

## 3. RGT2: exact positive remainder, and its true limitation

On Re s>-1/b, put D_r(s)=product_j(1+s x_j). Then

    S_r(s)-S(s)
      = s^(2r+1)/D_r(s)^2
          * int x p_r(x)^2/(1+sx) d sigma_N(x).                 (19)

**Proof.** Hermite-interpolate (1+sx)^(-1) at 0 once and at each x_j twice.
The interpolant H has degree <=2r. The numerator 1-(1+sx)H(x) vanishes
at those points with those multiplicities, so it is a constant times
x p_r(x)^2. Evaluating at x=-1/s determines the constant; after taking the
difference H-(1+sx)^(-1), it is s^(2r+1)/D_r(s)^2. Integrating H is exact
by (9), giving (19). The s=0 case follows by removal/continuity. This proof
also verifies the sign and the squared denominator.

Integrating (19) along the segment from 0 to s gives

    psi_r(s)-psi(s)=s^M K_r(s),                               (20)
    K_r(s)=int_0^1 t^(M-1)
        [int x p_r(x)^2/(1+stx)d sigma_N(x)]
          /product_j(1+st x_j)^2 dt.

K_r is the Laplace transform of a finite POSITIVE measure k_r on [0,infinity),
with total mass E_r/M. Indeed each denominator is the Laplace transform of
an exponential or shape-two gamma variable of the indicated positive scale;
products are transforms of independent sums. Integrate these laws with the
positive x,t weights in (20). At t=0 use the point mass at 0. Tonelli proves
finite mass and the identity on s>=0; exponential moments extend it to the
stated half-plane.

For every real s>0, therefore,

    E exp(-s Rtilde_(N,r)) < E exp(-s R_N).                       (21)

At s=0 both equal 1. This is a **positive-real Laplace ordering**. It is not a
Fourier ordering, Mellin zero theorem, or order between the physical densities.

### 3.1 A genuine positive-law interpolation, not formal operational calculus

For 0<=theta<=1 let R_theta have drift theta*d, independent gamma components
of shapes theta*alpha_j at scales x_j, and independent original tail components
of shapes 2(1-theta) at scales n^-2 for every n>N. Zero shapes at endpoints
mean deterministic zero, not undefined gamma variables. Its exponent is
psi_theta=(1-theta)psi+theta psi_r. Its mean remains tau.

Let u_theta be the density of X_N+R_theta. In distributions on the real line,
with the sources extended by zero on the negative side,

    partial_theta u_theta = - partial_x^M (k_r*u_theta).        (22)

Taking Laplace transforms gives exactly -s^M K_r(s) times the current transform.
The finite exponential moments and injectivity of Laplace transforms justify
(22); no boundary term is dropped in a half-line formal derivative. Under the
N>=r+2 condition below, the same vertical-line bound gives integrable Fourier
transforms after M derivatives, so an ordinary continuous representative is
available for the right-hand side as well.

Although k_r is positive, its even derivative is not a positivity-preserving
operator. For example the fourth derivative of exp(-x^2) is positive at 0 and
negative at 1. Accordingly (22) is not a defect-dissipation inequality. This
is exactly the point where a tempting generic completion argument stops.

## 4. RGT3: an explicit full-density error with order growing in N

Assume N>=r+2 and put J=r+2, so M=2J-2. Let u_(N,r) be the density of
X_N+Rtilde_(N,r). Then, for ALL x>=0,

    |u_(N,r)(x)-f(x)| <= epsilon_(N,r) exp(-x/2),                (23)
    epsilon_(N,r) = 64 E_r J^(4J-2)/M.

Both functions vanish on x<0. In particular the estimate includes x below
the positive drift, where the approximating density is identically zero.
There is no omitted small-x collar or future tail.

**Proof using a tilted Fourier inversion.** Let H_N(s)=product_(n<=N)
(1+s/n^2)^(-2). On s=-1/2+iu, every factor 1+stx with x<=b obeys
|1+stx|>=1-b/2. From (20),

    |psi_r(s)-psi(s)|
       <= E_r |s|^M/[M(1-b/2)^(2r+1)]
       <= 2 E_r |s|^M/M.                                     (24)

For the last inequality use r<=N-2, b=(N+1)^(-2), and
-log(1-b/2)<=b/[2(1-b/2)]. Its product with 2r+1 is less than 1/2;
exp(1/2)<2. These are uniform N/r estimates.

The interpolated positive laws give

    |exp(-psi_theta(s))| <= E exp(R_theta/2)
       <= exp[tau/(2(1-b/2))] < 4.                            (25)

The last bound holds for N>=2 from tau<=2/N. Apply the exact identity
exp(-psi_r)-exp(-psi)=-int_0^1(psi_r-psi)exp(-psi_theta)dtheta.
Consequently the difference of full transforms is bounded by
8 E_r |s|^M |H_N(s)|/M.

The first gamma factor and a telescoping upper product give H_N(-1/2)<=16.
Factoring out its value on the real line and retaining only the first J of
its normalized factors gives

    |H_N(-1/2+iu)| <=16(1+u^2/J^4)^(-J).                       (26)

Indeed n^2-1/2<=J^2 for n<=J; all omitted normalized factors have modulus
at most one. Moreover

    |s|^M=(u^2+1/4)^(J-1)
               <=J^(4J-4)(1+u^2/J^4)^(J-1).

The complete u integral is bounded using
int_R(1+u^2/J^4)^(-1)du=pi J^2. Multiplication by 1/(2pi) in Fourier inversion
gives exactly 64 E_r J^(4J-2)/M. The inversion is that of the integrable
functions exp(x/2)u_(N,r)(x) and exp(x/2)f(x), not an unexplained complex
contour shift. Their transform difference is L1 by (26), and their densities
are continuous by convolution with the head. This proves (23) pointwise. QED.

For N>=24 choose r=floor(N/4). Now J<=N/3 and 4r+6>=N+2. Inserting (16),

    epsilon_(N,r)
       <=128 J^(4r+6)/[(2r+2)(4r+3)N^(4r+3)]
       <=16 N^3 3^(-N).                                     (27)

There is no fixed-order remainder constant hidden in (27). It holds at the
stated simultaneous growing order. Computing those parameters to sufficient
accuracy may still be difficult; no bit-complexity or conditioning theorem
is asserted by a bound on the number of gamma components.

## 5. RGT4: the entire reciprocal source, normalization and exponential convergence

Define, using the positive real square root,

    h_(N,r)(t)=sqrt(u_(N,r)(pi e^(2t)) u_(N,r)(pi e^(-2t))),
    Z_(N,r)=int_R h_(N,r)(t)dt,
    F_(N,r)(z)=Z_(N,r)^(-1)int_R h_(N,r)(t)e^(izt)dt.          (28)

It is positive on |t|<T_(N,r)=log(pi/d)/2 and zero outside that interval.
Thus F_(N,r) is real even entire and F_(N,r)(0)=1. Notice that r=0 recovers
the centered family, NOT the raw Bessel N=1 family.

### 5.1 Common envelopes, including the normalizing lower bound

Separate the first Gamma(2,1) component from Y=X_N+Rtilde and write Y=G_1+V.
Balance of the first cumulant gives

    E V=pi^2/3-2<13/10.

Every remaining head gamma scale is <=1/4, and every tail quadrature scale
is <=b. Since -log(1-x)/x<=1/(1-b) for x<=b,

    E e^V <=4 exp(tau/(1-b)) <=64.                              (29)

The factor 4 bounds product_(n>=2)(1-n^-2)^(-2). The crude bound tau<=2/N
and b<=1/4 imply the last bound (exp(8/3)<16). The limiting source also
satisfies (29). Convolution with G_1 therefore gives, for x>=0,

    u_(N,r)(x), f(x) <=64 x e^(-x).                             (30)

On the other hand Markov gives P(V<=13/5)>1/2. For 3<=x<=4 and on this
event, 2/5<=x-V<=4, and (x-V)e^(-(x-V))>1/16. Thus both densities exceed
1/32 throughout [3,4]. For |t|<=1/100 the two arguments pi e^(+-2t) lie
in [3,4], by elementary bounds on pi and exp. Hence

    Z_(N,r), Z_infinity >1/1600,
    h_(N,r)(t), h(t) <=256 exp[-3 cosh(2t)].                    (31)

These constants are independent of N and r. All endpoint and infinite-tail
estimates below therefore survive normalization.

### 5.2 The square-root projection loses at most a square root in the error

For nonnegative a,b, |sqrt(a)-sqrt(b)|<=sqrt(|a-b|). Applying this twice,
using (23),(30) at x=pi e^(2t), y=pi e^(-2t), gives

    |h_(N,r)(t)-h(t)|
       <=32 sqrt(epsilon_(N,r))
                   exp[|t|-(3/2)cosh(2t)].                   (32)

This remains true at and beyond the new support endpoints, where one density
vanishes. No relative error near a small source value is assumed.

For a>=0 define I_a=int_R exp[a|t|-(3/2)cosh(2t)]dt. Elementary maximization
after using cosh(2t)>=e^(2|t|)/2 proves

    I_a <=3[2(a+2)]^(a/2).                                  (33)

For detail, split exp[-3e^(2|t|)/4] into two factors. The supremum of
exp[a|t|-3e^(2|t|)/8] is at most [2(a+2)]^(a/2). The integral of the remaining
factor is below 3, because e^(2|t|)>=1+2|t|. This proves (33) also at a=0.

Since |t|^k<=k!e^|t|, equations (31)--(33), including the difference of the
two normalizers, give for EVERY R>=0 and integer k>=0,

    sup_(|Im z|<=R) |F_(N,r)^(k)(z)-Phi^(k)(z)|
      <=2^40 k! (2R+8)^((R+2)/2) sqrt(epsilon_(N,r)).           (34)

For completeness the raw differentiated error is at most
32 sqrt(epsilon) k! I_(R+2), the normalizer difference is at most
32 sqrt(epsilon) I_1, and |Phi^(k)|<=409600 k! I_(R+1).
After division by Z_(N,r), use I_1<9 and
I_(R+1),I_(R+2)<=3(2R+8)^((R+2)/2). The remaining numerical factor is
51200*3*(1+409600*9)<2^40. No unknown numerical normalization is used.

The bound is uniform over every real frequency, not just on a compact disk.
It is an ABSOLUTE approximation: it does not give a relative estimate near
a zero or an exponentially small value of xi.

### 5.3 An evaluated growing-strip theorem

For N>=24, r=floor(N/4), (27),(34) imply

    error <=2^42 k! N^(3/2) (2R+8)^((R+2)/2) 3^(-N/2).        (35)

In particular, for N>=1024 put R_N=N/[16 log(N+3)]. Then

    sup_(|Im z|<=R_N) |F_(N,floor(N/4))^(k)(z)-Phi^(k)(z)|
                           <= k! exp(-N/4).                   (36)

Here the threshold 1024 is an explicit ANALYTIC bound, not a numerically
verified zero-census height. To check it, log(2R_N+8)<=2log(N+3), log3>1,
and 42log2<30 give the logarithm of (35)/k! at most

    30+(7/2)log(N+3)-7N/16.

For N>=1024, log(N+3)<=sqrt(N) and 30+(7/2)sqrt(N)<=3N/16. The first follows
from a check at 1024 and increasing sqrt(x)-log(x+3); the second is an
increasing positive quadratic in sqrt(N) from 32 onward. This proves (36)
without substituting a fixed-R big-O constant at a growing R.

The theorem preserves the exact source limit and positivity using N head
gammas, r additional gammas, and one deterministic drift. It is NOT a claim
that a full Fourier zero computation at those N has been performed.

## 6. RGT5: the finite-defect geometry survives this new family

Fix N,r. Removing its positive drift, Y is a finite independent gamma sum
with total shape A=2N+sum alpha_j and finitely many positive rates lambda_i.
Gamma--Dirichlet change of variables, with arbitrary positive shapes, gives

    u_(N,r)(d+x)=C x^(A-1) ell(x),
    ell(x)=E exp(-x sum lambda_i U_i), x>0,                     (37)

where U has the corresponding Dirichlet law and C>0. The linear average of
rates lies in a finite real interval. Thus ell is entire and positive on the
real axis. Multiplying by exp((lambda_min+lambda_max)x/2) makes its real part
positive when |Im x|<pi/(lambda_max-lambda_min). At equal rates it is zero-free
everywhere. This proves an analytic zero-free tube, not just real positivity.

With T=log(pi/d)/2, factor the two vanishing endpoint arguments as in the
centered source papers. Analytic logarithms of ell and sinh(v)/v on a small
simply connected tube about [-T,T] give

    h_(N,r)(t)=(T^2-t^2)^((A-1)/2) B_(N,r)(t),                 (38)

where B is even, real, positive and analytic/nonvanishing on that tube.
The fractional powers at the endpoints remain explicit.

The endpoint theorem proved in #858 and #862 now applies with beta=(A-1)/2:
for each FIXED N,r, every sufficiently large zero in the entire complex plane
is real and simple. There are only finitely many nonreal quartets. Its proof
uses the two oscillatory endpoints in the near-real sector and one dominant
endpoint in the near-imaginary sector; Rouche gives one zero in each late
conjugation-invariant disk, forcing exact reality. This is an application of
the inherited endpoint lemma with a new positive-shape source, not another
independent discovery of that lemma. No exterior radius uniform in N,r is
claimed. The component rates, shapes and endpoint exponents vary with N,r.

### 6.1 A uniform inverse-square zero tail does not remove the exceptions

The common envelope (31) gives uniformly

    |F_(N,r)(z)| <= C exp[C|z| log(2+|z|)]                       (39)

for a fixed explicit-able C: maximize |z||t|-e^(2|t|) and integrate the
remaining double-exponential factor, just as in (33). It also bounds the first
absolute moment uniformly. Hence all these normalized functions share a small
zero-free disk about 0, by |e^(izt)-1|<=|z||t|e^(|z||t|).

Jensen on radii R,2R gives a uniform zero count <=C'(1+R log(2+R)). Partial
summation then bounds the full inverse-square tail by
C''(1+log(2+R))/R. This includes every multiplicity. Local uniform convergence
from (34) and Rouche matching of zero clusters therefore extend #862's argument
to the new diagonal family, including multiple real limiting zeros.

## 7. RGT6: what the defect and its repair now mean

For one representative a+ib, a,b>0, of each distinct nonreal quartet, with
its analytic multiplicity, set

    Delta_(N,r)=sum m b^2/(a^2+b^2)^2.                          (40)

The sum is finite for each N,r by (38). There are no imaginary-axis zeros,
because F_(N,r)(iy)>0. The even genus-zero product in z^2 has no omitted
exponential factor. Replace each conjugate pair factor by its real radial
factor. The identity

    (1-z^2/rho^2)(1-z^2/bar(rho)^2)
       -(1-z^2/|rho|^2)^2=4(Im rho)^2 z^2/|rho|^4              (41)

and the uniform inverse-square budget give exactly the finite-repair bound
from #862, with a uniform constant. The repaired function need not remain a
positive-density Fourier transform; that is distinct from the positive gamma
compression proved here.

Define J_(N,r)(a) to be the circular average of log|F_(N,r)(a e^(i theta))|,
and mu_(2,N,r) the variance of h_(N,r)/Z_(N,r). The same complete Jensen
calculation gives

    Delta_(N,r)=(1/2)int_0^infinity J_(N,r)(a)da/a^3
                                       -mu_(2,N,r)/8.          (42)

Consequently, along r=floor(N/4),

    Delta_(N,r) -> Delta_xi,
    RH iff Delta_xi=0 iff Delta_(N,r)->0.                      (43)

This uses weighted zero-cluster convergence and the UNIFORM complete tail in
Section 6.1, not an exchange of the fixed-stage exterior cutoff with N.
Every term of Delta_xi is nonnegative and an off-axis zero would contribute
strictly positively. The exact coefficient 1/4 in its all-zero definition
and all multiplicities are as in #862.

Neither Delta_(N,r) nor its Jensen integral was computed in this packet.
Equation (43) identifies the necessary target; it does not evaluate its limit.

## 8. The attempted completion, and the exact point still open

The new positive remainder might suggest a monotone-defect argument:

    positive quadrature -> positive remainder -> decreasing Delta -> 0.

The second arrow has not been proved; (19)--(22) do not provide a proof of it.
Positivity there belongs to a Stieltjes/Laplace variable before a high-order
spatial derivative and the nonlinear reciprocal square root. The generator in
(22) changes sign even on elementary positive inputs. No sign for its action
on the circular logarithmic mean in (42) follows.

Nor does exponential approximation force real zeros. If Phi had a nonreal zero
z0 of multiplicity m, on any sufficiently small off-axis disk where Phi has a
nonzero boundary minimum, (36) would force exactly m approximant zeros in
that disk for all sufficiently large N. Improved accuracy follows a hypothetical
bad zero more faithfully; it does not exclude that zero.

The N=5 centered certificate in #858 is a required warning, and the r=0 member
of (28) is precisely that centered family. It does not refute possible zero
confinement at the growing r used in (36), nor has such confinement been proved.
A literal-source estimate is still needed, for example

    (1/2)int_0^infinity J_(N,floor(N/4))(a)da/a^3
                              -mu_(2,N,floor(N/4))/8 = o(1).   (OPEN-RGT)

The full implication to RH is (41)--(43) plus Hurwitz, or directly the
nonnegative limiting zero sum. OPEN-RGT is the missing mathematics, not a
routine check left to reviewers. No new complete RH proof is submitted.

### 8.1 RGT7: rapid positive compression can have a nonreal limiting target

Here is a stress test in the SAME positive gamma class, rather than an unrelated
polynomial model. It uses the named complete disk certificate CG4 in #855 as
an inherited proposed numerical input; no fresh replay of that certificate is
claimed. RGT1--RGT6 do not require this numerical input.

For independent shape-two rate-one gammas define, for 0<eta<=7/10,

    Z_eta=G_1+G_2/4+(7/90)G_3
                           +eta sum_(n>=4)G_n/n^2.             (44)

This is a CHANGED source, not the native integer-square law (1). In particular
its third coefficient is 7/90 instead of 1/9. It is not asserted to be a small
perturbation of the actual infinite xi source. Take its reciprocal projection
and normalization exactly as in (28), and call the entire limit Phi_eta.

As eta decreases to zero, its density converges pointwise, in fact uniformly,
to that of Z_0=G_1+G_2/4+(7/90)G_3. The first gamma density is globally
1-Lipschitz, and convolution preserves that bound, so the uniform density
error is at most eta*tau_3. All these laws satisfy the same envelopes and
normalizing lower bound (31): each coefficient is at most its native n^-2
value. Dominated convergence gives locally uniform Fourier convergence,
indeed uniform convergence on each fixed full horizontal strip.

CG4 asserts exactly one simple zero of the reciprocal transform of Z_0 in
the radius-10^-12 disk about the exact terminating center

    26.8135855368140614010181412691765400069731
       +0.4209949404628029929584207065487732398251 i.            (45)

The parent's exact receipt and CERTIFICATE.md give the stronger boundary
lower bound |I_0(z)|>10^-22 for the UNNORMALIZED half-line cosine integral.
That inherited numerical premise is source-pinned in SOURCES.json; it was
not regenerated by a fresh defining-integral calculation in this pass.

We can give an explicit perturbation allowance. Since f_0 is 1-Lipschitz and
eta*tau_3<eta, while both densities obey 64x e^-x, the square-root inequality
on t>=0 gives, for |Im z|<=1/2,

    |I_eta(z)-I_0(z)|
     <=16 sqrt(eta) [int_0^infinity e^(3t/2-3e^(2t)/2)dt
                                  +int_0^infinity e^(-t/2)dt]
     <48 sqrt(eta).

The first integral is less than 2/3 by e^(2t)>=1+2t, and the second is two.
These are COMPLETE time integrals. In particular for EVERY

    0<eta<=2^-256,
    |I_eta-I_0|<48*2^-128<10^-30<10^-22

on the circle in (45). Rouche gives exactly one simple zero in the same disk.
Thus eta=2^-256 specifies an explicit changed infinite positive gamma law
with a critical-band nonreal quartet. This is an analytic transfer of the
inherited disk certificate, not a new direct numerical integration or a zero
of xi. The zero has Im z>2/5 and |z|<27,
so the corresponding full quartet contributes more than

    4/(25*27^4) > 1/10^7                                      (46)

to the weighted defect. The disk is strictly inside the xi critical band.

Nevertheless, the entire positive Radau construction and exponential error
mechanism persist for Z_eta. At N>=3 the remaining scale measure has moments
eta^(j+1)m_j. Its Radau nodes, weights and drift are eta*x_j, eta*w_j and
eta*d, its gamma shapes are unchanged, and

    E_r^(eta)=eta^(2r+2) E_r.                                 (47)

All 2r+1 cumulants still match exactly; the positive remainder (19)--(22)
remains valid. For the modified finite head each scale lies between eta/n^2
and 1/n^2, so (26) becomes

    |H_N^(eta)(-1/2+iu)|
              <=16(1+eta^2 u^2/J^4)^(-J).

The same complete inversion has integral scale J^2/eta and power cost
eta^(-2J+2). Combining with (47) gives a density error at most

    eta^(-1) epsilon_(N,r) exp(-x/2).                          (48)

All geometric-mean and normalization constants remain as before. Thus on the
very SAME growing strip R_N, for N>=1024,

    sup |F_(N,floor(N/4))^(eta,k)-Phi_eta^(k)|
                      <=eta^(-1/2) k! exp(-N/4).               (49)

For each fixed 0<eta<=2^-256 this still converges exponentially. The exceptional
weighted defects converge to a value exceeding (46), by the same uniform
zero-tail argument. This disproves a UNIVERSAL finishing principle based only
on positive gamma structure, exact finite cumulant matching, positive Laplace
remainder and exponential whole-source approximation. It does not disprove
OPEN-RGT for the unmodified coefficient sequence. The exact native rates,
not merely their squared growth or these approximation properties, must enter
an additional zero-defect argument.

The exact tests verify the Radau rescaling, the inherited rational margin's
coarse bound, the explicit 48*2^-128 allowance and (46). They do not regenerate
the parent's defining-integral enclosures or numerically approximate Phi_eta.
The logical dependency on the original CG4 numerical theorem remains explicit.

### Why the relevant concurrent work changes the research plan

* The historical #144 description already connects positive-anchor xi work to
  Stieltjes/Gauss--Radau methods. This is not the first mention of those tools
  in the repository. Here their input is the unconditional explicit positive
  gamma-scale measure (5), not an assumed positive representation for the
  unknown xi zero power sums. Only that PR description was read in this pass.

* #858 and #862 overlap in endpoint reality and finite Hankel index. Their
  conclusions are retained once, not counted as separate proof votes. Their
  N-dependent exterior radii cannot be combined with a convergence rate as
  though they were uniform.
* #842 at its locked ten-moment head gives a proposed actual positive-pair
  ferromagnetic realization and fixed-order higher directions. Those are theta
  moments after normalization, whereas (13) matches gamma-tail cumulants before
  reciprocal projection. No adapter identifies the two. All-order Lee--Yang
  realization is still a different open theorem.
* #859/#860 have two different branching high-height proofs and receipts,
  including different control of the remainder. Only their descriptions were
  read for orientation; no branching theorem is an input here. The overlapping
  path/label in the alternative versions requires reconciliation, not pooling.
* #856 reports failure of the previously proposed native phase inequality;
  this is another reason not to assume that a positive companion supplies a
  global zero-excluding orientation. Its numerical campaign was not replayed.

The useful next analytical target is a source-specific logarithmic-mean
inequality exploiting the exact quadrature remainder before absolute values,
or a justified link to the growing-order ferromagnetic construction. The
current new advantage is a prescribed, positive, exponentially accurate source
with evaluated N/r constants, not an unproved universal stability principle.

## 9. Numerical and attribution boundary

The code reconstructs exact finite Radau resolvent identities, the first lost
cumulant, 36 complete even-zeta tail-moment enclosures and separate
Euler--Maclaurin overlaps, six actual one-component parameters, two actual
two-component rules, finite gamma moment identities, and the displayed
large-order error BOUNDS. It never numerically evaluates a new F_(N,r), a
new Fourier zero, a defect, or a high-r quadrature rule. The large-order
existence and convergence results depend on the written proof, not a sweep.

All arithmetic in the accepting program uses integers, Fractions and outward
320-bit dyadics. Pi is enclosed by Machin/alternating series, and even zeta
values by the classical Bernoulli formula [E3]. The independent complete
Euler--Maclaurin tail uses the periodic-Bernoulli remainder, not a finite
partial sum as the whole tail. The two primitive routes are same-author
calculations, not an independent referee or full numerical backend.

Sources and exact reading depths are in SOURCES.json. Existing proofs remain
proposed at their own scopes; the source readings are not silently new
acceptance of their complete programs or conclusions.

[E1] P. Biane, J. Pitman, M. Yor, *Probability laws related to the Jacobi theta
and Riemann zeta functions, and Brownian excursions*, Bull. AMS 38 (2001),
435--465; https://arxiv.org/abs/math/9912170 . Proposition 1 and Section 2.1,
including the shape-h gamma series and its scaling, are the imported source.
Those text passages and their page images were inspected. No full independent
reproof or external novelty claim is made.

[E2] Classical Gauss/Radau quadrature and orthogonal polynomials. NIST DLMF
3.5, https://dlmf.nist.gov/3.5 , provides the quadrature background. The
endpoint-Radau construction, weights, uniqueness and rational error identity
actually used here are proved in Sections 2--3, not imported without their
hypotheses. Related published Gauss--Radau error theory is discussed in
Alahmadi--Pranic--Reichel, JCAM 396 (2021), 113604,
https://doi.org/10.1016/j.cam.2021.113604 . The article's abstract/context was
inspected, not its complete proof corpus.

[E3] NIST DLMF 25.6.2, https://dlmf.nist.gov/25.6#E2 , for even zeta values;
24.8.1 for the complete periodic-Bernoulli Fourier bound; 2.10 for classical
Euler--Maclaurin with its complete periodic remainder. The finite formulas used are described in the checker.

[E4] The endpoint lemma is from the source-locked #858/#862 proofs, with
classical complex Watson background https://dlmf.nist.gov/2.4#i . Section 6
checks the new family satisfies its hypotheses; it does not claim a new
uniform spectral threshold or the reality of the remaining finite zeros.
