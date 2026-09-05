# X-105104 — Jet-coherence reverse--Rolle verification

This lightweight exact replay verifies L/T/R/M-105104.

It checks:

- arbitrary-multiplicity critical-node zero-count identities;
- fail-closed authentication of each supplied critical manifest against a
  separately frozen expected manifest;
- common parent multiplicity and active-component accounting;
- the odd-turn leading-principal-part sign dictionary;
- global and componentwise jet-coherence lower bounds;
- the exact derivative multiplicity-defect decomposition;
- recovery of the simple residue theorem;
- flat-good, flat-wrong, common-only, and even-stationary fixtures;
- the \(x^6\pm1/64\) ordinary-residue no-go pair;
- the frozen T-105103 dependency.

Run from repository root:

    python -B experiments/X-105104-jet-coherence-reverse-rolle/verify.py
    python -B -m unittest discover \
      -s experiments/X-105104-jet-coherence-reverse-rolle/tests \
      -p "test_*.py" -v
    python -B -O -m unittest discover \
      -s experiments/X-105104-jet-coherence-reverse-rolle/tests \
      -p "test_*.py" -v

Expected verdict:

    PASS_T105104_JET_COHERENCE_REVERSE_ROLLE

Expected proof digest:

    bcd3ac0f644c49e47be6b2e019a57b2e7d2b8b6df14dfec97da854cb44b3bed6

The replay uses standard-library rational arithmetic only. Its bounded
combinatorial certificate checks 141 sign patterns through eight turns. It
performs no Xi evaluation, zero scan, floating-point root finder, numerical
contour quadrature, broad suite, or heavy computation.
