# Validation boundary

The exact arithmetic controls are independent of the #792 producer: no
upstream code is imported. Python's standard library only is required.
`Fraction` and an explicit Gaussian-rational class carry the arithmetic.
The checker uses explicit exceptions, not assertions, for acceptance.

Commands from this directory:

```sh
python -I -S verify.py --check result.json
python -I -S -O verify.py --check result.json
python -I -S test_rejections.py
```

The recorded run used Python 3.13.5 on Linux. The checker reconstructs 618
bounded checks in 16 named groups. These are finite fixtures, not 618
analytic theorems. Included are exact polynomial coefficients, full complex
residual Grams, ridge systems with zero and dependent columns, continuum
polynomial moment corrections, primitive-tail constants, and a logarithmic
diagonal prototype with an infinite-tail enclosure proved in PROOF.md.
The original actual-W matrix experiment is not rerun or endorsed.

Normal and optimized mathematical payloads are compared byte for byte.
Twelve intentional mutations in each mode exercise the actual checker CLI,
including duplicate JSON, integer/Boolean and floating aliases, changed
RH/source/sign flags, altered proof/source bytes, and incomplete/duplicate
manifest coverage. Proof and source-lock SHA-256 values are literal checker
anchors. The manifest binds every delivered file except itself; these are
content checks, not cryptographic signatures or mathematical certification.

Preparation failure retained: the first checker run rejected a mistakenly
written factor 1/6 in its gamma partial-fraction helper. The correct factor
is 1/3 because the denominators differ by three. The manuscript's displayed
infinite gamma constants were unchanged. The corrected helper then passed.
No failed or interrupted run is counted as a successful execution.

The analytic domain/core proof, Carleman inequality, compactness, limiting
residual theorem, Littlewood conditional input, and RH implications are
paper proofs/imports, not machine-verified by these tests. The interval
budgets in LC5 are proved but the complete actual-source interval search
engine is NOT implemented. No actual positive-window certificate, Lean
build, remote CI, global theorem acceptance, or RH proof is claimed.
