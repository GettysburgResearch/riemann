# One source-exact polynomial remainder transport test

Status: bounded POST-QT / POST-JOINT-M3 experiment, design frozen BEFORE
evaluating the new polynomial-remainder criterion. This is not a blind
held-out point: index19 was selected because it had the best failing
joint-M3 ratio in the already observed fixed26-point comparison.

Exact source: QT `530732c5fd7f50364381f8af50e97ce809b674c5`.
Do not modify QT, the all-radius old-criterion obstruction or the joint-M3
packet. This experiment changes the remainder estimate, not source, gauge
or calibration.

## 1. Fixed finite experiment

Use ONLY zero-based QT critical-point index19, its full certified real
interval, lambda_(64), ratio r/y=1/2 and source precision512bits.
QT stores only coefficient-modulus upper bounds at orders8 through39,
not the signed complex coefficients needed below. BEFORE evaluating this
new criterion, explicitly correct that prerequisite: freshly evaluate one
40-term actual Xi jet at512bits over the inherited FULL certified real
critical interval, using the unchanged HA actual-Xi helper. No midpoint
substitution is allowed. The complete16x16 outer-cover bound for R=7/8
remains inherited from QT, whose exact science530732 has independent
reviewa99a357b. No new outer-cover evaluation is part of this experiment.

Use exactly N=32 terms of the joint companion remainder and exactly64
equal closed angular arcs covering the circle |w-i*y|=r. Each arc is
represented by outward512-bit sine/cosine intervals. Attempt all64 arcs,
including every failure. No alternate point, ratio, precision, Taylor
order, angular subdivision or source-parameter adjustment occurs.

## 2. Exact joint-polynomial remainder

Let g=f5, a=g(t), c=g''(t), with g'(t)=0 exactly at the inherited critical
point. Keep QT's q,d,y and quadratic P(w)=a+c*w^2/2-i*lambda*c*w.
If v_j=f^(j)(t)/j! are the literal Xi coefficients, then

    R(t+w)-P(w) = sum_(n=2..31) A_n w^n + tail,
    A_2 = -i*lambda*f8(t)/2,
    A_n = [f^(n+5)(t)-i*lambda*f^(n+6)(t)]/n!  (n>=3).

The zero constant and linear terms use the EXACT equation f6(t)=0;
they are not numerical midpoint substitutions. The quadratic f7 terms
cancel algebraically before interval evaluation. Coefficients are evaluated
over the entire unknown-t real interval.

For h>=|w| with h<R and x=h/R, a valid bound for the omitted tail is

    M*x^N * [5!*binom(N+5,5)/(R^5*(1-x)^6)
             +lambda*6!*binom(N+6,6)/(R^6*(1-x)^7)],

where M bounds literal Xi on the inherited outer rectangle around every
admissible t. This follows from Cauchy and the same binomial tail inequality
proved in QT. It bounds both entire companion tails, not f8 alone.

On each of the64 circle arcs, evaluate the polynomial by outward complex
Horner arithmetic and add the uniform scalar tail. Compare its upper
modulus with the uniform positive model margin
|c|*r*(d-r/2). ALL arcs must pass strictly to invoke Rouche.
Otherwise the experiment is UNRESOLVED, not a root nonexistence theorem.

If the full circle passes, separately require the complete known HA
root rectangle to lie inside the transport disc for ALL unknown t,y,r
in their source enclosures. Mere overlap is insufficient. A matched result
then inherits the already separate noncommon-root guards.

## 3. Evidence contract

The first output must retain the exact source identity, complete64 arc
stream, inherited critical/jet/cover identity, interval q/d/y/r, tail,
margin, every strict comparison and full-rectangle matching result.
Positive assertions require source authentication, resource/type guards,
fresh arithmetic replay in both modes and independent review.
Analytic Rouche/Cauchy review remains distinct from machine replay.

This tests one deliberately selected existing source point. It does not
give a cofinal theorem, an independent new zero census, general capture,
innerness, RH or novelty/priority. It is not excluded by the all-radius
obstruction to the DIFFERENT separate-triangle criterion.

## 4. Preregistration correction before new arithmetic

The original design689a93971cdd741a2b154f9506672667aa1a32dc incorrectly
described a reusable inherited signed coefficient array. The correction
above is frozen in a separate successor commit BEFORE any new arithmetic.
It adds only the necessary fresh signed40-term real-interval jet. Node19,
ratio1/2, precision512bits, N32, all64equalclosedarcs, source rectangle,
outer-cover bound and all no-tuning conditions are unchanged.

## 5. Complete analytic justification

JP1. Let f be entire and Schwarz-real, g=f^(5), and let t be a REAL
zero of f^(6). Write a=f^(5)(t), c=f^(7)(t), lambda>0. Assume ac<0 and
0<2q<lambda, where q=-a/(lambda*c). Set
d=sqrt(lambda^2-2lambda*q)>0, y=lambda-d=2lambda*q/(lambda+d)>0.
For 0<r<min(y,2d), put P(w)=a+c*w^2/2-i*lambda*c*w.
Then

    P(w)=(c/2)(w-i*y)(w-i*(lambda+d)).

The circle |w-i*y|=r lies in the open upper half-plane. Its interior
contains exactly the first model zero, with multiplicity one. On that
circle, the second factor has modulus at least2d-r; hence

    |P(w)| >= |c|*r*(d-r/2) > 0.

JP2. Entire Taylor expansion at the exact unknown real t gives
g(t+w)=sum_(n>=0) f^(n+5)(t) w^n/n! and
g'(t+w)=sum_(n>=0) f^(n+6)(t) w^n/n!. Subtract P before evaluation.
The constant companion correction and g-linear term vanish by the exact
equation f6(t)=0. The f7 quadratic and companion-linear terms cancel.
Thus the coefficients in section2, including A2=-i*lambda*f8(t)/2,
are exact. Replacing f6(t) by the value at the numerical center would
invalidate this cancellation; the producer never does so.

JP3. Suppose |f(t+z)|<=M for |z|<=R, for every possible true t in the
certified real interval. Cauchy's coefficient estimate gives
|f^(j)(t)|/j!<=M/R^j. The two tails n>=N in g and lambda*g' therefore
have combined modulus at most the section2 tail bound whenever |w|<=h<R.
Indeed, for each integer p>=0, j>=0,

    binom(N+j+p,p) <= binom(N+p,p)*binom(j+p,p),

because every factor obeys l*(N+j+l)<=(N+l)*(j+l), l=1,...,p.
Summing against x^j and using
sum_(j>=0) binom(j+p,p)x^j=(1-x)^(-p-1), 0<=x<1,
proves the bound for p5 and p6. This proves the infinite tail; testing
finitely many binomial inequalities is only a separate implementation
control. N32 uses signed Xi coefficients through index37; the fixed fresh
40-term jet also reproduces the entire inherited modulus panel8..39.

JP4. For theta in each of the64 closed intervals
[2*pi*j/64,2*pi*(j+1)/64], form w=i*y+r*(cos(theta)+i*sin(theta)).
Outward sine/cosine interval evaluation and complex Horner enclose the
finite polynomial at every such w, simultaneously for the entire allowed
real t and its induced y,r,lambda,c. The intervals cover the whole circle,
including all shared endpoints and angles0/2pi. Interval dependencies may
widen the enclosures but do not remove points. Although the rectangular
arc enclosure can contain points with |w|>h, only the TRUE circle is used
for the tail: every true circle point satisfies |w|<=y+r<=h. This does not
assume that the entire arc rectangle lies in the Cauchy disc.

If every polynomial-modulus upper bound plus the tail upper bound is
strictly smaller than the positive model-margin lower bound, then
|R(t+w)-P(w)|<|P(w)| on the full circle, with R=g-i*lambda*g'.
Rouche gives exactly one R zero counting multiplicity in the disc,
hence that zero is simple. Its imaginary part is positive. This argument
requires no inner-function hypothesis, no RH, and no physical projection.

JP5. A separately certified HA root lies in the parent rectangle.
The displacement calculation bounds the distance of EVERY point in that
rectangle from EVERY center t+i*y allowed by the source enclosures.
A strict upper displacement below the lower bound for r puts the whole
rectangle inside the transport disc. Its known R zero must equal the
unique newly transported zero. This transfers only the independently
certified parent guards; the transport lemma alone does not establish
C5 or any other numerator's nonvanishing.

## 6. Actual source, inheritance and observed result

The source is exactly f(z)=xi_R(1/2+i*z), evaluated by the unchanged
HA completed-zeta formula with pinned python-flint0.9.0 / FLINT3.6.0 runtime.
The manifest authenticates all five QT files, both JP preregistrations,
and QT's independent review
a99a357b96abf535af79a20d5e1948aed6bd3da7. QT in turn authenticates
HA, BC and OA executable sources and native runtime. Local imported QT/HA
files must equal their frozen source hashes.

QT's proof and accepted review supply the exact simple real critical
point inside the full interval t0 +/- 2^-120. The inherited fixed16x16
cover supplies a bound on the ENTIRE rectangle
[t0-R-2^-120,t0+R+2^-120] + i[-R,R], including the radius-R discs
around all possible true t. All256 cell counts, absence of failures,
the cell-stream hash and the maximum upper bound are preserved.
This packet authenticates and inherits those critical/cover certificates;
it does NOT freshly repeat the full26-node QT suite or the256 cover calls.

The fresh signed40-term jet is evaluated over that complete real interval.
Its real projections are legitimate because f^(j)(t) is real at real t;
each original complex enclosure's imaginary interval is checked to contain
zero and is also preserved in the fixture. The fresh T,a,c,lambda and
coefficient-modulus8..39 enclosures agree exactly with QT's frozen512-bit
jet metadata. No midpoint derivative or Gaussian surrogate is used.

Observed native result: all64 preregistered arc comparisons PASS and the
FULL parent HA rectangle matches. The worst error-upper/margin-lower
ratio is below the exact rational4/5, with the communication-only decimal
approximately0.7736072904. The tail/margin is approximately5.35e-7.
The full parent displacement divided by the radius lower bound is below
the exact rational3/10 (approximately0.26957819). The fixture retains
exact rational endpoints, not these explanatory decimals.

The calibrated lambda_(64) is approximately0.8616990871, not64.
The model center height is approximately0.1665054754 and r=y/2 is
approximately0.0832527377. This one source-exact local transport succeeds
although the different separate-M3 and joint-M3 sufficient bounds failed.
There was no new selection, changed radius, precision, order, arc split,
calibration or outer-cover optimization after the result.

Selection was explicitly POST-RESULT from the prior joint-M3 comparison:
node19 was its best failing point. This is constructive recovery at one
known point, not blinded predictive evidence, a new global census or a
uniform family theorem. A nonreal zero of the companion f5-i*lambda*f6
is not a nonreal classical-Xi zero and does not contradict RH.

## 7. Bounded certificate and replay contract

Arithmetic is MIXED: directed FLINT complex/real balls, exact rational
endpoint comparisons and complete finite64-arc coverage. The JSON parser
rejects duplicates, floating/nonfinite primitives, invalid types and
declared resource-cap violations; rational pairs retain strict canonical
integer components. Acceptance checks source/artifact/payload locks and
genuinely rebuilds the fresh signed jet and all64 arc comparisons.
No Python assertion is a scientific acceptance condition.

The source scope is finite and inherited where stated. Eight exact
rational-complex polynomial identities are reconstructed by direct
derivative sums and a separately organized remainder Horner recurrence;
130 exact binomial controls check the two coefficient shifts. These do
not replace the all-n analytic proof. Successful scientific acceptance
also requires independent exact-SHA review.

    python -B -m unittest tests.test_xi_joint_polynomial_point_transport
    python -B -O -m unittest tests.test_xi_joint_polynomial_point_transport
    python -B research/exploratory/xi_joint_polynomial_point_transport.py --check
    python -B -O research/exploratory/xi_joint_polynomial_point_transport.py --check

Both --emit and --emit-sources produce deterministic JSON after LF
normalization. The producer never writes or moves files. An unresolved
arc remains explicitly recorded and prevents a transport assertion;
insufficient comparisons would not establish root nonexistence.

No claim is made about other points, a growing-height limit, actual
innerness, corrected physical capture, RH, or external novelty/priority.
