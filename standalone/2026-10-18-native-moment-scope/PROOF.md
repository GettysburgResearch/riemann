# Native moments: the family quantifier and exact Euler-mask transfer

Status: **PROPOSED component deductions; independent review required.**
RH and the critical native estimate remain open. These arguments clarify
and refine the target in PR #976; they do not establish it.

Source: PR #976 at `bf845aa1d9d06b0ce62440edc5726de997a888db`, especially
`standalone/2026-10-18-full-moment-audit/CRITICAL_TARGET.md` §§1–3.
The Hecke-family conventions are de Faveri, arXiv:2610.04045v1, §2.5.1.
The analytic continuation, functional equation and polynomial strip bounds
of finite-order Hecke L-functions are classical inputs. See SOURCES.md.

## 1. Keep the literal source and every nonunit zero

Fix a number field F, a finite set S of finite primes, and the fixed family
construction used in #976. All indices below are nonzero integral ideals
coprime to S. Write q(a)=Na. The character chi_a is extended by zero at
nonunits, has order dividing six, and chi_1 is principal. Its primitive
inducing conductor has norm Q_a <= C_F,S q(a). The fixed character data,
F and S do not vary. No field-uniform or discriminant-uniform bound is
claimed. One fixed permitted finite-order twist can be included throughout,
but the principal-sector results below use the untwisted principal row.

For fixed c in R and tau>0 define

    W_(c,tau)(y) = y^(-c) exp[-(log y)^2/(4 tau)] / sqrt(4 pi tau),
    A_a(D) = sum_n mu_F(n) chi_a(n) W_(c,tau)(q(n)/D).       (1)

Every ideal n occurs. The Gaussian, its two infinite tails, and the original
coprimality zeros stay in (1). Tau=1 is exactly the normalization in #976.
Allowing any other fixed tau>0 changes the test, not the logical statements
below; both numerical companions explicitly use tau=1 and c=0.

Absolute ideal counting proves, on Re s>1,

    integral_0^infinity A_a(D) D^(-s) dD/D
          = exp[tau(s-c)^2] / L^S(s,chi_a).                (2)

It also proves A_a(D)=O_(a,R)(D^R) as D tends to zero, for EVERY fixed
R>0 (use a preliminary exponent greater than max(R,1)). The Gaussian
numerator in (2) is entire and nowhere zero. No zero-location-dependent
choice of c, tau, source or detector occurs.

For every a,b, including (a,b)>1, the adopted character law gives

    chi_(a b^6)(n) = chi_a(n) 1_((b,n)=1).                (3)

The right side includes the existing zeros of chi_a. Removing the mask in
(3) changes the source. In particular the rows b^6 are masked principal
rows, rather than independent sextic characters.

## 2. An unconditional convolution identity for all repeated rows

Let T(b) be the finite set of prime ideals dividing b. For any a,b and D>0,

    A_(a b^6)(D)
       = sum_(d: primes(d) subset T(b)) chi_a(d) A_a(D/q(d)), (4)

and conversely

    A_a(D) = sum_(d | rad(b)) mu_F(d) chi_a(d)
                                      A_(a b^6)(D/q(d)).    (5)

These are unconditional identities for the actual Gaussian source. The
sum in (4) includes all powers, including d=1. The sum in (5) is finite.
If a prime already divides a, its positive-power coefficients chi_a(d)
vanish. Thus common primes between a and b are retained without imposing
a new coprimality condition.

Proof. On Re s>1, the Dirichlet series of the left side of (4) is

    (1/L^S(s,chi_a)) product_(p|b) (1-chi_a(p)q(p)^(-s))^(-1).

Expand the finite Euler product into its absolutely convergent geometric
series and use (2), or convolve the coefficients before smoothing. At each
prime p|b, multiplication of (1-chi_a(p)X) by its geometric inverse leaves
1. This deletes precisely those squarefree columns divisible by p; it
neither changes the columns outside b nor inserts a different sign. The
inverse product is the finite squarefree expansion in (5). For fixed b,
the Gaussian flatness at zero makes (4) absolutely convergent: choose
R>1 and sum q(d)^(-R) over the b-smooth ideals. This also justifies direct
coefficient rearrangement. QED.

For any sigma>0 let

    P_sigma(b) = product_(p|b) (1-q(p)^(-sigma))^(-1),
    E_sigma(a;D) = sup_(0<t<=D) t^(-sigma)|A_a(t)|.

The latter is finite for every fixed a,D by continuity and Gaussian
flatness. Formula (4) gives the exact, source-preserving bound

    |A_(a b^6)(D)| <= D^sigma E_sigma(a;D) P_sigma(b).     (6)

This is a bound in terms of a maximal native source envelope, not an
estimate of that envelope. In particular it proves no critical cancellation.

## 3. The average mask cost is linear, with no subpower loss in B

This elementary lemma improves on bounding every mask by q(b)^epsilon.
Let r>0 and sigma>0 be fixed. If I_F(x)<=C_F x for x>=1, then, for every B>=1,

    sum_(q(b)<=B) P_sigma(b)^r <= C_F B C_(F,S,sigma,r),   (7)

where the finite constant is the absolutely convergent positive product

    C_(F,S,sigma,r)
      = product_(p outside S)
          [1 + ((1-q(p)^(-sigma))^(-r)-1)/q(p)].          (8)

Proof. Put f(b)=P_sigma(b)^r and define the nonnegative multiplicative
function g supported on squarefree ideals by

    g(p)=(1-q(p)^(-sigma))^(-r)-1,  g(p^j)=0 (j>=2).

Then f(b)=sum_(d|b) g(d), exactly, since f(p^j)=f(p) for all j>=1.
Consequently

    sum_(q(b)<=B) f(b)
      = sum_(q(d)<=B) g(d) I_F^S(B/q(d))
      <= C_F B sum_d g(d)/q(d).

The last sum is (8). By the mean-value theorem,

    0<=g(p)<= r(1-2^(-sigma))^(-r-1) q(p)^(-sigma).

The prime-ideal sum of q(p)^(-1-sigma) converges, so (8) converges for
EVERY sigma>0 and r>0. This proof uses no independence or prime randomness.
It retains b with repeated primes and all shared-prime cases. QED.

Combining (6) and (7), for any fixed k>=1,

    sum_(q(b)<=B) |A_(a b^6)(D)|^(2k)
      <= C_(F,S,sigma,k) B D^(2k sigma) E_sigma(a;D)^(2k). (9)

There is no restriction B<=D^C in (9). It is uniform over every B,D>=1;
the dependence on a is displayed in E_sigma(a;D).

The unique decomposition u=a b^6, with a sixth-power-free and no imposed
(a,b)=1, now yields the full deterministic lifting estimate

    sum_(q(u)<=H) |A_u(D)|^(2k)
      <= C D^(2k sigma) H^(1/6)
          sum_(q(a)<=H)^flat E_sigma(a;D)^(2k) q(a)^(-1/6). (10)

No row is omitted or counted twice. Formula (10) is useful if a genuine
maximal estimate for the actual flat core rows becomes available. A bound
for A_a at one scale does not automatically bound E_sigma(a;D).

### 3a. An explicit mask constant, uniform in the moment order

The Euler-mask part admits more uniformity than an unspecified fixed-order
constant. This subsection supplies it explicitly; it does not estimate the
native envelope E_sigma(a;D).

Fix 0<sigma<1, put c_sigma=(1-2^(-sigma))^(-1), and retain the counting
constant C_F from I_F(x)<=C_F x. For EVERY real r>=1 the product in (8)
satisfies

    log C_(F,S,sigma,r)
      <= C_F (c_sigma r)^(1/sigma)/(1-sigma)
                              +2 C_F(1+sigma)/sigma.       (U1)

Proof. Set L=c_sigma r and X=L^(1/sigma). Since sigma<1 and r>=1,
L>2 and X>2. For q=q(p), put a(q)=-log(1-q^(-sigma)); then
0<a(q)<=c_sigma q^(-sigma). At q<=X,

    log[1+(exp(r a(q))-1)/q] <= r a(q) <= L q^(-sigma).

Summing even over ALL ideals, partial summation and I_F(t)<=C_F t give
sum_(q(p)<=X) q(p)^(-sigma)<=C_F X^(1-sigma)/(1-sigma).
This part is at most C_F L^(1/sigma)/(1-sigma). At q>X,
r a(q)<=L q^(-sigma)<1. The inequality exp(v)-1<=2v for 0<=v<=1 gives

    log[1+(exp(r a(q))-1)/q] <= 2L q^(-1-sigma).

The complete ideal tail is at most
C_F(1+sigma)X^(-sigma)/sigma, again by partial summation. Its contribution
is therefore at most 2C_F(1+sigma)/sigma. Both estimates retain every prime
ideal, including distinct primes of the same norm, and prove (U1). QED.

Combining (9) and (U1), simultaneously for ALL integers k>=1 and B,D>=1,

    sum_(q(b)<=B) |A_(a b^6)(D)|^(2k)
      <= C_F B [D^sigma E_sigma(a;D)]^(2k)
         * exp[C_F(2c_sigma k)^(1/sigma)/(1-sigma)
                              +2C_F(1+sigma)/sigma].       (U2)

The dependence on k is now explicit. At sigma=1/2 the mask factor is
exp(O_F(k^2)); it is not a uniform constant in k. If sigma is FIXED and
E_sigma(a;infinity)<infinity is supplied, (U2) yields, for every sequence
of integer orders with k(D)^(1/sigma)=o(log D),

    sum_(q(b)<=B) |A_(a b^6)(D)|^(2k(D))
                          <= B D^(2k(D)sigma+o(1)),        (U3)

uniformly in every B>=1. If the supplied envelope is zero, this is trivial.
Otherwise the logarithm of the entire prefactor is
O_(F,S,sigma,a)(k(D)^(1/sigma)+k(D)+1)=o(log D). Thus this is a valid
growing-order statement for the repeated rows of ONE controlled native
source. A zero-free line strictly left of sigma supplies that source
envelope through ANALYTIC_ADAPTER.md; field RH supplies it for a=1 and
every fixed sigma>1/2. The estimate at sigma=1/2 itself is still unknown.
Sigma is not allowed to move toward 1/2 with D in (U3), and no estimate
for the varying flat cores in (10) has been obtained.

For completeness, at sigma=1 the same split at X=2r gives
log C_(F,S,1,r)<=2C_F r[1+log(2r)]+4C_F. For sigma>1 each Euler factor
in (8) is at most (1-q^(-sigma))^(-r), so
C_(F,S,sigma,r)<=zeta_F^S(sigma)^r. These endpoint variants are not used
to infer a critical native bound.

MASK_ASYMPTOTICS.md sharpens (U1) using the classical prime ideal theorem:
`log C_sigma(r) ~ [sigma/(1-sigma)] * (sigma r/log r)^(1/sigma)`.
It also proves the exact fixed-order mean and the corresponding stronger
growing-order transfer. The fully explicit elementary bound (U1) remains
valid independently of that asymptotic refinement.

## 4. The full #976 target forces each fixed Hecke member

Define ZF(Family) to mean that EVERY primitive Hecke L-function inducing
one of these chi_a has no zero in Re s>1/2. By the classical functional
equation and conjugation identity this is GRH for this represented family.
It does not mean GRH for arbitrary Hecke characters or varying number fields.

**Theorem A (exact strength of the growing-family target).** Fix any h>0.
The following statements are equivalent:

1. ZF(Family).
2. For every fixed k>=1 and epsilon>0,

       sum_(q(u)<=D^h) |A_u(D)|^(2k) <<_(k,epsilon) D^(h+k+epsilon).
                                                                    (11)
3. There is an unbounded subset K of the positive integers and e_k>=0
   with e_k/k ->0 along K such that, for every k in K and epsilon>0,

       sum_(q(u)<=D^h) |A_u(D)|^(2k)
                                  <<_(k,epsilon) D^(h+k+e_k+epsilon). (12)

All estimates hold for all real D>=2; constants may depend on the fixed
family, c,tau,h, k and epsilon. No uniformity for k growing with D is used.

Proof of (3)=>(1). Fix an arbitrary ideal a FIRST. For each fixed k, this
same row occurs once D>=max(2,q(a)^(1/h)). Positivity in (12) gives

    |A_a(D)| << D^(1/2+(h+e_k+epsilon)/(2k)).              (13)

Given delta>0, choose a sufficiently large FIXED k in K and then a small
fixed epsilon, obtaining A_a(D)=O_(a,delta)(D^(1/2+delta)). The finite
initial D interval is absorbed into the constant. Gaussian flatness at
zero and this estimate make the left side of (2) holomorphic throughout
Re s>1/2. An inducing primitive L-zero there cannot disappear: its finite
imprimitive Euler factors are holomorphic and nonzero in Re s>0, while the
numerator in (2) never vanishes. Thus the fixed L has no such zero. Since
a was arbitrary, ZF(Family) follows. This is the same principal extraction
argument as #976, applied to EACH fixed row, not only a=1.

Proof of (1)=>(2). The uniform reciprocal lemma in ANALYTIC_ADAPTER.md,
proved from the classical analytic contracts, gives for all fixed
sigma>1/2 and eta>0

    |1/L^S(sigma+it,chi_u)| << (2+q(u))^eta (2+|t|)^eta.   (14)

The extra imprimitive Euler factors, including the primes dividing u to
sixth-power multiplicity, are explicitly included in that lemma. Mellin
inversion of (2), shifted to sigma, then gives

    |A_u(D)| << D^sigma (2+q(u))^eta,                    (15)

because exp[tau(s-c)^2] decays as exp(-tau t^2) vertically. The implied
constant in (15) is uniform in u. There are O(D^h) rows. Choose
sigma=1/2+epsilon/(8k) and eta=epsilon/(8kh), reducing either if convenient
to keep sigma in a fixed compact strip. Then

    sum_(q(u)<=D^h)|A_u(D)|^(2k)
       << D^(h+2k sigma+2kh eta) <= D^(h+k+epsilon).

All horizontal contour edges tend to zero by the same uniform strip
bound and Gaussian decay. Statement (2) trivially implies (3) with e_k=0.
QED.

This does not refute (12), or invalidate #976's implication to field RH.
It identifies the additional scope of that proposed target. The principal
row is sufficient for its desired zeta conclusion; all the other fixed
members are also forced by its stated growing-family quantifier.

## 5. A second moment with slowly growing support has the same strength

**Corollary A1.** Fix L(D)=max(1,log D). ZF(Family) is also equivalent to

    sum_(q(u)<=L(D)) |A_u(D)|^2 <<_epsilon D^(1+epsilon)   (16)

for every epsilon>0 and all real D>=2.

For necessity, (15), ideal counting and L(D)=D^o(1) give (16), using a
slightly smaller sigma-1/2. For sufficiency, every fixed row is eventually
included and the single second moment already bounds it by
D^(1/2+epsilon/2). Apply (2). The same proof treats any fixed even order
and any height L(D) tending to infinity with L(D)=D^o(1).

Thus high orders are one way to overcome a polynomial family-size cost;
they are not an escape from the family zero-free problem. This is a logical
equivalence, not a new unconditional estimate for (16).

## 6. A target confined to the principal source and ALL its replicas

Let ZF(F) mean that the Dedekind zeta function zeta_F has no zero in
Re s>1/2, equivalently its nontrivial zeros lie on the critical line.
This is field RH. For F=Q(sqrt(-3)) it implies ordinary RH, but it also
includes the quadratic Dirichlet factor; we do not call the two statements
equivalent. The finite S deletions have no zeros in Re s>0.

**Theorem B (principal replicas need only the principal hypothesis).**
ZF(F) is equivalent to the following all-B assertion: for every fixed
k>=1, epsilon>0 and every B,D>=2,

    sum_(q(b)<=B) |A_(b^6)(D)|^(2k) <<_(k,epsilon) B D^(k+epsilon).
                                                                    (17)

The constant is independent of B. In fact ZF(F) implies (17) at EVERY
fixed order, whereas (17) at just ONE fixed order, including k=1, implies
ZF(F) because it permits the fixed choice B=2 and contains b=1.

Proof. Under ZF(F), the fixed-principal version of the reciprocal lemma
and (2) give E_sigma(1;infinity)<infinity for every sigma>1/2. Apply (9)
with a=1 and sigma=1/2+epsilon/(2k). This proves (17), uniformly for every
B. Conversely its b=1 term gives A_1(D)=O(D^(1/2+epsilon/(2k))). Let the
arbitrary epsilon tend to zero and apply (2). QED.

If the support is required instead to be B=D^b0 for one fixed b0>0, the
cofinal-order version

    sum_(q(b)<=D^b0) |A_(b^6)(D)|^(2k)
                                      << D^(b0+k+e_k+epsilon),        (18)

with e_k/k ->0 along an unbounded set of fixed orders, is equivalent to
ZF(F) by the same extraction. In the original row coordinate H=D^h,
the complete principal sector has b0=h/6 and natural row factor H^(1/6),
rather than H. Shared primes and EVERY sixth-power replica remain present.

There is a stronger fixed-order version of this last assertion. The prime
replicas carry substantially more information than the single b=1 term.

**Theorem B1 (one fixed order at any polynomial replica height).**
Fix ANY b0>0 and ANY ONE integer k>=1. Field RH is equivalent to

    sum_(q(b)<=D^b0) |A_(b^6)(D)|^(2k)
                                  <<_epsilon D^(b0+k+epsilon)        (18a)

for every epsilon>0 and all real D>=2. In particular, the complete
principal SECOND moment at B=D^b0 is already an equivalent open target;
cofinal orders are unnecessary for this restricted family. This statement
does not replace the full-family target (12) by its principal sector.

Proof. Field RH implies (18a) by (17). For the converse, absolute ideal
counting and the fixed Gaussian give a global bound |A_1(t)|<=C t for
all t>0. For example, integrate the absolute derivative of W against
I_F(x)<=C_F x; the finite constant is C_F integral_0^infinity y|W'(y)|dy.
The boundary terms vanish by the Gaussian at both endpoints. The same
argument works for every fixed c,tau in (1).

Suppose at some stage |A_1(t)|<=C_theta t^theta for all t>0, theta>0.
Let B=D^b0. The classical prime ideal theorem gives at least c B/log B
prime ideals p outside S with B/2<q(p)<=B, for all sufficiently large D.
For each of these prime replicas, the EXACT identity (4) gives

    |A_(p^6)(D)-A_1(D)|
        <= C_theta D^theta sum_(j>=1) q(p)^(-j theta)
        <<_theta D^((1-b0)theta).                       (18b)

No prime-power tail is removed; its geometric sum is included. The
triangle inequality in the finite l^(2k) norm on these prime rows and
(18a) therefore imply, for every eta>0,

    |A_1(D)| <<_(theta,eta) D^(1/2+eta)
                                  + D^((1-b0)theta).   (18c)

Here the prime-row count cancels B from (18a). Its log B factor is
absorbed into eta, choosing the preliminary epsilon after eta and the
fixed k. Using a subset of prime replicas for this LOWER extraction
does not change the hypothesis: (18a) is still over ALL ideals b in
the complete cap, with repeated powers and shared primes retained.

Put lambda=max(0,1-b0)<1. For a fixed eta>0, (18c) improves the global
growth exponent theta to max(1/2+eta,lambda theta). The compact initial
D interval is absorbed into the constant, and Gaussian flatness handles
0<t<2. Starting with theta=1, finitely many iterations give exponent
1/2+eta, since lambda^n eventually falls below that positive number.
All constants may depend on this finite iteration count; there is no
growing-order or uniform-in-eta assumption. Let eta be arbitrary and
apply (2), exactly as in Theorem B. This proves field RH. QED.

This bootstrap is an unconditional implication from the displayed open
moment premise. It uses the classical prime ideal theorem, not CT-31/32
or a conjectural prime-ideal distribution in short intervals: (B/2,B]
is a fixed-ratio interval. At original height H=D^h, it applies with
b0=h/6 for EVERY h>0, still only to the complete principal sector with
its natural H^(1/6) normalization.

The restriction to even orders is unnecessary for this principal criterion.
For ANY ONE fixed real p>0, field RH is likewise equivalent to

    sum_(q(b)<=D^b0) |A_(b^6)(D)|^p
                                 <<_epsilon D^(b0+p/2+epsilon).     (18d)

For p>=1 use the same finite l^p triangle inequality. For 0<p<1 use
|x+y|^p<=|x|^p+|y|^p before averaging the prime rows, then take the
fixed p-th root; its fixed constants do not change any exponent. The
resulting recurrence is still (18c), and the same finite bootstrap applies.
Conversely field RH supplies E_sigma(1;infinity)<infinity, and (6)--(7)
at r=p give (18d), taking sigma>1/2 sufficiently close. Thus even the
FIRST ABSOLUTE moment is an equivalent open target here. This is not a
signed first-moment assertion, and p does not tend to zero with D.

Theorems A and B separate two objectives that should not be conflated:
the full growing family asks for the represented family GRH; the principal
replica sector asks for field RH. Neither target is established here.
The theta moments of #976 do not give either native target without an
additional source-faithful arithmetic estimate.

## 7. An exact all-order growth abscissa, not just a critical implication

The preceding argument works with any fixed theta in [1/2,1] in place of
1/2. This gives a quantitative classification of the missing native bound.

Let Theta_fam be the supremum of the real parts of all nontrivial zeros of
all primitive L-functions represented by the family. Let Theta_F be the
corresponding supremum for zeta_F. Both lie in [1/2,1]. As usual these are
suprema, not assertions that a rightmost zero exists.

For h>0 define lambda_h to be the INFIMUM of theta in [1/2,1] for which
there are an unbounded set K and nonnegative e_k=o(k) along K such that
for every fixed k in K and every epsilon>0,

    sum_(q(u)<=D^h) |A_u(D)|^(2k)
                                  << D^(h+2k theta+e_k+epsilon).     (19)

Define lambda_h^P by replacing the left side with the complete principal
sector sum over q(b)<=D^(h/6), and the right exponent h with h/6.

**Theorem C (native moment abscissas).**

    lambda_h = Theta_fam,       lambda_h^P = Theta_F       (h>0).     (20)

Proof of the lower bounds. If (19) holds at theta, fix each row first and
let k range over the unbounded set, exactly as in (13). One obtains
|A_a(D)|=O_(a,delta)(D^(theta+delta)) for every delta>0. Its Mellin
transform is holomorphic on Re s>theta, so no represented primitive L-zero
can lie there. Thus Theta_fam<=theta. Take the infimum. The same argument
with b=1 gives Theta_F<=lambda_h^P.

For the upper bounds, suppose first Theta_fam<1 and choose any
Theta_fam<sigma<1. The proof of Lemma R applies with its zero-free boundary
1/2 replaced by Theta_fam: choose alpha0,alpha strictly between Theta_fam
and sigma. It supplies uniform subpower reciprocals on Re s>=sigma.
Consequently the contour argument proves (19) with theta=sigma, e_k=0,
at every fixed k. Let sigma decrease to Theta_fam in the INFIMUM.
If Theta_fam=1, absolute Euler convergence on Re s=1+delta, with delta
chosen after k and epsilon, gives (19) at theta=1 and e_k=0. This also
proves that the set defining lambda_h is nonempty. For the principal
sector use the fixed-principal version of the same analytic adapter and
the linear mask transfer (9); its row cost is exactly D^(h/6). QED.

No loss-free bound at the boundary exponent, absolute Mellin convergence
ON its boundary line, or exclusion of zeros ON that line is inferred.
Every displayed moment estimate retains its arbitrary epsilon loss.
Equality of the infima with 1/2 is equivalent to the corresponding open
zero-free half-plane, without asserting endpoint Mellin convergence.
These identities do not evaluate the unknown suprema; §8 separately uses
an imported upper boundary. Formula
(20) explains precisely why a proved source-specific improvement in the
native all-order exponent would be substantive arithmetic progress, and
why the theta or positive-numerator envelope cannot simply be substituted.

### 7a. The principal growth abscissa needs only ONE fixed order

The prime-replica bootstrap sharpens the principal part of Theorem C.
For fixed b0>0 and k>=1 let Gamma^P_(b0,k) be the infimum of real gamma
for which, for every epsilon>0,

    sum_(q(b)<=D^b0) |A_(b^6)(D)|^(2k) << D^(gamma+epsilon)

holds for all real D>=2. Then

    Gamma^P_(b0,k) = b0 + 2k Theta_F.                    (20a)

In particular, its infimum over k or a cofinal-order limit is unnecessary.
The principal SECOND moment's exponent already encodes the same rightmost
zeta-zero supremum, after subtracting its true row count and dividing by two.
This is an identity of unknown growth abscissas, not an evaluation of one.

For the upper bound, take any sigma>Theta_F, apply the fixed-principal
reciprocal adapter and the linear mask transfer (9), then let sigma
decrease to Theta_F in the infimum. The case Theta_F=1 uses absolute
Euler convergence just as in Theorem C.

For the lower bound, Theorem B1's proof works with ANY fixed alpha>0
in place of 1/2: the premise D^(b0+2k alpha+epsilon) gives the recurrence
theta -> max(alpha+eta,lambda theta), and hence A_1(D)=O(D^(alpha+eta))
for every eta>0. Its Mellin transform excludes zeta zeros in Re s>alpha.
If Gamma^P_(b0,k)<b0+2k Theta_F, choose a gamma strictly between these
values with gamma>b0. Such a gamma is an admissible upper exponent by
the defining infimum and upward closure. The bootstrap with
alpha=(gamma-b0)/(2k)>0 contradicts the definition of Theta_F. QED.

There is also a useful finite-order enclosure for the FULL family. If
Gamma_(h,k) is the analogous infimum for q(u)<=D^h, then

    h/6 + 2k Theta_fam <= Gamma_(h,k) <= h + 2k Theta_fam. (20b)

The upper bound is the uniform adapter. For the lower bound, fix ANY
core row a and use the prime replicas a p^6 with
q(p) in (B/2,B], B=(D^h/q(a))^(1/6), omitting the finitely many p|a.
There are at least c_a D^(h/6)/log D such rows for large D. Identity (4),
now with coefficients chi_a(p)^j of modulus one, gives the error in
(18b) with b0=h/6, up to a fixed a-dependent factor. The same finite
bootstrap shows that a full-family exponent gamma forces EVERY fixed
member to be zero-free to the right of

    alpha=(gamma-h/6)/(2k), whenever alpha>0.

Every fixed row starts with its unconditional O(t) bound. Constants may
depend on that row, which is sufficient for this zero-exclusion implication.
If the lower inequality in (20b) failed, choose gamma between the two
relevant values with gamma>h/6 and reach a contradiction as above. This
does not claim equality at either end of (20b), or reduce the full-family
moment premise to the principal-sector one.

For example, when 0<h<=k the displayed S6 exponent from #976 simplifies
to h/6+2k exactly. A genuine power saving Delta in that COMPLETE native
moment, 0<Delta<2k, would therefore force
Theta_fam<=1-Delta/(2k) by (20b). This is a source-specific implication
explaining the arithmetic content of such a saving; it is not a claim
that every proof strategy must obey a positive-envelope obstruction.

## 8. An explicit native power improvement using a separately named input

The new abscissa adapter also gives a concrete upper bound, beyond a scope
clarification. Here the external input must stay visible:

    CT-31/32: the finite-order Hecke nonvanishing statement in Cureton–Thorner
    2610.00200v2, cor:Hecke (following thm:dedekind), is adopted as stated.

The primary statement and relevant source were freshly read and hash-pinned;
its complete deep proof was not independently reconstructed. The separate
CT_BUILD_RECEIPT.json gives the actual external Lean build/CI observations.
This corollary is a SOURCE-QUALIFIED DEDUCTION from that printed theorem,
not a new proof or independent acceptance of CT-31/32.

Under that explicit input, for every fixed k>=1, h>0 and epsilon>0,

    sum_(q(u)<=D^h) |A_u(D)|^(2k)
                               << D^(h+31k/16+epsilon),               (21)

and, uniformly for EVERY B,D>=2,

    sum_(q(b)<=B) |A_(b^6)(D)|^(2k)
                               << B D^(31k/16+epsilon).               (22)

Proof. In Lemma R replace its zero-free boundary 1/2 by 31/32, choose
sigma>31/32 with a sufficiently small fixed buffer, and use the same
uniform conductor/imprimitive adapter. Sum (15) over q(u)<=D^h, taking
the preliminary conductor exponent small relative to epsilon/(kh).
This proves (21). For (22), the fixed-principal contour gives the bound
for E_sigma(1;infinity); apply (9) and choose 2k(sigma-31/32)<epsilon.
QED. No constant uniform in k or field is claimed.

Combining (21) with the stated S6 native theorem in #976, its excess over
the H D^k scale, at H=D^h, can be sharpened to

    min( max(0,k-5h/6,k/3-h/6,5k/6-2h/3), 15k/16 ).     (23)

This is strictly smaller than that displayed S6 envelope for k>40h/3.
For example h=1,k=32 gives

    old S6 envelope: D^(385/6+epsilon),
    CT-input envelope: D^(63+epsilon),

a power gain of 7/6 in the COMPLETE 64th native moment. This comparison
retains the original row height, all ideals, all masks and the same fixed
Gaussian. It is not an assertion of the best bound among every historical
packet, every source or every specialized field.

The limiting excess rate supplied by this external input is 15/16, still
strictly positive. It recovers its input zero-free boundary 31/32; it does
not improve that boundary or approach 1/2. Reusing (21) to claim an
independent proof of CT-31/32 would be circular. The unconditional mask
identities, average-mask lemma and exact abscissa classification above
do not use CT-31/32 at all.
