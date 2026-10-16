# Recovery and a direct Gaussian energy attack

Status: PROPOSED. The prior packet has now been published; the new one-sided
arithmetic energy estimate remains OPEN. No new zero-free boundary or RH proof.

The preserved 13-file packet is in ../2026-10-16-critical-power-factorization/.
Its initial recovery commit is bf55bad693d147747bdb8074fc555d408b60782e, on PR
#952. ../2026-10-16-critical-power-recovery/PUBLICATION.md supersedes only its
historical not-pushed status.

Read ENERGY_THEOREM.md. The continuation proves:

- A source-faithful exact Gaussian pair kernel for cumulative critical L2 energy.
- O_F(T) first and second coefficient masses for the coupled 0/1/m source,
  uniformly in m, and a complete O_(F,c)(1+log D) IDEAL-diagonal energy bound.
- Two-way direct ENERGY comparisons, without a pointwise-envelope hypothesis:
  constant cost between coupled/two-channel sources, one logarithm to native.
- A finite cutoff T=D exp(sqrt(32 log(2D))) with O_(F,c)(Z_w/D) squared-energy
  error, including the omitted cross terms and full Gaussian tail.
- An explicit one-sided finite signed covariance target sufficient for the
  principal Dedekind zero-exclusion argument, together with a counterexample
  to claiming that positivity and diagonal control alone prove that target.

The missing estimate is not smaller merely because it has an exact kernel.
The note prices the diagonal, tails, and comparison operators; it does NOT
pay the arithmetic signed correlation or claim a new full-moment exponent.

Concurrent #950/#951 overlap the recovered factorization and Gaussian adapter.
Their one-log budgets and coupled positive-compensation flow are credited.
This continuation is about the actual cumulative energy and its pair kernel.

Reproduce the EXACT checks from this directory:

    python chks/check_energy.py
    python -O chks/check_energy.py

Both must match EXACT.json. The separate NUMERICAL.json is an UNCERTIFIED
60-digit quadrature diagnostic of eight finite three-prime polynomials:

    python chks/check_energy.py --numerical-helper ../2026-10-16-critical-power-factorization/chks/eisenstein_source.py

It is not a native-column census or asymptotic evidence. See VALIDATION.md
for the detected-and-fixed root-basis issue, process mutations and scope.
No independent mathematical review, formal build or remote CI is claimed.
