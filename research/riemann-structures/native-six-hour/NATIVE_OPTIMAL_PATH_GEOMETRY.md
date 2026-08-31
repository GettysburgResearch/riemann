# Original-energy stability of the optimal path image

This is a proof-only consequence of the strict full-source certificate,
not a new numerical acquisition. The H450 source and original-kernel
calculation are frozen at a4f6ea24a703d183e569d4257ed8d7e867089b86;
the unchanged executable was calibrated at530ab2d0ee328c4902b102a693941ab49c860949.
The argument also applies to any separately certified horizon satisfying
the hypotheses below. It does not assert an infinite-horizon optimizer
or identify the full retained-gamma source.

The earlier NATIVE_OPTIMUM_STABILITY.md at
b58909695c2feb6cc74af7d4b3b41089b41c4871, blob
e70a9158744227ad7b5daff253fd4b1d39464990, already proves source-derived
Jacobian nondegeneracy, local coefficient stability, coercivity and an
interior planar graph estimate. Those results are not reproved here.
The contribution below uses both endpoint clips to cover the entire
three-dimensional path image in both Hausdorff directions, and proves
that the one-third exponent for energy-to-image recovery is sharp.

## Hypotheses and the actual geometric distance

Let gamma be any continuous coordinatewise monotone path from000 to111.
Write its coordinates as u,v,w and let

    f(u)=clip(lambda+mu*u,0,1),  mu>0,  f(0)=0, f(1)=1.

Both endpoint clips are essential to the following form of the estimate.
The certified H450 root has these strict properties. The optimal image is
the completed monotone graph

    G = {(u,f(u),0):0<=u<=1} union {(1,1,w):0<=w<=1}.

Distance between images means the two-sided Hausdorff distance for the
ordinary maximum-coordinate metric on the cube. It is independent of
pauses or of the chosen continuous parametrization. In particular it is
not a distance between parameter functions at artificially matched times.

The strict supporting-functional certificate supplies c>0 and delta>0
such that, in the original physical observation and measure,

    Delta E := E(gamma)-E_* >= 2c I + 2delta J + ||F_gamma-F_*||_nu^2,
    I = integral_gamma |v-f(u)|^2 du,
    J = integral_gamma w(du+dv).                              (1)

Here delta can be any positive lower bound for all eight certified
quadratic minima. These constants include the actual current2ds,
physical square-root weights and complete ratio collection; no source
norm replaces the observed energy.

## A monotone graph estimate

At a path point suppose v-f(u)=h>0. For the subsequent u-values from
u to u+h/mu, monotonicity of v and the mu-Lipschitz property of f give

    v(u+s)-f(u+s) >= h-mu*s,  0<=s<=h/mu.

This interval is available: f(1)=1 and v<=1 imply
h<=1-f(u)<=mu(1-u). Integrating its square against du gives

    I >= integral_0^(h/mu) (h-mu*s)^2 ds = h^3/(3mu).

If f(u)-v=h>0, use the preceding u-interval and f(0)=0 instead.
The argument applies to every point of a vertical path segment as well:
monotonicity propagates its discrepancy into preceding or subsequent
positive u-length. Thus

    eta := sup_gamma |v-f(u)| <= (3mu I)^(1/3).                (2)

There is no assumption that v is a single-valued function of u.

## Both directions of Hausdorff approximation

At every path point (u,v,w), the remaining coordinate increments imply

    J >= w[(1-u)+(1-v)].                                     (3)

The graph point(u,f(u),0) is at distance at most max(eta,w), while the
point(1,1,w) on the endpoint segment is at distance
max(1-u,1-v). The smaller of these two bounds is at most
max(eta,sqrt(J)), by (3). This proves approximation of every actual
path point by G.

For the reverse direction, first assume0<J<1 and set epsilon=sqrt(J).
Choose a path point p0=(u0,v0,epsilon), which exists by continuity of w.
Equation(3) gives1-u0<=epsilon and1-v0<=epsilon.

Every graph point(u,f(u),0) with u<=u0 is approximated by a preceding
actual point having that u, with errors at most eta in v and epsilon
in w. For u>=u0, use p0: its u error is at most epsilon, its w error
is epsilon, and both v0 and f(u) lie within max(1,mu)epsilon of1.
Finally, an endpoint-segment point with w>=epsilon has a following
actual point of that w, whose two other coordinates are within epsilon
of1. A point with w<=epsilon is within epsilon of p0.

If J=0, w can only increase after u=v=1 and the same argument uses
eta alone. If J>=1, the cube has diameter1 in this metric and the
following bound is automatic. Hence

    d_Hausdorff,infinity(image(gamma),G)
      <= max((3mu I)^(1/3), max(1,mu)*sqrt(J))
      <= max((3mu*Delta E/(2c))^(1/3),
             max(1,mu)*sqrt(Delta E/(2delta))).                (4)

This proves quantitative stability of the actual oriented path image
under the original energy. Rational upper and lower endpoints for
mu,c,delta may be substituted directly to obtain numerical certified
constants. No additional computation is needed for the implication.

## The one-third exponent is sharp

Choose u0 strictly inside the affine band, put v0=f(u0), and take h>0
small enough that u0+h/mu remains in that band. Follow the optimal path
until(u0,v0,0), move vertically to(u0,v0+h,0), move horizontally to
(u0+h/mu,v0+h,0), then follow the original graph and activate w last.
This is an admissible continuous monotone path. It has J=0 and

    I = h^3/(3mu).                                           (5)

Its changes in the three actual last-activation coordinates
x=(A,B,C/2) are exactly

    Delta A   = h^2/(2mu),
    Delta B   = u0*h^2/(2mu)+h^3/(6mu^2),
    Delta C/2 = v0*h^2/(2mu)+h^3/(3mu).                       (6)

The full source field on this subclass is affine in x. If G_plane is
its original physical Gram matrix, self-consistency of the supporting
gradient gives the exact energy identity

    Delta E = 2c*h^3/(3mu) + Delta x^t G_plane Delta x
            = 2c*h^3/(3mu)+O(h^4).                           (7)

The Gram term is nonnegative and uses the original observation; it is
not an omitted approximation. Formula(6) proves its O(h^4) upper bound
for the fixed source, without an assumption about diagonal orthogonality.

The detour point(u0,v0+h,0) is at maximum-coordinate distance
h/(1+mu) from the original affine graph. For sufficiently small h,
the other graph pieces and the endpoint w-segment are farther away.
Thus its image distance is bounded below by h/(1+mu) and above by h,
while its energy excess has order h^3. No uniform local estimate
d_Hausdorff<=C(Delta E)^alpha can therefore hold with alpha>1/3.

The sharpness concerns path-image recovery from this actual energy
minimum. It does not promote finite-horizon coefficients to the full
native family, change the observation kernel, or claim parametrization
uniqueness.
