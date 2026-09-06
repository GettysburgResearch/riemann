# C4-M: the missing Mellin analytic propositions and their exact scope

Status: complete proposed paper proofs and source-level interface review; **not Lean-compiled**.
Source baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Primary inspected files: SRC-M0 through SRC-M5 in `../SOURCES.tsv`.
These are classical analytic results reconstructed for the literal repository conventions,
not new arithmetic estimates, new historical claim IDs, or a claimed RH proof.

<a id="M1"></a>
## M1. The convention, and a defect in the singularity name

The deposited transform is exactly

\[
 \mathcal Mf(s)=\int_{[1,\infty)} f(x)x^{-s-1}\,dx.
\]

The exponent has a minus sign,
the lower endpoint is 1, and complex powers of positive real x use the real logarithm.
The endpoint itself has Lebesgue measure zero. It must not be changed in a
pointwise arithmetic summation statement merely because it is harmless here.

`Analysis/Foundations.lean` defines `NonremovableAt F s0` as
`not AnalyticAt C F s0`. This is not the usual punctured-germ definition of a
nonremovable singularity. For example, let f(0)=1 and f(z)=0 for z nonzero.
Then f is not analytic at 0, but the zero function is an analytic extension of
its punctured germ. The point-supported defect -f repairs the value, although
it is not analytic as a total function at 0.

The three deposited transfer lemmas in `SingularityTransfer.lean` remain valid
for their actual predicate and their **full-neighborhood/total-function** equalities.
They are not refuted by this example. What must not happen is silently weakening
an equality to punctured equality while retaining that predicate.

A suitable new analytic predicate is:

\[
 \operatorname{PuncturedNonremovable}(f,z_0)
 \iff \text{there is no analytic germ }g\text{ at }z_0
 \text{ agreeing with }f\text{ on a punctured neighborhood.}
\]

**Theorem M1.** If a is analytic at z0, a(z0) is nonzero, and b is analytic
there, then af+b has a punctured analytic extension if and only if f does.

**Proof.** In a sufficiently small disk a never vanishes. An extension g of af+b
produces (g-b)/a, analytic on that disk and equal to f punctured there. Conversely
an extension h of f gives ah+b. No value assigned to f(z0) enters this argument.
This also proves the transfer under a specified punctured equality F=af+b. QED.

If a meromorphic germ has order -m with integer m>0, write it as
(z-z0)^(-m)u(z), where u is analytic and u(z0) is nonzero. It has no analytic
extension: multiplying such an extension by (z-z0)^m and taking the limit
would give u(z0)=0. Thus the pole applications have the stronger punctured
property, although the deposited conclusion only records the weaker one.

<a id="M2"></a>
## M2. Holomorphy to the right of an absolute-convergence abscissa

**Theorem M2.** Suppose f is measurable on [1,infinity), locally integrable,
and its tail integral converges absolutely at every real sigma>c. Then
\(\mathcal Mf\) is holomorphic in Re(s)>c. For every nonnegative integer j,

\[
 (\mathcal Mf)^{(j)}(s)=
 \int_1^\infty(-\log x)^j f(x)x^{-s-1}\,dx,
\]

locally uniformly there.

**Proof.** Fix a compact K in that half-plane, and choose c<b<a=min Re(K).
For x>=1, the absolute jth derivative of the integrand is at most

\[
 |f(x)|x^{-b-1}(\log x)^j x^{-(a-b)}.
\]

The last two factors have a finite supremum: setting y=log x reduces this
to y^j exp(-(a-b)y). The first factor is integrable by hypothesis. Each finite
interval integral is entire; the displayed domination gives locally uniform
convergence and legitimates differentiation of every order. One can instead
apply Morera and Fubini to the same dominating function. QED.

This proof does not assume pointwise polynomial bounds on f. Absolute
integrability at a slightly smaller exponent is enough. For a nonnegative
density the convergence set in the real exponent is an upper interval. Its
infimum is either a real number or minus infinity when an initial convergent
exponent exists. The latter case is an entire transform, not a missing finite
abscissa that may be fabricated.

<a id="M3"></a>
## M3. Exact eventual-sign Landau theorem

The formal proposition `MellinLandauBoundarySingularity` quantifies a locally
integrable real f, an arbitrary total function F, real c and sigma_initial,
eventual nonnegativity, nonzero-a.e. data, a finite tail abscissa c, and agreement
of F with the transform on **every** point Re(s)>c. We prove precisely that
proposition, and in fact a stronger right-germ noncontinuation statement.

**Theorem M3.** Let f satisfy those assumptions. There is no function analytic
in a neighborhood of the real point c agreeing with \(\mathcal Mf\) on the
part of that neighborhood to the right of c. Consequently the formal total
function F is not analytic at c.

**Proof.** Choose X0>=1 beyond which f>=0. The finite head

\[
 B(s)=\int_1^{X_0} f(x)x^{-s-1}\,dx
\]

is entire, by compact domination (log x is bounded and f is integrable on
that compact interval). Removing B changes neither absolute convergence nor
the finite abscissa. With y=log x, the remaining integral is a Laplace transform

\[
 G(s)=\int_0^\infty h(y)e^{-sy}\,dy,
 \qquad h(y)=1_{y\ge\log X_0}f(e^y)\ge0.
\]

The change of variables is valid on finite intervals and then by absolute
convergence or monotone convergence; it also shows that a finite head cannot
alter the divergence on the left of c. Local integrability transfers because
dy=dx/x and x is bounded away from zero on compact source intervals.

Suppose G had an analytic extension to D(c,r), r>0. Glue it to the original
holomorphic transform on Re(s)>c using agreement on their connected overlap.
Let a=c+r/4. The disk D(a,r/2) lies in D(c,r) union {Re(s)>c}: a point not in
the half-plane is within 3r/4 of c. The glued function therefore has its Taylor
expansion at a throughout D(a,r/2).

By M2 and positivity,

\[
 (-1)^nG^{(n)}(a)=\int_0^\infty y^n h(y)e^{-ay}\,dy\ge0.
\]

Take u=3r/8, which satisfies a-c<u<r/2. The convergent Taylor series evaluated
at a-u has nonnegative terms. Tonelli's theorem gives

\[
 \begin{aligned}
 \sum_{n=0}^\infty\frac{u^n}{n!}(-1)^nG^{(n)}(a)
 &=\int_0^\infty h(y)e^{-ay}
       \sum_{n=0}^\infty\frac{(uy)^n}{n!}\,dy\\
 &=\int_0^\infty h(y)e^{-(a-u)y}\,dy<\infty.
 \end{aligned}
\]

But a-u=c-r/8<c, contradicting the declared left-of-abscissa divergence.
The assumed extension cannot exist. Adding back B does not change the result.
If the formal F were analytic at c, its stipulated equality on Re(s)>c would
supply exactly the forbidden extension. QED.

The `sigma_initial` convergence field is redundant once convergence for every
Re(s)>c is given, but is harmless. The nonzero-a.e. field is also consistent;
finite real abscissa already rules out an eventually zero density. Neither
redundancy licenses dropping the local-integrability or finite-abscissa premise.
No nonnegative assertion is made about the original compact signed head.

### Consequence used by the consumer

If a continuation agreeing to the right of c is analytic at every positive
real point, M3 forces c<=0. M2 then gives the defining transform throughout
Re(s)>0. This is exactly the mathematical content of the deposited
`landau_abscissa_nonpositive` and `nonnegative_tail_continuation_analytic` once
the new library proof of M3 is supplied. It is not an arithmetic sign theorem.

<a id="M4"></a>
## M4. Subpower logarithmic negative mass gives all required holomorphy

Let n=f_- be nonnegative and locally integrable on [1,infinity), and define

\[
 A(X)=\int_1^X n(x)\frac{dx}{x}.
\]

The formal hypothesis says: for every epsilon>0 there exist C>=0 and X0>=1
such that A(X)<=C X^epsilon for all X>=X0. There is no uniformity of C or X0
in epsilon. Our argument does not require any.

**Theorem M4.** Under these hypotheses, \(\mathcal Mn\) converges absolutely
and is holomorphic at every s with Re(s)>0, with locally uniform derivatives
of all orders. This proves the mathematical proposition
`SubpowerNegativeMassHolomorphy` as deposited. Its separate initial-convergence
assumption is not needed by the proof.

**Proof.** Fix a compact K with a=min Re(K)>0. Choose epsilon=a/2. Increasing C
to account for [1,X0] yields A(X)<=C' X^epsilon for every X>=1: local
integrability makes the compact contribution finite. On [2^k,2^(k+1)],

\[
 \int |(-\log x)^j n(x)x^{-s-1}|dx
 \le C'2^\epsilon ((k+1)\log2)^j
                 2^{-(a-\epsilon)k},\qquad s\in K.
\]

The right side is summable in k for each fixed j. This proves uniform
absolute convergence on K for the transform and every formal derivative.
Finite interval integrals are entire. The Weierstrass theorem or dominated
complex differentiation proves the assertion. QED.

For an explicit tail estimate, let Re(s)=sigma>epsilon and R>=1. Integration
by parts for the locally absolutely continuous A gives

\[
 \int_R^\infty x^{-s}\,dA(x)
 =-R^{-s}A(R)+s\int_R^\infty A(x)x^{-s-1}\,dx.
\]

The boundary at infinity vanishes and hence

\[
 \left|\int_R^\infty n(x)x^{-s-1}\,dx\right|
 \le C'\left(1+\frac{|s|}{\sigma-\epsilon}\right)R^{\epsilon-\sigma}.
\]

This estimate is uniform on each fixed compact half-plane subregion. It is not
a uniform bound as sigma goes to zero, and it does not bound any actual
Möbius negative mass without the displayed subpower hypothesis.

<a id="M5"></a>
## M5. The initial-agreement extension is a theorem, not an additional oracle

**Theorem M5.** Suppose F is holomorphic on Re(s)>c; f has the absolute
convergence in M2; and F(s)=M f(s) on some nonempty right half-plane contained
in Re(s)>c. Then equality holds on all of Re(s)>c.

**Proof.** Both functions are holomorphic on that connected half-plane by M2.
Their difference vanishes on a nonempty open subset. The identity theorem
makes the difference identically zero. QED.

For the exact source consumer, `NonnegativeTailMellinCore` includes analyticity
of the positive continuation on Re(s)>c and absolute convergence there.
Therefore `hContinuationExtension` follows from these fields and initial
agreement. This is a complete paper-level discharge of that adapter, not a
claim that the core package itself has been constructed for the native source.
The finite-abscissa and positive-real analyticity fields must not disappear
from the public dependency graph.

<a id="M6"></a>
## M6. Affine shifted pole order, with arbitrary multiplicity

**Theorem M6.** If zeta is analytic near rho and has a zero of finite order
m>=1 there, the reciprocal of zeta(s+1/2) has meromorphic order -m at
s0=rho-1/2. More generally affine precomposition zeta(a s+b), a nonzero,
preserves the zero/pole order; a zero derivative map would not.

**Proof.** The local factorization is zeta(z)=(z-rho)^m u(z), where u is
analytic and u(rho) is nonzero. Substituting z=s+1/2 gives
(s-s0)^m u(s+1/2). Its reciprocal on the punctured disk is
(s-s0)^(-m)/u(s+1/2). For a general a the extra factor is a^m, a nonzero
analytic unit. The order is therefore exactly -m. Total values assigned at
the zero are irrelevant to the meromorphic order. QED.

This is the specific mathematical adapter missing from
`ShiftedReciprocalPoleOrder`. Identifying its integer m with
`ProjectZeroMultiplicity` still uses the exact inspected Zeta23/Mathlib
multiplicity bridge. A paper proof is not a compiled proof term for that bridge.

<a id="M7"></a>
## M7. A complete classical fixed-source criterion, including the entire case

This statement identifies which burden remains after M1--M6. It is not a
claim that the native detector satisfies the burden.

**Theorem M7.** Let f be a fixed, real, locally integrable density on
[1,infinity) with one initial half-plane of absolute Mellin convergence.
Suppose its transform there is a fixed meromorphic function F on Re(s)>0
(intersected with that initial half-plane), and:

1. F has an analytic germ at every positive real point;
2. f has subpower logarithmic negative mass as in M4;
3. every hypothetical nontrivial zeta zero rho with Re(rho)>1/2 forces a
   genuine pole of F at rho-1/2, by a fixed zero-free numerator/multiplier and
   a fixed holomorphic defect.

Then there are no such right-side zeros. With the classical zero localization
and reflection adapters, RH follows.

**Proof.** By M4, N=M(f_-) is holomorphic in Re(s)>0. The positive density
p=f_+ has initial convergence, since |f_+|<=|f|. Initially its transform is
P=F+N by the absolutely convergent Jordan identity. Let c be its abscissa.
The initial convergence rules out +infinity. If c=-infinity, P is entire and
there is nothing to prove about its abscissa. If c is finite and positive,
P is holomorphic on Re(s)>c. Meromorphic uniqueness extends initial agreement
with F+N to that connected half-plane; in particular all its supposed poles
there are removable. F+N is analytic near the positive real point c by (1)
and M4, supplying the continuation prohibited by M3. Thus c<=0 or c=-infinity.
In either case P is holomorphic on Re(s)>0. Meromorphic uniqueness there now
gives F=P-N, with no poles. This contradicts (3) for any right-side zero.
For a zero left of the critical line, the full classical reflection adapter
would give a right-side one. QED.

The all-zero density and compact-support cases belong to c=-infinity. They
must not be excluded by insisting that every source admit a real finite c.
The existing conditional formal theorem remains valid at its narrower scope;
M7 is a proposed more general consumer, to be assigned its own identity.

The arithmetic work is still (2), plus the literal source identity and fixed
factorization in (3). M1--M7 contain no bound for the actual signed Möbius source.

<a id="M8"></a>
## M8. Removable values of reciprocal zeta are a second normalization gate

The fixed consumer defines `shiftedReciprocalZeta s` by the inverse of the
total Mathlib value `riemannZeta(s+1/2)`. At an ordinary zero this is a harmless
point assignment for pole-order arguments. At zeta's pole, s=1/2, the intended
reciprocal is analytic with value zero. Analytic-at-positive-real conclusions
require either proof that the assigned total inverse has that value and germ,
or use of the correctly extended reciprocal. This report does **not** assert
an unevaluated formula for Mathlib's assigned zeta(1), nor a second universal
emptiness result for the consumer.

Using the entire xi from X1, a correct meromorphic reciprocal in Re(z)>0 is

\[
 R(z)=\frac{z(z-1)\pi^{-z/2}\Gamma(z/2)}{2\xi_{\rm ent}(z)}.
\]

It agrees with 1/zeta away from z=1 and the zeros, and R(1)=0 since
xi_ent(1)=1/2 and the gamma factor is regular. Substitution z=s+1/2 supplies
the correctly normalized fixed Mellin coordinate. This is a normalization
recipe; it does not remove any nontrivial zero or prove RH.

## Scope and integration decision

M2--M6 provide complete analytic derivations for the named mathematical
interfaces, using standard measure/complex-analysis tools. The formal source
is unchanged and still requires proof arguments. M1 and M8 are statement
repairs that need new IDs and downstream type review. M7 is a fully explicit
conditional consumer with an **open arithmetic premise**, not an accepted
unconditional result. Compile and review the new proof terms before changing
a formal registry status or deleting any listed formal input.
