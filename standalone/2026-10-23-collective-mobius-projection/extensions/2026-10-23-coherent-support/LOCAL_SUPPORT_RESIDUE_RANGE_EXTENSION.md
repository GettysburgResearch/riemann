# The local-support bound extends both residue vectors to D^(1/6)

23 October2026. Proposed source-dependent deduction by the global-route agent;
independent review requested. This uses root's frozen
`LOCAL_SUPPORT_VECTOR_REFINEMENT.md`, SHA256
`499e1333611699c91a6c3b2cf5376f5b702bca74254b222bab47fdc93043f1dc`.
All good-ideal, fixed-ray, puncture, literal-zero and common smooth-profile
conventions are exactly those of that input and the sixth-free predecessor.
Ideal letters inside exponents denote their absolute norms.

For D>=1 and good sixth-power-free labels R of norm at most K<=D, the
full residue vector satisfies

    sum_R |P_R^full(D)|^2
       << (DKNQ)^epsilon [D^(2/3)+D^(1/2)K].              (V1)

The primitive residue vector satisfies

    sum_R |P_R^prim(D)|^2
       << (DKNQ)^epsilon
          [D^(2/3)+D^(1/2)K+D^(-1/6)K^(11/6)].          (V2)

In particular both are bounded by `(DKNQ)^epsilon D^(2/3)` throughout

    1<=K<=D^(1/6).                                     (V3)

This extends the earlier D^(1/7) residue-label range. It is not a bound for
the full primitive continuous vector or the complementary inverse operator.

## 1. Full residue at the unchanged reference scale

Choose the same nonnegative nonzero fixed test w used in the predecessor,
so the exact coefficient `c_w=zeta_S(2)*w_hat(2/3)` is nonzero. The completed
finite-minus-contour identity at reference Y=D is

    B_R(D)-F_R(D)=c_w D^(1/6) P_R^full(D).              (V4)

Root's improved original completion bound L5 gives

    sum_R |B_R(D)|^2
       << (DKNQ)^epsilon [D+K sqrt(D)+D^(5/6)K].         (V5)

For a label dyad NR~H, the reflected scale is C=DH/D=H. Its L6 gives
`H+H^(3/2)+D^(5/6)H^(1/6)+D^(5/6)H`. Summing dyads therefore yields

    sum_R |F_R(D)|^2
       << (DKNQ)^epsilon
          [K+K^(3/2)+D^(5/6)K^(1/6)+D^(5/6)K].         (V6)

Divide the sum of V5 and V6 by D^(1/3), using V4 and the squared triangle
inequality. For 1<=K<=D, every resulting term except D^(2/3) is bounded
by D^(1/2)K. The possibly largest additional term
`D^(-1/3)K^(3/2)` has ratio `D^(-5/6)K^(1/2)<=D^(-1/3)` to that term.
This proves V1. No residue estimate was used to prove this step: L5/L6
are finite-vector and functional-equation bounds, independent of root's L7.

## 2. Primitive density with its complete divisor tail

Use only the exact residue density identity, at all numerator valuations,
from the predecessor's L16--L17. For a fixed label R, its R-supported
density factor is at most1. Expanding the remaining n-supported factor
gives squarefree d dividing n with `(d,R)=1`, outside coefficient at most
`d^(-3/2)`, new free length `D/d`, new label dR, and fixed puncture Qd.
The arithmetic free coefficient remains the actual Möbius coefficient with
fixed ray data and allowed norm twists. Since `(d,R)=1`, dR is still
sixth-power-free. For each fixed d its set of labels is a subset of the
distinct sixth-free labels of norm at most dK. No reduction of a continuous
numerator modulo sixth powers is used.

Split the divisor sum at

    A=sqrt(D/K)>=1.                                    (V7)

For d<=A, one has `dK<=D/d`, so V1 applies at length D/d and label limit
dK. Minkowski in the original label Hilbert space gives the two amplitude
sums

    D^(1/3) sum_(d<=A) d^(-11/6),
    D^(1/4) sqrt(K) sum_(d<=A) d^(-5/4).               (V8)

They converge and give squared cost `D^(2/3)+D^(1/2)K`, up to subpowers.
The moving Qd puncture is fixed during each individual row average and has
only the inherited epsilon dependence.

For d>A, use the already proved label-uniform scalar bound L2, at new
length D/d and label dR. Summing the at most O(K) original labels gives,
including the squared outside d^(-3/2) weight,

    D^(2/3)K d^(-11/3) + D^(1/3)K^(4/3) d^(-3).       (V9)

The two square-root ideal tails are bounded by

    D^(1/3)sqrt(K) A^(-5/6),
    D^(1/6)K^(2/3) A^(-1/2),

both equal in scale to `D^(-1/12)K^(11/12)`. Their squared cost is
`D^(-1/6)K^(11/6)`, proving V2. Every divisor compatible with the original
annular support is included. Bounded subunit residual lengths are covered
by the same fixed unit-ball enlargement as in the scalar source; beyond
that support the original term is zero. All infinite majorant sums above
converge with a fixed margin, allowing the usual smaller internal epsilon.

For K<=D^(1/6), the second term in V2 is at most D^(2/3), and the third
is at most `D^(5/36)`, also smaller. This proves V3.

## 3. Consequence for the full raw contour vector

Root's L7 proof used K<=D^(1/7) only through the old residue range and
elementary cost dominations. Replacing that residue input by V3 gives

    sum_R |R_R(U)|^2
       << ((2+U)DKNQ)^epsilon
          [D^(11/12)K^(1/12)+D^(5/6)K],
    U>0, 1<=K<=D^(1/6).                               (V10)

The volume and pole dominations require only K<=D. The mixed volume term
`D^(1/4)K^(5/4)` is bounded by `D^(11/12)K^(1/12)` whenever K<=D^(4/7),
so the new range is inside it. The reciprocal-completion sums, finite
harmonic plateaux and exact subunit pole are otherwise unchanged.

At the natural dual label length `K=D/U=D^(1-h)`, V10 is available for
h>=5/6 and has exponents `1-h/12` and `11/6-h`. Both beat the old inverse
resource exponent `5/6+h/6` whenever h>6/7, with fixed slack. For instance,
at `U=D^(7/8), K=D^(1/8)`, the full raw vector bound is D^(23/24+epsilon),
versus the old resource D^(47/48+epsilon), a saving of1/48 for this vector.

This example concerns the full Gauss-series contour vector. It is not the
actual primitive projection without its separate simultaneous inversion,
and it does not control the complementary inverse space. No change to
B_flat, no zero-free theorem, and no RH conclusion is inferred here.
