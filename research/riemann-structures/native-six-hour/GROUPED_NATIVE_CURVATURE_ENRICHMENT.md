# Exact curvature dimension after grouped native synchronization

Status: proof and preregistration, before the two new finite acquisitions.
This is a theorem about the literal native half-source, its original
polarized current, and labelled integrated coefficients. It makes no
claim about physical ratio coalescence rank or a complete retained-gamma
decoder.

The source is the continuous half-divisor geodesic in
`L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md`
at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`.
The earlier complete source-curvature theorem is frozen at
`6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537`, and its occupation convention
at `a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc`.
The elementary polynomial calculation below extends those source
calculations. It is not a new general theorem about differential forms.

## 1. The actual grouped source is the full polynomial rectangle

Fix disjoint sets of distinct primes, with sizes p>=1 and q>=1. Give
every prime in the first set the same schedule u and every prime in the
second the same schedule w. Work over Q. For a supported integer n,
let lambda_n(u,w) denote the coefficient in the native product

    product_l [u_l sqrt(1-x_l)+(1-u_l)sqrt(1-x_l^2)].

If c_e=[x^e]sqrt(1-x), its local coefficient is

    1_(2|e)c_(e/2) + u_l(c_e-1_(2|e)c_(e/2)).

Consequently every lambda_n belongs to

    V_(p,q) = span_Q{u^i w^j: 0<=i<=p, 0<=j<=q}.

This is equality of spans for the actual source. For a squarefree n
using i primes from the first group and j from the second,

    lambda_n=(-1/2)^(i+j)u^i w^j.

All these constants are nonzero. Thus the squarefree source coefficients
already span V_(p,q); coefficients at higher prime powers cannot enlarge
that function space. This conclusion uses source coefficients, not a
postulated polynomial observation.

For an ordered pair define its native one-form and curvature by

    alpha_(n,m)=2 d(lambda_n) lambda_m,
    C_(n,m)=2 d(lambda_n) wedge d(lambda_m)=-d(alpha_(n,m)).

The sign in this convention agrees with the earlier source: the path
w-then-u minus the path u-then-w around a rectangle integrates C with
positive du dw area.

## 2. Exact dimension and the single missing corner

The Q-linear span of all C_(n,m) is exactly

    W_(p,q) = span_Q{u^r w^s du wedge dw:
                    0<=r<=2p-1, 0<=s<=2q-1,
                    (r,s)!=(2p-1,2q-1)}.

In particular its dimension is 4pq-1.

For f=u^i w^j and g=u^k w^l, the coefficient of df wedge dg is

    (i*l-j*k) u^(i+k-1) w^(j+l-1).

Terms with either exponent formally negative have zero coefficient.
The possible nonzero exponents lie in the displayed rectangle.
At its top corner the only split is
(i,j)=(k,l)=(p,q), and the determinant is zero.

Conversely fix a=r+1 in {1,...,2p} and b=s+1 in {1,...,2q}.
Admissible monomial pairs are obtained by choosing integer i,j in

    max(0,a-p)<=i<=min(p,a),
    max(0,b-q)<=j<=min(q,b),

then taking k=a-i and l=b-j. Their determinant is i*b-j*a.
If a<2p, the first interval contains at least two integers; fixing j
and changing i changes the determinant by the positive integer b.
At least one choice is nonzero. If a=2p but b<2q, the same argument
changes j, and the determinant changes by -a. This proves every
monomial other than the top corner occurs. Since these pairs can be
chosen among the actual squarefree coefficients in section1, it also
proves the result for the native source itself.

Let K be the product of the p+q primes. Each such squarefree index is
at most K, so all required ordered pairs occur in the literal source
at physical-product horizon K^2. This is a safe horizon bound, not a
claim that every pair up to that horizon must be enumerated to prove
the theorem.

## 3. Complete literal source readout through occupation moments

For each exponent pair in W_(p,q), define

    M_(r,s)(gamma) = 1/(s+1) integral_gamma u^r w^(s+1) du.

Every grouped native alpha_(n,m), at any supported prime powers,
is a Q-linear combination of these one-forms plus an exact polynomial
differential. Indeed its negative exterior derivative belongs to
W_(p,q), while

    -d[u^r w^(s+1)du/(s+1)] = u^r w^s du wedge dw.

Subtract the corresponding linear combination. The remaining polynomial
one-form is closed and is exact: integrate its du coefficient in u;
closedness makes the remaining dw coefficient depend only on w, where
it can also be integrated. Characteristic zero is used here.

For paths with fixed endpoints (0,0) and (1,1), every complete labelled
pair coefficient therefore has the form

    B_(n,m)(gamma) = b_(n,m) + sum_(r,s) c_(n,m;r,s) M_(r,s)(gamma),

with fixed rational coefficients. The coefficient matrix has rank
4pq-1, because its columns are precisely the independent source
curvature directions already proved above. Two such paths have the
same complete literal integrated source if and only if all these
occupation moments agree. The squarefree source-basis panel suffices
for that comparison.

This is the minimal dimension of this affine-linear source readout,
or equivalently of source one-forms modulo exact endpoint terms. It
does not assert independent attainability of arbitrary moment tuples,
nor a lower bound for unrestricted nonlinear encodings.

## 4. Actual monotone path differences span every direction

The rank is realized by actual monotone path differences, not just
formal two-forms. Take the grid of centers

    u_a=a/(2p+1), 1<=a<=2p,
    w_b=b/(2q+1), 1<=b<=2q,

omit its top-right center, and use square half-width

    h=1/[8(2p+1)(2q+1)].

All these rectangles lie strictly inside the unit square. For each,
use a common monotone prefix from (0,0) to its lower-left corner and
a common monotone suffix from its upper-right corner to (1,1).
The two middle paths traverse w-then-u and u-then-w. Their integrated
source difference is the rectangle integral of C_(n,m).

These 4pq-1 rectangle functionals are independent on W_(p,q).
For point evaluations, the full 2p by2q tensor Vandermonde matrix is
invertible. Delete the top monomial and the top-right point. The
remaining minor is nonzero: the corresponding entry of the inverse
full matrix is the coefficient of the top monomial in the product
of the two univariate cardinal Lagrange polynomials, and that
coefficient is nonzero.

Rectangle averaging preserves this conclusion. Dividing by its area,
the average of u^r w^s is u^r w^s plus terms with smaller coordinate
degrees. It is an invertible triangular operator preserving the space
with the top corner omitted. Thus its evaluation minor is also
invertible. The actual path-difference vectors consequently span
the whole source variation space of dimension4pq-1.

Only a linear-span conclusion is intended. An individual monotone
path still obeys moment inequalities. Source independence also does
not imply independence after physical weights, ratio coalescence,
or a different observation.

## 5. A family of actual physical prefixes separates the source

There is a precise positive physical consequence if one retains the
whole family of native product prefixes, with the same labelled path
at every cutoff. Let

    F_H(t)=sum_(nm<=H) B_(n,m)/sqrt(nm) exp(it log(n/m)),

where n,m run over the supported integers and H is a positive integer.
This is the original finite physical field, not just its squared norm.
At a fixed reduced ratio a/b its coefficient is

    z_H(a/b)=1/sqrt(ab) sum_(d^2 ab<=H) B_(da,db)/d.

Define F_0=0. For every supported pair n=da,m=db,

    z_(d^2 ab)(a/b)-z_(d^2 ab-1)(a/b)=B_(da,db)/(d sqrt(ab)).

There is just one equal-ratio summand at that product. Hence the
complete prefix family recovers every labelled pair coefficient.
Each z_H is determined by the actual L2(nu) field: finite distinct
exponentials are independent in the original nonzero observation
measure, as in the frozen curvature source. Diagonal pair coefficients
also follow from the fixed endpoint identity
`B_(n,n)=lambda_n(1,1)^2-lambda_n(0,0)^2` and have no path variation.

In particular the finite collection of fields for1<=H<=K^2 separates
all4pq-1 grouped source-variation directions, because it recovers the
squarefree source-basis panel from section2. The joint physical-prefix
readout therefore has the full source rank. This does not assert that
one fixed H has that rank, that squared energies recover fields, or
that the reconstruction is uniformly well conditioned as H grows.
Arbitrary masks or source paths changing with H are not substituted
for the stated common-path product-prefix family. No retained-gamma
decoder is inferred.

## 6. Comparison and held-out source predictions

The cases (p,q)=(1,1) and (2,1) give dimensions3 and7, respectively.
They are comparison cases, including the earlier synchronization-fiber
calculation; they are not new held-out cases.

The separate preregistration fixes (p,q)=(3,1) and (2,2), both on
the primes2,3,5,7. Their predicted dimensions are11 and15. Every
registered rank will be obtained from the literal local binomial
coefficients and differentiated pair currents, with complete matrices
and monotone rectangle witnesses retained. No physical-rank claim
is included in these predictions.
