# GCP26 — sharp grounding cost in the arithmetic divisor graph

**Proposed component proofs, independent review pending. Not a complete RH proof.**
This packet is a post-integration synthesis of selected proofs on #803, #819,
#825 and #826, with #812/#827 at metadata depth and older source context retained.
It does not claim to review every recent packet or confer acceptance on its sources.

The new theorem concerns the literal harmonic prime-power graph, on squarefree
primorial supports and on all exponent depths over a fixed finite prime set.
Its centered spectral gaps are absolute constants, yet the optimal cost of
anchoring at the integer 1 grows as

* (1/zeta(2)) log log P + O(1) for squarefree primorial supports;
* log log P + O(1) for the unbounded-exponent reservoir.

This proves the log-log order of the ANCHORED part of #825 is unavoidable,
even though it need not be necessary for the CENTERED gap. It supplies exact
root-contrast and grounded-resolvent formulas, as well as an exact coherent
Schur test. It does not identify that graph or root coupling with the full Xi
source, bound the residual minima, or set the intrinsic BSY defect to zero.

Read **PROOF.md**, then **SYNTHESIS_AND_ATTEMPT.md**. All needed one-prime
spectral formulas and elementary prime-product estimates are reconstructed.
The asymptotic theorem uses no PNT, RH, zero data or special-function computation.
Classical reversible-chain spectral/capacity theory is credited.

At prime cutoff 13, directed arithmetic gives:

| Reservoir | Optimal root-contrast energy constant G | Optimal anchored constant C |
|---|---|---|
| Squarefree, 64 vertices | (1.18532285971072, 1.18532285971074) | (1.91594153472685, 1.91594153472687) |
| All exponents, six primes | (1.82250119177775, 1.82250119177777) | (2.37221708831717, 2.37221708831720) |

The infinite-exponent result uses its proved spectral reduction to 63 visible
nonconstant modes. It is not an enumeration of infinitely many states or an
independent machine proof of that reduction. These are graph constants, not
zeta values, zeta zeros, or RH-facing approximation errors.

Reproduce from this directory:

```
python -I -S -B validate.py
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B test_rejections.py --optimized
```

Main and all predecessor packets are unchanged. The remaining full proof
requires a source-preserving comparison AND control of the retained channel;
neither is silently assumed by this packet. See the synthesis for the exact
failed composition and the source-pinned handoff questions.
