# Infinite native physical faithfulness from independent local radicals

This is a source theorem, with no new numerical acquisition. It concerns the
literal finite-prime half-source and the original physical observation. It is
separate from the companion finite-prime completion/convergence proof. The
short absolute-convergence argument below states exactly what is needed from
that completion. No full retained-gamma decoder is identified.

The source is L-102707 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`. The literal horizon filtration is
frozen at `2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a`, file
`SOURCE_CURVATURE_HORIZON_FILTRATION.md`. The exact physical/literal equality
through horizon900 is the separate bounded packet
`a4d610431d5edaf26b00bae903bb9111837e4c31`; none of its untested horizons is
assigned a rank here.

## 1. The actual tensor observation

Fix distinct primes p_1,...,p_r. Write V for the 2^r-dimensional space of
multilinear polynomials in independent schedules u_1,...,u_r, with basis u^a,
a in{0,1}^r. The literal source coefficients are

    lambda_n(u)=sum_a v_(n,a) u^a,
    S(u,z)=sum_n lambda_n(u) product_i z_i^(ord_(p_i)n)
          =product_i [A(z_i)+u_i B(z_i)],
    A(z)=sqrt(1-z^2),
    B(z)=sqrt(1-z)-sqrt(1-z^2).                         (1)

Only indices supported on the fixed primes occur. All square roots in the
unit disk take value1 at0. For a constant complex matrix M with rows and
columns indexed by a,b in{0,1}^r, define

    T_H(M)(t)=sum_(nm<=H) (v_n^t M v_m)/sqrt(nm) (n/m)^(it).  (2)

Here the superscript t denotes transpose, not conjugate transpose. For real t
the two source arguments are complex conjugates; M itself need not satisfy a
reality or symmetry condition. There are **4^r** tensor coefficients in this
statement. They are distinct from the smaller actual curvature space.

At a reduced ratio a/b, (2) combines the literal records with exactly

    (a/b)^(it)/sqrt(ab) * sum_(d^2 ab<=H) (v_(da)^t M v_(db))/d.  (3)

Thus this is the original physical coalescence, including its1/d weights.
It is not a norm on uncombined coefficients or on formal phase labels.

Put x_i=p_i^(-1/2+it), y_i=p_i^(-1/2-it), so x_i y_i=q_i=1/p_i.
If s_a(z) is the coefficient of u^a in S(u,z), the completed observation is

    T_infinity(M)(t)=sum_(a,b) M_(a,b) s_a(x) s_b(y).   (4)

## 2. Absolute convergence and the analytic strip

Write sqrt(1-z)=sum_e c_e z^e. The local coefficient in (1) is a_e+b_e u,
where a_e=c_(e/2) for even e and0 for odd e, and b_e=c_e-a_e. Since the
Taylor series converge absolutely at every |z|<1,

    sum_n ||v_n||_1/sqrt(n)
      =product_i sum_(e>=0) (|a_e|+|b_e|) p_i^(-e/2)<infinity.  (5)

Consequently the double tensor series is absolutely convergent, uniformly
for real t and for M in any bounded finite-dimensional set. On every compact
subset of |Im(t)|<1/2 the same argument applies to both x_i and y_i, with
their radii bounded strictly below1. Thus (4) is holomorphic on that strip,
and (2) converges uniformly on the real axis and normally on compact
substrips. In particular a zero on a real interval is a holomorphic identity.

This is the fixed-finite-prime completion only. No infinite-prime Euler
product, change in physical weight, or uniformity as the prime set grows is
asserted.

There is also an exact unweighted coefficient bound, consistent with
Section2 of the companion `FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md`.
For e>=1, c_e<0 and their absolute sum is1. The even/odd sums at z=1 and-1
give sum_(e odd)|c_e|=sqrt(2)/2 and
sum_(k>=1)(c_(2k)-c_k)=sqrt(2)/2. Therefore

    sum_e |a_e|=2,  sum_e |b_e|=sqrt(2),
    sum_n ||v_n||_1=(2+sqrt(2))^r.                    (5a)

For completeness, absolute convergence at the endpoints follows already
from the signs and the finite identity
sum_(e=0)^N c_e=binom(2N,N)/4^N ->0; the series at-1 then has value sqrt(2)
by continuity from the disk. Thus (5a) does not presume a conditional
rearrangement of the boundary series.

## 3. Four independent local tensor functions

Fix one prime and write q=1/p, x=x_i, y=q/x. On the annulus q<|x|<1 all local
factors are holomorphic and A(x)A(y) is nonzero. The decisive simplification is

    B(x)/A(x)=(1+x)^(-1/2)-1=U(x)-1,
    B(y)/A(y)=(1+q/x)^(-1/2)-1=V(x)-1.                 (6)

It follows directly from the chosen square-root branches in the unit disk:
sqrt(1-z)/sqrt(1-z^2)=1/sqrt(1+z). After dividing by A(x)A(y), the four local
tensor functions A(x)A(y), B(x)A(y), A(x)B(y), B(x)B(y) are an invertible
constant linear transform of

    1, U, V, UV.                                      (7)

These functions are linearly independent, even over C(x). Indeed

    U^2=1/(1+x),      V^2=x/(x+q).

The branch points of U are{-1,infinity}; those of V are{0,-q}. They are
disjoint because0<q<1. An identity in (7), initially on the annulus, can be
continued as an algebraic-function identity along paths avoiding these
points and any poles of its rational coefficients. A loop around-1 changes
the sign of U alone; a loop around-q changes the sign of V alone. Applying
the two sign changes to the identity and taking their four signed averages
isolates its four terms. Every coefficient must vanish. This also gives an
elementary monodromy proof without requiring a separately invoked
multiquadratic-extension theorem.

For r independent variables the products of these four local functions are
linearly independent. One can either apply the same sign changes in each
variable or iterate the one-variable argument with the other variables held
generic. Hence all4^r functions

    s_a(x_1,...,x_r) s_b(q_1/x_1,...,q_r/x_r)          (8)

are linearly independent as holomorphic functions on the product annulus.

## 4. The actual one-parameter observation is faithful

The continuous phase orbit

    t -> (exp(it log p_1),...,exp(it log p_r))

is dense in the r-torus. Its only possible annihilating integer character
would satisfy sum_i k_i log p_i=0, which unique prime factorization forces to
be the zero character. This is continuous-flow density: there is no discrete
time requirement involving an extra2pi. Equivalently, each nonconstant
Fourier character has zero long-time average on the orbit; trigonometric
approximation of a nonnegative continuous bump proves density.

Suppose T_infinity(M) vanishes on a real interval. Holomorphy in the strip
makes it vanish for every real t. Density and continuity then make the
function in (8) vanish on the complete product torus |x_i|=p_i^(-1/2).
Repeated use of the one-variable holomorphic identity theorem extends that
identity to the product annulus. The independence in Section3 gives M=0.

In particular the completed physical observation is injective on the full
4^r-dimensional complex monomial-tensor space. Let nu be the original
measure dnu=|kappa_hat(t)|^2 dt/(2pi). The fixed nonzero compactly supported
L2 kernel kappa has finite nu-mass, and its Fourier transform is entire and
nonzero. Its real zeros are isolated, so nu has a positive density on an
open interval. If ||T_infinity(M)||_(L2(nu))=0, continuity makes the function
zero on such an interval. Therefore the same injectivity holds in the
**actual** physical Hilbert space. More generally the argument needs only a
finite positive measure with a positive density on some interval.

## 5. Application to the actual curvature directions

Let W be the span of the literal polynomial two-forms

    C_(n,m)=2 d(lambda_n) wedge d(lambda_m).

For a complex linear functional ell on W set

    M_(a,b)=ell(2 d(u^a) wedge d(u^b)).                 (9)

This is a skew matrix, and v_n^t M v_m=ell(C_(n,m)). The squarefree source
monomials span V, so ell nonzero implies M nonzero. Thus (9) embeds W* into
the full tensor space considered above, and the original infinite physical
curvature observation is injective on W*.

For the three primes2,3,5 this is the actual20-dimensional direction space,
not64 independently attainable path parameters. Its dimension and source
accessibility are established by the separate multigroup theorem. Nothing
here asserts that arbitrary moment vectors are attained by monotone paths,
or that the full physical current has only20 unconstrained coefficients.

## 6. Eventual faithfulness at every sufficiently large finite horizon

Fix any norm on the finite tensor coefficient space. By (5),

    delta_H=sum_(nm>H) ||v_n||_1 ||v_m||_1/sqrt(nm)
           <=(2+sqrt(2))^(2r)/sqrt(H).                (10)

Uniformly on real t,

    |T_H(M)(t)-T_infinity(M)(t)| <= ||M|| delta_H

for the corresponding entrywise-bounded matrix norm (and after a fixed
finite-dimensional constant for any other norm). Hence the observation
operators converge in norm into L2(nu), with error at most
sqrt(nu(R))*(2+sqrt(2))^(2r)*H^(-1/2) for this matrix norm. The completed operator is injective
on a finite-dimensional domain, so its smallest singular value is strictly
positive. Norm convergence implies that T_H is injective on this full
tensor space for **every H beyond some finite H_0**. The same conclusion
holds on W*. No monotonicity of finite-horizon rank is used.

For2,3,5, after increasing H_0 to at least450, every H>=H_0 therefore has
physical curvature rank20, equal to its literal rank. The finite physical
Gram matrices converge to a positive-definite Gram matrix on these20
directions. This proves that only finitely many later horizons could fail
faithfulness, but supplies **no numerical upper bound for H_0**.

The bounded equality at every H<=900 and this eventual theorem do not prove
equality at every H: an unverified finite gap can remain above900. In
particular H_0<=900, monotonicity of all finite physical ranks, a quantitative
uniform conditioning bound, and an all-horizon optimizer are not claimed.
The theorem is for the declared finite-prime coefficient source and its
original observation; it does not identify the complete retained-gamma
decoder or prove a principal-member estimate.
