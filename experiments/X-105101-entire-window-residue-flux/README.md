# X-105101 — Entire-window residue-flux replay

Arithmetic class: **EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL**

This standard-library replay checks:

- narrow and full windows for \(x^3-3x+1\);
- a partial window in an asymmetric quartic;
- entry and exit of a genuinely nonreal critical pair for \(x^3+3x+1\);
- the algebraic-square versus absolute-square firewall;
- both numerator-removable residue cases;
- the real/nonreal/debt and global/exterior decompositions;
- independent \(V_2,V_4\) reconstruction of each global residue ledger;
- strict finite-segment boundary classification;
- complete, nonduplicated, and correct-kind derivative-root coverage;
- counterclockwise/reversed orientation and sign-killing paired-edge fixtures;
- Schwarz reflection and odd-Q reduction for even and odd sources;
- LF-normalized hashes for every load-bearing source file;
- fail-closed Xi and RH scope flags.

Run:

    python -B experiments/X-105101-entire-window-residue-flux/verify.py \
      --output experiments/X-105101-entire-window-residue-flux/results/verification.json

Then:

    python -B -m unittest discover \
      -s experiments/X-105101-entire-window-residue-flux/tests \
      -p "test_*.py" -v

The replay authenticates exact fixtures and orientation conventions. The
universal proof is the residue/edge calculation in L-105101. The replay does
not perform contour quadrature, evaluate Xi, prove an admissible asymptotic
height/strip estimate, prove RCMV104530, or prove RH.
