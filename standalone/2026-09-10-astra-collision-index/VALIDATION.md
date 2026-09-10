# Executed validation and remaining boundaries

**Research status:** proposed, not independently mathematically reviewed. No actual
theta boundary was evaluated or certified. No new Newman-constant bound or RH
proof is claimed. The manuscript's global source obligation remains open.

## Exact accepting computation

The complete standard-library reconstruction produces 22 polynomial boundary
certificates with 879 paid dyadic segments in total. The source polynomials,
backward/forward heat signs, all four edges, exact rational endpoints, full
second-derivative bounds, chord distances and polygon windings are reconstructed.
The retained receipt includes a hash of each complete regenerated witness; the
witness is not just a sampled phase plot. There is no truncated zero sum.

Local degrees in the tested Hermite orders 2--12 are -1,-1,-2,-2,-3,-3,-4,-4,
-5,-5,-6. Four translated controls retain their indices. Two separate collision
times give -2. The even off-axis pair has -2, and each half-box has -1. A zero-
time double excluded from the positive-time box gives 0. The forward-heat sign
control gives +1 and is explicitly not assigned the backward-heat theorem.
These finite cases do NOT prove the all-multiplicity theorem by induction.

There are also 32 exact Hermite derivative/PDE identities in the producer and
85 formal theta-jet controls through order six, comparing the differential
recurrence with a separately expanded formal exponential series. Those use
rational formal q,u,t, not actual pi*n^2*exp(4u) evaluations. The Gaussian-mixture
collision timing is checked rationally; its transform and persistence proof are
analytic, not a computed double-exponential epsilon threshold.

Both commands complete with identical stdout:

```sh
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
```

Canonical semantic receipt SHA256:

```
012f2d56b5d433c16c877fa9626b4ca67660219a8b76badb9f5b1f545a852165
```

The file's manifest hash is a separate byte identity. Producer `--write` mode
regenerates but does not authenticate a package or accept a mathematical claim.

## Adversarial tests

All 13 methods pass in each interpreter mode, with zero skips and identical
JSON summaries. Each mode executes one pristine complete CLI reconstruction,
eleven changed-receipt CLI refusals and two changed-package refusals (an extra
file and a real Linux symlink). In-process controls also reject incomplete,
reversed, overlapped and empty side covers; unpaid whole-segment curvature;
injected endpoint/error fields; and a common zero on the boundary. Orientation,
nonzero scalar multiplication, t=0 exclusion, symmetry/additivity, primitive
algebra and strict rational/JSON typing are checked separately.

```sh
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The first test run exposed a NO-OP mutation in the test itself: reversing a
one-segment side did not change it. The fixture now selects a side with more
than one segment and asserts that guard. Both final suites then pass. The
accepting engine and mathematical outputs did not require a repair.

No `assert` implements acceptance. Test-framework assertions are confined to
`test_check.py`. Strict receipts reject duplicate keys, floating values,
nonfinite values and Boolean/integer substitution. Complete declared file
inventory and SHA256 authentication are checked before accepting reconstruction.
A maliciously rewritten-and-resealed whole implementation is not authenticated
against a historical commit by the local manifest alone; use the published Git
identity as the external source pin.

## Delivery and nonexecuted work

The eight-file packet is add-only. Clean archive extraction and a separate
minimal-Git patch roundtrip replay both accepting modes and preserve an unrelated
sentinel. These are packet delivery checks, NOT a full Riemann checkout/build.
The final remote file/packet identities are checked against the locally tested
files and reported in the PR and accompanying delivery receipt.

The original analytic source formula, both tail bounds and derivative interface
are provided on paper, but a directed theta endpoint/quadrature backend is NOT
implemented in this executable. No actual low-root collar, global source phase,
new zero, large-height asymptotic constant, original research campaign, fresh
Lean proof, native Windows execution or remote CI success is claimed. An optional
python-flint installation attempt failed DNS; that package is unused and no
external numerical dependency is needed by these final programs.

The literature reading is selected and explicitly listed in SOURCES.json; it is
not a comprehensive originality search, external proof audit or independent
referee vote. New repository branches are moving sources; their descriptions
supplied orientation, not mathematical acceptance. Main, the existing integration
candidate and all predecessor research/accepted-source files remain untouched.
