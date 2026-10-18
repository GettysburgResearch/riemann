# Executed validation and the finite/infinite boundary

Run `python replay.py` from this directory, or pass its full path. Only the
Python standard library is required. The script regenerates CHECKS.json and
REPLAY.json; neither file supplies input to acceptance.

## What was actually executed

The complete checker passed under ordinary and optimized Python. Its reports
were byte-identical, with SHA-256

`8a314267209f9fe2b62dd6035ef2ff2dbb7ebad92bdf257fceda6dfa0e30628c`.

The report has **2,573 explicit predicates**, including repeated interval
domain/setup guards. This does not mean 2,573 independent analytic theorems
or arithmetic asymptotic cases were checked.

The exact finite work covers:

- Every integer 1<=n<=256: the complete divisor-convolution coefficient,
  independent prime-factor expression, one-boundedness, and its inverse
  Dirichlet convolution back to mu(n).
- Seven complete prime-local Euler fixtures, six positive shifts in each
  valuation, and the actual infinite geometric tails. Shared-prime controls
  reject the false coprime factorization when both valuations are positive.
- Every coprime pair 1<=r,s<=16 for the primitive-ratio mean factors. The
  common summation integer is not required to be coprime to either ratio.
- All 511 nonunit terms 2<=r<=512 of the signed constant in ARITHMETIC (10),
  computed with exact rational beta(r) and outward integer interval arithmetic.

The sign certificate encloses the INFINITE constant in

    [-709483157548514576863927690283163444776 / 2^128,
     -485230808240989404772689759993717528466 / 2^128].

The approximate endpoints are -2.0849836092545946 and -1.4259651848305392.
The strict accepted claim is only **-21/10<L_div<-7/5**. The approximately
-1.755474397042567 finite sum is not substituted for the infinite constant.
The certified absolute tail bound is approximately 0.3295092122120277 and
is added with BOTH signs. The checker authenticates the finite arithmetic;
the proof of (13) supplies complete infinite-tail coverage.

All logarithms use range reduction and the atanh series with its explicit
positive tail bound. All negative exponentials use even/odd alternating
Taylor bounds after fixed range reduction and then an integer power. Every
arithmetic endpoint is rounded outward on the dyadic grid 2^-128. Decimal
display fields are informational; no floating-point value decides the sign.

## Finite numerical QA, separately scoped

Eight ordinary binary64 adaptive-Simpson cases compare the analytic Gaussian
Gram kernel with direct integration, including a full eight-coefficient
quadratic form with all ordered pairs, plus the complete one-sided continuum
formula's norm/cross term. The observed maximum difference was approximately
2.16e-14, below the declared QA tolerance 1e-10. Numerical integration uses
[-40,log T] or [-40,40] as reported. This is NOT outward arithmetic, NOT an
infinite-source evaluation and NOT an analytic proof. It checks normalization
mistakes independently of the finite sign certificate.

## Three separately executed corrupted processes

The runner launched each mutation with optimized Python in its own process.
All exited unsuccessfully at the intended gate:

| Corruption | Required rejecting gate |
|---|---|
| Replace beta(2) by -1/2 | `ray beta constant` |
| Drop every nonsquarefree prime-power coefficient | `complete coefficient convolution` |
| Replace the Gaussian log-ratio denominator 8 by 4 | `finite Gaussian kernel quadrature` |

These are real subprocess executions, not three internal Boolean examples.
Their role is to verify the specified software checks, not to supply an
independent proof of the infinite analytic arguments.

## What remains outside computational validation

The checker does not prove Tao's logarithmic correlation theorem, rebuild
the inherited research repository, execute the #989-991 checkers, verify CT
or de Faveri, count zeta zeros, or bound the complete critical energy. It
does not certify a growing range of additive shifts or justify exchanging
the infinite two-variable primitive-ratio sum with a large-scale limit.

This packet's author wrote both proofs and checker. Independent mathematical
review must be recorded separately at the frozen file hashes. A source read,
an agent agreement, or a successful Python replay is not integrated referee
acceptance. The strongest mathematical upper premise needed for RH remains
explicitly open in PROOF.md and ARITHMETIC.md.
