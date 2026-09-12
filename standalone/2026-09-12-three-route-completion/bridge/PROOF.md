# BQ26: a quantitative finite-moment feasibility test for the spin route

Status: **PROPOSED elementary theorems and an exact synthetic countermodel.**
Scope: a necessary condition for Laguerre--Polya (LP) moment realization;
not an obstruction evaluated against theta, and not an RH result.
Dependencies: the classical even LP product; the Lee--Yang implication for
finite pair ferromagnets as used in PR847 and PR863; finite spectral theory.
Actual execution: `verify.py` reconstructs the rational source, moments,
positive forms and robust exclusion from first principles. No supplied zero
or theta-moment data are read. Normal and optimized runs both passed.
Smallest open gap for the native programme: construct an admissible extension
for the actual theta moments. This necessary test does not construct one.

## 1. Why this is part of the completion attempt

PR842 at `4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5` constructs a positive finite
quadrature for the logarithmic derivative from positive cumulant forms. Its
proof correctly warns that positive quadrature weights do not provide integer
analytic multiplicities, so integrating the resolvent need not produce an
entire function. Here that warning becomes a quantitative, finite-degree veto.
It can be checked before trying to lift a moment target into a spin model.

The two positivity tests in Section 3 below both pass **strictly**, and the
target is the moment jet of an actual positive symmetric probability law.
Nevertheless no finite ferromagnet, and no even LP characteristic function,
can approximate its first three even moments arbitrarily well. Thus neither
ordinary moment positivity nor a finite positive cumulant quadrature closes
the graph-extension problem. This is a changed-source countermodel, with no
claim that the actual theta moments have this defect.

## 2. BQ26-1: integer spectral occupancy is quantitatively constrained

Let an even, real LP entire function with F(0)=1 have the product

    F(z) = exp(-gamma z^2) product_j (1-lambda_j z^2),
    gamma >= 0, lambda_j > 0, sum_j lambda_j < infinity.       (1)

Each repeated zero is listed repeatedly. Its multiplicity is an INTEGER;
the list may be finite or countably infinite. This includes finite weighted
zero-field pair ferromagnets and their normalized locally uniform limits.
The product statement is the classical LP representation, not a new
classification of limits of spin laws. It is not asserted that every (1)
is a characteristic function.

Define q_k locally at zero by `-log F(z)=sum_(k>=1) q_k z^(2k)/k`.
Then

    q1 = gamma + sum lambda_j,
    q2 = sum lambda_j^2,
    q3 = sum lambda_j^3.                                  (2)

Assume q2>0 and put

    a=q2/q1,     b=q1^2/q2,
    delta=q1*q3/q2^2-1.

**Theorem.** Delta is nonnegative, and some nonnegative INTEGER m satisfies

    |b-m| <= b (4 delta + 2 sqrt(delta)).                   (3)

In particular delta=0 forces b to be an integer. Formula (3) is invariant
under a real rescaling of the random variable or Fourier variable.

**Proof.** Use the positive measure

    nu=gamma delta_0 + sum_j lambda_j delta_(lambda_j).

Its mass is q1, its mean is a, and

    integral (x-a)^2 dnu(x) = q1 a^2 delta.                (4)

This proves delta>=0. Let I=[a/2,3a/2] and let m count the lambda_j in I,
with multiplicity. This number is finite, since each contributes at least
a/2 to q1. Write W=nu(I), U=q1-W. Every point outside I is at distance
at least a/2 from a, so (4) gives

    U <= 4 q1 delta,      m <= 2q1/a=2b.

Weighted Cauchy--Schwarz, on the individually listed nodes in I, gives

    |W-am|
      <= [sum_I lambda_j(lambda_j-a)^2]^(1/2)
         [sum_I 1/lambda_j]^(1/2)
      <= [q1 a^2 delta * 2m/a]^(1/2).

Consequently

    |b-m| <= U/a + |W-am|/a
           <= 4b delta + sqrt(2bm delta)
           <= b(4delta+2sqrt(delta)).

The Gaussian reserve is included in U. No simple-zero, finite-spectrum or
source-specific hypothesis was suppressed. QED.

### Conversion to actual probability moments

If `F(z)=E exp(izX)` is even and `e_k=E X^(2k)/(2k)!`, then exactly

    q1=e1,
    q2=e1^2-2e2,
    q3=e1^3-3e1e2+3e3.                                   (5)

Thus (3) is already a sixth-moment necessary condition. It concerns the
cumulant spectral measure, not the always-positive ordinary moment measure.
There is no assertion that (3) together with any fixed set of inequalities
is sufficient for LP membership or ferromagnetic realization.

## 3. BQ26-2: a positive probability target with strict finite cumulant forms

Take the exact rationals

    b=21/2,    d=1/10^6,
    q1=b, q2=b, q3=b(1+d), q4=b(1+3d).                    (6)

These are the first four moments, with the indexing used by CSI, of the
positive two-atom measure

    nu=(b/2) delta_(1-1/1000) + (b/2) delta_(1+1/1000),
    q_k=integral x^(k-1) dnu(x), 1<=k<=4.

Both CSI forms are strictly positive:

    G2=[[q1,q2],[q2,q3]],  det G2=b^2 d >0,
    J2=[[q2,q3],[q3,q4]],  det J2=b^2 d(1-d)>0.           (7)

The theta source of PR842 is not used here. Applying Newton identities to
(6) yields these candidate even probability moments:

| k | E X^(2k) |
|---|---|
| 0 | 1 |
| 1 | 21 |
| 2 | 1197 |
| 3 | 2543625063/25000 |
| 4 | 133540327053/12500 |

These really are moments of a positive probability law, rather than a
formal Taylor series. Here is an explicit construction using only rationals
and positive square roots. Put

    A0 = 21,
    A1 = 24100001/300000,
    A2 = 16460916190909/362727300000,
    B1 = 756,
    B2 = 177080077799999/90000000000,

and define the symmetric matrix

    T = [[A0, sqrt(B1), 0],
         [sqrt(B1), A1, sqrt(B2)],
         [0, sqrt(B2), A2]].                             (8)

Its first two Schur pivots are A0>0 and D1=A1-B1/A0>0;
the last is exactly A2-B2/D1=1. Thus T is positive definite.
Its off-diagonal entries are nonzero. The vector e0=(1,0,0) is cyclic
(look successively at e0,Te0,T^2e0), so T has three distinct positive
eigenvalues y_j with positive spectral weights w_j summing to one.

Let X take values `+sqrt(y_j)` and `-sqrt(y_j)`, each with probability
w_j/2. This specifies an exact six-atomic symmetric probability source.
Its characteristic function is the even entire function

    F(z)=sum_(j=1)^3 w_j cos(sqrt(y_j) z).                 (9)

Direct multiplication of (8) verifies
`e0^T T^k e0 = E X^(2k)` for 0<=k<=4 with the table above. The checker
replays these identities by all closed walks of length k on the three-node
path; each edge appears an even number of times, so all arithmetic is rational.
It also verifies positive definiteness of the ordinary 3-by-3 moment form and
the shifted 2-by-2 form. No rounded eigenvalues define this source.

Nevertheless, in (3) this target has b=10.5, delta=10^-6, and

    b(4delta+2sqrt(delta)) = 10521/500000 = 0.021042.

The interval [10.478958,10.521042] contains no integer. Therefore no function
of the form (1) has even the same q1,q2,q3. In particular no finite zero-field
pair ferromagnet matches the source (9) through moment six.

This does not dispute the all-order, source-complete CSI criterion. The
actual higher cumulants of (9) cannot keep satisfying all its positive forms.
Nor is an off-real zero of (9) a zero of Xi. The conclusion is about finite
positive spectral quadrature and its possible LP lift.

## 4. BQ26-3: the failure persists on an explicit open neighborhood

For any candidate q'_1,q'_2,q'_3 satisfying

    |q'_k-q_k| <= 1/10000,  k=1,2,3,                    (10)

define b',delta' as in Section 2. If delta'<0 then (4) already rules out
(1). Otherwise direct rational bounds give

    b_lo=11024790001/1050010000 <= b'
      <= b_hi=11025210001/1049990000,
    0<=delta'<1/20000,  sqrt(delta')<1/100.

Set R=b_hi(4/20000+2/100). Exact rational comparisons yield

    b_lo-R>10,   b_hi+R<11.

Thus (3) still cannot hold. This is an exclusion neighborhood with a fixed
width, not an argument depending on a singular positive moment matrix.

For convenience, using interval arithmetic on the polynomials (5), the
checker also verifies that errors at most 10^-7 in EACH raw moment
`E X^2, E X^4, E X^6` map strictly inside (10). Hence no finite pair
ferromagnet approximates those three raw target moments simultaneously to
that tolerance. The raw scale here is fixed by the exact table; rescaling
requires rescaling these tolerances as well.

## 5. Computation and mathematical review boundary

Run with the Python standard library:

    python -S -B verify.py --write result.json
    python -S -B verify.py --check result.json --self-test
    python -S -O -B verify.py --check result.json --self-test

All tests use explicit `raise` checks, so optimization does not remove them.
The artifact is accepted only when it equals a fresh reconstruction of all
reported values, with duplicate JSON keys rejected and JSON types preserved.
Three parser/comparison mutation controls reject a changed power sum, a
Boolean substituted for an integer, and a duplicate key. These are bounded
in-process controls, not three independent mathematical reconstructions.
Primitive inputs are the two rationals in (6); the actual
probability construction (8) is regenerated, not merely checked against a
self-consistent list of derived moments. The code uses no third-party
library, transcendental approximation, floating operation or zero table.

This is one implementation, not independent computational authorship.
The infinite LP representation and the Lee--Yang theorem are classical
mathematical dependencies; the exact checker does not prove either theorem.
The analytic proof of the new necessary inequality is supplied in Section 2.
There is no novelty claim for the general observation that zero
multiplicities are integral, or for classical truncated moment constructions.
