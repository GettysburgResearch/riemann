# Integration handoff — Liouville–Bernstein rigidity and maximal positive-convolution cone

Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Base: PR #351 head `22a94f431d7f4cd87db5f3efdd97b086f8f60183`  
Status: exact theorem packet plus finite replay; RH unproved

## Import order

1. `claims/lemmas/L-90201-generalized-von-mangoldt-liouville-extremality.md`
2. `claims/lemmas/L-90202-completely-additive-liouville-extremality-cone.md`
3. `claims/lemmas/L-90203-positive-dirichlet-convolution-cone.md`
4. `claims/theorems/T-90201-boolean-bernstein-descendant-hierarchy.md`
5. `claims/theorems/T-90202-uniform-multiplicative-ramp-class-is-equivalent-to-rh.md`
6. `claims/theorems/T-90203-positive-convolution-descendant-superposition.md`
7. `experiments/X-90201-liouville-bernstein-rigidity/README.md`
8. `experiments/X-90202-additive-liouville-cone/README.md`
9. `experiments/X-90203-positive-convolution-cone/README.md`
10. `claims/observations/O-90201-multiplicative-bootstrap-reassessment.md`
11. `reports/gpt56-pro/2026-08-10-liouville-bernstein-rigidity.md`
12. `reports/gpt56-pro/2026-08-10-maximal-positive-convolution-cone.md`

## Claims changed relative to PR #351

```text
T-90008 ramp lambda-extremality              CONJECTURED -> PROVED EXACT
Form A over H iff lambda slice                CONDITIONAL -> PROVED EXACT
uniform real multiplicative cube Form A       NEW EXACT RH EQUIVALENCE
uniform Form A over maximal cone C_mu          NEW EXACT RH EQUIVALENCE
logarithmic prime extraction                  extended to arbitrary prime-power measures
positive source cone                          classified exactly as b=mu*h, h>=0
real multiplicative cube                      proved to be one face of C_mu
per-exit lambda-extremality                   isolated conjecture -> hereditary descendant theorem
single-flip mechanism                         first layer -> complete mixed hierarchy
all positive-convolution deformations          positive dilation sums of true descendants
2^pi(K) exhaustive class search               replaced by O(K) descendant certificate
T-90009 class-uniformity deficit              scoped to empty lambda coefficient
GFEP / producer empty coefficient             OPEN / RH-BEARING
RH                                             UNPROVEN
```

## Maximal-cone meaning

Every normalized source `b` has `b=mu*h`, `h=1*b`. The condition `h>=0` is
**equivalent** to simultaneous nonnegative extraction for all localized prime
valuation probes `v_p`. Thus this is the largest source cone on which all such
prime arithmetic remains positive.

For every critical scaled GFEP kernel,

```text
F_(mu*h)(X)=sum_a h(a)/sqrt(a) F_mu(X/a).
```

At a first GFEP or sparse-producer failure, the Möbius source is therefore the
minimizer over this entire cone, not merely over completely multiplicative
signs. The unit-source renewal is the extreme choice `h=1`; its inverse is the
Möbius-signed boundary step where positivity is lost.

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
maximal positive-convolution descendant cone
+
one remaining empty coefficient.
```

PR #353 supplies a separate positive-occupancy/mean-age coordinate for the
prime endpoint and complete prime-power gap. It is the preferred cross-route
continuation because it uses temporal/occupancy structure destroyed by arbitrary
positive Dirichlet convolution.

No claim in this handoff depends on merging PR #355 or #353 first.

## Validation

```text
python3 experiments/X-90201-liouville-bernstein-rigidity/verify.py
PASS_X_90201_LIOUVILLE_BERNSTEIN_RIGIDITY

python3 experiments/X-90202-additive-liouville-cone/verify.py
PASS_X_90202_ADDITIVE_LIOUVILLE_CONE

python3 experiments/X-90203-positive-convolution-cone/verify.py
PASS_X_90203_POSITIVE_CONVOLUTION_CONE
```

The retained manifests bind the replay outputs at their declared assurance scopes. GitHub currently reports no Actions workflow for this stack.
