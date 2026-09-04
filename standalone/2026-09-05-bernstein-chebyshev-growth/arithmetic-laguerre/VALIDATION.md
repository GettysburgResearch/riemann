# Validation and review boundary

Date: 2026-09-05 (Asia/Jerusalem).
Status: exact finite algebra replayed; analytic manuscript awaits independent
review; the requested RH-strength inequality remains NOT PROVED.

## Executed from the local publication bytes

```
python verify_arithmetic.py --check result.json
python -O verify_arithmetic.py --check result.json
```

Both runs passed 1,795 checks and produced byte-identical JSON. The groups
and exact synthetic witness values are listed in `result.json`. Checks use
Fraction and pairs of Fractions, not floating-point arithmetic.

The unchanged parent checker was also replayed in both modes:

```
cd ..
python verify_exact.py --check result.json
python -O verify_exact.py --check result.json
```

Both parent runs passed the original 1,922 checks and produced byte-identical
JSON. This is a fresh replay of PR #792, not of PR #790 or any external
zero-verification computation.

Four corrupted controls were tested in BOTH interpreter modes, for eight
refusal executions: a wrong saved model coefficient, a wrong saved source
hash, the numeric type alias 32.0 in place of integer 32, and changed proof
source bytes against the original result. Every run exited nonzero with
`REFUSED`. The type-alias test is deliberately stricter than ordinary Python
dictionary equality. A separate plain-text check found valid UTF-8, terminal
newlines, and no trailing whitespace in the five computational source/result
files present before this validation note was added.

`REPLAY_LOG.json` records the executed counts, mode comparisons, and refusal
exit codes. It is an execution receipt, not a machine proof of the analytic
arguments. `SHA256SUMS` covers all other files in this addendum. The exact
parent Git blob identities are independently fixed in the checker and the
source-lock file; all four matched their local bytes.

## What the checks establish

Finite checks compare independent polynomial recurrences and closed forms,
formal exponential Taylor recursion and Laguerre coefficients, elementary
Laplace integrals and rational pole coefficients, finite digamma-pole
normalizations, synthetic source logarithmic derivatives and trace return,
and the Gaussian-rational continuous model. Degrees stop at 32. The
all-degree statements rest on the written proofs, not extrapolation.

## What was not done

No actual-zeta derivative evaluation, infinite prime-sum evaluation, prime
sweep, zero census, external verifier replay, Lean run, independent proof
review, or GitHub Actions result is claimed. The target signed estimate over
`(exp(sqrt(N)), exp(4N)]` is not checked or proved by this package.

## Priority review

Read PROOF.md (1)--(4) for the original/auxiliary coordinate and 3/8 factor;
then (7)--(12) for pole subtraction, gamma cancellation, and uniform error;
then (13)--(19) for endpoint conventions and degree-uniform tails. Finally
review (21)'s continuous-source/non-Euler-product scope and the explicitly
unproved inequality (20). A review should not infer a bound on (20) merely
because both complementary ranges and all archimedean terms are controlled.
