# Validation scope and reproducibility

This is a proposed research packet, not independent mathematical acceptance.
The Python results are finite certificates; they do not prove Lee--Yang,
Li--Radziwill, the compactness arguments, or an all-order realization.

## Primitive computation

`check.py --check result.json` authenticates the exact regular-file inventory,
then recomputes the full theta moment enclosures through degree sixteen. It
integrates 84 degree-120 cells for theta indices 1 through 4, adds all four
infinite time tails, and the entire omitted theta-index tail. The dyadic scale
is 2^320. Scalar transcendentals use convergent rational series with complete
remainders; square roots use integer inequalities. No floating arithmetic,
zeta evaluation, zero oracle, or supplied moment receipt enters acceptance.

The actual seven-variable moment root is certified using an exact rational
inverse (49 multiplication identities), full interval residuals and row-sum
bounds over the complete radius-10^-14 box. The sixteenth moment is explicitly
not matched. A complete 272-spin enumeration is neither needed nor performed:
component independence plus exact four-state dimer sums give the cumulants.

The 57 other bounded algebra controls comprise 32 exact dimer even-moment
identities at four rational Gibbs ratios, one triple-angle identity and 24
independent block cumulant checks against direct small spin enumeration.
These counts are not infinite theorem counts or extra theta realizations.

## Accepting commands

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py --part 1
python -I -S -B test_rejections.py --part 2
python -I -S -B -O test_rejections.py --part 1
python -I -S -B -O test_rejections.py --part 2
```

The intended complete output is result.json, with `rh_proved` false. `--emit`
is a producer-only mode and bypasses packet authentication. Accepting runs use
canonical JSON comparison to distinguish boolean/integer aliases and reject
float tokens and duplicate keys. No Python assert implements acceptance.

The two rejection partitions each copy the entire packet and execute a pristine
CLI reconstruction, followed by four and five actual refusals respectively: a resealed false RH claim,
wrong sixteenth-moment endpoints, boolean alias, duplicate JSON, changed theta
coefficient in the producer, negative-coupling parameter, unsealed proof edit,
extra file and symlinked proof. The changed theta coefficient is caught by
source/moment reconstruction, not merely a hash. The negative-coupling case
checks the specified input contract. Hash/inventory refusals have their narrower
integrity role. Linux symlink behavior is tested, not Windows behavior.

## Exploration and dependency boundary

Ordinary mpmath/SciPy calculations selected the rational parameter centers. A
numerical path in the dimer probability led to q=2/3, followed by high-precision
refinement. None of those calculations is accepted evidence. The final box is
verified independently of the exploratory path, but the interval backend is
adapted from #847; it is not an independent transcendental implementation.

The first unmatched sixteenth-moment search did not produce a certified model.
Its numerical failure is not a theorem of impossibility. There is no all-order
induction, global parameter-continuation radius, or claimed moment-16 solution.

The #854 mathematical description and selected proof sections were inspected.
Its old code and source receipt were not imported or rerun. The local #847
checker was authenticated by length, SHA256 and Git blob before adaptation.
The full theta moments here are fresh primitive reconstructions. Literature
reading and failed PDF page-image retrievals are recorded in SOURCES.json.

No complete Riemann checkout, parent campaign, actual higher-order Xi sign,
remote CI, formal build, or independent referee acceptance is claimed. Archive
and Git publication receipts are kept outside the mathematical packet so their
creation does not change its sealed source inventory.

An initial combined rejection orchestration timed out before a complete receipt
was written. A later combined optimized command completed partition one but
timed out during the next pristine run. Neither interrupted orchestration is
counted as a complete suite; all four final partition receipts were obtained,
with optimized partition two rerun alone. The altered-density
primitive was then isolated and rejected by the whole-box invariance check.
Final acceptance uses the separate complete partitions listed above.

## Final retained execution

Both full accepting mathematical runs completed with byte-identical JSON.
Normal partitions 1 and 2 and optimized partitions 1 and 2 each completed;
together they give two pristine reconstructions and nine intended refusals per
mode. The density mutation is rejected at whole-box invariance. The numerical
receipt is unchanged by subsequent validation-prose and manifest updates.
The external delivery receipt records archive, patch and Git read-back checks.
