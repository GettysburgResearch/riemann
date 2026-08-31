# An attained original-kernel optimum on the synchronized native source face

This packet optimizes a whole, exactly attainable source subclass. The
source remains the horizon25 half-source on primes2,3,5, with all63
ordered factors, all45 physical ratios, actual2ds, and the original
Mellin measure nu. Its exact synchronized source and attainable face
are frozen at `a455dbe07c8d32fa3e7f3e74361abcfcafc681f9` in
NATIVE_PATH_SYNCHRONIZATION_AND_TEMPLATE_ACCESSIBILITY.md.
Only u=v is imposed. No output records are deleted,
and no substitute metric is introduced.

The synchronized-face theorem gives the complete attainable region

    K = {(D,E): 0<=D<=1, D/2<=E<=D-D^2/2}.              (1)

The observed field is

    F(D,E)=F0+D R0+E R1,
    R0=V25,0+V35,0, R1=V25,2.                           (2)

The source F0 has occupation coordinates(1/2,1/3,1/3,0,0,0).
Physical injectivity of the finite source implies that R0,R1 are
linearly independent in the original L2(nu). Thus their Gram matrix G
is strictly positive definite. If b_i=Re<F0,R_i> and c=||F0||^2, the
actual energy is

    I(D,E)=c+2b0 D+2b1 E+G00 D^2+2G01 DE+G11 E^2.       (3)

## 1. Why a complete convex-body certificate suffices

The set(1) is compact and convex: it is above a line and below a
concave parabola. Equation(3) is strictly convex, so there is exactly
one minimizer. A complete KKT point is therefore the unique global
minimum over this actual source subclass. No comparison with a grid
or with a single boundary curve is sufficient by itself.

Put g=G(D,E)^t+b, the half gradient. The candidate classes are:

* Interior: G(D,E)^t=-b, with both constraints strict.
* Straight boundary: E=D/2, g_D+g_E/2=0, g_E>=0.
* Curved boundary: E=D-D^2/2,
  g_D+(1-D)g_E=0, g_E<=0.
* At(0,0): g_D+g_E/2>=0 and g_D+g_E>=0.
* At(1,1/2): g_D+g_E/2<=0 and g_D<=0.

The scout certifies strict normal signs where available, rather than
silently deciding a zero interval. The straight-boundary stationary
point is

    D=-(b0+b1/2)/(G00+G01+G11/4).                        (4)

The restriction to the upper parabola is a quartic whose derivative
has coefficients, in increasing degree,

    2(b0+b1),
    2(G00+2G01+G11-b1),
    -3(G01+G11),
    G11.                                                (5)

All real roots in(0,1) are isolated by an outward interval Sturm
sequence. Polynomial division cancels its leading coefficient by
the exact algebraic definition; the other coefficients are enclosed
with outward-rounded interval arithmetic. A certified nonzero leading
coefficient is required at every division. Endpoint signs, total root
count, each isolated interval, and every candidate are retained.

Once an isolated root satisfies the full curved-boundary KKT sign,
strict convexity proves its global optimality on(1). The root need
not be rational: it is defined by the exact original-kernel cubic
and its certified isolating interval.

## 2. An actual monotone path realizes the optimum

Every point(1) is realized, including the optimum. For0<D<1 set

    lambda=(E-D/2)/(D(1-D)/2), 0<=lambda<=1,
    h=(1-lambda)D.

The path with u=v is

    000 -> (0,0,h) -> (1-D,1-D,h)
        -> (1-D,1-D,h+lambda) -> (1,1,h+lambda) -> 111.   (6)

Its exact occupation coordinates are D and E. At the lower boundary
lambda=0 it uses a constant intermediate height; at the upper
boundary lambda=1 it activates w at u=1-D. The endpoint cases have
the evident limiting paths. Assigning the five segments equal
parameter times gives a continuous piecewise linear monotone
primitive, so this is a source path rather than a formal convex
combination of fields.

Equation(6) uses the original2ds current. Its observed value is
unchanged by a common monotone reparameterization, but primitive
site-square ledgers need not be. The theorem does not optimize an
unidentified literal diagonal.

## 3. The original kernel selects a delayed final activation

The executed original-kernel certificate selects exactly

    (D,E)=(0,0).                                        (7)

Thus an optimal source path first increases u=v from0 to1 while w=0,
then increases w from0 to1. The unique minimizing field does not
require a unique parameterization of this path. Its original energy is

    I0 approximately 158.33334451701177.

The endpoint certificate is quantitative. The exact original half
gradients b satisfy the certified bounds

    b0+b1/2 approximately 5.773693577102361 > 5,
    b0+b1   approximately 5.356868909564772 > 5.          (8)

For D>0 the feasible ratio E/D lies in[1/2,1]. Therefore, if
kappa=min(b0+b1/2,b0+b1),

    b0 D+b1 E >= kappa D,
    I(D,E)-I0 >= 2kappa D >= 10D.                        (9)

The nonnegative remaining term is the original Gram quadratic, not
a discarded source contribution. Equations(8)--(9) prove the exact
global minimum and a strict cost for every D>0 on this source face.
The full preregistered candidate search is retained: the upper-boundary
cubic had no root in(0,1), and the other stationary/endpoint candidates
failed the full KKT conditions. No candidate class was omitted because
the winner happened to be simple.

The original observed improvement is greater than8.39 over the diagonal
geodesic, greater than4.97 over w=s^2, and greater than2.22 over the
previously fixed best joint quadratic schedule(1,0,-1). These are
absolute energies in this fixed source normalization; they are not
large-horizon principal-moment bounds. The fixed rational recovery
returns the exact point(0,0), and all63 original coefficients of its
monotone path were independently integrated.

## 4. Preregistered scope and comparison controls

SYNCHRONIZED_FACE_MINIMIZER_PREREGISTRATION.md fixes the source, all
candidate classes, the512-bit outward arithmetic, root width2^-64,
depth80 and1024-node limits before computation. An uncertified sign
or exhausted limit is retained as a failed certificate; it does not
change the source or search domain.

The comparisons are the true diagonal geodesic(D,E)=(1/2,1/3), the
actual w=s^2 path(D,E)=(1/3,1/4), and the previously fixed joint
quadratic schedule(a,b,c)=(1,0,-1). The last path need not lie in the
synchronized face. Every comparison sign is retained.

The exact source freeze and final replay are recorded by the accompanying
certificate. This is only the global minimum on(1). It is not an
all-path minimum, a principal-family estimate, or a decoder for the
full retained gamma source.
