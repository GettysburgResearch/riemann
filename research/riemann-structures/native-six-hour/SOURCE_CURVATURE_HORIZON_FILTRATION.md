# Exact product-horizon filtration of literal source curvature

This theorem was derived before the held-out horizon acquisition and before
inspection of its results. Calibration was already queued or running. The
new proof is separate from the calibration executable and its original
declaration; it does not retrospectively change either. No scientific job
is run by the author, and no physical-ratio rank is inferred here.

Use the same finite-prime native half-source as
`MULTIGROUP_NATIVE_CURVATURE_DIMENSION.md`, with r>=1 distinct primes
ell_1,...,ell_r and one independent schedule u_i for each prime. Arithmetic
indices are supported on these primes. The source formula and factor2
current are those of L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`.

Let W be the span of the actual polynomial curvatures

    C_(n,m)=2 d(lambda_n) wedge d(lambda_m).

Give du_i multidegree e_i. Write W_d for the homogeneous component of
total multidegree d in{0,1,2}^r, and let W_H be the span of the actual
ordered-pair curvatures with nm<=H. Define the arithmetic cost

    q(d)=product_i ell_i^(d_i).

## 1. The exact filtration, not just an upper bound

For every integer H>=1,

    W_H = direct_sum_(d in{0,1,2}^r, q(d)<=H) W_d.     (1)

For the forward inclusion, each lambda_n is separately affine in the
schedules. If u^a occurs in lambda_n, with a in{0,1}^r, then ell_i divides
n whenever a_i=1. Thus product_i ell_i^(a_i) divides n. A curvature term
from u^a in lambda_n and u^b in lambda_m has total differential multidegree
d=a+b, so q(d) divides nm. Every homogeneous component of C_(n,m) has
cost at most nm and belongs to the corresponding W_d. This proves that
W_H is contained in the right-hand side.

For the reverse inclusion, fix d and any admissible split a+b=d with
a,b in{0,1}^r. Take the actual squarefree indices

    n=product_i ell_i^(a_i), m=product_i ell_i^(b_i).

Their half-source coefficients are pure monomials,
lambda_n=(-1/2)^(sum a_i)u^a and
lambda_m=(-1/2)^(sum b_i)u^b. Therefore their curvature is a nonzero
constant multiple of d(u^a) wedge d(u^b), whenever that form is nonzero.
Moreover nm=q(d) exactly. All admissible splits at this exact product
span W_d, by the multigroup theorem. Hence W_d is already contained in
W_(q(d)), proving(1).

The full lambda_n at a higher prime power can mix several polynomial
degrees. Accordingly q(d) is a filtration cost on the curvature span;
this theorem does not assert that all arithmetic coefficient labels n
are homogeneous for that degree, or assign a new arithmetic grading to
the Euler product.

## 2. Rank jumps and the nonnegative multigraded character

Let m(d)=#{i:d_i=1} and k(d)=#{i:d_i=2}. The independent source dimension
formula specializes to

    beta(d)=dim W_d=
        m(d),   if k(d)>0;
        m(d)-1, if k(d)=0 and m(d)>0;
        0,      otherwise.                            (2)

Equations(1)--(2) give the exact literal rank at every horizon:

    rank_literal(H)=sum_(q(d)<=H) beta(d).             (3)

Unique factorization makes the costs q(d) distinct for distinct d. Thus
each nonzero beta(d) is the exact jump at its own cost; there are no hidden
coincident arithmetic thresholds in this finite family. In particular
the literal rank is nondecreasing. This says nothing yet about the rank
after combining equal physical ratios.

The polynomial recording these nonnegative dimensions is

    sum_d beta(d)x^d
      =sum_i x_i product_(j!=i)(1+x_j+x_j^2)
                            - product_i(1+x_i)+1.     (4)

The first sum contributes m(d); the subtraction removes one precisely
for nonzero degrees with no saturated coordinate, while the final1
repairs the zero degree. Hence despite the displayed subtraction, its
coefficients are exactly the nonnegative dimensions in(2). It is an honest
multigraded curvature character, not a proposed Hilbert numerator of a
new algebra or an alternating count substituted for a source rank.

At x_i=1 the full dimension is

    r*3^(r-1)-2^r+1.

For r>=2, order the primes increasingly and put K=product_i ell_i. The
first horizon at which the full literal rank is attained is exactly

    H_full=K^2/ell_1.                                 (5)

Indeed every nonzero component has at least one coordinate below2, so
its cost is at most K^2/ell_1. The degree (1,2,...,2) has cost equal to
that bound and dimension1. By(1) it is absent at every smaller horizon.
For r=1 the curvature space is zero at every horizon, so this nontrivial
first-saturation statement is not applied.

## 3. Complete hand-derived prediction for primes2,3,5

Here K=30, the full source dimension is20, and(5) gives450 rather than
the earlier safe squarefree-pair bound900. Enumerating only the27 possible
degrees in{0,1,2}^3 by(2) gives the following nonzero jumps. These entries
are theorem consequences, not measurements from the held-out atlas.

| Product horizon | Multidegree d | Jump | Cumulative literal rank |
| --- | --- | ---: | ---: |
| 6 | (1,1,0) | 1 | 1 |
| 10 | (1,0,1) | 1 | 2 |
| 12 | (2,1,0) | 1 | 3 |
| 15 | (0,1,1) | 1 | 4 |
| 18 | (1,2,0) | 1 | 5 |
| 20 | (2,0,1) | 1 | 6 |
| 30 | (1,1,1) | 2 | 8 |
| 45 | (0,2,1) | 1 | 9 |
| 50 | (1,0,2) | 1 | 10 |
| 60 | (2,1,1) | 2 | 12 |
| 75 | (0,1,2) | 1 | 13 |
| 90 | (1,2,1) | 2 | 15 |
| 150 | (1,1,2) | 2 | 17 |
| 180 | (2,2,1) | 1 | 18 |
| 300 | (2,1,2) | 1 | 19 |
| 450 | (1,2,2) | 1 | 20 |

There are no other literal jumps. Rank6 atH25 is an already known
comparison. The rank20 prediction at450 and its persistence at all
larger horizons follow from the proof, independently of a numerical
matrix census. An exact source acquisition should test these predictions
after constructing the actual full curvature rows; it must not assign
them in place of calculating the rows and their ranks.

## 4. What remains a separate physical question

Multiplying individual labelled rows by their nonzero1/sqrt(nm) factors
does not change their span. Combining rows at a common reduced ratio does
change the map. At ratio a/b the curvature row is proportional to

    sum_(d^2 ab<=H) C_(da,db)/d.

Those sums can mix the polynomial multidegrees in(1). Equation(3) is
therefore not a formula for a fixed-H physical rank, its monotonicity,
or its first saturation horizon. The full prime-power census and these
actual1/d weights remain necessary for that question. The independent
same-path joint-prefix recovery theorem also remains valid, but it is a
different observation from one fixed field or one scalar energy.

All claims here concern the finite-prime literal source and its filtration.
No full retained-gamma decoder, principal-member bound, or transport of
the H25 optimal path to a different horizon is inferred.
