# X-0602 — Carrier-packet Weil search

Experiment ID: X-0602  
Issue: #6, with cross-route comparison to #26  
Agent: `gpt56-02-b`  
Branch: `agent/gpt56-02-b/6-global-weil-search`  
Status: EMPIRICAL; analytic packet and gridding identities PROPOSED  
Created: 2026-07-23

## Research question

Can a finite packet of translated compact-support carriers produce a strict
negative Guinand--Weil value above the verified critical-line range, while
retaining a finite prime-power sum and an eventual compact dyadic certificate?

A strict certified negative would be an unconditional RH counterexample under
the D-0001/L-0001 normalization. This experiment did not find one.

## Cross-agent starting point

Issue #26 introduced the scalar translated Fejer family

```text
g_hat(xi) = (1-|xi|/Delta)_+ cos(2*pi*T*xi).
```

PR #23 supplied exact prime-power edge identities and a Lerch acceleration for
the cutoff-free background. X-0602 combines those ideas with the finite matrix
route:

- L-0606 proves a multi-carrier nonnegative packet family containing the scalar
  carrier as its one-dimensional case;
- the scalar value at lattice height `T=2*pi*n/log(c)` is exactly the D-0001
  diagonal `Q_nn/(2*pi)`;
- L-0605 evaluates all finite prime entries from two source sequences;
- M-0602 evaluates wide consecutive carrier windows using moment-corrected
  nonuniform gridding with an explicit Taylor remainder.

## Files

- `prime_source_direct.cpp` — exact integer prime-power enumeration, quad phase
  reduction, compensated long-double source accumulation.
- `moment_nufft.cpp` — moment-corrected gridding and ordinary radix-2 FFT.
- `analyze.py` — mpmath pole/archimedean assembly and NumPy packet eigensolve.
- `validate_bridge.py` — independent scalar-versus-diagonal normalization test.
- `tests/test_transform.py` — elementary regression tests for the Taylor bound.
- `results/bridge-calibration.json` — ten scalar/diagonal comparisons.
- `results/summary.json` — compact retained search result.
- `results/tests.txt` — test transcript.

## Build and calibration

The C++ discovery programs require GCC-compatible `__float128` and
`libquadmath`:

```bash
g++ -O3 -std=c++17 -Wall -Wextra \
  prime_source_direct.cpp -lquadmath -o /tmp/x0602-direct

g++ -O3 -std=c++17 -Wall -Wextra \
  moment_nufft.cpp -lquadmath -o /tmp/x0602-nufft

python -m unittest discover -s tests -v
python validate_bridge.py --dps 70 \
  --output results/bridge-calibration.regenerated.json
```

The bridge calibration checks `c in {13,100}` and
`n in {1,2,3,8,50}`. The maximum observed discrepancy between the independently
assembled D-0001 diagonal and Issue #26 scalar formula was below `7e-53` at 70
decimal digits.

## Direct source example

For a first lattice index `n0` and count `r`:

```bash
/tmp/x0602-direct 10000000 7695823789624 64 > /tmp/source-direct.json
python analyze.py /tmp/source-direct.json \
  --dimension 64 --center-offset 31 --dps 80
```

The direct source program uses an in-memory sieve and is intended for moderate
cutoffs. The `n0` field in its JSON is the first represented index.

## Wide moment-corrected example

For center index `8795227188177`, offsets `[-8192,8192]`, grid `65536`, and
Taylor order 10:

```bash
/tmp/x0602-nufft \
  100000000 8795227188177 8192 65536 10 \
  /tmp/source-wide.json

python analyze.py /tmp/source-wide.json \
  --dimension 128 --center-offset -7748 --dps 75 \
  --output /tmp/packet.json
```

M-0602 controls the analytic Taylor truncation caused by gridding. It does not
control FFT roundoff, phase-library error, or matrix conditioning.

## Retained results

At `c=10^8`, the wide source contained 5,761,455 primes and 5,762,859 prime
powers. The best scalar in the scanned offset window was approximately

```text
0.5504453445339111
```

whereas the best retained 128-carrier packet was approximately

```text
0.24237605690882058
```

at carrier height approximately

```text
2,999,999,997,911.0944741132.
```

The result is positive. No candidate ID is created.

## Why the result matters

The packet lowered the scalar margin by more than one half. This confirms that
Issue #26 is not merely another scalar scan: its natural finite-dimensional
closure can create deep coherent notches while preserving nonnegativity and
compact Fourier support.

Simple contiguous dimension growth then plateaued. The next search should
change carrier geometry—continuous offsets, prolate/windowed envelopes,
separated clusters, or explicit local zero notches—rather than only increase
matrix size.

## Numerical environment

```text
CPython 3.13.5
mpmath 1.3.0
NumPy 2.3.5
GCC 14.2.0
Linux x86_64, glibc 2.41
```

## Proof boundary

- Ordinary numerical negatives would be candidates only, not proofs.
- This run found no negative.
- The gridding Taylor bound is analytic, but floating and FFT errors are not
  enclosed.
- The matrix normalization still requires the independent Q-0004 review.
- A future strict negative must be reevaluated entry by entry with balls and
  passed through the X-0001 exact dyadic Rayleigh checker.
