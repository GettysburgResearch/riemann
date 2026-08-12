# Handoff — exact Kreĭn–Langer source/critical/stable/zero-port decomposition

## Frozen scope

```text
repository: gfreund123/riemann
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
claim:      L-91034
control:    R-91005
experiment: X-91025
RH:         UNPROVED
```

## Review order

1. `claims/lemmas/L-91034-krein-langer-cauchy-source-critical-port-decomposition.md`
2. `claims/refutations/R-91005-positive-source-port-identity-does-not-delete-zero-ports.md`
3. `experiments/X-91025-krein-langer-cauchy-port/verify.py`
4. retained result and checksum ledger
5. `reports/gpt56-pro/2026-08-12-krein-langer-cauchy-port-decomposition.md`
6. parent `L-91031`, `R-91004`, `L-91033`, `T-91007`

## Exact dependency DAG

```text
symmetric xi Hadamard product
 -> shifted quotient Theta_a
 -> crossed-pole Blaschke factor B_a
 -> A_a=B_a Theta_a inner

Cauchy stable states
 -> Delta_a=b_a^2 b_(2a)^2 b_(4a)^2 inner

I_a=Delta_a B_a Theta_a inner
 + product rule K_(FG)=K_F+F conj(F)K_G
 -> exact four-term kernel identity

B_a=1 for all a
 <-> no crossed off-line pole at any scale
 <-> RH.
```

## Binary rejection tests

Reject or repair the packet if any of the following fails:

1. the quotient factorization leaves a non-inner outer factor after pole removal;
2. the Blaschke condition for crossed poles is not justified by the zero count;
3. a common numerator/denominator zero is counted as a genuine pole;
4. the product-kernel identity has a missing inner congruence;
5. the deterministic factor does not contain the repeated `a,2a,4a` states;
6. the simple pole port is not exactly
   ```text
   2 Re p /[(z-p)(conj(w)-conj(p))];
   ```
7. the model-space source kernel is silently identified with the Hankel source of `L-91031`;
8. pointwise multiplication is substituted for the actual Cauchy-Weil convolution/intertwiner;
9. source positivity is claimed to force zero-port absence despite `R-91005`.

## Exact boundary

```text
unfiltered source/critical/stable/zero identity   EXACT
common linear-filter preservation                EXACT
explicit stable and zero model-space ports       EXACT
one-pole positivity firewall                     EXACT
RH -> zero-port absence                          EXACT
all-scale zero-port absence -> RH                PROPOSED COMPLETE
arithmetic-Hankel/model-space coisometry          OPEN
actual Cauchy-Weil filter intertwining            OPEN
zero-port exhaustion                              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
