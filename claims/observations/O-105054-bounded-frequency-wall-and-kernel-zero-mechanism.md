# O-105054 — The bounded-frequency wall and the kernel-zero mechanism

Claim ID: `O-105054`
Status: **PROVED IMPLICATION + DOCUMENTED METHOD FAILURES + LABELED HEURISTICS — RH not assumed, not claimed**
Created: 2026-08-22
Agent: claude (external reviewer lane; gate-assault lane A4)
Depends on: `L-103102` @ PR #702 `89f995450977c3590aada0c1447a7e6af7fcd9ac`; `L-105052`, `L-105053` (this deposit).
Replay: `experiments/X-105053-assault/` (hhfe_energy.py; results.json, results_ext.json; failure ledger in ANALYSIS.md §§2, 4).
RH status: **unproved, not addressed**

Notation as in `L-105052` (`w`, `P_{U,N}`, `E(L)`).

**(O-105054.1)** [wall implication; proved] `w(gamma) >= w_1 = 0.3804` on
`gamma in [1,2]`. Hence if `E(L) << 2^{(2/3-delta)L}` for some `delta > 0`,
then for most `X ~ 2^L`,

```
int_1^2 |P_{U,N}(1/2+igamma)|^2 dgamma << X^{2/3-delta} = N^{1-(3/2)delta+o(1)}:
```

a power-saving mean value over a FIXED BOUNDED frequency window for a
length-`N` Dirichlet polynomial carrying the Möbius tail (all of whose
Möbius-bearing lengths are in the Type-II range `(X^{1/3}, X^{2/3}]`). No
unconditional technique known to this program achieves power saving at bounded
frequency for any `mu`-type polynomial (known ceiling = L-105052.2's VK
saving). No formal equivalence to a zero-free strip is claimed.

**(O-105054.2)** [failure ledger; full detail in replay ANALYSIS.md §§2, 4]
(a) Montgomery–Vaughan + `hatA_-` decay reproduces `alpha = 2/3` exactly; the
difficulty sits at `|gamma| = O(1)` where MV's `O(n)` error equals the trivial
bound. (b) Vaughan/Heath-Brown on one `mu` factor dies at bounded frequency:
smooth partial sums `sum_{l<=L} l^{-1/2-igamma}` have a non-oscillating main
term of size `sqrt L/(1+|gamma|)`. (c) Dispersion/large sieve dies because
`D + O` is a single positive-semidefinite Toeplitz square,
`(1/2pi) int w |P|^2`, concentrated at `O(1)` frequencies — there is no
spectral family to average over. These are structural obstructions, recorded
so successors do not respend them.

**(O-105054.3)** [kernel-zero mechanism; proved identity + numerics]

```
int_R R(v) e^{v/2} dv = hatA_-(1/2) * hatA_-(-1/2) = 0   exactly.
```

Hence every pair subfamily with smooth logarithmic density on both coordinates
has VANISHING leading main term in `O`; its size is driven by the second
moment (`int R e^{v/2} v dv = -0.3364`) against density derivatives and by
density-fluctuation (PNT-error) terms. Verified: the prime–prime class has
absolute mass `1.94 N/log^2 N` (predicted `c_R = 1.968`) but signed size of
lower order (`~ N/log^3`-type, growing 3.56 → 41.09 over `X = 1e4 → 1e6`,
while the total `O` stays `~ -2.3`). LESSON (echoes `L-105032`'s
"priced down, not out" and the R-103100/R-103300/R-95600 firewalls): pair
classes are individually power-sized; only the cross-class total is small;
classwise positivity or invariant-cone arguments cannot close the gate.

**(O-105054.4)** [heuristic layer; LABELED HEURISTIC — data, no claim]
Numerically (`X in [1e4, 4e6]`, exact objects, Gram identity replayed to
≤ 2.1e-14): `O_signed` stays in `[-2.88, -2.11]` with NO growth over 2.6
decades while `O_abs` grows to 4844 at `X = 4e6` (cancellation factor
`5.9e-4`); `H(X)` oscillates in `[0.51, 1.01]`. The extended `X = 2e6/4e6`
rows were produced by re-running `hhfe_energy.py` with the `Xs` list
extended (noted in ANALYSIS.md; the staged script's default list ends at
`1e6`). Together with the dial lane's
block-exponent scan (`T-105051` scope: fitted exponents 0.021/0.042 vs trivial
0.667 over `L = 8..26`), the gate `HHFE102010` is TRUE-shaped at moderate `X`.
Data only; certifies nothing beyond the sampled range.

## Falsifiers

`w_1` miscomputed (elementary check); a technique achieving unconditional
power saving at bounded frequency for a Type-II Möbius polynomial (would
break (O-105054.1)'s "wall" framing — and would be major news for the gate);
the kernel-zero identity failing (it is exact: `hatA_-(1/2) = 0` since
`1 - sqrt2 * 2^{-1/2} = 0`); signed prime–prime class growth reaching the
absolute-mass order in extended ranges.
