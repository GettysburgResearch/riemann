# What every numerator moment can and cannot buy in the retained detector

Status: PROPOSED source-qualified component mathematics, awaiting independent review.
This file proves an arbitrary fixed-order numerator estimate, its shifted-detector
adapter, and an exact obstruction for a specified positive exponent-budget
architecture. The obstruction is NOT a lower bound on actual L-values, exceptional
sets, the physical theta integral, or any zeta zero. No new global zero-free
fraction or RH theorem is asserted.

The useful conclusion is specific. Even after allowing every fixed numerator and
mollifier moment order, every real detector shift, finite complex interpolation,
and asymmetric short-support physical scales, the retained Type-II/independent-
numerator budget cannot produce a boundary below 100/111. A concrete original
Möbius-convolution polynomial whose treatment must change is isolated in Section 6.
The number 100/111 is a necessary floor of this architecture, not an achievable
global boundary or its optimized endpoint.

## 1. Native family and imports

Fix the field F containing mu_6, the permissible finite set S, deep ray data and
generator choices in de Faveri's sixth-order family. Rows a are SIXTH-POWER-FREE
exterior integral ideals, ordered by their FULL ideal norm. A fixed finite list
of finite-order S-supported twists psi is allowed; constants depend on this list
and all fixed source data. The original character values at nonunits remain zero.
Infinite-order angular twists and growing field/discriminant uniformity are not
asserted. The physical application uses the separately pinned CT identification
of these rows; the arithmetic moment argument itself does not use CT.

The large-sieve input is de Faveri, Theorem 1.1, arXiv:2610.04045v1:

    sum_(Na<=U)^flat |sum_(Nc<=V)^flat b_c chi_a(c)|^2
      <<_eta (UV)^eta K(U,V) sum_c |b_c|^2,
    K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).           (1.1)

Both indices are sixth-free. The primary HTML was freshly read in this pass,
including the definitions preceding Theorem 1.1 and the final detector in Section
9. Theorem 1.1 is imported, not reproved. A fixed psi multiplies common column
coefficients. Restriction to any subset of rows is legitimate after taking the
nonnegative square, including conductor dyads and the row masks below.

We also import the complete Hecke functional equation and approximate functional
equation, with their actual conductor, both pieces, gamma factors, fixed omitted
Euler factors and rapid tails. BGL, arXiv:1112.1650, Section 5, is the inherited
family/AFE source. The inducing conductor Q is O(Na), not necessarily comparable
to Na. Outside S its support is the radical of the sixth-free row. Inducing-
principal rows form a fixed finite exceptional list; they are treated separately
away from s=1 and omitted in zero counts.

Prior repository components are credited as follows: #968 at
14f544fb4293ffb59942ff8d345ab9d6da67025c proves the central fixed-order envelope;
#966 at 8d94494698ee447711a53dec922986586418e398 proves the central fourth mean;
#969 at 6542781188469e8a23dadf9d419b3d5cf4d11de7 proves the complementary
7/12,5/12 fourth means; #971 at 3f1d2a07631eb6cca1f2716be01f64e874667639
reconstructs the shifted rowwise detector and its maxima; #976 at
92a0f2c9c4855f03558a93ede0ddbf2892b946d4 recovers the 3/4,1/4 eighth-mean
packet. The latter's archive SHA-256 and original thirteen-file Git tree were
authenticated before reading it; no historical checker replay is claimed here.
#974 at 89c37b6707cb77fc5a86143ea98d8756759fdcbc contains our earlier finite-vector
interpolation and enlarged local domain. None of their proposed global zero-free
conclusions is an input. The new deductions below are separately identified.

## 2. Arbitrary fixed order, including the actual dual conductor

**Theorem 1.** For every fixed integer r>=1, fixed 1/2<=sigma<1, and eta>0,

    sum_(Na<=U)^flat |L_F^S(sigma+it,psi chi_a)|^(2r)
      << U^(kappa_r(sigma)+eta)(2+|t|)^C,
    kappa_r(sigma)=max(1, r(1-sigma),
                         5/6+r(2/3-sigma),
                         1/3+r(11/12-sigma)).           (2.1)

For 0<y<=1/2, the corresponding exponent is

    kappa_r(1-y)+r(1-2y).                               (2.2)

The constants and height exponent may depend on r and the fixed lines/data.
There is no uniformity in growing r. On any fixed finite set of real strips the
height powers can be fixed before taking sufficiently small norm losses, by
using bounded small positive Mellin shifts and absorbing their blow-up in the
constants. Alternatively, for a single zero-density application, choose the
small height exponent after the finite norm-loss parameters have been fixed.

**Proof.** Apply the complete AFE to L(s)^r, on each actual conductor dyad
Q0<=Q<2Q0, Q0<<U. Its two pieces have length Q0^(r/2), up to a small U power
and a fixed polynomial height factor. The main coefficients are the complete
ordered divisor coefficients d_r(n)n^(-s), with their actual complex phases.
The dual scalar has modulus Q^(r(1/2-sigma)) times a polynomial height factor.
Its squared modulus is Q^(r(1-2sigma)). No negative power of Q is replaced
by a negative power of U.

Mellin inversion on a small positive line separates the smooth conductor weights
into common column arrays and bounded-modulus row phases. The real conductor
power costs U^O(delta). Split finite gamma/S types. The Mellin kernels have
integrable, polynomially weighted tails; truncate them first, apply Minkowski,
and then pass through their absolutely integrable tails. Both AFE pieces are
retained by |A+epsilon B|^2<=2(|A|^2+|B|^2). Root numbers have modulus one.

For a dyadic product range Nn~V and coefficient line s0, the coefficient bound
is |b_n|<<(Nn)^(-s0+delta), with a fixed divisor-function loss. Decompose

    n=c d^6, c sixth-free,
    (psi chi_a)(c d^6)
      =psi(c)psi(d)^6 chi_a(c) 1_((a,d)=1).              (2.3)

There is NO condition (c,d)=1. Exponents 7,13,... retain shared primes. The
twist need not have sixth power one, so psi(d)^6 is retained. For each d, the
c coefficient-square mass is O(V^(1-2s0+O(delta))/(Nd)^6). Apply (1.1) on the
positive row restriction (a,d)=1. Minkowski over d costs the convergent sum
sum_d (Nd)^(-3+O(delta)). Thus the full product dyad has row squared norm

    << (UV)^O(delta) V^(1-2s0) K(U,V).                  (2.4)

This keeps distinct ideals of equal norm, all product columns and their masks.
Subunit effective c-ranges are empty. Rapid dyadic AFE tails use the same bound
with the available decay, rather than being deleted at the formal AFE length.

For the main piece, maximize (2.4) on 1<=V<=Q0^(r/2). A negative V exponent
uses its small endpoint, not its large endpoint. The resulting upper bound is

    U + Q0^(r(1-sigma))
      + U^(5/6) max(1,Q0^(r(2/3-sigma)))
      + U^(1/3) max(1,Q0^(r(11/12-sigma))).             (2.5)

The U and the terms with a nonpositive Q0 exponent are bounded by U. In the
others, Q0<<U gives precisely (2.1). For the dual coefficient line 1-sigma,
all V exponents in V^(2sigma-1)K(U,V) are nonnegative. Its large endpoint,
multiplied by the ACTUAL Q0^(r(1-2sigma)), is

    Q0^(r(1/2-sigma)) K(U,Q0^(r/2)).                    (2.6)

The U term in (2.6) is at most U; each other term is bounded as in (2.5),
including when its Q0 exponent is negative. Sum conductor and norm dyads,
integrate the common Mellin parameters, and choose delta sufficiently small
for eta. Fixed omitted S Euler factors are finite Dirichlet-polynomial
operations, with line-dependent constants. The conjugate family obeys the
conjugate sieve. Finally the primitive functional equation at y, with its
positive conductor factor Q^(1/2-y), proves (2.2). QED.

At r=1 this gives the full second mean on the right half strip. At r=2 it gives
max(1,13/6-2sigma), already present in #971. For r>=4 it simplifies EXACTLY to

                    kappa_r(sigma)=max(1,r(1-sigma)).  (2.7)

Indeed the other affine terms differ from r(1-sigma) by 5/6-r/3 and 1/3-r/12,
both nonpositive. At r=3 the intermediate sixth-mean point is sigma=25/36.

### A finite interpolation description

At the four vertices

    (sigma,p)=(1/2,2), (7/12,4), (3/4,8), (1,infinity)  (2.8)

the full-family p-moment has exponent 1, with the last vertex understood through
Euler convergence on 1+delta and then arbitrary norm loss. Finite-vector complex
interpolation therefore gives sum |L(sigma+it)|^p << U^(1+eta)(2+|t|)^C on
the connecting segments in coordinates (sigma,1/p), where

    1/p=2-3sigma                    for 1/2<=sigma<=7/12,
    1/p=(11-12sigma)/16             for 7/12<=sigma<=3/4,
    1/p=(1-sigma)/2                 for 3/4<=sigma<1.   (2.9)

Use analytic dual vector weights in the strip, damp the height by a Gaussian,
apply scalar three-lines, then optimize the dual vector, exactly as in #974's
finite-vector lemma. First remove the finite inducing-principal list before
interpolating through Re s=1, so no principal pole lies in the analytic vector.
Add those rows back afterward on each fixed target line sigma<1 by their
classical fixed-function bounds. Finite row subsets can be chosen before this operation;
no independence from denominator zeros is required. The point (25/36,6) lies
on the middle segment. For every r>=4, the mean-U point (1-1/r,2r) lies on
the last segment. These observations do not require constants uniform in r.

## 3. Every fixed-order shifted detector still retains the same tail

Let lambda in [1/2,sigma), A=U^a, B=U^b, 0<=a<=b, and define the literal
finite mollifier

    M_A(s,chi)=sum_(Nd<=A) mu_F(d)chi(d)(Nd)^(-s),

over exterior ideals. Its 2k-th moment, for every fixed integer k>=1, is

    sum_(Na<=U)^flat |M_A(lambda+it,psi chi_a)|^(2k)
       << U^(m_k(lambda,a)+eta),
    m_k=max(1,ka(2-2lambda),
               5/6+ka(4/3-2lambda),
               1/3+ka(11/6-2lambda)).                 (3.1)

To prove this, power the actual polynomial; its product coefficient is bounded
by a fixed divisor function times (Nn)^(-lambda). Apply (2.3)-(2.4) to all
columns up to A^k. The unit/small endpoint contributes U. All other endpoints
give (3.1). The coefficient identity is not replaced by unweighted periodicity.

Let R count rows with one chosen zero in Re s>=sigma, |Im s|<=T. The shifted
rowwise detector in #971, Sections 3-4, before Holder, has the same Type-II tail
for every lambda. Its finite-height maxima can be paid by the neighboring-strip
subharmonic argument for L M_A and binary-prefix/Sobolev bounds for the tail.
Applying Holder with exponents 2r,2k and the remaining row factor gives

    sum_E |L(lambda+it)M_A(lambda+it)|
      <= R^(1-delta) U^(kappa_r(lambda)/(2r)+m_k(lambda,a)/(2k)+eta),
    delta=1/(2r)+1/(2k).                               (3.2)

Therefore the first detector term is controlled with count exponent

    g_I=[(lambda-sigma)b+kappa_r(lambda)/(2r)
                          +m_k(lambda,a)/(2k)]/delta. (3.3)

The other SIX endpoint terms remain

    (2-2sigma)b,  1+(1-2sigma)a,
    1/3+(11/6-2sigma)v,
    5/6+(4/3-2sigma)v,       v=a,b.                    (3.4)

This follows by solving R<=C R^(1-delta)U^d+C U^g: either the second term
is at least R/2, or R^delta<=2C U^d. It is a fixed-parameter statement.
The height power and all finitely many preliminary losses are absorbed by
choosing a sufficiently short fixed polynomial-height rectangle afterward.
The shifted detector and its maximal arguments are source-qualified imports
from #971; changing the Holder exponents above does not change those arguments.

Here is the decisive fact, independent of r,k,lambda,a,b:

    5/6+(4/3-2sigma)v = 5/6       at sigma=2/3.         (3.5)

For sigma<=2/3 and v>=0 it is at least 5/6. Thus optimizing ANY first-term
moment estimate while retaining (3.4) cannot certify a density exponent below
5/6 at 2/3. This is a property of the displayed upper-bound budget, not a lower
bound for R. The actual exceptional set could be empty.

## 4. An exact certificate valid for every order and interpolation

We now define the exponent-budget architecture precisely. A primitive numerator
budget is a pair (y,p) with the whole-family ell-p norm exponent e supplied by
(2.1)-(2.2), individual convexity, or Euler convergence. Write t=1/p. Permit
finite complex interpolation, Holder, restriction to the same zero-selected
subset, ell-p monotonicity and finite positive addition of bounds. No additional
mean estimate, coefficient cancellation, or dependence estimate is included.
Constants and arbitrarily small losses do not alter the zero-loss exponents.

After restriction, e is allowed to denote an upper-budget exponent for the
SELECTED ell-p norm, not just for the whole family. Fix one class count exponent
nu in [5/6,1]; the trivial full row count lets us cap it at 1. Its starting
whole-family budgets have e>=t>=nu*t. Interpolation preserves e>=nu*t;
selected ell-p monotonicity either adds nu times the increase of t to e or
decreases t while leaving e fixed. Finite positive addition also preserves it.
Thus every allowed selected budget retains e>=nu*t, and its final first-mean
budget m=nu*(1-t)+e satisfies m>=nu. These are invariants of the declared
upper-budget operations, not lower bounds for actual norms.

**Lemma 2 (supporting plane).** Every budget in this architecture satisfies

                      66e-55t+45y >= 27.               (4.1)

For 0<y<=1/2 the primitive budget from Theorem 1 obeys

    e >= 1/2-y+t,
    e >= 1/3-y/2+(5/6)t,
    e >= 11/24-y/2+t/3.                               (4.2)

Multiply these three inequalities by 24,34,8, respectively. Their coefficients
sum EXACTLY to

    66e >= 27-45y+55t.                                (4.3)

For 1/2<=y<=1, the middle affine term alone gives

    66e-55t+45y >= 22+12y >= 28.                       (4.4)

Individual convexity and the Euler vertex also satisfy (4.1). All coefficients
in (4.3) are nonnegative; no numerical search or finite moment-order limit is
part of this certificate. Complex interpolation is convex combination in
(y,t,e), so it preserves the affine inequality. Increasing an upper-bound
exponent also preserves it. On a subset counted by U^nu with nu>=5/6,
changing t upward by ell-p monotonicity costs nu times that change in e, hence
changes the left side of (4.1) by (66nu-55) times that change, a nonnegative
quantity. Changing t downward while keeping e only increases the left side.
This covers intermediate norm changes on the selected set, not only a final
application of Holder. Finite positive sums take a maximum and cannot lower
the certificate. QED.

In particular, if a class has count exponent nu>=5/6, its selected first-mean
budget m=nu(1-t)+e satisfies

                         66m+45y >= 82.                (4.5)

For p>=1, increasing nu can only increase m. Derived p<2 bounds obtained from
Holder/monotonicity are covered by the preceding argument. For y>1 the Euler
line y=1 gives an at least as good physical bound, so no such point is needed.
This lemma constrains what follows from the declared estimates. It does NOT
assert that an actual moment must be as large as its permitted exponent.

## 5. The 100/111 floor, including asymmetric scales

Consider the original CT scale monomial and the retained two-term physical norm

    X^(1/2-z) Z^(xi+z-1)Y^(w-1),
    |I| << [(XY+(XY)^2/Z)(1/X+1/Y)]^(1/2) Z^eta.       (5.1)

These are the pinned source contracts, not new estimates. Put X=Z^alpha,
Y=Z^beta, alpha,beta>0, alpha+beta<1. Define

    h=1-alpha, theta=max(alpha,beta)/2,
    b=5/6-alpha/3, boundary b+theta.                   (5.2)

The principal shift b follows from w=1,z=1/6, with the ACTUAL X exponent.
At frequency norm U=Z^h, a class placed on x=Re xi,y=Re w and assigned
selected numerator exponent m has positive-bound exponent

    E=x-1+alpha/2+beta(y-1)+(1-alpha)m.                 (5.3)

The z cost cancels exactly at this frequency scale. Allowing every real y in
[0,1], even before checking correction-domain restrictions, only makes the
budget more permissive. Thus an obstruction in this relaxed set also applies
to the source domain. A successful positive comparison must pay this dyad;
a different split of small/large frequencies cannot delete it. Contour buffers
and fixed norm losses vanish in the zero-loss necessary inequalities below.

**Theorem 3 (method saturation).** Suppose the complete zero stratification
retains (3.4), its numerator classes are bounded only by the architecture of
Section 4, and the physical estimate is (5.1). Then it cannot certify a strict
zero-free boundary less than 100/111 by this comparison, for ANY asymmetric
short-support scales. This says nothing about other proofs, actual lower
bounds, a signed comparison, or a strengthened Type-II/numerator estimate.

**Proof.** Every complete finite threshold partition has a class that must be
placed at x>=2/3 with count budget nu>=5/6. If the full good class is already
placed at x>=2/3 its count exponent is 1. Otherwise take the first class whose
upper threshold reaches 2/3. Its lower counting threshold is <=2/3, and (3.5)
forces the stated budget. No claim that this class is nonempty is needed:
the retained estimates must handle it without an additional emptiness theorem.
Skipping intermediate thresholds does not remove this class.

First take balanced scales alpha=beta=a. Then theta=a/2 and

    E-theta=x-1-a+a y+(1-a)m.                          (5.4)

At a0=15/37, (4.5) gives

    a0 y+(1-a0)m >= 82/111,
    E-theta >= 2/3-1-15/37+82/111 = 0.                (5.5)

For a<a0 this lower budget is strictly larger: the derivative of (5.4) in a
is y-1-m<0, since y<=1 and the declared whole-family/selected-set budgets have
m>=nu>=5/6. Thus smaller a cannot pay this class. Consequently

    a>=15/37,
    b+theta=5/6+a/6 >= 100/111.                       (5.6)

The single-class certificate is sharp in this relaxed budget: x=2/3,nu=5/6,
y=5/12,p=4,e=1/3 gives m=23/24 and equality in (5.5). Other classes may impose
a strictly larger bound, as they do in the existing compositions. We make no
claim that 100/111 is an achievable global estimate.

For asymmetric scales let c=boundary-5/6=theta-alpha/3. If alpha>=beta,
then c=alpha/6. Raising beta to alpha holds the boundary fixed and can only
decrease E-theta because y<=1. If beta>=alpha, hold c fixed and raise alpha
toward a=6c while keeping beta=2c+2alpha/3. This reaches alpha=beta=a.
Along that path the derivative of E-theta is

                    -1/2-m+(2/3)y < 0.                (5.7)

The inequality follows already from m>=5/6 and y<=1. Thus the balanced endpoint
is at least as favorable for every such class. If the original boundary were
less than 100/111, this endpoint would have a<15/37 and 2a<1, so the path stays
inside short support. The balanced obstruction applies. QED.

For completeness, taking alpha+beta>=1 in the SAME two-term physical estimate
cannot evade this floor: its physical exponent is now
theta=(alpha+beta+max(alpha,beta)-1)/2. If alpha>=beta the proposed boundary is
1/3+2alpha/3+beta/2, minimized on alpha+beta=1 at alpha=beta=1/2. If beta>=alpha
it is 1/3+alpha/6+beta, with the same minimum. Both give at least 11/12, which
is larger than 100/111. Thus the long-support regime of this retained norm has
no lower boundary than the short-support cases just analyzed.

## 6. A concrete native escape estimate

The immutable term in (3.5) comes from a particular original polynomial, not
from an unspecified inverse-L conjecture. Define

    c_A(n)=sum_(d|n, Nd<=A) mu_F(d).                    (6.1)

It has c_A(1)=1 and c_A(n)=0 for 1<Nn<=A. For A<=V, a real prefix cap
V<=H<=2V, and an actual row character chi=psi chi_a, put

    P_(a;A,V,H)(t)
      = sum_(V<Nn<=H, Nn>A) c_A(n) chi(n) (Nn)^(-2/3-it).  (6.2)

All sums are over exterior IDEALS, not rational norms with ideals merged.
The fixed S exclusions and every original nonunit zero remain. The cap H is
literal. In the zero detector, the additional monotone weights
(Nn)^(2/3-beta)exp(-Nn/B), for beta>=2/3, are recovered by partial summation
over these same prefixes; the rapid tail past B U^delta is retained and paid.
Sorting equal-norm ideals for binary-prefix bounds does not delete any of them.

For fixed d in n=c d^6 the coefficient is still c_A(c d^6), and the exact phase is

    psi(c)psi(d)^6 chi_a(c) 1_((a,d)=1).                (6.3)

Neither c_A nor this mask is replaced inside the polynomial by an unrelated
majorant. The existing PROOF of its norm estimate subsequently uses a divisor
bound and the sieve, which loses its specific Möbius-convolution cancellation.
Binary-prefix and Sobolev estimates give, with harmless logarithms and fixed
height powers absorbed,

    T(U,A,V,T):=sum_(U<=Na<2U)^flat
                 sup_(|t|<=T) max_(V<=H<=2V) |P_(a;A,V,H)(t)|^2
      << (UV)^eta(1+T)^C
           [V^(2/3)+U V^(-1/3)+U^(1/3)V^(1/2)+U^(5/6)]. (6.4)

The last term is EXACTLY

             V^(-1/3) [U^(5/6)V^(1/3)]=U^(5/6).       (6.5)

Changing the auxiliary lambda or Holder orders affects the L M_A term, not
(6.2)-(6.5). Therefore a concrete possible escape is a NEW bound for this
specific polynomial, for example replacing the final U^(5/6) in (6.4) by
U^(5/6-delta) on the scale ranges needed in a redesigned detector, while
retaining every term, cap, mask and the literal convolution. This estimate
is OPEN here. A generic improvement of the whole sieve is not claimed;
the coefficients in (6.2) are much more specific than arbitrary sieve columns.

The necessary numerical size of an escape can be stated exactly. At boundary
9/10 the favorable balanced scale is a=2/5. With the same numerator budget,
one cannot pass the x=2/3 class if its count exponent is at least 22/27.
An independent exact certificate is

                    27e-22t+18y >= 11.                 (6.6)

On the left half strip it is the sum of the three inequalities (4.2) with
weights 9,14,4. On the right half strip the middle affine bound gives
27e-22t+18y>=9+(9/2)y+t/2>=45/4>11. Its selected-norm closure is
explicit: for nu>=22/27, increasing t by ell-p monotonicity costs nu times
that increase in e, so the left side changes by (27nu-22) times the
increase, which is nonnegative. Decreasing t with e fixed also preserves
the plane. Interpolation, restriction and finite positive sums act exactly
as in Lemma 2; throughout, e>=nu*t remains an invariant of these budgets.
Thus (6.6) holds after every allowed selected-norm operation, not only at
the primitive whole-family vertices. At nu=22/27, (6.6) implies
9m+6y>=11, exactly E-theta>=0 at x=2/3,a=2/5. Monotonicity covers larger nu.

Thus a density-only change must get STRICTLY below 22/27 at 2/3; the fixed
5/6 contribution would need a saving exceeding

                        5/6-22/27=1/54.                (6.7)

This is NECESSARY, not sufficient: the other terms in (6.4), the L M_A detector
term, all other thresholds and all physical remainders must still be paid.
In particular merely replacing one exponent and reusing an old table is not
a new zero-free proof.

Alternatively, keeping nu=5/6 and the present favorable numerator line y=5/12,
the selected first-mean exponent is 23/24. The 9/10 budget would need it below
17/18, a strict saving exceeding

                       23/24-17/18=1/72.                (6.8)

This isolates a second concrete target on the zero-selected family. A coupled
or signed estimate can leave the architecture altogether; none is supplied by
the all-order theorem itself. These exact losses quantify what an all-order-only
proposal must overcome instead of suggesting that arbitrarily many moments
automatically reach the critical line.

## 7. Verification and scope

The accompanying checker authenticates the positive rational certificates,
the exact arithmetic of (5.5)-(5.6) and (6.6)-(6.8), the moment specializations,
the interpolation vertices, the literal sixth-power mask fixtures and the
native convolution/cap identities on a declared finite model. It uses explicit
failing checks in ordinary and optimized Python. Synthetic masks are not a full
number-field character census. The infinite all-order statement follows from
the written AFE proof and the affine certificates, not from a finite r sweep.

The floating optimizer in explore_envelope.py only suggested examples. It is
not a premise of any theorem, its numerical optimum is not claimed exact, and
no tiny new global fraction from that search is promoted. No original proof
or published #974 file is changed. The full physical Mellin projection and
native critical signed estimates remain outside what is proved here.
