# X-105100 — Critical-residue second-moment replay

Arithmetic class: **EXACT_RATIONAL**

This standard-library replay checks:

- the complete residue balance for a cubic whose \(p'\) and \(p''\) roots are
  rational;
- the balance for an asymmetric quartic with a fully rational two-level
  critical ladder;
- a factor-free Laurent-series recomputation in every degree from two through
  eight;
- translation invariance of the centered ledger;
- complete-root coverage rejection;
- the exact \(x^4-2x^2+2\) debt firewall;
- the exact \(x^3+x+1\) algebraic-versus-absolute nonreal correction;
- LF-normalized content hashes for every load-bearing claim and producer file;
- fail-closed scientific scope flags.

Run:

    python -B experiments/X-105100-critical-residue-second-moment/verify.py \
      --output experiments/X-105100-critical-residue-second-moment/results/verification.json

Then:

    python -B -m unittest discover \
      -s experiments/X-105100-critical-residue-second-moment/tests \
      -p "test_*.py" -v

Expected verdict:

    PASS_T105100_CRITICAL_RESIDUE_SECOND_MOMENT_LEDGER

The replay authenticates exact fixtures and adversarial boundaries. The
universal proof is the Laurent/residue calculation in L-105100. The replay
does not evaluate Xi, justify a canonical-product limit, estimate either
correction, localize the global identity to a height window, prove
RCMV104530, or prove RH.
