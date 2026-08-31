# The complete six-dimensional native path-variation span

Status: proposed source theorem with explicit rational witnesses; bounded
primitive replay is being prepared separately. This is the same source and
physical observation as the63-pair global experiment, not a new scalar model.

Fix primes2,3,5 and retain every ordered factor pair(n,m) with n*m<=25 whose
prime factors lie in that set. There are63 pairs. Let

    Lambda_n(u) = coefficient_n product_p [
        u_p sqrt(1-x_p)+(1-u_p)sqrt(1-x_p^2)].

All coefficients are literal rational polynomials in u=(u_2,u_3,u_5).
For a piecewise smooth monotone path u from0 to1, define the original
integrated source vector

    B(u)_(n,m)=2 int d Lambda_n(u(s)) Lambda_m(u(s)).                (1)

No physical multiplier has yet been absorbed into these coefficients.
The actual observation is

    O(B)(t)=sum_(n,m) B_(n,m)/sqrt(n*m) * (n/m)^(it),               (2)

in nu=|kappahat(t)|^2 dt/(2pi), with the frozen real kernel.

## 1. Fixed endpoint current and exact curvature

Let T swap the two factor coordinates. Direct differentiation gives

    (B+TB)/2 = Lambda(1) tensor Lambda(1)
               - Lambda(0) tensor Lambda(0),                    (3)

with the same product cutoff. Thus every path difference is antisymmetric.
Multiplication of the two formal factors kills it, and every unit coordinate
of a path difference vanishes. These are source identities before observation.

Define the vector-valued two-form coefficients

    C_ij(u)=2[partial_i Lambda tensor partial_j Lambda
              -partial_j Lambda tensor partial_i Lambda].      (4)

For a rectangle in the u_i,u_j plane, the native path j-then-i minus
i-then-j has source difference equal to the area integral of C_ij.
This sign follows either by four-edge integration or from
d(2dLambda tensor Lambda)=-C_ij du_i wedge du_j with the conventional
counterclockwise orientation. Both paths can have identical monotone
prefix and suffix joining0 and1; those pieces cancel exactly.

Let V be the rational span of every coefficient vector of these curvature
polynomials. Every endpoint-preserving native path difference belongs to
its real scalar extension. Indeed, interpolate two paths pointwise in the
convex cube. The resulting homotopy has fixed endpoints, and Stokes expresses
their difference as an integral of the curvature. No source coefficient is
replaced by an endpoint-only value map in this argument.

## 2. An explicit source basis and completeness

The horizon25 is below2*3*5, so no retained product contains all three prime
labels. For each pair of labels, direct local coefficient multiplication gives

    C_23 = V_23,0 + u_2 V_23,2 + u_3 V_23,3,
    C_25 = V_25,0 + u_2 V_25,2,
    C_35 = V_35,0.                                                (5)

Here23 labels the prime pair(2,3), not the integer23. The table lists all
nonzero entries with n<m; reversed entries are their negatives. Every
unlisted coordinate among the63 retained pairs is zero.

| vector | (n,m): coefficient |
|---|---|
|V_23,0|(2,3):1/2; (3,4):3/8; (2,9):-3/8; (2,12):-1/4; (3,8):-1/16|
|V_23,2|(2,6):-1/4; (2,12):3/16; (4,6):3/16|
|V_23,3|(3,6):1/4|
|V_25,0|(2,5):1/2; (4,5):-3/8|
|V_25,2|(2,10):-1/4|
|V_35,0|(3,5):1/2|

For example Lambda_2=-u_2/2, Lambda_3=-u_3/2,
Lambda_4=-1/2+3u_2/8 and Lambda_6=u_2u_3/4.
These give C_23(2,3)=1/2 and C_23(4,6)=3u_2/16.
The remaining entries follow from the same coefficient formula; the
bounded replay must reconstruct every local factor and every derivative
site, not merely compare this table with a copy of itself.

The six vectors are linearly independent, already as raw source vectors.
Equation(5) proves that no further curvature directions occur at this horizon.
Thus dim V=6.

There are also six EXACT path-difference witnesses, not only infinitesimal
or limiting vectors. Use rectangles of half-width1/16 with centers

    pair(2,3): (1/4,1/4), (3/4,1/4), (1/4,3/4);
    pair(2,5): (1/4,1/2), (3/4,1/2);
    pair(3,5): (1/2,1/2).

Fix the unused coordinate at1/2. The rectangle integrals in each prime pair
are its positive area times the coefficient vectors evaluated at the center.
The three center rows(1,c_2,c_3), the two rows(1,c_2), and the last constant
row have full ranks3,2,1 respectively. Hence these actual monotone
path differences span V. Combining this with the Stokes inclusion proves:

    span_R {B(u)-B(v): native monotone endpoint paths u,v}
       = V tensor_Q R,   dimension6.                             (6)

This is an equality of LINEAR SPANS. It does not say every vector of V,
with arbitrary coefficient size, is realizable by one monotone path.

## 3. Source-faithful observation on the variation span

Before evaluating any Gram matrix, coalesce physical ratios with their
correct weights. For a reduced ratio a/b, write n=ad,m=bd. Equation(2)
then has coefficient

    (1/sqrt(ab)) sum_d B_(ad,bd)/d.                              (7)

Using raw source coefficients as if the weight1/d were absent would be
a different map. For the six basis vectors, the following ratios provide
six independent pivots in the rationalized coefficient sum in(7):

| basis vector | reduced ratio | rationalized coefficient |
|---|---:|---:|
|V_23,0|3/4|3/8|
|V_23,2|1/3|-1/8|
|V_23,3|1/2|1/12|
|V_25,0|4/5|-3/8|
|V_25,2|1/5|-1/8|
|V_35,0|3/5|1/2|

At each listed pivot, the other five vectors have coefficient zero.
Thus O is injective on V. The real Gram form induced by the actual
original measure is strictly positive there: a nonzero finite exponential
sum cannot vanish on a set of positive measure, while the nonzero
compactly supported real kernel has a Fourier transform nonzero on an
open interval. Consequently its squared original-nu norm is positive.

This proves a source-owned six-dimensional physical variation space.
It does not infer accessibility from a formally negative or positive
ambient eigenspace. The six rectangle path differences form an authenticated
spanning basis, and the physical map is checked before any norm claim.

Because nu is even, the fixed symmetric field in(3) and the antisymmetric
variation fields are orthogonal. The former is an even real exponential
combination and the latter an odd imaginary one. This exact exchange
decomposition is tied to this source, observation and real kernel. It
does not identify an arbitrary Boolean parity quotient with the same space.

## 4. What this supplies and what remains open

The two-dimensional derivative space of a particular three-parameter
schedule at its diagonal path can sit inside this six-dimensional span.
Its rank is not the dimension of all native endpoint path variations.
Likewise, a common parameter shift away from that diagonal need not be a
common time reparametrization. The separate joint-metric packet tests those
finite nonlinear questions.

The affine relaxation B(u_0)+V has a unique least-energy projection under
the physical Gram norm. Its minimizer would only be a lower bound for the
attainable monotone-path problem until an actual path realizes it. This
packet makes no attainment claim and does not replace the path constraints
by unrestricted linear coefficients.

All conclusions retain the finite horizon25, the full63-pair source,
the original2ds measure and physical1/sqrt(nm) weights. They do not
identify the full retained carrier/renewal/selector source, reconstruct
the amplified principal member, or establish any RH/GRH bound.
