# NGR26: globally admissible native feedback without losing zero detection

Date: 2026-09-10. Status: proposed component proofs; independent review pending.
**No proof of RH or subexponential feedback-energy bound is claimed.**
Parent: PR #838, 459c3f78b3dc8c95ae6cc7b1bec0154499d76c9f.

This is a continuation on the actual factorial/Mobius source. The new construction
removes an all-order square-integrability assumption from polynomial feedback,
without paying an exponential-in-horizon loss at any fixed hypothetical zero.
It does not bound the resulting norms at the strength required to conclude RH.
Gamma convolution, Young's inequality, Hardy evaluation and ridge minimization
are classical. No external priority is asserted for the construction or criteria.

## 1. Exact input, coordinates and the issue being addressed

Fix an integer Y>=1, Q=Y+1 and L=log Q. Let p_j(s)=sum_n a_jn n^(-s),
1<=j<=J, be a finite bank of real Dirichlet polynomials satisfying

    a_jn=mu(n) for n<=Y,             p_j(1)=0.                 (1)

They can additionally have p_j'(1)=1 and p_j(0)=-2, as does the literal triple
in the parent. The new regularization needs only (1). Put

    A_j(x)=sum_n a_jn floor(x/n),  F_j(s)=1-zeta(s)p_j(s),
    f_j(t)=exp(-t/2)[1-A_j(exp t)]  for t>=0,
    e(t)=exp(-t/2)  for t>=0.                                (2)

All functions are zero at negative times. With s=z+1/2, Laplace transformation
is Lf(z)=integral_0^infinity exp(-zt)f(t)dt. Its Hardy norm has boundary
factor 1/(2pi). Balance in (1) makes A_j=-sum a_jn {x/n}. Thus, for

    B=max_j(1+sum_n |a_jn|),

one has |f_j(t)|<=B exp(-t/2). Ordinary Mobius inversion gives f_j=0 before L.
In particular f_j belongs to L1 and L2. Direct floor integration and analytic
uniqueness give the ACTUAL source identity

    Lf_j(z)=F_j(s)/s,                     Re z>0.             (3)

The pole of zeta at 1 is removed by p_j(1)=0. No raw meromorphic boundary value
is assigned an L2 source without construction.

Let P(w)=sum_alpha c_alpha w^alpha be a polynomial with no terms below total
degree m>=1, maximum degree D>=m, and

    P(1,...,1)=sum_alpha c_alpha=1.                           (4)

The raw feedback R(s)=P(F_1(s),...,F_J(s)) has an absolutely convergent
Dirichlet expansion in Re s>1, supported on n>=Q^m. Its locally finite
summatory source need not be known to have finite critical L2 norm. Section 7
shows why all pure powers cannot simply be declared admissible for free.

## 2. An order-matched gamma regularizer

Use the integer degree D BOTH as shape and rate:

    gamma_D(t)=D^D t^(D-1) exp(-Dt)/(D-1)!,   t>=0,
    M_D(z)=L gamma_D(z)=[D/(D+z)]^D.                         (5)

Its mass is 1, mean is 1 and variance is 1/D. Crucially the rate is not fixed
while the order grows. A fixed-rate gamma family would move its mean by order D
and could attenuate a fixed zero exponentially in D.

For 1<=k<=D define a finite signed stable kernel

    v_Dk(t)=D^D exp(-Dt)
       sum_(j=0)^(k-1) binom(k-1,j)(1/2-D)^j
                     t^(D-k+j)/(D-k+j)!,  t>=0.            (6)

It is an ordinary L1 function, with

    L v_Dk(z)=M_D(z)(z+1/2)^(k-1),
    ||v_Dk||_1 <= (2D-1/2)^(k-1).                           (7)

Indeed expand (z+1/2)=(z+D)+(1/2-D) and invert each proper rational term.
For the norm bound integrate the absolute values of the coefficients in (6):

    D^(k-1) sum_j binom(k-1,j)[(D-1/2)/D]^j
                  =(2D-1/2)^(k-1).

There is no uncancelled derivative of a Dirac mass: the numerator degree is
at most D-1. Coefficient absolute values are used only for this explicit upper
bound, not to replace a signed arithmetic identity.

**NGR1 (unconditional all-degree admissibility).** Define

    u_P = sum_alpha c_alpha v_D,|alpha| * f_1^(*alpha_1)
                                          *...*f_J^(*alpha_J). (8)

Each term is a convolution of L1 functions with at least one L2 factor.
Therefore u_P is in L1 intersect L2, vanishes for t<mL, and satisfies

    L u_P(z)=M_D(z) P(F_1(s),...,F_J(s))/s,  Re z>0.          (9)

No zeta moment estimate, Lindelof hypothesis, RH or numerical zero enters this
assertion. It holds for every finite polynomial (4), with arbitrary coefficient
size and any D>=m. It is NOT an assertion that its norm is small.

For an explicit bound put M=max_j||f_j||_1 and V=max_j||f_j||_2. Repeated Young
inequalities and (7) give

    ||u_P||_2 <= V sum_alpha |c_alpha|
                            [(2D-1/2)M]^(|alpha|-1).        (10)

Both M and V are finite, for example M<=2B and V<=B. The parent's small-seed
certificate can improve V for its specific bank, but is NOT required for NGR1
and is not reexecuted in this packet.

Equation (9) is first checked from (3) on a safe half-plane, or directly from
the L1 transforms, and then holds on Re z>0. The Dirichlet-series raw residual
and (8) agree after gamma smoothing locally: a locally finite sum of the
corresponding delayed g_D sources gives the same transform on the initial
half-plane. This is not a claim that the UNSMOOTHED residual belongs to L2.

## 3. A bounded source map and a target which does not disappear

Let

    g_D=gamma_D*e,                   y_P=g_D-u_P.           (11)

Then y_P=g_D on [0,mL). These targets are not the original e; that change is
retained exactly throughout the argument.

The literal factorial source is

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)],
    Ld(z)=(s-1)zeta(s)/s^2.                                (12)

The identity g(t)=1-{exp t}+integral_0^t {exp u}du proves 0<g(t)<=1+t,
so d belongs to L1 and L2. The full floor-sum formula proves (12).

Set h_j=e-f_j=exp(-t/2)A_j(exp t). The explicit compact signed measure

    kappa_j = sum_n a_jn/sqrt(n) delta_log(n)
              +exp(t/2)sum_(n<=exp t) a_jn/n dt             (13)

has zero continuous density beyond log(support p_j). Its transform is
s p_j(s)/(s-1), including the removable value. Therefore

    h_j=d*kappa_j,
    ||kappa_j||_TV <= sum_n |a_jn|/sqrt(n)
                          +2sqrt(N_j)sum_n |a_jn|/n.       (14)

This reconstructs the parent's source adapter; it is not newly discovered here.

For each alpha choose an ordered list j_1,...,j_k of its factors. The finite
identity

    1-product_(r=1)^k w_(j_r)
       =sum_(r=1)^k (1-w_(j_r)) product_(ell<r) w_(j_ell)

and (4) give

    y_P = d * K_P,
    K_P=sum_alpha c_alpha sum_(r=1)^k
               v_Dr * kappa_(j_r) * product_(ell<r) f_(j_ell). (15)

An empty convolution product is delta_0. K_P is an actual L1 kernel: every term
contains the proper stable v_Dr, compact finite measure kappa, and finitely many
L1 functions. Its L1 norm is bounded by the corresponding sum of the products
in (7), (10), and (14). Thus (15) is a bounded causal source map for each P in
the ORIGINAL L2(dt) metric. No bound uniform in m or coefficients is asserted.
In particular y_P belongs to the original factorial-source domain, even if that
domain is proper. This conclusion does not use an assumed RH or reverse synthesis.

**NGR2 (fixed nonzero limiting target).** Let S_a be causal translation. Then

    ||g_D||_2<=1,
    ||g_D-S_1 e||_2^2 <= D^(-1/2).                          (16)

The proof is elementary and quantitative. For a,b>=0,

    ||S_a e-S_b e||_2^2=2(1-exp(-|a-b|/2))<=|a-b|.

Regard (5) as a probability density for tau. Jensen's inequality gives the
left error in (16) at most E|tau-1|<=sqrt(Var tau)=D^(-1/2).
Thus g_D converges to the unit-norm target S_1 e, not to zero or to a target
receding to infinity. The squared error bound in (16) is not an operator-norm
approximation on arbitrary degree-dependent inputs.

## 4. Every fixed off-line zero retains its full exponential detection rate

**NGR3 (unchanged zero-detection exponent).** If rho=beta+i gamma is any zero
of zeta with beta>1/2, set z_rho=rho-1/2 and delta=Re z_rho>0. Every P in (4)
satisfies

    ||u_P||_2^2 >= [2delta/|rho|^2] Q^(2delta m)|M_D(z_rho)|^2
                 >= [2delta exp(-2|z_rho|)/|rho|^2] Q^(2delta m). (17)

At rho all F_j equal 1, so (9) is M_D(z_rho)/rho. The exact support t>=mL and
Cauchy--Schwarz give the first inequality. For EVERY D>=1,

    |M_D(z)|=(|1+z/D|)^(-D)
                    >=(1+|z|/D)^(-D)>=exp(-|z|).           (18)

This is a fixed-zero lower constant independent of m, D and coefficients.
No simplicity or inverse-zero-derivative condition is used. Therefore:

    if m_k->infinity and log(1+||u_(P_k)||_2^2)/m_k ->0,
    then RH follows by (17) and reflection.                 (19)

The new regularizer does not make (19) weaker by suppressing the very zeros
being tested. Conversely, (19) is not proved here and is not inferred from
NGR1's finiteness or NGR2's fixed-target limit.

For any fixed z, M_D(z)->exp(-z); in particular the actual fixed-zero
attenuation tends to exp(-Re z), although the uniform bound (18) is coarser.
This observation does not give a uniform bound at heights depending on D.
The parent's coefficient-cost lower bound evaluated at MOVING simultaneous
near-zeros must consequently NOT be copied unchanged into this packet. Such
high frequencies can be strongly damped. The fixed-zero RH consumer is what
has been preserved.

## 5. A complete finite-time computation contract with an explicit infinite tail

The tail is controllable without unknown zeta values. Define the positive
constants

    C_Dk=2^(k-1) D^D/(D-1/2)^(D-k+1),
    A_k=sum_(|alpha|=k)|c_alpha|,
    B=max_j(1+sum_n |a_jn|),
    W_P(t)=sum_(k=m)^D A_k B^k C_Dk t^(k-1)/(k-1)!.       (20)

Then

    |u_P(t)| <= exp(-t/2) W_P(t),
    integral_T^infinity |u_P(t)|^2dt
       <=exp(-T)sum_(r=0)^(2D-2) b_r r!
                              sum_(j=0)^r T^j/j!,         (21)

where W_P(t)^2=sum b_r t^r. All b_r are nonnegative.

To prove it, the k-fold convolution of |f_j| is bounded by
B^k exp(-t/2)t^(k-1)/(k-1)!. Also the weighted L1 norm of the coefficientwise
absolute kernel in (6) is

    integral_0^infinity exp(u/2)|v_Dk(u)|du
       <= D^D sum_j binom(k-1,j)(D-1/2)^j
                                /(D-1/2)^(D-k+1+j)
       = C_Dk.

Use (t-u)^(k-1)<=t^(k-1), and integrate the resulting polynomial square.
The factorial sum in (21) is the exact incomplete-gamma formula for each integer
power. No cutoff past T is set to zero. This can be a very loose bound, and no
small arithmetic tail is claimed from it.

For fixed m,D,P and finite T the initial portion is computable from finitely many
ordinary coefficients. Expand R(s) as an initially absolutely convergent
Dirichlet series sum b_n n^-s. Its coefficients through exp(T) follow by finite
divisor convolution, with every overlap added. Exactly on [0,T],

    u_P(t)=sum_(n<=exp T) b_n/sqrt(n) S_log(n) g_D(t).      (22)

On each logarithmic integer cell the sum is a finite combination of exponentials
with polynomial coefficients. Since D is integer, g_D has rates D and 1/2.
Outward bounds for rational input arithmetic, log(n) and sqrt(n) suffice to
integrate any prescribed finite part and its pairwise Grams. Finite logarithmic
coefficients in the parent seed must also be enclosed, not replaced by ordinary
high precision. Equation (21) covers the omitted future. No efficient large-rank
implementation is claimed or executed in this packet.

## 6. Scalar powering remains excluded after the regularization

For one fixed finite p with p(1)=0 and p'(1)!=0, vertical almost-periodicity
produces simple p-zeros w with Re w arbitrarily close to 1 and unbounded
imaginary part. Here is the relevant proof. Simultaneous pigeonhole
approximation makes all its finitely many prime phases arbitrarily close to 1;
adjoin 2 and 3 to ensure an unbounded sequence of returns. The shifted p then
converges uniformly on a small circle about its simple zero 1. Rouche gives
recurrent simple zeros. Unique factorization rules out a bounded set of exact
returns. These are zeros of p, not asserted off-line zeros of zeta.

For scalar P_m with P_m(1)=1, the same evaluation proof (17) applies at each
fixed w!=1 with p(w)=0, since F_p(w)=1. For maximum degree D_m>=m, (18) is
uniform in D_m. Taking m->infinity first and then fixed zeros with Re w->1 gives

    liminf_m log(1+||u_(P_m)||_2^2)/(m log Q) >=1.         (23)

Here all the regularized norms ARE finite, by NGR1. Thus scalar feedback remains
a failed whole-problem route even after fixing admissibility. It is not rescued
by arbitrary scalar polynomial coefficients or by a high-frequency cutoff.
This result does not apply to a genuinely multivariate adaptive polynomial by
substituting a zero of only one of its seed polynomials.

## 7. A separate diagnostic: raw all-order admissibility is Lindelof-strength

This section is NOT used in NGR1--NGR3. It explains why regularizing is substantive.
Use the parent's p_0,p_2 with

    p_2-p_0=epsilon H^-s(1-2^(1-s))^2(1-2^-s), epsilon!=0. (24)

Let E_raw(j,m) be the complete physical energy of the locally finite summatory
Dirichlet source for F_j(s)^m/s, allowed to be infinite. Then the classical
Lindelof hypothesis (LH) is equivalent to

    E_raw(0,m)<infinity and E_raw(2,m)<infinity
                                for every integer m>=1. (25)

No uniformity of these energies in m is part of (25). This is NOT an assertion
that a particular high-order energy is infinite, nor that every multivariate
feedback criterion separately needs LH.

Proof that (25) implies LH. For every fixed 1/2<sigma<1, Hardy evaluation of the
actual L2 sources gives

    |F_j(sigma+it)| <= [sqrt(E_raw(j,m))/sqrt(2sigma-1)
                                     *|sigma+it|]^(1/m).

On that ENTIRE vertical line, (24) has the positive lower modulus

    |p_2-p_0| >= |epsilon| H^-sigma
                        (2^(1-sigma)-1)^2(1-2^-sigma).

Since F_0-F_2=zeta(p_2-p_0), zeta(sigma+it)=O_sigma,m((1+|t|)^(1/m)).
Taking m arbitrarily large proves subpower growth at each sigma>1/2. For any
eta>0 the functional equation and Stirling transfer the bound at 1/2+eta to
O((1+|t|)^(eta+epsilon)) at 1/2-eta. The standard strip three-lines/
Phragmen--Lindelof theorem, with the classical polynomial growth bound to justify
it and the pole removed if necessary, gives exponent eta/2+epsilon at 1/2.
Let eta and epsilon be arbitrarily small. This is LH.

Conversely LH, the safe Euler bound and Phragmen--Lindelof give the uniform
bound zeta(sigma+it)=O_epsilon((1+|t|)^epsilon), sigma>=1/2, away from a fixed
neighborhood of its pole. The finite p_j are uniformly bounded there. Their
balance removes the pole in F_j, so the compact neighborhood is harmless.
For fixed m choose epsilon<1/(4m). Then F_j(z+1/2)^m/(z+1/2) has uniformly
bounded L2 norms on ALL vertical lines Re z>0: its tail is bounded by a constant
times (1+|t|)^(2m epsilon-2), which is integrable. Thus it is H2. The Hardy/Laplace
theorem gives an actual causal L2 inverse. In the initial Euler half-plane that
inverse agrees with the locally finite Dirichlet source by Laplace uniqueness.
This proves (25).

The classical ingredients in this diagnostic are explicitly imported: Hardy
representation/evaluation, zeta functional equation, Stirling and strip
Phragmen--Lindelof. NGR1--NGR3 avoid this LH-strength assumption entirely.

## 8. A fully specified multivariate candidate; the upper bound is still open

Use exactly the parent's normalized triple at its frozen source, and for m>=1
all monomials of total degree m in three variables. There are d_m=(m+1)(m+2)/2.
Let u_alpha be their regularized sources (8), with D=m, and let G_m be their
COMPLETE real Gram matrix. Every entry exists unconditionally and has the
finite-part/tail description in Section 5. Define lambda_m=2^(-m^2),

    A_m=G_m+lambda_m I,
    c_m=A_m^(-1)1/[1^T A_m^(-1)1],
    b_m=[1^T A_m^(-1)1]^(-1).                              (26)

This is the unique minimizer of ||sum c_alpha u_alpha||_2^2+lambda_m||c||_2^2
under 1^T c=1. Completion of squares proves it; A_m>=lambda_m I supplies the
inverse contract without assuming independence of the monomial outputs.
The target may depend on m only through g_m in (11). The output is still an
explicit bounded convolution of d and agrees with g_m before m log 3.

For each fixed m the complete matrix, inverse and b_m can be enclosed to any
prescribed accuracy using Section 5, the known positive lambda_m and interval
linear algebra. This is an existence/coverage algorithm, not a claimed fast
implementation. No actual G_m for m>=2 or b_m was computed in this packet.

A sufficient closing theorem for this fully defined family is

    liminf_(m->infinity) log(1+b_m)/m=0.                    (27)

It would imply (19). It is NOT proved. Nor is necessity under RH asserted for
this particular homogeneous, ridge-penalized family. The unrestricted feedback
class is larger. Applying Young and (10) to a pure monomial gives only a bound
of exp(O(m log m)), with fixed-bank constants. Small single-seed errors do not
remove that loss. Positivity of G_m and its ridge floor do not bound its affine
minimum. The exact unresolved quantity is (27), not integrability, an ignored
future, or an unidentified source domain.
