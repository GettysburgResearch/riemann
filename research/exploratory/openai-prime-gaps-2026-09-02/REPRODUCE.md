# Reproduction and audit commands

This packet preserves the upstream repositories as exact submodules. The commands below are review instructions, not claims that this import pass reran every computation.

## Source-lock verification

```bash
git submodule update --init --recursive

git -C research/exploratory/imports/openai-prime-gaps-2026-09-02/PrimeGaps186 \
  rev-parse HEAD
# 61340d0b74163003b32756bb16e91d9209a5e330

git -C research/exploratory/imports/openai-prime-gaps-2026-09-02/LongGapsBetweenPrimes \
  rev-parse HEAD
# 8f5fa88c88b4750028c05b66b081d56a92418054
```

## Long-gap package

The package matches Riemann's current Lean 4.33 generation.

```bash
cd research/exploratory/imports/openai-prime-gaps-2026-09-02/LongGapsBetweenPrimes
lake update
lake build
```

The audit should inspect at least:

```lean
#print axioms LongGapsBetweenPrimes.short_translates
#print axioms LongGapsBetweenPrimes.long_prime_gaps
#print axioms LongGapsBetweenPrimes.long_gap_theorem
```

Do not count the intentional `sorry` in `Challenge.lean` as part of the completed implementation without first checking which targets the lake package compiles. The completed source to audit is `LongGapsBetweenPrimes.lean`; `Challenge.lean` is the comparator reference statement.

## Bounded-gap package

This package pins Lean 4.34.0-rc2 and should be built in its own directory rather than by Riemann's Lean 4.33 project.

```bash
cd research/exploratory/imports/openai-prime-gaps-2026-09-02/PrimeGaps186
lake update
lake build
```

Inspect the theorem boundary explicitly:

```lean
#print axioms PrimeGap186.dhl_40_2
#print axioms PrimeGap186.infinite_two_prime_translates_admissibleTuple
#print axioms PrimeGap186.primeGapLiminf_le_186
```

The expected nonstandard assumptions are:

```text
PrimeGap186.kloosterman3_bound
PrimeGap186.kloosterman2_correlation_bound
PrimeGap186.physical_integral_bounds
```

Run the upstream numerical checker only in the environment documented by the pinned README:

```bash
python prime_gap_186_certificate.py
```

A passing Python run corroborates the physical inequalities but does not by itself remove `PrimeGap186.physical_integral_bounds` from `#print axioms`.

## Minimum exact-SHA review record

For each package, retain:

```text
reviewer identity
date
OS and architecture
Lean version
mathlib lock
command transcript
stdout/stderr hashes
#print axioms output
source-tree hash
semantic statement comparison
```

Promotion is blocked until the transcript is attached to an exact source commit and a second reviewer checks the theorem statement rather than merely the build result.
