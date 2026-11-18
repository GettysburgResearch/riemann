# Quantitative growing-order Riesz approximation

Date:2026-11-17. Contributor:equivalences. **New rate extension pending independent review.** This note is separate from the already independently reconstructed convergence argument so its stronger scope is not accepted merely by inheritance. All results assume RH; no historical novelty or RH advance is claimed.

Use the exact notation and classical inputs in `growing_logarithmic_riesz_round3.md`. Fixc>0, epsilon=c/loglogN, alpha=epsilon logN, and integerq>=1. The free auxiliary exponentr from that note is fixed, depends onc, and is chosen to leave the kernel tail exponent at most−kappa_eta alpha/2.

The proposed bound is

||zeta(s)V_N(s)−zeta(s)/zeta(s+epsilon)||_q
 <=C_(q,c)[alpha^(-1/2)+sqrt(alpha)exp(−kappa_eta alpha/2)],       (QR1)

where ||F||_q²=(2pi)^−1 integral_R |F(1/2+it)|²/|1/2+it|^(2q)dt. Consequently

d_q(V_N)=O_(q,c)((loglogN)^(-1/3)),

d_q(V_N)²=O_(q,c)((loglogN)^(-2/3)).                           (QR2)

No constant uniform asc↓0,q→infinity or with movingc is asserted. This is a prescribed growing logarithmic taper, not a fixed Selberg window, and the distinction between the norm and its square is explicit.

## 1. An exact first absolute kernel moment

Writingy=v/epsilon, the absolute kernel density is

|K(v)|dv=B_alpha(1+y²)^(-(alpha+1)/2)dy,

B_alpha=Gamma(alpha+1)e^alpha/(2pi alpha^alpha)<=C sqrt(alpha).

Foralpha>1 a direct substitution gives

integral_R |K(v)| |v|/epsilon dv
 =B_alpha integral_R |y|(1+y²)^(-(alpha+1)/2)dy
 =2B_alpha/(alpha−1)=O(alpha^(-1/2)).                         (QR3)

The equality is exact; it is not a Gaussian approximation or a formal moment expansion.

## 2. Quantitative central difference

Put R_epsilon(t,v)=zeta(s)/zeta(s+epsilon+iv),s=1/2+it. On|v|<=eta epsilon integrate zeta'/zeta along the vertical segment. The source-anchored bound gives an exponentw with

|w|<=D_1|v|log(|t|+3)/epsilon.

Since R_epsilon(t,v)=R_epsilon(t,0)e^w, the inequality|e^w−1|<=|w|e^|w| and the RH completed-product ratio imply

|R_epsilon(t,v)−R_epsilon(t,0)|
 <=C |v|/epsilon log(|t|+3)(|t|+3)^(epsilon/2+D_1eta).         (QR4)

At a critical zero the numerator is0 and the inequality is valid directly; no logarithm of the numerator is required. Chooseeta<=min(1,1/(16D_1)) and eventuallyepsilon<=1/8, so the exponent is at most1/8. The weightedL² norm of log(|t|+3)(|t|+3)^(1/8) is uniformly finite for every fixedq>=1. Therefore Minkowski and(QR3) bound the central kernel integral of this difference byC_q alpha^−1/2.

Because integralK=1,

zeta V_N−R_epsilon(t,0)
 =integral_central K(v)[R_epsilon(t,v)−R_epsilon(t,0)]dv
  +integral_tail K(v)R_epsilon(t,v)dv
  −R_epsilon(t,0)integral_tail K(v)dv.

The first tail is bounded by the free-r global inverse-zeta argument in the convergence proof: C_(q,c)sqrt(alpha)e^(−kappa_eta alpha/2). The second is no larger, since ||R_epsilon(t,0)||_q is uniformly bounded by the completed-product ratio. This proves(QR1), subject to the same declared classical inputs as the convergence proof.

## 3. A separately reconstructed horizontal-ratio rate

For completeness, the following zero-excision argument is included for this **horizontal** ratio rather than silently substituting a symmetric functional-equation ratio. It is the familiar mechanism in the earlier Báez-Duarte audit.

Let B_delta be the union of intervals|t−gamma|<delta around nontrivial zero ordinates, with0<delta<=1/4. The RH product bound gives|R_epsilon(t,0)|<=C(|t|+3)^(epsilon/2), uniformly for0<epsilon<=1/8. Riemann–von Mangoldt and a dyadic sum give

integral_(B_delta) |R_epsilon(t,0)−1|² dt/|s|^(2q)<=C_q delta.  (QR5)

Multiplicity-counting in the union only overcounts. The weighted sum over ordinates converges uniformly because2q−epsilon>1. Any finite low-height set is absorbed by a fixed constant; no lower bound on zero gaps or simplicity is used.

OffB_delta, every zero is at ordinate-distance>=delta. Along the horizontal path sigma from1/2 to1/2+epsilon, the partial-fraction logarithmic derivative formula gives

|zeta'/zeta(sigma+it)|<=C log(|t|+3)/delta.

The pole at1 is outside this path since sigma<=5/8. At bounded heights use the same meromorphic compact-set estimate; at the left endpoint no zero is met. Integrating gives

|R_epsilon(t,0)−1|
 <=C(epsilon/delta)log(|t|+3)(|t|+3)^(Cepsilon/delta).

WhenCepsilon/delta is sufficiently small, its weighted squared integral is at mostC_q epsilon²/delta². Thus

||R_epsilon(t,0)−1||_q²<=C_q[delta+epsilon²/delta²].           (QR6)

Setdelta=epsilon^(2/3), which satisfies the smallness condition eventually. This yields ||R_epsilon(t,0)−1||_q=O_q(epsilon^(1/3)). The excluded zero ordinates form a null set; no pointwise limit1 at such ordinates is asserted.

Combine(QR1),(QR6). Since alpha^−1/2=o(epsilon^(1/3)) for the displayedepsilon, the proposed rate(QR2) follows. The uniform real-height tail and kernel moment are proved before the final norm limit; numerical agreement would not replace them.

## Independent review targets

Check the2/(alpha−1) moment normalization, the exact three-term mass decomposition, the fixed-r decay margin, and the weighted union estimate(QR5). Verify that the logarithmic-derivative source is used away from zero ordinates and never across the zeta pole. The resulting rate is conditional and may have enormous unevaluated thresholds; it is not a practical finite certificate for RH.
