# Exact-SHA review checklist

Use one completed copy per upstream repository. A build log without semantic review is insufficient.

## A. Shared provenance

- [ ] Gitlink equals the commit in `SOURCE_LOCK.json`.
- [ ] Upstream tree and all submodule paths are clean.
- [ ] Commit date, author, signature state, default branch, and license recorded.
- [ ] `lean-toolchain`, `lakefile.toml`, and `lake-manifest.json` hashed.
- [ ] Clean checkout and build transcript deposited.
- [ ] Completed module does not import `Challenge`.
- [ ] Comparator configuration and permitted axioms inspected.
- [ ] `#print axioms` output deposited for every exported theorem.
- [ ] Compiled environment searched for `sorryAx` and unexpected unsafe declarations.
- [ ] Two reviewers sign the statement-equivalence report.

## B. `PrimeGaps186`

### Theorem boundary

- [ ] `dhl_40_2` depends on exactly K3, K2C, PHY, and ordinary Lean/mathlib axioms.
- [ ] `infinite_two_prime_translates_admissibleTuple` introduces no additional project axiom.
- [ ] `primeGapLiminf_le_186` introduces no additional project axiom.
- [ ] The completed theorem matches the intended `EReal` liminf statement.

### Kloosterman inputs

- [ ] Additive character and complex norm conventions match the source theorem.
- [ ] Rank-three normalization by `1/p` is correct.
- [ ] Nonzero-parameter hypothesis is sufficient.
- [ ] Correlation exclusions `t=0,-1` are correct in every characteristic.
- [ ] Exceptional parameter configurations for `A,B` are classified.
- [ ] Constants `3` and `8` survive every normalization conversion.
- [ ] Small-prime cases are proved separately where necessary.

### Physical certificate

- [ ] Exactly 104 outer clauses are present and checked.
- [ ] Exactly 45 inner clauses are present and checked.
- [ ] Exactly 3 scalar caps are present and checked.
- [ ] No row is skipped, duplicated, or reordered without an index proof.
- [ ] Every fixed coefficient/table hash matches the Python input.
- [ ] All interval operations are outward rounded.
- [ ] The custom FLINT correction is reproduced and independently reviewed.
- [ ] A second implementation reproduces all margins.
- [ ] Lean checks a proof object or verified rational enclosure for every clause.
- [ ] `physical_integral_bounds` disappears from endpoint axioms.

### Tuple and final transfer

- [ ] Tuple cardinality is exactly 40.
- [ ] All shifts are distinct natural numbers in `[0,186]`.
- [ ] Minimum and maximum certify diameter 186.
- [ ] Admissibility is proved for all primes, with the `p>40` shortcut justified.
- [ ] Infinitely many two-prime translates are obtained from the exact DHL statement.
- [ ] A consecutive pair of primes of gap at most 186 is extracted.
- [ ] The infinite-occurrence statement implies the declared liminf inequality.

## C. `LongGapsBetweenPrimes`

### Statement

- [ ] `LongGapTheorem`, `long_prime_gaps`, `long_gap_theorem`, and `Challenge.long_prime_gaps` are compared explicitly.
- [ ] Strict versus non-strict inequalities are documented.
- [ ] The upper endpoint prime is below or at `X` exactly as claimed.
- [ ] The final gap scale contains the correct powers of `log_2`, `log_3`, and `log_4`.
- [ ] The existential constant is strictly positive.

### Random sieve and short translates

- [ ] Probability space and all random variables are measurable.
- [ ] Collision classes are exhaustive and disjoint.
- [ ] First, second, and third moment expansions have correct diagonal factors.
- [ ] Tail bounds have the required strictness to give positive success probability.
- [ ] Sparse-set cardinality and interval hypotheses match at each application.
- [ ] The chosen translate lies in the advertised range.

### Residue cover

- [ ] Small, medium, and large prime bands are disjoint and cover the intended primes.
- [ ] Every uncovered integer receives a residue/divisor witness.
- [ ] All selected moduli divide the final primorial.
- [ ] CRT hypotheses are present and residue conventions agree.
- [ ] Interval endpoints include every intended integer.
- [ ] Divisor witnesses prove compositeness rather than possible equality with the integer.

### Prime extraction and asymptotics

- [ ] The translated interval is a full block of consecutive composites.
- [ ] The primes immediately before and after the block exist.
- [ ] They are consecutive and have gap at least the block length.
- [ ] The upper prime satisfies the location bound.
- [ ] `coverScale` to `gapScale` conversion is replayed independently.
- [ ] Constants `8`, `16`, and `128` are traced to named lemmas.
- [ ] Every logarithm denominator is eventually positive before division.

## D. Promotion decision

### Long gaps

- [ ] Independent exact-SHA review complete.
- [ ] Extracted module builds under Riemann's stable toolchain.
- [ ] No statement broadening during refactor.
- [ ] Eligible for `research/integrated/` and possibly `formal/Experimental/`.

### Bounded gaps

- [ ] Physical premise kernelized.
- [ ] K3 and K2C either proved or retained visibly as theorem inputs.
- [ ] Conditional status preserved in every index and title.
- [ ] Unconditional promotion blocked until all project inputs are discharged.

## E. RH firewall

- [ ] No arrow from either gap endpoint to RH is registered.
- [ ] Any RH-to-gap consequence cites a reviewed explicit formula and prime-power correction.
- [ ] Finite numerical evidence remains classified as finite.
- [ ] Finite-field RH analogies are not stated as classical RH implications.
