# A source support certificate for an actual all-path minimizer

This is the exact criterion for the next discovery stage, not a claim
that its hypotheses have already been met. Use the original H25 source
and original physical Gram frozen in affine discovery
`46c8453e3976d242479202bf4d58489282a64d2a`. Write

    x=(A,B,C/2,D,E,F),
    I(x)=c0+2g.x+x^t G x.                              (1)

All six coordinates are the actual Stieltjes occupation integrals.
The matrix G is strictly positive definite in this physical source
chart. No new inner product, atom diagonal or gamma decoder is used.

## 1. A global criterion, not just stationarity on a chosen family

Let x* be realized by one continuous monotone source path, and set
L=g+Gx*. Define the literal linear functional

    ell(x)=aA+bB+cC+dD+eE+fF,
    (a,b,c,d,e,f)=(L0,L1,L2/2,L3,L4,L5).                (2)

If ell is minimized among ALL actual source paths at x*, then

    I(x)-I(x*)=2(ell(x)-ell(x*))
                  +(x-x*)^t G (x-x*) >= 0.             (3)

Strict positivity of G makes x* the unique minimizing observed source
vector. This does not assert a unique parametrization or a unique
source path. Conversely, checking stationarity only within a two- or
three-parameter path template is insufficient for (3).

The exact linear-support reduction in
`NATIVE_OCCUPATION_SUPPORT_REDUCTION.md` supplies the full-support
obligation when a simple sufficient cone below is unavailable.
Its positive-c fixed-mark replay is not itself a global support solver.

## 2. A sufficient cone forcing the last activation to occur last

Every actual path has D>=0, F>=0 and D/2<=E<=D. The lower E bound
is the monotone covariance inequality for u and w; the upper follows
from u<=1. Therefore

    dD+eE+fF >= (d+min(e/2,e))D+fF.                    (4)

If f>=0 and d+min(e/2,e)>=0, this part of the linear objective
is minimized by taking w=0 until the planar path reaches (u,v)=(1,1),
then increasing w to1. It has D=E=F=0. Equation (4) applies to every
competing three-coordinate path, including simultaneous activations.
It is a sufficient condition; failure of this cone is not a proof
that the candidate fails the full-support test.

## 3. The self-consistent planar profile

On that last-activation path, the remaining support problem is

    minimize integral_0^1 [c v(u)^2+(a+bu)v(u)] du       (5)

over nondecreasing v in[0,1]. Vertical endpoint segments are allowed
and contribute zero to (5). If c>0 and b<=0, its unique du-almost
everywhere minimizer is

    v(u)=clip(lambda+mu u,0,1),
    lambda=-a/(2c), mu=-b/(2c).                         (6)

For b>0 the isotonic minimizer is the constant
clip(-(a+b/2)/(2c),0,1), with vertical endpoint completion.
Both statements concern an actual monotone path. For (6), write
u0=max(0,-lambda/mu), u1=min(1,(1-lambda)/mu) in a nonempty
sloping regime with mu>0 and 0<=u0<u1<=1. The source moments are the elementary integrals

    A=integral_(u0)^(u1)(lambda+mu u)du+1-u1,
    B=integral_(u0)^(u1)u(lambda+mu u)du+(1-u1^2)/2,
    C=integral_(u0)^(u1)(lambda+mu u)^2du+1-u1.          (7)

The clipping breakpoints and constant regimes must be checked rather
than inferred from an unconstrained stationary point. In particular,
for an entirely unsaturated affine segment,

    A=lambda+mu/2,
    B=lambda/2+mu/3,
    C=lambda^2+lambda mu+mu^2/3.                         (8)

A candidate satisfies self-consistency only if the coefficients in
(2), evaluated at these SAME moments, satisfy (6). In the unsaturated
regime the two equations are

    L2 lambda+L0=0,   L2 mu+L1=0.                       (9)

These are coupled equations in the original physical metric, not a
fit to independent coefficient observations. Exact or interval-certified
solutions of (9), the actual clipping inequalities, c>0 and the full
cone in (4) together prove global optimality by (3). A root found
outside the declared regime is retained as a failed candidate.

## 4. Discovery and failure conditions

The complete N=2,3 calibration and frozen N=4 grid supply actual
source evidence before choosing a continuous candidate family.
The next calculation must retain the full original G,g,c0, record
any clipping or support-cone failure, and independently integrate a
rational nearby path through all63 source records. A candidate that
only improves the grid upper bound is an upper-bound result, not an
all-path theorem. A small stationarity residual without a certified
support inequality does not meet (3). If the simple cone fails, the
remaining question is the full signed support minimum over the
two marked activation coordinates, not another canonical positive
coefficient example.

All claims here have fixed H25 source scope. The known H60 failure
of synchronization descent prevents silently transporting this
finite-chart criterion to every physical horizon.
