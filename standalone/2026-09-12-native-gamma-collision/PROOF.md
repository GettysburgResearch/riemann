# Native gamma martingales, zero-collision flux, and a local annihilation theorem

Date: 2026-09-12. Local labels MCF26 are **PROPOSED component results**, awaiting
independent mathematical and implementation review. **The Riemann Hypothesis
and the global native vanishing-defect estimate are not proved.**

This is a direct attack on the outstanding sign, not another accuracy upgrade.
We return to the *uncompressed mean-centered gamma family* retained in #855 and
#862. The newer Radau construction in #865 remains unchanged. Its positive
higher-order remainder does not establish a Fourier-zero ordering; the local
collision proved here is not asserted for its compressed r>0 family.

The contributions are an exact centered gamma martingale transition, a
source-complete defect-flux formula, and a computer-assisted existence theorem
for a nondegenerate real double zero during the native fifth-to-sixth update.
Near this collision a conjugate pair is annihilated, not created. Neither a
full step census nor identification of this local pair with the particular
N=5 disk in #858 has been certified. The all-stage balance of deaths, births,
and complex-root drift remains the substantive open estimate.

Gamma self-decomposability, convex order, implicit functions, contour zero
counts and endpoint asymptotics are classical. No external priority claim is
made. All transition and local-collision arguments used here are supplied.

## 1. The exact arithmetic update is a mean-preserving martingale

Let independent G_j have shape 2, rate 1. Put

    X_N = sum_(j<=N) G_j/j^2,
    tau_N = 2 sum_(j>N) j^-2,
    Y_N = X_N + tau_N.

The infinite sum X exists with finite mean and variance. In the natural
filtration, Y_N=E[X | G_1,...,G_N]. Thus the discrete centered construction is
already a martingale, not merely a family of positive laws. Its unresolved
Fourier geometry is not a failure of source admissibility.

For a=(N+1)^2 and 0<=u<=1 define the *marginal* interpolation

    Y_(N,u) = X_N + tau_N - 2u/a + Gamma(shape 2, scale u/a),      (1)

where the last variable is zero at u=0 and independent of X_N. Its mean is
independent of u; its endpoints are Y_N and Y_(N+1). Writing uG/a using the SAME
random G at every u gives these marginals but does NOT give the martingale
coupling. The following different coupling does.

**MCF1 (explicit Markov transition).** For 0<=u<v<=1, independently of Y_(N,u),
take two independent Bernoulli variables B_i of success probability 1-u/v,
and two independent exponentials E_i of rate a/v. Then the transition

    Y_(N,v) = Y_(N,u) + B_1 E_1+B_2 E_2 - 2(v-u)/a              (2)

has the required marginal, conditional mean Y_(N,u), and conditional increment
variance 2(v^2-u^2)/a^2. These transitions satisfy Chapman--Kolmogorov.

**Proof.** The uncentered increment has Laplace transform

    [u/v+(1-u/v)/(1+vs/a)]^2
      = [(1+us/a)/(1+vs/a)]^2.

Multiplication by the gamma transform at u gives the gamma transform at v.
The centering exponent accounts for the last term of (2); it is not omitted.
The first two cumulants give the stated conditional moments. Transform ratios
telescope over three parameters, proving consistency. All variables are on the
same positive-source domain: the deterministic lower endpoint at v is
X_N+tau_N-2v/a, which is strictly positive almost surely. QED.

In particular, for every convex test with integrable expectations,
E q(Y_(N,v))>=E q(Y_(N,u)). This is a theorem in the physical positive variable
x. A complex Fourier test after reciprocal projection is not such a convex
test, so no zero ordering follows from this observation.

### 1.1 The complete generator, with its drift retained

For u>0 set k_u(y)=(a/u)exp(-ay/u)1_(y>0). The backward generator is

    L_u q(x) = -2q'(x)/a
                 +(2/u) integral k_u(y)[q(x+y)-q(x)]dy
             = (2/u) integral k_u(y)[q(x+y)-q(x)-yq'(x)]dy.      (3)

One obtains this from (2) with v-u tending to zero. The probability of two
active Bernoulli variables is O((v-u)^2); the first active jump gives (3).
The final expression is nonnegative for a convex C2 test. The jump intensity
2/u is singular at zero, but its mean and variance budgets are integrable;
the finite transitions (2) already define the zero-endpoint process.

Let g_u be the density of (1), zero below d_u=tau_N-2u/a. For u>0 its exact
forward equation is

    partial_u g_u = (2/a) partial_x g_u +(2/u)(k_u*g_u-g_u)
                  = (2u/a^2) partial_x^2(k_u*g_u).              (4)

Equivalently, with L denoting the ordinary positive-variable Laplace transform,

    partial_u log Lg_u(s) = 2us^2/[a(a+us)].                    (5)

The boundary values needed to transform the derivatives vanish: g_u has
positive support endpoint d_u and vanishes there to order 2N+1. The identities
also follow directly from the finite product transform of (1). These formulas
retain the WHOLE gamma tail and do not use a finite time cutoff.

At u=0, the first variation vanishes; on compact positive density arguments
its second variation is 2g_0''/a^2. This explains the variance scale but does not
establish a spectral sign. The coefficient in (4) is positive, yet the second
derivative and subsequent reciprocal square root cannot be dropped.

## 2. Exact reciprocal score and zero motion

For u>0 write

    x(t)=pi exp(2t), y(t)=pi exp(-2t),
    T(u)=log(pi/d_u)/2,
    h_u(t)=sqrt(g_u(x(t))g_u(y(t))) for |t|<T(u), zero otherwise,
    I(z,u)=integral_0^T(u) h_u(t)cos(zt)dt,
    F(z,u)=I(z,u)/I(0,u).                                      (6)

For joint analyticity near a real u>0, substitute t=T(u)q on a fixed q interval. The endpoint factor is then (1-q^2)^(N+1/2) times a locally nonvanishing analytic factor. Positive real branches determine local holomorphic branches in u, and dominated integration gives the required joint analyticity.

F is the actual mean-centered reciprocal transform. It is not xi at finite
N or u. It is even entire, real under conjugation, and F(iy,u)>0 for real y.
In particular there is no zero at the origin or elsewhere on the imaginary
axis. A zero of I is exactly a zero of F with the same multiplicity.

Let

    R_u(x)=partial_u g_u(x)/g_u(x),
    S_u(t)=[R_u(x(t))+R_u(y(t))]/2.

Differentiating (6), including its support, gives

    partial_u I(z,u)=integral_0^T(u) h_u(t)S_u(t)cos(zt)dt.      (7)

The moving boundary contributes zero. Locally uniformly in u>0, h vanishes
there as (T-t)^(N+1/2), and its first parameter derivative has an integrable
one-lower-power bound. Differentiation on smaller intervals followed by
dominated passage proves (7). The appropriate normalized formula is a
covariance: partial_u F=E[cos(zt)S]-F E[S], using the probability h/I(0,u) on
the half interval. That subtraction matters away from zeros.

For a simple zero rho(u), the holomorphic implicit function theorem gives

    rho'(u)=-I_u(rho(u),u)/I_z(rho(u),u).                       (8)

The probability martingale supplies an exact expression for the numerator;
it does not give its phase relative to the denominator.

### 2.1 Uniform finite exceptional region away from u=0

**MCF2.** Fix N and 0<u0<u1<=1. There is a finite B(N,u0,u1) such that for
EVERY u in [u0,u1], every zero with |z|>B is real and simple. No numerical value
or bound uniform in N or as u0 tends to zero is claimed.

Here is the source and uniformity argument. The density g_u is a translated
sum of 2(N+1) exponentials, whose rates are 1^2,...,N^2,a/u, each repeated twice.
If m=2N+2, c_u=product(rates)/(m-1)!, and V is uniform on the (m-1)-simplex,

    g_u(d_u+w)=c_u w^(m-1) E exp(-w R_u^simplex),
    R_u^simplex=sum rates_j V_j.                               (9)

This notation is separate from the score R_u above. The positive simplex
factor is entire. Rotating by the midpoint of the rate interval proves it
zero-free whenever |Im w| times the rate range is less than pi. On a compact
u interval this gives a common neighborhood for both reciprocal arguments.
Consequently

    h_u(t)=(T(u)^2-t^2)^(N+1/2) A(t,u),                        (10)

where A is positive, even and real analytic in t and u on a common relative
neighborhood of the closed moving segments. The endpoint leading coefficient
has a strictly positive minimum on [u0,u1]. All finite derivative bounds are
uniform there.

For alpha=N+3/2, the two endpoint contour integrals give, in |Im z|<=Re z,

    I(z,u)=C(u) z^-alpha
      [cos(T(u)z-pi alpha/2)+O(e^(T(u)|Im z|)/|z|)],           (11)

with the next term and a uniform quadratic remainder obtained by one more
endpoint Taylor coefficient. On Im z>=Re z>=0, the left endpoint instead
supplies a nonzero leading Laplace term, uniformly in u. The compact top
contour is exponentially smaller. Symmetry covers the other sectors.

In the first sector, outside shrinking disks around the real cosine zeros the
cosine lower bound excludes all sufficiently large zeros. Rouché gives one
zero counted with multiplicity in each sufficiently late disk. Each disk is
invariant under conjugation, so that one zero is real and simple. This is the
same two-sector mechanism proved in #858/#862, now with uniform constants on
the explicitly compact parameter set. It does not interchange fixed-stage and
unbounded-stage limits. QED.

Thus nonreal zeros cannot enter from infinity during such a compact substep.
They may cross a chosen *finite* observation boundary, and special care is
still needed at u=0: the endpoint power changes there from N-1/2 to N+1/2.
The theorem does not make that singular corner uniform.

## 3. The weighted defect has a signed, not automatically dissipative, flux

Take one first-quadrant representative rho=a+ib from each nonreal quartet and
retain its multiplicity. At parameters with simple exceptional zeros put

    Delta(u)=sum_(quartets) b^2/(a^2+b^2)^2.                   (12)

MCF2 makes this sum finite on a compact substep. Differentiating a summand,
using (8), gives the exact identity

    Delta'(u) = -2 sum_(quartets) b/|rho|^6
                         Im[conj(rho)^2 I_u(rho,u)/I_z(rho,u)]. (13)

Indeed the gradient of b^2/(a^2+b^2)^2 is
(-4ab^2, 2b(a^2-b^2))/|rho|^6. The factor 2 and the conjugate square are
necessary. An adjoint square, absolute square, or unsigned phase estimate is
not (13).

### 3.1 A real double zero gives an exactly priced birth or death

Suppose at real x*>0,u*,

    I=I_z=0,       I_zz !=0,        I_u !=0.                    (14)

The two zeros near x* admit a real analytic sum and product in u. For example,
choose a small circle containing only this double zero; the contour integrals
of z^k I_z/I, k=1,2, give these symmetric functions. The associated local
quadratic is exactly

    (z-c(u))^2-D(u),
    c(u*)=x*, D(u*)=0,
    D'(u*)=kappa=-2I_u(x*,u*)/I_zz(x*,u*).                     (15)

A nonvanishing analytic factor relates it to I. Differentiating at the double
zero proves the last formula, without choosing labels through the collision.
Real coefficients give c,D real for real u.

If kappa>0, for u just below u* the two zeros form a conjugate nonreal pair,
and for u just above u* they are distinct real simple zeros. If kappa<0, the
orientation is reversed. The reflected pair near -x* is automatically present.
The quartet's contribution is exactly

    Delta_fold(u)=(-D(u))_+/(c(u)^2-D(u))^2.                   (16)

For a death, its left derivative at u* is -kappa/x*^4 and its right derivative
is zero. There is no missing jump or multiplicity charge at the collision.
This result also illustrates why tracking only simple real-root velocities
misses the decisive event.

Equations (13),(16) give a complete balance on any compact substep whose
exceptional roots are simple except for finitely many nondegenerate real
folds. General higher collisions require separate cluster control; they are
not assumed absent throughout the actual cascade.

## 4. A native fifth-to-sixth annihilation, from the defining integral

**MCF3 (computer-assisted existence theorem).** In (1),(6) take N=5,a=36.
There is a unique real solution (x*,u*) of I=I_z=0 in the closed square of
radius 10^-35 about the following EXACT rational center:

    x0=31.1001854446439890503617267697554065740922204460843963878401,
    u0= 0.323788258419987986775868946870425118445263688003329898058626. (17)

Throughout that square the accepting calculation proves I_u>0 and I_zz<0.
Thus kappa in (15) is positive and this is a local annihilation. The exact
slope interval is retained in result.json; the displayed center is NOT the
exact double zero. Uniqueness is only in this square.

The complete certificate is detailed below. It uses the same 512-bit integer
interval primitive as #855, authenticated byte for byte, but a new source,
new integrated parameter derivatives, and a two-variable contraction test.
No zeta evaluator, zero table, floating quadrature, or scouting residual is
used for acceptance.

### 4.1 Finite density and literal centering

At each of u0 and u0+-10^-32 the six gamma rates are exactly
1,4,9,16,25,36/u, all with shape 2. Write

    d_u=pi^2/3-2 sum_(j=1)^5 j^-2-u/18.

For distinct rates lambda, partial fractions give

    f_u(w)=sum_i B_i(w+C_i)exp(-lambda_i w),
    B_i=lambda_i^2 product_(j!=i)[lambda_j/(lambda_j-lambda_i)]^2,
    C_i=-2 sum_(j!=i)(lambda_j-lambda_i)^-1.                    (18)

Its Laplace transform is exactly product (lambda/(lambda+s))^2. The physical
density in (6) is g_u(x)=f_u(x-d_u), not f_u(x) and not a floating centering.
The simplex representation (9) also applies with m=12 and p=11.

The supplied outward pi primitive encloses the true value via the complete
Machin arctangent remainder. All rational parameters in (17),(18) remain
exact rationals until outward interval conversion.

### 4.2 Every quadrature cell and complex square-root branch

The support endpoint at each of the three parameters lies in

    Llo=1.10496674354148199,
    Lhi=1.10496674354148200.

These inequalities are checked by outward exponential comparisons with pi/d_u.
Integrate on [0,B], B=1.10496674349, and pay the full remainder [B,T(u)].
For each real cell center c and halfwidth delta, the complex Taylor circle has
radius

    rho=min(1/64,(Llo-c)/4, 31 exp(2c)/(72*112)),               (19)

where the exponential in the implementation is rounded DOWN. Dyadic bisection
continues until delta/rho<=1/8. The algorithm proves exact gap-free coverage;
its final panel count is recorded, not an assumed sampling density.

Both density arguments have positive real part on that circle. For the smaller
argument y=pi exp(-2t)-d_u, (19) ensures

    (lambda_max-1)|Im y| < (8/9)pi < pi.

The simplex strip therefore makes f_u(y) zero-free. For the larger argument
x=pi exp(2t)-d_u, Re x>13/5 and |Im x|<Re x. The first exponential row in (18)
dominates the sum of the others by the explicit rational ratio tested in code:

    sum_(i>1) (B_i/B_1)
       *[2+|C_i|/(13/5)]/[1+C_1/(13/5)]
       *2^(-floor((lambda_i-1)*13/5)) <1/4.                    (20)

It is consequently zero-free too. Each local analytic square root agrees with
the positive one on the real cell. No unrestricted continuation of a square
root or probability density is presumed.

On all these circles |x|<32, |y|<4. The partial-fraction and simplex bounds give

    |f_u(x)|<2^14,       |f_u(y)|<2^39.

For real x0 in (17), |cos(x0 t)| and |sin(x0 t)| are at most exp(32/64), and
|t|<9/8. Therefore every integrand for I,I_z,I_zz is bounded by M=2^48.
The code forms and integrates the complete degree-72 Taylor polynomial in
the SCALED variable (t-c)/rho. All coefficient arithmetic is outward integer
arithmetic; no bound comes from sampled high derivatives.

Summing the analytic Cauchy remainders pays at most

    E_quad=2B * 2^48 * (1/8)^73/(1-1/8).                      (21)

Odd polynomial terms integrate to zero; the full remainder, not just its even
part, is bounded by (21).

### 4.3 The moving endpoint is included completely

The rate-one shape-two density has supremum below 1, so every convolution in
(18) has f_u(w)<=1 for w>0. The simplex coefficient is below 90000.
For r=T(u)-t<10^-10, the small argument is

    d_u(exp(2r)-1)<=r.

Thus h_u(t)<=300 r^(11/2). Since t^j<=2 for j<=2, the ENTIRE omitted endpoint
interval contributes at most

    E_end=(1200/13)(10^-10)^6/10^5                            (22)

to each real integral. No integral beyond the compact support is needed; there
the density is exactly zero. This support is the current interpolated source's
support, not the older N=5 endpoint.

### 4.4 Parameter derivatives and a deliberately coarse complete majorant

For the contraction we use I_u and I_zu obtained from the two complete
parameter-displaced integrals, not a numerical derivative without a remainder.
A common bound H=10^18 covers all first, second, and third partial derivatives
needed for the Jacobian of (I,I_z), on

    31<x<32,       0.32<=u<=0.33.                             (23)

Here is a proof of this generous bound. In the simplex formula f_u(w)=c_u w^11
ell_u(w), the variable rate is lambda=36/u. On (23), lambda<=112.5,
|lambda'|<352, |lambda''|<2200, |(log c)'|<7, |(log c)''|<20.
For either density argument w(t,u), w_u=1/18. Differentiating the positive
simplex expectation at REAL w>0 gives

    |partial_u log f_u(w)| <=14+352w+1/w,
    |partial_u^2 log f_u(w)|
       <=60+2200w+(352w+7)^2+1/w^2.                           (24)

The variance term is bounded by the maximum squared score; it has not been
assumed favorable. On 0<t<T(u), the larger argument is between 2 and 32 and
the smaller y is in (0,3). Hence, for L=log h_u,

    |L_u|<=20000+1/y,        |L_uu|<=2*10^8+1/y^2.

It follows that

    |h_uu|<=h(10^9+3/y^2),
    |h_u|<=h(20000+1/y).

Use h<=300 y^(11/2) near the small argument, and y<3 everywhere. With T<9/8,
the integrals, even after multiplication by t^j for j<=3, are much smaller
than 10^18. The simple bound h<=1 handles pure spectral derivatives.
Both h and h_u vanish at the moving endpoint; differentiating twice produces
no hidden boundary atom. The bounds just displayed are integrable uniformly
on (23), proving the asserted differentiated-integral identities and H.

For eps=10^-32, centered real finite differences enclose I_u,I_zu with error
at most H eps/2. This follows by integrating the Lipschitz bound for the first
derivative on [-eps,eps], not by invoking an unbounded higher derivative.

### 4.5 The two-variable contraction is the existence proof

Let G(x,u)=(I(x,u),I_z(x,u)). Construct a rational matrix Y by EXACT inversion
of the midpoints of the enclosed Jacobian at (x0,u0). Midpoint inversion only
proposes the preconditioner; the accepting inequalities use the whole interval
Jacobian. Each of its entries is widened by 2H R, R=10^-35, to cover the square.
The final calculation verifies

    beta = sup_square ||Id-Y DG||_infinity <1/100,
    delta=||Y G(x0,u0)||_infinity,
    delta+beta R<R/2.                                         (25)

It also proves Y nonsingular by exact rational arithmetic. Thus the map
(x,u)->(x,u)-Y G(x,u) maps the square into itself and is a strict contraction.
Its unique fixed point is the claimed exact solution of G=0. Interval signs
I_u>0,I_zz<0 throughout the square prove nondegeneracy and the orientation
in (15). A root-finder residual alone would not prove any of these statements.


### 4.6 A complete local continuation tube, not two unrelated endpoint pictures

There is also a fully quantified local tube at rational parameter endpoints.
Let h=10^-32, r=10^-15, and take

    u in [u0-h,u0+h],          |z-x0|<r.                       (26)

The endpoints are exact rationals, not rounded values relative to the unknown
u*. The independent tube arithmetic in check.py uses the three full integral
outputs. On the entire tube it proves exactly TWO zeros counted with
multiplicity and no boundary zero. It also proves that the lower endpoint has
two nonreal simple conjugate zeros, the upper endpoint has two real simple
zeros, and there is precisely one real collision between them.

For completeness, denote absolute upper bounds for I,I_z,I_u,I_zu at the center
by A0,A1,B0,D0, and set M=10^18. For all the parameters in (26),

    |I(x0,u)|<=C0=A0+B0 h+M h^2/2,
    |I_z(x0,u)|<=C1=A1+D0 h+M h^2/2.

The complex pure spectral third derivative is bounded by 8, since h_u(t)<=1,
T<9/8 and exp(|Im z|T)<2. Rouché relative to the fixed central quadratic
I_zz(x0,u0)(z-x0)^2/2 has the strict lower margin

    (-I_zz(x0,u0)_upper)r^2/2
       -C0-C1 r-M h r^2/2-8r^3/6 >6.48*10^-40.               (27)

These inequalities cover EVERY real u in the closed interval, not a grid.
On its real diameter the complete curvature is below -1.30148*10^-9.
The parameter derivative is above 2.16855*10^-10: Taylor in x and then u
bounds its loss by D0 r+M r^2/2+M h. The derivative I_z is positive at x0-r
and negative at x0+r. It therefore has exactly one real critical point at
each parameter; the critical value is strictly increasing in u.

At the lower endpoint the complete maximum on the real diameter is negative.
A rigorous upper bound is I(x0,u0-h)+|I_z(x0,u0-h)|^2/(2c), where c is the
positive curvature magnitude lower bound. It is below -2.17*10^-42. At the
upper endpoint I(x0,u0+h)>2.17*10^-42, while both real ends of the diameter
are negative by (27). The intermediate value theorem supplies two real roots
there. The complex count of two makes them simple and excludes others.
At the lower endpoint that count and the absence of real roots give two
nonreal simple conjugates. Monotonicity of the critical value permits exactly
one collision; Section 4.5 identifies it in its much smaller rational square.

The squared splitting coefficient satisfies

    0.33402067 < kappa < 0.33403612.                           (28)

This tube is deliberately tiny. It certifies the local event and its orientation,
not a continuation all the way back to u=0 or forward to u=1. Reflecting the
tube through z=0 gives the other half of the disappearing quartet. These are
zeros of the finite gamma approximant, NOT a double zero claimed for xi.

## 5. The direct missing completion: what was gained and what was not

The probability ordering is now explicit, and at one ACTUAL centered update
its reciprocal Fourier effect has a rigorously priced local sign: a nonreal
quartet disappears. The local defect is

    Delta_fold(u)=kappa(u*-u)/x*^4+O((u-u*)^2) below u*,
    Delta_fold(u)=0 above u* sufficiently nearby.              (29)

The O term follows from the analytic c,D in (16). This says nothing about
other roots at the same u. There may be births or adverse drift elsewhere.
Nor was a full homotopy from the #858 N=5 disk carried out. The two observations
are suggestively near each other, but proximity does not establish lineage.

A possible complete route is to control (13) on the ENTIRE finite exceptional
set at every stage, together with all collision and corner contributions.
For example, a proved native recursion

    Delta_(N+1) <= (1-eta_N)Delta_N+eta_N epsilon_N,
    0<eta_N<=1, sum eta_N=infinity, epsilon_N->0,               (30)

would give Delta_N->0. To check this implication, subtract any fixed positive
upper allowance for epsilon_N at late N, iterate the factors 1-eta_N, and use
product(1-eta_N)->0. The tail-defect convergence and xi identification in #862
then give RH, with multiplicities retained. Equation (30) is an OPEN proposed
upper estimate, not a proved consequence of the martingale or the one fold.

Even an inward sign at every simple nonreal root, were it proved, would not
by itself force a positive limiting height to vanish. The total remaining
variance is O(N^-3). The prior local expansion around a hypothetical simple
nonreal xi zero permits convergent, summable root displacements. A proof needs
a true global gain or a different native cancellation mechanism; neither
probability convex order nor faster absolute approximation supplies that gain.

We attempted to replace the missing sign by convexity of the martingale tests.
Equations (7),(13) expose the failure: the reciprocal score is tested against
a complex oscillatory function, and divided by the actual spectral derivative.
The generator's nonnegative convex remainder has no sign for that expression.
No assertion of global dissipation is made. The useful next test is a validated
whole-window birth/death balance at ONE stage with a simultaneous exterior
certificate, followed by an analytic stage-uniform bound. Neither has been
completed here, and neither is delegated to a reviewer as a routine last lemma.

## 6. Sources, version boundaries, and what is new relative to adjacent work

- #865 at 03cb3cb0b14922b839d0a6a64a59236377b1848d: the nine-file RGT26 payload
  matches the supplied ZIP and tree 1b7306283ac56043bbfd96e29db34d030fa0395f.
  Its source construction was read locally; the supplied full file was authenticated to remote blob
  3b61dfb773d091d5b24d81bb4876ff6f50547b87. Its r>0 approximation theorem is
  not needed to prove MCF1--MCF3 and is not re-reviewed here.
- #862 at 67d5d6a5f588642f4c451fe35d2369b5ddac9346: finite weighted defect,
  real-zero repair and convergence to the actual xi defect. The supplied
  manuscript is the inherited RH consumer, not a newly accepted theorem.
- #855 at 0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad: exact centered family and
  its distinction from the raw interpolation. The interval primitive is reused
  verbatim, blob 36d6341b574fe5a512196bfa0d66fbae897365a6. No parent numerical
  campaign is rerun or counted as an independent arithmetic backend.
- #858 at 72ccb357e774db1189e82f4f1b83459f00638c7e: endpoint proof and native
  N=5 defect provide relevant context. Its certificate.py was read for the
  complete-endpoint/scaled-Taylor architecture; it is not imported as executable
  code or replayed here. This packet's double-zero source and parameter test
  are new. No continuous identification of the two pairs is assumed.
- #851 at 57726ef9b3bf90561df5a361e3b01169c892a62a and #866 at
  14b20cc85aec1dc1909990d2d8a517740f2dd536 received PR-body reconnaissance,
  not full proof review. Their simple-zero transfers and degree-growth target
  are not imported as theorems. No exhaustive census of new research is claimed.
- Biane--Pitman--Yor, arXiv:math/9912170, is the classical infinite gamma/xi
  source imported through the predecessors. The finite martingale and finite
  collision do not need an RH statement, a zero list, or that external proof.
- NIST DLMF 2.4(i), classical complex Watson/Laplace estimates, underlies the
  endpoint mechanism; the two-sector and uniformity argument is supplied in
  Section 2.1. No spectral reality is inferred from real-axis asymptotics alone.

Normal and optimized executions use the SAME interval implementation. Numerical
certificate reconstruction is not independent mathematical review. No full
repository validator, Lean build, remote CI, all-zero census, large-r Radau
solve, new actual xi zero, or RH proof is claimed.
