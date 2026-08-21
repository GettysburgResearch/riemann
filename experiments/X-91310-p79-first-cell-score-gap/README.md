# X-91310 — Exact `P_79` first-cell score audit

This replay performs four independent checks against the direct-Euler factor-54 proposal.

1. It enumerates the 51 squarefree divisors of `P_79` through `83` and proves exactly that
   
   ```text
   A_P79(83) < 0.
   ```

2. At the admissible splice `p=83`, `y=1`, it proves exactly that
   
   ```text
   score residual - target residual < 0.
   ```

   This refutes the positive surplus claimed in `L-91351.11` and `T-91304.5`.

3. It uses rational square-root enclosures and exact atanh logarithm truncations to prove
   
   ```text
   residual target < 1.813,
   single n=2 physical-entropy atom > 1.825.
   ```

   Thus the scalar counterexample is not itself a physical component-entropy obstruction.

4. It streams all `2^22 = 4,194,304` reciprocal-prefix activation states and proves
   
   ```text
   A_P79(x) < 1/5 for every x >= 83,
   ```

   with the exact maximum attained at the activation `x=221`.

Run:

```bash
python3 verify.py
```

Expected output:

```text
PASS_P79_FIRST_CELL_SCORE_REFUTATION_AND_ENTROPY_REPAIR
```

The replay uses only the Python standard library.  It does not prove the global physical-score recurrence or the Riemann Hypothesis.
