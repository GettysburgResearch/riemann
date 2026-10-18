# Selected-cardinality moments and a 5/7 sextic zero-density bound

**Status: proposed complete deductions from de Faveri's stated unconditional fixed-order large sieve and the classical Hecke AFE. Independent mathematical review is required. No RH, new individual zero-free half-plane, or critical inverse-Mobius moment is claimed.**

This continuation adds an arithmetic estimate instead of another equivalent RH criterion. The useful change is to retain the number R of exceptional characters INSIDE the mollifier norm, not only in the final Holder factor.

## Principal result

For every fixed n>=6, fixed admissible field/family/twist, and epsilon>0, there is a fixed rho>0 such that

    sum_(Na<=U)^n-free N(3/4,4U^rho,psi chi_a)
       << U^(g_n+epsilon),
    g_n=3(n^2-2n-4)/(n(5n-16)).

N counts zeros WITH multiplicity. Indexing is by full exterior ideal norm; the original nonunit zeros, fixed finite S-supported twists, and complete product columns remain. Height dependence is not optimized and constants are not uniform over n, field degree, or discriminants.

| Fixed character order n | New density exponent g_n |
| --- | --- |
| 6 | 5/7 |
| 8 | 11/16 |
| 10 | 57/85 |
| 12 | 29/44 |

For n=6 the exponent improves the inspected #971 count 395/552 by 5/3864, #966's 43/60 by 1/420, and DF's displayed 8/11 at this threshold by 1/77. Compare at a common sufficiently small polynomial height, not at unproved optimal T dependence. The limit g_n->3/5 changes the character family and the field requirements; it is NOT a route to RH for one fixed L-function.

Read **ZERO_DENSITY.md** for the full proof. At n=6, lambda=7/12, A=U^(5/7), B=U^(8/7), the decisive inequality includes U^(10/21)R^(1/3), rather than replacing the selected mollifier by a full-family bound. The argument solves for R; it does not assume R<=U^(5/7).

## All-fixed-order selected numerator moments

**SPARSE_MOMENTS.md** proves an explicit continuous exponent formula for every fixed moment order 2r, every fixed character order n>=3, and arbitrary selected rows of cardinality <=U^nu. It takes the smaller of RV and K_n(U,V) on each full AFE product dyad, BEFORE the dyads are summed. The actual conductor dyads and negative dual conductor power are retained.

The illustrative selected fourth moment U^(3/4+epsilon) at sigma=3/4, on U^(1/2) sextic rows, improves the same-order full-family comparison. However, its first-mean exponent 9/16 is also obtained from the known full-family eighth moment. We explicitly do NOT count that example as a new gain over the complete higher-moment envelope. Concurrent #976's full-strip hierarchy is credited. The strict new density gain is the selected mollifier estimate and its self-consistent use in the zero detector.

## Replay and review

    python verify.py > /tmp/sparse-checks.json
    cmp CHECKS.json /tmp/sparse-checks.json
    python -O verify.py > /tmp/sparse-checks-O.json
    cmp CHECKS.json /tmp/sparse-checks-O.json
    python run_mutations.py > /tmp/sparse-mutations.json
    cmp MUTATIONS.json /tmp/sparse-mutations.json
    python verify_manifest.py

All code is Python standard library. The tests authenticate finite algebra and report bytes, not de Faveri's theorem, analytic continuation, or asymptotic zero counts. No real L-values or zeros are computed. The same author wrote the proofs and checker. See SOURCES.md and VALIDATION.md before interpreting the word unconditional.

The base is #975 at edbc27b61208ccc7ee1fa99fa3f4e861f5a03452. Only a new standalone directory is proposed. Inherited work and main are not changed.
