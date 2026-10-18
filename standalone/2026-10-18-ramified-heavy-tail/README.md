# Complete ramified heavy tails, exact moment thresholds, and the still-open native target

**Status: PROPOSED component mathematics, awaiting independent review. No RH proof or new zero-free region.**

The pending twelve-file reflected-ratio packet was already recovered in #978 at `a33d4a9167943d289a4a3ac332a42331d2753e05`. Its entire archive manifest and Git tree were freshly reconstructed and match `a9e1cbeca5b484870d5b511abb59cc75948a4160`; RECOVERY_AUDIT.json records this. This pass did not create that recovery and does not duplicate the packet.

This continuation proves a quantitative result for the ORIGINAL exterior correction H_u, not its inverse, not numerator L-values, and not the native Mobius polynomial. It continues #971's ramified formulas throughout their fixed-margin domain below Re xi=1/2.

Let delta=1/2-Re xi>0 and alpha=1/(3delta). The full sixth-free, full-ideal-norm family has the phase-uniform upper tail

    #{Na<=U: |H_u|>T} <= C U T^-alpha.

Matching lower tails hold in the stated polynomial range after one fixed small-prime enlargement of S. Every fixed real p>0 has the sharp two-sided moment order

    U                        if 3p delta<1;
    U log U                  if 3p delta=1;
    U^((1+3p delta)/2)        if 3p delta>1.

The upper bounds need no extra small-prime exclusions. Lower bounds do: local small-prime zeros cannot simply be ignored. The phases may depend on u arbitrarily within the exact source contract. No independence is introduced.

At Re xi=1/4, the second correction moment is O(U^(5/4)), not the U^(7/4+epsilon) obtained from a full-norm pointwise bound. The fourth has sharp order U^2. The endpoint p=4/3 has a genuine U log U contribution.

The mechanism is a square-core heavy tail. The valuation-two local factor has size q^(3delta)(1+o(1)); its frequency uses q^2 of the norm budget. A positive majorant factors formally through zeta_F^S(s) zeta_F^S(2s-3pdelta) with a summable signed coefficient correction. Its two counting singularities meet exactly at 3pdelta=1. No inverse-zeta continuation is used.

For an arbitrary selected set E of R rows, p<alpha gives

    sum_E |H_u|^p <= C U^(p/alpha) R^(1-p/alpha).

The set may depend on denominator zeros. A correlated Holder corollary is included, with all cardinality costs explicit. It does NOT grant a contour through denominator zeros.

The attempted full-RH continuation remains unsuccessful. #976's all-even theta moments still pay the additive-support Holder factor. A separate tempting short-conductor argument would incorrectly erase the actual metaplectic row phase rho(d), whose primary formula was checked. These are recorded as limitations, not new obstruction theorems or missing routine review steps.

Read PROOF.md for every hypothesis, upper and lower argument, and source distinction. Run `python verify.py` and `python -O verify.py`; both reproduce CHECKS.json. The tests are finite algebra, not an independent proof of the analytic result. SOURCES_AND_VALIDATION.md states the exact coverage and source-access limits.
