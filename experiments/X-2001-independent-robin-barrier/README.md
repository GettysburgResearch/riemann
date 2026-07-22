# X-2001 — Independent Robin finite-barrier verification

Experiment ID: X-2001  
Agent: `gpt56-03-b`  
Issue: #20  
Status: PROPOSED certified computation; independent review pending  
Base contribution: PR #19, T-0201, X-0202

## Research question

Can the exact finite maxima and transcendental signs used by T-0201 be reproduced without importing X-0201/X-0202's divisor-sum sieve or Decimal transcendental engine?

## Result

Yes. The committed verifier independently reproduces:

- the unique maximum `403/105` at `5040` on `[1,5040]`;
- the unique maximum `224/65` at `5460` on `[5041,5582]`;
- a strict positive sign at `5041` against `224/65`;
- a strict positive sign at `5583` against `403/105`;
- exact containment of both new intervals inside the committed X-0202 intervals.

It also adds a new adjacent check:

- `e^gamma log log(5582) - 403/105 < 0`;
- `e^gamma log log(5583) - 403/105 > 0`.

Thus `5583` is the sharp first integer crossing of the record threshold.

No Robin counterexample was found.

## Independence boundary

This implementation deliberately does **not** import X-0201 or X-0202 code.

| Component | X-0202 | X-2001 |
|---|---|---|
| `sigma(n)` | divisor-addition sieve | fresh trial-division factorization for each `n` |
| ratio comparison | exact integers | exact integers, independently implemented |
| logarithm | CPython Decimal `ln` | positive atanh series with rational tail |
| Euler's constant | Decimal harmonic bound | dyadic harmonic bound from L-2002 |
| exponential | CPython Decimal `exp` | positive Taylor series with geometric tail |
| interval representation | directed decimal | integer endpoints over `2^B` |

The only imported data are the published X-0202 decimal endpoints, parsed as exact finite rational numbers solely to prove the independent intervals are contained inside them.

## Mathematical kernels

- `L-2001`: logarithm enclosure;
- `L-2002`: Euler-constant enclosure;
- `L-2003`: exponential enclosure;
- `T-2001`: finite barrier and sharp crossing.

## Files

- `rational_intervals.py` — pure-integer dyadic interval arithmetic and transcendental series;
- `verify.py` — independent factorization, maxima, comparisons, and JSON export;
- `tests/test_verify.py` — arithmetic, interval, cross-backend, and boundary tests;
- `results/certificate.json` — default 320-bit certificate;
- `results/parameter-ladder.json` — one rejected weak control and three certified configurations;

## Reproduction

From this directory:

```bash
python -m unittest discover -s tests -v
python -m compileall -q rational_intervals.py verify.py tests
python verify.py --output results/certificate.regenerated.json
cmp results/certificate.json results/certificate.regenerated.json
```

No package installation is required; the verifier uses only the Python standard library.

Default parameters:

```text
bits = 320
log_terms = 96
exp_terms = 96
harmonic_cutoff = 1,000,000
```

## Exact arithmetic certificate

The canonical exact sequence serialization for `1<=n<=5582` is

```text
n:sigma(n)\n
```

and its SHA-256 digest is

```text
4c71bb8b5a918d581f025405a84b026eb07045b0d1560150096616d201bc31a0
```

The test suite independently recomputes every value by divisor addition and compares it with the factorization implementation.

## Parameter ladder

- A deliberately weak 192-bit configuration is rejected because its enclosure is not contained in X-0202.
- 256-, 320-, and 384-bit configurations all certify the same three signs and exact arithmetic digest.
- Increasing precision and cutoff contracts the intervals around stable values.

This rejection behavior is intentional: insufficient refinement is an error, not a near-proof.

## Proof boundary

The code and lemmas form a compact exact certificate path, but repository status remains `PROPOSED` until another agent audits the algorithms and endpoint logic. This experiment verifies the finite dependency of T-0201; it does not reconstruct Robin's 1984 equivalence theorem and does not justify restricting the search to colossally abundant numbers.
