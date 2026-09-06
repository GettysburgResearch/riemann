# Reviewer A: final mathematical reconstruction and extraction repairs

This document completes the independently assigned **disposition pass**, not a
proof of every statement stored in the repository. Source IDs resolve uniquely
in `SOURCES.tsv` to repository, exact commit, path and blob. `CLAIMS.tsv` is a
relational claim ledger: the source join is mandatory, and similarly named
claims on different branches are not aliases. Earlier arguments remain in
`MATHEMATICAL_AUDIT.md`; the final source/coverage decisions are in `REPORT.md`.
No source research branch is edited by these proposed extractions.

## F01. Reverse Rolle and the missing nonreal-critical block {#f01}

Sources: RR_FINITE (#716), BEZOUT_INERTIA and BEZOUT_WINDOW (#724).

The real count in L-104500 is reconstructed by monotonicity on each interval
between consecutive real critical points. With simple critical points and
regular endpoints, an interior extremum whose value has the wrong sign loses
two crossings, not one. On the complete real line for a real polynomial,

    N_nr(p) - N_nr(p') = 2 E(p).

Nonreal critical points are not absent from this identity.

For a degree-n real polynomial whose critical points are simple and noncommon
with p, partial fractions give

    p/p' = z/n + b + sum_c rho_c/(z-c),   rho_c=p(c)/p''(c).

Thus the deposited Bezoutian factorization is correct:

    B_p(x,y) = p'(x)p'(y)/n - sum_c rho_c q_c(x)q_c(y),
    q_c(x)=p'(x)/(x-c).

Its **inertia** cannot be read as a real diagonal congruence when c is
nonreal. Write a conjugate pair as rho=a+ib and q=u+iv, where u,v have real
coefficients. Its real coefficient block is

    [[-2a, 2b], [2b, 2a]],       determinant = -4(a^2+b^2) < 0.

It contributes exactly one negative square. Linear independence of the
features follows by evaluation at the distinct critical points; replacing
conjugate features by real and imaginary parts is an invertible real basis
change. The correct formula is therefore

    n_-(B_p) = #{real c : rho_c>0} + #{c in C+ : p'(c)=0}.

The source's equation L-105213.9 omits the second term. Its stated hypotheses
do not require all critical points to be real.

A rational counterexample is p=x^4+x^2+1. In the basis (1,x,x^2,x^3),

    B = [[-2,0,-4,0], [0,-2,0,2], [-4,0,-2,0], [0,2,0,4]].

Its eigenvalues are -6,2,1-sqrt(13),1+sqrt(13). The critical points are
0 and +/-i/sqrt(2), with residues 1/2,-3/16,-3/16. Hence the asserted count
is 1, while the negative index is 2. This is a counterexample to the
intermediate statement, **not** to the final total-root identity: combining
the corrected count with L-104500 still gives 2 n_-(B_p)=N_nr(p).

Extraction: preserve the factorization; either impose real critical points
or add their nonreal pairs. Recheck every downstream inertia use. A real
critical node remains a genuine negative diagonal pivot when its residue is
positive, and the fixed-window Cauchy remainder still vanishes on those rows.

## F02. An overstrong Gaussian tail, and the entry theorem that survives {#f02}

Sources: GLOBAL_GAUSSIAN and CAUCHY_LAYER (#773), RR_BOX (#716).

Let the positive-frequency density be comparable, with fixed positive
constants, to exp S_m(u), where

    S_m(u)=m log u + 9u/2 - pi exp(2u),
    2pi exp(2w)=m/w+9/2,
    a^-2=m/w^2+2m/w+9.

Then w~(1/2)log m and a^2~w/(2m). The displayed assertion
nu_m(|u-w|>Aa)<=C exp(-c A^2), **uniformly for all A>=1**, is false.
Take A_m=w/(2a) and the interval [w/2-1/m,w/2). On this interval,

    S_m(u)-S_m(w) = -m log 2 + O(m/w+w+log m).

A local lower integration bound and a Laplace upper bound for the
normalization imply

    log nu_m([w/2-1/m,w/2)) >= -m log 2 - O(m/w+w+log m).

But A_m^2~mw/2. Therefore the ratio of this logarithmic lower bound to
A_m^2 tends to zero, contradicting every fixed positive Gaussian exponent.
The weighted version in the source is also false because it includes the
unweighted case. This is an analytic countersequence for the literal source,
not a finite numerical trend.

The appropriate repair is local quadratic concentration and an exterior
linear-exponential bound. On |u-w|<=1, S''<=-c/a^2; outside that interval,
concavity gives a slope at least c/a^2 in the outward direction. The ratio
between the actual theta density and exp S_m is uniformly bounded above and
below. Integration gives, for a fixed H,

    Z_m asymp a exp S_m(w),
    E[exp(H|u-w|)|u-w|] <= C_H a.

For instance a global bound with exponent proportional to
min(A^2,A/a), rather than A^2, follows from the same argument. No all-scale
Gaussian assertion is needed.

Here is a direct repaired entry proof. Normalize the mth derivative by its
positive moment and write its cosine or sine phase explicitly. On
|Re z|<=c/a and |Im z|<=H, the preceding expectation gives an error at most
C_H c exp(w|Im z|), after harmless eventual adjustments for |z|. Choose c
sufficiently small. On circles of radius rho/w around model trigonometric
zeros, the model has a positive rho-dependent margin. On the complement,

    |cos(x+iy)|^2=cos^2 x+sinh^2 y

(and the analogous sine identity) gives the requisite weighted lower bound.
Rouche gives one zero per disk and none outside. Reality gives conjugation
symmetry, so the one zero is real and simple. This proves the stated small-c
growing window, of size sqrt(m/log m), with fixed H. It also proves the older
fixed-rectangle normalized conclusion. It does not descend to fixed derivative
order or pay an endpoint/winding sum.

For L-107200 the local arctangent argument is correct. An upward crossing of
r=f'/f contributes 1 to the positive Cauchy layer, a downward crossing 0, and
an even contact 1/2. At a zero of f, r'=-q/(x-z)^2+O(1), so no spurious
positive mass remains. The multiplicity correction sum(m_c-1) is mandatory.
A finite-screen estimate proportional to 1/epsilon cannot itself be sent to
epsilon=0.

## F03. Natural-window CLT and adjacent residue rigidity {#f03}

Sources: NATURAL_CLT and NATURAL_RESIDUE (#725). These claim IDs collide with
other branches; always retain the source ID.

With the **actual** saddle of m log u+log Phi(u), the standardized densities
of (u-w_m)/a_m converge in exponentially weighted L1 to the normal density,
uniformly in eta N<=m<=N for fixed eta>0. To justify that statement without
the false F02 global Gaussian, fix a standardized compact first, use Taylor
with a_m^3 S_m'''=O(sqrt(log N/N)), then use the local Gaussian up to physical
distance one and the exterior linear tail. For any fixed exponential weight
in the standardized coordinate, its growth is absorbed by the exterior slope
of order 1/a_m. The normalization is controlled by the same local lower
integral. These estimates are uniform throughout the constant-fraction band.

For |Re z|<=C/a_m and |Im z|<=H, t=a_m z stays in a fixed bounded set with
imaginary part tending to zero. Dominated convergence yields

    exp(-iw_m z+a_m^2 z^2/2) A_m(z) -> 1.

The Gaussian characteristic function is bounded away from zero on that fixed
set, legitimizing the relative statement. C and H are fixed before N tends
to infinity. No conclusion for C_N->infinity follows.

There is a display repair: the error in the reflected Xi model must be
measured after multiplication by exp(-w_m|Im z|). The prose of the source
says this, but equation (10) prints an unweighted supremum. The reflected
summands each carry the corresponding exponential; the raw error need not
tend uniformly to zero off the real axis.

At a real zero of the mth derivative, the phase is pi/2+jpi+o(1). The
adjacent saddle displacement is O(1/m), and its product with the natural
window tends to zero. Also (a_(m+1)^2-a_m^2)c^2=o(1). Adjacent orders
therefore have opposite cosine signs with the same Gaussian factor. Their
ratio is -M_(m-1)/M_(m+1)(1+o(1)), uniformly, and that moment ratio is
(1+o(1))/w_m^2. This proves the high-band residue statement after the
weighted error repair. It does not prove summability of an unspecified
low-order error, or global real-rootedness of one finite derivative.

## F04. Rank-two Cauchy proof: two distinct repairs {#f04}

Sources: CTI_THEOREM and CTI_CODE (#729). The exact original checker bytes were
reconstructed and authenticated against blob
`e708af8c5235b71e7382d43220236536fc3f20a8` before execution in an isolated
review directory. The imported source has no network/subprocess operations.

The original SymPy script uses the pairs returned by symmetrize(formal=True)
as substitution keys. These are (formal_symbol, elementary_polynomial), not
formal_symbol alone. The source execution raises TypeError at
`s1**2-2*s2 >= 0`. Correcting the keys does **not** complete the proof:
it then rejects its coefficientwise numerator claim.

The exact reduced denominator is

    (H^2+HP+R)^2 (H^2+2HP+4R)
    (H^2+2HP+P^2+U) (4H^2+4HP+P^2+U)^2,

where P=A+B, R=AB, U=D^2. It is positive. The 67-term numerator has exactly
three negative monomials:

    -40 H^8 R U,  -32 H^4 R^3 U,  -2 H^4 R U^3.

They are absorbed using the **necessary physical relation** P^2>=4R:

    152 P^2 U - 40 R U = 152(P^2-4R)U + 568 R U,
    932 P^2 R^2 U - 32 R^3 U = 932(P^2-4R)R^2 U + 3696 R^3 U,
    P^2 U^3 - 2 R U^3 = (P^2-4R)U^3 + 2R U^3.

The three indicated positive monomials occur with matching H powers, and
all other coefficients are nonnegative. Equivalently substitute
V=P^2-4R=(A-B)^2>=0 in each even power of P, retaining a factor P for odd
powers. The repaired numerator has nonnegative coefficients; the monomial
32 H^11 P makes it strictly positive. The exact rewrite identity is checked.

Thus rank-two CTI survives. The source's independent-coefficient assertion
in free P,R,U,H does not. The new checker and certificate retain both
failures, the invariant-cone repair and four exact rational trace controls.
This is exact symbolic-rational computation, not a Lean/kernel proof and
not an arbitrary-rank theorem. At coincident nodes the original Gram inverse
is undefined: take a normalized derivative-basis limit before asserting the
confluent statement. Its repaired denominator remains strictly positive at
U=0,R=P^2/4 with P,H>0.

Execution boundaries are recorded separately. A tool timeout during a grouped
optimized-mode rerun is not a PASS; the successful normal-mode repaired
calculation is not described as an independently built formal certificate.

## F05. Hyperbolic smoothing: integral strip versus analytic continuation {#f05}

Sources: HYPERBOLIC and HYP_SAMPLING (#759).

For h-hat(t)=exp(1-cosh t), contour shifts give exponential physical tails
at every rate sigma<pi/2. Therefore its bilateral Laplace integral equals
exp(1-cos s) on |Re s|<pi/2. The latter has an entire zero-free continuation.
The deposited equality must not be read as absolute integral convergence
for all s. If an absolute exponential moment existed beyond pi/2, the
Fourier transform on a horizontal line t+i sigma with pi/2<sigma would be
bounded by that L1 norm. Its continued value instead has modulus
exp(1-cosh(t)cos(sigma)), which is unbounded. Evenness removes a one-sided
escape from this contradiction. No endpoint assertion at sigma=pi/2 is used.

The actual RH application survives this domain repair. Its overlap strip
and detector strip lie inside the established integral strip. The negative-
time field has O(exp(u)) decay as u->-infinity, hence its transform is
holomorphic on Re s<1, not Re s>1. On a finite positive horizon [0,T], the
source beyond exp(7T) costs an exponentially small tail. Subpower prefix
energy then supplies a subexponential causal L2 bound, preserving every
hypothetical open-strip pole through the zero-free multiplier. The native
compact-source premise and its Mellin consumer remain explicit.

For sampling, the compact-prefix autocorrelation has support [-L_X,L_X]
and L1 norm O(X). Convolution with the hyperbolic autocorrelation prices all
nonzero period aliases by O(X exp(-2R)). Taking R=C_A log X pays X^-A.
The multiplier's double-exponential frequency decay then allows a cutoff
loglog X+O_A(1), yielding O_A(log X loglog X) coordinates. This is an
approximation theorem for a literal vector, not cancellation of its norm.

## F06. Residue ledgers, finite Cauchy remainder and selector costs {#f06}

Sources: RESIDUE_SECOND, ABSORPTION (#723), BEZOUT_WINDOW (#724).

For Q=p^2/(p'p''), the residues at simple p'-zeros are rho_c^2 and those at
simple p''-zeros are p(d)^2/(p'(d)p'''(d)). The coefficient of z^-1 at
infinity is reconstructed by expanding L=p'/p and Q=1/[L(L'+L^2)]. In
centered coordinates it is

    [(6n^2-18n+13)V2^2 - 3n(n-1)(n-2)V4]/[n^4(n-1)^3].

These are algebraic squares at complex points. Subtracting the nonreal
critical contribution and adjacent-derivative debt is essential to obtain
an absolute real second moment. Neither correction has a general sign.

On a bounded **rectifiable** regular contour, Cauchy's formula gives
F/F'=H+sum rho_c/(z-c), including removable zero-residue terms. Divided
differences give exactly the boundary-Loewner plus residue decomposition.
Every real critical row kills the boundary remainder. A general Jordan
curve should not be integrated with d zeta without a rectifiability or
appropriate approximation hypothesis; piecewise smooth rectangles suffice.

The selector/Cartan continuation encodes residues once the complete actual
pole manifest is provided. This does not bound selectors on the boundary,
price small denominator products, or prove positive signed first moments.
Origin multiplicity contributes q/z to a logarithmic derivative. The
historical theta kernel has a factor-two raw-amplitude correction, and
quadratic formulas inherit factor four; normalized tilted probabilities do
not change. These costs and the cofinal absorption estimate remain explicit.

## F07. Inner charge, topology and physical adjoints {#f07}

Sources: CALDERON, GRADE_ZERO (#720), TOPOLOGICAL, NONNORMAL, ANTIPHASE (#731),
and the already reviewed #765 physical-source correction.

The gamma integral gives an identity resolution of positive multipliers
strongly on L2(0,infinity). Tonelli then gives the finite-rank trace identity.
The one-zero distribution is 2ay H^(a-1)/(H+2y)^(a+1). Its cumulative mass
is (H/(H+2y))^a. The finite-inner tail bound additionally needs the causal
contraction theorem for a decreasing profile; it is not the false arbitrary-
band additive trace found in #777.

The projected Krylov family contains P_A X at grade zero. Orthogonal
projection therefore already minimizes ||X-Y||^2 over that family. Ridge
adds the nonnegative regularizer printed in L-104639; six further grades do
not create source-to-inner control.

For Q=P_-(I-P_+)P_-, the rank of P_-P_+P_- is at most deg B_+. Thus at
least (deg B_- - deg B_+)_+ eigenvalues of Q are exactly one. The factor
(1-tau)^d in det(I-tau Q) is rigid. Small regularization tends to the
canonical charge, not to a weaker source quantity.

For the compressed inner multiplier, unitary Schur triangularization gives

    canonical charge = sum |A(b_j)|^2 + ||strict upper triangle||_HS^2.

The value sum is a lower bound, not an upper bound. This abstract statement
is convention-independent; the printed Cauchy expression must be mapped to
the physical adjoint convention of #765 before use. Do not pass a formally
commuting matrix identity into the physical metric unchanged.

The odd-K antiphase inequality follows from
K*binom(K,2j+1)-binom(K,2j)>=0. Its scale 2/xi varies with Fourier frequency.
Replacing one constant physical companion scale by that multiplier is a
nonlocal change and does not preserve a zero-count theorem. The 1/(2K)
Xi asymptotic retains its source-concentration dependency. No endpoint-31
or fifth-order 90% conclusion is accepted without the remaining physical
charge estimate and the exact derivative-proportion input.

## F08. Analytic strict-gain mechanism versus numerical records {#f08}

Sources: STABILITY, THREE_POINT, SEVEN_LOCK (#726), AINTA_PROOF, MULT_FORMAL,
and the independent finite Hilbert reconstruction A-M18/A-M19 for #788.

Let P=VV*, with r columns of norm at most one, and Q Hermitian with at most
b positive eigenvalues. Write Q=Q_+-Q_-. The cross term tr(PQ_+) is
nonnegative and Q_+Q_-=0. Rearrangement for P and Q_- reduces the remaining
bound to

    min_(n>=0) [(p-n)^2+4n] = 2p-1+Psi(p),

where Psi=(p-1)^2 for 0<=p<=2 and 2p-3 for p>=2. Accounting for the zero
eigenvalues of VV* and V*V and tr(P)<=r gives

    ||P+Q||_HS^2 >= 4tr(P+Q)-3r-4b+tr Psi(V*V).

In the exact finite Hilbert zero model, tr H=M. Each positive direction of
the nonsimple/nonreal remainder consumes at least two multiplicity units,
so b<=(M-S)/2. Hence

    pair energy >= 2M-S+Delta,   Delta=tr Psi(V*V).

This establishes the finite retained-defect step independently of merely
quoting the numerical baseline theorem.

For the limiting optimized overlap kernel, a positive zero implies
x tan(pi x)=c>0. Three positive zeros at x,y,x+y would imply
x^2+xy+y^2+c^2=0. Removable apparent singularities are not zeros; the
one-way implication is sufficient. Thus the compact triangle
u,v>=0,u+v<=4 has a strictly positive minimum epsilon of
k(u)^2+k(v)^2+k(u+v)^2. The minimum is at most one by taking u=0 and v a
zero between 1 and 3/2, so 1-epsilon/2 stays positive.

For a graph of degree at most two on unit-bounded columns, form the Hermitian
matrix Y with the selected off-diagonal Gram entries and zero diagonal.
Its norm is at most two. The dual inequality

    tr Psi(M) >= tr[Y(M-I)] - tr(Y^2)/4

therefore yields Delta >=(3/2)sum_edges |M_ij|^2. Splitting each normalized
length-four cell into disjoint triples produces at least
(S-M/2)/3-o(M) triples by the zero-counting normalization. Consequently
Delta >=epsilon(S-M/2)/2-o(M).

To apply classical support-one pair correlation, first approximate the
optimizer by a **fixed admissible smooth** density. Its compact-distance
kernel and epsilon converge uniformly. Choose the approximation so its
baseline loss is smaller than the positive epsilon gain; only then let
height tend to infinity. This recovers a strict analytic improvement over
H0, conditional on the classical pair-correlation and counting inputs, without
an explicit new numerical value or a seven-gap computation. It is not a
claim of external novelty. Uniform overlap errors are required only on the
bounded-distance edges used here, of which there are O(M).

The explicit 269/280-block records have a different acceptance boundary.
The 707901-node external certificate, primitive arithmetic/rounding,
complete coverage and precise formal-to-analytic adapter were **not** replayed
here. The source locks and formulas are preserved, but neither advertised
record is independently numerically certified by this A pass. C/B questions
are narrow: exact version/rounding replay, dimension normalization, and the
coherent passage of the retained defect, not the already reconstructed finite
inequality. The Lean excerpt is not represented as a full dependency audit.

## F09. Clark sampling: a global premise is not a fixed-box conclusion {#f09}

Source: CLARK_GATE (#728), compared to RR_BOX, NATURAL_CLT and GLOBAL_GAUSSIAN.

The stated WSEG extinction implication is valid when its moment vectors,
positive first moment, complete weighted second moment and real-rooted
Clark/de Branges setting are supplied. The 9/25 local weight lower bound
then makes a subthreshold nonnegative defect exclude an integer event.

But the Clark construction invokes an already simple and real-rooted
derivative in the global required class. A theorem saying that for every
fixed rectangle there exists a sufficiently high derivative order does not
provide one globally real-rooted derivative. The quantifiers cannot be
interchanged. The proposed global-Clark composition therefore remains
conditional. A valid fixed-window exterior-factor construction or a genuinely
global endpoint would be an additional theorem, not a notation change.

## F10. Cauchy determinant and rank extension {#f10}

Sources: CTI_DETERMINANT and CTI_EXTENSION (#780).

Cauchy's determinant formula gives the displayed exact ratio. Each diagonal
factor exceeds one by xH/(x+2H)^2. For z=x+iy, the paired modulus numerator
minus denominator is

    H(8H^2x+9Hx^2+9Hy^2+2x^3+2xy^2)>0.

This proves the determinant gain for every finite distinct packet. Normalized
confluence is required at repeated nodes. AM-GM gives precisely the stated
spectral-dispersion sufficient region, not unrestricted trace order.

Writing P_r=P_(r-1)+u_r u_r* and Q_r=Q_(r-1)+v_r v_r* gives the trace
increment ||Q_(r-1)u_r||^2+||P_r v_r||^2. Subtracting the current increment
<Tu_r,u_r> yields the exact extension ledger. Testing projection against
T^2u_r bounds ||Q_r u_r||^2 below by m2^2/m4. Therefore the declared
old-space return condition is sufficient. It is not proved for arbitrary
exponential packets. Even a future all-rank trace theorem needs its exact
source, localization and cofinal adapters before any RH consequence.

## F11. Compact beta kernels, maximal exponents and coarea {#f11}

Sources: KERNEL_INFO (#758), ABSCISSA and ABSCISSA_ENERGY (#762), Q_COAREA and
Q_EXPONENT (#779), together with the reviewed #757/#760 source.

For a nonzero compact L2 kernel, some polynomial moment is nonzero by
polynomial density. Let r be its first such order and b its signed moment
normalization. Convolution with the finite beta source preserves the lower
vanished moments and multiplies the rth moment by the prefix B(X). Projection
onto the monic shifted Legendre polynomial on the full support hull gives

    ||K*mu_X||_2^2 >= |b|^2 (r!)^2(2r+1)binom(2r,r)^2 |B(X)|^2 / L^(2r+1).

BV Abel summation, with zero extension and endpoint contributions, gives the
upper bound L (||K||_infinity+TV(K))^2 B*(X)^2. These prove the fixed-kernel
equivalence under the exact beta-prefix criterion. For moving kernels the
stated geometric factor is a **sufficient** forward condition; failure of
that factor is not a counterexample for the actual family.

Two-way Abel summation shifts a maximal Mertens power exponent by 1/2.
Demodulation costs at most 1+|t|log X. Thus the exponent statements retain
their named classical Mertens zero-abscissa theorem and rough-conditioning
range; no endpoint-only substitution or unrestricted moving frequency is
licensed. The VK saving stays X^(1-o(1)), not a fixed power improvement.

For stationary coarea, two logarithmic points share a unit grid cell for a
set of shifts of measure (1-|x-y|)_+. Expanding the finite square proves
the tent identity for arbitrary complex coefficients. A band sum is a
difference of prefixes and a prefix is the sum of its bands; the maximal
comparison loses only O(log X). The q-free/duplicate-beta transport uses
(1-aS)^2 and the absolutely summable inverse sum_(j>=0)(j+1)a^j S^j,
a=q^-1/2. Every sign and truncation remains present. The arithmetic bound
on the assembled energy is still open.

## F12. Boolean half-squares and the principal-mode boundary {#f12}

Sources: WICK_HALF, REFLECTION (#751), PRINCIPAL_FIREWALL (#778); #756 is
tracked for the A/B source interface, not silently accepted as an entire atlas.

On finite labelled supports, T_theta is an algebra homomorphism for
**disjoint-support** convolution. A fixed unordered owner pair occurs in two
orders. Integrating 2 theta^(k-2)(1-theta) gives 1/binom(k,2), proving the
half-square identity conditional on the stated b=f star f. It is not an
ordinary convolution square and certainly not an autocorrelation norm.

There is a small source-typing repair. The assertion that labelled atoms map
injectively to p*a^2 is true on a chart with genuinely distinct physical prime
labels and the declared coprimality. Two labelled copies of 67 can yield the
same physical atom, or the exceptional exponent 3 or 4. On the two-copy
marked model the physical fibre has size at most two. Aggregate its signed
coefficients first, or use |sum c_i|^2<=2 sum |c_i|^2. This fixed factor does
not change subpower diagonal scope; it must not be silently omitted as exact
injectivity. The separate repeated-owner ledger remains necessary.

For a **fixed horizon** real L2 half-field, R_x f(u)=f(x-u) is a self-adjoint
unitary involution. Its even/odd projections give E+O=N, J=E-O. A differential
operator with a factor D annihilates N, hence D_out J=-2D_out O. This exact
identity gives no estimate of its positive part. If the horizon moves with
x, differentiating the cutoff creates additional terms; freeze before using
the displayed identity.

The later #719 source reset matters to this descendant. Exact Boolean
identities are retained, but a historical claim that all ordinary-contraction
errors are subpower does not automatically bind them to the current native
wavelet after a semiprime-main failure. SFSC/BCI/HMO arrows must be reopened at
that source interface, not declared universally false and not reused as a
reviewed RH path. The required conjunction includes a new source-exact
comparison with its actual weighted error norm.

The #778 countermodel is elementary and valid in its stated model class:
constant functions on finite groups have zero nonprincipal Fourier data and
zero uniform-comparator fluctuation while retaining arbitrary principal
energy. It refutes a **source-blind** inference. It neither produces a large
value for fixed arithmetic coefficients nor rules out every arithmetic-
geometric realization. #756's exact finite-field channels and selected-mode
estimates require B's assigned review; its family-to-principal arrow remains
open under A's source audit.

## F13. Resolvent/Weil/Pick equivalences and multiplicity {#f13}

Sources: PHASE_RESOLVENT, PHASE_GAUSS (#768), GENERAL_INDEX (#783), and the
full-source #792 arguments in A-M13--A-M15.

The symmetric resolvent weights are (a^2-lambda_rho^2)^-m, a>1/2, m>=2.
The two-point Hermite remainder cancels the safe interpolation poles and
retains a nonzero coefficient at every actual zeta zero. On RH the time
function is the Fourier transform of a finite positive measure. Conversely
boundedness/positive definiteness or a **holomorphic** right-half-plane
Hardy statement excludes the nonremovable pole of a hypothetical off-line
zero. Each implication retains full source identification and convergence;
finite meromorphic boundary norms cannot replace the Hardy condition.

For the phase Gauss law, G=(s-1)^2 zeta' removes the pole. Along Re s=1/2,
Re(2/(s-1))=-1/(t^2+1/4), giving exactly the Q term when returning to
zeta''/zeta'. The rectangle orientation fixes the side and horizontal terms.
In a finite model, integral(L-R)_+=pi N_left-integral min(L,R). Screening is
not negligible without a theorem. No petal-by-petal Speiser assignment follows.

For the generalized-Schur kernel, congruence with the Nevanlinna kernel of
-f'/f preserves inertia. Each distinct nonreal conjugate pole pair gives a
2x2 off-diagonal block with one negative direction; multiplicity changes its
coefficient, not its rank. The locally uniform genus-one expansion gives the
upper bound. For any finite selected pole set, contour residue functionals
paired with interpolating evaluations give a matrix -2t diag(m_j)+O(1);
large t makes it negative, and finite Riemann-sum approximation preserves the
strict gap. Thus arbitrary finite subsets are captured and the global index
is the number of **distinct** upper-half-plane zero locations. The family
(z^2+1)^m has index one, not m. A fixed spatial rectangle still needs exterior
control before a local index equality is claimed.

## F14. Later changes to old research heads: #568 and #599 {#f14}

The published C census was used as navigation, then both exact commit
comparisons were read independently. #568 changes from
085d046905bfd32a5725632650039e58bb7fc1f7 to
3a70470e3a8bbd60e0b7387ea46fd391cfb1d2e2; the two changed files are its
parity-grouping checker and retained JSON. This is a computational/provenance
delta requiring C's disposition, not a new accepted theorem from A.

#599 changes from 223f11259b3e7134f78d6492795e6e94caca8be3 to
8daa0a5d94de56c68a1ce710824b26cacc1a9bbc in four commits. Besides publication
files it adds SMALL_CUBE, TERMINAL_STRIP and PRODUCT_BOUNDARY, read here.
The date printed inside a file does not determine whether its exact source
was in the August 22 release.

Given the reviewed base b(Y)=a_*sqrt(Y)+O(1) globally, substitute its bounded
remainder into the **complete** finite Euler cube, including inactive child
endpoints. This yields exactly a_*prod(1-1/p) plus an error at most
C X^-1/2 prod(1+p^-1/2). At Z=(kappa log X loglog X)^2 the latter is
X^(kappa-1/2+o(1)). For kappa<1/2 it is smaller than the positive main;
removing initial primes only improves both sides. The boundary kappa=1/2 is
loss of this proof's margin, not a proved failure of the actual cube.

The terminal largest-prime strip has absolute cost O(H^2/log X), using
|U_<p(Y)|=O(log(2Y)) and a prime harmonic upper bound on the strip.
Comparison with the small-cube main needs H^2 log Z=o(log X). The product
expansion then bounds v<=X^beta by
X^(kappa+(beta-1)/2+o(1))*log X/log Z; beta<1-2kappa pays it. Every v>X^beta
remains, including v>X with inactive child endpoints. No positive-main
asymptotic for the full native scalar follows. Its signed boundary is the
first open arithmetic theorem.

The manuscript's reference to “PR #590 at 223f1125...” needs provenance
repair: the audited old PR row here is #599. The exact SHA, rather than the
printed PR number, is the binding source. Workflow/PDF publication additions
are not a scientific argument and were not executed by this review.

## F15. Literal chiral beta source before norms {#f15}

Source: CHIRAL_SOURCE (#775), with #758 geometric source retained separately.

For Re z>1 the two beta Dirichlet series converge absolutely and P_z is L1.
Fourier product-convolution and Fubini are therefore licensed. Acting on
exp(it log(m/k)) supplies exp(-z|log(m/k)|/2), converting (mk)^(-(1+z)/2)
exactly to 1/[sqrt(mk)max(m,k)^z]. This proves the displayed signed source
identity. For complex z it is not a modulus square.

At the exceptional prime the beta local coefficients are 1,-2,1, hence their
squares are 1,4,1. The diagonal Euler factor is therefore
(1+4x+x^2)/(1+x) times zeta(1+z)/zeta(2+2z). Parseval supplies the kernel
norm multiplier; for the unit-height step it is one, independently of order.
A growing cusp cannot amplify that diagonal. The directed Fourier branch
samples the carrier at the **negative** source lag, so the corrected m>k
orientation is necessary. None of these facts bounds the complete signed
outer-frequency contribution or licenses crossing the absolute-convergence
boundary without an analytic theorem.

## F16. Acceptance and cross-review boundary {#f16}

The independent A report is now complete as a source-qualified disposition
and repair handoff for the assigned programmes. Unchecked objects are listed
in OMISSIONS.md, not left as implicit acceptance. B's automorphic/sheaf/
representation-theoretic work, non-author review of A-authored #793/E
material, and C's primitive replay/formal/PDF/version audit remain **pending
integrator reconciliation**. No unpublished report is a dependency of any
finite argument reconstructed here.

The external LongGaps full Lean/paper proof is not independently accepted
from metadata; its local source algebra and statement normalization were
checked. PrimeGaps186 retains its three explicit input assumptions. Lamzouri's
finite and scalar mechanisms were reconstructed, while the exact imported
analytic statements and formal theorem hypotheses stay visible. Catalan's
height objection remains an audit of the quoted fixed-version argument,
not a claim of rationality or an authenticated audit of a later version.
These are final first-pass exclusion/hold decisions, not theorem refutations.
