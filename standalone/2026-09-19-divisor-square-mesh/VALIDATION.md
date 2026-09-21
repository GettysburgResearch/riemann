# DSE27 execution and trust boundaries

## Mathematical status

The prime-mode identity/bounds and critical-mesh theorem are proposed written
proofs. The finite computations below exercise them but do not prove the
unbounded statements or approve the surrounding research programme.

## Runs actually completed

- Ten-method standard-library test suite passed in ordinary Python and under
  `python -O`, with zero failures, errors or skips. These include 2,187 ternary
  paths under three sample meshes, all 4,095 short-source future Mertens
  checks, seed/trial agreement through 4,095, native reciprocal-crossing prime
  amplitudes, rational Fourier reconstruction, prime-square and quadratic-
  alias controls, input refusals and a real corrupted-report CLI refusal.
- The Y=1023 report was produced and reconstructed in ordinary and optimized
  pure Python. Both outputs are identical. The compiled recurrence plus
  independent full sieve also reproduces that SAME report.
- The Y=4095 report was produced and reconstructed in ordinary and optimized
  Python front ends using the compiled integer recurrence. Both also execute
  the independent full sieve through B=16,777,215; all 16,129 samples agree.
  Both source methods have the same author; no external reviewer is implied.
- C++ compiled with `g++ -std=c++17 -O2 -Wall -Wextra -Wconversion` without
  warnings. The large compiled/full-sieve run was observed at about 5.81
  seconds and 96,440 KiB maximum resident memory on this Linux container.
  This is one measured local run, not a portable performance guarantee.
- Ordinary and optimized large reports are byte-identical at the canonical
  stdout level. The independent full-energy interval is, in units of 2^-64,
  `[32217801479141878785, 32217801479158640251]`. It is wholly inside the
  sparse report's 112-bit outward enclosure.

The ten-method suite includes in-process input tests plus one actual pristine
CLI creation/check and one actual modified-report refusal. It is not described
as ten independent external validation implementations.

## Arithmetic contracts

`check.py` uses arbitrary-precision integers. Every positive rational sum is
rounded down/up in units of 2^-112. Square roots use integer square roots with
outward endpoints, followed by outward squaring. The acceptance comparison
squares the finite p=3/2 gain and uses only nonnegative integers.

`native.cpp` first generates the required sample values using only mu through
Y and an exact integer quotient recurrence. With B<2^24, intermediate signed
sums are bounded by 1+B^2 and fit int64. The optional full comparison generates
mu through B with a different prime-sign/square-removal sieve. Its energy
numerators are at most B^2*2^64<2^112 and fit unsigned __int128. Whole finite
rounding errors are retained by summing lower and upper integer endpoints.

The field `future_mobius_values_used_in_recurrence: 0` refers ONLY to the first
producer. The independent second sieve intentionally uses the full new source.
The number of retained samples is not the number of recursive arithmetic steps.

## Interrupted or unexecuted work

- An initial large pure-Python Y=4095 attempt hit the execution limit before
  writing a result. No partial output was accepted. The compiled implementation
  was then supplied, tested, and used for the completed large runs.
- An early shell call requesting unsupported interactive execution did not
  execute; ordinary noninteractive calls were used afterwards.
- No full repository checkout, inherited RCB26/NSR26 checker replay, Lean build,
  remote CI, native Windows/macOS run, independent compiler verification or
  independently authored mathematical review was performed.
- No all-scale native covariance or energy bound is inferred from either
  finite report. The existing proposed statements retain their status.

## Reproduction and publication

README gives exact commands. `SHA256SUMS` authenticates all other packet files.
Publication should preserve these bytes, compare the resulting subtree with
the locally computed Git tree, and record the actual commit/PR separately.
No main, prior research, canonical pointer, formal source or workflow is changed.
