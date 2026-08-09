# Long-pass checkpoint — Q4 two-state reflected ledger

Status: **RH UNPROVED.** This report preserves the exact progress and the firewalls from the long continuation on PR #341.

## Durable new results on this branch

The branch now contains `L-34007`--`L-34009` in addition to `L-34001`--`L-34006`.

1. `L-34007` proves that the adaptive critical-Haar root-of-unity source bank has only two inverse-source boundary/current Fourier modes. For `B_omega=(1-omega u)B`, `u=sqrt(2)2^{-s}`, the normalized DFT is
   ```text
   Bhat_0=B, Bhat_1=-uB;
   qhat_0=q, qhat_1=u((log 2)B-q);
   that_0=t,
   that_1=u(-t+2(log 2)q+(log 2)^2 B),
   that_k=2(log 2)^2 u^k B, k>=2.
   ```
   Because the bare-source DFT has support only in modes 0 and 1, every `k>=2` second-current mode disappears exactly from the source-convolved reflected individual terms. The adaptive reflected boundary therefore has fixed state dimension two, independent of the number of positive generalized-prime channels used to diagonalize the arithmetic forcing.

2. `L-34008` proves an exact two-state source-curvature splitting. For
   ```text
   C_B=||q||^2-Re<B,t>,
   ```
   the critical-Haar detail state has
   ```text
   C_detail=C_B+2(log 2)^2||B||^2.
   ```
   Thus channel-averaged source curvature is one current-scale state plus one unit-amplitude predecessor state and a positive deterministic bare-source square.

3. `L-34009` proves that the complete product and individual reflected blocks are also exactly two-state. Removing the common unit delay from the detail mode,
   ```text
   Btilde=-B,
   qtilde=(log 2)B-q,
   ttilde=-t+2(log 2)q+(log 2)^2B.
   ```
   The exact reflected difference is
   ```text
   P_det-I_det=2||q-(log 2)B||^2.
   ```
   Root-of-unity averaging therefore yields a current-scale base block plus one predecessor detail block and no higher dynamic source states.

These identities materially reduce the final reflected-dissipation problem: adaptive channelization may use arbitrarily many positive arithmetic forcing channels without increasing the dynamical inverse-zeta state dimension beyond two.

## Other exact closures retained from the same continuation

- `L-34001`: physical/carry Jordan placement for the full Q4 deformation; physical current and second current are exactly the corresponding carry jets.
- exact inverse-source curvature cancellation: `A + (1/2) product-curvature = R + 2Q^2`.
- `L-34002`: PNT + four-adic renewal gives the historical current/full-quadratic-reserve ratio `->0` (not the critical-scale innovation theorem).
- `L-34003`: continuous source-complete augmented reserve is positive cofinally in actual real-X carry coordinates.
- `L-34004`: terminal all-pass Jordan state has nonnegative cofinal curvature.
- `L-34005`: every adverse compact-source fixed endpoint child `r=1,2,3` has only `O(log n)` current forcing.
- `L-34006`: the radix-four reserve increment is an exact relative Jordan log-curvature.

## Firewalls discovered / retained

Several tempting shortcuts were deliberately not promoted:

1. The compact current is not prime-free. Its aligned innovation contains the genuine Chebyshev radix-four fluctuation; the earlier prime-free formula is withdrawn on PR #329 `L-32305`.
2. A generic positive curvature or large Kummer reserve is not an upper bound for the reciprocal-zeta current. The direction/sign in the reflected identity remains load bearing.
3. Raising the scalar Q4 inner factor to powers does not close the problem: PR #325 `R-32404` gives an exact row `(8,4)` failure already at power two.
4. The direct pointwise current/reserve inequality remains RH-strength. Finite scans are discovery only.

## Cross-branch advances incorporated conceptually

Concurrent live work supplies important complementary pieces:

- PR #346: exact compact-current parity jet frame and deterministic odd-prime reserve increment `Theta_eta(n log n)`.
- PR #329: one matching augmented parity curvature absorbs the complete parity current/bare jet with no double spending.
- PR #342/#345: exact compact Q4 innovation and coefficient-one normalized recurrence reduction.
- PR #325: root-of-unity/critical-Haar forcing separation with frame constants independent of channel count.
- PR #349: repair of the odd-relative bare charge/orientation; any future composition must import the repaired version rather than stale formulas.

## Exact remaining theorem

The remaining Q4 theorem is now a fixed **two-state reflected dissipative orientation / upper recurrence** problem, not a source-placement or channel-proliferation problem.

One must prove, from the complete source-convolved independent-frequency ledger, that the separated generalized-prime reserve enters with dissipative sign so that the current-scale principal state plus the unit-amplitude predecessor detail state satisfy a coefficient-one delayed upper recurrence, modulo the already-controlled fixed collars and deterministic bare-square gauges.

Equivalently, one needs an upper/delayed law for the positive compact/odd relative augmented curvature that forces the RH-sensitive current innovation to have at most `n log^A n` scale.

No generic PSD, Cauchy, PNT, or finite-scan argument supplies this. The surviving mode is exactly the reciprocal-zeta mode.

## Status

```text
Q4 physical/carry source placement          proposed complete exact
adaptive inverse-source state dimension=2   proposed complete exact
adaptive source-curvature state dimension=2 proposed complete exact
complete reflected product/individual ledger=2-state proposed complete exact
endpoint/terminal bookkeeping               proposed complete/cofinal
reflected dissipative upper recurrence       OPEN / RH-bearing
Riemann Hypothesis                           UNPROVED
```
