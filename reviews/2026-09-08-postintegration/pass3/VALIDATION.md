# Pass-three execution and assurance

All runs here use reviewer-written standard-library Python. No author mathematical/numerical producer or full author package is executed. The scripts do not claim to authenticate the whole repository or machine-prove the infinite analytic statements. Manuscript blob IDs in FILES.tsv are the connector-reported source identities; those manuscripts are not presented as locally hashed executable inputs.

## Executed mathematical reconstruction

| Script | Actual coverage | Result |
|---|---|---|
| checks.py | Six groups: directed arithmetic; all 4095 ANT profile cells and full tail; both P13 root-capacity reservoirs; Lyapunov/stopped-source work; rational optimizers/duals/terminal/hyperbola identities; annular scalar constants and bounded actual prime-power values | 13,607 runtime checked assertions, including 4095 profile cells. Normal and optimized outputs identical. These are overlapping finite checks, not theorem counts. |
| gram_checks.py | Complete pairwise periodic Grams with two-sided Euler--Maclaurin tails; four two-jet RN minima; full DO/BG projection, leakage, coefficient-nine and failed detail-lift bounds | 496 unique matrix entries and 73,621 cached periodic weights; 599 checked assertions. Both complete runs agree byte-for-byte. |
| rc_checks.py | Three one-jet RC minima at H=4096 using independent free-coordinate KKT and separately minimized comparison forms | All three printed brackets reproduce; 175 checked assertions; identical outputs. |
| test_controls.py | Fifteen arithmetic/typing/receipt contracts, including actual CLI pristine acceptance and seven distinct corrupted-receipt refusals per mode | Fifteen methods pass in each mode, no skips, identical JSON summary. |

The code uses 176-bit outward dyadic endpoints where intervals are needed, exact Fraction operations elsewhere, and decimal floor/ceiling display. Logarithms use a range-reduced positive atanh series with its full remainder. Pi uses Machin's identity and alternating rational remainders. The Gram calculation includes 32 direct terms of each periodic weight followed by eight Bernoulli corrections and a complete two-sided remainder; no digamma oracle or floating quadrature enters acceptance.

The rational midpoint KKT systems are proposal mechanisms only. RN's actual endpoint coefficients are defined by exact algebraic logarithm formulas; an interval containing zero is a check, not the proof of feasibility. Residual floors control the true minima. The full Green/detail reconstruction retains every old-coarse cross term. The author numerical implementation is not consumed.

The RC free-coordinate routine is adapted from the earlier locally prepared reviewer draft, not from the author's implementation. It is freshly executed and recorded here; the published pass-two record did not contain a completed RC-minimum replay. Its finite table is compared with source result blob 2a26708785c5ba505b48dd56696cbc9aafe3c085 at the commit in FILES.tsv.

## Reproduction

Run from this directory, placing output outside the repository if later authenticating a clean checkout:

```sh
python3 -I -S -B checks.py > /tmp/pass3-controls.json
python3 -I -S -B -O checks.py > /tmp/pass3-controls-optimized.json
cmp /tmp/pass3-controls.json /tmp/pass3-controls-optimized.json
cmp /tmp/pass3-controls.json evidence/controls.json
python3 -I -S -B gram_checks.py > /tmp/pass3-grams.json
python3 -I -S -B -O gram_checks.py > /tmp/pass3-grams-optimized.json
cmp /tmp/pass3-grams.json /tmp/pass3-grams-optimized.json
cmp /tmp/pass3-grams.json evidence/grams.json
python3 -I -S -B rc_checks.py > /tmp/pass3-rc.json
python3 -I -S -B -O rc_checks.py > /tmp/pass3-rc-optimized.json
cmp /tmp/pass3-rc.json /tmp/pass3-rc-optimized.json
cmp /tmp/pass3-rc.json evidence/rc.json
python3 -I -S -B test_controls.py > /tmp/pass3-tests.json
python3 -I -S -B -O test_controls.py > /tmp/pass3-tests-optimized.json
cmp /tmp/pass3-tests.json /tmp/pass3-tests-optimized.json
cmp /tmp/pass3-tests.json evidence/contracts.json
```

The complete controls script also supports `--verify-receipt`; it reconstructs the mathematics before comparing the strictly parsed, type-sensitive expected JSON. A digest match alone is never its mathematical acceptance step. The other scripts are independent reconstructions whose emitted outputs can be compared with the retained receipts; they are not general certificate importers.

EXECUTION.json pins final code and receipt hashes, modes, platforms and exclusions. SHA256SUMS covers the delivered regular files except itself. Source texts, proof sketches, and finite regression successes are different evidence classes.

## Failed/prepublication checks and limits

An initial RC result serialization hit Python's decimal-integer length guard after the numerical calculation. The final fingerprint uses hexadecimal rational numerators/denominators; both final complete executions finished. Before publication, receipt comparison was strengthened from Python equality (which aliases false and zero) to type-sensitive canonical serialization, and actual CLI tests verify that the alias rejects. Initial development outputs are not counted as a completed final suite.

No full Riemann checkout was available. No fresh Lean/comparator/axiom audit, native Windows test, author-package rejection suite, remote CI, high-zero verification, large prime-error/entropy campaign or exhaustive history/discussion audit is claimed. The finite source reconstructions do not certify the formal proof or external originality of the analytic asymptotics. Previous pass-one/pass-two checks are not counted as fresh runs.
