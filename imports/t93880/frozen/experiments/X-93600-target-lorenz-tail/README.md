# X-93600 — Complete Target-Lorenz tail AVLT replay

This experiment certifies the proposed tail theorem `L-93601` on the frozen
`P_61` arithmetic inputs.

The C++ generator:

- enumerates all `2^18` squarefree `P_61` divisors;
- orders every activation event exactly with unsigned 128-bit integers;
- sweeps rows `2,...,66` and every real interval `x>=166000`;
- inserts the analytic `5Y^(-3/2)` Euler-ramp reserve;
- retains the exact first activation strip;
- subtracts a uniform child correction for every `1<=y<67`;
- returns strict margins below the computed minima.

Replay:

```bash
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_COMPLETE_TARGET_LORENZ_TAIL_AVLT
```

The replay authenticates the stated analytic/event-sweep certificate. It does
not independently replay the 702,511,095-cell compact theorem below `166000`,
the common-parent endpoint realization, the endpoint consumer, or RH.
