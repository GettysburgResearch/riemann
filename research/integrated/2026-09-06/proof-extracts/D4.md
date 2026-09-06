# Reviewer D, pass four — reconstructions R25–R31

Status: proposed independent review proofs and a new full computational certificate.
These do not establish RH. All historical sources are immutable. Source labels
refer to `SOURCES.tsv`; the exact main baseline is
`8d16f8d9c475db290bc85e53d775b93b9bcdb336`.

## R25. Literal P61 bias: a complete replacement computational certificate

### Statement and object

Let P be the product of the eighteen primes through 61. Let

    q = 6*1 - 6*delta_1 + 9*delta_2 - 3*delta_4,
    H_x(n) = min(log 4, log(x/n))_+,
    A(x) = sum_n q(n) H_x(n)/sqrt(n),
    F(x) = sum_(d|P) mu(d) A(x/d)/sqrt(d),
    M(x) = sum_(d|P) A(x/d)/sqrt(d).

Then the new certificate, with the analytic input below, proves

    0 <= F(x) <= M(x)                    (1 <= x < 67),
    M(x)/42 <= F(x) <= M(x)/8            (x >= 67).

For x>=67 all three quantities are strictly positive. This is a fixed-P61
all-real-endpoint theorem, not a theorem uniform in a growing prime cutoff.
The old 1/40 bound is false. The conclusion is the same repaired theorem as
L-97400, not a claim of mathematical novelty.

### Exact coefficients, independently constructed

Write omega_P(n) for the number of distinct prime factors of n that divide P,
and mu_P(n)=mu(n) if n divides P, zero otherwise. Then

    f(n) = 6*1_(omega_P(n)=0) - 6*mu_P(n)
           + 9*1_(2|n)*mu_P(n/2) - 3*1_(4|n)*mu_P(n/4),
    m(n) = 6*2^omega_P(n) - 6*1_(n|P)
           + 9*1_(2|n)*1_(n/2|P) - 3*1_(4|n)*1_(n/4|P).

These follow by convolving q with the signed or unsigned divisor indicator
of P. The constant term uses respectively sum_(d|gcd(n,P))mu(d) and the
number of divisors of gcd(n,P). The C++ replay computes these formulas by a
prime-divisibility sieve, rather than copying the source's in-place Euler
convolution. An independent Python calculation compares both constructions
through 2000.

For any real coefficient sequence b define the two prefixes

    S_b(N)=sum_(n<=N) b(n)/sqrt(n),
    L_b(N)=sum_(n<=N) b(n)log(n)/sqrt(n).

For integer N and k=floor(N/4), finite rearrangement gives

    sum_n b(n)H_N(n)/sqrt(n)
    = log4*S_b(k)+logN*(S_b(N)-S_b(k))-(L_b(N)-L_b(k)).

Every activation/saturation knot is an integer. The observation is continuous
and affine in log x between adjacent integers. Hence endpoint bounds imply
bounds on every intervening real point.

### Primitive and arithmetic inclusion contracts

The new producer uses directed MPFR at 256 bits only for sqrt, reciprocal
sqrt, log, log/sqrt and zeta(1/2). All positive rational arguments are first
bracketed in opposite directions; no nearest-rounded rational is silently
regarded as exact. Bounds are converted by directed floor/ceiling into
integers with denominator 2^48. All subsequent finite-prefix and observation
operations are integer interval operations, at denominator 2^96. Signed
addition and multiplication check __int128 overflow. No decimal field is
used as a proof endpoint.

Tail primitives use denominator 2^96; products and sums use arbitrary-precision
Boost integers, at denominator 2^192. Each divisor and activation point is an
exact integer of fewer than 128 bits and therefore is exactly representable
at 256 MPFR bits. The finite inputs and fixed powers of two are likewise
exact. Integer extraction is within the documented bounds of the native
64-bit long for the small primitives. No underflow, overflow or limiting
precision branch occurs for these bounded inputs.

The implementation relies on MPFR/GMP's correctly rounded primitives and the
stated compiler/ABI. The fallback header declares the public MPFR 4 ABI on the
tested 64-bit platform; use vendor mpfr.h where installed. This is not a
separate implementation of transcendental arithmetic and not a proof kernel.

### Finite coverage

The replay tests:

    F(N)>0                    3 <= N <= 66,
    M(N)-F(N)>0                5 <= N <= 66,
    42F(N)-M(N)>0             67 <= N <= 1,000,000,
    M(N)-8F(N)>0              67 <= N <= 1,000,000.

There are 1,999,994 strict finite inequalities. The initial omitted cells have
no active atom or only the positive n=2 atom; M-F first activates at n=4.
Their required non-strict inequalities follow exactly, including the knots.
The new lower bounds include

    42F(184)-M(184) > 3,
    M(67)-8F(67) > 135,
    40F(184)-M(184) < -18.

The stored integer intervals give sharper values; these displayed rational
thresholds, not nearest decimals, are the proof-facing margins.

### Analytic tail and compact base error

The reviewed ramp estimate L-93600, reconstructed in pass-three R21, is

    S(y)=sum_(n<=y)n^(-1/2)log(y/n)
        =4sqrt(y)+zeta(1/2)log(y)+zeta'(1/2)+R(y),
    |R(y)|<5 y^(-3/2), y>=1.

Using q and subtracting the scale-four copy gives, for y>=16,

    A(y)=12sqrt(y)+C0+E(y),
    C0=(6zeta(1/2)-15/2+9/sqrt2)log4,
    |E(y)|<270 y^(-3/2)<5.

The zeta-prime constant cancels in the scale subtraction. This is a named
analytic dependency, not inferred from a finite check or a differentiated
asymptotic. For 2<=y<=16 the new directed replay checks 1401 mesh points at
spacing 1/100 and proves |E|<13/4 there. On every open cell

    A'(y)=y^(-1)sum_(y/4<n<y) q(n)/sqrt(n).

Since 0<=q(n)<=15 and sum_(n<=y)n^(-1/2)<=2sqrt(y),
|A'(y)-6/sqrt(y)|<=36 on y>=2. Continuity at knots implies the same Lipschitz
bound across cells. Thus the complete compact error is less than
13/4+36/100<5. Directed evaluation also gives |C0|<20. The proof needs no
numerically delicate derivative interpolation.

For a_d=42mu(d)-1 or a_d=1-8mu(d), let D_x={d|P:2d<=x}. The literal
observation is bounded below by

    12sqrt(x) sum_(D_x) a_d/d
    -20 |sum_(D_x) a_d/sqrt(d)|
    -5 sum_(D_x) |a_d|/sqrt(d).

Between activation points 2d this is affine in sqrt(x). Enumerate all 2^18
=262144 divisors of P exactly, sort them, and check both endpoints of every
slab meeting [10^6,infinity). At an activation the true A(2) is zero; the
left-limit and right-limit lower bounds are both legitimate, so no jump is
silently omitted. The last infinite slab is controlled by its left endpoint
and a strictly positive slope. The replay checks 256805 slabs for EACH
inequality and proves lower margins >119 and >40000 respectively. This covers
every real endpoint beyond 10^6, including the final unbounded interval.

### What changed relative to the retained producer (D-F17)

S01 first rounds rational arguments to nearest and casts final long-double
endpoints to nearest double before printing them. The latter is a concrete
failure in S02: its C0 interval is the singleton

    [-13.721771741974681191, -13.721771741974681191].

The independent directed `constant_audit.cpp` proves C0 belongs to

    [-22050037046817073440859741106187837389840250209508308839836332,
     -22050037046817073440859741106187837389840250209508308839836331] / 2^200.

This interval lies strictly below that singleton. Consequently the printed
field does not enclose the mathematical constant. No irrationality conjecture
is used. Directed function evaluation at a nearest-rounded rational argument
also lacks the stated general inclusion contract; the new replay removes that
issue rather than speculating that its tiny magnitude changes the sign.

This does NOT refute the fixed-P61 theorem. The new full replay independently
establishes the required inequalities and supplies new provenance. Preserve
the original bytes; replace the evidence adapter and serialization contract
under a new identity. Both compilers used the same MPFR library; compiler
agreement is not a second special-function backend.

## R26. Safe completed source and a negative elementary prime atom (D-F16)

### Safe identity reconstructed before making a sign claim

Let Q=xi'/xi and sigma>1. The normalization constant 1/2 in xi cancels in its
ratios. With c=1/2, put

    B(u)=1/(1-exp(-2u))-(1+exp(u)),
    dnu_sigma = sum_(p,k) p^(-k sigma)/k delta_(k log p)
                + exp(-sigma u)B(u)du/u.

The Euler logarithm gives the atomic part. The gamma identity follows by
twice differentiating its integral in t, using the convergent trigamma
integral, and matching the value and first derivative at t=0. It is

    log Gamma((sigma-it)/2)-log Gamma(sigma/2)
    = -it psi(sigma/2)/2
      + integral (exp(itu)-1-itu) exp(-sigma u)
                   /[u(1-exp(-2u))] du.

The rational factors sigma and sigma-1 contribute the same integrals with
negative densities exp(-sigma u)/u and exp(-(sigma-1)u)/u. The pi factor adds
it log(pi)/2. Therefore, with

    lambda_sigma = (log pi-psi(sigma/2))/2
       - integral_c^infinity exp(-sigma u)/(1-exp(-2u)) du
       - integral_0^c [exp(-sigma u)+exp(-(sigma-1)u)] du,

one has exactly

    log[xi(sigma-it)/xi(sigma)]
    = it lambda_sigma
      + integral (exp(itu)-1-itu*1_(u<=c)) dnu_sigma(u).

The branch is the continuous logarithm equal to zero at t=0. The continuous
measure is of order u^-2 at zero, so the compensation is indispensable.
Its compensated integrand is O(u^2); the exponential tail is integrable for
sigma>1. Primes have log p>=log2>c, hence no compensator at prime atoms.
Differentiation gives the safe Q and Q' formulas in S18. This derivation
checks the complex phase and drift signs, not merely real parts. It proves
no positive-measure continuation through the critical region.

### The observation kernel has its own sign

S19 correctly establishes

    P(x,y) = <U_x-V_x,U_y-V_y> - <U_x,U_y> - <V_x,V_y>.

This is a signed observation in positive Hilbert spaces. S18 subsequently
states that all indefiniteness is localized to the explicit negative source
measure and the deterministic connection. That inference omits the sign of
the elementary observation kernel itself.

Indeed S18.16 identifies, on prime atoms,

    K_(a;x,y)(u) = -[k_(a;x,y)(u)+k_(a;x,y)(-u)].

At equal carriers x=y=0 and the safe scale a=1 this is -2r_1(u). The actual
residual from L-91022 is

    r_1(u)=-1/4(1+u)e^-u +17/32(1+2u)e^(-2u)
           -1/16(1+4u)e^(-4u), u>=0.

At the literal prime atom u=log2,

    r_1(log2)=1/256+log2/8,
    K_(1;0,0)(log2)=-1/128-log2/4 < 0.

The prime-2 atom belongs to the POSITIVE part of the base measure. A positive
Gram kernel cannot have a negative diagonal. Thus the proposed pointwise
positive elementary factorization cannot hold on that source, and positivity
of the integration measure alone does not establish positivity of its
observation. The signed safe representation and Wick identity survive.

Required repair: retain the two endpoint counterterms (or an explicit signed
observation metric) and formulate a lower bound on the COMPLETE form. This
calculation does not prove the integrated positive-source piece is negative,
does not prove full xi has a negative form, and is not an RH counterexample.
It sharpens the existing signed decomposition, rather than claiming discovery
of a new general principle about signed kernels.

## R27. Brownian normalization and fixed-compact asymptotics

Let independent Gamma(2,1) variables be Gamma_n and let
S_N=sum_(n<=N)Gamma_n/n^2. Its increasing limit S has Laplace transform

    E exp(-t S)=product_(n>=1)(1+t/n^2)^(-2)
               = [pi sqrt(t)/sinh(pi sqrt(t))]^2.

Every positive moment is finite, since E exp(epsilon S)<infinity for
0<epsilon<1. Every fixed negative moment is finite, since S dominates a
positive multiple of a fixed finite gamma sum with sufficiently large shape.
The Mellin expectation is therefore entire in its exponent. For Re u<0,
Tonelli followed by y=2pi sqrt(t) and
exp(-y)/(1-exp(-y))^2=sum_(n>=1)n exp(-ny) gives

    E S^u = 2^(2u+1) pi^(2u) Gamma(2-2u) zeta(1-2u)/Gamma(-u).

Gamma duplication and the functional equation of xi identify
pi^(-s/2) E S^(s/2)=2xi(s), initially in that half-plane and then everywhere.
This uses the classical sinh product, gamma identities and functional
equation, not RH or an empirical Brownian zero comparison.

Put R_N=S-S_N, independent of S_N. For each fixed p>=1 Minkowski gives
||R_N||_p=O_p(sum_(n>N)n^-2)=O_p(N^-1). The first two moments are
ER_N=2/N+O(N^-2), ER_N^2=O(N^-2). To justify a uniform Taylor remainder on a
compact set of exponents, choose A larger than every absolute real part in
that compact set plus two. Taylor's integral remainder is bounded by a
constant times

    R_N^2 [S_N^(-A) + S_N^A + R_N^A + 1].

Increasing A to an integer if necessary makes this elementary bound uniform.
Independence pays the first two terms; the stated higher moments pay the
third. Uniform negative S_N moments follow by domination by a fixed initial
gamma sum. Thus the expectation of the complete remainder is O_K(N^-2), not
an unsupported product of two expectations of dependent quantities.

It follows that, uniformly on each fixed compact K for sufficiently large N,

    m_N(s)=pi^(-s/2) E S_N^(s/2)
          =2xi(s)-2s xi(s-2)/(pi N)+O_K(N^-2).

For a fixed simple zero rho, Rouché on a fixed small isolating circle and a
Taylor expansion give the unique nearby zero

    s_N=rho+rho xi(rho-2)/(pi xi'(rho)N)+O_rho(N^-2).

The gamma-ratio simplification in S17 is correct. The displayed continuum
integral in its section 4 directly converges only for Re z<1/2; there it is a
vanishing integral by the gamma recurrence. Elsewhere the zero statement is
about analytic continuation, not a convergent improper integral.

This supports the fixed-compact and fixed-simple-zero theorem. It supplies
no estimate uniform in a zero height growing with N, and does not weaken the
separate finite-Brownian high-frequency instability theorem.

## R28. Q4 fine-mode and Haar reductions, with the actual measure boundary

For N=2^M and arbitrary complex c, put C(j)=sum_(m<=j)c(m). On each open
Lebesgue cell (j/N,(j+1)/N), the carry field equals
R_j=C(N)-C(j)-C(N-j-1). It obeys R_(N-1-j)=R_j and
R_j-R_(j-1)=c(N-j)-c(j). Thus its continuous squared norm is N^-1 sum|R_j|^2.

At a dyadic half-width ell, summing these differences against the triangular
weights min(t,2ell-t) proves the reflected-window Haar formula. The exact
weight square sum is (2ell^3+ell)/3. Disjointness of open windows at one scale
and a geometric sum over dyadic scales give

    sum_(ell<=L,u)|H_(u,ell)|^2
    <= L^2 sum_(j=1)^(N-1)|c(N-j)-c(j)|^2
    <=4L^2 sum_(m<N)|c(m)|^2.

For c_circle=Lambda-4*shift_4(Lambda)+3log4*1_(powers of 4), the elementary
Chebyshev estimate gives sum|c_circle|^2=O(Nlog(2N)). Dividing first by N for
the Lebesgue field and then by N for the stated PIG normalization proves
O(log(2N)) for all ell<=sqrt(N). Fewer than sqrt(N) coarse coefficients and
the constant mode remain. All statements preserve complex cross terms.

The Fourier bulk estimate follows in the same measure from Parseval and
sin(pi a/N)>=2 min(a,N-a)/N. It is a different orthogonal decomposition of
the same complete uniform field. Restriction to a measurable subset in the
SAME measure is harmless; changing to an arbitrary physical bank is not.

A concrete check of the latter distinction: a nonnegative density
N*1_(0,1/N) integrates to one, but the function 1_(0,1/N) has Lebesgue squared
norm 1/N and weighted squared norm one. Point evaluation is even less
controlled on general L2. A valid transfer needs a bounded density, an exact
finite Gram comparison, or a separately proved sampling theorem. No such
unrestricted transfer is inferred here. The existing source correctly leaves
the global PIG-to-pole adapter open. Fine modes are not a proof of the coarse
mode or mean estimate.

## R29. Carry hinge representations and complete finite counterexamples

For integer T>=3 and h_T(q)=q^-1/2-T^-1/2, extended by h_T(T+1)=0, set
omega_(T,K)=h_T(K)-2h_T(K+1)+h_T(K+2), 2<=K<T. Convexity of x^-1/2 makes the
interior weights strictly positive, and the final weight is
(T-1)^-1/2-T^-1/2>0. Twice telescoping gives

    h_T(q)=sum_(K=2)^(T-1) omega_(T,K)*(K+1-q)_+.

The finite carry matrix is triangular with diagonal (q-1)/(q+1)>0. Its
inverse therefore exists, and applying that linear inverse gives exactly
the signed-response sum in L-90705. Positivity of the weights is not
positivity of the response kernel.

The fresh rational implementation reconstructs EVERY equation of the E=60
linear-hinge inverse and finds c(11)=-2/55, c(10)=53/45, c(12)=131/33.
For T=126 and x=99/100 it reconstructs the complete geometric-atom inverse
and proves -666/10^6<g(9)<-665/10^6. These refute the generic cone and geometric
atom arguments, not the square-root hinge statement.

For the T=894 staged residual, the union of the four eliminated bands is
n=56,...,894. Let B_(q,n)=beta_(n,q), d_n=beta_(n,28)-beta_(n,29), and solve
B_high^T p=d exactly by forward triangular substitution. The residual
functional is

    h_T(28)-h_T(29)-sum_(n=56)^894 p_n h_T(n).

Integer-square-root rational bounds on every n^-1/2 give a strictly negative
interval between -0.000004638 and -0.000004637. This recreates the actual
four-stage failure without floating recursion. No new global sign or
fifth-stage theorem is inferred from that test.

The factor-64 reward is independently generated from

    P(t)=(1-t)^2(1-t/sqrt2)(1+t)(1+3t/4+t^2)=sum q_j t^j.

Writing S_j=sum_(l<=j)q_l and F(m)=m-S_j on 2^j<=m<2^(j+1), the direct
uniform-Pascal action gives

    m(m-1)d(m)=(m-1)F(m)-2sum_(k<m)F(k)
              = A_j+(m+1-2^(j+1))S_j,
    A_j=2sum_(l<j)2^l S_l.

Here S_6=0 and A_6=39(sqrt2-1). The finite affine blocks prove negativity
exactly for 13<=m<=63, followed by the positive telescoping reciprocal-square
tail. The extrema of reward prefixes reduce to m=2,12,63 and the infinite
tail; exact Q(sqrt2) bounds reproduce 9/10<D(M)<21/10. Finite Abel summation
then proves the stated monotone and signed-upward-variation inequalities.
The actual square-root weighted cancellation and cofinal occupation bound
remain open.

## R30. Wavelet, carrier and phase-Hasse transfers

The ratio-eight kernel K0 is continuous, zero at 1 and 8, and piecewise C1.
For w_X(t)=t^-1/2 K0(X/t), Stieltjes integration by parts against the
right-continuous Mertens prefix gives

    G_mu(X)=-integral M(t)w_X'(t)dt
           =X^-1/2 integral_1^8 M(X/y)V(y)dy,
    V(y)=y^-1/2 [K0(y)/2+yK0'(y)].

There are no endpoint or internal jump atoms in w_X. This proves the compact
Abel frame; its Mellin multiplier gives the stated pole exclusion with the
same multiplicities. The critical inverse sum of 2^(j/2) has square-root
mass, so no source-blind desmoothing step has subpower cost.

Direct branchwise differentiation gives

    (I-sqrt2 S2)(I-S2)^2 T = D K0,
    T(y)=(4sqrt(y)-3)1_(y>=1).

This is an a.e./distributional identity for the derivative of the continuous
K0; assigning step endpoint values does not add unmentioned delta masses.
Finite convolution with beta and the positive 67-resolvent yields L-101102.
Signed differentiation does not preserve an available one-sided bound.

The short-sector prime asymptotic in S26 is supported: partial summation on
[X/8,X] gives the main coefficient
kappa0=Khat0(1/2)=8log2(1-2^-1/2)^2. Squarefree composites with all prime
factors within ratio eight occupy O(X/log^2 X) integers. To see uniformity in
the number k of prime factors, put the least prime in a dyadic interval. At
most six such windows are possible for each k; Chebyshev and k! division
give O(X(C/log X)^k) for k<=log_2(X)/10. Above that range all factors belong
to a fixed finite prime set, impossible for large X by squarefreeness.

Classical zero-free-region bounds for Mertens, applied in the compact Abel
frame, make the total G_mu=o(sqrt(X)/log^2 X). Thus the long sector is the
positive cancellation partner of the short prime main, exactly as S27
states. The sum projection removes (-P,+P); regional absolute values do not.
Neither separate asymptotic implies the critical subpower total bound.

For a finite Euler cube with weights 1/P_A and potential
K0(X/P_A)/sqrt(X/P_A), its signed weighted observation is exactly G_mu/sqrt X
once the cube includes every active prime. For X>8 the unit potential is
zero. Any source-owned flow whose divergence is the stated signed cube
therefore gives the Hasse realization. This audits the implication from the
divergence identity; it does NOT construct an arbitrary admissible flow or
reprove the separate PR688 phase-symbol producer. That imported premise is
explicit in the disposition, not silently accepted as a new theorem.

## R31. Finite boxes, source identity and formal-assurance boundaries

The new Pick68 calculation starts with a transparent transcription of the
eight supplied complex rectangles. It reconstructs the complete Hermitian
matrix, proves all eight rational LDL pivots positive after subtracting
2^-137 I, and obtains exactly the source's row-sum radius

    17323180600797004701 /
    2254578897614762850471633369732311757216541650824262434476989171630080.

Subtracting it leaves a strict margin greater than 2^-138. This is an exact
finite-box proof conditional on the rectangles, not a fresh evaluation of
xi'/xi at the very high ordinate. The transcription file declares this limit;
it is not advertised as the original full certificate byte stream.

D-F18: at the frozen PR68 ref, the named retained JSON file has blob
4ca16739f485e1d27c969b965c9614d6faffa383. The integrated packet's advertised
97f722bf2cbdca6ca19ac8134cc718dc7937e9e6 does not resolve in the repository
lookup performed here. Use the verified path/ref/blob instead. This is a
provenance repair, not a negative mathematical result.

The PR71 checker has sound exact complex contraction and midpoint/radius
algebra on its stated same-ordinate inputs. It deliberately returns successful
processing for an unresolved check and uses a separate status field. A caller
must freeze the intended point IDs, nonempty check list and required
whole-matrix status; exit code zero or `verified:true` is not acceptance of a
positive matrix. The 512-bit source rectangles and both special-function
production backends were not regenerated. Retain both controls only at their
already stated conditional-box scope in this review.

The inspected Lean fixed-detector consumer requires explicit proof arguments
for negative mass, Landau singularity, negative-part holomorphy, shifted pole
order, initial source identity, analytic continuation, and zero reflection.
The Landau and holomorphy declarations are Props, not installed axioms. The
consumer genuinely assembles an implication; it does not discharge those
arguments. Its finite-abscissa and nonzero-tail assumptions also exclude the
entire-transform case unless handled separately. They must stay visible.

The registry correctly labels generic wavelet/owner helpers more weakly than
the full physical source theorems. The release runner uses fail-on-error and
executes build, comparators, no-sorry and axiom audits, but those commands
were NOT run here: lake is unavailable in this runtime. Source inspection
is not a new kernel check or a transitive audit of every imported Lean file.
Prior formal evidence remains prior evidence at its recorded exact tree.
