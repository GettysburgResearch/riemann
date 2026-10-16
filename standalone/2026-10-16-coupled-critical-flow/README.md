# Coupled critical flow: constant remainder, one logarithm, exact Gaussian restoration

**PROPOSED component proofs. The Riemann Hypothesis, the full native generalized moments and the required terminal signed estimate remain unproved. No independent mathematical review or Lean build was performed.**

This continuation of #949 combines the actual weighted 0/1/6 arithmetic source identified in sibling #948 with the positive-compensation mechanism of #946. It does not claim that their previously established conclusions alone compose into RH.

## Main additions

1. **A stronger analytic normalization.** Separating one more explicit powerful Euler factor leaves a product U_6 which is holomorphic and nowhere zero for Re(s)>3/7, with the existing norm-2 exclusions. This is a correction-factor domain, NOT a zeta zero-free region. The general degree-m domain is Re(s)>m/[2(m+1)].
2. **Constant-cost critical remainder and a sharp one-logarithm budget.** Both U_m and its inverse have uniformly bounded absolute coefficient mass at weight 1/2, independent of m. The full comparison kernels cost at most C_F[1+log(T)/m], rather than the earlier log(T)^(12[F:Q]) upper budget. A logarithm is necessary already over Q for unit phases. The field is fixed; no uncontrolled discriminant-uniform constant is asserted.
3. **The actual noncompact Gaussian is handled.** The same-height Gaussian root envelopes compare in both directions with cost C_F[1+log(D)/m]. The entire Gaussian tail is included. This closes the specific compact-to-Gaussian interface left open in #948 and identifies #949's signed detector with the coupled Gaussian ideal sum.
4. **An exact two-channel arithmetic flow.** Randomize PRIME OCCUPANCY once, not the prime exponent. Restoring one prime has cofactor
   V=-(1-1/q)a_p B^(p)(D/q)-b_p q^(m/2-1)B^(p)(D/q^m).
   The same cofactor and physical row occur at both scales. At fourth order the compensation is E|V|^4, including the mixed terms. The positive starting reference is diagonal-sized at every fixed order, uniformly in m; the infinite-prime Gaussian restoration is absolutely well-defined.

## Where the attempted full proof stops

The coupled moment is exactly M=G+I-D, with G already controlled and D>=0. The needed one-sided estimate I-D<=C H X^(k+epsilon) remains OPEN. A direct Holder/Young bound pays only by an uncontrolled sum of intermediate U moments, and therefore does not prove the claim.

For one principal Gaussian source, m=6 and k=2, the scalar estimate I-D<=C_epsilon X^(2+epsilon) would imply the critical Dedekind zero exclusion through the actual Mellin identity. This is an explicit full-proof target without a replica-height loss, not a proof of the target. The original reciprocal L-function survives the new normalization unchanged.

## Read in this order

- [Critical factor, one-logarithm theorem, and Gaussian adapter](CRITICAL_FACTOR_AND_GAUSSIAN.md).
- [Coupled prime flow, full Gaussian convergence, and remaining inequality](COUPLED_PRIME_FLOW.md).
- [Latest-work synthesis and the unsuccessful closure attempt](ATTACK_STATUS.md).
- [Sources and provenance](SOURCES.md), [validation limits](VALIDATION.md), and [exact checks](CHECKS.json).

Reproduce finite checks with `python checks/check_packet.py` and `python -O checks/check_packet.py`; both must match CHECKS.json. `python checks/verify_manifest.py` checks byte identities. These checks do not certify the infinite analytic theorems.

The arithmetic fixtures include all 54 nonzero Eisenstein rows of norm at most 13, but columns are ONLY the allowed 0/1/m ideals in the named three-prime semigroup (norms 7,7,25). The large numerical norm caps are not complete enumerations of all ideals. The diagnostic uses a hard norm cap, not a numerical evaluation of the analytic Gaussian.
