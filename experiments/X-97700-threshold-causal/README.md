# X-97700 threshold-flexible causal decision

The C++ producer uses MPFR 4.2.2 at 256 bits to certify the finite arithmetic
stress cases. The Python verifier checks exact rational owner/resolvent algebra,
the 239-atom odd-history target obstruction, coefficient convolution and the
asymptotic comparison fixtures.

```bash
bash build_and_replay.sh
```

Expected:

```text
PASS_T97700_DIRECTED_FINITE_STRESS_CASES
PASS_T97700_THRESHOLD_FLEXIBLE_CAUSAL_DECISION
```

The replay does not prove `CSHT67` or RH.
