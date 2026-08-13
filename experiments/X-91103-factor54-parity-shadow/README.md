# X-91103 — Factor-54 positive parity-shadow certificate

Companion replay for `L-91109`.

```bash
python3 experiments/X-91103-factor54-parity-shadow/verify.py
```

Expected verdict:

```text
PASS_FACTOR54_POSITIVE_PARITY_SHADOW
```

The checker uses only the Python standard library and verifies with exact
`Fraction` arithmetic plus directed rational square-root enclosures:

- every Hall prefix for the reserve transport `e <= o`;
- every Hall prefix for the equality transport `e <= o+1`;
- strict uniform margins above `0.39` and `0.11`;
- the complete even/odd squarefree support through the reset window;
- the sixteen primes at most `53` and the exact `1/59<c_0` contraction;
- the least-prime parity recursion on a finite combinatorial replay.

The certificate proves the finite-window positive transport geometry only. It
does not provide the divisor-capacity lift, the endpoint reset recurrence, or
RH.
