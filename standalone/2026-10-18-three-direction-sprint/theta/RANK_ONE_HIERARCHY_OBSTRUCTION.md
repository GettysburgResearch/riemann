# A full weak-closure obstruction to the positive-cosh hierarchy

Status: **PROPOSED complete native analytic theorem.** This is an
all-order construction attempt with a decisive obstruction, rather than
another finite moment search. It excludes a specified Gaussian-mediated
rank-one ferromagnetic hierarchy, including critical limits in which the
finite Gaussian factor disappears. It does not exclude arbitrary Ising
graphs, real-field models, higher-rank mediators or other hierarchies,
and proves neither RH nor an improved zero-free region.

## 1. A plausible exact transfer construction

For each N choose a_N>0, a finite number m_N of real nonnegative
b_{j,N}, and the probability density

    p_N(x)=Z_N^(-1) exp(-a_N x^2)
                             product_(j=1)^m_N cosh(b_{j,N} x). (1)

All parameters and m_N may vary without any prior bound. These are
legitimate ferromagnetic Gaussian-mediated laws. Indeed, expanding the
coshes gives the joint density proportional to

    exp[-a_N x^2+x sum_j b_{j,N} sigma_j].            (2)

Integrating out x gives a zero-field Ising law with couplings

    J_ij=b_i b_j/(2a_N)>=0.

Conditioned on the spins, x is normal with mean
`sum_j b_j sigma_j/(2a_N)` and variance `1/(2a_N)`. Equivalently it is
a positive rank-one ferromagnetic spin observable plus an independent
Gaussian. Thus the finite laws have real-zero characteristic functions
by finite Lee--Yang and the zero-free Gaussian factor. They are a natural
candidate for a growth-controlled, exactly tied hierarchy.

The earlier infinitely-divisible-factor obstruction does not already
dispose of a cofinal construction: a_N may tend to infinity, allowing
the independent Gaussian variance to vanish. Critical mean-field limits
can survive precisely this way. The theorem below covers that escape.

**Theorem.** If the laws (1) converge weakly to a law having a continuous
everywhere-positive even density p on R, then there are finite constants
C_0,C_2,C_4, independent of x, such that

    -log[p(x)/p(1)] <= C_0+C_2 x^2+C_4 x^4,  x>0.  (3)

Consequently the actual theta density is not a weak limit of (1).
No moment, derivative, support, parameter or tail bound on (1) is assumed.

The proof has two essential parts: weak convergence yields local density
ratios through convexity in x^2; three such ratios bound a global
fourth-order resource. We do not infer any tail convergence directly
from weak convergence.

## 2. Native local compactness lemma for logconcave densities

Let I be a compact interval with nonempty interior. Suppose probability
densities g_N on I are positive and logconcave in its interior and their
laws converge weakly to a law with positive continuous density g there.
Then

    log g_N -> log g locally uniformly in int(I).   (4)

Here is a direct proof. For a chosen compact subinterval K in int(I),
take a strictly larger compact K' and disjoint intervals L,R lying to
the left and right of K', still inside I. Positive limiting masses on
L,R give a uniform positive lower mass for large N. Hence there exist
points l_N in L and r_N in R with g_N(l_N),g_N(r_N)>=c>0. Concavity of
log g_N gives the lower bound log c throughout their joining interval,
in particular on K'.

For x in K', at least one of those anchors is a fixed distance d>0
away. If M=log g_N(x)>=log c, the half of that segment adjacent to x
has length at least d/2 and logarithmic density at least
`(M+log c)/2`. Its integral cannot exceed1. Thus

    M <= 2log(2/d)-log c.

Both upper and lower bounds are uniform on K'. A concave function
bounded on a larger interval has bounded slopes on its strictly inner
interval; applying the secant inequalities gives equicontinuity on K.
Every subsequence therefore has a uniformly convergent subsubsequence
of log densities on K. Its exponential is the weak limiting density,
first almost everywhere and then everywhere by continuity. The only
possible limit is log g. This proves (4), and exhaustion proves it on
every compact interior interval.

## 3. Weak convergence really does control the needed ratios

Write the unnormalized potential of (1) as

    V_N(x)=a_N x^2-sum_j log cosh(b_{j,N} x),
    V_N(0)=0.                                      (5)

For u>0 the function `log cosh(b sqrt(u))` is concave. In fact its
derivative is `b^2 tanh(y)/(2y)`, y=b sqrt(u), and tanh(y)/y strictly
decreases for y>0: its derivative has the sign of
`y sech(y)^2-tanh(y)<0`, equivalent to
`y<sinh(y)cosh(y)`. Thus V_N(sqrt(u)) is convex.

Let U_N=X_N^2. Its density on (0,infinity) is

    p_N(sqrt(u))/sqrt(u).

Fix an arbitrary interval I=[A,B] with 0<A<B<infinity. Restrict the
law of U_N to I, multiply by sqrt(u), and renormalize. The resulting
probability density is

    g_N(u)=p_N(sqrt(u))/integral_I p_N(sqrt(v)) dv,
                         u in I.                   (6)

It is logconcave by (5). The multiplier sqrt(u) is bounded on I. Weak
convergence of X_N gives weak convergence of U_N and then of these
weighted restrictions: the only endpoint discontinuities are on a set
of zero limiting measure, and their normalizing mass tends to a
positive number. The limiting density in (6) is the same expression
with p in place of p_N; it is positive and continuous.

Apply section2. For any x,y>0 whose squares lie in int(I),

    V_N(x)-V_N(y) -> -log[p(x)/p(y)].                (7)

The interval may contain any prescribed finite list of positive x's.
This proves local density-ratio convergence using only weak convergence;
it needs neither uniform integrability nor convergence of p_N(0).

## 4. Three local ratios bound all microscopic parameters

Put `f_b(x)=log cosh(bx)` and

    G(b)=-f_b(3)+(8/3)f_b(2)-(5/3)f_b(1).           (8)

For b>0, concavity of `u -> f_b(sqrt(u))` at u=1,4,9 implies

    [f_b(2)-f_b(1)]/3 > [f_b(3)-f_b(2)]/5,

so G(b)>0. Taylor expansion and the elementary large-argument form of
log cosh give

    G(b)=(10/3)b^4+O(b^6),           b->0;
    G(b)=(2/3)b+O(exp(-2b)),         b->infinity.    (9)

The constants log2 cancel in the second identity. Therefore continuity
and positivity give a universal constant c_*>0 with

    G(b)>=c_* min(b^4,b),             b>=0.         (10)

This is a purely analytic existence bound: the quotient is positive on
compact subsets of (0,infinity), and has positive limits at both ends.
No numerical minimization is used. As an independent algebraic check,
put w=tanh(b)^2. The root track supplied the exact identity

    exp(3G)=(1+w)^8/[(1-w)(1+3w)^3],

whose numerator minus denominator is

    10w^2+56w^3+97w^4+56w^5+28w^6+8w^7+w^8>0.

The coefficients in (8) have sum0 and their weighted x^2 sum is0.
Consequently

    V_N(3)-(8/3)V_N(2)+(5/3)V_N(1)=sum_j G(b_{j,N}). (11)

By (7), the left side converges to a finite value; rewriting it as
`[V_N(3)-V_N(1)]-(8/3)[V_N(2)-V_N(1)]` makes the canceled normalization
explicit. Equations(10)--(11) imply a finite uniform resource S with

    sum_(b_j<=1)b_j^4 <= S,
    sum_(b_j>1)b_j <= S,
    sum_(b_j>1)b_j^2 <= S^2.                        (12)

Finitely many initial N may be omitted. Enlarging S covers them if
needed. This is the step that prevents a weak-limit tail argument from
silently losing its coefficient bounds.

## 5. The quartic envelope follows

Define

    q(y)=y^2/2-log cosh(y).

It is even and satisfies

    0<=q(y)<=min(y^2/2,y^4/12).                     (13)

Indeed q''(y)=tanh(y)^2 lies between0 and min(1,y^2), and integrating
twice from0 proves (13). Set

    c_N=a_N-(1/2)sum_j b_{j,N}^2,
    V_N(x)=c_N x^2+sum_j q(b_{j,N}x).              (14)

The sum b_j^2 in this identity is finite for each N; it is not asserted
uniformly bounded. From (12)--(13), for every real x,

    0<=sum_j q(b_j x)<=S x^4/12+S^2 x^2/2.         (15)

By (7), `V_N(2)-V_N(1)` is bounded. Equation(14) gives

    3c_N=V_N(2)-V_N(1)-sum_j[q(2b_j)-q(b_j)].

The final sum is bounded by (15) at x=1,2. Thus |c_N|<=C for a finite
constant C independent of N. Equations(14)--(15) now imply, for x>0,

    V_N(x)-V_N(1)
       <= C(x^2+1)+S x^4/12+S^2 x^2/2.             (16)

Pass to the limit using (7) for each fixed x. This proves (3).
The constants in (16) work simultaneously for every x, because they
were derived from only the fixed local ratios at1,2,3.

## 6. Apply the theorem to the actual complete theta density

Use the same original positive kernel as PROOF22.md and THETA_GROWTH.md:

    Phi(t)=sum_(n>=1)
      [4pi^2 n^4 exp(9t/2)-6pi n^2 exp(5t/2)]
                                   exp[-pi n^2 exp(2t)], t>=0, (17)

with its smooth even Jacobi-theta extension. All terms are positive on
t>=0. The full-source ratio estimate in THETA_GROWTH.md gives
`sum_(n>=2)g_n(t)/g_1(t)->0` as t->infinity. This also follows directly
from its exact ratio there by a summable exponential majorant. Hence

    -log[Phi(t)/Phi(1)]
       =pi exp(2t)-(9/2)t+O(1),       t->infinity.  (18)

The normalized actual theta law has positive continuous density
`p_theta(t)=Phi(t)/integral_R Phi`. Its potential ratio is the left
side of (18), so it exceeds every quartic envelope. This contradicts
(3). Thus the proposed rank-one hierarchy cannot converge weakly to
the actual theta law.

In particular, no sequence of models(1) can match every fixed theta
moment asymptotically while having any of the uniform entire/MGF
resources used in this packet: those resources give weak convergence
to the actual moment-determinate law, which the theorem excludes.

## 7. Scope of the surviving construction problem

The theorem covers arbitrary numbers of auxiliary spins, arbitrary
inhomogeneous positive b_j, arbitrary a_N, and critical a_N->infinity.
It does not rely on the harmonic lattice or on a persistent independent
Gaussian factor. It is therefore distinct from both earlier
obstructions.

It concerns exactly the zero-field positive product of coshes with a
single quadratic mediator. Correlated auxiliary-spin graphs, multiple
interacting mediators, asymmetric or paired nonzero fields, and
nonquadratic transfer energies do not automatically have the form(1).
They require their own construction and compactness argument. No claim
that all Lee--Yang laws have the representation(1) is made.
