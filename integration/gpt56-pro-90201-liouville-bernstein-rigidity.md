# Integration handoff — Liouville rigidity, near-square-root frozen-policy refutation, and uniform Pascal pivot

Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Base: PR #351 head `22a94f431d7f4cd87db5f3efdd97b086f8f60183`  
Status: exact theorem/refutation packet plus directed replays; RH unproved

## Import order

1. `claims/lemmas/L-90201-generalized-von-mangoldt-liouville-extremality.md`
2. `claims/lemmas/L-90202-completely-additive-liouville-extremality-cone.md`
3. `claims/lemmas/L-90203-positive-dirichlet-convolution-cone.md`
4. `claims/theorems/T-90201-boolean-bernstein-descendant-hierarchy.md`
5. `claims/theorems/T-90202-uniform-multiplicative-ramp-class-is-equivalent-to-rh.md`
6. `claims/theorems/T-90203-positive-convolution-descendant-superposition.md`
7. `claims/lemmas/L-90204-euler-fragmentation-mellin-factorization.md`
8. `claims/lemmas/L-90205-fragmentation-increment-renewal-and-continuation.md`
9. `claims/lemmas/L-90206-fragmentation-characteristic-has-no-spectral-gap.md`
10. `claims/lemmas/L-90207-nonreal-mellin-resonance-forces-integer-sign-oscillation.md`
11. `claims/refutations/R-90201-frozen-gfep-exit-and-producer-eventual-positivity-fail.md`
12. `experiments/X-90204-certified-fragmentation-resonance/README.md`
13. `claims/lemmas/L-90208-finite-atomic-no-gap-and-uniform-pascal-resonance-free.md`
14. `claims/lemmas/L-90209-two-low-row-zero-safe-volterra-bridge.md`
15. `experiments/X-90205-policy-dichotomy-lowrow-bridge/README.md`
16. `claims/observations/O-90201-multiplicative-bootstrap-reassessment.md`
17. `reports/gpt56-pro/2026-08-10-certified-fragmentation-resonance-and-policy-dichotomy.md`
18. earlier reports and `X-90201..X-90203` support packages

## Claims changed relative to PR #351

```text
T-90008 ramp lambda-extremality                 CONJECTURED -> PROVED EXACT
Form A over H iff lambda slice                   CONDITIONAL -> PROVED EXACT
uniform real multiplicative cube Form A          NEW EXACT RH EQUIVALENCE
uniform Form A over maximal cone C_mu             NEW EXACT RH EQUIVALENCE
positive source cone                             classified exactly as b=mu*h, h>=0
all nonempty class directions                     proper-descendant arithmetic
Euler/source versus fragmentation geometry        exact Mellin factorization
frozen binary-ternary continuation                 meromorphic through RH-facing strip
finite-atomic stationary policy gap                IMPOSSIBLE GENERICALLY
fixed GFEP coordinate Sigma_(N,2)(2)                TWO-SIDED EXCURSIONS TO X^(0.49657-)
frozen producer A_N(2)                              TWO-SIDED EXCURSIONS TO X^(0.49657-)
frozen producer pointwise positivity                REFUTED
frozen BTF absolute variation                        REFUTED NEAR SQUARE-ROOT SCALE
GFEP-full                                            REFUTED
uniform Pascal deterministic resonance               ABSENT / EXPLICIT TRANSFER
low-row SHARP and critical-log criteria               SAME ZERO-SAFE SOURCE
signed pairing / Cycle Debt                           NOT REFUTED
RH                                                      UNPROVEN
```

## Certified near-conservation resonance

The characteristic

```text
Delta(u)=1-1/2[2^(1-u)+3^(-u)+(3/2)^(-u)]
```

has exactly one simple zero in the radius-`1e-18` disk around

```text
0.9965737487663334042655023867051966592...
+108.6843160063763813085769124318175668569... i.
```

Directed numerator margins are

```text
|N_exit|     > 0.00987978337,
|N_producer| > 0.00199031875.
```

After shifting by `1/2`, the physical Mellin pole has real part exceeding

```text
0.496573748766333403.
```

`L-90207` transfers it to integer endpoints and proves both positive and negative parts are not `O(N^delta)` for any smaller `delta`.

This refutes the frozen policy's antecedents, not their downstream RH consumers.

## Policy dichotomy

Every finite atomic stationary characteristic

```text
Delta_nu(u)=1-sum_j b_j v_j^u,
sum_j b_j v_j=1
```

has nonconservation zeros with real parts approaching one. The uniform continuum split instead has

```text
Delta_unif(u)=(u-1)/(u+1).
```

Its exact discrete analogue, the uniform internal Pascal chain, has explicit hitting law and deterministic factor

```text
A_n(u)=n^(1-u)+(2-n)(n+1)^(-u)+2/(n+1) zeta(u,n+2),
```

with no deterministic nonreal poles. This selects uniform Pascal/SHARP as the canonical resonance-free fragmentation front.

## Two-row route

The uniform-Pascal critical-log scalar

```text
S(X)=5c_X(2)+3c_X(3)
```

and the two-low-row SHARP hinge scalar use the same arithmetic source

```text
omega=(epsilon-delta_2)*(2epsilon-delta_2)*mu.
```

In logarithmic time,

```text
S(e^t)=2H(e^t)+integral_0^t H(e^u)du.
```

Both have a zero-safe reciprocal-zeta numerator. Full SHARP is much stronger than the actual two-row RH consumer.

## Cross-PR status corrections

- PR #292: `GFEP` is no longer an open positivity conjecture; it is refuted by a fixed oscillatory coordinate.
- PR #247: pointwise frozen producer positivity and BTF absolute variation are refuted; the weaker signed pairing estimate remains live.
- PR #355: its positive Stieltjes packets and genuine cut-cone theorems remain correct; their empty coefficient is now known to oscillate for the frozen policy.
- PR #351: the multiplicative class is free, but the frozen GFEP hinge itself is false.
- PR #353: the prime-endpoint positive-occupancy route is unaffected and becomes a higher-priority front.
- PR #329/#335: the uniform Pascal/SHARP route is unaffected and is now singled out by the resonance classification.

## Validation

```text
python3 experiments/X-90201-liouville-bernstein-rigidity/verify.py
PASS_X_90201_LIOUVILLE_BERNSTEIN_RIGIDITY

python3 experiments/X-90202-additive-liouville-cone/verify.py
PASS_X_90202_ADDITIVE_LIOUVILLE_CONE

python3 experiments/X-90203-positive-convolution-cone/verify.py
PASS_X_90203_POSITIVE_CONVOLUTION_CONE

python3 experiments/X-90204-certified-fragmentation-resonance/verify.py
PASS_X_90204_CERTIFIED_FRAGMENTATION_RESONANCE

python3 experiments/X-90205-policy-dichotomy-lowrow-bridge/verify.py
PASS_X_90205_POLICY_DICHOTOMY_LOWROW_BRIDGE
```

The resonance verifier uses exact Fractions, 70-digit directed complex intervals, a Rouché disk, and analytic infinite-tail bounds. GitHub currently reports no Actions workflow for this stack.
