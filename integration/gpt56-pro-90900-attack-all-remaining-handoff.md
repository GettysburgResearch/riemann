# GPT-5.6 Pro attack on the remaining Riemann fronts

Date: 2026-08-11  
Branch: `research/gpt56-pro/90900-attack-all-remaining-fronts`  
Base: `main@3a441dfa2d287b17b22dcd5dbfc0123355ce8232`  
Status: **new exact reductions, quantitative detection theorems, and firewalls; RH remains unproved**

## Deposits

1. `L-90901` scalarises every exterior coefficient of the corrected odd trace-class Weil operator as a fermionic Lenard determinant.
2. `R-90901` proves that no fixed exterior degree, bounded Fredholm/heat range, or fixed Hankel order is a complete positivity test.
3. `L-90902` gives explicit Hankel degree and heat-time bounds detecting any negative eigenvalue, with trace-norm stability.
4. `L-90605` gives the Brownian truncation through order `N^-3` and an all-fixed-order inversion algorithm.
5. `T-90902` gives a direct central filtered-Chebyshev block-energy criterion equivalent to RH, bypassing the incomplete old Q4 state assembly.
6. `L-90903` identifies the safe-Euler resolvent hierarchy as a Gamma/Stieltjes moment transform of the first-Hermite zero-heat family.
7. `L-90904` proves unconditional small-heat positivity and effective compactness in the centre parameter for each first-Hermite slice.
8. `R-90902` proves that absolute-value Chebyshev-error majorants cannot close the first-Hermite sign below RH strength.

## Source heads used

```text
main                                   3a441dfa2d287b17b22dcd5dbfc0123355ce8232
PR #368 odd trace-class operator       023434958a4c115c4d1f7d93ea310716f8bd81ae
PR #376 Brownian Bohr refutation       0ed0e7de3aa1b81bb832df53d861dd6f27f2db8b
PR #362 filtered-Chebyshev Q4          31c57c56c00c0a062a49a126d4e5a68ff28e9fe8
PR #371 Q4 specialist review           fd9292cac2e12e825135b8949b3c3b778f4344d0
PR #378 safe-Euler resolvent            e1d74d60956329486f94c45e26d105608c973397
PR #379 first-Hermite zero heat         589f1c05ccaf248cf08c87fefa7d5ab6d2380708
```

The branch is a cross-route research deposit based on current `main`; it does not merge or inherit review status from those source PRs. Every new analytic claim requires independent review, and none inherits upstream Anthropic Lean status.

## Retained verifier verdicts

```text
PASS_X_90901_FERMIONIC_LENARD_HIERARCHY
PASS_X_90603_BROWNIAN_THIRD_ORDER
PASS_X_90902_CENTRAL_Q4_ENERGY
PASS_X_90903_HEAT_RESOLVENT_UNIFICATION
```

The replays verify finite algebra and numerical identities only. They do not prove any Riemann-data sign inequality or RH.
