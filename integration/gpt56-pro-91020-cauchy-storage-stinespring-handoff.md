# Handoff — all-order Cauchy storage and generalized-Jordan Stinespring

## Frozen stack

```text
repository: gfreund123/riemann
parent PR:  #396
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
RH status:  UNPROVED
```

## Review order

1. `claims/lemmas/L-91020-all-order-dyadic-cauchy-storage-hierarchy.md`
2. `claims/lemmas/L-91021-generalized-jordan-divisor-stinespring-isometry.md`
3. `claims/theorems/T-91007-coefficient-one-cauchy-storage-rh-criterion.md`
4. `experiments/X-91020-cauchy-storage-stinespring/verify.py`
5. retained result and SHA ledger
6. session report
7. parent files `L-91011/L-91012/L-91013/T-91004`
8. PR #398 control-model firewall

## Dependency DAG

```text
positive sieve cocycle
 -> divisor-splitting probabilities
 -> explicit coassociative isometry V_(a,b)
 -> exact phase and logarithmic coproduct

critical-line Cauchy gate
 -> all-order dyadic storage hierarchy
 -> sharp factor 4^(m+2)
 -> coefficient-one normalized return
 -> stable minimum-phase first innovation Psi_a

V_(a,a) + completed gamma/pole channels + Psi_a
 -> completed source-to-Weil Gram intertwiner     OPEN
 -> coefficient-one recurrence
 -> dyadic Cauchy gate
 -> RH.
```

## Binary rejection tests

Reject or repair this packet if any of the following fails:

1. the base integral identity for `F_0`;
2. the recurrence `W_(m+1)'=W_m-(1/4)W_m(r/4)`;
3. vanishing of integration-by-parts boundary terms;
4. sharpness of `4^(-(m+2))` from the tail coefficient;
5. the spectral-factor modulus identity;
6. the divisor probability normalization;
7. coherent-vector factorization or the shift `s+a` in its second tensor leg;
8. logarithmic coproduct coefficients;
9. noncancellation in the false-RH reverse direction;
10. any attempt to infer the completed boundary map from source positivity alone.

## Exact frontier

```text
all-order storage positivity                EXACT
sharp storage factors                       EXACT
factorial lower-end suppression             EXACT
stable minimum-phase first residual         EXACT
explicit positive divisor Stinespring       EXACT
source coassociativity and log coproduct     EXACT
coefficient-one recurrence criterion        PROPOSED COMPLETE
completed gamma/pole boundary intertwiner    OPEN / RH-EQUIVALENT
Riemann Hypothesis                           UNPROVED
```

## Recommended next attack

Write the completed explicit formula for the causal test `Psi_a` in source-ordered form. The target is an identity, not a norm bound:

```text
completed Weil Gram(Psi_a)
 = source carré-du-champ Gram
   + explicit archimedean square
   + coefficient-one returned state.
```

Any leftover signed boundary term must be displayed explicitly. The control models of PR #398 show that an abstract continuation theorem cannot be substituted for this calculation.
