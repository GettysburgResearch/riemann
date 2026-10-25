# Independent review of the integer bridge and weighted triangle count

Reviewer: `/root/hlc_joint_paths`. Author reviewed:
`/root/coherent_identity`. Date: 25 October 2026.

## Frozen objects and outcome

- `THREE_EDGE_INTEGER_BRIDGE.md`, SHA256
  `9f4f7e2c327a30b8ce530da9d588d671367eb9d8bb1778c3c3dc8bccb68ff067`.
- `check_three_edge_integer_bridge.py`, SHA256
  `65b15c1ed27765285347b85b0235f2524ceab33b52229957dba4b5f206909866`.

**Outcome: accepted as fixed-data algebraic and measure theorems,
including the summed gcd-weighted triangle estimate.** The review does
not certify a full HLC path sum, native inverse moment, or new zero-free
region. The separate transfer of (15e) to original source state weights
is authored in `CLOSED_TRIANGLE_WEIGHT.md` by this reviewer and is being
reviewed independently by another agent; it is not self-certified here.

I read the complete note and independently ran the checker under
`python -O`. I also checked the source PDF's actual root measure
(4.29), derivative (4.31), position range (4.33), and determinant
parametrization (4.40). The checked PDF has SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.

## 1. Integer bridges and their exceptional cases

In the fixed unimodular basis, the two remaining determinant equations
are `h y-j_0 x=j_1` and `B x-A y=j_2`. Their Cramer identities give
`Delta y=N` and `Delta x=A j_1+h j_2`, with
`Delta=B h-A j_0`, `N=B j_1+j_0 j_2`. When B,N are nonzero,
Delta cannot vanish. Each signed divisor Delta of N gives at most one
h, then one pair x,y. The two divisibility conditions in Theorem 1
are necessary and sufficient; no integrality condition is omitted.
Primitivity is unchanged by the unimodular basis.

The N=0 classification correctly separates Delta nonzero, which
forces `z_2=z_0` under the common positive functional, from Delta
zero, which forces `z_1=z_3`. The corresponding determinant signs
are correct. This does not infer list or memory restoration.

For B=0, primitivity and positivity give `z_3=z_0`, and h remains
free in one residue class modulo `|j_0|/gcd(|j_0|,|j_2|)`, when the
congruence is soluble. Treating a fixed Delta as determining h here
would be false; the note does not do so. The displayed prime-q closed
triangle example is primitive outside its two excluded residues and
has the asserted positive measure. It is expressly a geometric
example, without a lower bound for an arithmetic pairing.

## 2. Unwrapped root windows and source constants

For a fixed candidate h, the first position test has interval length
`W/|j_0|` in the unwrapped coordinate R. The at-most-`2 tau(|N|)`
candidate count therefore gives (12). Endpoint and good-state tests
can be retained by restriction; no claim that their endpoints remain
constant in R is used.

With the source convention `tau_r(z)=z_1-2r z_2` and determinant
one, the derivative is exactly `-2/tau_r(z_0)^2`. The retained tau
range gives inverse Jacobian at most 128. The first ratio interval
has length `255/16`. Hence the general constant is
`128*2*(255/16)=4080`. At the global root, `R=-2r` and the inverse
Jacobian is exactly one half, giving the sharper `255/16` constant.
Neither deduction replaces R by its fractional part.

The general-vertex closed-triangle corollary also checks. The identity
`R=w_2/z_2-1/(z_2 tau_r(z_0))` bounds the image length by less than
16 when `z_2` is nonzero; the primitive horizontal case is the global
root. Covering by 17 unit intervals and applying the inverse Jacobian
gives 2176. Multiplying by `255/16` gives 34680 as printed.

## 3. Closed-triangle multiplicity and the weighted sum

The projected closed-triangle event has period `1/g` in R, where
`g=gcd(|j_0|,|j_2|)`. Its period density is the minimum with one
in (15a). For an operator path expansion the count, not that union
probability, is needed. Equation (15d) correctly retains every h:
the integral over one period is `W/|j_0|`, and `R in [-2,0]`
covers exactly `2g` periods with Jacobian one half. Thus its mean
is exactly `Wg/|j_0|`, without a minimum with one.

The final note states the actual-source chronological determinant
tuple `sigma D(b-a,a-c,c-b)`. The overall sign and the permissible
swap of the last two difference labels do not change the gcd ratio.
The common D cancels, and the determinant sum zero ensures congruence
solvability. The scalar summation then bounds the two signed differences
by `floor(3Y)`. The estimates
`sum_(k<=H) gcd(h,k)<=H tau(h)` and
`sum_(h<=H) tau(h)/h<=(1+log H)^2`, followed by the four sign
choices, at most `4Y` base values and `1/(abc)<=Y^(-3)`, give
exactly `48W Y^(-1)(1+log(3Y))^2`.

The enlargement only adds nonnegative numerical terms after a valid
weighted count. It does not create extra original prime paths. The
note explicitly requires the additional original-state normalization
argument before applying this theorem to a source contraction.

## 4. Eisenstein extension

The same Cramer equations hold over the Eisenstein fraction field.
For B,N nonzero, an element divisor of N determines at most one
candidate. The Euclidean property makes every divisor ideal principal;
its six generator associates account for the factor six exactly.
The N=0 classification retains unit-proportional returns. There is no
unlicensed positivity argument eliminating the five other units.
The B=0 congruence includes its endpoint unit correctly.

For fixed data and an unwrapped complex position region Omega,
multiplication by `j_0` scales planar area by `N(j_0)`. Dividing
by the fundamental parallelogram's area `sqrt(3)/2` gives (19).
It is legitimate to intersect each preimage with the parallelogram
before the union bound. A condition modulo the lattice would have
different multiplicity; the note explicitly excludes that inference.
The ideal-divisor subpower bound is also proved by its finite/small
prime-ideal factor split, rather than assumed to follow from the
finite checker.

## 5. Reproduction and limits

The independent optimized-Python replay passed, including:

- 5,880 nonresonant integer data sets and 12,856 independently
  enumerated integer bridges;
- 890 positive first backtracks, 494 positive last backtracks, and
  216 closed congruence classes;
- 5,880 rational phase unions, 756 exact gcd-event densities and
  756 exact candidate-count integrals;
- 54,540 weighted distinct-product triples, nine weighted sum
  scales, 2,080 gcd inner-sum inequalities and 64 harmonic checks;
- 12,312 nonresonant Eisenstein data sets, 54,072 independent
  Eisenstein bridges, 25,128 unit-return cases and 288 area dilations;
- 576 exact source Jacobians and two nontrivial large source-root
  measure examples.

These checks support the finite algebra and constants. The proofs in
the note establish the stated exact and measure results. The complete
source root-replacement theorem, conditional history densities,
arbitrary surrounding paths, and native arithmetic coefficient
matching remain outside this review's conclusion.
