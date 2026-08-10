# Integration handoff — Liouville–Bernstein rigidity

Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Base: PR #351 head `22a94f431d7f4cd87db5f3efdd97b086f8f60183`  
Status: exact theorem packet plus finite replay; RH unproved

## Import order

1. `claims/lemmas/L-90201-generalized-von-mangoldt-liouville-extremality.md`
2. `claims/theorems/T-90201-boolean-bernstein-descendant-hierarchy.md`
3. `experiments/X-90201-liouville-bernstein-rigidity/README.md`
4. `experiments/X-90201-liouville-bernstein-rigidity/verify.py`
5. `claims/observations/O-90201-multiplicative-bootstrap-reassessment.md`
6. `reports/gpt56-pro/2026-08-10-liouville-bernstein-rigidity.md`

## Claims changed relative to PR #351

```text
T-90008 ramp lambda-extremality              CONJECTURED -> PROVED EXACT
Form A over H iff lambda slice                CONDITIONAL -> PROVED EXACT
per-exit lambda-extremality                   isolated conjecture -> hereditary descendant theorem
single-flip mechanism                         first layer -> complete mixed hierarchy
2^pi(K) exhaustive class search               replaced by O(K) descendant certificate
T-90009 class-uniformity deficit              scoped to empty lambda coefficient
GFEP / producer empty coefficient              OPEN / RH-BEARING
RH                                              UNPROVED
```

## Cross-PR relationship

PR #355 independently proves positivity of every transported Stieltjes/path
kernel and restores the genuine nonnegative-throughput cut cone. This packet
does not duplicate those proofs and is based directly on the later head of PR
#351. After both are imported, the sparse producer has:

```text
positive packet kernels
+
complete hereditary Boolean derivative hierarchy
+
one remaining empty coefficient.
```

No claim in this handoff depends on merging PR #355 first.

## Validation

```text
python3 experiments/X-90201-liouville-bernstein-rigidity/verify.py
PASS_X_90201_LIOUVILLE_BERNSTEIN_RIGIDITY
```

Remote-byte SHA verification should be repeated after connector upload.
