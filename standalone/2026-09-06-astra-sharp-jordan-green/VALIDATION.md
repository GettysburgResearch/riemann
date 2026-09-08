# Executed validation and assurance boundary

Date: 2026-09-06. Environment: Python 3.13.5, SymPy 1.14.0 on the provided Linux
runtime. The accepted result is 24 named exact control groups / 778 bounded
fixtures in each Python mode. These are not 778 independent mathematical
theorems. Polynomial interval controls use exact Bernstein coefficients,
not dense real sampling. Other fixtures reconstruct finite factorial/divisor
identities, Jordan coefficients, association examples and the synthetic port.

Executed on the final source:

```bash
python checks.py --output checks.normal.json
python -O checks.py --output checks.optimized.json
cmp checks.normal.json checks.optimized.json
python checks.py --compare checks.normal.json
python -O checks.py --compare checks.normal.json
python rejections.py > rejections.normal.json
python -O rejections.py > rejections.optimized.json
python validate.py
python -O validate.py
```

Both mathematical outputs are byte-identical. The rejection script invokes
the actual checker CLI on eight corruptions per mode: RH flag, machine-proof
flag, fixture count, Boolean in a count, evaluation count, schema, removed
control and duplicate JSON key. Every invocation exits 2 with REJECTED.
The corruption record is a parser/comparator test, not a semantic proof that
the analytic manuscript is correct.

Three package mutations (changed proof, missing source ledger, unexpected
file) are tested in temporary copies with the actual validator in each mode.
The deterministic outcomes are retained in package_rejections.json. No
mutated copy is published. SHA256SUMS covers every regular file except itself;
validate.py enforces the exact inventory and rejects unexpected subdirectories.
After extraction the same validator must pass. The final remote subtree is
checked against the locally computed Git blob/tree identities before the
publication receipt is written outside the scientific packet.

## Mathematical inputs

No upstream computational producer is imported. The checker evaluates no
zeta, gamma, exponential, floating-point root or large prime sum. SymPy is
used only for exact rational polynomial algebra and bounded integer factoring.
The unbounded results rely on the complete analytic arguments in PROOF.md
and REAL_AXIS.md, including source association, factorial bounds, signed
Taylor remainder, Euler--Maclaurin and beta integration. Finite checks do
not machine-prove these arguments, nor do they certify RH.

Ordinary mpmath reconnaissance was used during discovery, including sample
Jordan knot values and exploratory mean inequalities. It was not directed
arithmetic, is not an input to any proof, and is not presented as a certificate.
The completed mathematical inequalities cover the continuum analytically.

## Authoring corrections before this freeze

A draft file-writing helper had a Python quoting SyntaxError caused by three
prime marks inside a raw string; no partial generated proof from that command
was accepted. The corrected helper wrote the intended full text.
The bounded checker was adjusted to expand before exact rational cancellation,
and to normalize a uniformly negative rational denominator before testing its
Bernstein coefficients. These are exact representation fixes; both normal
and optimized final runs were executed after the changes.
An exploratory polynomial join at 9/10 was too weak in the middle-scale
estimate. The manuscript uses 19/20, with its positive rational margin proved
explicitly. This is recorded to distinguish improving a lower bound from
mistakenly claiming every attempted bound worked.

## Not run / not claimed

No Lean, proof-kernel, Comparator, repository-wide CI, zero census, interval
campaign, or historical reviewer test suite was run. No independent human or
agent referee acceptance is asserted. A second invocation of the same exact
checker is not an independent mathematical proof. The packet's research
status stays PROPOSED / REVIEW PENDING after publication.
