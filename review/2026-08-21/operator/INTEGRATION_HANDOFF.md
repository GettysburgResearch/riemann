# Reviewer B integration handoff

Repository: `gfreund123/riemann`  
Review base: `677203992eb0168920365ee45ae9db76bfa97dcf`  
Review branch: `review/2026-08-21/operator-heat-q4`  
Generated: `2026-08-21T12:31:56Z`  
RH: **unproved**

## Integration gate

Do not integrate by PR ancestry. Extract exact mathematical objects only after
Reviewer A reconciliation. This review records 167 claim rows,
30 typed edges, 18 alias rows, 26
refutation rows, and 13 computation records.

```text
PROVEN_ONLY_PATH_TO_RH: false
```

## Highest-value canonical extractions

1. **Mellin–Landau consumer**
   * PR #641 holomorphic-defect lemma only;
   * PR #652 fixed rows `2,3`;
   * PR #653 zero-safe boxes and subpower negative mass;
   * multiplier, positive-real, multiplicity, and fixed-detector firewalls.

2. **Actual-Xi Pick order three**
   * PR #445 determinant factorization;
   * PR #446 reserve allocation and global assembly;
   * repair the corrupt replay and source lock before canonical `VERIFIED`.

3. **Loewner/fractional string**
   * PR #460 exact low-order identities and order-two theorem;
   * PR #461 fixed-order scaling/beta-Hankel law;
   * quarantine the growing-order claim as `GAP_BLOCKED`.

4. **Suzuki/Hardy**
   * imported amplitude embedding;
   * compressed delay/leakage and three-channel colligations;
   * critical Pick-jet identification;
   * all source-conflation and fixed-colligation no-go results.

5. **Heat**
   * canonical fractional uniform-center refutation;
   * Sibuya/difference-Gram and pole-centered signed frontier;
   * separate First-Hermite criterion and unconditional positivity wedge.

6. **Q4**
   * factor-1024 filter and ten-band packet;
   * exact Type-I/II reduction;
   * UOSACF equivalence/filter exhaustion;
   * no empirical scan in the proof graph.

7. **Brownian / Weil / Fredholm**
   * import binding Brownian Bohr no-go;
   * use corrected hyperbolic pole convention;
   * extract fixed-degree Fredholm blindness;
   * keep all conclusion-facing signs open.

## Blocking fixes before extraction

* replace PR #446's corrupt `verify.py`;
* repair its external citation/source lock;
* correct PR #408's margin to `21587/38416`;
* exclude PR #641's moving-row conclusion;
* exclude PR #461's growing-order theorem;
* apply PR #429's normative supersession map;
* exclude the obsolete positive pole model and corrupted `T-90502`;
* preserve semantic aliases for numeric-ID collisions.

See `FIXES.md` for exact dispositions.

## Reconciliation questions for Reviewer A

1. Does Reviewer A agree that PR #641's conclusion changes the fixed detector
   after the hypothetical zero?
2. Are PR #652 rows `2,3` the canonical finite detector family?
3. Does the arithmetic producer supply both fixed rows, one fixed scalar, or
   only a zero-dependent choice?
4. Are signed calibration errors genuinely Mellin-holomorphic in `Re s>0`?
5. Does any arithmetic smoothing multiplier vanish at a possible off-line zero?
6. Is the minimal wavelet critical estimate classified as RH-equivalent?
7. Do Q4/Hermite aliases preserve source type and normalization?

## Live interfaces after integration

| Semantic interface | Status |
|---|---|
| fixed rows/scalar source-faithful positivity | open |
| subpower logarithmic negative mass | open |
| actual-Xi Pick orders >=4 | open / RH-equivalent |
| near-cut all-order Xi string | open / RH-equivalent |
| Suzuki first-chaos domination | open / RH-equivalent |
| theta/Brownian DtN identification | open / RH-equivalent |
| fractional fixed-center signed heat | open |
| First-Hermite constant-four signed cancellation | open / RH-equivalent |
| Q4 SACF/UOSACF | open / RH-equivalent |
| Brownian producer outside Bohr class | absent |
| Weil corrected arithmetic floor | open / RH-equivalent |
| Fredholm all-order prime sign | open / RH-equivalent |

## Verification command

```bash
cd review/2026-08-21/operator/replay
python3 run_all.py
sha256sum -c SHA256SUMS
```

Expected replay verdict:

```text
PASS_REVIEWER_B_ALL_LIGHT_REPLAYS
```

No heavy campaign is part of this command.
