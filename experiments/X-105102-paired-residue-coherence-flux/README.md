# X-105102 — Paired residue-coherence flux replay

Arithmetic class: **EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL**

This lightweight replay checks:

- local and exterior first-residue ledgers;
- independent \(V_2\) reconstruction of global first charges;
- exact pairing with the frozen L-105101 second-moment producer;
- a positive-coherence real cubic and a unit-coherence one-point window;
- complete cancellation by a nonreal first-residue correction;
- a common parent/critical numerator-removable event;
- pointwise thin-strip elimination of both nonreal corrections;
- a negative first moment that is killed by the positive part;
- positive formal coherence withheld by failed endpoint and common-zero
  transfer hypotheses;
- the \(x^5-x^3+x\) false-carrier firewall;
- the \(x^4-2x^2+2\) sub-threshold coherence firewall;
- an integrated sign oracle for both \(F/F'\) and \(F^2/(F'F'')\);
- fail-closed root coverage, boundary, dependency, and scientific-scope
  checks.

Run:

    python -B experiments/X-105102-paired-residue-coherence-flux/verify.py \
      --output experiments/X-105102-paired-residue-coherence-flux/results/verification.json

Then:

    python -B -m unittest discover \
      -s experiments/X-105102-paired-residue-coherence-flux/tests \
      -p "test_*.py" -v

The replay performs no Xi evaluation, zero scan, floating-point contour
quadrature, or heavy campaign.
