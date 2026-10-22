# Review addendum 105103 — merged-support multiplicity ledger

Review L/T/R/M-105103 against checkpoint base
0c1aedcafe7c6fe384695eee64435cc87b792aea.

The load-bearing review questions are:

1. Are valuation triples taken before cancellation?
2. Are the coefficient indices \(r-m-1\) and \(r+s-2m-1\)?
3. Is every common \(F'/F''\) point processed exactly once?
4. Are simple common \(F,F'\) points excluded from the transferable stratum
   even though their quotient residues vanish?
5. Are the merged corrections added to the signed first carrier and
   subtracted from the second moment?
6. Are algebraic, rather than modulus, squares used off the real axis?
7. Is direct L-104522 transfer withheld exactly when a real critical event is
   multiple/common or another prerequisite fails?

Exact replay:

    python -B experiments/X-105103-confluent-residue-ledger/verify.py
    python -B -m unittest discover \
      -s experiments/X-105103-confluent-residue-ledger/tests \
      -p "test_*.py" -v
    python -B -O -m unittest discover \
      -s experiments/X-105103-confluent-residue-ledger/tests \
      -p "test_*.py" -v

Expected digest:

    e208cceb8b09c639f6587024e5bef334a37d650435453515f68b8f42512c53c2

No Xi numerics or heavy campaign is part of this review.
