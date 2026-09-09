# A direct global xi attack: exact modular source and complex Laguerre sign

Date: 2026-09-09. **Unsuccessful global proof attempt; RH remains unproved.**
The reductions and the failure mechanism below have complete proposed proofs.
The central sign in (G) is not proved. Independent review is required, including
for the new finite certificate. Classical material is explicitly credited.

## 1. Why the target changes

The repository's arithmetic paths have exact native-source formulas and full-norm
certificates, but still lack the signed critical upper bound. Its graph theorems
control complementary fluctuations, not the native coherent component. The new
#803 compression reduces the dimension of a budgeted minimization without
bounding its distance. It is not an ingredient that proves a small distance.

The safe-axis Xi and high-derivative paths offer another global target, but
#724 still requires the real-critical residue sign AND the boundary Loewner
sign. #765 explicitly corrects raw companion innerness as RH-equivalent and
retains a positive-kernel/tail counterexample to generic reverse-Rolle descent.
None of those open assertions is imported as proved here.

I therefore work directly with the ORIGINAL entire Xi function, without an
optimized coefficient sequence, a new graph, unknown-zero inputs, or a passage
from fixed low-order positivity to arbitrary order. The global sign criterion
below is classical (Jensen/complex Laguerre); it is not a newly discovered or
easier reformulation. The attempted proof concerns its literal theta source.

This is orientation across the cumulative map and selected current branches,
not a fresh exhaustive mathematical audit of every repository packet.

## 2. Original function and the complete modular kernel

Define by analytic continuation

    xi(s) = (1/2)s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
    F(z) = Xi(z) = xi(1/2+iz).

The pole removals are analytic, not pointwise multiplication of totalized poles.
The classical xi function is even, real entire, nonzero, and of order one.
Its zeros lie in |Im z|<1/2. Euler nonvanishing and the functional equation
supply that strip, not an assumption of RH.

For real u put

    Phi(u) = sum_(n>=1) phi_n(u),
    phi_n(u) = [4 pi^2 n^4 exp(9u/2)-6 pi n^2 exp(5u/2)]
                 exp[-pi n^2 exp(2u)].

The COMPLETE sum is even and positive. On u>=0, each summand is positive,
since pi*n^2*exp(2u)>3/2. It and all derivatives decay faster than every
ordinary exponential as u tends to +infinity. Modularity gives the same at
-infinity for the complete sum. The exact Fourier representation is

    F(z) = integral_R Phi(u) exp(izu) du
         = 2 integral_0^infinity Phi(u) cos(zu) du.             (2.1)

These are the standard theta representation and normalization; see Gasper
(2008), Section 3, and Csordas (2014), Section 4. They are reconstructed here
only to fix which source is being attacked.

In detail, theta(x)=sum_(n in Z)exp(-pi*n^2*x) satisfies
 theta(x)=x^(-1/2)theta(1/x).
Thus Q(u)=exp(u/2)theta(exp(2u)) is even, and termwise differentiation gives

    Phi(u) = (Q''(u)-Q(u)/4)/2.                              (2.2)

The constant theta term is annihilated. The positive-index terms give precisely
the two coefficients in phi_n above. Normal convergence near each finite u
justifies every fixed derivative. In particular,

    Phi^(2j+1)(0)=0 for EVERY j>=0.                          (2.3)

These infinitely many exact cancellations matter in the failed attempt below.

## 3. A complete global criterion, with no derivative descent

For z=x+iy define

    L_F(x,y)=|F'(z)|^2-Re(F''(z) conjugate(F(z))).

Elementary differentiation gives

    L_F(x,y)=(1/2) d^2/dy^2 |F(x+iy)|^2.                    (3.1)

**Global target (G):** prove L_F(x,y)>=0 for ALL real x and |y|<=1/2.

(G) implies RH directly. If F(x0+iy0)=0, 0<|y0|<1/2, reality gives the
conjugate zero. The nonnegative convex function U(y)=|F(x0+iy)|^2 has value
zero at both +/-y0; convexity forces it to vanish on the entire segment.
The identity theorem would make F identically zero, a contradiction.
All nontrivial zeros already lie in the band, so they must be real.

Conversely RH implies (G). Under RH, the even order-one canonical product is

    F(z)=F(0) product_(gamma>0)(1-z^2/gamma^2)^(m_gamma).

The product and its derivatives converge locally uniformly. Each finite product
has only real roots. For a real-rooted polynomial P,

    |P(x+iy)|^2 = c^2 product_r [(x-r)^2+y^2]

is a polynomial in y^2 with nonnegative coefficients, and is convex in y.
Taking the locally uniform derivative limit proves (G). This is a direct
specialization of the classical complex Laguerre criterion, not a proof of
its application to Xi.

### The source inequality that would finish

Change variables u=t+s and v=t-s in the product of (2.1) with its conjugate.
All integrals below are absolutely convergent for fixed y. Evenness of Phi
in both directions yields

    |F(x+iy)|^2 = 2 integral_R integral_R
          Phi(t+s)Phi(t-s) cosh(2yt) cos(2xs) dt ds.

Consequently define the NONNEGATIVE, even kernel

    K_y(s)=integral_R t^2 Phi(t+s)Phi(t-s) cosh(2yt) dt.

Then the full original sign is exactly

    **L_F(x,y)=4 integral_R K_y(s) cos(2xs) ds.**             (3.2)

No prime tail, theta tail, cross term or boundary value has been omitted.
The missing assertion is that this cosine transform is nonnegative for every
x and every y in the band. K_y(s)>=0 by itself does NOT prove that assertion.
For example a sum of two translated positive Gaussians has an oscillating
cosine transform. Csordas's associated-kernel work makes this positive-definite
versus pointwise-positive distinction explicit.

This attempted proof does not obtain a sum-of-squares representation of (3.2)
for the actual modular source. Gasper's positive-square representations prove
real zeros for K_{iz}(a) and specified Polya approximants. No identity identifies
those functions with the COMPLETE theta source in (2.1); their conclusions are
not transferred by similarity of their tails or by positive addition.

## 4. Test the finite-source route before using Hurwitz

For an integer N>=1 and a fixed REAL heat parameter lambda define

    Phi_N(u)=sum_(n=1)^N phi_n(u), u>=0,
    F_(N,lambda)(z)=2 integral_0^infinity
                         exp(lambda*u^2) Phi_N(u) cos(zu) du.

Every F_(N,lambda) is real even entire. For lambda=0 these functions converge
locally uniformly to F as N tends to infinity. A real-zero or zero-free-band
property would still need proof before Hurwitz could be used.

### 4.1 No finite raw truncation is globally real-rooted

Put q=pi*n^2. Direct differentiation gives

    phi_n'(0)=exp(-q)(-8q^3+30q^2-15q).                     (4.1)

For n>=2 this is strictly negative: q>4, and
8q^2-30q+15 is positive for q>=4. Modularity (2.3) and termwise differentiation
therefore give, for EVERY finite N>=1,

    a_N:=Phi_N'(0)=-sum_(n>N)phi_n'(0)>0.                   (4.2)

Let G(u)=exp(lambda*u^2)Phi_N(u). Its right derivative at zero is a_N.
G and all its derivatives are integrable with every polynomial weight.
Repeated integration by parts gives along the REAL axis

    F_(N,lambda)(x) = -2a_N/x^2 + O_(N,lambda)(x^-4),
    F_(N,lambda)'(x) = 4a_N/x^3 + O_(N,lambda)(x^-5),
    F_(N,lambda)''(x) = -12a_N/x^4 + O_(N,lambda)(x^-6).

For the derivative statements, apply the same integrations to uG and u^2G,
rather than differentiating an unspecified asymptotic remainder. Hence

    **(F_(N,lambda)')^2-F_(N,lambda)F_(N,lambda)''
                   = -8a_N^2/x^6 + O_(N,lambda)(x^-8)<0**  (4.3)

for all sufficiently large real x. This violates the necessary real Laguerre
inequality for a real-zero entire function of order at most one.

For completeness the order bound needs no zero assumption. The double
exponential exp[-pi exp(2u)] absorbs exp(lambda*u^2); gamma-integral comparison
then bounds log max_(|z|<=R)|F_(N,lambda)(z)| by O_(N,lambda)(R log(R+2)).
If it had finitely many zeros, Hadamard factorization would make it exp(az+b)
times a polynomial. Evenness forces a=0, contradicting its nonzero x^-2
asymptotic. It has infinitely many zeros, only finitely many of them real by
the eventual strict negative sign. It therefore has infinitely many nonreal
zeros. Positivity of the source makes F_(N,lambda)(iy)>0, so none is purely
imaginary. This conclusion concerns these CHANGED functions, not Xi.

This theorem by itself does NOT place those nonreal zeros inside the critical
band. The separate certificate below rejects the stronger attempted band claim
already at N=3, lambda=0. No statement about all N band zeros is inferred.

### 4.2 The omitted source supplies cancellation, not a negligible sign error

For lambda=0 put R_N=F-F_N. At each fixed N its real-axis asymptotics have the
opposite leading terms to F_N:

    R_N(x)=2a_N/x^2+O_N(x^-4),
    R_N'(x)=-4a_N/x^3+O_N(x^-5),
    R_N''(x)=12a_N/x^4+O_N(x^-6).

Indeed all odd derivatives of the FULL even smooth source vanish at zero,
so the complete Fourier transform has no algebraic boundary expansion.
Separately the two real Laguerre numerators both have leading term
-8a_N^2/x^6. Their mixed term

    2F_N'R_N'-F_N R_N''-R_N F_N''

has leading term +16a_N^2/x^6. Thus the leading negative terms cancel exactly.
Deleting the mixed term gives the wrong sign analysis. Keeping it does not
prove the next, much smaller, total is positive.

Absolute tail control is nevertheless available. For |Im z|<=1/2 and j>=0,

 |F^(j)(z)-F_N^(j)(z)| <=
  8*pi^2*2^(-j)*j!*(N+1)^4*exp[-pi*(N+1)^2]
                    /[pi*(N+1)^2-3/2]^(j+1).               (4.4)

Proof: bound phi_n(u) by 4pi^2 n^4 exp(9u/2)exp[-pi*n^2 exp(2u)],
substitute v=exp(2u), and use log v<=v-1 and v^(3/2)<=exp[3(v-1)/2].
The resulting gamma integral gives the sum version with coefficient
4pi^2*2^(-j)j!. For n>=2, its successive summands have ratio at most
(3/2)^4 exp(-5pi)<1/2. Summing that geometric majorant proves (4.4).
The bound is uniform in ALL real x, but is ABSOLUTE, not relative to an
exponentially small oscillating F. It cannot make the sign step automatic.

## 5. One certified zero INSIDE the critical band of F_3

The following is a finite analytic countercertificate to the attempted assertion
that EVERY positive half-line theta truncation is zero-free off the real axis
in |Im z|<1/2. It is not an RH counterexample, a zeta zero computation, or a
numerical argument for the global signs of the full source.

Let z_c be the EXACT Gaussian rational with components

 real: 67.8801896551476196444591034890974615868760577967044779253851906685118397
 imag:  0.4773438417708229856896978584442346997998462219509442426117227298339156

and let r=10^-25. The disk |z-z_c|<r is entirely inside 0<Im z<1/2.
The directed reconstruction encloses F_3(z_c) and F_3'(z_c) and proves

    |F_3(z_c)| < 2*10^-57,
    |F_3'(z_c)| > 17*10^-21,
    sup_(|z-z_c|<=r) |F_3''(z)| <1000.                     (5.1)

Consequently

    |F_3(z_c)|+500r^2 < |F_3'(z_c)|r.                     (5.2)

Rouche applied to F_3 and F_3'(z_c)(z-z_c) proves that the disk contains
exactly ONE zero, counted with multiplicity. In particular it is simple.

### Complete quadrature and analytic tail contract

The checker sums the exact integrands

 [4q^2 exp(9u/2)-6q exp(5u/2)] exp(-q exp(2u)) exp(sign*i*z_c*u),
 q=pi*n^2, n=1,2,3, sign=+1,-1.

Cutoffs are respectively U_1=9/4, U_2=3/2, U_3=1. Each interval is partitioned
into cells of width 1/32: 72+48+32=152 cells. At each rational midpoint,
Taylor coefficients through degree 80 are computed by the exponential-series
recurrence. The scaled cell variable lies in [-1,1]. Its even moments are
integrated EXACTLY; differentiating with respect to z is implemented by
multiplication by sign*i*u, retaining the entire polynomial.

For a Cauchy circle of radius 1/8 about a midpoint, Re(exp(2u))>0, because
|Im u|<=1/8. Thus |exp(-q exp(2u))|<=1. Since |Re z_c|<68 and |Im z_c|<1/2,
each full summand, including its coefficient, is less than 10^13 on that
circle. This last constant is verified independently for each n using
pi<4, e<3, and the explicit U_n: it is bounded by

  4(4n^2)^2 * 3^ceil(5(U_n+1/8)+68/8) < 10^13.

The half-cell to radius ratio is 1/8. Summing all terms and cell lengths
therefore gives complex absolute integral error at most

    e_C = 10^16 (1/8)^81/(1-1/8).

Multiplication by u costs at most another factor three for the derivative.
The code inflates BOTH rectangle components by these bounds.

For each of the three infinite tails, and for derivative orders j=0,1,
u^j<=exp u on u>=0 gives

  2 integral_(U_n)^infinity u^j phi_n(u) exp(u/2)du
    <=4 exp(-q v0)(q v0^2+2v0+2/q), v0=exp(2U_n).

Elementary 8/3<e<3 and 3<pi<4 give qv0>190 and v0<243 in all three cases.
The displayed expression is <9,000,000(3/8)^190<10^-70. The code checks the
last rational inequality and includes MORE than all three tails in the
reported enclosures. No infinite integral is replaced with zero.

For the second derivative, exp(2u)>=1+2u gives everywhere |Im z|<=1/2

  |F_3''(z)| <=256 sum_(n=1)^3 n^4/(6n^2-5)^3 <1000.

This bound is independent of Re z and is evaluated as an exact rational.

### Arithmetic boundary

All interval endpoints are integers divided by 2^384. Addition is exact;
multiplication/division round down/up with integer operations and reject a
zero denominator. Pi uses Machin's formula and alternating arctangent sums
with complete remainder. exp and sine/cosine use halving, convergent Taylor
series with explicit remainder, then exact interval doubling/squaring.
The initial root center was selected by ordinary mpmath reconnaissance;
mpmath values and incomplete gamma are NOT used in this accepting replay.
The certificate proves only the disk claim for F_3. Neither analytic proofs
nor a global claim follow from a count of finite checks.

## 6. Outcome of the global attack

The direct route is

    exact full theta identity (2.1)
    -> full Fourier sign (G), equivalently the sign in (3.2)
    -> vertical convexity on the WHOLE critical band
    -> exclusion of EVERY off-real xi zero
    -> RH.

Only the first and the last two arrows have been justified here. The attempt
to supply (G) from positive finite theta kernels fails concretely at (5.2),
and even every fixed heat modification of a finite truncation fails global
real-rootedness by (4.3). Known positive-square Bessel/Polya formulas do not
identify the actual full modular source. Generic reverse-Rolle descent and
raw-innerness substitution are already excluded by the repository's own work.

The unproved statement is therefore not an error tolerance, a small-rank Gram
floor, an unknown numerical constant, or a source truncation convention. It
is the GLOBAL Fourier-sign inequality for the unchanged Phi. No assertion in
this packet proves it, and no presumed easy review step is assigned its proof.

I have not found a full unconditional proposal in this pass. The record keeps
the attack at the actual global function and rejects one tempting completion;
it should be read as an unsuccessful proof attempt, not advertised as a new
milestone toward an already imminent RH solution.
