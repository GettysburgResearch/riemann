# IMR26 — ferromagnetic realization of the exact theta moments

Date: 2026-09-10. Status: proposed component proofs and a new research programme;
independent mathematical and implementation review required. **RH and the
all-order Ising realization are NOT proved.** The general Lee–Yang and weak-limit
mechanisms are classical. This is not a claim of priority for connecting RH and
statistical mechanics. Local labels below are not canonical acceptance IDs.

## 1. Why this is a different full-problem construction

The recent gamma-feedback work makes high-degree arithmetic outputs admissible
without making their norms small. The centered-theta determinant represents Xi
without proving that its non-self-adjoint spectrum is real. Raw positive theta
truncations can acquire nonreal zeros. Here finite approximants are instead
chosen from a class whose zero geometry is supplied by an independent theorem:
finite ferromagnets. The unresolved work becomes a CONSTRUCTIVE realization of
the unchanged theta moments inside that class.

This programme has a full sufficient ending, a certified eight-moment starting
point, an open-neighbourhood feasibility theorem, and a necessary restriction on
a successful sequence's couplings. It does not solve the realization at all
orders. No limiting source other than the literal theta law is an acceptable
completion. Neither similarity of tails nor a finite moment match identifies it.

## 2. Source and imported theorems

For t>=0 retain every term of

    phi(t)=sum_(n>=1) [4 pi^2 n^4 exp(9t/2)-6 pi n^2 exp(5t/2)]
                                      exp(-pi n^2 exp(2t)).          (1)

The COMPLETE source is extended evenly. Jacobi inversion identifies that
extension with the classical smooth theta source on the whole real line. With
analytic removals in xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2,

    Xi(z)=xi(1/2+iz)=integral_R phi(t) exp(izt)dt,
    Z=Xi(0)>0,    w(t)=phi(t)/Z,
    mu_(2r)=integral_R t^(2r)w(t)dt,    mu_0=1.                   (2)

These are the classical theta identity and normalization, not a proposed new
formula. On t>=0 every summand in (1) is positive. The n=1 double-exponential
tail and evenness give all exponential and all Gaussian moments. In particular

    M(h)=integral exp(ht)w(t)dt=xi(1/2+h)/xi(1/2)                 (3)

is entire, even and nonzero at zero. No claim about its other zeros is assumed.

Classical inputs:

[E1] Weighted multivariate Lee–Yang: for finitely many spins sigma_i=+/-1,
zero external field, Jij>=0 and ai>=0, the probability law

    Prob(sigma)=Z_J^(-1) exp(sum_(i<j) Jij sigma_i sigma_j),
    X=sum_i ai sigma_i                                             (4)

has characteristic function with only real zeros. See Lee–Yang (1952), and
Newman–Wu (2019), p.11, (21) and the paragraph immediately after it. Their
ordered-pair convention merely rescales Jij; ours counts unordered pairs once.
Zero-weight spins, if present, remain in the Gibbs law as hidden spins; they
are not deleted together with their couplings. Zero couplings ARE allowed.
Graphs need not be connected or lattices. Independent spins form the J=0 special case.

[E2] Even order-one canonical factorization, Hurwitz, elementary probability
weak convergence, and the finite-dimensional implicit function theorem. The
needed uniform-limit argument is proved below. The general weak closure of
Lee–Yang laws is already in Newman–Wu (2019), Theorem 16, using their earlier
weak-convergence theorem; it is not claimed as our new theorem.

[E3] Rodgers–Tao (arXiv:1801.05914v5): the classical de Bruijn–Newman constant
for the actual theta source is nonnegative. We use the consequence that for
EVERY eta>0 the Fourier transform of exp(-eta t^2)phi(t) has a nonreal zero.
Their variable u is our t/2: phi(2u)=2 Phi_RT(u), so a tilt -eta t^2 is the
negative heat parameter -4eta in their convention. No quantitative zero or
simplicity result is imported. The theorem is used only in Section 7, not
in the moment-transfer implication or the finite construction.

The relevant repository source snapshots and exact reading scopes are in
SOURCES.json. Their research proofs are not silently independently accepted.

## 3. IMR1 — finite moment realization pays the whole complex limit

Call X admissible when it has a finite law (4). Put v_X=E X^2. Its MGF is even,
entire of exponential type, normalized at zero. Lee–Yang and paired Hadamard
factorization give

    E exp(hX)=product_k (1+h^2/gamma_k^2),
    sum_k gamma_k^(-2)=v_X/2.                                  (5)

Each gamma_k>0 represents a positive Fourier zero, with multiplicity. The
finite-spin MGF can have infinitely many zeros as an entire exponential
polynomial. Thus (5) is generally an INFINITE convergent paired product, not a
polynomial. Exponential type excludes a Gaussian factor exp(c h^2); evenness
excludes a nonconstant linear exponential. Its value at zero fixes the scalar.
A zero-free degenerate law is handled by the empty product and v_X=0.

Expanding finite subproducts with nonnegative coefficients and then passing to
the locally uniform limit proves

    E X^(2r)/(2r)! <= (v_X/2)^r/r!,
    |E exp(hX)| <= exp(v_X |h|^2/2),       h in C.                 (6)

For the coefficient bound, the r-th elementary symmetric sum of the positive
numbers gamma_k^(-2) is bounded by their total sum to power r divided by r!.
This is not an inference about coefficients from a real pointwise inequality.

**Theorem IMR1.** Suppose a sequence of admissible X_m satisfies

    E X_m^(2r) -> mu_(2r) for EVERY fixed r>=1.                   (7)

Then E exp(izX_m) converges locally uniformly on C to Xi(z)/Xi(0). In particular
(7) implies RH. Conversely, this packet does NOT assert that RH supplies an
Ising representation or that this realization class exhausts Lee–Yang laws.

Proof. Variance convergence gives a uniform bound v_Xm<=V after finitely many
terms. Equation (6) bounds every approximant coefficient and its Taylor tail by
those of exp(V|z|^2/2). First fix a Taylor degree, use (7), then increase the
degree. The limiting moment series is the ENTIRE series in (2), since phi has
all exponential moments. This proves uniform convergence on every complex disk.
Each approximant is nonvanishing in each of the upper and lower half-planes,
and the limit is not identically zero (its value at zero is one). Hurwitz
therefore excludes zeros in those half-planes. These are exactly the off-line
zeros in Xi coordinates. No finite zero census is used. QED.

Here is a quantitative version useful BEFORE solving all moment equations.
If |E X_m^(2k)-mu_(2k)|<=epsilon_m for 1<=k<=m, v_Xm<=V, and r>R>0, then

 sup_(|z|<=R)|E exp(izX_m)-Xi(z)/Z|
 <= epsilon_m sum_(k=1)^m R^(2k)/(2k)!
      +sum_(k>m)(V R^2/2)^k/k! + (R/r)^(2m+2) M(r).              (8)

The last term follows by factoring (R/r)^(2k) from the POSITIVE theta moment
series at the safe real MGF argument r. All complex directions are included.
For example epsilon_m=2^(-m), with all those finite equations solved, suffices.
The certified mu_2<1/20 below implies v_Xm<1 for every m>=1 under that tolerance.
Thus a SINGLE uniform V=1 is available. No uniform inverse/source norm or
unknown reciprocal-zeta estimate remains in this passage to the limit.

**OPEN CONSTRUCTIVE TARGET (IR).** For every m>=1 produce some finite graph,
nonnegative Jij and ai, with

    |E X_m^(2r)-mu_(2r)|<=2^(-m),       1<=r<=m.                 (9)

The graph size, topology, weights and couplings may all depend on m. Their
complex partition functions cannot be replaced by raw theta truncations.
Sections 4–6 solve exact matching only through order eight. That is NOT (IR).

## 4. IMR2 — a literal 28-spin solution through eight moments

Set v=mu_2, and define the STANDARDIZED cumulants

    k4=mu_4/v^2-3,
    k6=mu_6/v^3-15 mu_4/v^2+30,
    k8=mu_8/v^4-28 mu_6/v^3-35(mu_4/v^2)^2+420 mu_4/v^2-630.

Put s2=-k4/2, s3=k6/16, s4=-k8/272. These depend on the exact full source,
not rounded midpoint moments. For a variable a let

    r1=1-25a, r2=s2-25a^2, r3=s3-25a^3,
    e1=r1, e2=(r1^2-r2)/2,
    e3=(r1^3-3r1r2+2r3)/6,
    G(a)=25a^4+e1 r3-e2 r2+e3 e1-s4.                           (10)

The directed source certificate proves that G has exactly one root a in

    0.0220907 < a < 0.0220909.                                 (11)

At that root let b<c<d be the three roots of

    t^3-e1 t^2+e2 t-e3=0.                                    (12)

For EVERY a in (11), the checker verifies three disjoint positive root brackets

    b in (0.0404,0.0406), c in (0.1415,0.1418),
    d in (0.2655,0.2658).                                    (13)

It also verifies G(left)>0 and G(right)<0 for the actual full-source parameters.
One verifies algebraically that G'(a)=100(a-b)(a-c)(a-d). All three roots in
(13) exceed a, so G'<0 throughout (11). This gives both existence and uniqueness
in the declared interval; it is not a numerical solver status.

Take 28 INDEPENDENT symmetric spins and define

    X_*=sqrt(v)[sqrt(a) sum_(i=1)^25 sigma_i
                 +sqrt(b)sigma_26+sqrt(c)sigma_27+sqrt(d)sigma_28].   (14)

The weights are exact reals defined by (2),(10)–(12), not rationals. The finite
law is admissible with every Jij=0. Newton's identities give

    25a+b+c+d=1,
    25a^2+b^2+c^2+d^2=s2,
    25a^3+b^3+c^3+d^3=s3,
    25a^4+b^4+c^4+d^4=s4.                                 (15)

For a symmetric unit spin the cumulants of orders 2,4,6,8 are 1,-2,16,-272.
Cumulants add under independence. Equations (15) therefore prove EXACTLY

    E X_*^(2r)=mu_(2r), r=1,2,3,4; E X_*^(2r+1)=0.          (16)

This matches Xi/Xi(0)'s full Taylor jet through degree eight. Its characteristic
function is explicitly

 cos(sqrt(va)z)^25 cos(sqrt(vb)z) cos(sqrt(vc)z) cos(sqrt(vd)z),  (17)

which has only real zeros. This is an approximant, not the actual Xi function.
The exactness in (16) uses the defined roots, not the displayed decimal scouts.

Readable approximate weights are 25 copies of 0.031950206882282596 and one each
of 0.043258402442199226, 0.080895111058302667, 0.110789371603665563. The machine
receipt retains outward dyadic intervals rather than these rounded numbers.

The same complete moment calculation also proves

    -0.123 < [E X_*^10-mu_10]/v^5 < -0.122.                   (18)

So (14) definitely does NOT match the tenth moment. No fitted-trend claim or
claim that one fixed 28-spin law solves all orders is made.

## 5. IMR3 — this is an interior feasible point, including strict ferromagnets

The solution is not an isolated accidental contact in moment space. Let the
four positive squared group weights vary, with multiplicities nu=(25,1,1,1).
At J=0 the Jacobian of the first four even cumulants with respect to the four
group variables x=(a,b,c,d) has entries

    D_(r,i)=r c_(2r) v^r nu_i x_i^(r-1),  r=1,...,4.        (19)

Its determinant equals

    25 product_(r=1)^4[r c_(2r) v^r]
                         product_(i<j)(x_j-x_i),            (20)

which is nonzero by (11),(13). The moment/cumulant change of coordinates is
triangular with diagonal one. The inverse function theorem proves that the
actual first-four-even-moment vector has an OPEN NEIGHBOURHOOD of realizations
by such positive weighted independent spins. This is a finite-dimensional
statement; it does not imply all higher moment vectors are feasible.

Now set ALL unordered pair couplings in the 28-spin model equal to a common
J. Its partition sums and its four moments are real analytic in J and the
positive weights near (x,0). The implicit function theorem applied to (19)
gives some J0>0 and positive real analytic group weights x(J), 0<=J<J0, that
retain all four moments EXACTLY. For every 0<J<J0 these are STRICTLY
ferromagnetic, connected complete graphs. We have not numerically instantiated
J0 or computed the weight functions. This is an analytic existence corollary
from a certified nonsingular finite starting point, not a claimed numerical
certificate for a chosen nonzero coupling.

No sum over 2^28 arbitrary configurations is required to write this finite
problem. If k of the first 25 spins are positive and eps in {+/-1}^3 records
the other three, the statistical weight is proportional to

    binomial(25,k) exp[J((2k-25+eps1+eps2+eps3)^2-28)/2].     (21)

There are 26*8=208 such grouped configurations. The observable is
sqrt(v)[sqrt(a)(2k-25)+sqrt(b)eps1+sqrt(c)eps2+sqrt(d)eps3].
This gives an explicit exact finite moment map for verified continuation.
The independent seed certificate uses cumulants, not a 208-state nonzero-J run.

## 6. Full source moment certificate — no omitted theta indices or time tail

The accepting program uses only integers and Fraction arithmetic. Intervals
have denominator 2^256 and every operation is rounded OUTWARD. Pi uses the
alternating Machin identity 16 atan(1/5)-4 atan(1/239), retaining 96 terms and
the first omitted positive term in each arctangent. Exponentials use monotone
endpoint evaluation, range reduction to [0,1/8], 96 positive Taylor terms, a
complete geometric remainder, repeated squaring and reciprocal for negative
arguments. The exp degree convention is terms 0 through 96 inclusive.

For raw moments I_j=2 integral_0^infinity t^j phi(t)dt, j=0,2,4,6,8,10, integrate
the first four summands to T=(2,3/2,1,3/4), respectively. The interval width is
1/16 and midpoint halfwidth is 1/32. There are 32+24+16+12=84 cells, ALL retained.
For each exact rational center expand the defining density through degree 80.
The exponential-of-series recurrence is

    h_0=exp(g_0), h_n=(1/n)sum_(k=1)^n k g_k h_(n-k).

Multiply by the EXACT polynomial t^j, then integrate every even monomial in
the scaled cell variable on [-1,1]. Dependence overestimation is allowed;
rounding is never replaced by a midpoint computation.

### 6.1 Complete analytic Taylor error

On the complex circle of radius 1/8 about each center, Re exp(2t)>0, so
|exp(-pi n^2 exp(2t))|<=1. Also Re t<17/8 and |t|<3. Using pi<4 and e<3,

 sum_(n=1)^4 (64n^4+24n^2) 3^10 *3^12 < 10^15.             (22)

This bounds the density times each required real-cell power t^j (j<=12),
with deliberately generous constants. The halfwidth/radius ratio is 1/4.
The omitted analytic density series, after multiplication by t^j and
integration over ALL cell lengths including even reflection, is bounded by

    E_C=16*10^15*(1/4)^81/(1-1/4).                         (23)

We truncate the density, then multiply by the entire finite t^j polynomial;
we do not delete its higher polynomial degrees. This explains the error use.

### 6.2 All four infinite time tails

For j<=12 use t^j<=j! exp(t), t>=0. With q=pi n^2 and v0=exp(2T_n),
substitution v=exp(2t) and v^(7/4)<=v^2 give

 2 integral_(T_n)^infinity t^j phi_n(t)dt
 <=4 j! exp(-qv0)(q v0^2+2v0+2/q).                        (24)

For the four declared endpoints, qv0>150, v0<81 and q<64. For n=1 use
e>8/3 to get qv0>3(8/3)^4>150; the other three follow at once from the same
bound and exp(1/2)>3/2. Hence the total is less than

    E_time=16*12!*(64*81^2+162+1)*exp(-150).               (25)

The complete polynomial factors and the infinite tail integrals are retained.

### 6.3 All theta indices n>=5, for all times

For j>=0 one may enlarge the integrand by exp(t/2), substitute v=exp(2t),
and use log v<=v-1 and v^(3/2)<=exp[3(v-1)/2]. This gives

 2 integral_0^infinity t^j phi_n(t)dt
 <=4pi^2 2^(-j) j! n^4 exp(-pi n^2)/(pi n^2-3/2)^(j+1).   (26)

The ratio of successive right sides for n>=5 is less than
(6/5)^4 exp(-33)<1/2. Thus the ENTIRE index tail is at most

 128 * 2^(-j) j! *625 exp(-75)/(147/2)^(j+1)
 <= E_index=128*625 exp(-75)/(147/2) <10^(-28), j<=12.     (27)

For the second inequality j!/147^j<=1 suffices. The last strict comparison
is reconstructed by the directed exponential primitive. This is not merely
four-term numerical quadrature: (25),(27) pay everything else.

Inflate the integrated I_j intervals by [-E_C,E_C+E_time+E_index], then divide
by the strictly positive interval for I_0. These enclose the full mu_j.
Resulting readable values include

    mu_2=0.04620998623083794157786762086...,
    mu_4=0.00596001729093946021737255468...,
    mu_6=0.00120553389214916389991181320...,
    mu_8=0.00032379772001648245619746251....

The saved artifact contains rigorous intervals, not equality to these decimals.
It then reconstructs the signs in (11),(13), refines the roots by sign bisection,
and encloses (18). Formal cumulant identities are separately checked by direct
rational spin-law convolution through moment order ten. A changed eighth-
order matching claim is not accepted by inference from the lower moments.

## 7. IMR4 — the approximation must lose its removable mean-field reserve

There is a significant constraint on an all-order solution of (IR). For an
admissible model with at least two positive weights, define

    tau(X,J)=min_(i<j, ai*aj>0) Jij/(ai*aj).                   (28)

This depends on the exhibited graph realization, not just the marginal law.
It is zero for sparse models with a missing edge between weighted vertices.
It does NOT measure every coupling or constitute a definition of a
thermodynamic critical temperature.

**Theorem IMR4.** If a sequence of exhibited finite ferromagnets satisfies (7),
then its reserves (28) tend to zero. A fixed positive reserve is impossible,
using Rodgers–Tao's unconditional theorem [E3].

Proof. Suppose a subsequence has tau>=tau0>0. Tilt its spin probability by
exp(-tau0 X^2/2). Since

    X^2/2=(1/2)sum ai^2+sum_(i<j)ai aj sigma_i sigma_j,

the tilted law is a ferromagnet with couplings Jij-tau0 ai aj>=0. This identity
retains the constant spin-self terms, which disappear only in normalization.
By IMR1 the original laws converge weakly to w(t)dt. The positive bounded
continuous tilt therefore gives weak convergence to

    w_tilt(t)=C exp(-tau0 t^2/2) w(t).                       (29)

For completeness this weak limit also preserves the needed entire convergence.
If E X^2<=V, Jensen yields E exp(-tau0 X^2/2)>=exp(-tau0 V/2).
Thus the tilted variance is at most V exp(tau0 V/2), uniformly. The bound (6)
makes their transforms a normal family on C, and weak convergence identifies
it on the real Fourier axis. Every subsequential entire limit is the entire
Fourier transform of (29), by the identity theorem. Hurwitz says it has only
real zeros. But (29) is negative heat deformation of the ACTUAL theta law,
with Rodgers–Tao parameter -2tau0<0. This contradicts [E3]. QED.

Only the minimum complete-graph reserve tends to zero. Individual couplings
can remain large, and sparse interactions are not excluded. This statement
is compatible with Section 5: a FIXED finite moment jet can be matched with
strictly positive couplings. It is retaining a uniform reserve while matching
EVERY order that is impossible.

One corollary is an existential finite obstruction: for every fixed tau0>0,
there exists some moment order m at which the simultaneous tolerance targets
(9) cannot all be met by models with reserve >=tau0. Otherwise selecting one
model at every m contradicts the theorem. No numerical value for that first
obstructing order is provided.

Finally, a successful sequence cannot have bounded spin counts. A weak limit
of probability measures supported on at most K points has at most K support
points (use K+1 disjoint positive-mass continuity neighborhoods otherwise).
Each n-spin law has at most 2^n points, whereas the target has a strictly
positive smooth density. Consequently the spin counts must escape every fixed
bound along a convergent realizing sequence. The 28-spin start is not a
fixed-bank proof mechanism.

## 8. Exact endpoint of the proposed route

The intended argument is

    (IR) for the unchanged arithmetic theta moments
       -> bounded variance and full complex convergence by (6)–(8)
       -> Lee–Yang + Hurwitz
       -> Xi has only real zeros -> RH.

The first statement is OPEN. We have constructed only its exact r<=4 start,
not a sequence with r tending to infinity. The generic IFT gives local
feasibility in those four equations; it supplies no global induction in rank.
A theorem extending these realizations to every finite theta moment vector
would be the load-bearing missing step. It is not implied by a positive
Hankel matrix, an even positive density, the moment problem alone, or by
fitting arbitrarily many UNCONSTRAINED discrete atoms.

The strong-coupling subtraction theorem gives a design restriction rather
than a no-go theorem for this route. A proof must use increasingly many spins,
with no fixed removable quadratic reserve. We propose verified sparse/block
ferromagnetic continuation as described in PROGRAMME.md. This is a new concrete
research direction for the project, not an unconditional proof proposal with
its central lemma left to reviewers.
