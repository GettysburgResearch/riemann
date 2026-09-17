# Separated-set lift of the simple-zero proportion

**Proposed complete improvement, pending independent review. RH is not proved.**

The new argument removes the fixed-block loss from the existing seven-point simple-zero method. It gives the proposed unconditional bounds

```
simple AND on the critical line:  >= 0.673058325315610967410539842203...
distinct:                       >= 0.836529162657805483705269921101...
```

These are lower limits of proportions, not a claim about every finite height. The previous 280-block value is 0.673009652279136912.... The numerical improvement is modest; the new ingredient is an all-size spectral-defect theorem, not another decimal optimization over block sizes.

Read [PROOF.md](PROOF.md), especially Sections 2–3 (the new separated/paired decomposition), Section 5 (the complete growing-Gram trace-norm adapter), and Section 6 (the analytic composition). [DEPENDENCIES.md](DEPENDENCIES.md) identifies exactly what is imported. [REVIEW.md](REVIEW.md) names the mathematical checks. [RESEARCH_DECISION.md](RESEARCH_DECISION.md) records how this responds to the criticism of the earlier RH work.

## What is new in this packet

For the actual normalized Montgomery–Taylor kernel Gram G on any r ordered points of span D,

```
tr Psi(G) + D/500 >= (19/5000)(r-6).
```

A sinc-square majorant proves that every 2/3-separated Gram has eigenvalues at most 15/8. A greedy disjoint close-pair removal makes the surviving block separated; each removed pair more than pays the two-point cost in the existing seven-point inequality. Convex spectral pinching completes the proof. The trace-norm adapter retains the finite taper and every omitted grid column, even as the matrix dimension grows.

The seven-point continuum inequality is inherited from `ainta/zeta-simple-zeros` and the repo's independent reviewer-A replay. The stability-enhanced rank inequality is also inherited and rederived with attribution. The unconditional analytic traces and complete outside-zero tail are imported from the primary August 2026 Claude manuscript's Theorem D and its supporting propositions. This packet does not claim those imports as new results or claim an independent rebuild of their full proofs/certificates.

## Bounded replay

Run in this directory:

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py --optimized
```

The checker uses integers and `fractions.Fraction`, with complete alternating-series enclosures for the displayed scalar. It checks only the new finite algebra, matching algorithm, synthetic matrix controls and constants. It does **not** replay the 713,315-node inherited seven-point search, the analytic number-theory input, or any actual zeta-zero census. See [VALIDATION.md](VALIDATION.md).

This is an add-only research packet based on `main@f99d9e3908dde4865377c75d9ca051c1f545bf4f`. It does not alter the beta/branching programme, earlier claims, canonical acceptance, formal sources, workflows or settings. Publication is not mathematical acceptance. No external-priority or world-record claim is made.
