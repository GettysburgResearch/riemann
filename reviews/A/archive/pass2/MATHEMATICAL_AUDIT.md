# Reviewer A — independent mathematical reconstructions and required corrections

Baseline: `main@8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
This is an informal mathematical review, not a Lean verification. Source commits and
file identities are in `SOURCES.tsv`; the numbered findings below are review-local
identifiers, not new canonical research claims. No verdict here proves RH.

<a id="a-m01"></a>

## A-M01. The #786 minority-sign argument has a false inequality

Source: #786, `standalone/2026-09-02-ninety-percent-descent/PROOF.md`,
`fc550cb0531e7abbc438a9b6eefa5ca11f90abc7`, blob
`f79f8b2849b4b357665c9a91010c4d2051597c70`; compare #777 L-108301 at
`399410ba3b38e135ad6961a850bdaa02fa9cbba2`.

For a two-colour path, let V be the number of colour-changing edges and m the
minority count. The valid inequality is V <= 2m: assign each changing edge to
its minority endpoint, of which there are at most two incident edges. There is
no general lower bound V >= m. The sequence `++++----` has V=1 and m=4.
Longer two-block sequences make m arbitrarily large with V=1.

At consecutive simple zeros c_j of f^(K), the signs of f^(K+1)(c_j) alternate.
Consequently, for rho_j=f(c_j)/f^(K+1)(c_j), the exact equivalence is

    rho_j rho_(j+1) > 0  iff  f(c_j) f(c_(j+1)) < 0.

Thus M-1-V counts **intervals with opposite endpoint signs**, not all zeros
inside those intervals. It certifies one zero per such interval, not exactly
one zero there. An interval can contain additional zeros.

The minority criterion in L-108301 is sufficient for the desired yield. It is
not equivalent to that yield, and it is not equivalent to a 95% sign-change
law. In particular m/N < 0.0495 gives V/N < 0.099, not V/N < 0.0495.
The false inequality and the stronger stated interpretation must be removed.

Disposition: retain the endpoint-sign identity and V <= 2m; reject the literal
lower inequality and the asserted equivalence of the minority gate with a
95% mesh law. This does not settle the actual Xi minority estimate.

<a id="a-m02"></a>

## A-M02. #786 does not prove its cofinal 90%-gate refutation

The proof advertises a limsup lower bound >=0.35 using finite observed
sign-change rates and a phase visit near a particular large height. A finite
height, however large, is not a sequence tending to infinity. Moreover its
own fixed-K formula gives delta_K(t) tending to a limiting phase modulo pi.
A finite sweep through other phases does not establish infinitely many late
visits to those phases.

There is an independent analytic problem. For fixed K and a fixed n>=2,

    [ ((theta'(t)-log n)^2+pi^2/16)
      /(theta'(t)^2+pi^2/16) ]^(K/2) -> 1.

Accordingly the absolute estimate displayed for the nonleading
Riemann–Siegel terms does not tend to zero. With the actual truncation at
sqrt(t/(2pi)), its size is not controlled by the n=2 term alone; without that
truncation the displayed sum is not even a convergent bound. Differentiating
Riemann–Siegel also requires a differentiated remainder and treatment of the
moving endpoint. Neither follows merely from differentiating its first term.

A valid all-height mesh theorem would require an explicit uniform remainder
small enough for zero localization. A valid asymptotic refutation would then
still require a proved cofinal sign statistic, not the sampled statistic.

Disposition: `PROOF_GAP` for T-109201 in its global mesh interpretation and
R-109203 in its advertised unconditional/cofinal interpretation. Preserve
X-109202 as a finite, non-directed numerical record at its actual heights.
Do not replace the open #744/#772/#777 global gate by an accepted refutation.
This finding is independent of whether that open gate is ultimately true.

<a id="a-m03"></a>

## A-M03. The #786 Fejer contour argument is invalid; a narrower conclusion is repairable

Source: #786 `standalone/2026-09-01-fixed-detector-dichotomy/PROOF.md`, blob
`36fe5753442672904f1d6cb9ea1b1c5349c4005a` at the same source head.

The proposed contour weight w(s)=1-|Im(s)|/T is not holomorphic. Its vanishing
on the horizontal edges does not license a residue-theorem contour shift.
One cannot obtain the stated weighted residue sum by treating w as analytic.
For higher-order poles, an analytic weighted residue calculation would also
have to retain derivatives of the weight. Thus the deposited argument is not
a self-contained proof of its Ingham lemma. This is a proof defect, not a
claim that the appropriate classical oscillation theorem is false.

Here is a direct repair of the **no-real-main-term wavelet conclusion**.
Assume D is real, locally integrable and of finite power growth. Its Mellin
transform F(s) initially converges on a right half-plane. Suppose its
meromorphic continuation is holomorphic at every nonnegative real s and has
a genuine pole at i*gamma, gamma != 0. Then D cannot be eventually
nonnegative almost everywhere, and it cannot be eventually nonpositive
almost everywhere either.

Proof. Under eventual nonnegativity remove a bounded initial interval. Its
Mellin transform is entire, while the remaining nonnegative tail has a finite
abscissa of convergence sigma_c. Landau's theorem says that a finite
sigma_c is a singular point on the real axis. Since F is holomorphic at
every nonnegative real point, sigma_c<0 (or sigma_c=-infinity). The tail
transform would therefore be holomorphic on a half-plane containing the
imaginary axis. This contradicts the pole at i*gamma. Apply the same argument
to -D for the other sign. QED.

For the minimal ratio-eight Mobius wavelet, use its **actual** multiplier

    Khat(s)=(s+3/2)(1-sqrt(2)*2^(-s))(1-2^(-s))^2
             /[s^2(s-1/2)],
    F(s)=Khat(s)/zeta(s+1/2).

The apparent real singularities at 0 and 1/2 are removable; on the other
nonnegative real points there is no zeta zero. A critical-line zero with
14<gamma<15 is not annihilated by the dyadic factors: 2pi<gamma log 2<4pi.
The factor with modulus sqrt(2) cannot vanish on the imaginary axis. Thus the
classical validated existence of that zero supplies a genuine pole. Its
simplicity is not needed. This gives arbitrarily late signs of both kinds,
without RH or linear independence of ordinates.

Reading/trust boundary: the analytic inputs here are Landau's theorem, the
standard real-axis nonvanishing facts, and the validated first-zero location;
the review does not rerun a zero census or machine-prove those inputs. The
new argument repairs R-109002 at this precise source, not the whole broad
catalogue or the flawed proof of L-109000.

Finally, `RH + absolute residue summability => eventual positivity` and
`eventual positivity => RH` do **not** establish that residue summability is
necessary, that positivity is equivalent to their conjunction, or that the
criterion is strictly stronger than RH. Rewrite #786's stronger labels as
the two implications actually justified. A box-smoothed constant main term
must not be reclassified as a logarithmically growing main term.

<a id="a-m04"></a>

## A-M04. A two-factor counterexample to #777's additive Fourier-band trace

Source: R-108350 at #777 head `399410ba3b38e135ad6961a850bdaa02fa9cbba2`,
blob `0aeae02f84d4166ac371064579e6168390f2b7e7`.

The one-factor Fourier density is correct. The passage from it to the exact
n-factor formula (R-108350.3) is not: multiplication by preceding Blaschke
factors in a Takenaka basis does not preserve Fourier-band mass.

Take distinct upper-half-plane nodes i and 2+i. On the boundary a normalized
orthonormal Takenaka basis is

    e1(x)=1/[sqrt(pi)(x+i)],
    e2(x)=(x-i)/[sqrt(pi)(x+i)(x-2+i)].

The exact partial fractions are

    (x-i)/[(x+i)(x-2+i)] = i/(x+i)+(1-i)/(x-2+i).

In the half-line Fourier convention of the source, a common unimodular
constant is irrelevant and the transforms are sqrt(2)e^(-t) and
sqrt(2)e^(-t)[i+(1-i)e^(-2it)]. Hence the true trace density is

    2e^(-2t)[4-2cos(2t)-2sin(2t)],  t>0,

not 4e^(-2t). Both basis vectors have norm one: integrating this density on
the whole half-line gives two.

Let r=e^(-pi) and choose the band [pi/2,pi]. Direct integration gives

    actual trace = 6r-2r^2,
    advertised additive trace = 2r-2r^2,
    difference = 4r > 0.

These are two distinct nodes, so the counterexample does not depend on
allowing confluent zeros. The deposited formula and any exact asymptotic
claimed from that formula must be withdrawn or replaced.

There is another independent scope error. Writing arbitrary real polynomials
F,G with E=G+i*epsilon*F does not impose G=F^(K). It realizes an unrestricted
entire companion, not necessarily the direct derivative companion. A
counterexample in that larger class cannot refute an actual Xi-specific or
fixed-derivative theorem without the additional adapter.

<a id="a-m05"></a>

## A-M05. A corrected shrinking-band obstruction, with its proper nonnative scope

The failure above does not make a generic lower-capture theorem true. A
replacement counterexample can be proved without the invalid additive trace.

Let R>=2, n=floor(R log R), a_j=(j-(n+1)/2)R/n, and

    y=1/(100n^2),   b_j=a_j+i*y.

All nodes lie in [-R,R]+i(0,1]. Let phi_j be their normalized Cauchy kernels
and G their Gram matrix. Its diagonal is one and

    |G_ij| <= 2y / |a_i-a_j|  (i != j).

The off-diagonal row sum is at most
4yn(1+log n)/R <= 1/(25R), using 1+log n<=n. Thus G>=I/2.
For a Fourier band I=[X,X+Delta] contained in the positive half-line let H be
the Gram matrix after band restriction. The exact projection trace is
Tr(G^(-1)H), not a sum of uncorrected kernel traces. Since H>=0,

    Tr(G^(-1)H) <= 2Tr(H) <= 4ny Delta.

Choose Delta=C/n. The trace is at most C/(25n^2), whereas the finite Blaschke
product has degree and winding n. This provides a genuine counterexample
with O(R log R) nodes and shallow heights. Unlike the original attempted
example its heights decrease with R; no fixed-height-one conclusion is
claimed. The proof is finite-dimensional Gram algebra plus the correct
one-kernel Fourier formula.

This is a **nonnative** control for the unrestricted inner/entire-companion
class. It supplies no counterexample to actual Xi, no derivative-companion
realization G=F^(31), and no refutation of the global arithmetic winding gate.
The review should retain the warning about lower capture at that scope.

<a id="a-m06"></a>

## A-M06. Repairing the RH-to-PRIMLS direction, with all uniformities explicit

Sources: #786 L-109101/T-109100; #757 primitive-pair large-sieve packet at
`b870366141fe8d5f43d5b81f6e50a67d2a888070`, blob
`2abd49b975837c924009e33912e786b4b720e29c`.

Under RH the standard fixed-offset reciprocal-zeta bound is: for every
eta>0 and every delta>0,

    1/zeta(sigma+it) <<_(eta,delta) (2+|t|)^delta,
    sigma >= 1/2+eta.

Use separate eta and delta; their exponents may be renamed at the end. For
q>=1 the finite Euler multiplier is uniformly bounded by C*q^delta on that
half-plane. Indeed for all sufficiently large primes p,
(1-p^(-1/2-eta))^(-1)<=p^delta; the finitely many remaining primes contribute
one fixed constant. No prime-number asymptotic is needed for this step.

For

    S(y;q,xi)=sum_(n<=y,(n,q)=1) mu(n)n^(-1/2-i*xi),

start Perron at **s=c+it**, with c=1/2+1/log(2y), not at a segment whose
centre is shifted by -i*xi and then silently treated as zero-centred. The
Dirichlet function in the integrand is

    [1/zeta(s+1/2+i*xi)] prod_(p|q)(1-p^(-s-1/2-i*xi))^(-1).

For half-integer y choose T=y^3(2+|xi|)^2. The usual absolute truncated
Perron error is O(y^(1/2)log^2(2y)/T); it uses |mu(n)n^(-i*xi)|<=1 and is
uniform in xi and q. Shift to Re(s)=eta>0, crossing no pole under RH. The
new vertical segment is at most

    C y^eta q^delta (2+|xi|+T)^delta (1/eta+log(2T)),

and the horizontal segments are at most

    C y^c q^delta (2+|xi|+T)^delta/T.

Choosing eta and delta sufficiently small in terms of a requested epsilon
proves

    |S(y;q,xi)| <<_epsilon (2y)^epsilon
                                  [q(2+|xi|)]^epsilon.

Move a general endpoint to an adjacent half-integer; at most one term
changes. Endpoints below two are bounded directly. This proves the required
uniform sharp-prefix lemma; it does not prove RH.

Now use the exact autocorrelation Fourier representation from #757. With
A in {1,67,67^2}, the primitive rectangle is

    G(d;T)=(1/(2pi)) int |Khat_bd(xi)|^2 A^(i*xi)
             sum_(k<=T/A,(k,67d)=1) mu(k)/k
             S(T/(Ak);67dk,-xi) S(T/k;67dk,xi) dxi.

All sums are finite before integration. This identity is just Mobius
inversion of (a,b)=1, retaining the additional coprimality with k. In the
product of the two S bounds the k^(-2epsilon) from the two lengths cancels
the k^(2epsilon) from the two sieve factors. Thus, for small delta>0,

    |G(d;T)| << (dT)^(2delta) log(2T)
                  int |Khat_bd(xi)|^2(2+|xi|)^(2delta) dxi.

The integral is finite for delta<1/2 since K_bd is compact BV and its
Fourier transform is O((1+|xi|)^(-1)). A panel is the difference of two
rectangles, uniformly in H<=U<=2H. Squaring and summing d^(-1) gives

    sum_(d<=D) d^(-1) sup_U |P(d;H,U)|^2
         << (2DH)^(4delta) log^3(2DH).

Exponent renaming proves PRIMLS under RH. Together with the source-locked
#757 beta consumer, this repairs PRIMLS <=> RH, including the uniform sieve
and endpoint quantifiers. The exact central-channel reduction of #760
remains compatible with this argument.

External-input boundary: this is an analytic proof conditional on RH and
the classical reciprocal-zeta/Perron theorems, not a new unconditional
Mobius bound. No numerical test certifies those analytic inputs.

<a id="a-m07"></a>

## A-M07. What the PRIMCAR comparison still does not prove

The literal central height layer identity

    A_t(d)=2*mu(t)/sqrt(t) * c_t(d)

with its squarefree and sieve indicators is valid. Replacing c_t(d) by a
constant gives a different model. Its coprimality condition changes with t;
a size bound and smoothness of the ratio kernel do not make that arithmetic
weight constant or slowly varying.

Accordingly a short-interval theorem for unweighted Mobius does not establish
the original weighted, sieved PRIMCAR square function without a transfer
estimate. An aligned dyadic block sum and an average over all translated
intervals also require an actual comparison, with all shorter-scale terms
and maximal losses retained.

The claimed use of Ng's explicit formula must specify a precise error bound.
The statement that any O(x^(1/2-delta)) error suffices is false at this level:
its trivial squared integral over [H,2H] is O(H^(2-2delta)), which need not be
O(H^(1+epsilon)) at interval length one. For the high-zero part, one cannot
bound a mixed phase solely by |gamma-gamma'| without checking shifts in x;
a safe first step is to separate the two endpoint sums before mean-square
estimation.

Disposition: retain the exact layer identity and the explicitly labelled
frozen-weight model. The paper's displayed route `RH+J_-1 => literal
PRIMCAR` is not an accepted implication. T-109102 needs the precise imported
formula, a valid mean-square calculation and the block/weight adapters.
Nothing here refutes PRIMCAR; COREAGG <=> PRIMCAR remains the separate exact
all-positive-exponent equivalence proved in #760.

<a id="a-m08"></a>

## A-M08. Common mother, completed sources, and the native F1 repair

The #715 multiplier identities are direct. The compact filter annihilates
sqrt(y), 1 and log(y) beyond y=16. Zero endpoint value and first logarithmic
derivative make Phi_* globally C^1. The Bezout reconstruction
Phi_*=-(2/3)CV+(4/3)XD is exact, with no critical inverse. For a real compact
field the integration-by-parts orthogonality gives the advertised Gram
identity; Poincare on a one-octave source shell yields the strict 0.934564
upper bound. Neither determinant nor contraction signs the arithmetic field.

The squared-core estimate in L-102505 is a **relative operator estimate**:
O(log Z) times the norm of the unsquared input. It cannot convert a
power-sized unsquared owner field into an absolute subpower error.

For the literal unmarked squarefree Euler–Beta field in R-103121, the live
core coefficient is strictly positive by the finite-product inequality and
absolute convergence, and its detector moment at 1/2 is strictly negative.
Landau's squarefree-semiprime asymptotic and the source's three-range core
split give the negative main term. This refutes that exact producer, not RH.

Important extraction repair: deleting a fixed **owner prime** does not change
the leading semiprime asymptotic for a fixed core. Deleting or changing fixed
**core coefficients** generally changes the convergent core constant. A
sentence that all finite exceptions leave the leading coefficient unchanged
must not be used to transport the result to duplicate-labelled 67 data.
Retain the literal source formula and separately prove the normalization and
sign of any modified coefficient. The ordinary Mobius wavelet is not that
completed semiprime source.

The #730 repair preserves the ordinary source:

    a_U=1*nu_U,  a_U*mu=nu_U,
    b_U=a_U*a_U*mu=a_U*nu_U,  nu_U=mu 1_(n>U).

Both factors vanish up to U and b_U vanishes up to U^2. Thus the QPTI
semiprime main does not transfer merely because an atom has shape pqc^2.
The finite Chow/Hodge identity is exactly a centred variance identity; it
survives the withdrawal of a cofinal physical-trace claim.

The reflected mismatch identities are correct on a fixed finite horizon
where both coloured factorizations give the same convolution. Norms of
finite-horizon fields give an x-independent baseline, but a horizon change
must not be differentiated as if that baseline were fixed. The dyadic-frozen
cutoff of L-105504 is the appropriate separate device. Its derivative Type-I
bound is O(U^2/sqrt(X))=O(X^(-1/6)), not the smoother K1 rate. The remaining
one-sided variation is open; positivity of the mismatch norm does not give
the sign of its third-order differential image.

<a id="a-m09"></a>

## A-M09. Reverse Rolle, curvature and high derivatives: retain the exact quantifiers

L-107100's multiplicity-sensitive formula follows by counting distinct poles
of f'/f and oriented crossings at nonshared critical points. A parent zero
of multiplicity m contributes m-1 shared derivative zeros but only one sign
jump of f'/f. Eliminating the distinct-zero count gives

    N_I(f)=N_I(f')-sum_c(r_c+iota_c)+epsilon_I(f).

The wrong simple extremum costs two. Shared zeros, stationary critical
points and endpoint signs cannot be dropped. L-107101's conjugate-pair
curvature has negative integral 2/b, but the resulting budget can be
infinite and it does not count shallow clustered critical wells without
separation and depth estimates.

L-107102's real Laguerre reserve follows from its explicit bounds
6(delta/u0)+8|t|delta <=14/32<1/2. Its Rouché conclusion requires the
comparison on the complete relevant disk boundaries as well as the
rectangle; enlarge the displayed height by the disk radius or decrease the
absolute constant. The weighted-tail hypothesis must be stated against a
quantified margin before a numerical constant or growing Xi window is
extracted. A general concentration implication is not an actual-Xi saddle
estimate, and an actual high-derivative entry is not low-order descent.

For older #744 descendants, keep original-height, rescaled-height, fixed-K,
growing-K and finite-window statements separate. A global cumulative zero
proportion is not automatically the same proportion on every (T,2T) block.
A source theorem or an explicit conversion is required wherever a dyadic
consumer uses it. This is an extraction question, not a claim that the
original Conrey theorem is false.

<a id="a-m10"></a>

## A-M10. The W-pinch disposition is conditional; the explicit Conrey tail needs a proof

At #742's inspected head the final controlling W-pinch route retains the
corner residual in its stated units **and CLUSTER-3**. Earlier prose saying
there is exactly one open FAR-WIN statement is superseded. The local weld's
original bounded-derivative condition was amended because a genuine
half-power term has derivative of order |s-s0|^(-1/2). Preserve that amendment.
An asymptotic refutation conditional on the remaining interfaces is not an
unconditional refutation of HHFE.

In L-105075 an O(m^(-2)) asymptotic alone proves qualitative summability of
the relevant weights, not the explicit tail beginning at m=6 with coefficient
one. The all-m inequality or a validated finite-to-uniform tail theorem must
be supplied to accept 1.4457. Checking m<=4000 does not by itself prove the
infinite quantifier. Retain a qualitative summability statement on the
stated Conrey input and keep the explicit constant conditional on a uniform
tail bound.

The pointwise-pricing lower bound theta_0>=8/5 follows algebraically from
C_omega>=3, A'>=16/15 and c_0<=1, once those sharpness inputs are proved. It
is a no-go for that specific pricing class, not for converse Rolle in general.
The 4.5692 end-to-end number is vacuous as a proportion bound and must not
be advertised as a new zero proportion. A divergent majorant is not proof
that the actual defect series diverges.

<a id="a-m11"></a>

## A-M11. Hardy source orientation and the raw-innerness boundary

For an inner U, M_U^*k_b=conjugate(U(b))k_b. Therefore in a Cauchy-kernel
column basis with Gram G and V=diag(U(b_j)), the projected-source Gram is
V G V^*, not V^* G V. The latter can be a different matrix with a different
contraction or determinant verdict. Confluent jets and an outer metric
must be transported in the same adjoint convention. Algebraic covariance
in an unspecified convention is not a physical-source certification.

For any nonzero entire h with a zero b of multiplicity m, the reduced
companion Theta=(h-i*lambda*h')/(h+i*lambda*h') has

    Theta(b)=-1,  Theta'(b)=-2i/(lambda*m).

Consequently a zero in C+ contradicts holomorphic contractivity there by the
maximum-modulus principle. For actual real-even Xi, contractivity of its
raw zeroth companion for one fixed lambda>0 implies RH. Conversely under RH
its paired real-zero product gives the required logarithmic-derivative
sign, and Rolle/Hurwitz gives the fifth-derivative component. This retains
the source's equivalence, including multiplicities and the exclusion of
lambda=0.

Thus an actual-Xi Hardy theorem assuming both raw components are inner is
RH-conditional. An arbitrary supplied-inner theorem is not itself circular;
its attempted use as an unconditional Xi producer would be circular. A
quotient-of-inners representation of the ratio is weaker than asserting
that both raw components have one common **inner** prefactor. In particular
|U(b)|>=|Theta_0(b)| requires that prefactor to be contractive.

Finite companion nodes, local raw values and their Cauchy Gram matrices can
remain unconditional. They do not establish a complete denominator,
cofinal physical capture, global raw innerness or an omitted-direction bound.
The bare model-space trace and the physical numerator-projected trace must
be separate nodes. A countable exceptional-parameter theorem does not name
a usable rational parameter or certify a prescribed varying calibration.

<a id="a-m12"></a>

## A-M12. Architecture E negative squares: a full local-pole argument

This is a self-audit/repair of A-related Architecture-E material; independent
acceptance belongs to a non-author reviewer.

Let h=X'/X and

    K(z,w)=[h(z)-conjugate(h(w))]/[conjugate(w)-z].

The genus-one product gives the normally convergent zero-feature expansion.
Real zeros contribute PSD rank-one kernels; each distinct nonreal conjugate
pair contributes one positive and one negative feature. This proves the
upper bound on negative squares when finitely many such pairs exist.

For the lower bound, do not rely only on finite feature independence while
ignoring the infinite positive background. Choose any k distinct upper
zeros b_j with multiplicities m_j and set z_j=b_j-i*m_j*epsilon. For small
epsilon>0 these points are still in C+, avoid the zeros, and

    h(z_j)=i/epsilon+O(1).

Hence on this fixed k-point packet

    K[z]=-(2/epsilon) G[b]+O(1),
    G[b]_ij=i/(b_i-conjugate(b_j)).

G[b] is strictly positive definite: it is the Gram matrix of the distinct
exponentials exp(i*b_j*t) on t>0. Thus K[z] is negative definite for small
epsilon. Congruence by the nonzero X(z_j) gives the same negative index for
the Hermite–Bezout kernel. This proves at least k negative squares. It works
for every finite selection if there are infinitely many upper zeros.

Accordingly the index counts **distinct upper locations**, not their
multiplicities. Multiplicity determines the sampling displacement but does
not create additional independent features. This proof completes the local
separation step missing from a bare finite-linear-independence explanation.

The companion/Hermite congruence, source transport equation, factor
A_Phi=4K_0, safe-axis restriction and Stieltjes two-channel identity retain
their stated normalizations. Their all-order positivity remains RH-strength.
The infinite Fourier, density, product and analytic-continuation arguments
are not certified by the finite algebra checker.

<a id="a-m13"></a>

## A-M13. A scalar-monotonicity correction and two valid positivity firewalls

In #784's Loewner addendum, scalar monotonicity does not pay a two-node
Loewner PSD condition. It pays the one-node derivative signs only.
For example p(t)=1/(1+t^2) is decreasing and t*p(t) is increasing on (0,1).
At t_1=1/2 and t_2=3/4 the determinant of -L_p is

    -256/15625 < 0.

The exact identity H=L_(tp)-D_x L_p D_x is valid, and a positive Stieltjes
measure does give both full Gram matrices. The invalid low-order sentence
must be corrected rather than used as an order-two theorem.

The nonisometric-compression counterexample is valid: C=diag(M,1), E=C^-1
and K the swap matrix give CE=I, ||K||=1, but ||CKE||=M. Pointwise multiplier
contractivity therefore does not prove contractivity in the compressed
metric. The metric inequality expands to the original source sign unless a
new compatible intertwining theorem is supplied.

Likewise the positive-sum PF-infinity counterexample is valid within the
standard Schoenberg characterization: individual transforms
Gamma(s+nu)*alpha^(-s-nu) have reciprocal Laguerre–Polya form; the sum for
two distinct alpha,beta acquires nonreal continuation zeros. This refutes a
universal positive-addition closure, not every possible theta positivity
proof. Any verdict about the named external preprint still requires a
source-version reading distinct from this self-contained counterexample.

<a id="a-m14"></a>

## A-M14. All-rank spectral positivity is not coefficientwise positivity

For the #785 spectral kernel B(u,tau)=cosh(tau*sqrt(u+1/4)), L_tau B=uB.
Evenness at zero and the superexponential theta tail justify repeated
half-line integration by parts at every fixed finite order. Andreief on the
ordered chamber therefore gives

    2^r int det[L^(h_p)Phi(tau_l)] det[B(u_q,tau_l)] d tau
      = prod_q Xfrak(u_q) det[u_q^(h_p)] > 0.

The factor 2^r and the transpose orientation are consistent. Strict total
positivity of B also follows directly from the positive cosh power series
and the strict generalized Vandermonde kernel in the increasing variables
u+1/4 and tau^2. This avoids needing to promote a numerical minor scout.

The Cauchy–Binet coefficient identity is exact, but its coefficients need
not be nonnegative merely because the full spectral expression is positive.
For X(u)=1+u+2u^2, H=(0,1), N=(1,2), the coefficient minor is -1 although
X(u1)X(u2)(u2-u1)>0. The coefficient-resolved TLSE gate remains open.

The theta-atom identity D_tau=M+1/2 gives
(D_tau^2-1/4)g=M(M+1)g. The continuum integral of the divergence-form
operator vanishes on the stated Gaussian ladder. Fourier self-duality is a
full-line statement (or an even-extension/cosine-transform statement), not
an unqualified half-line Fourier identity. These source identities do not
supply a signed lattice-defect estimate.

The huge finite PF order imported from a zero-height/sector theorem remains
an **imported finite-order** statement. Neither the size of that order nor
the all-rank spectral identity proves unbounded coefficient positivity.
Non-author review and the precise sector/source lock remain required.

<a id="a-m15"></a>

## A-M15. Divisor cusps and energy Schur reduction: what is genuinely closed

For #790 DC-1 the coefficient is Lambda(p^k)=log p, not k log p. With every
prime power and both orientations included, expansion of

    sum_(n*j<=N) Lambda(n)||v_(nj)-v_j/sqrt(n)||^2

gives exactly <v,(D_N-C_N)v>. The divisor identity supplies log j; the
outgoing square supplies M(N/j). Connectivity through prime edges gives
null vectors v_j=w/sqrt(j). The elementary binomial/factorial estimates
bound D_N by (log N+3)I. This is a signed interaction estimate, not PSD of C_N.

The narrow-window application retains only functions with **one vanishing
damped mean per window**. Integration by parts then places the full prime
cusp graph in the primitive block with the correct minus sign. The small
regular-cross error and local convex reserve yield the stated strict
primitive-norm bound. The means, their matrix, and their coupling to the
primitive sector are not paid. The support measure tends to zero; bounded
supported sequences are weakly null, not cofinal approximations to fixed
nonzero L2 tests. The heat-Hankel and Hardy/Weil operators are different
objects until an explicit adapter is proved.

For #792 the finite-window tail has two opposite rank-one terms. Killing the
cosh moment makes the remaining tail nonnegative. The two exponential
constraints validate the growing-kernel Fourier calculation through a
clamped primitive. The digamma partial fractions and a finite prime bound
then give coercivity outside the explicitly chosen finite-dimensional
space. This is compatible with compactness because the lower norm is the
primitive norm, not the original L2 norm.

The energy Schur argument does close a real domain issue. W is W^(1,1) on
each finite window, including its logarithmic derivative singularity and
prime cusps. Only one derivative is used in

    q(v,z)=b <phi'_v, Pi[-(W*z)' + c^2 int_0^t(W*z)]>.

Together with the proved primitive lower bound this gives continuity in the
positive energy norm. The Riesz representatives can therefore be taken in
the energy completion, without asserting they lie in L2. Completing the
square proves PSD equivalence and negative-index equality with the finite
**effective** matrix. It does not prove a nullity equality.

The Galerkin matrices decrease to that effective matrix **from above**.
Their positivity alone proves no lower sign. The residual Gram bound
U-3R<=S<=U, and U-(15/8)R<=S_1<=U for the stated improved L=1 subspace, has
the correct direction and retains all complex cross terms. Source and
rounding errors must be subtracted from the lower matrix before acceptance.
The reported sampled 4e-10 positive minima have no continuum enclosure and
are not sign certificates. A 104-dimensional reduction for L=1 is not a
reduction of all RH to 104 numbers.

<a id="a-m16"></a>

## A-M16. #793 remains a self-audit; line-one completion is not a critical-strip estimate

The exact initial horizon of the finite Euler source, the signed
rough-number recombination and the causal Dickman correction are compatible
with the source-preserving programme. The claimed norm theorem is at
Re(s)=1 and consumes classical quantitative PNT/Mertens estimates. It is not
a result uniform on Re(s)>1/2.

The correction multiplier is not a contraction. Below one its separate
norms can be exponentially large. The only potentially conclusion-facing
bound is for the **assembled product** P_X C_X on all compact subsets of
Re(s)>1/2, or the separately stated all-damping causal bounds. No such bound
has been established in the inspected packet. The prime-base cutoff retains
all prime powers and cannot be swapped for a hard prime-power cutoff without
the explicit error term.

Every positive scientific recommendation for #793 is marked self-audit
pending non-author review. Neither its exact finite controls nor this
reviewer's authorship constitutes independent acceptance.

<a id="a-m17"></a>

## A-M17. External prime-gap imports: scientific scope and input accounting

At the pinned PrimeGaps186 source the endpoint is conditional on three
explicit project axioms. Rank-three normalization divides the raw sum by p;
the quoted raw Deligne bound 3p becomes 3. For the rank-two correlation, two
normalized Kloosterman factors contribute p when converted to the raw
convention, so 8sqrt(p) becomes 8p sqrt(p). Preserve the excluded poles and
nonzero A,B assumptions; do not add or silently rely on A!=B.

The 152 physical inequalities are 104 outer, 45 inner and three cap bounds.
A Python/FLINT receipt is not a Lean proof of the axiom. The custom signed
convolution environment and the source's prohibition of optimized Python
are part of that certificate's trust boundary; this review's own -O controls
are not a rerun of it.

DHL[40,2] plus an authenticated admissible 40-tuple of diameter 186 gives
infinitely many consecutive gaps <=186: choose any consecutive pair between
two primes in each sufficiently large qualifying translate. This logical
consumer is valid. It does not discharge either exponential-sum input or the
physical-integral input.

The LongGaps source states a different, all-sufficiently-large-X extremal
lower bound. Its new scale divided by the earlier cited scale is
log_2 X/log_3 X, not a constant. The local mean-zero divisor normalization
and negative covariance at distinct residue roots are exact. The
ShortTranslates-to-cover-to-consecutive-prime chain must retain the location
bound q<=X, not just a long composite interval somewhere. The full imported
proof is not granted independent acceptance merely from a no-sorry report
or a standard-axiom Comparator configuration. C's outstanding build/type
reconciliation is pending, not a failed scientific review.

Neither extremal-gap theorem supplies the uniform all-test-function signed
prime discrepancy of an RH criterion. Any proposed such adapter is a new
open mathematical edge, not part of these imports.

<a id="a-m18"></a>

## A-M18. Independent reconstruction of the Lamzouri finite Hilbert mechanism

Pinned formal source: `AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7`.
This reconstruction concerns the mathematical mechanism, not a claim to have
rebuilt that Lean project.

Let eta be real and even with integral eta^2=1 and compact support. Put
f_z(t)=eta(t)exp(2pi i zt), and K(z)=integral eta(t)^2 exp(2pi i zt)dt.
K is even. For a finite conjugation-invariant support with positive integer
multiplicities define the finite-rank operator

    T=sum_z m_z |f_z><f_(bar z)|.

Conjugation invariance makes T self-adjoint. Direct finite expansion gives

    Tr(T)=M=sum_z m_z,
    ||T||_HS^2=Tr(T^2)=sum_(z,w) m_z m_w K(z-w)^2 = E.

In particular the assembled E is real and nonnegative, although its
individual summands need not be. These identities require the genuine
finite Hilbert inner products, not termwise positivity at complex points.

For one conjugate pair put g=(f_z+f_(bar z))/sqrt(2) and
h=(f_z-f_(bar z))/sqrt(2). Its operator is
m(|g><g|-|h><h|), with ||g||^2-||h||^2=2.
A real support vector has norm one.

Let s be the number of simple real support points, r the number of multiple
real support points, and c the number of conjugate pairs. Let U be the span
of multiple-real vectors and the g vectors, and V its enlargement by the
simple-real vectors. Write u=dim U, j=dim(V intersect U-perp), so u<=r+c and
j<=s. The compression of T to V-perp is nonpositive. Also

    Tr(P_U T) >= sum_(multiple real) m_z + 2 sum_(pairs) m_z
                = M-s >= 2(r+c) >= 2u.

Indeed U contains every indicated positive vector, and each negative h
projection can cost at most its full norm squared; the simple-real
contribution to this trace is nonnegative.

Choose an orthonormal basis adapted to U subset V and restrict to the finite
span of all source vectors. For its real diagonal entries alpha_l, Bessel
on the Hilbert–Schmidt operator and the inequalities

    alpha^2 >= 4alpha-4  on U,
    alpha^2 >= 2alpha-1  on V intersect U-perp,
    alpha^2 >= 2alpha    on V-perp (where alpha<=0)

give

    E >= 2M + 2Tr(P_U T)-4u-j >= 2M-s.

This proves s>=2M-E. Retaining Tr(P_U T)>=M-s and u<=r+c, j<=s instead gives

    E >= 4M-3s-4r-4c >= 3M-2(s+r+2c),

since M>=s+2r+2c. Therefore the distinct count D=s+r+2c obeys
D>=(3/2)M-E/2. This independently reconstructs both finite-multiset
inequalities, including arbitrary multiplicities, dependent source vectors
and the nonreal negative sector. It does not presume RH.

<a id="a-m19"></a>

## A-M19. The support-one constant and the pair-weight correction

The scalar minimization can also be checked independently. For a normalized
real density phi on [-1/2,1/2], the relevant quadratic functional is

    J(phi)=int phi(x)^2 dx + int int |x-y| phi(x)phi(y) dxdy.

The positive extremizer is

    phi_*(x)=cos(sqrt(2)*x)/[sqrt(2)*sin(1/sqrt(2))].

It integrates to one. Its Euler equation is
phi_*(x)+int|x-y|phi_*(y)dy=lambda, with

    lambda=1/2+cot(1/sqrt(2))/sqrt(2).

To prove minimality, not just stationarity, take a zero-mass variation v and
V(x)=int_(-1/2)^x v. Integrating twice with V zero at both endpoints gives

    J(v)=||v||_2^2-2||V||_2^2
         >=(1-2/pi^2)||v||_2^2 >0  for v!=0.

Thus the extremizer is unique and the infimum has the stated value. Smooth
compactly supported normalized approximations recover it in L2; the bounded
|x-y| kernel makes J continuous there. The two counting inequalities then
give the advertised constants 2-lambda and 3/2-lambda/2. Improving the same
scalar support-one quadratic problem cannot improve these constants.

For the zeta adapter, let d=rho-rho' and z=i*d*log(T)/(2pi). Under the
Fourier convention exp(-2pi i z alpha), replacing Q by

    Q - Q''/[4(log T)^2]

multiplies its transform by 1+pi^2*z^2/(log T)^2=1-d^2/4. This cancels the
rational pair weight 4/(4-d^2) exactly, before asymptotics. Compact smooth
support and the corresponding bounded derivative seminorms are needed when
the pair-correlation theorem is applied to this T-dependent test.

Formal boundary: `Solution/Basic.lean` explicitly quantifies
`hRvM : RiemannVonMangoldt` and `hPC : PairCorrelation` for its zeta endpoints.
Standard logical axioms do not eliminate explicit mathematical hypotheses.
The finite Hilbert theorem is a separate closed production theorem. The
ordinary analytic status of the imported RvM/BGST inputs and their exact
formal interface must be recorded separately. A positive density, even one
approaching one, does not by itself exclude finitely many off-line zeros.

<a id="a-m20"></a>

## A-M20. Catalan: what the compulsory-summand countercheck actually establishes

Source: #789 `HEIGHT_BOUND_COUNTERCHECK.md` at
`dba7d5aa2555ea1a921c28720dc045976fd7195d`, blob
`09f8eddec986da2ba26a8475c509ba11778145dc`.

For I_0={0,...,S-1}, the Pascal minor on any S distinct selected row nodes
2B+a equals their Vandermonde divided by product_(i=0)^(S-1) i!. It is a
nonzero integer, so its absolute value is at least one. The Cauchy minor is
nonzero, and the positive alternating tails have a two-term lower bound.
Consequently this term cannot be omitted from a largest-absolute-summand
majorant.

Grant the paper's stated common-minimum asymptotic with singular coefficient
A_rho=2rho-rho^2/2 and its claimed row-transfer error. The exact baseline
cancellation removes the a_Q contribution but not the clearing factors of
this compulsory term. They contribute 2rho B^2 log B+O(B^2), whereas its
Cauchy determinant contributes O(B^2) and its tail product at worst
-O(B log B). Therefore that **particular majorant** satisfies

    M_B >= (rho^2/2) B^2 log B - O(B^2).

At rho=1/20 the coefficient is 1/800. If the claimed common-minimum
asymptotic is unavailable uniformly, the original proof already lacks an
input; if it is granted, it defeats the asserted leading cancellation in
this max-summand argument. Additional cells controlling a finite B^2
coefficient cannot cancel this B^2 log B obstruction.

Disposition: the reasoning in the deposited countercheck is valid at these
explicit quoted premises. It invalidates this height-majorant proof method;
it does not prove Catalan rationality, logically falsify a theorem whose
premise could be false, or forbid a different signed-determinant repair.
Exact page/byte matching to arXiv v1, the other listed typo/support defects,
and any later erratum are separate source-verification tasks. Do not convert
an imported PDF receipt into a claim of a new independent full-page audit.
