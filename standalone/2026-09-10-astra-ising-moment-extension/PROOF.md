# IME26 — moment lifting, an exact degree-twelve ferromagnet, and a finite independent-spin obstruction

Date: 2026-09-10. Proposed component theorems, pending independent mathematical
and code review. **The all-order ferromagnetic realization and RH are not proved.**
This is an add-only continuation of IMR26, PR847 at
`6f3b816e6e8e4eafc0e3bc4dc830267f07f3a44d`.

The contribution is not a general claim that a positive moment vector admits a
ferromagnet. We prove a local next-moment direction, construct the exact theta
jet through degree twelve, and prove that independent spins cannot realize
all of this particular source's moments. A two-spin interacting example shows
why that last obstruction does NOT apply to general ferromagnets.

## 1. Source, notation, and the actual global target

For t>=0 use the COMPLETE series

    phi(t)=sum_(n>=1) [4 pi^2 n^4 exp(9t/2)-6 pi n^2 exp(5t/2)]
                                  exp[-pi n^2 exp(2t)].                (1)

Its even extension is the classical smooth theta Fourier density, by Jacobi
inversion. Put Z=integral_R phi=Xi(0), w=phi/Z, v=mu_2, and

    mu_j=integral_R t^j w(t)dt,
    Xi(z)=xi(1/2+iz)=integral_R exp(izt)phi(t)dt.                        (2)

All exponential moments exist, and odd moments vanish. We do not assume RH.
These classical identities have the same normalization as IMR26. Its accepted
numerical values are NOT imported: Section 8 reconstructs all moments through
14 and three Fourier evaluations from (1), with the entire omitted source paid.

A finite admissible magnetization has the law

    X=sum_i a_i sigma_i,  a_i>=0,
    Prob(sigma) proportional to exp(sum_(i<j) J_ij sigma_i sigma_j),
    sigma_i in {-1,1}, J_ij>=0.                                       (3)

Zero couplings are allowed. Weighted Lee--Yang is a classical input: (3) has
only real Fourier zeros. Newman--Wu, arXiv:1901.06596v2, page 11, (21) and the
following paragraph state precisely this weighted version. Their page 16,
Theorem 16 and (27)--(28), give the broader classical closure context. The
moment-tail argument required here is reproduced in Section 7; its general
mechanism is not claimed new.

Write c_(2r) for the cumulants of a symmetric unit sign. Through order 14:

    1,-2,16,-272,7936,-353792,22368256.                                 (4)

They have sign (-1)^(r-1), for example by expanding the paired product for cosh.
For standardized theta cumulants kappa_(2r) of t/sqrt(v), set

    s_r=kappa_(2r)/c_(2r).                                            (5)

Cumulants are defined by the Taylor series of the logarithm at zero. Only this
local logarithm is used, never a global logarithm across unknown zeros.

## 2. IME1 — a next-moment direction that preserves all earlier moments

Consider independent symmetric signs and an independent standard Gaussian G:

    X(g,x)=sqrt(g)G+sum_(i=1)^r sqrt(x_i) sum_(l=1)^nu_i sigma_il,
    g>=0, x_i>0 distinct, nu_i positive integers.                     (6)

Its even cumulants are

    K_(2k)=g 1_(k=1)+c_(2k) sum_i nu_i x_i^k.                         (7)

Fix the first r cumulants at a point with distinct positive x_i. The Jacobian
in those r variables is [k c_(2k) nu_i x_i^(k-1)]. Its determinant is a
nonzero scalar times product_(i<j)(x_j-x_i). The real analytic implicit
function theorem therefore provides a local curve x(g) preserving all r
cumulants; at g=0 use its one-sided g>=0 part. The weights remain positive
and distinct after reducing the parameter interval if necessary.

**The exact next-moment derivative is**

    d K_(2r+2)/dg = (r+1)|c_(2r+2)| product_i x_i >0.                  (8)

Since lower cumulants remain fixed, (8) is also the derivative of the next
raw even moment. Thus variance can be redistributed to many small spins in
a direction raising the first unmatched moment, while every lower moment
remains unchanged. This is LOCAL: the curve can meet a zero weight or a
collision before reaching a prescribed higher moment.

Proof of (8). Differentiation of (7) gives

    sum_i nu_i x_i^(k-1) x_i' = -1_(k=1)/k, 1<=k<=r.

At each node x_i use its monic root polynomial
p(t)=product_i(t-x_i). The constant term of t^r-p(t) is
(-1)^(r+1) product_i x_i; all other terms have degree between 1 and r-1.
Multiply by nu_i x_i' and sum. Every positive-degree term vanishes and the
constant is multiplied by -1. Hence

    sum_i nu_i x_i^r x_i'=(-1)^r product_i x_i.

Multiplication by (r+1)c_(2r+2) proves (8). QED.

### Finite replacement, rather than an unimplemented Gaussian reservoir

Suppose g>0 and r distinct positive x_i give prescribed first r+1 cumulants
in (6). Replace sqrt(g)G by K independent signs of weight sqrt(g/K).
The power-sum equations now contain g^k/K^(k-1) for k>=2 and g for k=1.
Regard epsilon=1/K as a real parameter. At epsilon=0 their Jacobian in
(g,x_1,...,x_r) has first column (1,0,...,0); its remaining minor has rows
k=2,...,r+1 and columns k nu_i x_i^(k-1). Its determinant is nonzero because
all x_i are distinct and nonzero. The implicit function theorem gives exact
finite replacements for EVERY sufficiently large integer K, with positive
parameters differing from the limit by O(1/K). The threshold may depend on
the exhibited solution. This assertion does not prove existence of a starting
Gaussian solution at arbitrary moment order.

## 3. IME2 — exact theta matching through degree twelve, with 270 spins

Set nu=(256,10,1,1,1,1). Let x* be the unique solution, in the rational box
specified below, of the SIX equations

    sum_(i=0)^5 nu_i x_i^k=s_k,  1<=k<=6.                             (9)

The centers, all exact terminating rationals, are:

```
0.000784100483934504800021164523067768053084801521311093425055476
0.0261028464767228925702550599632506400078323685567327434446549
0.0651834120102568568686597721894087581412131502974407889759052
0.0852279920789717575679293799226624764155747893511433191156653
0.120571177056070609724805507537325348644144706077350482344551
0.267259230200238621330636622812748395131034479251098058303145
```

Every box radius is 10^-16. All six intervals are positive and disjoint, and
lie in (1/2000,1). With independent signs define

    X*=sqrt(v) sum_i sqrt(x_i*) sum_(l=1)^nu_i sigma_il.               (10)

Then EXACTLY

    E (X*)^(2k)=mu_(2k), 1<=k<=6; E (X*)^(2k+1)=0.                  (11)

This is a 270-spin law, not a 270-point quadrature or a 270-root truncation.
Its characteristic function is product_i cos(sqrt(v x_i*)z)^nu_i.

### Certified existence, not substitution of rounded fitted weights

Let F(x) be the left side of (9) minus its exact target, let c be the rational
center, J0=F'(c), and R=J0^(-1), computed by exact rational elimination.
All 36 entries of R J0=I are reconstructed. Directed source intervals and
interval polynomial evaluation prove

    ||R||_infinity < 10^10,
    beta=||R F(c)||_infinity <10^-20,
    L=sup_box ||I-R F'(x)||_infinity <10^-9,
    beta+L*10^-16 <10^-16.                                         (12)

The retained sharper beta is below 1.309*10^-22 and L below 2.206*10^-11.
The norm uses maximum ROW SUM, not maximum entry. The map x -> x-RF(x)
therefore maps the closed box strictly into itself and is a contraction.
Banach proves existence and uniqueness in this box for the ACTUAL full theta
moments; there is no claim of global uniqueness of all positive solutions.
Cumulant addition (7), then the triangular moment/cumulant identities, proves
(11). The exact roots, not the displayed decimal approximations, define (10).

The physical weight approximations are, respectively,

    0.006019407991339916 (256 copies),
    0.03473056544709633  (10 copies),
    0.0548828258335247, 0.06275654818782858,
    0.07464310036163387, 0.11113075788285336.

The accepting receipt stores outward intervals. This model is NOT Xi: since
its lower six cumulants match, its standardized next raw-moment error is

    [E (X*)^14-mu_14]/v^7
       = c_14[sum_i nu_i (x_i*)^7-s_7] in (0.0409,0.0410).            (13)

The earlier four-moment solution is not asserted to be connected to (10) by
a globally certified curve. Gaussian reservoir exploration suggested the new
multiplicities; (12) independently proves the resulting finite construction.

### An explicit strictly ferromagnetic interval, not only an unspecified IFT

For EVERY common pair coupling j in [0,10^-100], the same box contains a unique
weight vector x(j) whose 270-spin COMPLETE GRAPH has all the moments (11).
For j>0 it is connected and strictly ferromagnetic. No 2^270-state enumeration
is needed for this existence theorem; the following analytic bounds include
all states. The tiny interval is a conservative rigorous allowance, not an
estimate of the maximal continuation radius.

Use the STANDARDIZED observable Y_x=sum_i sqrt(x_i)sum_l sigma_il and
H(sigma)=sum_(a<b)sigma_a sigma_b. Throughout the box,

    |Y_x|<270, |H|<=36315<40000,
    |partial_(x_i)Y_x|<10000.

For any real common coupling, differentiating a normalized Gibbs expectation
in j gives covariance with H. For moments M_n=E_j Y_x^n this yields

    |partial_j M_n| <=2*40000*270^n,
    |partial_(x_i) M_n| <=n*10000*270^(n-1),
    |partial_(x_i)partial_j M_n| <=2*40000*n*10000*270^(n-1).          (14)

These bounds are uniform over all real j since the Gibbs law is a probability.
For the cumulant polynomial the sum of absolute coefficients is at most
C_n=n! 2^(n-1). This follows by expanding log(1+sum M_k t^k/k!) and counting
ordered compositions of n, dropping denominators only in an upper bound.
The product rule gives

    |partial_j kappa_n| <=C_n*2*40000*n*270^n,
    |partial_(x_i)partial_j kappa_n|
                          <=C_n*2*40000*n^2*10000*270^(n-1).

For every n<=12 these are less than 10^55; the integer inequality is checked.
Divide even cumulants by c_n, whose absolute value is >=1, to define F_j.
Thus each entry of F_j-F_0 and of its x-Jacobian is bounded by 10^55*j.
The same R as in (12) now has

    beta_j <= beta+||R||_infinity 10^55*j,
    L_j <= L+6||R||_infinity 10^55*j.

For j<=10^-100, beta_j+L_j*10^-16<10^-16 and L_j<10^-8.
The same Banach argument proves the statement for EVERY j in the displayed
interval, including the explicitly specified j=10^-100. These are exact
analytic finite partition sums, not a reported numerical positive-j fit.

## 4. IME3 — why the initially proposed coupling direction was wrong

At IMR26's independent 28-spin solution, use its four standardized squared
weights x=(a,b,c,d), of multiplicities (25,1,1,1). Keep the first FOUR even
moments fixed along any differentiable path of the SAME 28 spins, allowing
individual weights to change and couplings to turn on with J'_(uv)(0)>=0.
Then the first derivative of the standardized tenth moment is NEGATIVE if any
coupling has positive first derivative; it is zero if all do. This is a
first-order statement, not a global no-go or an obstruction to changing size.

Here is an explicit seven-class certificate. At independence, differentiation
of log E exp(hX) in the one edge joining weights A,B gives

    tanh(Ah)tanh(Bh).

Let D_k(A,B) be its derivative of order 2k at h=0, and let e_j be the elementary
symmetric polynomials in a,b,c,d. Define

    lambda_k=5 c_10 (-1)^(4-k)e_(5-k)/(k c_(2k)), 1<=k<=4.

At all four weight nodes the identity

    5 c_10 x^4=sum_(k=1)^4 lambda_k k c_(2k) x^(k-1)

holds, by the monic root polynomial. It eliminates ALL first-order weight
changes from the first-unmatched-cumulant derivative, even when the 25 equal
weights are varied individually. The compensated one-edge derivative is

    Delta(A,B)=D_5(A,B)-sum_(k=1)^4 lambda_k D_k(A,B).                  (15)

The full theta calculation and the old scalar root brackets are reconstructed;
interval evaluation of (15), using the exact tanh coefficients, proves

    -0.030 < Delta(A,B) < -0.009                                     (16)

for all seven edge classes (a,a),(a,b),(a,c),(a,d),(b,c),(b,d),(c,d).
There are no (b,b),(c,c),(d,d) edges because those groups have one spin each.
By linearity, any positive combination moves the tenth moment downward. The
old target error was already NEGATIVE. Thus infinitesimally adding positive
edges to that particular seed is not the promised way to fix its deficit.
The Gaussian/small-spin direction (8) is different and has the opposite sign.
No statement about paths with zero first derivative, or later nonlinear turns,
is inferred from (16).

## 5. IME4 — independent spins cannot realize the theta law at all orders

A finite independent symmetric sign sum X=sum a_i sigma_i, with variance V,
has chi_X(t)=product_i cos(a_i t). The exact triple-angle identity gives

    chi_X(3t)=chi_X(t) product_i[1-4 sin^2(a_i t)].

For every real u, |1-4 sin^2 u|<=1+2u^2<=exp(2u^2): if the left inner
expression is nonnegative it is <=1; otherwise use
sin^2 u<=min(u^2,1)<=(u^2+1)/2. Therefore

    |chi_X(3t)| <= exp(2Vt^2)|chi_X(t)|, ALL real t.                  (17)

This holds at zeros too, without division by a cosine. It also holds with an
independent Gaussian summand: its triple-to-single ratio is exp(-4g t^2),
which only improves the same bound with the total variance.

Any weak limit of such laws with bounded variances satisfies (17), because
characteristic functions converge pointwise. In particular its zero set is
closed under tripling. This elementary statement needs neither Lee--Yang nor
a classification theorem for limits of independent sums.

### A complete actual-theta certificate violates zero tripling

Define the exact rationals

    a=14.13472514173469, b=14.13472514173470,
    q=3(a+b)/2=42.404175425204085.

The defining integrals (1), with all tails included, prove

    5*10^-18 < Xi(a) < 6*10^-18,
   -9*10^-18 < Xi(b) <-8*10^-18,
   -3.0*10^-12 < Xi(q) <-2.9*10^-12.                                (18)

By the intermediate value theorem SOME real zero gamma lies in (a,b). No
claim that it is the first zero, unique in that interval, or simple is needed.
The same source gives Z<1/2 and mu_2<1/20. Cauchy--Schwarz yields

    |Xi'(t)|<=Z sqrt(mu_2)<1/8, all real t.

Every point of [3a,3b] is within 1.5*10^-14 of q. Combining this derivative
bound with (18) proves

    chi_w(gamma)=0, chi_w(3gamma)<-4*10^-12.                         (19)

Thus the actual theta law is NOT a bounded-variance weak limit of independent
weighted spins, even with extra independent Gaussian variance. This does NOT
refute RH or the proposed general ferromagnetic route.

### A quantitative uniform separation

For any independent-spin/Gaussian law of variance V<=1/20,

    sup_(|t|<=43)|chi_X(t)-chi_w(t)| > 10^-22.                         (20)

Otherwise (17), gamma<14.2, and 2*(1/20)*14.2^2<21 imply
4*10^-12 <=(1+exp(21))*10^-22<(1+3^21)*10^-22<4*10^-12,
a contradiction. The constants are deliberately loose and rationally checked.
The finite sign change in (18), not any numerical zero list, supplies (19).

## 6. IME5 — an explicit finite moment obstruction, and a needed interaction size

The following cutoff is sufficient, not claimed earliest or sharp:

**No independent-spin law can satisfy the original IR tolerances at m=256**,
namely errors <=2^-256 in moments 2,4,...,512. The same holds with an independent
Gaussian summand. A general ferromagnet satisfying those tolerances must have

    sum_(i<j) J_ij > 10^-24.                                       (21)

This is TOTAL coupling of the exhibited finite graph, including hidden-spin
edges, not a lower bound on every edge or on the parent rank-one reserve.

Proof of the finite independent obstruction. The assumed second-moment accuracy
and the interval for v imply V<=1/20. For independent spins with Gaussian
variance, coefficientwise comparison of cosh with exp(h^2/2) gives

    E X^(2k)/(2k)! <= (V/2)^k/k!.

No zero theorem is needed for that fact. On |z|<=43 the matched polynomial
error and complete two Taylor tails are bounded respectively by

    2^-256 * 3^43,
    [47^257/257!]/[1-47/258],
    10^100/2^514.                                                (22)

The second uses V*43^2/2<47 and the ratio of successive exponential-series
terms. For the third, all theta coefficients are nonnegative at the real MGF
argument 86, so the tail at 43 is at most 2^-514 M_w(86).
We have M_w(86)=xi(86.5)/Z<10^100 unconditionally: Z>49/100, zeta(86.5)<2,
pi^(-86.5/2)<1, 86.5*85.5/2<4000, and
Gamma(43.25)<1+43! by splitting its defining integral at one and bounding
x^42.25<=x^43 above one. The checker confirms
(800000/49)(1+43!)<10^100. The sum in (22) is <10^-50.
This contradicts (20). No theta moments of order 16 through 512 have been
numerically evaluated; they are bounded analytically by the complete MGF tail.

For (21), Lee--Yang gives the SAME coefficient bound for any finite admissible
ferromagnet, by its even paired canonical product; Section 7 recalls the proof.
Thus its characteristic function is within 10^-50 of chi_w on that disk.
Let S=sum J_ij. Relative to independent signs with the SAME weights, its
Gibbs density is between exp(-2S) and exp(2S). Its characteristic function
therefore differs from the independent one by at most exp(2S)-1.
Also the independent variance sum a_i^2 is no greater than the interacting
variance: all pair correlations in a zero-field ferromagnet are nonnegative.
For a self-contained proof, expand each exp(J sigma_i sigma_j) as
cosh(J)(1+tanh(J)sigma_i sigma_j). The partition sum is a positive sum over
even-degree edge sets, and the pair numerator is a nonnegative sum over sets
with precisely the designated two odd-degree vertices. This includes all graph
cycles and all hidden spins. Nonnegative a_i then prove the variance comparison.
If S<=10^-24, exp(2S)-1<3*10^-24. The independent law would be within
10^-50+3*10^-24<10^-22 of chi_w, contrary to (20). QED.

### Interactions can break (17): a two-spin exact control

Take two equal weights A>0 and common coupling J>0. With r=exp(-2J) in (0,1),

    chi(t)=[cos(2At)+r]/(1+r).

At any real theta with cos(theta)=-r, t=theta/(2A) is a zero, but

    chi(3t)=4r(1-r)>0.                                             (23)

For J=(log2)/2, r=1/2 and chi(3t)=1. This is a legitimate ferromagnet, whose
zeros remain real by Lee--Yang (or directly from |r|<1). The zero-replication
obstruction therefore diagnoses the INDEPENDENT subclass, not the full route.
A two-spin building block is not itself an all-order theta realization.

## 7. What would close RH, and what is NOT proved

For a finite (3), the MGF is even, entire of exponential type and normalized.
Lee--Yang and the paired genus-zero product give

    E exp(hX)=product_j(1+h^2/gamma_j^2),
    sum gamma_j^-2=Var(X)/2.

There is no quadratic exponential factor at exponential type. Elementary
symmetric coefficients are bounded by powers of their total sum divided by
factorial. Thus the coefficient and whole complex bounds are

    E X^(2k)/(2k)! <= (Var(X)/2)^k/k!,
    |E exp(hX)|<=exp(Var(X)|h|^2/2).                                (24)

The product can be infinite despite a finite number of spins. Constants and
zero-variance cases are handled by the empty product. Under convergence of
all theta moments, variances are bounded; the coefficient tail in (24) gives
locally uniform entire convergence to the actual normalized Xi transform.
Hurwitz excludes off-real zeros in the nonzero limit. Hence producing the IR
model for every m would prove RH. This is the previously proposed sufficient
route, not a newly proved membership theorem for all theta moments.

The present result constructs exact matching for r<=6 and forbids a purely
independent completion by an explicit later order. It does not prove a graph
extension theorem at arbitrary order. The local identity (8) and Gaussian
replacement cannot simply be iterated forever: (19)--(22) show that some
continuation must leave their independent/Gaussian class. The interval of
strict positive couplings in Section 3 is far too small to evade (21) at high
order. General interacting moment reachability remains the central OPEN
assertion, not a routine step left to reviewers.

## 8. Complete numerical proof contract

`core.py` adapts the earlier IMR26 outward integer interval primitives and
four-group root-bracketing formulas; it is not an independent backend. SHA and
reading boundaries are in SOURCES.json. New computations are source replays,
not acceptance of earlier artifacts. All arithmetic uses integers/Fractions
and 256-bit outward dyadics. No zeta, gamma, zero, quadrature or eigenvalue
oracle is called in acceptance. Standard-library code alone suffices.

Pi is enclosed by the 96-term Machin arctangent sums with their alternating
remainders. Exponentials use range reduction to [0,1/8], positive terms through
96, a complete geometric remainder, squaring, and reciprocals. Real sine/cosine
use a pi/2 reduction to |u|<=1, checked explicitly, then 101 polynomial terms
and first-omitted factorial bounds. The integer chosen for reduction uses no
floating computation; any integer would preserve the exact identity.

For n=1,2,3,4 integrate to T_n=(2,3/2,1,3/4), using 32,24,16,12 cells of width
1/16. EACH density is expanded to degree 120 at its rational midpoint,
with the exact exponential-of-series recurrence. For moments j=0,2,...,14,
multiply by the WHOLE polynomial t^j, including degrees beyond 120, then
integrate all even monomials over the cell. For each of the three real Fourier
arguments in (18), multiply the two Taylor series and keep total degree 120.

On the complex radius-1/8 circle about every center, Re exp(2t)>0, |t|<3,
Re t<17/8. The sum of absolute prefactors/densities of n<=4 is <10^15; this
loose bound follows from pi<4, e<3 and
sum_(n=1)^4(64n^4+24n^2)3^10<10^15.
The halfwidth/radius ratio is 1/4. A complete moment Taylor error is

    E_c(j)=16*10^15*3^j*4^-121/(1-1/4).                            (25)

For real Fourier arguments |z|<43, use |cos(zt)|<=exp(43/8)<3^6 on the
complex circle, giving E_c(0)*3^6. The harmless factor 16 exceeds the sum of
all interval lengths including even reflection. These are Cauchy-series
remainder bounds, not asymptotic extrapolations.

For EVERY j>=0, t^j<=j! exp(t) on t>=0. With q=pi n^2 and v0=exp(2T_n),
substitution v=exp(2t) and v^(7/4)<=v^2 give

    2 integral_(T_n)^infinity t^j phi_n(t)dt
      <=4 j! exp(-qv0)(q v0^2+2v0+2/q).

The declared endpoints satisfy qv0>150, v0<81, q<64. Hence all four time tails
are bounded by

    E_t(j)=16 j!(64*81^2+163) exp(-150).                            (26)

For the COMPLETE index tail n>=5 the classical elementary substitution yields

    E_i(j)=128*625*2^-j j! exp(-75)/(147/2)^(j+1).                  (27)

Indeed the individual term is at most
4pi^2 2^-j j! n^4 exp(-pi n^2)/(pi n^2-3/2)^(j+1), and its successive ratios
for n>=5 are bounded by (6/5)^4 exp(-33)<1/2. This pays all later indices
at all times. No signed cancellation is used to discard the tail.

The moment interval is enlarged by [-E_c,E_c+E_t+E_i], since phi_n>=0 there.
For real Fourier transforms both sides are enlarged by E_c+E_t(0)+E_i(0),
since cosine can have either sign. Dividing raw moments by positive Z then
feeds cumulant recurrences, the Banach conditions (12), and the derivative
certificates (15). The receipt also reconstructs the exact rational
inequalities in (20)--(22). Finite tests do not machine-prove Lee--Yang,
Hurwitz, Banach, the Gaussian IFT or any claim of all-order reachability.
