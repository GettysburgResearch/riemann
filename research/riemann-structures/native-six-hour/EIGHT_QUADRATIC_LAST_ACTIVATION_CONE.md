# Eight exact quadratic tests for the full three-prime support cone

This proof-only refinement uses the explicit basis in
`ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md`. The native input remains
the original half-source in L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`. No new physical Gram,
horizon acquisition, candidate path or numerical sign is asserted here.

The four square-positivity conditions from that note need no general
bivariate optimization. Their source-specific bidegrees reduce them
exactly to eight univariate quadratic tests. Their total degree can be
three, so describing them as arbitrary total-degree-two polynomials
would be inaccurate.

## 1. Coefficient map in the declared twenty-moment basis

Let c_j multiply the integral of the following one-form, in this order:

| j | One-form | j | One-form |
| ---: | --- | ---: | --- |
| 1 | v du | 11 | u^2 w^2 dv |
| 2 | w du | 12 | v^2 dw |
| 3 | w dv | 13 | u^2 dw |
| 4 | v w du | 14 | u^2 v^2 dw |
| 5 | u w dv | 15 | v w^2 du |
| 6 | w^2 du | 16 | u w^2 dv |
| 7 | v^2 du | 17 | v^2 w du |
| 8 | v^2 w^2 du | 18 | u v^2 dw |
| 9 | w^2 dv | 19 | u^2 w dv |
| 10 | u^2 dv | 20 | u^2 v dw |

Write the resulting form as P du+Q dv+R dw. Crucially, this actual basis
has no w power in R:

    R=c12 v^2+c13 u^2+c14 u^2 v^2+c18 u v^2+c20 u^2 v.

Consequently the gauge potential is exactly T=wR. Subtracting dT
changes the integral by the fixed endpoint value R(1,1). The remaining
coefficients are P0+wP1+w^2P2 and Q0+wQ1+w^2Q2, where

    P0=c1 v+c7 v^2,                  Q0=c10 u^2,

    P1=c2+c4 v+(c17-c18)v^2-2u(c13+c20 v+c14 v^2),
    P2=c6+c15 v+c8 v^2,

    Q1=c3+c5 u+(c19-c20)u^2-2v(c12+c18 u+c14 u^2),
    Q2=c9+c16 u+c11 u^2.                              (1)

These identities follow by differentiating the displayed R; no scalar
trace, fitted coefficient cancellation or positivity assumption is used.

In particular P1 and P1+P2 are affine in u and quadratic in v. Likewise
Q1 and Q1+Q2 are affine in v and quadratic in u. The independent terms
on a final-activation path reduce, including endpoints, to

    R(1,1)+c10 + integral [c1 v-2c10 u v+c7 v^2]du.    (2)

Thus its planar coefficients are a=c1, b=-2c10, c=c7. The constant in(2)
must remain when comparing absolute support values, though it does not
affect the minimizing planar graph.

## 2. Exact reduction from four squares to eight intervals

For sigma,tau in{0,1}, define

    p_(sigma,tau)(z)
      = (c2-2sigma c13+tau c6)
        +(c4-2sigma c20+tau c15)z
        +(c17-c18-2sigma c14+tau c8)z^2,

    q_(sigma,tau)(z)
      = (c3-2sigma c12+tau c9)
        +(c5-2sigma c18+tau c16)z
        +(c19-c20-2sigma c14+tau c11)z^2.              (3)

The four source conditions

    P1>=0, P1+P2>=0, Q1>=0, Q1+Q2>=0

on the unit square hold if and only if all eight polynomials in(3) are
nonnegative on[0,1]. Indeed, for fixed v each P expression is the convex
combination of its values at u=0 and u=1; those endpoint quadratics are
exactly the corresponding p polynomials. The Q expressions work in the
other coordinate. Necessity follows by restricting to the same edges.

The reduction is exact for this source cone. The cone itself is a
sufficient full-path support condition and is not asserted necessary
for an all-path quadratic optimum.

## 3. A sharp quadratic minimum test, including degeneracies

For h(z)=A z^2+B z+C with real coefficients, retain both endpoint values

    h(0)=C,                   h(1)=A+B+C.

There is an additional minimizing interior stationary point precisely
when A>0 and -2A<B<0. Its location and value are

    z_*=-B/(2A),              h(z_*)=C-B^2/(4A).        (4)

Thus h is nonnegative on[0,1] if and only if both endpoint values are
nonnegative and, in the stated interior case, 4AC-B^2>=0. For A<=0 the
minimum is at an endpoint. The linear case A=0 and the constant case
A=B=0 need no division. Vertex equalities B=0 or B=-2A are already
covered by endpoints. A zero discriminant/minimum is retained as a
valid nonnegative polynomial, not rejected as a singular numerical case.

This gives an exact bounded sign test for all eight source quadratics.
It neither discards boundary minima nor assumes generic coefficients.

## 4. Bernstein certificates and outward rational coefficients

The degree-two Bernstein coefficients on[0,1] are

    (C, C+B/2, A+B+C).                                (5)

Their nonnegativity suffices, but is not equivalent to nonnegativity of h.
For example h=(z-1/2)^2 has Bernstein coefficients(1/4,-1/4,1/4), while
(4) certifies its exact zero minimum. A declared subdivision can improve
the Bernstein test. It is not a universal replacement for(4): if a double
zero lies strictly inside one subinterval, that interval's middle
Bernstein coefficient is negative. An irrational double zero therefore
cannot be isolated as an endpoint by a finite rational partition.

For actual gradient coefficients supplied by outward rational intervals,
let A_-,B_-,C_- and A_+,B_+,C_+ be their respective lower and upper bounds.
Because 1,z,z^2 are nonnegative on[0,1],

    A_-z^2+B_-z+C_- <= h(z) <= A_+z^2+B_+z+C_+.         (6)

One sound bounded acceptance policy is:

* PASS if the exact test(4) makes every lower-envelope quadratic
  nonnegative on[0,1].
* Certify failure of this sufficient cone if some upper-envelope quadratic
  has a strictly negative minimum. Its endpoint or rational vertex is
  an explicit witness where the actual quadratic is negative.
* Otherwise retain UNKNOWN. A negative lower-envelope value alone is not
  evidence that the actual cone fails. Correlations or exact zeros in the
  source coefficients may require a sharper certified enclosure or an
  authenticated exact identity.

The same distinctions apply to interval Bernstein coefficients. No
floating-point sign choice or unregistered subdivision is justified by
this note. A later producer can use rational cross-multiplication in(4)
and explicit coefficient/bit caps; no algebraic root solver is needed.

## 5. Consequence for an actual higher-horizon candidate

At a fixed horizon, form c_j from the candidate's actual twenty-moment
half gradient in the original physical Gram. If(3)--(4) certify the cone,
the w-dependent part of the gauged form is nonnegative on every monotone
path and vanishes on the final-activation path. A self-consistent planar
support solution for(2) therefore minimizes this linear functional over
the entire source path class. The original Gram identity proves global
quadratic optimality.

No positive-definiteness assumption on all twenty coordinates is needed
for that implication: the actual Gram is positive semidefinite. Equality
of minimum energies forces equality of the observed fields through the
squared-norm remainder, but need not force equality of all twenty moments
when the physical readout has a kernel. Any stronger path or moment
uniqueness conclusion needs its own support argument.

If every interval minimum in(3) is bounded below by a common delta>0,
the additional support cost is at least delta(D+F), where D=integral w du
and F=integral w dv. This gives quantitative final-activation control.
No such strict margin, no H30 optimum and no larger-horizon persistence
are claimed before the actual coefficient acquisition and verification.
