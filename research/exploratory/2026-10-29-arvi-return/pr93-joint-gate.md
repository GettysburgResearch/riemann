# PR #93 selected joint count at the PR #94 obstructing bin

**Status:** Source-interface audit and exact scalar comparison; no new zero-free theorem and no proof that the necessary extensions are impossible. Sources are [PR #93 at `70c4d642c4c6263a09bf0f3930a74e2aa7c99f00`](https://github.com/GTimG/QuasiRiemannTracker/tree/70c4d642c4c6263a09bf0f3930a74e2aa7c99f00/submissions/2026-10-28-joint-detector-fine-chain/src/Candidate/Local/Qrh/JointDetector) and [PR #94 at `e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4`](https://github.com/GTimG/QuasiRiemannTracker/tree/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density). The independent obstruction and source references are in [fixed-face-obstruction.md](fixed-face-obstruction.md). Both source proofs are imported, not independently audited here.

The PR #94 blocking bin has zero-location parameter `delta=223/500`, amplitude ratio `p=1/2`, and hence zero level `a=(1+delta)/2=723/1000` and average unsquared amplitude `q=delta*p=223/1000`. PR #94's `ReturnD/PhysicalDirect/SourceSelection.lean` uses amplitude bins bounded by `delta/2` and gives a selected-product squared-response lower exponent `2*q*capacity` less a mesh error. Thus its best guaranteed selected squared-response slope at this bin is `2*q=223/500=0.446`.

PR #93's `FineNaturalSelectedNormContract.lean`, `FineNaturalAggregateSlotNorm`, requires its selected squared-amplitude parameter to be at least `500001/1000000`, strictly above `0.446`. In addition, `FineNaturalCount.lean`, `WholeJointCountOn`, requires `b >= (1+nuMin)/2`; the `AdaptivePrice.lean` `adaptive58` policy fixes `nuMin=29/50`, hence `b >= 79/100`. The blocking bin's `b=a=723/1000` lies below this and also below the separate `b >= 3/4+buffer` hypothesis in the selected count. These are distinct gates. The small mesh loss in PR #94 only weakens its guaranteed squared-response exponent. No direct invocation of the existing PR #93 selected-count theorem is justified at this bin. This does not rule out a stronger selected norm, a count valid at lower zero levels, or a different detector/normalization; those require new proofs and source-interface checks.

As a **hypothetical scalar extrapolation** to theta `43643617/50000000 = 0.87287234`, retain the PR #94 geometry formulas and the limiting `h=0.806`. This theta is outside PR #94's `BoundsN` box, so no existing physical return theorem is asserted there. At the obstructing bin, even granting the full PR #94 physical conductor line, the old C-branch row gap is the exact positive rational

```text
9488573505575711579/2031816416850000000000 ≈ 0.00466999549.
```

Holding the conductor line and all other row terms fixed, an additional valid count branch would need to lower the envelope from `R_C ≈ 0.6093710568` by at least `9488573505575711579/1228233023985825000000 ≈ 0.00772538543`, to at most `122828829151237/204154762500000 ≈ 0.6016456714`, at this single bin. This is a necessary arithmetic condition at the limiting point, not a sufficient condition for global coverage or for an improved region. Varying the physical face or other terms changes the requirement.

Run `python research/exploratory/2026-10-29-arvi-return/check_joint_gate.py` to reproduce the rational comparisons and the hypothetical gap. The equation linking PR #94's amplitude bins to a prospective PR #93 selected norm is a source-interface interpretation; it has not been implemented as a new Lean interface.

The existing PR #93 selected-norm contraction also does not extend to this slope by simply running more iterations. Its scalar recurrence is `e_0=1+delta`, `e_(n+1)=2*delta-1+((1-delta)/delta)*e_n`, so `e_n=delta+((1-delta)/delta)^n`. At `delta=223/500` the multiplier is `277/223 > 1`, and every `e_n >= 1+delta`; the iteration moves away from its fixed point. This is a barrier to that recurrence, not a counterexample to any stronger selected-norm estimate.

An independent agent checked the source definitions of the squared selected slope, the two zero-level gates, and the rational comparison. That review does not establish any extension of the selected norm or the detector count.
