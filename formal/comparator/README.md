# Comparator statement lock

The trusted side imports only Mathlib through `ChallengeDeps`. The solution side imports the formal library and must be sorry-free.

The bootstrap topic checks only that the project conclusion is exactly Mathlib's `RiemannHypothesis`. Future topics must expose every mathematical hypothesis explicitly and copy their complete statement-definition closure into the trusted side.

Quick checks:

```bash
cd formal
bash scripts/build_local_comparators.sh
lake env lean comparator/PrintAxioms/RH.lean
```

A full independent comparator run uses `comparator/config-rh.json` and an external `leanprover/comparator` binary.
