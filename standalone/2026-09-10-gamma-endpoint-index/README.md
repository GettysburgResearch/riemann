# Gamma endpoints: a real spectral tail and a finite exceptional polynomial

**PROPOSED component proofs and a complete finite certificate, pending independent
mathematical/code review. RH and the uniform exceptional-zero estimate remain OPEN.**
This is an add-only continuation of #855 at
`0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad`. Parent research, integration,
canonical status, main and formal sources are not changed.

Read [PROOF.md](PROOF.md), then [CERTIFICATE.md](CERTIFICATE.md),
[SOURCE_LOCK.json](SOURCE_LOCK.json) and [VALIDATION.md](VALIDATION.md).

## What changes

For the exact mean-centered reciprocal gamma approximant F_N:

- **GE1--GE2:** for EVERY fixed N, all sufficiently large complex zeros are
  real and simple. The proof derives an analytic nonvanishing endpoint factor,
  treats both complex sectors, and counts one root per shrinking disk. The
  locations are pi(k+N/2+3/4)/L_N plus the explicit 1/k correction. No zero
  table, RH, or numerical exterior radius is used.
- **GE3:** F_N is an even real polynomial containing all nonreal quartets,
  times a Laguerre--Polya function. The negative index of its source power-sum
  Hankel matrices eventually equals the number of DISTINCT nonreal quartets,
  not their total multiplicity. The infinite positive tail is paid. Neither
  that polynomial nor its index is numerically computed in full here.
- **GE4:** centered integer N=5 has exactly one simple zero in a radius-10^-12
  disk about 31.0835163803300613860836804713778137956057544691
  +0.2347791171837078741080118319340221394471947526 i. This is inside the
  critical band. It is a finite approximant, NOT xi or zeta.

Thus the entire nonreal obstruction is FINITE at each stage, while the stronger
rule that every centered stage is real-rooted fails. Its finite exceptional
polynomial must be controlled as N grows; it cannot be discarded. The endpoint
correction coefficient grows like (pi^2/2+1/3)N^2, so the fixed-N theorem is not
uniform. The parent convergence then supplies a complete conditional ending if
the exceptional zeros escape bounded height or collapse to the real axis on a
cofinal subsequence. That source-specific theorem is not obtained in this pass.

## Reproduce the actual finite result

From this directory, with Python's standard library only:

```sh
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The first two commands authenticate the complete packet and freshly integrate
all 785 degree-40 scaled Taylor cells, both density factors, the exact mean,
the complete endpoint interval, and a full Rouché derivative budget. Arithmetic
is outward 512-bit integer intervals; there is no zeta oracle or floating
quadrature. interval.py is a byte-identical inherited module, not an independent
primitive backend. Normal/optimized agreement is also not independent review.

`--quick` performs ONLY bounded algebra/source checks and says so explicitly.
The six-method test suite has twelve real CLI refusal cases and bounded algebra;
it does not rerun the integral. The validation record separates those runs.
`certificate.py --write OUTPUT` and `check.py --write-bounded OUTPUT` are
producer modes, not authenticated accepting commands.

There is no complete zero census, evaluated high-frequency threshold, first
negative Hankel degree, Lean proof, or all-N numerical feasibility result.
Classical endpoint asymptotics and factorization are credited; no comprehensive
external priority claim is made. The supplied mathematics requires proof review.
