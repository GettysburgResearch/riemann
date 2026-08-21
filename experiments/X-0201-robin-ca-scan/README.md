# X-0201 — Exploratory Robin scan on colossally-abundant transitions

Experiment ID: X-0201  
Status: EMPIRICAL  
Agent: gpt56-02  
Issue: #2  
Date: 2026-07-22  
Related claims: L-0201, M-0201  
Candidate IDs: none

## Research question

Can a structured search produce an integer \(n>5040\) with

\[
\frac{\sigma(n)}n\ge e^\gamma\log\log n,
\]

and can any such hit be converted into a compact, independently checkable
interval certificate?

Robin proved that RH is equivalent to the strict opposite inequality for every
integer \(n\ge 5041\). Thus a single rigorously certified violation would be an
unconditional finite counterexample to RH. The scan in this directory is a
discovery tool only; `certify.py` is the proof-oriented one-integer verifier.

## Contents

- `run.py` — segmented-prime, streaming CA-transition scan; binary64 and
  explicitly non-rigorous.
- `certify.py` — directed-decimal verifier for one exact prime factorization.
- `tests/` — regression, arithmetic, transition, and certificate tests.
- `results/scan-pmax-100000000.json` — compact output of the main scan.
- `results/scan-pmax-100000000.time.txt` — wall/user/system time and peak RSS.
- `certificates/calibration-*.json` — proof-oriented calibration outputs.
- `certificates/request-example.json` — certificate input schema example.

## Discovery algorithm

For a prime \(p\), the transition increasing its exponent from \(a-1\) to
\(a\) occurs at

\[
\varepsilon_{p,a}=
\frac{\log((1-p^{-a-1})/(1-p^{-a}))}{\log p}.
\]

The exponent-one boundaries decrease with \(p\), so `run.py` streams primes in
ascending order. It sorts only the exponent-at-least-two events above the chosen
cutoff and merges them into the prime stream. At `--p-max 100000000`, there are
5,761,455 exponent-one events and only 1,868 additional events.

The program maintains

\[
\log n=\sum a_p\log p,
\qquad
\log\frac{\sigma(n)}n,
\]

incrementally, without constructing the integer itself.

## Main command

```bash
python run.py --p-max 100000000 --top-k 20 --json \
  > results/scan-pmax-100000000.json
```

Timing command used:

```bash
/usr/bin/time -f 'wall=%e user=%U sys=%S maxrss_kb=%M' \
  -o results/scan-pmax-100000000.time.txt \
  python run.py --p-max 100000000 --top-k 20 --json \
  > results/scan-pmax-100000000.json
```

## Environment

- OS/kernel: Linux 6.12.13, x86_64
- Python: CPython 3.13.5
- Dependencies: Python standard library only
- Discovery numerical backend: CPython `math`, IEEE-754 binary64
- Randomness: none
- Default transition near-tie guard: 64 relative binary64 ulps
- Certification arithmetic: `decimal.Context` with directed rounding;
  correctly-rounded Decimal `ln`/`exp` expanded by adjacent values

## Result

The completed scan reported:

- largest prime cutoff: \(10^8\);
- primes processed: 5,761,455;
- CA transition events processed: 5,763,323;
- near-tie warnings: 0;
- endpoint/best event: multiply by prime 99,999,989 at exponent 1;
- approximate \(\log n\): 100,002,363.04910879;
- approximate decimal digits of \(n\): 43,430,474.4495;
- best empirical normalized Robin quotient:

\[
0.9999956947778097;
\]

- empirical gap below violation: approximately
  \(4.3052221903\times10^{-6}\).

**No counterexample candidate was found.** This is a negative empirical result,
not a certification that all scanned states satisfy Robin's inequality. The
transition order and quotient are binary64, and the CA sequence is only a
structured subsequence of the superabundant search space.

## Tests

```bash
python -m unittest discover -s tests -v
python -m compileall -q run.py certify.py tests
```

Thirteen tests passed. They include:

- agreement of simple and segmented prime sieves;
- monotonic transition sanity checks;
- exact recovery of the first 22 classical CA values;
- a small end-to-end scan;
- exact agreement between the streaming merge and an independent all-events sort on a small cutoff;
- deterministic 64-bit primality checks;
- rejection of composite factor bases;
- directed-interval calibration at 5040, 5041, and 55440;
- stability of the 55440 sign at increased precision and gamma terms.

## One-integer certificate format

Example request:

```json
{
  "schema": "riemann.robin.factorization.v1",
  "factorization": [
    {"p": 2, "a": 4},
    {"p": 3, "a": 2},
    {"p": 5, "a": 1},
    {"p": 7, "a": 1}
  ],
  "precision": 60,
  "gamma_terms": 100000
}
```

Run:

```bash
python certify.py --request certificates/request-example.json
```

The verifier computes \(\sigma(n)/n\) from exact integer prime-power ratios,
encloses \(\gamma\), \(\log n\), and \(\log\log n\), and returns one of:

- `CERTIFIED_VIOLATION`;
- `CERTIFIED_SATISFACTION`;
- `UNRESOLVED`;
- `OUT_OF_DOMAIN` for \(n\le 5040\).

Any `CERTIFIED_VIOLATION` must still be reproduced with an independent interval
or ball library before the project treats it as a genuine RH counterexample.

## Limitations

1. Binary64 transition ordering is not proof-grade.
2. No completeness theorem is supplied for scanning only CA states.
3. The endpoint's full 5.7-million-prime factorization is not committed.
4. The discovery scan and one-integer verifier are not yet joined by a compact,
   verified factorization recipe.
5. A finite negative scan cannot establish RH.
6. CPython Decimal's documented rounding contract is a software dependency;
   independent Arb/MPFI reproduction is required for a decisive witness.

## Next experiment

Build a certified event-ordering layer and branch-and-bound search over monotone
prime-exponent vectors around the best CA states. Use rigorous upper bounds on
unassigned prime factors to prune a whole subtree only when it cannot reach
Robin quotient 1.

## References

- G. Robin, “Grandes valeurs de la fonction somme des diviseurs et hypothèse de
  Riemann,” *J. Math. Pures Appl.* (9) 63 (1984), 187–213.
- Y.-J. Choie, N. Lichiardopol, P. Moree, and P. Solé, “On Robin's criterion for
  the Riemann hypothesis,” *J. Théorie des Nombres de Bordeaux* 19 (2007),
  357–372, doi:10.5802/jtnb.591.
- L. Alaoglu and P. Erdős, “On highly composite and similar numbers,”
  *Trans. Amer. Math. Soc.* 56 (1944), 448–469,
  doi:10.1090/S0002-9947-1944-0011087-2.
- Python 3 standard-library documentation, `decimal` module (`ln`, `exp`,
  directed contexts, and adjacent representable values).
