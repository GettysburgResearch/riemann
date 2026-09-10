# Exact degree-twelve theta ferromagnets; why interactions cannot stay negligible

**Proposed component proofs, pending independent review. RH and the all-order
Ising realization remain open.** This continuation of PR847 adds no canonical
acceptance status and changes no earlier file.

Read [PROOF.md](PROOF.md), then [ATTEMPT.md](ATTEMPT.md). The exact source and
replay boundary are in [SOURCES.json](SOURCES.json) and
[VALIDATION.md](VALIDATION.md).

The main results are:

1. A local Gaussian-reservoir direction preserving the first r even moments
   raises moment 2r+2 with an exact positive derivative. A separate IFT replaces
   a positive Gaussian reservoir with sufficiently many finite small spins.
2. An exact 270-spin model matches the unchanged theta moments 2,4,6,8,10,12.
   There are six positive distinct weight groups (256,10,1,1,1,1). A rational
   preconditioned contraction proves existence, not rounded numerical fitting.
   The same box contains exact models at every common ferromagnetic coupling
   J in [0,10^-100], including a specified strictly positive connected model.
   The independent model misses moment 14 by a certified amount.
3. At the previous 28-spin point, every positive first-order edge perturbation,
   with lower four even moments preserved, moves the tenth moment the wrong
   way. This is a local derivative result, not a general no-go theorem.
4. A tripling inequality for independent sign sums yields a complete numerical
   and analytic separation from the ACTUAL theta law. No independent model
   meets the original IR tolerances at m=256. A successful general ferromagnet
   at that accuracy must have total coupling greater than 10^-24. A two-spin
   ferromagnet explicitly breaks the independent zero-replication rule.

The finite obstruction is not asserted earliest or sharp. It uses three
certified theta Fourier evaluations and analytic Taylor tails, not numerical
moments through 512. It does not imply an off-line zeta zero or disprove RH.
The old all-order programme is still possible for genuinely interacting graphs;
it cannot be finished by repeatedly fitting only independent spins.

Reconstruct the complete source and retained receipt:

```
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
python -I -S -B test_rejections.py --part 1
python -I -S -B test_rejections.py --part 2
```

Add `--optimized` to either refusal-test partition for its optimized replay.
`--emit` is deliberately a producer operation, not package acceptance.
No parent numerical campaign is imported as an unexamined numerical premise.
The interval primitives are adapted from the parent, not an independent backend.
