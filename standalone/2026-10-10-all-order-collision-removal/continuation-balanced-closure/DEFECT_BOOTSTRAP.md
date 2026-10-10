# Quantitative target: a fractional defect improvement can be bootstrapped

**Status:** conditional deductions and a precise open target. No fractional defect saving is proved here. The balanced-closure theorem is unconditional as a norm comparison; all zero-free consequences in this file retain their explicit arithmetic hypotheses.

## 1. The actual first saving to seek

The sibling PR #913 states a conductor-uniform consequence of a common zero-free boundary beta and its imported inverse second moment:

    sum_(Nu<=H) |A_u(D)|^(2k) << H D^(1+2(k-1)beta+epsilon).

This is used here as an explicitly imported baseline, not independently reverified. It also follows directly from the corresponding uniform pointwise bound and second moment by multiplying |A|^(2k-2) into |A|^2. Its defect above H D^k is

\[
 \lambda_k^{\mathrm{old}}=(k-1)(2\beta-1).
\tag{1.1}
\]

At H=D^h, the predecessor's exact extraction gives a new boundary below beta precisely when

\[
 \lambda+5h/6<k(2\beta-1).
\tag{1.2}
\]

Writing lambda=lambda_k^(old)-eta, the condition becomes

\[
 \eta>5h/6-(2\beta-1).
\tag{1.3}
\]

At beta=7/8 and the limiting h=1, this is eta>1/12. For the fourth moment, the inherited defect is 3/4 and the useful threshold is strictly below 2/3. Thus the first objective is a saving slightly larger than D^(1/12) relative to that imported baseline, not necessarily the optimal defect zero. This quantitative comparison improves on the cruder second-moment-plus-trivial-bound starting point in the first packet; it does not prove the saving.

The balanced-closure theorem shows that this improvement may be sought just for the balanced, fixed-exclusion polynomial, with its stated full-row and fixed-cutoff quantifiers.

## 2. A reusable fractional improvement would imply RH

Here is a different sufficient architecture from demanding sublinear defects in a single pass. Let a family of finite-order Hecke L-functions be closed under the twists used by the row construction and under duality. Suppose a common zero-free boundary 1/2<beta0<1 is available. Fix 0<=r<1 and h>0.

Assume the following **new arithmetic transfer theorem**, which is not proved: whenever the family has a common boundary beta>1/2, an unbounded sequence of fixed orders k satisfies the full-row balanced hypothesis of BALANCED_CLOSURE.md Theorem 4.1 with

\[
 \lambda_k\le r(k-1)(2\beta-1),
\tag{2.1}
\]

for every target and required smooth test. Constants and chosen cutoffs may depend on beta and k; h is fixed (a sequence h_k=o(k) also suffices).

### Proposition 2.1. Fractional-defect bootstrap

Under these hypotheses, the family satisfies its critical-line conclusion.

**Proof.** Balanced closure supplies the corresponding actual moments. At one fixed valid beta their extracted boundaries are at most

\[
 \frac12+r(1-1/k)(\beta-1/2)+\frac{5h}{12k}.
\tag{2.2}
\]

For any fixed zero strictly right of 1/2+r(beta-1/2), choose a finite k from the unbounded sequence large enough to place (2.2), with its remaining arbitrarily small loss, to the left of that zero. This is a contradiction. Hence beta'=1/2+r(beta-1/2) is a valid new common boundary. If r=0 this already gives the conclusion. Otherwise apply the hypothesized transfer theorem again at beta'. Repetition gives beta_j=1/2+r^j(beta0-1/2), which tends to 1/2. Any fixed off-line zero is excluded after finitely many steps and finitely many moment choices. Duality reflects the other side of the strip. No bound uniform as k tends to infinity is used. QED.

The input (2.1) still has a defect linear in k at every positive distance from the critical line. It is logically sufficient because the same *relative* improvement is assumed to remain available after each common-boundary improvement. This stability is an essential new hypothesis, not an inference from one estimate at beta0.

For illustration only, r=7/8 at beta=7/8 asks at order four for lambda=21/32. The extracted limiting boundary is 335/384, below 7/8 by 1/384. If the hypothesized improvement held at unbounded orders, the first limiting update would be 53/64, followed by further updates. None of these numbers is a newly proved zero-free bound.

## 3. Why a single fourth moment does not automatically tensorize

A fourth-moment improvement and the old uniform pointwise bound only give

    sum |A|^(2k) <= (max |A|)^(2k-4) sum |A|^4.

The resulting defect is (k-2)(2beta-1)+lambda_2. Its saving relative to (1.1) is the fixed number (2beta-1)-lambda_2, not a positive fraction of the k-dependent defect. Holder alone therefore does not provide (2.1) at unbounded orders. Genuine joint arithmetic control remains necessary.

The present continuation supplies the balanced-only norm reduction, exact Euler-source analysis, and these quantitative targets. It does not claim the full balanced estimate, a first new numerical boundary, or the missing reusable fractional-defect theorem.
