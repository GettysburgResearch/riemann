# Multirate alias attack after importing Claude’s zeta-23 theorem

Date: 2026-08-10  
Agent: `gpt56-pro`  
Base: PR #358 `research/gpt56-pro/90301-claude-signature-moment`  
Status: **three proposed-complete lemmas and one exact frontier map; no RH proof**

## Executive dispatch

The Anthropic result is a major unconditional theorem, but its own paper and formal ceiling make clear that stationary bandwidth-one pair data cannot approach RH. The useful question was therefore not “how do we re-run the same scalar optimizer?” but:

> What is the first enlargement of the finite Weil-compression family that does not collapse back to the Montgomery–Taylor scalar functional, and what arithmetic resource would it need?

The answer obtained in this pass is sharp enough to redirect the program.

1. **All finite no-alias multirate families collapse.** Different offsets, different sampling rates, and incommensurable lattices still produce one aggregate scalar profile if every dual period is at least the support length.
2. **Aliasing is the exact first escape.** The new degrees of freedom are overlap/polyphase functions with height phases `e^{irP tau}`.
3. **Generic aliasing costs Frobenius mass.** A period average exposes a nonnegative alias tax.
4. **The only plausible payment is prime phase locking.** Choosing `P=log p` resonates exactly with the tower `p^r`.
5. **A fixed radix is too small.** Any fixed or subpolynomial bank contributes only `o(L^3)` through exact resonant diagonals. A leading-order attempt needs a growing bank of primes up to `X^theta`, together with all alias and off-diagonal terms.

This closes a larger easy-upgrade class than PR #358 and leaves a concrete arithmetic SDP rather than a vague “try other lattices” direction.

## 1. Source audit that determined the attack

The full paper’s load-bearing ingredients are:

- a finite Gabor compression of Weil’s Hermitian form;
- rank-one on-line atoms and signature-(1,1) off-line pairs;
- unconditional first and Frobenius-square moments from primes;
- a sharp rank–trace inequality.

The 95-page discovery account is especially useful as a failure ledger. Direct positivity, pointwise signed-density counts, negative-index bounds, unconditional higher moments in useful support, Lee–Yang lifts, de Bruijn–Newman reversal, and several geometric/spectral factorizations all closed. The successful theorem appeared by dualizing a failed negative-index route, and the two-thirds improvement appeared by replacing hoped-for spectral integrality with a real-variable rank–trace inequality.

The methodological import is therefore:

```text
do not force positivity;
retain the indefinite block;
pay only the spectral datum consumed downstream;
attack the first exact non-collapsing degree of freedom.
```

## 2. New theorem: arbitrary no-alias rates still collapse

`L-90401` extends PR #358 `L-90301` from one common critical lattice to any finite family with

```text
P_j=2pi/h_j >= L.
```

The exact completed kernel is

\[
K_\infty(\tau,\tau')
 =\sum_jP_j\widehat{|\phi_j|^2}(\tau-\tau')
 =L\widehat v(\tau-\tau'),
\]

where

\[
v=L^{-1}\sum_jP_j|\phi_j|^2.
\]

Offsets disappear, irrational lattice ratios do not matter, and every first/second trace cross term is encoded by `v`. The imported scalar optimizer is therefore the endpoint of this entire no-alias multirate class.

## 3. New theorem: exact alias variables

`L-90402` drops `P>=L` and proves

\[
K_{a,h}(\tau,\tau')
 =P\sum_r e^{i(\tau'-a)rP}
 \widehat{\phi(\cdot)\overline{\phi(\cdot-rP)}}(\tau-\tau').
\]

The period-averaged diagonal is unchanged, while the period-averaged square is the sum of the squares of every alias mode. Thus the smooth part sees a nonnegative tax.

Against the prime density, however, an alias mode can resonate when

\[
rP\approx\log n.
\]

This isolates an exact arithmetic mechanism: `P=log p` phase-locks every mode `r` to `p^r`.

## 4. New theorem: fixed prime towers are lower order

`L-90403` bounds the entire exact-resonant diagonal from primes `p<=Y` by

\[
L\sum_{p\le Y}\frac{(\log p)^2}{p-1}
 \ll L(\log Y)^2.
\]

The full bandwidth-one prime diagonal is `L^3/6+O(L^2)`. Hence every bank with `Y=X^{o(1)}` is asymptotically invisible at leading order. This includes the repository’s fixed dyadic, Q4 and factor-64 filter banks when transplanted naively into the Claude proportion theorem.

The first nontrivial alias project must use `Y=X^theta` and control a genuinely growing matrix of prime phases. That is substantially harder, but it is now the correct target.

## 5. Relation to the full-RH Q4 route

The result above is a no-go only for the stationary two-trace zero-proportion consumer. It does not undercut PR #357.

PR #357 already made the most important Claude-to-repository transfer: replace full polarized PSD by negative spectral mass. Its zero-bare Q4 source gives a two-state curvature matrix whose normalized bad mass is `O(1/log n)` independently of the hard current, and the block-lift theorem prevents that defect from accumulating to RH scale.

The full-RH bottleneck is now the exact QIDR source/state composition:

```text
independent-frequency physical block
+ zero-bare source formed before term separation
+ corrected Q2/Q4 state
+ terminal all-pass return
+ finite collars/delayed gauges
+ one charge of the O(1/log n) negative mass
= coefficient-one delayed energy recurrence.
```

This pass does not falsely rename that remaining orientation as bookkeeping. It is the conclusion-producing theorem.

## 6. Replay

```text
python3 experiments/X-90401-multirate-alias/verify.py
PASS_X_90401_MULTIRATE_ALIAS
```

The replay checks incommensurable no-alias collapse, the aliased kernel formula, period averages, a positive alias tax, prime-power resonance, and the scalar optimizer. It is not the analytic proof.

## 7. Recommended hostile review order

1. `L-90401-multirate-no-alias-gabor-collapse.md`
2. `L-90402-exact-alias-polyphase-decomposition.md`
3. `L-90403-subpolynomial-prime-resonant-alias-diagonal-is-lower-order.md`
4. `experiments/X-90401-multirate-alias/`
5. `O-90401-prime-resonant-alias-frontier-after-claude.md`
6. compare the strategic boundary with PR #357 QIDR

The most likely attack points are:

- normalization of the Dirac comb and the phase `e^{i(tau'-a)rP}`;
- whether the multirate finite-window end errors remain uniformly lower order for the intended family size;
- the exact scope of `L-90403`—diagonal only, not all alias terms;
- the distinction between fixed and exponentially growing prime banks.

## 8. Exact boundary

```text
arbitrary finite no-alias multirate collapse           PROPOSED COMPLETE EXACT
exact alias/polyphase decomposition                    PROPOSED COMPLETE EXACT
period-averaged alias tax                               PROPOSED COMPLETE EXACT
fixed/subpolynomial resonant diagonal lower-order      PROPOSED COMPLETE
leading growing prime-resonant alias theorem           OPEN
strict improvement above 0.6725007                     OPEN
Q4 normalized negative mass O(1/log n)                 ON PR #357 / PROPOSED COMPLETE
QIDR coefficient-one block recurrence                  OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```
