# Exact literal curvature dimension for several schedule groups

This is an elementary source theorem, before any new multi-group atlas
acquisition. It generalizes the two-group calculation in
`GROUPED_NATIVE_CURVATURE_ENRICHMENT.md`. No new general theory of
polynomial differential forms is claimed. The source is the native
half-divisor geodesic in L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`; the earlier literal curvature
and occupation conventions are frozen at
`6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537` and
`a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc`.

Fix r disjoint nonempty groups of distinct primes, with group sizes
p_1,...,p_r. Every prime in group i uses the same schedule u_i. All
arithmetic indices in this note are supported on these chosen primes.
Work over Q, with continuous monotone paths from 0 to 1 in the unit
r-cube, and the original polarized current with its factor2.

## 1. Actual source and multidegree curvature spaces

The local native half-source factor is

    u_i sqrt(1-x_l)+(1-u_i)sqrt(1-x_l^2).

Its coefficient at every prime power is affine in u_i. Hence all supported
coefficients lambda_n lie in

    V = tensor_i P_(p_i)(u_i)
      = span{u^a: 0<=a_i<=p_i}.

Conversely a squarefree n choosing a_i primes in group i has
lambda_n=(-1/2)^(sum a_i)u^a. These coefficients span V exactly. Higher
prime powers therefore cannot enlarge this source function space.

For an ordered supported pair use

    alpha_(n,m)=2 lambda_m d(lambda_n),
    C_(n,m)=2 d(lambda_n) wedge d(lambda_m)=-d(alpha_(n,m)).

The nonzero scalar factors do not affect the Q-linear curvature span. It is
therefore the span W of df wedge dg for f,g in V, derived from actual source
coefficients rather than assumed polynomial observations.

Give du_i multidegree e_i, so that differentiation preserves multidegree.
Fix d with 0<=d_i<=2p_i. For monomials f=u^a,g=u^b with a+b=d,

    df wedge dg
      =sum_(i<j) (a_i d_j-a_j d_i)
                    u^(d-e_i-e_j) du_i wedge du_j.      (1)

Any term with a formally negative exponent has zero coefficient and is
omitted. Thus its coefficient array is identified with a wedge d. The
admissible integer splits are precisely

    max(0,d_i-p_i)<=a_i<=min(p_i,d_i).                   (2)

Write m(d) for the number of coordinates with 0<d_i<2p_i, and k(d) for
the number with d_i=2p_i. Then

    dim W_d = m(d),       if k(d)>0;
              m(d)-1,    if k(d)=0 and m(d)>0;
              0,         otherwise.                   (3)

To prove this, let E_d be the coordinate span of e_i for the m(d) partial
coordinates. Each such interval in(2) contains consecutive integers;
the remaining coordinates of a are fixed at d_i/2. Also a and d-a are
both admissible, so the midpoint d/2 belongs to their affine span.
Consequently the affine span of all admissible a is d/2+E_d, and

    span{a wedge d}=image[E_d -> wedge^2 Q^r,
                          v -> v wedge d].             (4)

For nonzero d the kernel of this map is E_d intersect Qd. If k(d)>0,
d has a nonzero coordinate outside E_d, so the kernel is zero. If there
are only partial and zero coordinates and at least one partial coordinate,
d belongs to E_d and the kernel is one-dimensional. The remaining cases
give zero. This proves(3), including the all-saturated corner and d=0.

## 2. Closed formula and comparisons

Different multidegrees are linearly independent. Sum(3) over all d.
The sum of m(d) is

    sum_i (2p_i-1) product_(j!=i)(2p_j+1).

The one-dimensional kernel must be subtracted exactly for the nonzero
degrees with no saturated coordinate. There are product_i(2p_i)-1 such
degrees. Therefore

    dim W = sum_i (2p_i-1) product_(j!=i)(2p_j+1)
                         - product_i(2p_i) + 1.        (5)

For a single group this gives zero, as all one-variable one-forms are
exact. For two groups it gives4pq-1, recovering the single missing-corner
theorem. For three independent single-prime schedules it gives
3*9-8+1=20; for four it gives4*27-16+1=93. These are full literal-source
dimensions, not claims that a previously studied small fixed horizon has
those ranks. In particular the H25 rank6 calculation is not contradicted
by the three-prime full-source dimension20.

Let K be the product of all chosen primes. Each source-basis monomial is
represented by a squarefree index dividing K. All ordered pairs of those
indices occur by product horizon K^2. Hence that squarefree panel already
realizes the entire span in(5); all supported pairs at any larger horizon
remain in the same span. The bound K^2 is sufficient, not a claimed first
rank-saturation horizon or a requirement to enumerate every index below it.

## 3. Literal affine readout and exact endpoint terms

Every omega in W is a closed polynomial two-form. For a homogeneous
component of nonzero total degree |d|, let E=sum_i u_i partial_(u_i) be
the Euler vector field. Cartan's identity gives

    d(i_E omega)=|d| omega,

since d omega=0. Thus tau_omega=-i_E omega/|d| is a polynomial one-form
with -d tau_omega=omega. Choose any homogeneous rational basis
omega_1,...,omega_D of W and define M_l(gamma)=integral_gamma tau_(omega_l).

For every actual source pair, subtract from alpha_(n,m) the combination
of tau_(omega_l) having its curvature. The difference is closed and hence
exact as a polynomial one-form over Q. With fixed endpoints its integral
is constant. Therefore every supported labelled integrated coefficient is

    B_(n,m)(gamma)=b_(n,m)+sum_l c_(n,m;l) M_l(gamma).   (6)

The coefficient matrix has rank D=dim W, already on the squarefree
source-basis panel. Two paths have the same complete literal integrated
source if and only if all D coordinates M_l agree. The underlying quotient
by exact endpoint differentials is intrinsic to the source; choosing a
basis of W merely chooses its affine coordinates.

This is a minimal affine-linear readout dimension. It does not imply
independent attainability of arbitrary coordinates, a nonlinear encoding
lower bound, or a complete retained-gamma decoder.

## 4. Actual monotone rectangles realize the full affine hull

For a coordinate pair i<j, choose an interior rational rectangle in that
coordinate plane, with every other schedule fixed at an interior rational
value. Join its lower corner to0 by a common monotone prefix and its upper
corner to1 by a common monotone suffix. The middle paths traverse j-then-i
and i-then-j. Their actual integrated source difference is the rectangle
integral of C_(n,m), with the sign convention above.

These rectangle functionals span W^*. Indeed, if a polynomial two-form
in W integrates to zero on every such rational coordinate rectangle, take
shrinking rectangles and use continuity and density of the rational
centers. Every coefficient of du_i wedge du_j vanishes on the open cube,
and hence is the zero polynomial. The common annihilator is therefore
zero. Since W is finite-dimensional, D rational rectangles can be selected
whose restrictions are independent. This proves that differences of
actual monotone source paths span all D literal variation directions.

Conversely any two fixed-endpoint paths differ only through the D affine
coordinates in(6). Thus their literal source family has affine hull of
dimension exactly D. This is a linear-span statement: it does not assert
that all points in that hull, or all combinations of rectangle differences,
are individually attainable by one monotone path.

## 5. Physical prefixes and the fixed-horizon boundary

The previous joint-prefix argument remains valid with any number of groups.
For one fixed labelled path, retain the actual fields

    F_H(t)=sum_(nm<=H) B_(n,m)/sqrt(nm) exp(it log(n/m)).

At a reduced supported ratio a/b, the coefficient is

    z_H(a/b)=1/sqrt(ab) sum_(d^2 ab<=H) B_(da,db)/d.

The jump from H=d^2 ab-1 to H=d^2 ab recovers precisely
B_(da,db)/(d sqrt(ab)). Distinct finite frequencies are independent in
the original nonzero observation measure, as proved in the frozen native
curvature source. Consequently the finite collection of full physical
fields with1<=H<=K^2 recovers the squarefree source-basis panel and jointly
separates all D directions in(5).

This does not determine the rank at one fixed H. Ratio coalescence may
still lose directions there, and retaining only energies is a different
observation. The path must be the same at every prefix. No uniform
conditioning, arbitrary-mask equivalence or all-height gamma identification
is inferred. A new exact horizon/coalescence atlas requires its own bounded
declaration and acquisition; the counts20 and93 above are theorem
predictions before that separate execution.
