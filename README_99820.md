# T99820 — Native box normalization audit and Hardy-tail frontier

Status: **reviewable exact mathematics; RH remains unproved**  
Created: 2026-08-20  
Frozen base: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`

## Purpose

Continue the newest active-pair/collar attack, but first enforce the canonical
normalization of the zero-free factor-67 box. The normalized box source has
coefficient `beta(n)/n`, not `beta(n)/sqrt(n)`. Consequently a native prime
step on the normalized potential is

```text
I - p^(-1) U_p,
```

not `I-p^(-1/2)U_p`.

This packet proves the correction exactly, reconstructs the native collar
coefficient, and gives an exact Hardy factorization of PR #659's Cauchy–Poisson
square.

## Main results

1. **Normalization/conjugation theorem.** If `W_67` is the box kernel and
   `phi=W_67/sqrt(.)`, then

   ```text
   (S_67 h)(X)/sqrt(X) = sum beta(n)/n phi(X/n).
   ```

   Equivalently, the unnormalized `p^(-1/2)` step on `W_67` becomes the
   normalized `p^(-1)` step on `phi`.

2. **Binding correction to PR #664.** Its `p^(-1/2)` operator on the normalized
   potential is not the native scalar operator. The claimed annihilation of
   the half-order mode and the unweighted ratio-67 Mertens collar coefficient
   therefore cannot be used in the canonical proof chain.

3. **Correct native collar window.** The `u exp(-u/2)` coefficient is

   ```text
   -3 sum_(exp(u)/67 < n <= exp(u)) beta(n)/sqrt(n).
   ```

4. **Hardy–Cauchy factorization.** For every finite coefficient packet,

   ```text
   Q_tau = |sum c_n|^2
           + 2 tau integral_1^infinity
               |sum_(n>=v) c_n|^2 v^(2tau-1) dv.
   ```

   Hence GPMOC is exactly a nested real tail-square theorem; local owner
   coercivity alone does not estimate its off-diagonal part.

5. **Exact final criterion.** Subpower logarithmic negative mass of the native
   half-order ratio-67 window is equivalent to RH. It is not proved here.

## Replay

```bash
python3 experiments/X-99820-native-box-audit/verify.py \
  --output experiments/X-99820-native-box-audit/results/verification.json
python3 -m unittest discover \
  -s experiments/X-99820-native-box-audit/tests -v
sha256sum -c T99820_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99820_NATIVE_BOX_NORMALIZATION_AND_HARDY_TAIL
```

## Exact boundary

```text
native normalized prime coefficient        PROVED: p^(-1)
PR #664 p^(-1/2) normalized promotion      REFUTED AS NONNATIVE
native one-/two-prime box positivity       PROVED
native collar slope                        HALF-ORDER BETA WINDOW
Cauchy-Poisson square                      EXACT HARDY TAIL SQUARE
window negative-mass criterion             RH-EQUIVALENT / OPEN
Riemann Hypothesis                         UNPROVED
```
