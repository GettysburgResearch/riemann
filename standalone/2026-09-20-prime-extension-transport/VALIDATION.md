# PET26 validation and scope

## Executed

Environment: Python 3.13.5, Linux; standard library only. These commands
passed in ordinary mode and with `-O` (eight accepting runs in total):

```sh
python -S -B check.py --check result.json
python -S -B verify.py result.json
python -S -B algebra.py
python -S -B test_check.py
```

The algebra output was also byte-compared with algebra_result.json in both
modes. The main report's canonical semantic SHA-256 is

`c15ca5dfac630a18566b1ef3c8e6b349c0177d8bc00cf0b712f188af0c539c60`.

Producer arithmetic uses directed dyadic intervals at 112 bits. Logarithms
use range reduction and a finite atanh series with an explicit positive
tail. Square/fourth roots use integer roots and directed endpoints. There
is no floating-point or quadrature acceptance decision. Descriptive decimal
values in README are rounded from these enclosures.

## What was checked

Seven complete stages Y=3,7,15,31,63,127,255. The largest reconstructs the
observables on every cell k=256,...,65535. There are 87,369 checked coefficient
indices counting overlapping stages; this is not a claim to have checked
87,369 distinct integers. Each stage retains the full prime and prime-power
sums, the logarithmically weighted energy, the primitive term, both signed
means, and the complete canonical updated energy.

The producer computes prime and higher-power coefficient convolutions. The
second implementation in verify.py uses trial factorization, per-prime exact
valuation identities, a reverse weighted Mertens tail sum for the prime
covariance, and the finite single-squared-prime formula for the higher-power
covariance. It imports neither check.py nor repository code. It shares
exact.py's interval primitives; it is not a fully independent arithmetic
kernel. It independently checks E,I, both means, both complete states and
both covariances, NOT every Schur maximum or every field of result.json.
The producer and the separate constant regression replay those other fields.

The algebra test covers 4,140 logarithmic-defect coefficients, 1,364 horizon
coefficients, five nonzero excluded-boundary cases, 105 local-tail coefficient
identities, and twelve direct finite-field point counts. The finite elliptic
Euler fixture uses only three good primes; it is NOT a global L-function.

Eight unit-test methods pass per mode. Ten report mutations are refused by
canonical typed comparison; duplicate JSON keys, numeric/Boolean type aliases,
invalid interval shapes, a bad elliptic prime and a wrong inert-square sign
are also covered. These are in-process tests, not ten complete subprocess
replays. The nonnative delta control has prime covariance above 5.39297 while
the falsely applied native signed bound is below 0.29900, so omitting the
logarithmic defect is demonstrably wrong.

## Scope of proof and computation

The all-scale result is the proof in PROOF.md, not an inference from seven
negative covariance values. Classical logarithmic inversion, the PNT and
Schur's test are credited in SOURCES.json. No optimality or broad priority
claim is made for the 1/12 asymptotic constant.

The finite signed estimate concerns P_Y, NOT PCR26's full product covariance.
Its positive-part bound does not upper-bound the next energy without new
control of the negative part. No uniform negative-part estimate, all-scale
sign theorem, new native Newton gain, or RH/GRH proof is claimed.

This pass did NOT run the whole repository validator, any predecessor's full
campaign, Lean/Metamath, remote CI, CM integrals, elliptic L-values, analytic
ranks, heights or zero computations. The authors of the two implementations
are the same research agent. Independent mathematical acceptance is pending.
The external Sylvester theorem is frozen to the supplied v2 PDF, whose hash
is recorded; its global proof was not re-certified here.

## Development and publication

The initial internal scout used floating-point descriptive values and a
weaker R-operator constant 2. The accepted proof uses the exact finite Schur
constant 2(1-b^(-1/4)); all accepted values were recomputed with directed
arithmetic. The first local Euler fixture was synthetic; before final replay
it was replaced by directly counted good-prime factors of E_17. No earlier
synthetic count is represented as elliptic data.

Only this new directory is intended for publication. Existing BCP26, SBC26,
RCB26, the #848 branch, main, canonical statuses and workflows are preserved.
The remote commit receipt belongs in the PR discussion, outside this frozen
packet. SHA256SUMS authenticates the other packet files and excludes itself.
