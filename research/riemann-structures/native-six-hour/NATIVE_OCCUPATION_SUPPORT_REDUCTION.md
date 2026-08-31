# Exact support reduction for the original H25 occupation body

Status: theorem and finite oracle reduction, before a new numerical panel.
The source is the actual primes2,3,5 / physical-product25 current with
all63 ordered records. Keep the occupation identities of
`NATIVE_OCCUPATION_MOMENTS.md` and the original physical metric in
`NATIVE_AFFINE_PHYSICAL_FLOOR.md` at
`46c8453e3976d242479202bf4d58489282a64d2a`. No full retained-gamma or
all-height assertion is introduced.

An admissible path is a continuous coordinatewise nondecreasing path
(u,v,w) from(0,0,0) to(1,1,1), with Stieltjes integration; piecewise
smooth paths and coordinatewise vertical segments are allowed. Every
path constructed below has finitely many smooth/vertical pieces and can
be reparameterized Lipschitzly. Define

    A=integral v du, B=integral uv du, C=integral v^2 du,
    D=integral w du, E=integral uw du, F=integral w dv.

For arbitrary real a,b,c,d,e,f, let

    ell=aA+bB+cC+dD+eE+fF.                                    (1)

The conclusions concern the minimum of this linear functional over actual
paths, equivalently over the convex hull of their occupation vectors.

## 1. One activation of w is exact, not a restricted-path conjecture

**Theorem SUPPORT.ONE_ACTIVATION.** The minimum in (1) is attained by a
path on which w increases from0 to1 in one vertical segment, at a point
(s,t) of its planar (u,v) path. Its value is

    min_(0<=s,t<=1) [ J(0,s;0,t)+J(s,1;t,1)
          +d(1-s)+e(1-s^2)/2+f(1-t) ],                       (2)

where J(L,R;alpha,beta) minimizes
`integral_L^R [c v(u)^2+(a+b u)v(u)]du` over nondecreasing functions
with values in[alpha,beta]. Endpoint values may be completed by vertical
segments; they are not imposed as spurious pointwise endpoint conditions.

**Proof.** Fix a planar path. Put Q(u,v)=d u+e u^2/2+f v.
Stieltjes integration by parts for continuous bounded-variation functions
gives the w-dependent cost as

    integral w dQ = d+e/2+f - integral Q dw.

The positive measure dw has total mass1. Its average of Q is at most the
maximum of Q along this compact planar path. Insert a vertical w-segment
at a maximizing point, leaving u,v fixed there; this realizes that bound
exactly without changing the planar cost. Equivalently, the layer-cake
decomposition of w averages the costs of these single activations.

For a marked planar point(s,t), represent the path as a nondecreasing
graph v(u), ignoring the values at vertical segments in the du integral.
On u<s it takes values in[0,t], and on u>s in[t,1]. Conversely any two
such nondecreasing graphs can be joined through(s,t) by vertical pieces,
and completed to the prescribed endpoints. Their costs minimize
independently, proving (2). The explicit optimizers below have finitely
many pieces. Their minimum costs are continuous on the compact square
(s,t) in[0,1]^2, including the zero-length intervals. This follows also
by the displayed formulas, or by clamping bounds and estimating the
bounded integrand on the small changed interval. Hence (2) has a minimizer,
and the construction makes it an actual admissible path. QED.

## 2. The planar isotonic minimizations are explicit

Write h(u)=a+b u. If L=R, set J=0. If alpha=beta, the only relevant
value is the constant alpha. Otherwise the following formulas apply.

For c>0 and b<=0, the exact optimizer is

    v(u)=clip_[alpha,beta] (-(a+b u)/(2c)).                    (3)

The unclipped target is nondecreasing, so its pointwise quadratic minimum
is admissible. For c>0 and b>0, the exact optimizer is the constant

    v(u)=clip_[alpha,beta] (-(a+b(L+R)/2)/(2c)).               (4)

To prove (4), let m be the average of any admissible v and mid=(L+R)/2.
Subtracting its constant-m cost leaves

    c integral(v-m)^2 du + b integral(u-mid)(v-m)du >=0.

The covariance is nonnegative for nondecreasing v: its value is
`[2(R-L)]^-1 integral integral (u-r)(v(u)-v(r))du dr`.
Minimize the remaining constant quadratic over m in[alpha,beta].
For b=0, (3) and (4) coincide.

These formulas need only polynomial integration. On a constant segment
v=z a primitive is `(c z^2+a z)u+b z u^2/2`; on an unsaturated segment
v=-h/(2c), a primitive is
`-(a^2u+a b u^2+b^2u^3/3)/(4c)`.
The clipping breakpoints are the intersections of that affine target
with alpha and beta, retaining zero-length and endpoint cases.

For c<=0, an optimizer of J takes only the two endpoint values: alpha
before one threshold r in[L,R], and beta after it. Indeed the concave
quadratic lies above its chord between alpha and beta. Writing
v=alpha+(beta-alpha)theta, the chord cost is linear in a nondecreasing
theta in[0,1]; its layer cake is an average of single-threshold costs.
Some threshold is therefore no worse, and endpoint values attain equality
with the original quadratic. The threshold cost is

    integral_L^r [c alpha^2+h(u)alpha]du
       +integral_r^R [c beta^2+h(u)beta]du.                   (5)

It is a quadratic in r. Evaluate L,R and, when b!=0 and it lies in the
interval, r=-(a+c(alpha+beta))/b. This covers minima and degeneracies
without presuming a favorable coefficient sign.

For c>0, substituting (3)--(4) in (2) produces an explicit continuous
piecewise polynomial of degree at most3 on a finite polygonal partition
of the(s,t) square. For rational coefficients its pieces and partition
are rational: switching conditions are affine. Thus the support problem
has an exact two-dimensional real-algebraic oracle formulation. A solver
must retain boundary strata, degenerate critical loci and exact root
isolation; no unexecuted numerical optimization is claimed here.

## 3. When c<=0, both v and w activate once

For fixed s and the two thresholds from (5), the cost is a concave
quadratic in the marked value t. The only t^2 coefficient is c times
the length of the plateau where v=t, hence is nonpositive; the w-term
is affine in t. Therefore t can be replaced by0 or1 without increasing
the cost. The resulting v has a single activation, at u=r.

Put

    Q(s,r)=(a+c)(1-r)+b(1-r^2)/2
                         +d(1-s)+e(1-s^2)/2.

The exact support minimum is consequently

    min { min_(0<=s<=r<=1) [Q(s,r)+f],
          min_(0<=r<=s<=1) Q(s,r) }.                         (6)

The first triangle activates w before v; the second activates v before w.
At s=r both orders are retained: the vertical segments can be traversed
in either order, and their F values are1 and0 respectively. Identifying
the orders at that boundary would lose a real source distinction.

Each objective in (6) is quadratic. Its exact minimum is obtained from
the triangle vertices, stationary points on each edge and interior
stationary points, retaining any flat critical case. If a stationary
set is not isolated, a boundary point of that set has the same value;
one must not divide by a zero Hessian coefficient. Thus rational inputs
in this regime admit finite rational candidate comparisons. This is a
support-functional statement, not a claim that every source moment or
every quadratic-energy optimizer is a two-activation path.

## 4. Certified original-metric lower bounds and their limitation

Use x=(A,B,C/2,D,E,F) and the exact physical Gram form
`E(x)=c0+2g^T x+x^T Gx`, with G positive definite. For any fixed trial y,

    E(x)>=c0-y^T G y+2(g+G y)^T x.                           (7)

If lambda=2(g+G y), the linear support coefficients in (1) are
`(lambda1,lambda2,lambda3/2,lambda4,lambda5,lambda6)`.
The factor1/2 in the C coefficient is mandatory. Inserting the exact
minimum (2), or (6) when applicable, yields a certified lower bound for
every original source path. Certified interval versions may enclose the
same expression without replacing the original metric.

All linear support functionals determine the convex hull of the source
body. A minimizer of the convex quadratic on that hull need not itself
be the moment vector of one actual path. The support oracle alone does
not close that gap or identify the all-path energy optimum. This work
does not replace the separate synchronized-family optimizer, alter its
parameter restrictions or imply any all-height capture theorem.
