# Sources, self-audit, and validation boundary

Status: proposed proofs and executed bounded certificates. RH unproved.
No external novelty claim. Exact old files are preserved, not rewritten.

## Frozen repository reading

The live PR was read at 6ebbe5efe6430584736649b87495af2be073f693, including its
publication comments and SIGNED_ENERGY_IMPORT.md. This confirms that the
attached signed-energy packet was imported without modifying its seven
files, alongside the separate fourth-pass study.

Proof-level sources used:

- PR #793, the same head, pass4/PRIME_TAIL_TRANSITION.md: complete reading
  of the raw-cutoff pole, all-degree PNT comparison, balanced repair and its
  surviving sign gap. None of its PNT or Gaussian-limit claims is needed
  for the new cutoff or source-compiler theorem.
- PR #793, pass4-signed-energy-attempt/PROOF.md: the source normalization,
  extended Hardy norm identity and the sharp Abel diagonal. The supplied
  local proof was read, and the remote import receipt verified its identity.
- PR #793, bfb66e07f7e38306dbcb916911332a591efce917,
  pass3/R1_MOMENTS.md and R3_LAGUERRE_CAPTURE.md: source definitions,
  moment/quadrature endpoint and exact Hardy matrix recurrence. These were
  already present in the conversation and the uploaded packet. Their
  infinite capture results are retained as parent theorems, not independently
  re-reviewed by the new finite certificate.
- PR #792 at dc4bb9dbb49876732eb656339e79ee4ec43b157f: current PR description
  read for the cutoff/compression distinction. The BRIDGE.md directory was
  identified, but its full proof and code suite were NOT reviewed this pass.

Current work imports no predecessor implementation: the interval engine,
finite series operations, zeta/digamma remainder handling and tests here are
self-contained. The old 706/331/622-control suites were not rerun this pass.

## Classical mathematical ingredients

NIST DLMF was checked for the classical generating identity and the standard
zeta/digamma setting. Relevant primary reference pages:

- https://dlmf.nist.gov/18.12.E13 — Laguerre generating function.
- https://dlmf.nist.gov/25.2 — zeta definition and expansions.
- https://dlmf.nist.gov/5.11 — gamma/digamma asymptotic expansions.
- https://dlmf.nist.gov/24.8 — periodic Bernoulli Fourier expansions.

The exact Euler--Maclaurin formulas and error bounds USED are written out in
SOURCE_COMPILER.md, rather than asserting a bound from an unspecified
software routine. Cauchy's estimate, finite Jacobi recurrence, Gaussian
saddle analysis, Stieltjes integration, LDL congruence and finite spectral
quadrature are classical tools. The outer Laguerre saddle is proved from
the generating contour for the particular rate theorem; it is not a claim
of priority for Plancherel--Rotach asymptotics.

## Load-bearing checks for a referee

1. CT1 uses max Re(-z/(1-z))=r/(1+r), not r/(1-r). The latter would give
   an unnecessarily different cutoff. The exponent alpha and 544/195 are
   checked exactly. The integer cutoff is inclusive; the omitted sum is k>X.
2. The sharp constant is for the UNIVERSAL ABSOLUTE tail. It is not a lower
   bound on what actual Mobius cancellation can achieve. The saddle lower
   bound stays in t>2; it does not cross a turning point.
3. In the sharp lower bound, the exponential number of integers (or
   squarefree integers) in a log interval supplies the factor exp(tn).
   Omitting it would change -3t/2 to the wrong exponent instead of -t/2.
4. For zeta, retain the periodic-Bernoulli remainder with its full rising
   product. Scaling the rising factors by K before multiplication is also
   important for numerical enclosure width.
5. The inverse-zeta denominator bound is used ONLY on Re s>=23/18.
   There is no continuation of that bound to Re s>1/2.
6. Logarithmic differentiation requires one extra Taylor coefficient. The
   code computes degree N+1 before forming the degree-N derivative jet.
7. Digamma is shifted by K before its asymptotic expansion. Its remainder
   is explicitly bounded; a truncated divergent series is not presumed exact.
8. Moment and Hardy matrices use the completed xi expression, including both
   rational completion terms and log(pi)/2. The 200 scalings are positive
   congruences, not changes of the source.
9. Interval LDL gives finite PSD certificates only. Five quadrature weights
   are arbitrary positive real weights, not integer zero multiplicities.
10. SC6 is an error amplification bound, not a positivity induction. The
    signed boundary forcing of the matrix recurrence has not been controlled.

## Execution actually performed

The two default producer runs, normal and python -O, independently
reconstructed SOURCE_RESULTS.json from the constants and matched it byte for
byte. They prove eighteen STRICT interval pivot signs for the stated matrices
and enclose thirteen Mobius coefficients. No zero values enter acceptance.
All fourteen unit/rejection tests pass in both modes. They include exact
interval arithmetic, inadmissible numeric types, domain failures, elementary
constant identities, Bernoulli values, the analytic error budgets, the
critical-slope signs, an independent finite recurrence expansion, zeta(2),
a digamma shift and an indefinite-matrix refusal.

Two intentionally corrupted saved-result files (one per mode) were rejected.
The checksum manifest is checked separately, with exact file coverage. The
file REPLAY.json records executed commands, return codes and hashes.

The optional 110-digit mpmath regression agrees with the seven low Mobius
coefficients, three moments and three Hardy-source coefficients it checks.
It also records three outer-saddle ratios, not an asymptotic certificate.
An earlier attempt to run ALL nested high-order derivatives at 140 digits
hit the execution timeout and produced no accepted result. It was replaced
by the stated bounded check. This optional run is NON_DIRECTED_HIGH_PRECISION
and contributes nothing to the rigorous acceptance or remainder bounds.

## Explicitly not accomplished

The all-degree subexponential signed energy inequality, all-order moment PSD,
and all-rank Hardy positivity have not been proved. The analytical cutoff
and source approximation theorems are completed component results, not an RH
completion. The moment and matrix size increases are finite validations, not
an extrapolation. No broad zero/prime sweep, Lean formalization, remote CI
verification, comprehensive novelty search, or independent referee review
was performed. The code caps protect execution; the analytical approximation
statements have their stated arbitrary-degree quantifiers separately.
