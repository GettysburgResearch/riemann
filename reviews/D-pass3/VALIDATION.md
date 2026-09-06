# Executed validation and trust boundary — D pass 3

Environment: Python 3.13.5, SymPy 1.14.0. The checker is a fresh file for this
review. It imports no original research producer. All acceptance comparisons
use integers, fractions, exact symbolic algebra, or explicitly outward-rounded
rational intervals. Python optimization does not disable checks: failures
raise explicit exceptions, not assert statements.

## Executed mathematical controls

`checks.py` contains 34 named bounded controls with 6,999 fixtures. The majority
(5,187) are finite disjoint-sector/gcd pairs, not separate theorems. The same
complete output was generated in ordinary and optimized Python and compared
byte for byte. Additional controls include:

- Gaussian Fourier differential/zero identities and finite multiplicity-aware
  cardinal interpolation; no actual zeta zeros are numerically supplied.
- Every carry row through 128, the centered spectral and forcing moments,
  fixed inverse masses, and exact positive-divisor logarithmic recursion.
- All 60 annular-kernel coefficients reconstructed from their primitive finite
  formulas and compared to the frozen Q(sqrt2) certificate, plus 22 endpoint
  comparisons and the corrected sector counterexample. The latter's actual
  Q4 numerator weights are independently enclosed away from zero, with
  opposite signs.
- Finite Goldbach/zero-mode identities, the absolute Hilbert-kernel logarithmic
  loss and the signed averaging remainder algebra. These do not execute a
  continuous Hilbert transform or prove its infinite operator bound.
- Bounded weighted-Jordan tests, boundary-contact algebra, rational terminal
  Green margins, the exact raw/net pole-cancellation model and kernel product
  identity. No numerical small-scale threshold is inferred from these tests.
- Literal P61 X=184 divisor-convolution regeneration with a 90-bit dyadic
  outward interval class. Square roots use integer square roots; logarithms
  use 48 positive atanh terms after reduction to [1,2], with explicit tail.
  Every subsequent operation rounds outward. It proves 40F-M<-18 and
  42F-M>3. It does not evaluate zeta, use MPFR, or rerun the large campaign.
- All 128 sparse 5:3 coefficient controls, 585 per-atom four-band identities
  in exact formal prime-log coordinates, prime ownership, native score
  duality, affine-cell compression and Cauchy storage/telescoping controls.

The source coefficient list is transcribed from the inspected exact blob and
compared with an independent reconstruction. `SOURCES.tsv` records source
SHA/path/blob identities; neither this checker nor the package validator
refetches or authenticates the upstream files by network access.

## Commands run

From this directory:

```sh
python -B checks.py --output checks.normal.json
python -B -O checks.py --output checks.optimized.json
cmp checks.normal.json checks.optimized.json
python -B checks.py --compare checks.normal.json
python -B -O checks.py --compare checks.optimized.json
python -B rejections.py --output /tmp/d3-rejections-normal.json
python -B -O rejections.py --output /tmp/d3-rejections-optimized.json
cmp /tmp/d3-rejections-normal.json /tmp/d3-rejections-optimized.json
python -B validate.py --prior
python -B -O validate.py --prior
```

The two rejection runs send eight deliberately changed result records through
the actual comparator used by `checks.py --compare`. Each also launches four
corrupted-package validation subprocesses. Every mutation is rejected in both
Python modes; the rejection records are byte-identical. These are tests of
record and package integrity, not adversarial refutations of an infinite
analytic theorem.

The manifest covers all fifteen non-manifest files and the validator requires
exactly sixteen files. It also checks table IDs, primary source resolution,
coverage of the 139-row canonical denominator, and declared result counts.
With `--prior`, the published Git-blob identities of the two old manifests are
fixed anchors and every old file hash/inventory is reauthenticated. **The old
mathematical checker and old rejection suites were not rerun in this pass.**
Their previously published results remain unchanged historical records.

## Authoring corrections before the validated run

An initial checker draft raised KeyError while recognizing primes: it indexed
a composite's factor dictionary by the composite. It was changed to exact
comparison with `{p:1}`. A second draft used a needlessly loose mixed-endpoint
bound for the terminal Green margin, giving 0.129972 rather than the requested
0.13. Using the proved monotonicity in log 2 gives the valid rational lower
bound 0.130972. This was a checker-bound repair, not a failure of positivity.
No failed draft is represented by the retained successful outputs.

Later exact controls strengthened the cardinal transform check, added the
literal C4 sparse dictionary, and certified the actual active Q4 pair weights.
The final outputs correspond to the final checked file, not to an earlier
smaller fixture count.

## Deliberately not executed

No production zeta or zero census, million-endpoint P61 loop, complete P61
large-divisor certificate, high-ordinate Pick primitive, large Robin stream,
Lean/Comparator/Nanoda build, or remote CI was run. SymPy verifies bounded
symbolic identities; it does not formalize the analytic arguments in
`PROOFS_AND_REPAIRS.md`. Exact finite checks are supporting evidence only.

The add-only publication is verified separately by an exact subtree/file
identity comparison, non-force branch update and fresh PR-head read. Its
receipt is outside the committed directory to avoid self-reference. The
combined handoff ZIP is validated after extraction. Those publication checks
are recorded in the outer receipt rather than inferred from local success.
