# X-105103 — Confluent residue ledger verification

This lightweight exact replay verifies L/T/R/M-105103.

It checks:

- the finite Taylor-division recurrence for \(P=F/F'\) and
  \(Q=F^2/(F'F'')\);
- full principal parts at higher-order poles;
- a unique merged support for common \(F'/F''\) points;
- exact reconstruction of the simple noncommon real stratum;
- reversed-series residue-at-infinity oracles;
- the independent frozen \(V_2\) and \(V_2,V_4\) polynomial ledgers;
- shift/scale invariance, algebraic nonreal squares, pole-order, zero-residue,
  sign, and transfer firewalls;
- the frozen T-105102 dependency.

Run from repository root:

    python -B experiments/X-105103-confluent-residue-ledger/verify.py
    python -B -m unittest discover \
      -s experiments/X-105103-confluent-residue-ledger/tests \
      -p "test_*.py" -v
    python -B -O -m unittest discover \
      -s experiments/X-105103-confluent-residue-ledger/tests \
      -p "test_*.py" -v

Expected verdict:

    PASS_T105103_CONFLUENT_RESIDUE_LEDGER

Expected proof digest:

    e208cceb8b09c639f6587024e5bef334a37d650435453515f68b8f42512c53c2

The replay uses standard-library rational and Gaussian-rational arithmetic
only. It performs no Xi evaluation, zero scan, numerical contour quadrature,
broad test suite, or heavy computation.
