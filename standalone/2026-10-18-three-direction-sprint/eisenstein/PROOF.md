# Correlated Eisenstein probes that remove the quadratic factor

Status: **PROPOSED component mathematics; independent review required.**
Scope: a fixed Eisenstein field, the actual complete Gaussian Mobius source,
and ordinary zeta. No critical signed upper bound, improved zero-free boundary,
field RH, or ordinary RH is claimed.

Exact sources: #983 at `e9ce2d171fba2bcca4cb4d8c6e78dc97f69613e9`, especially
`PROOF.md` and `EISENSTEIN_FAMILY.md`; #998 at
`65a0e7e4016aad5aeb099973c0d079c6059a6c76`, `PROOF.md`.
The Euler-mask identities are credited to those sources. The ordinary
quadratic factorization and the analytic facts explicitly named below are
classical. This packet gives its own character pairing, complete growing-order
Euler--Maclaurin remainder, and constructive probe obstructions.

What was actually run: see CHECKS.json and NOTES.md. Finite checks authenticate
their stated coefficient caps and controls; they do not certify the analytic
upper bound left open in section 8.

## 1. The target should require ordinary RH, rather than field RH

Let K=Q(omega), omega^2+omega+1=0. Remove the prime ideals above 2 and 3,
calling the remaining ideals exterior. Write q(I)=NI. Fix real c and tau>0,
and retain the full Gaussian

    W(y)=y^(-c) exp[-log(y)^2/(4tau)]/sqrt(4pi tau).

Define the complete sources, for every real D>0,

    E(D)=sum_(exterior I) mu_K(I) W(q(I)/D),
    R(D)=sum_((n,6)=1) mu(n) W(n/D).                         (1)

Every ideal, conjugate ideal, nonunit zero and both Gaussian tails remain in
E. The rational source R is not inferred by replacing ideal norms by integers.
Let chi(n) be 1 for n=1 mod6, -1 for n=5 mod6, and zero otherwise. This is
chi_{-3}(n)1_((n,6)=1). Let zeta^(6)(s)=zeta(s)(1-2^(-s))(1-3^(-s)), and
L^(6)(s)=L(s,chi_{-3})(1+2^(-s)). Then, initially for Re s>1,

    zeta_K^S(s)=zeta^(6)(s)L^(6)(s),
    Mellin E(s)=exp[tau(s-c)^2]/zeta_K^S(s),
    Mellin R(s)=exp[tau(s-c)^2]/zeta^(6)(s).                 (2)

These identities follow directly from the Euler factors and the Gaussian
integral. At split p=1 mod3, the reciprocal ideal factor is (1-X)^2;
at inert p=2 mod3 it is 1-X^2. Multiplication by the chi factor gives

    (1-X)^2/(1-X)=1-X;  (1-X^2)/(1+X)=1-X.                (3)

Thus, writing a_K(n)=sum_(q(I)=n, exterior I) mu_K(I),

    sum_(d|n) chi(d) a_K(n/d)=mu(n)1_((n,6)=1).           (4)

In particular every unwanted rational prime-square term cancels before a
norm is taken. This is exact arithmetic cancellation, not an estimate of the
remaining squarefree Mobius source. The finite factors omitted at 2 and 3
are nonzero for Re s>0. Therefore the fixed target in (2) retains every
ordinary-zeta zero with Re s>0, while canceling the entire unnecessary
L(s,chi_{-3}) factor, including its multiplicities at shared zeros.

## 2. Paired rational dilations: a uniform causal Sobolev bound

The coefficient identity (4), absolute Gaussian convergence and divisor
counting give the exact pointwise identity

    R(D)=sum_(k>=0) [E(D/(6k+1))-E(D/(6k+5))].             (5)

Absolute convergence of the unpaired sum holds for each fixed D, because
E(x)=O_R(x^R) as x tends to zero for every fixed R>0. No zero location is used.

For sigma>0, 1<=p<=infinity and T>0 put

    ||A||_(sigma,p,T)=||D^(-sigma)A(D)||_(L^p((0,T],dD/D)),
    mathcal D A(D)=D A'(D).

For any differentiable A with finite derivative norm and sufficient flatness
at zero, the paired operator in (5) satisfies

    ||sum_(k>=K)[A(D/(6k+1))-A(D/(6k+5))]||_(sigma,p,T)
      <= (6K+1)^(-sigma)/sigma * ||mathcal D A||_(sigma,p,T). (6)

This holds for EVERY K>=0, p,T; the cost is independent of p,T and K.
Indeed

    A(D/a)-A(D/b)=integral_a^b mathcal D A(D/u) du/u.

After multiplication by D^(-sigma), the integrand is u^(-sigma) times
a contraction of D^(-sigma)mathcal D A(D) on the same past interval (0,T].
The disjoint intervals [6k+1,6k+5] lie inside [6K+1,infinity). Minkowski and
integral_(6K+1)^infinity u^(-sigma-1)du prove (6), including p=infinity.
For native E all hypotheses hold unconditionally. This estimates the
converter, not the critical size of its input or its signed output.

## 3. A source-specific complex bound, uniform in derivative order

The elementary full ideal count satisfies I_K(x)<=3x for every x>=0.
Here is a convenient proof. The norm is Euclidean by nearest-lattice-point
rounding, so every ideal is principal and has six generators of its norm.
Since a^2-ab+b^2>=(a^2+b^2)/2, the number of nonzero lattice points of norm at
most x is at most 8x+4sqrt(2x). For x>=1 this divided by six is less than 3x;
for x<1 the count is zero. Exterior restriction only decreases the count.

Stieltjes integration, followed by a Gaussian integral, therefore gives

    sum_(exterior I) W(q(I)/D)<=C0 D,
    C0=3 exp[tau(1-c)^2](1+1/sqrt(pi tau)).                 (7)

For completeness, the integral used is
3D integral_0^infinity y|W'(y)|dy. Under u=log y its absolute-value factor
is |c+u/(2tau)|, and the Gaussian tilt has mean 2tau(1-c) and variance 2tau.
Its mean absolute value is at most 1+1/sqrt(pi tau). All boundary terms vanish.

For fixed D let F_D(z)=E(D/z), using the principal logarithm in Re z>0.
Normal absolute convergence makes it holomorphic there. On |z-x|<=x/2,
x>0, one has |z|>=x/2 and |arg z|<=pi/6. The modulus of each Gaussian is
at most exp[pi^2/(144tau)]W(q(I)|z|/D). Hence

    |F_D(z)|<=C* D/x,
    C*=2 C0 exp[pi^2/(144tau)],
    |F_D^(m)(x)|<=C* D m!2^m/x^(m+1),  EVERY m>=0.          (8)

The constant is independent of D,x,m. Cauchy's formula proves the last
inequality. This all-order estimate is the load-bearing uniformity; a
separate unspecified constant at each growing derivative order would fail.

Define normalized rising-Euler probes

    J_m(u)=[mathcal D(mathcal D+1)...(mathcal D+m-1)E](u)/(2^m m!),
    J_0(u)=E(u).                                          (9)

Repeated differentiation gives

    F_D^(m)(N)=(-1)^m N^(-m)2^m m! J_m(D/N),
    |J_m(u)|<=C* u, simultaneously for ALL m,u.             (10)

These probes are the original Gaussian source with an explicitly specified
polynomial Gaussian profile. Their Mellin multiplier is (s)_m/(2^m m!);
its zeros have nonpositive real part. This statement does not assert a
critical bound uniform in m for J_m.

## 4. Logarithmically many probes, with the complete quadratic tail

Let M>=2 be EVEN and N=6K an integer. Euler--Maclaurin with a shifted lattice
and step 6 gives the exact tail identity

    sum_(k>=K)[F_D(6k+1)-F_D(6k+5)]
      =sum_(1<=j<=M) C_j F_D^(j-1)(N)+Rem_(M,N)(D),
    C_j=-6^(j-1)[B_j(1/6)-B_j(5/6)]/j!.                  (11)

B_j denotes the Bernoulli polynomial with B_1(x)=x-1/2. Even j cancel;
C_1=2/3, C_3=-5/9, C_5=17/36. An independent formal-series check is

    sum_(j odd) C_j z^(j-1)=sinh(2z)/sinh(3z).             (12)

The precise remainder bound needed here follows directly from the standard
periodic-Bernoulli remainder:

    |Rem_(M,N)(D)|
      <= [2*6^(M-1)/M!] sup_(0<=x<=1)|B_M(x)|
                               *integral_N^infinity |F_D^(M)(x)|dx
      <= (4/3) C* D (M!/M) [6/(pi N)]^M.                 (13)

Indeed the Bernoulli Fourier series gives
sup|B_M|<=2M!zeta(M)/(2pi)^M<=4M!/(2pi)^M, and (8) supplies the complete
integral. The two shifted remainders have both been included. No tail is
replaced by its leading integral, and no finite ideal cutoff occurs.

Write

    beta_m(N)=C_(m+1)2^m m!/N^m,       m even,
    P_(M,N)(D)=sum_(0<=k<K)[E(D/(6k+1))-E(D/(6k+5))]
                         +sum_(m even,0<=m<=M-2) beta_m(N)J_m(D/N).

Then the exact ordinary source obeys

    R(D)=P_(M,N)(D)+Rem_(M,N)(D).                         (14)

This is the promised correlated numerator--denominator construction. It
is essential to keep the WHOLE expression P inside the final norm: separate
bounds on E and each J_m can reintroduce the unwanted field-RH requirement.

If N>=12M then, using M!<=M^M,

    |Rem_(M,N)(D)|<=(4/3)C* D/M * (1/(2pi))^M.            (15)

The normalized derivative coefficients have bounded total mass:

    sum_(m even,0<=m<=M-2)|beta_m(N)|<3/4.                 (16)

To check (16), beta_0=2/3. For even m>=2, the Bernoulli bound gives
|beta_m|<=(4/pi)m![6/(pi N)]^m<=(4/pi)(1/(2pi))^m.
Sum the even geometric series; already pi>3 bounds the extra mass by 4/105,
so total mass is at most 74/105<3/4. The raw coefficient mass of the complete
finite bundle is at most 2K+3/4, not a constant.

For any A>=0 and T>=2 choose

    M=2 ceil[(A+1)log T/(2log(2pi))],   N=12M,   K=2M.     (17)

For every FIXED 0<sigma<1 and EVERY 1<=p<=infinity, (15) yields

    ||R-P_(M,N)||_(sigma,p,T)<=C_(sigma,c,tau) T^(-A).      (18)

For finite p integrate D^(p(1-sigma)); its root factor
[p(1-sigma)]^(-1/p) is uniformly bounded for p>=1. For p=infinity use the
endpoint directly. Constants are independent of T,p,M and A. There are
2K+M/2=O_A(log T) source evaluations, maximal derivative order M-2, and
coefficient mass O_A(log T). This is a growing-order statement with the
uniform constants supplied in (8), not inferred from a finite ladder.

The Gaussian and rational Mobius source R are fixed while M,N depend on the
observation horizon. We do NOT take the Mellin transform of a varying source.
The complete small remainder in (18) is what connects the finite bundle to
the one fixed source in (1).

## 5. A fixed compact profile family represents all normalized jets

The bound in (16) must not disguise an unbounded-order probe norm. There is
also an exact Cauchy representation using a profile family independent of m:

    J_m(u)=(-1)^m integral_(-pi)^pi
      E(u/(1+(1/2)e^(it))) e^(-imt) dt/(2pi).              (19)

Apply Cauchy's coefficient formula to z -> E(u/(1+z)) on |z|=1/2. The factor
2^m m! in (9) is exactly the normalization produced by that circle. For the
even m in (14), no extra sign appears. Thus the complete counterterm equals
an integral of E(u/(1+(1/2)e^(it))) against a trigonometric polynomial of
L^1 norm at most 3/4. Its arguments stay in a fixed compact right-half-plane
dilation circle, with |arg(1+(1/2)e^(it))|<=pi/6.

This replaces growing jet order by a specified compact complex-Gaussian
profile family. It does not assert a critical upper estimate for that family.
One may use either the exact derivative probes or this exact integral; no
uncertified finite quadrature is substituted for (19).

## 6. Two sharp obstructions to simpler principal probes

### 6.1 Ideal-norm mask dilations cannot produce the ordinary source

Consider the architecture of arbitrary convergent causal convolutions

    H(D)=sum_I h(I)E(D/q(I)),

or limits in a coefficient algebra preserving coefficientwise identities.
At any inert rational prime p outside S, EVERY ideal norm has even p-adic
valuation. Consequently both a_K and every allowed dilation kernel have
only even p-adic valuation support. Their Dirichlet convolution still has
zero coefficient at p. The ordinary source has coefficient mu(p)=-1.

Therefore no such ideal-norm mask/dilation architecture can equal R. This
includes the complete Euler-mask algebra in #983/#998, even with infinitely
many masks and signed coefficients, whenever the stated convergence permits
coefficientwise passage. The obstruction is support, not a bad norm bound.
Rational paired dilations in (5) genuinely escape it. This does not rule out
different profiles or a construction that merely has another valid detector.

### 6.2 Any finite local Kummer phase projector misses legal nonprincipal cores

Let P be ANY finite set of exterior prime ideals. Consider a finite vector of
probes whose row responses depend only on the values chi_u(P), P in P, their
powers, conjugates and products. Then there exists a legal nonprincipal
sixth-free core a whose response vector equals that of the principal core.

Proof. Put M0=6 times the product of rational primes below P. Choose a fresh
inert rational prime q not dividing M0. Such a prime can be obtained without
a prime-distribution theorem: a prime factor congruent to 2 mod3 of 3M0-1 is
fresh, and repeating this argument supplies further choices. CRT gives a
positive integer n with n=1 mod M0 and n=q mod q^2. The ideal u=(n) is
exterior and its unique primary generator is n. At every selected P its
sextic residue value is 1. Its valuation at the inert ideal (q) is exactly
one, so its sixth-free core a has valuation one there. Here is the precise
Kummer justification, rather than an inference from a zero value: in the
tame local field K_(q), containing mu_6, T^6-n is Eisenstein and its Kummer
extension is totally ramified of degree six. Local Kummer duality therefore
gives a nontrivial local character. Equivalently n is not a sixth power
already by its valuation, and the global Kummer character cannot be
principal. This is the valuation case of #983's primitive-core interface
(CT's lemma `lem:kummer` identifies equal characters exactly modulo sixth
powers). Removing a sixth-power ideal factor does not
change any selected value, because n is coprime to every selected P.

At the fresh (q), the original nonunit value is zero. It has not been erased.
Thus this is a literal arithmetic row, not a freely chosen synthetic vector.
The target response c is a nuisance response column. There can be no weights
w annihilating ALL such nonprincipal response columns while w*c=1.

The conclusion covers a Gauss rephasing architecture ONLY when its probe
ratios depend on those finite multiplicative evaluations, leaving one common
row phase as a scalar. It does not claim that arbitrary global CT factors
have this form. Nor does it forbid cancellation of a smaller, explicitly
identified bias subspace. Growing local sets must pay their support and
physical-probe cost; finite rank experiments alone cannot omit this population.

### 6.3 The generic derivative cost cannot simply be discarded

For every 0<sigma<=1, the full rational character convolution T_chi in (5)
has NO bounded map from the weighted L-infinity past norm to itself, even
at the single horizon T=1. This statement concerns arbitrary smooth compact
past sources, not just the special arithmetic E or its complete bundle.

To see this, choose a smooth function f_N on the log axis, supported in
(-log(N+1/2),epsilon), with |f_N|<=1 and

    f_N(-log n)=chi(n), 1<=n<=N, gcd(n,6)=1.

Such a function exists by disjoint smooth bumps around the finitely many
nodes; it may be chosen constant with the assigned sign on a smaller
neighborhood of each node. Put A_N(D)=D^sigma f_N(log D). Its input weighted
past norm is one. All terms at n>N vanish at D=1, so

    [T_chi A_N](1)=sum_(n<=N,gcd(n,6)=1) n^(-sigma).     (20a)

The same identity persists continuously near D=1, so essential-supremum
norms give the same lower bound, rather than a measure-zero evaluation.
Counting the two admissible residue classes modulo six and partial
summation give growth N^(1-sigma)/[3(1-sigma)] for sigma<1 and
(1/3)log N for sigma=1. Thus no generic zero-derivative weighted
L-infinity estimate can replace the paid derivative in (6). The rapidly
growing derivatives of these test sources explain why they do not
contradict (6), (8), or the source-specific finite compression.

This obstruction is not asserted for L2 at sigma=1/2 and does not rule out
a bound exploiting the actual arithmetic correlations of E.

## 7. A separate Hilbert improvement: just over a quarter derivative suffices

This optional analytic refinement is independent of Euler--Maclaurin (11)--(18).
It imports classical Dirichlet continuation/functional equation, Stirling,
Phragmen--Lindelof, Plancherel and the causal half-plane multiplier theorem.
No reciprocal-L estimate is assumed.

Let 0<sigma<1, r>(1-sigma)/2, and put t=log D, f(t)=e^(-sigma t)E(e^t).
Use the causal fractional power of 1+partial_t. Its inverse is

    J_r g(t)=integral_0^infinity e^(-u)u^(r-1)g(t-u)du/Gamma(r).

For smooth flat-past f, g=(1+partial_t)^r f is well defined by the usual
causal semigroup fractional derivative (or successive integer derivatives if
r>=1). Then, on EVERY past horizon (-infinity,log T],

    ||D^(-sigma)R(D)||_2<=C_(sigma,r)||g||_2.               (20)

Here is the multiplier argument and its scope. The degree-one convexity
bound makes

    H(z)=L^(6)(sigma+z)/(1+z)^r

bounded and holomorphic on Re z>0. To derive the needed convexity power,
take Euler convergence at 1+epsilon, reflect at -epsilon using the primitive
degree-one functional equation, and apply Phragmen--Lindelof. This yields
|L(v+it)|<<_(epsilon) (1+|t|)^((1-v)/2+epsilon) on fixed v in [sigma,1],
with a harmless epsilon bound through the line one. Choose epsilon smaller
than r-(1-sigma)/2. For v>=2 Euler convergence is uniform; the remaining
compact real strip is covered by the same bound. The fixed omitted factor
1+2^(-s) is bounded for Re s>=sigma. Thus H is bounded on the WHOLE right
half-plane, not just pointwise on one vertical line.

A bounded analytic half-plane multiplier is a bounded causal L^2 convolution
operator. One direct construction takes its boundary multiplier under
Plancherel; moving the Laplace line right shows that its convolution kernel
is supported in [0,infinity). Its norm is at most sup_(Re z>0)|H(z)|.
Extend g by zero beyond log T, apply that whole-line operator, and restrict
back to the past. Causality means the extension does not alter the answer.
Since J_r g=f on this past interval, the resulting operator is precisely
the paired L^(6) convolution in (5), first on a far-right Laplace line and
then by distributional uniqueness. This proves (20).

At sigma=1/2 any r>1/4 suffices. The cost is a specified causal fractional
Sobolev norm. It is NOT a zero-derivative L^2 bound or a critical estimate
for f. The threshold 1/4 is a sufficient convexity cost, not claimed optimal.

## 8. The remaining ambitious estimate

For the fixed ordinary source R, the explicit bundle P_(M(T),N(T)) in (14)
is now a concrete principal-target correlated observable. A bound for its
COMPLETE critical energy

    integral_0^T |P_(M(T),N(T))(D)|^2 dD/D^2 <<_epsilon T^epsilon

would transfer to R by (18) and then exclude ordinary-zeta zeros in Re s>1/2
by its fixed Mellin identity (2). This bound is OPEN. Replacing its signed
bundle by separate norms of E or the individual jets loses the exact
quadratic-factor cancellation and can restore the stronger field-RH burden.

The substantive component obtained here is an exact arithmetic deflation,
a uniform complete cofinal approximation with O(log T) probes, a compact
profile representation of every normalized derivative, and two constructive
obstructions to cheaper local/mask substitutes. None supplies the missing
critical cancellation or an improved ordinary-zeta boundary by itself.
