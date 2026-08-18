# X-97900 — Logarithmic cubes, top completion, and the activation boundary

Run:

```bash
python3 verify.py --output results/verification.json
```

Expected:

```text
PASS_X_97900_LOG_CUBE_AND_BOUNDARY_ALGEBRA
171f49bf4688d0d54ac53e00e4aaef8d916f7e625beab82ebb47137d8dd1b352
```

The replay uses exact rational arithmetic to check:

- commutation of the additional factor-four scale filter with every Euler factor;
- largest-prime Bellman telescoping;
- the exact top-history completion identity;
- unique ownership of every nonempty top-prime subset;
- collapse of omitted states at terminal endpoints below every omitted prime;
- exact cancellation of the annular base's constant asymptotic coordinate;
- low/corridor/high Bellman budget partition;
- rejection of a mutated top-history coefficient.

The parameter hierarchy scan is diagnostic only. It does not replay the prime
number theorem, Mertens estimates, Rankin tail theorem, upper-bound sieve,
`LSCB67`, `FABP67`, or RH. Those boundaries are explicit in the retained JSON.