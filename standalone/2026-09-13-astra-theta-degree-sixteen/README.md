# D16: exact theta moments through degree sixteen

**Proposed computer-assisted component proofs; independent review required. RH
and unbounded-order theta realization remain open.**

This is a target-reaching finite continuation, not another generic infinite
completion. The earlier fourteen-moment interacting realization is extended
by a new independently certified finite model, not an assumed continuation
path from its old parameters.

- 280 spins: independent groups (256,10,1,1,1,1) and five interacting pairs.
- Each pair has the fixed physical coupling J=(1/2)log(3/2), correlation 1/5.
- The exact full theta moments 2,4,6,8,10,12,14,16 match. Odd moments vanish.
- The five pairs carry approximately 19.1163% of the variance at the uncoupled-
  components checkpoint. This is not a negligible coupling ornament.
- A uniformly certified interval also keeps the first fourteen theta moments
  fixed while varying the standardized sixteenth by every delta in [-10^-15,10^-15].
- Adding ANY common pair coupling j in [0,10^-150] to all spin pairs preserves
  these target realizations after exact weight adjustment. For j>0 the finite
  graph is connected, with 39060 positive edges. This interval is conservative.
- The standardized eighteenth-moment discrepancy stays in (0.169,0.170).
  The model is therefore NOT Xi.

The parameters are roots in a specified rational box. Printed approximate
weights are not substituted for the exact root. `primitive.py` reconstructs
normalization and theta moments through eighteen from all required source
integrals and complete remainders. No stored moment table is a numerical input.

## Reading and replay

Read `PROOF.md`, then `RESEARCH_NOTE.md`, `SOURCES.json`, and `VALIDATION.md`.
The accepting commands are

```sh
python -I -S -B certify.py --check result.json
python -I -S -B -O certify.py --check result.json
python -I -S -B test_rejections.py --part 1
python -I -S -B test_rejections.py --part 2
python -I -S -B test_rejections.py --part 1 --optimized
python -I -S -B test_rejections.py --part 2 --optimized
```

`--emit` is producer-only. It does not authenticate a published package.
The exact code checks the finite certificate, not the truth of RH or the
infinite analytic theorems in the wider repository. The general weighted
Lee--Yang theorem is classical and explicitly imported for the connected
model; the disconnected product's zero geometry has an elementary proof.

Suggested publication: add this directory on a new branch from #880 head
2398203ec171d9cbaac73acc62e1a643757f0a35, preserving current branch additions.
Do not edit main or earlier research packets. The external delivery receipt
records the actual publication status; this README is not a push receipt.
