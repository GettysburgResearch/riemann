# X-9312 — Positive-node one-scalar extension

This experiment implements the exact finite algebra of L-9314.

Given old moments `a_0,...,a_(2m-2)`, a positive added node `w`, and the one new
scalar `b_0`, the checker reconstructs

```text
a_k = b_(k+1) + w b_k
```

and the exact admissible interval

```text
ell(w) <= b_0 <= u(w).
```

A lower failure emits an explicit square polynomial `q_-^2`; an upper failure
emits an explicit `y q_+^2` witness. The checker uses only integers and
`fractions.Fraction`.

## Files

- `verify.py` — exact recurrence, Schur interval, and witness checker;
- `certificates/synthetic.json` — one positive finite measure plus strict lower
  and upper synthetic violations;
- `results/synthetic-summary.json` — compact digest-bound summary;
- `results/pr103-positive-node-scan.json` — ordinary, non-directed real-data
  reconnaissance and candidate handoff;
- `tests/test_verify.py` — adversarial mutation suite.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output /tmp/positive-node-verification.json
python -m unittest discover -s tests -v
```

The empirical PR #103 scan is deliberately not reproduced by the exact checker:
it requires a special-function backend. It is retained only as a candidate
ledger for a later directed FLINT/Arb pass.

## Candidate handoff

Run direct and reduced directed contractions at exact

```text
x = 1/20, 1, 3, 4, 5.
```

The `x=1/20` row is closest in scale-free boundary position. The `x=5` row has
the smallest raw moat and should be reproduced with a right-half-plane zeta
backend independent of the high-height Riemann--Siegel implementation.
