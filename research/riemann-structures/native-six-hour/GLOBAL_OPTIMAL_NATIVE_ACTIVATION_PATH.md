# The globally optimal activation path for the complete H25 source

The fixed sixteen-start experiment frozen at
`a10385170ae8d1555299b6e1ed981e44c5d1c6e5` certifies a global
minimum over ALL continuous monotone activation paths for the original
H25 primitive source on primes2,3,5. It retains every one of the63
ordered factor records, all45 physical ratios, the native2ds measure,
the physical1/sqrt(nm) factors and the original Mellin measure.
This is not a claim about the unresolved full retained-gamma source
or about arbitrary physical horizons.

## 1. The actual minimizing path

There are certified parameters, approximately

    lambda=-0.26752438274590645,
    mu=1.2067025166647434,
    u0=-lambda/mu=0.22169870291256905.                   (1)

The oriented path is

    (0,0,0) -> (u0,0,0)
              -> (1,lambda+mu,0) -> (1,1,0) -> (1,1,1). (2)

The middle segment has v=lambda+mu*u; the first segment is its
lower clipping at v=0. Its endpoint lambda+mu is strictly below1.
The final two segments complete v and then activate w. The original
physical energy is approximately

    157.46733527260562.                                 (3)

The certificate supplies rational enclosing boxes and intervals;
the decimal digits in(1)-(3) describe their midpoints. The complete
heldout N=4 grid minimum is about157.49597972322044 and the previously
optimized synchronized face has minimum about158.333344517. Neither
comparison is used to prove global optimality.

All sixteen declared floating starts produced a candidate that passed
the SAME independent rational certificate. Floating Newton iterations
only propose centers. Each center is treated as an exact binary
rational and surrounded by the predeclared radius2^-30 box. The
original source coefficients are enclosed on a2^-512 lattice.

## 2. Existence is certified before optimality is asserted

Let x=(A,B,C/2,0,0,0) be the exact moments of the clipped graph and
L=g+Gx in the original physical Gram. The equations are

    L2*lambda+L0=0,   L2*mu+L1=0.                       (4)

In each accepted box mu>0, lambda<0 and lambda+mu<1 hold strictly.
Thus the moments and(4) are differentiable rational functions there.
Their moving-boundary derivatives retain the cancellation at the
clipping point; no endpoint term is discarded without that identity.

The verifier constructs an invertible rational preconditioner R and
bounds the derivative of T(z)=z-R F(z) throughout the entire box.
Its row-sum norm is strictly less than1, and the Krawczyk enclosure
of T(box) lies strictly inside the box. These two checked inequalities
prove existence and uniqueness of a root in that box by contraction.
The center and actual box endpoints are required to lie exactly on
the declared outward lattice, so its radius is not understated.

Each center additionally gives a nearby rational actual path. Direct
integration of all63 original2ds records agrees with the moment
formula, and coalescing all45 ratios reproduces the complete original
energy. For this lower-clipped regime, an independent formula uses
t=-lambda/mu and h=1-t:

    A=mu*h^2/2, B=mu*h^2*(t+2)/6, C/2=mu^2*h^3/6.       (5)

This explicitly keeps the C/2 normalization in the physical chart.

## 3. A full-source support certificate proves the global minimum

The half-gradient linear functional on actual occupation moments is

    ell=aA+bB+cC+dD+eE+fF,
    (a,b,c,d,e,f)=(L0,L1,L2/2,L3,L4,L5).                 (6)

The root boxes certify, conservatively,

    c>3/2, f>5/2, d+e/2>2, d+e>2.                      (7)

For every competing monotone source path, D,F>=0 and D/2<=E<=D.
Therefore its last three support terms are at least2D+(5/2)F.
Taking w last makes D=E=F=0. In the remaining planar problem,
(4) makes v*=clip(lambda+mu*u,0,1) the pointwise minimizer of
c v^2+(a+bu)v. It is itself monotone, so it is also the global
planar support minimizer. This comparison covers every actual path,
not just the fitted two-parameter family.

The exact physical energy identity gives

    I(x)-I(x*)=2[ell(x)-ell(x*)]+(x-x*)^t G(x-x*).       (8)

Consequently (2) is globally minimizing. More quantitatively, writing
v(u) for a competing path's monotone graph representative, the
pointwise projection inequality and(7) give

    I(path)-I(*) >= 3 integral_0^1 |v(u)-v*(u)|^2 du
                     +4D+5F+||F_path-F_*||^2_L2(nu).    (9)

Vertical planar segments have zero du measure in this formula.
The final norm is the original complete observed source norm,
since its square is exactly the last term of(8).

## 4. Uniqueness of the oriented source path

Equality in(9) forces D=F=0. If w became positive before u=v=1,
a later positive u or v increment would contribute positively to D
or F. Thus w can increase only after both other coordinates finish.
Strict planar convexity forces v=v* du-almost everywhere. The target
clipped graph is continuous. Monotonicity makes any off-graph point
at an interior u, or any nontrivial interior vertical jump, force
disagreement on an interval of positive u length. Such deviations
are impossible. The endpoint vertical segment from lambda+mu to1
is forced, and then w must rise from0 to1.

Hence (2) is the unique oriented path image. Arbitrary pauses and
nondecreasing reparameterizations are allowed; uniqueness modulo
strictly increasing homeomorphisms is not claimed for paths with
different pauses. Strict positivity of G also separately gives
uniqueness of the observed source vector.

## 5. Validation and limits

The coordinator executed all16 starts and all rational root/support
certificates successfully, with full literal source replay. The final
producer passed ordinary write/check, and all14 dedicated tests passed
in both ordinary and optimized modes. Two optimized-producer attempts
were stopped by the RAM reserve guard before completion; they are not
reported as mathematical failures or as completed checks. Final
note-bound write/check/optimized-check is pending available memory and
will be recorded in the freeze handoff. Independent static review
caught and repaired the actual-box radius guard before the discovery
run. No scientific job was run by the author.

This source selection result does not give a principal-moment bound
for the full retained-label source, an atom-diagonal isometry, or
an all-height synchronization map. Those are separate interfaces;
in particular the known H60 synchronization-fiber obstruction remains.
