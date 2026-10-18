# A bounded zero strip still cannot complete the quadratic mediator

Status: **PROPOSED complete native analytic theorem.** This extends the
Gaussian-mediated weak-closure obstruction to bounded, rather than
exactly real, auxiliary zeros. It also permits a nonnegative quartic
onsite term. It rules out a specified cofinal transfer architecture for
the actual theta law; it does not rule out arbitrary strip models,
arbitrary ferromagnetic spin observables or RH.

## 1. Exact statement

For each N let Y_N be a symmetric bounded-support random variable. Its
characteristic function is entire, and assume that all its zeros lie in

    |Im z|<=epsilon,                                (1)

where epsilon is one fixed finite constant, independent of N. The
supports and variances need not be bounded. Write M_N(x)=E exp(xY_N).
Let d_N>=0, and choose real a_N so that the density

    p_N(x)=Z_N^(-1) exp(-d_N x^4-a_N x^2) M_N(x)    (2)

is integrable. In particular a_N>0 suffices when d_N=0.

**Theorem.** If the laws(2) converge weakly to a law with positive
continuous even density p on R, then for some finite constants C,L,

    -log[p(x)/p(L)]<=C(1+x^2+x^4),        x>=L.      (3)

The actual theta density is not such a limit, since its left side grows
as pi exp(2x). The conclusion requires no prior bound on a_N,d_N,
support, graph size, moment order or the auxiliary variance.

The zero-strip hypothesis is an assumption on the AUXILIARY law Y_N,
not a claim already proved for the actual target. The weak-limit proof
below derives the needed resource from local density ratios; it does
not transfer tail bounds by weak convergence alone.

## 2. Fixed rescaling and the exact quartet product

Changing variables x=L y for `L=10max(epsilon,1)` replaces the auxiliary
MGF by M_N(Ly), whose zeros have real parts bounded by1/10. Proving a
quartic envelope in y proves (3). Thus assume henceforth that every MGF
zero zeta satisfies

    |Re zeta|<=1/10.                                (4)

No MGF zero is real, because M_N(x)>0 for every real x. Symmetry and
real coefficients group its zeros into quartets
`zeta,-zeta,bar zeta,-bar zeta`, or pure imaginary pairs. Choose one
representative `zeta=beta+i gamma` with beta>=0,gamma>0 for each group
and retain multiplicities. Set r=|zeta| and

    P_zeta(x)=(1-x^2/zeta^2)(1-x^2/bar zeta^2).

For a genuine quartet use weight m=1. For a pure imaginary pair use
m=1/2, so `P_zeta(x)^m=1+x^2/gamma^2` on the real line. Repeated
groups are repeated with multiplicity.

The bounded-support MGF is even and of exponential type. Its paired
order-one Hadamard factorization has no linear exponential by evenness
and no quadratic exponential by the order bound. Therefore, on R,

    M_N(x)=product_zeta P_zeta(x)^m,
    sum_zeta m/r^2<infinity.                        (5)

The positive real square root at a pure imaginary pair is unambiguous.
All logarithmic sums used below converge for each N and fixed x.

## 3. Logconcavity away from the narrow zero strip

Put u=x^2. Apart from an additive constant,

    log P_zeta(sqrt(u))
       =log[(u-zeta^2)(u-bar zeta^2)].

Its second derivative is

    -2 Re[(u-zeta^2)^(-2)].                         (6)

Write `A=u+gamma^2-beta^2` and `B=2beta gamma`. When u>2beta^2,

    A-|B|=u+(gamma-|beta|)^2-2beta^2>0.

It follows that `Re[(A-iB)^(-2)]>0`, so (6) is negative. In particular
log M_N(sqrt(u)) is concave on u>1/50, uniformly for all N.

The log density in (2), as a function of u, is this concave function
minus d_N u^2+a_N u. Since d_N>=0, it too is concave on u>1/50.

The native weighted-restriction argument in sections2--3 of
RANK_ONE_HIERARCHY_OBSTRUCTION.md applies on any compact interval
I inside (1/50,infinity): let U_N=X_N^2, restrict to I, multiply by
sqrt(u) and normalize. These densities are logconcave. Weak convergence
and the anchor/secant compactness proof give locally uniform logarithmic
density ratios. In particular, with

    V_N(x)=d_N x^4+a_N x^2-log M_N(x),

one obtains

    V_N(x)-V_N(y)->-log[p(x)/p(y)],   x,y>=1.        (7)

The harmless fixed rescaling of p is understood. No convergence near
u=0 is required.

## 4. Three ratios bound the whole quartet resource

Define

    G(zeta)=-log P_zeta(3)+(8/3)log P_zeta(2)
                                      -(5/3)log P_zeta(1). (8)

Strict concavity in u at u=1,4,9 gives G(zeta)>0. For pure imaginary
pair weights, use mG. The following uniform comparison holds on (4):

    G(zeta)>=c min(r^(-4),1)                       (9)

for some universal c>0. Here is a complete compactness proof of (9).

* As r->infinity while |beta|<=1/10, the angle tends uniformly to the
  imaginary direction. Expanding the logarithms at the fixed arguments
  1,2,3 gives

      G(zeta)=40 Re(zeta^(-4))+O(r^(-6)),
      r^4G(zeta)->40.

  The error is uniform because the arguments are fixed and r is large.
* As zeta->0, all terms involving log r cancel in (8), and

      G(zeta)->2[(8/3)log4-log9]>0,

  uniformly in the argument of zeta.
* On the remaining compact parameter region the function is continuous
  and strictly positive. This includes gamma=0 by continuity: such real
  points lie in [-1/10,1/10], away from the evaluation points1,2,3, and
  the same strict concavity in u persists. No assertion that a real MGF
  zero actually exists is made.

These three facts prove a positive global lower comparison constant.

The finite difference annihilates the quadratic and constant terms.
Since `3^4-(8/3)2^4+5/3=40`, it gives exactly

    V_N(3)-(8/3)V_N(2)+(5/3)V_N(1)
                       =40d_N+sum_zeta mG(zeta).    (10)

By (7) the left side is bounded. All terms on the right are nonnegative.
Thus for a finite uniform S,

    d_N<=S,
    sum_(r>=1)m r^(-4)<=S,
    sum_(r<1)m<=S.                                 (11)

This handles the possible infinitely many zeros of each finite model
without dropping multiplicities. The finite-difference identity first
holds for partial products and then for the convergent logarithmic
series; positivity permits the resource conclusion.

## 5. Far zeros have a positive quartic remainder

For r>=1 write

    P_zeta(x)=1+A_zeta x^2+B_zeta x^4,
    A_zeta=2(gamma^2-beta^2)/r^4,
    B_zeta=r^(-4).

By |beta|<=1/10 and r>=1,

    1.96/r^2<=A_zeta<=2/r^2,
    A_zeta^2>=2B_zeta.                             (12)

Set

    q_zeta(x)=A_zeta x^2-log P_zeta(x).

As a function of v=x^2 its derivative is

    [(A_zeta^2-2B_zeta)v+A_zeta B_zeta v^2]
                           /[1+A_zeta v+B_zeta v^2]>=0.

Therefore q_zeta(x)>=0 and it increases with x>=0. Also
`P_zeta(x)>=1+A_zeta x^2`, so

    q_zeta(x)<=A_zeta x^2-log(1+A_zeta x^2)
              <=A_zeta^2 x^4/2<=2r^(-4)x^4.        (13)

These statements also cover pure imaginary pairs with weight1/2.

## 6. Near-zero factors have the favorable tail sign

For r<1 and x>=1, the derivative of P_zeta in v=x^2 has the sign of

    v+gamma^2-beta^2>0.

Thus `P_zeta(x)/P_zeta(1)>=1`. Such factors only LOWER the potential
difference V_N(x)-V_N(1). At the anchor x=2 their cost is bounded:

    P_zeta(2)/P_zeta(1)
      =|(4-zeta^2)/(1-zeta^2)|^2
      <=[5/(1-1/100)]^2.

Consequently `0<=log[P_zeta(2)/P_zeta(1)]<=C_0` for a fixed C_0.
By (11) their total weighted anchor cost is bounded. Individual near
zeros are allowed to approach0; a lower zero-radius bound is not used.

## 7. The global envelope follows from the local anchors

For each N set

    c_N=a_N-sum_(r>=1)m A_zeta.

This is finite for each N by the order-one summability in (5). The exact
potential difference is

    V_N(x)-V_N(1)=d_N(x^4-1)+c_N(x^2-1)
       +sum_(r>=1)m[q_zeta(x)-q_zeta(1)]
       -sum_(r<1)m log[P_zeta(x)/P_zeta(1)].         (14)

Evaluate at x=2. Equations(7), (11), (13) and section6 bound every term
other than 3c_N uniformly; hence |c_N|<=C_1. For any x>=1 the final
sum in (14) is nonpositive, and the far sum is at most2Sx^4.
Therefore

    V_N(x)-V_N(1)<=C_1(x^2-1)+3Sx^4.               (15)

The constants were fixed at the three points1,2,3. Passing to (7) for
each x gives a uniform quartic envelope. Undo the fixed rescaling from
section2 to prove(3).

## 8. Consequence for controlled-field Gaussian transfers

Consider a finite auxiliary Ising graph with positive interactions,
real fields h_i, positive b_i, and assume its b-weighted observable is
symmetric, for example by a graph involution preserving b and reversing
h. Suppose the observed Gaussian-mediated coordinate has joint density

    exp[-a_N x^2+x sum_i b_i sigma_i
                     +sum J_ij sigma_i sigma_j+sum h_i sigma_i],
    a_N>0,

and the desired observable-field budget is

    |h_i|<=b_target b_i/(2a_N),                     (16)

for one fixed finite target band. The already established positive-edge
strip theorem gives the auxiliary MGF zero bound

    |Re zeta|<=b_target/(2a_N).                     (17)

Weak convergence of these Gaussian-coordinate marginals to ANY
probability law forces a_N to be bounded away from0 eventually. To see
this, integrate out x. The resulting marginal is an independent
Gaussian of variance1/(2a_N) plus the appropriately tilted auxiliary
spin observable. Consequently its characteristic function has modulus
at most exp[-t^2/(4a_N)]. A subsequence a_N->0 would make the limit
zero at every fixed t!=0, contradicting continuity at0 of a limiting
characteristic function. This argument does not require symmetric fields.

Thus (17) is uniformly bounded along any weakly convergent sequence.
The theorem applies and excludes the actual theta density. This covers
arbitrary positive auxiliary graphs and controlled symmetric real fields;
allowing a_N->infinity does not escape it.

The conclusion concerns the Gaussian-coordinate transfer construction,
whose observed law has the exact density(2). It does not exclude direct
spin observables from the wider correlated-field strip class, nor
nonquadratic growing-degree transfer energies. The actual cofinal
construction in those surviving classes remains open.
