# Validation and analytic review boundary

Status: executed bounded checks plus ordinary floating diagnostics. **No RH proof, zero certificate, formal proof, or independent-author acceptance.**

## Executed exact reconstruction

Environment: Python 3.13.5; standard library `fractions.Fraction` and integer arithmetic. `check.py` does not use `assert` for acceptance, so optimized Python retains all acceptance conditions.

Executed from this packet directory:

```sh
python -I -S -B check.py --write result.json --self-test
python -I -S -B check.py --check result.json --self-test
python -I -S -B -O check.py --check result.json --self-test
```

The first is producer mode, not independent acceptance. Both acceptance modes reconstruct the same entire receipt and report:

```
PASS c3253680f4b938259b08b8d2fc54ecb290a09ef36116d21da650f929026232d1 4243 bounded exact checks
SELF-TEST PASS: 7 altered/invalid records rejected by actual comparator/parser
```

The digest summarizes the finite algebraic transcript, **not an authentication of a whole xi computation**. The full counts and exact rational witnesses are in `result.json`. The checks cover source coefficients, native and Pareto moment recurrences, finite eigenmode and delay identities, survival-ratio derivatives, explicit inverse coefficients, hyperbolic conjugacy, the rational TP3 counterexample, and the polynomial arithmetic underlying the finite shifted-xi identity. Several checks compare whole finite coefficient vectors; the 4,243 figure counts the script's test calls, not a claimed number of separate theorems.

The seven negative tests are six mutated in-memory receipts and duplicate-key JSON tested with the actual comparison/parser functions. They are not seven separate full reconstructions or subprocess replays. No interval arithmetic is required for these rational identities. No exact theta moments or zeta values are consumed by `check.py`.

## Executed floating diagnostics

```sh
python diagnostic.py --dps 70 --out diagnostic_70.json
python diagnostic.py --dps 90 --out diagnostic_90.json
```

Each run compared 18 independently written integral/finite-shift expressions, six removable coefficient values via nearby evaluations, and six exact-in-principle integer moment normalizations. Maximum integral-pair relative discrepancies were approximately `6.355e-71` and `5.484e-91` respectively. The actual values, precision, and mpmath version are retained in the JSON files.

Both runs share mpmath; their agreement is not independent verification of its backend. Its quadrature extends over an infinite interval but supplies no proved remainder here. No result from this diagnostic enters the analytic proofs. These are not directed enclosures and do not certify complex zeros, phases, or any continuum.

## Analytic hypotheses requiring review

The paper, not the finite checker, must establish the all-order moment bounds; analytic Wiener domain and compactness; all-spectrum and resolvent arguments; differentiation of bounded and Pareto affine integrals; positive survival density, exact normalization and full tails; Mellin cancellation and entire continuation; gamma/eta normalization; and the claim that the native kernel is TN2 but not TN3.

The actual BPY/xi scaling is credited as classical and additionally derived in Section 1 from the explicit source integral, sinh expansion, gamma duplication and the classical functional equation. The new arithmetic-shift identity is proved on an absolutely convergent left half-plane before continuation; no numerical extrapolation supplies that continuation.

## Other exploration and exclusions

`EXPLORATION.md` records the unsuccessful Gaussian-polynomial lifting attempt and the finite moment-ratio scout. Their original scripts, data, and outputs are preserved separately in the downloadable archive, not incorporated into the exact checker. No mathematical obstruction is inferred from an optimizer's failure.

No parent certificate was replayed. No full-repository validator, CI workflow, Lean build, general source-file authentication service, independent author review, or remote publication occurred. `SHA256.json` is a file-integrity inventory only; it cannot establish mathematical validity.
