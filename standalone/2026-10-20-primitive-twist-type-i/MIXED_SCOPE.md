# What the new finite-twist block buys, and what it does not

Status: source-dependent consequences of PROOF.md; no new zero-free region.

## 1. Concrete improvement with a growing quadratic conductor

Write Y=AB and K=C0*C1^2. The marked theorem is

    |T| << Y^(p+epsilon) (B^3 K)^q,
    p=(2 beta+1)/6, q=(5-2 beta)/12.                         (1)

The direct Euler-product version of the same proof has beta=1,
so p=1/2,q=1/4. Their ratio, ignoring subpowers, is

    [sqrt(B C0)*C1/A]^((1-beta)/3).                         (2)

Thus the zero-free input improves this estimate when
A>sqrt(B C0)*C1 with a power margin. It is not an improvement uniformly
at every conductor size.

For B=Y^theta and K<=Y^lambda, (1) has exponent
p+q(3theta+lambda). It is below 1 when 3theta+lambda<2 and below 5/6 when

    3theta+lambda < 4(2-beta)/(5-2 beta).                   (3)

These are exact scale inequalities. As an explicit nonresonant sixth-order
example, take ell=0, C0 fixed, B=Y^(1/4), and C1<=Y^(3/10). The weaker
input beta=7/8, implied by the imported B_flat input, gives

    |T| << Y^(791/960+epsilon)
          = Y^(5/6-3/320+epsilon).                         (4)

The Euler-only baseline in the same regime is Y^(67/80+epsilon), whose
exponent exceeds 5/6. Using beta=B_flat improves (4) to

    |T| << Y^(0.823946053429329...+epsilon).                 (5)

This is a bound for the explicitly defined twisted cubic sum T. Neither
0.823946 nor 791/960 is a zero-free boundary for zeta or an L-function.
This example uses growing finite conductors and does not depend on the
candidate angular Hecke theorem of #1009.

## 2. How it relates to #1009

At c1=1 and ell!=0 the new theorem recovers the level exponents of the
pure cubic/angular Type-I block in #1009. The genuinely changed interface
is c1!=1: primitive quadratic and other finite twists are allowed,
including ell=0, while their nonmatching level costs are retained.
The source has an explicit general periodic functional equation, but its
printed Lemma 5.4 and special level calculation use cubic characters.
Our completion uses psi^3 and our dual transform distinguishes the two
local conductor types. No claim of literature-wide novelty is made.

The previous block could not simply be multiplied by a quadratic
character while retaining its cheap level. The exact q^2 local mass
shows why that substitution would be wrong. The new proof repairs that
interface rather than claiming that all its resulting costs are free.

## 3. Why this does not prove the requested 0.874 region

The original full mixed norm in #1006 is over sixth-power-free rows:

    sum_u |M_u(D) S_u(N)|^2,
    D=U^r, N=U^m,
    1<=r<=3/2, 0<=m<=1/2, 3/2<=r+m<=2,

including robust neighborhoods, all original nonunit zeros, shared
primes, finite twists, heights and common profiles. The U^(6/5+epsilon)
consumer in that PR is conditional on this WHOLE norm. It would yield
ordinary-zeta/fixed-Eisenstein-family nonvanishing for Re(s)>437/500.
It is not automatically an all-number-fields theorem.

The present work bounds one actual primitive twisted block with a
short divisor mark, NOT that norm. In particular:

* Large nonmatching conductor has the cost C1^(2q). The boundary (3)
  makes the restricted useful range explicit; absolute summation of
  individual blocks may exceed the mixed budget.
* The source also contains nonsquarefree rows, pair-conductor patterns,
  quadratic components, correlated off-diagonal coefficients and common
  profile integrations. A complete physical-to-block map with a paid
  joint average is still required. Arbitrary prime-power characters are
  not covered by the primitive squarefree-modulus theorem.
* Even the pure inverse edge (r,m)=(3/2,0) has the recorded available
  exponent 17/12, above 6/5. Bounding a marked nonresonant block cannot
  be substituted for an improvement on this edge. No native saving of
  0.01225 at the previously identified binding class is established here.

The exact high-conductor/high-core remainder in #1006 remains open. No
part of that signed remainder has been discarded as positive or small.

## 4. Revised concrete next target

The new useful distinction is matching versus nonmatching conductor,
not total conductor alone. In the actual opened mixed covariance, retain
the primitive pair character and record K=C0*C1^2 before estimating.
The next meaningful theorem must bound the aggregate complementary
blocks where 3theta+lambda violates (3), with the original correlated
coefficients and all row multiplicities still present. A quadratic
conductor-average or a two-variable spectral estimate may improve this
cost; no such estimate is proved here.

The exact local transform and the short-mark estimate supply a checked
starting identity for that task. They do not replace it. We publish this
component because it resolves a concrete finite-twist restriction in the
previous Type-I interface, not because it already moves B_flat.
